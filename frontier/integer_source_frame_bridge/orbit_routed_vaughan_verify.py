#!/usr/bin/env python3
"""Verify exact Vaughan identity and primorial-adapted routing bounds."""
from __future__ import annotations

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


def vaughan_terms(n: int, U: int, V: int) -> tuple[float, float, float, float]:
    ds = [int(d) for d in divisors(n)]
    t1 = sum(float(mobius(d)) * math.log(n // d) for d in ds if d <= U)
    t2 = 0.0
    for d in ds:
        if d <= U:
            rem = n // d
            t2 += sum(float(mobius(d)) * von_mangoldt(int(c))
                      for c in divisors(rem) if int(c) <= V)
    t3 = von_mangoldt(n) if n <= V else 0.0
    t4 = 0.0
    for a in ds:
        if a > U:
            rem = n // a
            t4 += sum(float(mobius(a)) * von_mangoldt(int(c))
                      for c in divisors(rem) if int(c) > V)
    return t1, t2, t3, t4


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


def routed_factors(n: int, Y: int) -> set[int]:
    ds = [int(d) for d in divisors(n)]
    out: set[int] = set()
    for d in ds:
        if d <= Y:
            out.add(n // d)
    for d in ds:
        if d <= Y:
            rem = n // d
            for c0 in divisors(rem):
                c = int(c0)
                if c <= Y and von_mangoldt(c) != 0:
                    out.add(rem // c)
    for a in ds:
        if a > Y:
            rem = n // a
            for c0 in divisors(rem):
                c = int(c0)
                if c > Y and von_mangoldt(c) != 0:
                    out.add(max(a, rem // c, c))
    return out


def main() -> None:
    universal_max_error = 0.0
    universal_cases = 0
    for U, V in ((2, 3), (5, 7), (11, 13), (19, 29)):
        for n in range(2, 2001):
            t1, t2, t3, t4 = vaughan_terms(n, U, V)
            err = abs(t1 - t2 + t3 + t4 - von_mangoldt(n))
            universal_max_error = max(universal_max_error, err)
            assert err < 5e-11, (n, U, V, err)
            universal_cases += 1

    # X=31 is the first tested prime block for which floor(P0^(1/3)) > H.
    X = 31
    block, centres, P0, H = block_data(X)
    Y, _ = integer_nthroot(P0, 3)
    Y = int(Y)
    assert Y > H, (X, P0, Y, H)

    rng = random.Random(SEED)
    offsets = sorted({2, 3, 5, 7, 11, X, X + 1, H - 1, H} |
                     {rng.randrange(2, H + 1) for _ in range(50)})
    shifted_max_error = 0.0
    minima = {"type1": None, "type2": None, "type4": None}
    column_support: dict[int, set[int]] = defaultdict(set)

    for j, P in enumerate(centres):
        for m in offsets:
            n = P + m
            t1, t2, t3, t4 = vaughan_terms(n, Y, Y)
            err = abs(t1 - t2 + t3 + t4 - von_mangoldt(n))
            shifted_max_error = max(shifted_max_error, err)
            assert err < 2e-9, (j, m, err)
            assert t3 == 0.0
            ds = [int(d) for d in divisors(n)]
            for d in ds:
                if d <= Y:
                    e = n // d
                    minima["type1"] = e if minima["type1"] is None else min(minima["type1"], e)
                    assert e > H
            for d in ds:
                if d <= Y:
                    rem = n // d
                    for c0 in divisors(rem):
                        c = int(c0)
                        if c <= Y and von_mangoldt(c) != 0:
                            b = rem // c
                            minima["type2"] = b if minima["type2"] is None else min(minima["type2"], b)
                            assert b > H
            for a in ds:
                if a > Y:
                    rem = n // a
                    for c0 in divisors(rem):
                        c = int(c0)
                        if c > Y and von_mangoldt(c) != 0:
                            D = max(a, rem // c, c)
                            minima["type4"] = D if minima["type4"] is None else min(minima["type4"], D)
                            assert D > H
            if m > X:
                for D in routed_factors(n, Y):
                    column_support[D].add(j)

    assert minima["type1"] is not None and minima["type2"] is not None
    all_recorded_minima_exceed_H = all(v is None or v > H for v in minima.values())
    assert all_recorded_minima_exceed_H

    max_support = 0
    max_ratio = 0.0
    worst_D = None
    for D, support in column_support.items():
        delta = max(1, math.ceil(math.log(D / H) / math.log(2 * X)))
        bound = 1 + (len(centres) - 1) // delta
        assert len(support) <= bound, (D, sorted(support), delta, bound)
        if len(support) > max_support:
            max_support, worst_D = len(support), D
        max_ratio = max(max_ratio, len(support) / bound)

    payload = {
        "status": "PASS",
        "scope": "exact Vaughan identity and post-threshold primorial routing",
        "universal": {"cases": universal_cases, "max_error": universal_max_error},
        "shifted_block": {
            "X": X, "N": len(centres), "H": H, "P0": P0,
            "Y_floor_cuberoot_P0": Y, "Y_exceeds_H": Y > H,
            "offsets_per_centre": len(offsets), "max_error": shifted_max_error,
            "minimum_type1_routed_factor": minima["type1"],
            "minimum_subtraction_routed_factor": minima["type2"],
            "minimum_large_large_routed_factor": minima["type4"],
            "all_recorded_minima_exceed_H": all_recorded_minima_exceed_H,
        },
        "routed_columns": {
            "active_column_count": len(column_support),
            "observed_max_centre_support": max_support,
            "worst_D": worst_D,
            "maximum_support_to_theorem_bound_ratio": max_ratio,
        },
        "boundary": "Exact identities and routing only; signed trilinear dispersion remains open.",
    }
    Path(__file__).with_name("orbit_routed_vaughan_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
