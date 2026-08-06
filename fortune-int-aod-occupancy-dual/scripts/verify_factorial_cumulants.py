#!/usr/bin/env python3
"""Exact factorial moment/cumulant algebra checks."""

from __future__ import annotations

import math
from fractions import Fraction


def falling(z: int, k: int) -> int:
    out = 1
    for r in range(k):
        out *= z - r
    return out


def factorial_moments(rows: list[int], order: int) -> list[Fraction]:
    n = len(rows)
    return [
        Fraction(sum(falling(z, k) for z in rows), n)
        for k in range(order + 1)
    ]


def factorial_cumulants(moments: list[Fraction]) -> list[Fraction]:
    order = len(moments) - 1
    cumulants = [Fraction(0, 1)] * (order + 1)
    for n in range(1, order + 1):
        correction = sum(
            Fraction(math.comb(n - 1, r - 1), 1)
            * cumulants[r]
            * moments[n - r]
            for r in range(1, n)
        )
        cumulants[n] = moments[n] - correction
    return cumulants


def reconstruct(cumulants: list[Fraction]) -> list[Fraction]:
    order = len(cumulants) - 1
    moments = [Fraction(0, 1)] * (order + 1)
    moments[0] = Fraction(1, 1)
    for n in range(1, order + 1):
        moments[n] = sum(
            Fraction(math.comb(n - 1, r - 1), 1)
            * cumulants[r]
            * moments[n - r]
            for r in range(1, n + 1)
        )
    return moments


panels = [
    [0, 1],
    [1, 1, 2, 3],
    [0, 2, 2, 4, 7],
    [3, 3, 3, 3],
]
for rows in panels:
    order = 8
    moments = factorial_moments(rows, order)
    cumulants = factorial_cumulants(moments)
    assert reconstruct(cumulants) == moments

# Bernoulli(p) has factorial cumulants (-1)^(n-1) (n-1)! p^n.
num, den = 3, 10
rows = [1] * num + [0] * (den - num)
moments = factorial_moments(rows, 8)
cumulants = factorial_cumulants(moments)
p = Fraction(num, den)
for n in range(1, 9):
    expected = ((-1) ** (n - 1)) * math.factorial(n - 1) * (p ** n)
    assert cumulants[n] == expected

print("FORTUNE_INT_AOD_O4_FACTORIAL_CUMULANT_PASS")
