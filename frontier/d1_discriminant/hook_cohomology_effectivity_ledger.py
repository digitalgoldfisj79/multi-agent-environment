#!/usr/bin/env python3
"""Exact hook-cohomology ledger for the fixed-q p-cycle character.

Uses only integer arithmetic and the proved local inertia data:
  I_infinity = C_p semidirect C_((p-1)/2), lower jump (p-3)/2.

For V_i = wedge^i Std, computes:
  rank(V_i), dim V_i^{C_p}, Swan_infinity(V_i), dim H_c^1(U,V_i),
and the even/odd totals.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def ledger_for_prime(p: int) -> dict:
    if p < 5 or p % 2 == 0:
        raise ValueError("p must be an odd integer at least 5")

    rows = []
    for i in range(p):
        rank = comb(p - 1, i)
        cp_invariants_numerator = rank + (p - 1) * ((-1) ** i)
        if cp_invariants_numerator % p:
            raise ArithmeticError("C_p invariant formula was not integral")
        cp_invariants = cp_invariants_numerator // p

        swan = Fraction(p - 3, p - 1) * (rank - cp_invariants)
        if swan.denominator != 1:
            raise ArithmeticError("Swan conductor was not integral")
        swan_int = swan.numerator

        h2 = 1 if i == 0 else 0
        h1 = rank + swan_int + h2
        rows.append(
            {
                "i": i,
                "parity": "even" if i % 2 == 0 else "odd",
                "rank": rank,
                "cp_invariants": cp_invariants,
                "swan_infinity": swan_int,
                "h_c_2": h2,
                "h_c_1": h1,
            }
        )

    total_rank = sum(row["rank"] for row in rows)
    total_swan = sum(row["swan_infinity"] for row in rows)
    total_h1 = sum(row["h_c_1"] for row in rows)
    even_h1 = sum(row["h_c_1"] for row in rows if row["i"] % 2 == 0)
    odd_h1 = sum(row["h_c_1"] for row in rows if row["i"] % 2 == 1)
    virtual_h1 = even_h1 - odd_h1

    expected_total_swan = (p - 3) * (2 ** (p - 1) - 1) // p
    expected_total_h1 = ((2 * p - 3) * 2 ** (p - 1) + 3) // p

    checks = {
        "total_rank": total_rank == 2 ** (p - 1),
        "total_swan": total_swan == expected_total_swan,
        "total_h1": total_h1 == expected_total_h1,
        "virtual_h1": virtual_h1 == 4 - p,
        "parity_reconstruction": (
            even_h1 == (total_h1 + 4 - p) // 2
            and odd_h1 == (total_h1 - 4 + p) // 2
        ),
    }
    if not all(checks.values()):
        raise ArithmeticError(f"ledger check failed for p={p}: {checks}")

    return {
        "p": p,
        "checks": checks,
        "total_rank": total_rank,
        "total_swan": total_swan,
        "total_h_c_1": total_h1,
        "even_h_c_1": even_h1,
        "odd_h_c_1": odd_h1,
        "virtual_h_c_1": virtual_h1,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--primes",
        nargs="+",
        type=int,
        default=[5, 7, 11, 13, 17, 19, 23, 29, 31],
    )
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument(
        "--omit-rows",
        action="store_true",
        help="omit per-hook rows from JSON output",
    )
    args = parser.parse_args()

    results = [ledger_for_prime(p) for p in args.primes]
    if args.omit_rows:
        for result in results:
            result.pop("rows", None)

    payload = {
        "status": "PASS",
        "method": "Exact integer arithmetic from the proved inertia and GOS formulas.",
        "results": results,
    }
    rendered = json.dumps(payload, indent=2)
    print(rendered)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
