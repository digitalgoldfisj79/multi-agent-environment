#!/usr/bin/env python3
"""Generate the saturated affine-normalized cubic nonzero-defect root ideal.

The root variables are a_i,b_i,c_i,d_i (i mod 3), with lambda normalized
to 1, rho=r, and the translation gauge a0+a1+a2=0.  The open locus is
implemented exactly by Rabinowitsch variables for the four tuple
discriminants, the six pairwise tuple resultants, and r(r-1).

The generated Singular ideal therefore has 24 variables and 24 equations.
It is equivalent to the required localization, while avoiding expansion of a
single 66-factor Vandermonde polynomial.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def product(items: list[str]) -> str:
    return "*".join(f"({item})" for item in items) if items else "1"


def difference(x: str, y: str) -> str:
    return f"{x}-{y}"


def tuple_resultant(left: str, right: str) -> str:
    return product(
        [difference(f"{left}{i}", f"{right}{j}") for i in range(3) for j in range(3)]
    )


def discriminant_factor(prefix: str) -> str:
    return product(
        [difference(f"{prefix}{i}", f"{prefix}{j}") for i in range(3) for j in range(i + 1, 3)]
    )


def build(characteristic: int) -> tuple[str, dict[str, object]]:
    roots = [f"{prefix}{i}" for prefix in "abcd" for i in range(3)]
    localization_variables = [f"u{i}" for i in range(11)]
    variables = roots + ["r"] + localization_variables

    root_equations: list[str] = []
    for i in range(3):
        nxt = (i + 1) % 3
        root_equations.append(
            f"({difference(f'a{nxt}', f'a{i}')})*"
            f"{product([difference(f'a{i}', f'b{j}') for j in range(3)])}-"
            f"{product([difference(f'a{i}', f'c{j}') for j in range(3)])}"
        )
        root_equations.append(
            f"({difference(f'c{nxt}', f'c{i}')})*"
            f"{product([difference(f'c{i}', f'd{j}') for j in range(3)])}+"
            f"{product([difference(f'c{i}', f'a{j}') for j in range(3)])}"
        )
        root_equations.append(
            f"({difference(f'b{nxt}', f'b{i}')})*"
            f"{product([difference(f'b{i}', f'a{j}') for j in range(3)])}+r*"
            f"{product([difference(f'b{i}', f'd{j}') for j in range(3)])}"
        )
        root_equations.append(
            f"({difference(f'd{nxt}', f'd{i}')})*"
            f"{product([difference(f'd{i}', f'c{j}') for j in range(3)])}-r*"
            f"{product([difference(f'd{i}', f'b{j}') for j in range(3)])}"
        )

    gauge = "a0+a1+a2"
    localization_factors = [discriminant_factor(prefix) for prefix in "abcd"]
    for index, left in enumerate("abcd"):
        for right in "abcd"[index + 1 :]:
            localization_factors.append(tuple_resultant(left, right))
    localization_factors.append("r*(r-1)")
    assert len(localization_factors) == 11

    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
    ]
    all_base_equations = root_equations + [gauge]
    for index, equation in enumerate(all_base_equations):
        lines.append(f"poly e{index}={equation};")
    for index, factor in enumerate(localization_factors):
        lines.append(f"poly s{index}={factor};")
        lines.append(f"poly l{index}=u{index}*s{index}-1;")

    generators = [f"e{i}" for i in range(len(all_base_equations))] + [
        f"l{i}" for i in range(len(localization_factors))
    ]
    lines.extend(
        [
            f"ideal I={','.join(generators)};",
            "int started=timer;",
            "ideal G=slimgb(I);",
            "int elapsed=timer-started;",
            'print("STATUS=COMPUTED");',
            f'print("CHAR={characteristic}");',
            'print("DIM="+string(dim(G)));',
            'print("GB_SIZE="+string(size(G)));',
            'print("ELAPSED="+string(elapsed));',
            'if (dim(G)==0) { print("VDIM="+string(vdim(G))); }',
            'print("LEAD_IDEAL_BEGIN");',
            "lead(G);",
            'print("LEAD_IDEAL_END");',
        ]
    )

    manifest: dict[str, object] = {
        "characteristic": characteristic,
        "variables": variables,
        "variable_count": len(variables),
        "root_equations": root_equations,
        "gauge": gauge,
        "localization_factors": localization_factors,
        "equation_count": len(generators),
        "status": "GENERATED EXACT IDEAL; DIMENSION AND DEGREE NOT PREJUDGED",
    }
    return "\n".join(lines) + "\n", manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path)
    arguments = parser.parse_args()

    singular, manifest = build(arguments.characteristic)
    arguments.output.write_text(singular, encoding="utf-8")
    if arguments.manifest:
        arguments.manifest.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    print(json.dumps({"characteristic": arguments.characteristic, "variables": 24, "equations": 24}))


if __name__ == "__main__":
    main()
