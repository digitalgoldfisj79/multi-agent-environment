#!/usr/bin/env python3
"""Audit CRH.2 on every conjugacy type of S_p.

No group enumeration is required.  The exterior-character polynomial of the
permutation representation at cycle type (l_1,...,l_r) is
    product_j (1-(-u)^l_j),
and the standard representation is obtained by dividing by 1+u.
"""
from __future__ import annotations

import argparse
import json
from math import factorial, isqrt

import sympy as sp


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def exterior_value(cycle_type: tuple[int, ...]) -> int:
    u = sp.symbols("u")
    poly = sp.Integer(1)
    for length in cycle_type:
        poly *= 1 - (-u) ** length
    quotient, remainder = sp.div(sp.Poly(sp.expand(poly), u), sp.Poly(1 + u, u))
    assert remainder.is_zero
    return int(quotient.eval(-1))


def induced_difference_value(p: int, cycle_type: tuple[int, ...]) -> int:
    if cycle_type == (1,) * p:
        return 0
    if cycle_type == (p,):
        # Ind_C^G 1 has value p-1 and Ind_C^G psi has value -1.
        return p
    return 0


def audit_prime(p: int) -> dict:
    failures = []
    values = []
    for part in partitions(p):
        ext = exterior_value(part)
        ind = induced_difference_value(p, part)
        values.append({"cycle_type": part, "exterior": ext, "induced_difference": ind})
        if ext != ind:
            failures.append(values[-1])
    return {
        "p": p,
        "conjugacy_types": len(values),
        "virtual_dimension": exterior_value((1,) * p),
        "p_cycle_value": exterior_value((p,)),
        "induced_dimension_each": factorial(p - 1),
        "pass": not failures,
        "failures": failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=47)
    args = parser.parse_args()
    rows = []
    for p in primes_upto(args.max_prime):
        if p < 5:
            continue
        row = audit_prime(p)
        rows.append(row)
        print(json.dumps(row), flush=True)
    print(json.dumps({"status": "PASS" if all(r["pass"] for r in rows) else "FAIL", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
