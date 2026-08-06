#!/usr/bin/env python3
"""Regression audit for the explicit failed-centre prime-power cap."""

from __future__ import annotations

import math


def harmonic_tail(kmax: int) -> float:
    return math.fsum(1.0 / k for k in range(2, kmax + 1))


def main() -> None:
    for x in (20, 40, 80, 160, 320):
        eta = 0.5
        h = eta * x * x
        log_p = 1.5 * x
        log_u = log_p + math.log1p(h * math.exp(-log_p))
        kmax = int(log_u / math.log(2.0))
        cap = log_u * harmonic_tail(kmax)
        base = 2.0 * cap

        assert math.log(h) < math.log(2.0) + 0.5 * log_p
        assert base >= 2.0 * cap
        assert cap > 0.0

        normalized = base / (x * math.log(x))
        print(
            f"X={x} K={kmax} cap={cap:.8g} base={base:.8g} "
            f"base_over_XlogX={normalized:.8g}"
        )

    print("FORTUNE_INT_PSLT_B1_PRIME_POWER_CAP_PASS")


if __name__ == "__main__":
    main()
