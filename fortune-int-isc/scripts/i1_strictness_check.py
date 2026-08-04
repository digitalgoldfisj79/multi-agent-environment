#!/usr/bin/env python3
"""Exact finite witnesses that INT-LTQ is strictly weaker than full variance."""

from fractions import Fraction


def lower_tail_sq(z: Fraction, base: Fraction) -> Fraction:
    return max(Fraction(0), base - z) ** 2


def run() -> None:
    rows = []
    for n, base in ((3, 5), (10, 100), (100, 1000)):
        z = [Fraction(2 * base) for _ in range(n)]
        b = [Fraction(base) for _ in range(n)]
        tail = sum(lower_tail_sq(x, y) for x, y in zip(z, b))
        variance = sum((x - y) ** 2 for x, y in zip(z, b))
        first = sum(x - y for x, y in zip(z, b))
        assert tail == 0
        assert variance == n * base * base
        assert first == n * base
        rows.append((n, base, tail, variance, first))

    for n, base, tail, variance, first in rows:
        print(
            f"n={n} base={base} lower_tail={tail} "
            f"variance={variance} signed_first_moment={first}"
        )
    print("FORTUNE_INT_ISC_I1_STRICTNESS_PASS")


if __name__ == "__main__":
    run()
