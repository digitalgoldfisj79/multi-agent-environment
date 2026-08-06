#!/usr/bin/env python3
"""Verify the selected-residue BDH exponent region and its 1/3 frontier."""
from __future__ import annotations

from fractions import Fraction


def admissible(rho: Fraction, delta: Fraction) -> bool:
    return 2 * delta < rho < 1 - delta


def main() -> None:
    rho = Fraction(2, 3)
    for denominator in (12, 30, 60, 300):
        eps = Fraction(1, denominator)
        delta = Fraction(1, 3) - eps
        assert admissible(rho, delta)
        diag_exponent = delta - rho / 2
        collision_exponent = (rho + delta - 1) / 2
        assert diag_exponent < 0
        assert collision_exponent < 0
        print(
            f"rho={float(rho):.9g} delta={float(delta):.9g} "
            f"diag={float(diag_exponent):.9g} collision={float(collision_exponent):.9g}"
        )

    # Exact feasibility: 2 delta < rho < 1-delta implies 3 delta < 1.
    for numerator in range(1, 100):
        delta = Fraction(numerator, 300)
        feasible = any(
            admissible(Fraction(r, 300), delta) for r in range(1, 300)
        )
        assert feasible == (delta < Fraction(1, 3))

    print("FORTUNE_INT_SCME_M4_BDH_EXPONENT_PASS")


if __name__ == "__main__":
    main()
