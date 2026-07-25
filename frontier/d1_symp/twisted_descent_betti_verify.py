#!/usr/bin/env python3
"""Verify the primitive Betti formula for the smooth (2,3) model.

For X_p, a smooth complete intersection of type (2,3) in P^(p-3),
with m=p-5 even, the theorem is

    dim H^m_prim(X_p) = (2^(p-1)-1)/3.

The calculation uses exact rational power-series arithmetic for

    c(TX) = (1+H)^(p-2) / ((1+2H)(1+3H)).

No third-party packages are required.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
from typing import Iterable


def odd_primes(limit: int) -> Iterable[int]:
    for n in range(5, limit + 1, 2):
        if all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            yield n


def inverse_linear_series(c: int, degree: int) -> list[int]:
    """Coefficients of 1/(1+cH) through H^degree."""
    return [(-c) ** j for j in range(degree + 1)]


def multiply_truncated(
    left: list[Fraction],
    right: list[Fraction],
    degree: int,
) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                out[i + j] += a * b
    return out


def primitive_betti_from_chern(p: int) -> int:
    m = p - 5
    numerator = [Fraction(comb(p - 2, j)) for j in range(m + 1)]
    inv2 = [Fraction(value) for value in inverse_linear_series(2, m)]
    inv3 = [Fraction(value) for value in inverse_linear_series(3, m)]

    series = multiply_truncated(numerator, inv2, m)
    series = multiply_truncated(series, inv3, m)

    euler = 6 * series[m]
    assert euler.denominator == 1, (p, euler)

    primitive = int(euler) - (m + 1)
    return primitive


def main() -> None:
    checked = list(odd_primes(199))
    for p in checked:
        actual = primitive_betti_from_chern(p)
        expected = (2 ** (p - 1) - 1) // 3
        assert actual == expected, (p, actual, expected)

    print(
        "PASS: primitive Betti formula verified by exact Chern-series "
        f"calculation for {len(checked)} odd primes through {checked[-1]}."
    )


if __name__ == "__main__":
    main()
