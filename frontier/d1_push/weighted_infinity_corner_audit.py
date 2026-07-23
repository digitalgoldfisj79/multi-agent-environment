#!/usr/bin/env python3
"""Exact audit for the weighted infinity corner theorem.

Requires python-flint and sympy.
"""
from __future__ import annotations

import argparse
import json
from math import isqrt

import sympy as sp
from flint import nmod_poly


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def irreducible(f: nmod_poly) -> bool:
    _, fac = f.factor()
    return len(fac) == 1 and fac[0][1] == 1 and fac[0][0].degree() == f.degree()


def symbolic_for_prime(p: int) -> dict:
    m = (p - 1) // 2
    r, Z, C, E, a, X, D = sp.symbols("r Z C E a X D")
    # After multiplying the original equation by r^(2p), the scaled RHS is:
    scaled = sp.expand(Z * (Z**m + C + a * r ** (p - 3) * Z) ** 2)
    exceptional = sp.expand(Z * (Z**m + C) ** 2)
    factor_left = sp.expand(X**2 * (X ** (2 * m) + C) ** 2 - D**2)
    factor_right = sp.expand((X**p + C * X - D) * (X**p + C * X + D))
    return {
        "p": p,
        "m": m,
        "exceptional_specialization_pass": sp.expand(scaled.subs(r, 0) - exceptional) == 0,
        "square_factorization_pass": sp.expand(factor_left - factor_right) == 0,
    }


def finite_case(p: int) -> dict:
    x = nmod_poly([0, 1], p)
    mismatches = []
    irreducible_pairs = []
    for C in range(p):
        for D in range(p):
            f = x**p + C * x + D
            got = irreducible(f)
            expected = C == p - 1 and D != 0
            if got:
                irreducible_pairs.append((C, D))
            if got != expected:
                mismatches.append({"C": C, "D": D, "irreducible": got, "expected": expected})
                if len(mismatches) >= 10:
                    break
        if mismatches:
            break
    projected_trace = 2 * p * ((p - 1) // 2)
    return {
        "p": p,
        "irreducible_count": len(irreducible_pairs),
        "expected_count": p - 1,
        "projected_adams_trace": projected_trace,
        "expected_projected_trace": p * (p - 1),
        "pass": not mismatches
        and len(irreducible_pairs) == p - 1
        and projected_trace == p * (p - 1),
        "mismatches": mismatches,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=101)
    args = parser.parse_args()
    rows = []
    for p in primes_upto(args.max_prime):
        if p < 5:
            continue
        sym = symbolic_for_prime(p)
        fin = finite_case(p)
        row = {"symbolic": sym, "finite": fin, "pass": all(sym[k] for k in ("exceptional_specialization_pass", "square_factorization_pass")) and fin["pass"]}
        rows.append(row)
        print(json.dumps({"p": p, "pass": row["pass"], "irreducible_count": fin["irreducible_count"]}), flush=True)
    print(json.dumps({"status": "PASS" if all(r["pass"] for r in rows) else "FAIL", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
