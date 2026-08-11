#!/usr/bin/env python3
"""Oriented-coefficient reduction for the normalized cubic defect geometry.

For an ordered cubic root cycle, replace the three roots by the coefficients
of the monic cubic and the oriented Vandermonde eta.  This gives a 17-variable,
17-equation system equivalent to the 13-variable root-cycle system on the
separable locus, but the known q=11 point is rational over F_11 and no
extension-field coefficients are needed.

The script verifies the canonical point and exact Jacobian rank, and can emit
local Singular or expanded msolve inputs.  It does not infer dimension from
the rank calculation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import sympy as sp


BLOCKS = "ABCD"  # A=P, B=S, C=P', D=S'
POINT_11 = {
    "A2": 0, "A1": 8, "A0": 5, "eA": 7,
    "B2": 10, "B1": 2, "B0": 1, "eB": 10,
    "C2": 10, "C1": 1, "C0": 9, "eC": 4,
    "D2": 0, "D1": 9, "D0": 9, "eD": 1,
    "rho": 8,
}


def modular_rational(value: sp.Expr, characteristic: int) -> int:
    rational = sp.Rational(value)
    numerator = int(rational.p) % characteristic
    denominator = int(rational.q) % characteristic
    return numerator * pow(denominator, -1, characteristic) % characteristic


def polynomial_string(polynomial: sp.Poly, variable_names: list[str], characteristic: int) -> str:
    terms: list[str] = []
    for monomial, coefficient in polynomial.terms():
        scalar = modular_rational(coefficient, characteristic)
        factors: list[str] = []
        if scalar != 1 or not any(monomial):
            factors.append(str(scalar))
        for name, exponent in zip(variable_names, monomial, strict=True):
            if exponent == 1:
                factors.append(name)
            elif exponent > 1:
                factors.append(f"{name}^{exponent}")
        terms.append("*".join(factors) if factors else "0")
    return "+".join(terms) if terms else "0"


def rank_mod(matrix: list[list[int]], characteristic: int) -> tuple[int, list[int]]:
    work = [[entry % characteristic for entry in row] for row in matrix]
    row = 0
    pivots: list[int] = []
    for column in range(len(work[0])):
        pivot = next((index for index in range(row, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[pivot], work[row] = work[row], work[pivot]
        inverse = pow(work[row][column], -1, characteristic)
        work[row] = [entry * inverse % characteristic for entry in work[row]]
        for index in range(len(work)):
            if index != row and work[index][column]:
                factor = work[index][column]
                work[index] = [
                    (work[index][j] - factor * work[row][j]) % characteristic
                    for j in range(len(work[index]))
                ]
        pivots.append(column)
        row += 1
        if row == len(work):
            break
    return row, pivots


def build_system() -> tuple[list[sp.Symbol], list[sp.Expr], dict[str, sp.Symbol]]:
    names: list[str] = []
    for block in BLOCKS:
        names.extend([f"{block}2", f"{block}1", f"{block}0", f"e{block}"])
    names.append("rho")
    variables = list(sp.symbols(" ".join(names)))
    symbol = dict(zip(names, variables, strict=True))
    t = sp.Symbol("t")

    def cubic(block: str) -> sp.Expr:
        return t**3 + symbol[f"{block}2"] * t**2 + symbol[f"{block}1"] * t + symbol[f"{block}0"]

    def discriminant(block: str) -> sp.Expr:
        a = symbol[f"{block}2"]
        b = symbol[f"{block}1"]
        c = symbol[f"{block}0"]
        return a*a*b*b - 4*b**3 - 4*a**3*c - 27*c**2 + 18*a*b*c

    def cycle_numerator(block: str) -> sp.Expr:
        a = symbol[f"{block}2"]
        b = symbol[f"{block}1"]
        c = symbol[f"{block}0"]
        eta = symbol[f"e{block}"]
        return (
            (a*a - 3*b) * t**2
            + (a**3 - sp.Rational(7, 2)*a*b + sp.Rational(9, 2)*c - sp.Rational(3, 2)*eta) * t
            + sp.Rational(1, 2)*a*a*b + sp.Rational(3, 2)*a*c - 2*b*b - sp.Rational(1, 2)*a*eta
        )

    equations: list[sp.Expr] = [
        symbol[f"e{block}"]**2 - discriminant(block) for block in BLOCKS
    ]
    rho = symbol["rho"]
    incidence = [
        (cycle_numerator("A") * cubic("B") - symbol["eA"] * cubic("C"), "A"),
        (cycle_numerator("C") * cubic("D") + symbol["eC"] * cubic("A"), "C"),
        (cycle_numerator("B") * cubic("A") + rho * symbol["eB"] * cubic("D"), "B"),
        (cycle_numerator("D") * cubic("C") - rho * symbol["eD"] * cubic("B"), "D"),
    ]
    for expression, modulus_block in incidence:
        remainder = sp.Poly(expression, t).rem(sp.Poly(cubic(modulus_block), t))
        equations.extend(sp.expand(remainder.coeff_monomial(t**degree)) for degree in range(3))
    equations.append(symbol["A2"])
    assert len(variables) == len(equations) == 17
    return variables, equations, symbol


def verify(characteristic: int = 11) -> dict[str, object]:
    variables, equations, symbol = build_system()
    substitution = {symbol[name]: value for name, value in POINT_11.items()}
    evaluations = [modular_rational(equation.subs(substitution), characteristic) for equation in equations]
    assert not any(evaluations), evaluations
    jacobian = [
        [
            modular_rational(sp.diff(equation, variable).subs(substitution), characteristic)
            for variable in variables
        ]
        for equation in equations
    ]
    rank, pivots = rank_mod(jacobian, characteristic)
    assert rank == 16
    return {
        "status": "MACHINE-VERIFIED IDENTITY AND LOCAL TANGENT",
        "characteristic": characteristic,
        "variables": len(variables),
        "equations": len(equations),
        "maximum_total_degree": max(sp.total_degree(equation) for equation in equations),
        "canonical_point_satisfies_system": True,
        "jacobian_rank": rank,
        "zariski_tangent_dimension": len(variables) - rank,
        "pivot_columns": pivots,
        "boundary": "Rank 16 does not decide whether the local dimension is zero or one; a local standard-basis certificate is required.",
    }


def emit_local_singular(path: Path, characteristic: int = 11) -> None:
    variables, equations, _ = build_system()
    original_names = [str(variable) for variable in variables]
    local_names = [f"x{index}" for index in range(len(variables))]
    local_symbols = list(sp.symbols(" ".join(local_names)))
    shift = {
        variable: local_symbols[index] + POINT_11[original_names[index]]
        for index, variable in enumerate(variables)
    }
    lines = [f"ring R={characteristic},({','.join(local_names)}),ds;", "option(redSB);"]
    for index, equation in enumerate(equations):
        shifted = sp.Poly(sp.expand(equation.subs(shift)), *local_symbols, modulus=characteristic)
        lines.append(f"poly e{index}={polynomial_string(shifted, local_names, characteristic)};")
    lines.extend(
        [
            "ideal I=" + ",".join(f"e{index}" for index in range(len(equations))) + ";",
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
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def emit_msolve(path: Path, characteristic: int = 11) -> None:
    variables, equations, _ = build_system()
    names = [str(variable) for variable in variables]
    expanded = [
        polynomial_string(sp.Poly(sp.expand(equation), *variables, modulus=characteristic), names, characteristic)
        for equation in equations
    ]
    path.write_text(",".join(names) + f"\n{characteristic}\n" + ",\n".join(expanded) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--local-singular", type=Path)
    parser.add_argument("--msolve", type=Path)
    parser.add_argument("--characteristic", type=int, default=11)
    arguments = parser.parse_args()
    if arguments.verify or (arguments.local_singular is None and arguments.msolve is None):
        print(json.dumps(verify(arguments.characteristic), indent=2, sort_keys=True))
    if arguments.local_singular is not None:
        emit_local_singular(arguments.local_singular, arguments.characteristic)
        print(f"wrote {arguments.local_singular}")
    if arguments.msolve is not None:
        emit_msolve(arguments.msolve, arguments.characteristic)
        print(f"wrote {arguments.msolve}")


if __name__ == "__main__":
    main()
