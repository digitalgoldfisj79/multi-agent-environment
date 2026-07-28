#!/usr/bin/env python3
"""Verify the exact three-orbit-column source and additive completion."""
from __future__ import annotations

import cmath
import json
import math
import random
from collections import defaultdict
from pathlib import Path

from sympy import divisors, factorint, integer_nthroot, mobius, primerange

ETA = 0.8
SEED = 20260728


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def block_data(X: int):
    block = [int(p) for p in primerange(X, 2 * X)]
    P = 1
    for p in primerange(2, X):
        P *= int(p)
    P0 = P
    centres = []
    for ell in block:
        centres.append(P)
        P *= ell
    return block, centres, P0, int(ETA * X * X)


def A_Y(q: int, Y: int) -> float:
    return sum(float(mobius(d)) * von_mangoldt(q // d)
               for d in divisors(q) if d <= Y and q // d <= Y)


def B_Y(q: int, Y: int) -> float:
    return sum(von_mangoldt(int(c)) for c in divisors(q) if int(c) > Y)


def additive_completion(P: int, D: int, lo: int, hi: int) -> complex:
    total = 0j
    for r in range(D):
        physical = sum(cmath.exp(2j * math.pi * r * m / D)
                       for m in range(lo, hi + 1))
        total += physical * cmath.exp(2j * math.pi * r * P / D)
    return total / D


def main() -> None:
    X = 31
    _, centres, P0, H = block_data(X)
    Y, _ = integer_nthroot(P0, 3)
    Y = int(Y)
    assert Y > H, (X, P0, Y, H)

    rng = random.Random(SEED)
    offsets = sorted({2, 3, 5, 7, 11, X, X + 1, H - 1, H} |
                     {rng.randrange(2, H + 1) for _ in range(50)})
    max_source_error = 0.0
    max_column_errors = {"type1": 0.0, "type2": 0.0, "type3": 0.0}
    output_cases = 0
    active_columns: dict[int, set[int]] = defaultdict(set)

    for j, P in enumerate(centres):
        for m in offsets:
            n = P + m
            ds = [int(d) for d in divisors(n)]
            type1: dict[int, float] = defaultdict(float)
            type2: dict[int, float] = defaultdict(float)
            type3: dict[int, float] = defaultdict(float)

            for d in ds:
                if d <= Y:
                    type1[n // d] += float(mobius(d)) * math.log(n // d)
            for d in ds:
                if d <= Y:
                    rem = n // d
                    for c0 in divisors(rem):
                        c = int(c0)
                        if c <= Y:
                            type2[rem // c] -= float(mobius(d)) * von_mangoldt(c)
            for a in ds:
                if a > Y:
                    rem = n // a
                    for c0 in divisors(rem):
                        c = int(c0)
                        if c > Y:
                            type3[a] += float(mobius(a)) * von_mangoldt(c)

            for D, value in type1.items():
                q = (P + D - 1) // D
                assert D * q - P == m and q <= Y and D > H
                expected = float(mobius(q)) * math.log(D)
                err = abs(value - expected)
                max_column_errors["type1"] = max(max_column_errors["type1"], err)
                assert err < 2e-11
                if m > X:
                    active_columns[D].add(j)
            for D, value in type2.items():
                q = (P + D - 1) // D
                assert D * q - P == m and D > H
                err = abs(value + A_Y(q, Y))
                max_column_errors["type2"] = max(max_column_errors["type2"], err)
                assert err < 2e-11
                if m > X:
                    active_columns[D].add(j)
            for D, value in type3.items():
                q = (P + D - 1) // D
                assert D * q - P == m and D > Y
                err = abs(value - float(mobius(D)) * B_Y(q, Y))
                max_column_errors["type3"] = max(max_column_errors["type3"], err)
                assert err < 2e-11
                if m > X:
                    active_columns[D].add(j)

            orbit_value = sum(type1.values()) + sum(type2.values()) + sum(type3.values())
            source_error = abs(orbit_value - von_mangoldt(n))
            max_source_error = max(max_source_error, source_error)
            assert source_error < 2e-9, (j, m, orbit_value, von_mangoldt(n))
            output_cases += 1

    max_support = 0
    for D, support in active_columns.items():
        delta = max(1, math.ceil(math.log(D / H) / math.log(2 * X)))
        bound = 1 + (len(centres) - 1) // delta
        assert len(support) <= bound
        max_support = max(max_support, len(support))

    completion_max_error = 0.0
    P = centres[0]
    completion_cases = 12
    for D in range(H + 1, H + completion_cases + 1):
        got = additive_completion(P, D, 2, H)
        residue = (-P) % D
        expected = 1.0 if 2 <= residue <= H else 0.0
        completion_max_error = max(completion_max_error, abs(got - expected))
        assert abs(got - expected) < 3e-9, (D, residue, got, expected)

    payload = {
        "status": "PASS",
        "scope": "post-threshold three-orbit-column source and additive completion",
        "parameters": {"X": X, "N": len(centres), "H": H, "P0": P0, "Y": Y},
        "source": {
            "output_cases": output_cases,
            "max_source_error": max_source_error,
            "max_type1_column_error": max_column_errors["type1"],
            "max_type2_column_error": max_column_errors["type2"],
            "max_type3_column_error": max_column_errors["type3"],
            "active_column_count": len(active_columns),
            "observed_max_candidate_centre_support": max_support,
        },
        "completion": {
            "cases": completion_cases,
            "D_range": [H + 1, H + completion_cases],
            "max_error": completion_max_error,
        },
        "boundary": "Exact reduction only; nonzero reciprocal-mode estimate remains open.",
    }
    Path(__file__).with_name("three_orbit_column_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
