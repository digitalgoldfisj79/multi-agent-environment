#!/usr/bin/env python3
"""Audit Theorem CWFR.1 from CARTIER_WEIGHT_FILTRATION_REDUCTION.md.

For each prime p and deterministic parameter triples (a,c,d), construct the
(p-1)x(p-1) coefficient matrix

    A[n,e] = [X^e](aX^3+cX+d)^n,

n=1..p-1, e in {0,..,p-1}\{p-3}, and verify

    det A = -c^(p(p-3)/2)d^(p-3)((p-3)ad^2-c^3) mod p.

All arithmetic is exact in F_p.
"""
from __future__ import annotations

import argparse
import json
from math import isqrt


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
    return [i for i, value in enumerate(sieve) if value]


def determinant_mod(matrix: list[list[int]], p: int) -> int:
    a = [[entry % p for entry in row] for row in matrix]
    n = len(a)
    det = 1
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pivot_value = a[col][col] % p
        det = det * pivot_value % p
        inverse = pow(pivot_value, p - 2, p)
        for row in range(col + 1, n):
            factor = a[row][col] * inverse % p
            if not factor:
                continue
            for j in range(col, n):
                a[row][j] = (a[row][j] - factor * a[col][j]) % p
    return det % p


def coefficient_matrix(p: int, a: int, c: int, d: int) -> list[list[int]]:
    exponents = [e for e in range(p) if e != p - 3]
    coefficients = [0] * p
    coefficients[0] = 1
    rows: list[list[int]] = []
    for _n in range(1, p):
        new = [0] * p
        for e, value in enumerate(coefficients):
            if not value:
                continue
            new[e] = (new[e] + d * value) % p
            if e + 1 < p:
                new[e + 1] = (new[e + 1] + c * value) % p
            if e + 3 < p:
                new[e + 3] = (new[e + 3] + a * value) % p
        coefficients = new
        rows.append([coefficients[e] for e in exponents])
    return rows


def predicted(p: int, a: int, c: int, d: int) -> int:
    exponent_c = p * (p - 3) // 2
    exponent_d = p - 3
    core = ((p - 3) * a * d * d - pow(c, 3, p)) % p
    return (-pow(c, exponent_c, p) * pow(d, exponent_d, p) * core) % p


def audit_prime(p: int) -> dict[str, object]:
    raw_triples = [(1, 1, 1), (2, 3, 4), (p - 1, 2, 5), (3, p - 2, 1)]
    rows = []
    for a, c, d in raw_triples:
        a %= p
        c %= p
        d %= p
        observed = determinant_mod(coefficient_matrix(p, a, c, d), p)
        expected = predicted(p, a, c, d)
        rows.append({
            "a": a,
            "c": c,
            "d": d,
            "observed": observed,
            "expected": expected,
            "pass": observed == expected,
        })
    return {"p": p, "pass": all(bool(row["pass"]) for row in rows), "tests": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=199)
    parser.add_argument("--output")
    args = parser.parse_args()

    results = [audit_prime(p) for p in primes_upto(args.max_prime) if p >= 5]
    output = {
        "status": "PASS" if all(bool(row["pass"]) for row in results) else "FAIL",
        "method": "Exact iterative coefficient construction and Gaussian elimination over F_p; no floating point.",
        "prime_count": len(results),
        "comparison_count": 4 * len(results),
        "max_prime": max((int(row["p"]) for row in results), default=None),
        "all_checks_pass": all(bool(row["pass"]) for row in results),
        "results": results,
    }
    text = json.dumps(output, indent=2) + "\n"
    print(text, end="")
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)


if __name__ == "__main__":
    main()
