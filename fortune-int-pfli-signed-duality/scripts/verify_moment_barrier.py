#!/usr/bin/env python3
"""Exact binomial finite-difference countermodels for one-defect moment tests."""

from math import comb


def falling(z: int, k: int) -> int:
    out = 1
    for t in range(k):
        out *= z - t
    return out


def panels(K: int) -> tuple[list[int], list[int]]:
    n = K + 1
    even: list[int] = []
    odd: list[int] = []
    for r in range(n + 1):
        target = even if r % 2 == 0 else odd
        target.extend([r] * comb(n, r))
    return even, odd


for K in range(0, 18):
    even, odd = panels(K)
    assert len(even) == len(odd) == 2**K
    assert even.count(0) == 1
    assert 0 not in odd

    for k in range(K + 1):
        assert sum(z**k for z in even) == sum(z**k for z in odd)
        assert sum(falling(z, k) for z in even) == sum(falling(z, k) for z in odd)
        assert sum(comb(z, k) for z in even) == sum(comb(z, k) for z in odd)

    # Padding preserves all equalities and the zero/nonzero distinction.
    N = 2**K + 7
    pad = K + 3
    even_padded = even + [pad] * (N - len(even))
    odd_padded = odd + [pad] * (N - len(odd))
    assert len(even_padded) == len(odd_padded) == N
    assert 0 in even_padded and 0 not in odd_padded
    for k in range(K + 1):
        assert sum(comb(z, k) for z in even_padded) == sum(comb(z, k) for z in odd_padded)

    print(f"K={K} rows={2**K} matched_factorial_orders=0..{K} zero_panel=1 nonzero_panel=1")

print("FORTUNE_INT_PFLI_D4_MOMENT_BARRIER_PASS")
