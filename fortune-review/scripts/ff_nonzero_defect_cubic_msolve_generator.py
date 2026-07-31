#!/usr/bin/env python3
"""Generate a canonical expanded msolve input for the saturated cubic ideal.

msolve requires each monomial to occur exactly once.  The compact factored
root equations therefore cannot be passed directly: this generator expands,
combines and reduces every coefficient modulo the requested characteristic
before writing the input file.
"""
from __future__ import annotations

import argparse
from itertools import combinations
from pathlib import Path

import sympy as sp


def build(characteristic: int) -> tuple[str, dict[str, int]]:
    names = [f"{prefix}{index}" for prefix in "abcd" for index in range(3)]
    names += ["r"] + [f"u{index}" for index in range(11)]
    symbols = sp.symbols(" ".join(names))
    variable = dict(zip(names, symbols, strict=True))

    def roots(prefix: str) -> list[sp.Symbol]:
        return [variable[f"{prefix}{index}"] for index in range(3)]

    a, b, c, d = (roots(prefix) for prefix in "abcd")
    rho = variable["r"]
    equations: list[sp.Expr] = []
    for index in range(3):
        nxt = (index + 1) % 3
        equations.extend(
            [
                (a[nxt] - a[index]) * sp.prod(a[index] - root for root in b)
                - sp.prod(a[index] - root for root in c),
                (c[nxt] - c[index]) * sp.prod(c[index] - root for root in d)
                + sp.prod(c[index] - root for root in a),
                (b[nxt] - b[index]) * sp.prod(b[index] - root for root in a)
                + rho * sp.prod(b[index] - root for root in d),
                (d[nxt] - d[index]) * sp.prod(d[index] - root for root in c)
                - rho * sp.prod(d[index] - root for root in b),
            ]
        )
    equations.append(sum(a))

    factors: list[sp.Expr] = []
    for tuple_roots in (a, b, c, d):
        factors.append(
            sp.prod(tuple_roots[left] - tuple_roots[right] for left, right in combinations(range(3), 2))
        )
    tuples = (a, b, c, d)
    for left, right in combinations(range(4), 2):
        factors.append(sp.prod(x - y for x in tuples[left] for y in tuples[right]))
    factors.append(rho * (rho - 1))
    equations.extend(variable[f"u{index}"] * factor - 1 for index, factor in enumerate(factors))

    def canonical(expression: sp.Expr) -> str:
        polynomial = sp.Poly(sp.expand(expression), *symbols, modulus=characteristic)
        terms: list[str] = []
        for monomial, coefficient in polynomial.terms():
            scalar = int(coefficient) % characteristic
            factors_out: list[str] = []
            if scalar != 1 or not any(monomial):
                factors_out.append(str(scalar))
            for name, exponent in zip(names, monomial, strict=True):
                if exponent == 1:
                    factors_out.append(name)
                elif exponent > 1:
                    factors_out.append(f"{name}^{exponent}")
            terms.append("*".join(factors_out) if factors_out else "0")
        return "+".join(terms)

    text = ",".join(names) + f"\n{characteristic}\n"
    text += ",\n".join(canonical(equation) for equation in equations) + "\n"
    return text, {
        "variables": len(names),
        "equations": len(equations),
        "bytes": len(text.encode("utf-8")),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    text, metadata = build(arguments.characteristic)
    arguments.output.write_text(text, encoding="utf-8")
    print(metadata)


if __name__ == "__main__":
    main()
