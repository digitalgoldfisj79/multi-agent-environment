#!/usr/bin/env python3
"""Verify a logarithmic Bonferroni order suffices in the conditional Poisson benchmark."""

from __future__ import annotations

import math

EPS = 0.10
BETA = 10.0
MEAN_RATIO = 1.10

for total_rows in (100, 1_000, 10_000, 1_000_000, 100_000_000):
    logm = math.log(total_rows)
    x_max = (1.0 + 3.0 * EPS) * MEAN_RATIO * logm
    k = int(math.ceil(BETA * logm))
    if k % 2:
        k += 1
    log_remainder = (k + 1) * math.log(x_max) - math.lgamma(k + 2)
    target_log = -(1.0 + 2.0 * EPS) * logm
    assert log_remainder < target_log
    print(
        f"rows={total_rows} x_max={x_max:.8g} even_order={k} "
        f"log_remainder={log_remainder:.8g} target_log={target_log:.8g}"
    )

print("FORTUNE_INT_AOD_O6_RUHL_BUDGET_PASS")
