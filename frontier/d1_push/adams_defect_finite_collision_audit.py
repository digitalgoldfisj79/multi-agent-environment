#!/usr/bin/env python3
"""Exact audit of finite collision multiplicities for the descended cover.

For p>=5, m=(p-1)/2,
  H_c(Y)=Y^m+aY+c,
  R_a(c,Y)=Y H_c(Y)^2,
  y0=-c/(3a), B_a(c)=R_a(c,y0).

At B_a(c)=0 the theorem predicts the geometric multiplicity partitions
  c=0: 3,2^(m-1),
  c!=0: 1,4,2^(m-2).
No such partition contains a p-cycle.

Requires python-flint. All arithmetic and factorisation are exact.
"""
from __future__ import annotations

import argparse
import json
from math import isqrt
from flint import nmod_poly


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(x for x in range(2, p) if chi(x, p) == -1)


def value(poly: nmod_poly, x: int, p: int) -> int:
    return int(poly(x)) % p


def geometric_multiplicity_partition(poly: nmod_poly) -> list[int]:
    _, factors = poly.factor()
    out: list[int] = []
    for factor, exponent in factors:
        out.extend([int(exponent)] * int(factor.degree()))
    return sorted(out, reverse=True)


def audit_case(p: int, a: int) -> dict:
    m = (p - 1) // 2
    inv_3a = pow((3 * a) % p, p - 2, p)
    rows = []
    failures = []

    for c in range(p):
        y0 = (-c * inv_3a) % p
        H = nmod_poly([c, a] + [0] * (m - 2) + [1], p)
        R = nmod_poly([0, 1], p) * H * H
        B = (y0 * value(H, y0, p) ** 2) % p
        if B != 0:
            continue

        partition = geometric_multiplicity_partition(R)
        if c == 0:
            expected = sorted([3] + [2] * (m - 1), reverse=True)
            derivative_checks = {
                "H_y0": value(H, y0, p),
                "Hprime_y0": value(H.derivative(), y0, p),
            }
        else:
            expected = sorted([4, 1] + [2] * (m - 2), reverse=True)
            hp = H.derivative()
            hpp = hp.derivative()
            derivative_checks = {
                "H_y0": value(H, y0, p),
                "Hprime_y0": value(hp, y0, p),
                "Hsecond_y0": value(hpp, y0, p),
            }

        row = {
            "c": c,
            "y0": y0,
            "partition": partition,
            "expected": expected,
            "derivative_checks": derivative_checks,
            "contains_p_cycle": p in partition,
            "pass": partition == expected and p not in partition,
        }
        if c != 0:
            row["pass"] = (
                row["pass"]
                and derivative_checks["H_y0"] == 0
                and derivative_checks["Hprime_y0"] == 0
                and derivative_checks["Hsecond_y0"] != 0
            )
        rows.append(row)
        if not row["pass"]:
            failures.append(row)

    return {
        "p": p,
        "a": a,
        "square_class": chi(a, p),
        "collision_count_Fp": len(rows),
        "pass": not failures,
        "failures": failures,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=199)
    args = parser.parse_args()

    results = []
    for p in primes_upto(args.max_prime):
        if p < 5:
            continue
        for a in (1, least_nonsquare(p)):
            result = audit_case(p, a)
            results.append(result)
            print(json.dumps({k: v for k, v in result.items() if k != "rows"}), flush=True)

    output = {
        "status": "PASS" if all(r["pass"] for r in results) else "FAIL",
        "scope": "exact F_p collision audit; symbolic theorem is over the algebraic closure",
        "max_prime": args.max_prime,
        "cases": len(results),
        "results": results,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
