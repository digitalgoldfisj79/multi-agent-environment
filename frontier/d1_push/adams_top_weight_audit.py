#!/usr/bin/env python3
"""Exact symmetric-group audit of the Adams hook expansion and top multiplicity.

For each conjugacy type of S_p, compute
  det(1+t sigma | Std_p)
and its hook coefficients. Verify
  sum_i (-1)^i chi_(wedge^i Std)(sigma)
    = p if sigma is a p-cycle, else 0.
Then average over conjugacy classes to verify that the trivial and sign
multiplicities in W are both exactly one.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from math import isqrt


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield []
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield [first] + rest


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def divide_by_one_plus_t(poly: list[int]) -> list[int]:
    """Exact quotient by 1+t, assuming divisibility."""
    n = len(poly) - 1
    quotient = [0] * n
    quotient[0] = poly[0]
    for i in range(1, n):
        quotient[i] = poly[i] - quotient[i - 1]
    assert poly[n] == quotient[n - 1]
    return quotient


def hook_characters(cycle_type: list[int]) -> list[int]:
    # det(1+t P_sigma)=prod_cycles (1-(-t)^length).
    poly = [1]
    for length in cycle_type:
        factor = [0] * (length + 1)
        factor[0] = 1
        factor[length] = -((-1) ** length)
        poly = poly_mul(poly, factor)
    # P=1 direct_sum Std.
    return divide_by_one_plus_t(poly)


def class_size(cycle_type: list[int]) -> int:
    n = sum(cycle_type)
    counts = Counter(cycle_type)
    denominator = 1
    for length, multiplicity in counts.items():
        denominator *= (length**multiplicity) * math.factorial(multiplicity)
    return math.factorial(n) // denominator


def sign(cycle_type: list[int]) -> int:
    return (-1) ** (sum(cycle_type) - len(cycle_type))


def audit_prime(p: int) -> dict:
    failures = []
    trivial_numerator = 0
    sign_numerator = 0
    type_count = 0

    for cycle_type in partitions(p):
        type_count += 1
        hooks = hook_characters(cycle_type)
        assert len(hooks) == p
        adams = sum(((-1) ** i) * value for i, value in enumerate(hooks))
        expected = p if cycle_type == [p] else 0
        if adams != expected:
            failures.append(
                {
                    "cycle_type": cycle_type,
                    "hooks": hooks,
                    "adams": adams,
                    "expected": expected,
                }
            )
            break
        size = class_size(cycle_type)
        trivial_numerator += size * adams
        sign_numerator += size * adams * sign(cycle_type)

    factorial = math.factorial(p)
    return {
        "p": p,
        "conjugacy_types": type_count,
        "trivial_multiplicity": trivial_numerator // factorial,
        "sign_multiplicity": sign_numerator // factorial,
        "divisibility_pass": trivial_numerator % factorial == 0
        and sign_numerator % factorial == 0,
        "pass": not failures
        and trivial_numerator == factorial
        and sign_numerator == factorial,
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

    print(
        json.dumps(
            {
                "status": "PASS" if all(row["pass"] for row in rows) else "FAIL",
                "max_prime": args.max_prime,
                "prime_cases": len(rows),
                "total_conjugacy_types": sum(row["conjugacy_types"] for row in rows),
                "rows": rows,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
