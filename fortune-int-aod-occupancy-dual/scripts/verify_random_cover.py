#!/usr/bin/env python3
"""Brute-force exact checks for the random-cover dual identities."""

from __future__ import annotations

import itertools
import math
from fractions import Fraction


def hypergeometric_formula(m: int, k: int, z: int) -> Fraction:
    if k > m - z:
        return Fraction(0, 1)
    return Fraction(math.comb(m - z, k), math.comb(m, k))


for m in range(1, 11):
    universe = tuple(range(m))
    for z in range(m + 1):
        successes = set(range(z))
        for k in range(m + 1):
            subsets = list(itertools.combinations(universe, k))
            missed = sum(1 for subset in subsets if successes.isdisjoint(subset))
            brute = Fraction(missed, len(subsets))
            assert brute == hypergeometric_formula(m, k, z)

for z in range(0, 10):
    for q_num in range(0, 11):
        q = Fraction(q_num, 10)
        probability = sum(
            (q ** len(chosen))
            * ((1 - q) ** (z - len(chosen)))
            for mask in itertools.product((0, 1), repeat=z)
            for chosen in [tuple(i for i, bit in enumerate(mask) if bit)]
            if not chosen
        )
        assert probability == (1 - q) ** z

print("FORTUNE_INT_AOD_O2_RANDOM_COVER_PASS")
