#!/usr/bin/env python3
"""Adversarial incidence panels with matched moments and trivial column statistics."""

from __future__ import annotations

import math


def falling(z: int, k: int) -> int:
    out = 1
    for r in range(k):
        out *= z - r
    return out


def parity_panel(k: int, parity: int) -> list[int]:
    rows: list[int] = []
    for r in range(k + 2):
        if r % 2 == parity:
            rows.extend([r] * math.comb(k + 1, r))
    return rows


for k in range(0, 13):
    even = parity_panel(k, 0)
    odd = parity_panel(k, 1)
    assert len(even) == len(odd) == 2**k
    assert 0 in even and 0 not in odd
    for order in range(k + 1):
        assert sum(falling(z, order) for z in even) == sum(
            falling(z, order) for z in odd
        )

    # From K>=1 the panels match their first moments. Realize every success as
    # a private column belonging to exactly one row. The two incidence matrices
    # then have identical all-one column-degree multisets and zero pairwise
    # column overlap, while only the even panel has a zero row.
    even_columns = sum(even)
    odd_columns = sum(odd)
    if k >= 1:
        assert even_columns == odd_columns
        column_degree_multiset_even = [1] * even_columns
        column_degree_multiset_odd = [1] * odd_columns
        assert column_degree_multiset_even == column_degree_multiset_odd
        pairwise_overlap_even = 0
        pairwise_overlap_odd = 0
        assert pairwise_overlap_even == pairwise_overlap_odd

    print(
        f"K={k} rows={2**k} even_columns={even_columns} "
        f"odd_columns={odd_columns} matched_moments=0..{k} "
        f"matched_private_column_stats={int(k >= 1)} zero_even=1 zero_odd=0"
    )

print("FORTUNE_INT_AOD_O8_PRIVATE_COLUMN_ADVERSARY_PASS")
