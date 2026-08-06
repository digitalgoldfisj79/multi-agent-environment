#!/usr/bin/env python3
"""Verify the unconditional large-sieve exponent obstruction."""
from __future__ import annotations

from fractions import Fraction


def relative_exponent(rho: Fraction, delta: Fraction) -> Fraction:
    # Q=X^(1+delta), H=X^2.  Even with collision-free selected residues,
    # the large-sieve variance Q^2 H gives error/main exponent below.
    return Fraction(1, 2) + Fraction(3, 2) * delta - rho / 2


def main() -> None:
    for delta in (Fraction(1, 100), Fraction(1, 12), Fraction(1, 6), Fraction(1, 3)):
        best = min(relative_exponent(Fraction(r, 300), delta) for r in range(1, 301))
        assert best == Fraction(3, 2) * delta
        assert best > 0
        print(f"delta={float(delta):.9g} best_relative_exponent={float(best):.9g}")

    # No post-terminal delta>0 is admissible for any row exponent rho<=1.
    for d in range(1, 100):
        delta = Fraction(d, 300)
        assert all(relative_exponent(Fraction(r, 300), delta) > 0 for r in range(1, 301))

    print("FORTUNE_INT_SCME_M4_LARGE_SIEVE_OBSTRUCTION_PASS")


if __name__ == "__main__":
    main()
