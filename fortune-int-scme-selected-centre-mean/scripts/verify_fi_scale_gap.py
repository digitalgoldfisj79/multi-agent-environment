#!/usr/bin/env python3
"""Numerical log-scale audit of direct Friedlander–Iwaniec eligibility."""
from __future__ import annotations

import math


def main() -> None:
    for x in (50, 100, 250, 500, 1000, 5000):
        # log P_j ~ X. Compare logarithms to avoid constructing the primorial.
        log_required_d = 2 * x / 3
        available_d = x  # H^(1/2) for H=X^2/2, up to constants.
        log_available_d = math.log(available_d)
        gap = log_required_d - log_available_d
        assert gap > 0
        print(
            f"X={x} log_D_required={log_required_d:.8g} "
            f"log_D_available={log_available_d:.8g} log_gap={gap:.8g}"
        )
    print("FORTUNE_INT_SCME_M2_FI_SCALE_GAP_PASS")


if __name__ == "__main__":
    main()
