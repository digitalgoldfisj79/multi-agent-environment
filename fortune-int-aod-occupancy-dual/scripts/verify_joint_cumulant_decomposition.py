#!/usr/bin/env python3
"""Verify ordinary cumulants as sums of common-row joint column cumulants."""

from __future__ import annotations

import itertools
import math
import random
from fractions import Fraction


def partitions(items: tuple[int, ...]):
    if not items:
        yield []
        return
    first = items[0]
    for rest in partitions(items[1:]):
        yield [(first,), *rest]
        for i in range(len(rest)):
            yield [*rest[:i], tuple(sorted((first, *rest[i]))), *rest[i + 1 :]]


def canonical_parts(k: int):
    seen = set()
    for p in partitions(tuple(range(k))):
        key = tuple(sorted(tuple(sorted(block)) for block in p))
        if key not in seen:
            seen.add(key)
            yield key


def joint_moment(matrix: list[list[int]], cols: tuple[int, ...]) -> Fraction:
    return Fraction(sum(math.prod(row[c] for c in cols) for row in matrix), len(matrix))


def joint_cumulant(matrix: list[list[int]], cols: tuple[int, ...]) -> Fraction:
    total = Fraction(0)
    for part in canonical_parts(len(cols)):
        coeff = Fraction(((-1) ** (len(part) - 1)) * math.factorial(len(part) - 1))
        prod = Fraction(1)
        for block in part:
            prod *= joint_moment(matrix, tuple(cols[i] for i in block))
        total += coeff * prod
    return total


def ordinary_cumulants(zs: list[int], order: int) -> list[Fraction]:
    moments = [Fraction(1)]
    for k in range(1, order + 1):
        moments.append(Fraction(sum(z**k for z in zs), len(zs)))
    cumulants = [Fraction(0)] * (order + 1)
    for k in range(1, order + 1):
        cumulants[k] = moments[k] - sum(
            Fraction(math.comb(k - 1, r - 1)) * cumulants[r] * moments[k - r]
            for r in range(1, k)
        )
    return cumulants


rng = random.Random(560825)
for rows, cols in ((5, 4), (7, 5), (9, 6)):
    matrix = [[rng.randrange(2) for _ in range(cols)] for _ in range(rows)]
    zs = [sum(row) for row in matrix]
    max_order = min(4, cols)
    cumulants = ordinary_cumulants(zs, max_order)
    for k in range(1, max_order + 1):
        # Multilinearity of ordinary cumulants for Z=sum_m I_m requires all
        # ordered column tuples, including repetitions.
        connected_sum = sum(
            joint_cumulant(matrix, ordered)
            for ordered in itertools.product(range(cols), repeat=k)
        )
        assert connected_sum == cumulants[k], (
            rows,
            cols,
            k,
            connected_sum,
            cumulants[k],
        )
    print(f"rows={rows} cols={cols} verified_ordinary_orders=1..{max_order}")

print("FORTUNE_INT_AOD_O5_ORDINARY_JOINT_CUMULANT_PASS")
