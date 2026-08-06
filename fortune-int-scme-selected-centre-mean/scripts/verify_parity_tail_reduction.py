#!/usr/bin/env python3
"""Exact arithmetic regression for the band-plus-tail implication."""
from __future__ import annotations

from fractions import Fraction


def main() -> None:
    panels = [
        # (band mass, tail, proved band lower bound, allowed negative fraction)
        (Fraction(40), Fraction(-25), Fraction(39), Fraction(3, 4)),
        (Fraction(120), Fraction(-70), Fraction(115), Fraction(2, 3)),
        (Fraction(75), Fraction(-30), Fraction(72), Fraction(1, 2)),
    ]
    for band, tail, band_lower, alpha in panels:
        total = band + tail
        assert band >= band_lower
        assert tail >= -alpha * band
        assert total >= (1 - alpha) * band_lower
        print(
            f"band={band} tail={tail} total={total} "
            f"certified_lower={(1-alpha)*band_lower}"
        )

    # Adversarial control: divisor-band positivity alone does not imply prime mass.
    band = Fraction(100)
    tail = -band
    total = band + tail
    assert band > 0 and total == 0

    print("FORTUNE_INT_SCME_M6_PARITY_TAIL_PASS")


if __name__ == "__main__":
    main()
