#!/usr/bin/env python3
"""Numerical scale audit for the occupancy programme."""

from __future__ import annotations

import math

eta = 0.5
for x in (100, 1_000, 10_000, 100_000, 1_000_000, 100_000_000):
    n = x / math.log(x)
    h = eta * x * x
    m = h / math.log(h)
    gamma = math.log(x)
    tau = 2.0 * math.log(n) / gamma
    q = 1.0 - math.exp(-tau)
    k = q * m
    assert 0.0 < q < 1.0
    assert k > math.log(n)
    print(
        f"X={x} N~{n:.6g} M~{m:.6g} gamma~{gamma:.6g} "
        f"tau~{tau:.6g} q~{q:.6g} K~{k:.6g} "
        f"K/logN~{k / math.log(n):.6g}"
    )

print("FORTUNE_INT_AOD_O3_SCALE_PASS")
