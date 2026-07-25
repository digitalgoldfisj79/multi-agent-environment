#!/usr/bin/env python3
"""Exact verifier for FIXED_INTERIOR_QLINE_CELL_NO_GO_20260725.md.

Requires python-flint.
"""

from __future__ import annotations

from math import isqrt

from flint import nmod_poly


CANDIDATES = (-5, -4, -3, -2, -1, 1, 3, 4, 5, 6, 7)
EXPECTED_FIRST_FAILURE = {
    -2: 5,
    3: 5,
    -5: 11,
    -3: 11,
    -1: 11,
    6: 11,
    -4: 17,
    4: 17,
    7: 17,
    1: 23,
    5: 53,
}


def admitted_primes(limit: int):
    for p in range(5, limit):
        if p % 6 != 5:
            continue
        if all(p % divisor for divisor in range(2, isqrt(p) + 1)):
            yield p


def irreducible_count(p: int, q_integer: int) -> int | None:
    q = q_integer % p
    if q in (0, 2):
        return None

    count = 0
    for t in range(p):
        coefficients = [0] * (p + 1)
        coefficients[0] = (-(q - 2) * t) % p
        coefficients[1] = -3 % p
        coefficients[3] = 1
        coefficients[p] = q
        polynomial = nmod_poly(coefficients, p)
        _, factors = polynomial.factor()
        irreducible = (
            len(factors) == 1
            and factors[0][1] == 1
            and factors[0][0].degree() == p
        )
        count += int(irreducible)
    return count


def main() -> None:
    first_failure: dict[int, int] = {}
    for p in admitted_primes(60):
        for q_integer in CANDIDATES:
            if q_integer in first_failure:
                continue
            count = irreducible_count(p, q_integer)
            if count == 0:
                first_failure[q_integer] = p

    assert first_failure == EXPECTED_FIRST_FAILURE, first_failure
    print("FIXED_Q_CELL_NO_GO_VERIFY: PASS")
    for q_integer in CANDIDATES:
        print(
            f"q={q_integer}: first zero cell at "
            f"p={first_failure[q_integer]}"
        )


if __name__ == "__main__":
    main()
