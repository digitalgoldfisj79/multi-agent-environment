#!/usr/bin/env python3
"""Verify the post-primorial factor range begins beyond the s=2 sieve boundary."""

from __future__ import annotations

import math


def main() -> None:
    for x in (10**2, 10**3, 10**4, 10**5, 10**6):
        eta = 0.75
        h = eta * x * x
        z = x
        d_ideal = h
        d_bv = math.sqrt(h)
        s_ideal = math.log(d_ideal) / math.log(z)
        s_bv = math.log(d_bv) / math.log(z)

        assert z > math.sqrt(h)
        assert s_ideal < 2.0
        assert s_bv < 1.0
        print(
            f"X={x} H={h:.8g} z_min={z} "
            f"s_ideal={s_ideal:.10f} s_BV={s_bv:.10f}"
        )

    print("FORTUNE_INT_PSLT_B4_SIEVE_BOUNDARY_PASS")


if __name__ == "__main__":
    main()
