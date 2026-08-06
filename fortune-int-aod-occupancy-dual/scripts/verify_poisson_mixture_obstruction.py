#!/usr/bin/env python3
"""Exact surrogate obstruction for an unstratified connected expansion."""

from __future__ import annotations

import cmath
import math

# Equal mixture of Poisson laws with means lambda_- and lambda_+ has
# G(1-q)=0.5*exp(-q lambda_-)+0.5*exp(-q lambda_+).
# Its nearest complex zero has modulus pi/(lambda_+-lambda_-).
for x in (100, 1000, 10_000, 100_000, 1_000_000):
    lam_lo = 0.6 * x
    lam_hi = 1.2 * x
    delta = lam_hi - lam_lo
    zero_radius = math.pi / delta
    n = x / math.log(x)
    useful_q = 2.0 * math.log(n) / ((lam_lo + lam_hi) / 2.0)
    ratio = useful_q / zero_radius
    assert ratio > 1.0

    q0 = 1j * math.pi / delta
    value = 0.5 * cmath.exp(-q0 * lam_lo) + 0.5 * cmath.exp(-q0 * lam_hi)
    assert abs(value) < 1e-12
    print(
        f"X={x} delta_lambda={delta:.8g} zero_radius={zero_radius:.8g} "
        f"useful_q={useful_q:.8g} q_over_radius={ratio:.8g}"
    )

print("FORTUNE_INT_AOD_O4_GLOBAL_MIXTURE_OBSTRUCTION_PASS")
