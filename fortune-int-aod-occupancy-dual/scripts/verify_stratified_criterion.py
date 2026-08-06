#!/usr/bin/env python3
"""Exact finite verification of the stratified occupancy implication."""

from __future__ import annotations

import math
import random


def check(blocks: list[list[int]], qs: list[float]) -> tuple[float, list[float]]:
    total = 0.0
    pieces = []
    for zs, q in zip(blocks, qs, strict=True):
        value = sum((1.0 - q) ** z for z in zs)
        pieces.append(value)
        total += value
    return total, pieces

rng = random.Random(20260805)
for block_count in (1, 2, 4, 8):
    blocks = []
    qs = []
    budgets = []
    for b in range(block_count):
        size = 20 + b
        base = 30 + 5 * b
        zs = [base + rng.randrange(0, 8) for _ in range(size)]
        q = min(0.8, (math.log(size * block_count) + 2.0) / min(zs))
        blocks.append(zs)
        qs.append(q)
        budgets.append(1.0 / block_count)
    total, pieces = check(blocks, qs)
    assert all(piece < budget for piece, budget in zip(pieces, budgets, strict=True))
    assert total < 1.0

    failed = [list(zs) for zs in blocks]
    failed[-1][0] = 0
    failed_total, _ = check(failed, qs)
    assert failed_total >= 1.0
    print(
        f"blocks={block_count} total={total:.12g} failed_total={failed_total:.12g} "
        f"max_piece_budget_ratio={max(p/b for p,b in zip(pieces,budgets,strict=True)):.8g}"
    )

print("FORTUNE_INT_AOD_O4_STRATIFIED_CRITERION_PASS")
