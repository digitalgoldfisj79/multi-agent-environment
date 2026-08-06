#!/usr/bin/env python3
"""Verify the exact occupancy expansion and Bonferroni inequalities."""

from fractions import Fraction
from math import comb

for q in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
    for z in range(0, 30):
        exact = (1 - q) ** z
        expansion = sum(((-q) ** k) * comb(z, k) for k in range(z + 1))
        assert exact == expansion, (q, z, exact, expansion)
        for K in range(0, 8):
            even_end = min(2 * K, z)
            odd_end = min(2 * K + 1, z)
            upper = sum(((-q) ** k) * comb(z, k) for k in range(even_end + 1))
            lower = sum(((-q) ** k) * comb(z, k) for k in range(odd_end + 1))
            # Once the full finite expansion has been reached both bounds are exact.
            assert lower <= exact <= upper, (q, z, K, lower, exact, upper)

print("FORTUNE_INT_PFLI_D3_FACTORIAL_EXPANSION_PASS")
