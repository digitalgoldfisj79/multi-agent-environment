#!/usr/bin/env python3
"""Exact character audit for the hook sign-pairing theorem.

For every conjugacy type of S_p, compute

    det(1+t sigma | Std_p)

from the cycle type and verify the hook identity

    chi_(p-1-i)(sigma)=sgn(sigma) chi_i(sigma).

For the central hook i=(p-1)/2, verify exact vanishing on odd conjugacy
types. Only Python's standard library is used.
"""
from __future__ import annotations

import json
from pathlib import Path

PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def multiply(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def divide_by_one_plus_t(poly: list[int]) -> list[int]:
    quotient = [0] * (len(poly) - 1)
    quotient[0] = poly[0]
    for k in range(1, len(quotient)):
        quotient[k] = poly[k] - quotient[k - 1]
    assert quotient[-1] == poly[-1]
    return quotient


def standard_exterior_characters(cycle_type: tuple[int, ...]) -> list[int]:
    # On the permutation representation, an l-cycle contributes
    # det(1+t sigma)=1-(-t)^l.
    poly = [1]
    for length in cycle_type:
        factor = [0] * (length + 1)
        factor[0] = 1
        factor[length] = -((-1) ** length)
        poly = multiply(poly, factor)

    # Remove the global trivial eigenline.
    return divide_by_one_plus_t(poly)


def main() -> None:
    rows = []
    for p in PRIMES:
        type_count = 0
        odd_type_count = 0
        maximum_character = 0

        for cycle_type in partitions(p):
            characters = standard_exterior_characters(cycle_type)
            assert len(characters) == p
            sign = -1 if (p - len(cycle_type)) & 1 else 1

            for i in range(p):
                assert characters[p - 1 - i] == sign * characters[i]
                maximum_character = max(maximum_character, abs(characters[i]))

            if sign == -1:
                odd_type_count += 1
                assert characters[(p - 1) // 2] == 0

            type_count += 1

        rows.append(
            {
                "prime": p,
                "conjugacy_type_count": type_count,
                "odd_conjugacy_type_count": odd_type_count,
                "maximum_absolute_hook_character": maximum_character,
                "hook_sign_pairing_verified": True,
                "central_hook_odd_vanishing_verified": True,
            }
        )

    result = {
        "status": "PASS",
        "statement": (
            "For every conjugacy type of S_p and every hook, "
            "chi_(p-1-i)=sgn*chi_i. The central-hook character vanishes "
            "on every odd conjugacy type."
        ),
        "range": "all prime p from 5 through 47",
        "rows": rows,
    }

    output = Path(__file__).with_name("hook_sign_pairing_audit_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
