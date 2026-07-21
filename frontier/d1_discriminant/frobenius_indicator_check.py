#!/usr/bin/env python3
"""Verify J_a(c,d)=3a on irreducibles and 0 otherwise.

This imports the independent matrix and Rabin routines from
frobenius_determinant_check.py and strengthens the earlier nonvanishing check
to the exact value theorem.
"""

from __future__ import annotations

from frobenius_determinant_check import (
    is_irreducible,
    least_nonsquare,
    reduced_determinant,
)


def verify() -> None:
    for p in (5, 7, 11, 13):
        for a in (1, least_nonsquare(p)):
            values = set()
            count = 0
            determinant_sum = 0
            for c in range(p):
                for d in range(p):
                    value = reduced_determinant(p, a, c, d)
                    expected = 3 * a % p if is_irreducible(p, a, c, d) else 0
                    assert value == expected, (p, a, c, d, value, expected)
                    values.add(value)
                    count += int(expected != 0)
                    determinant_sum = (determinant_sum + value) % p

            assert values == {0, 3 * a % p}
            assert determinant_sum == 3 * a * count % p
            print(
                f"PASS p={p}, a={a}: values={sorted(values)}, "
                f"count={count}, sum={determinant_sum}"
            )

    print("ALL EXACT FROBENIUS INDICATOR CHECKS PASSED")


if __name__ == "__main__":
    verify()
