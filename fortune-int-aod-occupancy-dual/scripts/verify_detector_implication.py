#!/usr/bin/env python3
"""Exact finite checks for the weighted occupancy implication."""

from __future__ import annotations

import itertools
import math


def detector(row: tuple[int, ...], weights: tuple[float, ...]) -> float:
    return math.exp(-sum(w * hit for w, hit in zip(weights, row, strict=True)))


for rows_n in range(1, 5):
    for cols_n in range(1, 6):
        all_rows = list(itertools.product((0, 1), repeat=cols_n))
        profiles = [
            tuple(0.0 for _ in range(cols_n)),
            tuple(0.25 for _ in range(cols_n)),
            tuple((i + 1) / cols_n for i in range(cols_n)),
        ]
        for panel_rows in itertools.product(all_rows, repeat=rows_n):
            has_failure = any(not any(row) for row in panel_rows)
            for weights in profiles:
                total = sum(detector(row, weights) for row in panel_rows)
                assert total >= 0.0
                if has_failure:
                    assert total >= 1.0 - 1e-12

print("FORTUNE_INT_AOD_O1_WEIGHTED_DETECTOR_PASS")
