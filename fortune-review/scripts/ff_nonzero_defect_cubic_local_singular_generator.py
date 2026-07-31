#!/usr/bin/env python3
"""Generate a local Singular standard-basis computation at the canonical q=11 point.

The coefficient field is F_11(z), z^3+8z+5=0.  The 13 root/rho variables
are translated so the known normalized nonzero-defect point is the origin,
and the local degree ordering `ds` computes the dimension of its local ring.
This directly distinguishes an actual positive-dimensional component from an
isolated singular point with a large tangent space.
"""
from __future__ import annotations
import argparse
from pathlib import Path

BASE = [
    (0, 1, 0), (10, 9, 6), (1, 1, 5),
    (1, 3, 7), (9, 7, 3), (2, 1, 1),
    (3, 10, 6), (4, 10, 0), (5, 2, 5),
    (2, 10, 10), (3, 8, 4), (6, 4, 8),
    (8, 0, 0),
]


def coefficient(value: tuple[int, int, int]) -> str:
    terms: list[str] = []
    for degree, entry in enumerate(value):
        entry %= 11
        if not entry:
            continue
        if degree == 0:
            terms.append(str(entry))
        elif degree == 1:
            terms.append(f"{entry}*z")
        else:
            terms.append(f"{entry}*z2")
    return "+".join(terms) or "0"


def product(items: list[str]) -> str:
    return "*".join(f"({item})" for item in items)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    variables = [f"x{i}" for i in range(13)]
    shifted = [f"({variables[i]}+{coefficient(BASE[i])})" for i in range(13)]
    a, b, c, d, rho = shifted[:3], shifted[3:6], shifted[6:9], shifted[9:12], shifted[12]

    equations: list[str] = []
    for index in range(3):
        nxt = (index + 1) % 3
        equations.append(
            f"({a[nxt]}-{a[index]})*"
            f"{product([f'{a[index]}-{root}' for root in b])}-"
            f"{product([f'{a[index]}-{root}' for root in c])}"
        )
        equations.append(
            f"({c[nxt]}-{c[index]})*"
            f"{product([f'{c[index]}-{root}' for root in d])}+"
            f"{product([f'{c[index]}-{root}' for root in a])}"
        )
        equations.append(
            f"({b[nxt]}-{b[index]})*"
            f"{product([f'{b[index]}-{root}' for root in a])}+{rho}*"
            f"{product([f'{b[index]}-{root}' for root in d])}"
        )
        equations.append(
            f"({d[nxt]}-{d[index]})*"
            f"{product([f'{d[index]}-{root}' for root in c])}-{rho}*"
            f"{product([f'{d[index]}-{root}' for root in b])}"
        )
    equations.append(f"{a[0]}+{a[1]}+{a[2]}")

    lines = [
        f"ring R=(11,z),({','.join(variables)}),ds;",
        "minpoly=z^3+8*z+5;",
        "poly z2=z^2;",
    ]
    for index, equation in enumerate(equations):
        lines.append(f"poly e{index}={equation};")
    lines.extend(
        [
            "ideal I=" + ",".join(f"e{i}" for i in range(13)) + ";",
            "int started=timer;",
            "ideal G=std(I);",
            'print("STATUS=COMPUTED");',
            'print("DIM="+string(dim(G)));',
            'print("GB_SIZE="+string(size(G)));',
            'print("ELAPSED="+string(timer-started));',
            'if(dim(G)==0){print("VDIM="+string(vdim(G)));}',
            'print("STANDARD_BASIS_BEGIN");',
            "G;",
            'print("STANDARD_BASIS_END");',
        ]
    )
    arguments.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"generated {arguments.output} with 13 variables and 13 equations")


if __name__ == "__main__":
    main()
