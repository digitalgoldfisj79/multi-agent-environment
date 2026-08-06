#!/usr/bin/env python3
"""Finite checks for the adaptive occupancy detector and strict softening."""

import math

# A failed row contributes exactly one and forces the sum to be at least one.
for N in (2, 5, 20):
    gamma_min = 10.0
    tau = 2.0 * math.log(N) / gamma_min
    failed = [0] + [100] * (N - 1)
    value = sum(math.exp(-tau * z) for z in failed)
    assert value >= 1.0

# The soft detector can pass even with a positive row far below gamma_min.
for N in (2, 5, 20, 100):
    gamma_min = 10.0
    tau = 2.0 * math.log(N) / gamma_min
    panel = [1] + [1000] * (N - 1)
    value = sum(math.exp(-tau * z) for z in panel)
    assert value < 1.0, (N, value)
    assert panel[0] < gamma_min

# If every row is at least (1-eps) gamma_min, the chosen tau gives N^{-1+2eps}.
for N in (100, 1000, 10000):
    gamma_min = 1000.0
    eps = 0.1
    tau = 2.0 * math.log(N) / gamma_min
    z = (1.0 - eps) * gamma_min
    total = N * math.exp(-tau * z)
    expected = N ** (-1.0 + 2.0 * eps)
    assert math.isclose(total, expected, rel_tol=1e-12, abs_tol=1e-15)

print("FORTUNE_INT_PFLI_D2_ADAPTIVE_OCCUPANCY_PASS")
