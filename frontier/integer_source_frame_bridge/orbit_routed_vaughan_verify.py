#!/usr/bin/env python3
"""Verify exact Vaughan identity and primorial-adapted routing bounds."""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

from sympy import divisors, factorint, integer_nthroot, mobius, primerange

ETA = 0.8


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    if len(fs) == 1:
        return math.log(int(next(iter(fs))))
    return 0.0


def vaughan_terms(n: int, U: int, V: int) -> tuple[float, float, float, float]:
    ds = [int(d) for d in divisors(n)]
    t1 = sum(float(mobius(d)) * math.log(n // d) for d in ds if d <= U)

    t2 = 0.0
    for d in ds:
        if d > U:
            continue
        rem = n // d
        for c in divisors(rem):
            c = int(c)
            if c <= V:
                t2 += float(mobius(d)) * von_mangoldt(c)

    t3 = von_mangoldt(n) if n <= V else 0.0

    t4 = 0.0
    for a in ds:
        if a <= U:
            continue
        rem = n // a
        for c in divisors(rem):
            c = int(c)
            if c > V:
                t4 += float(mobius(a)) * von_mangoldt(c)

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


def routed_columns_for_output(n: int, U: int, V: int) -> set[int]:
    out: set[int] = set()
    ds = [int(d) for d in divisors(n)]

    for d in ds:
        if d <= U:
            e = n // d
            out.add(e)

    for d in ds:
        if d > U:
            continue
        rem = n // d
        for c0 in divisors(rem):
            c = int(c0)
            if c <= V and von_mangoldt(c) != 0.0:
                b = rem // c
                out.add(b)

    for a in ds:
        if a <= U:
            continue
        rem = n // a
        for c0 in divisors(rem):
            c = int(c0)
            if c > V and von_mangoldt(c) != 0.0:
                b = rem // c
                # Lexicographic tie breaking is irrelevant for the numerical value.
                out.add(max(a, b, c))
    return out


def main() -> None:
    universal_max_error = 0.0
    universal_cases = 0
    for U, V in ((2, 3), (5, 7), (11, 13), (19, 29)):
        for n in range(2, 5001):
            t1, t2, t3, t4 = vaughan_terms(n, U, V)
            got = t1 - t2 + t3 + t4
            err = abs(got - von_mangoldt(n))
            universal_max_error = max(universal_max_error, err)
            assert err < 5e-11, (n, U, V, got, von_mangoldt(n), (t1, t2, t3, t4))
            universal_cases += 1

    X = 23
    block, centres, P0, H = block_data(X)
    Y, exact = integer_nthroot(P0, 3)
    Y = int(Y)
    assert Y > H

    shifted_max_error = 0.0
    shifted_cases = 0
    type1_min = None
    type2_min = None
    type4_min = None
    column_support: dict[int, set[int]] = defaultdict(set)

    for j, P in enumerate(centres):
        for m in range(2, H + 1):
            n = P + m
            t1, t2, t3, t4 = vaughan_terms(n, Y, Y)
            got = t1 - t2 + t3 + t4
            err = abs(got - von_mangoldt(n))
            shifted_max_error = max(shifted_max_error, err)
            assert err < 2e-9, (j, m, got, von_mangoldt(n))
            assert t3 == 0.0

            ds = [int(d) for d in divisors(n)]
            for d in ds:
                if d <= Y:
                    e = n // d
                    type1_min = e if type1_min is None else min(type1_min, e)
                    assert e > H

            for d in ds:
                if d > Y:
                    continue
                rem = n // d
                for c0 in divisors(rem):
                    c = int(c0)
                    if c <= Y and von_mangoldt(c) != 0.0:
                        b = rem // c
                        type2_min = b if type2_min is None else min(type2_min, b)
                        assert b > H

            for a in ds:
                if a <= Y:
                    continue
                rem = n // a
                for c0 in divisors(rem):
                    c = int(c0)
                    if c > Y and von_mangoldt(c) != 0.0:
                        b = rem // c
                        D = max(a, b, c)
                        type4_min = D if type4_min is None else min(type4_min, D)
                        assert D > H

            if m > X:
                for D in routed_columns_for_output(n, Y, Y):
                    column_support[D].add(j)
            shifted_cases += 1

    # Apply the exact D-specific shrinking-target bound to every routed column.
    max_support = 0
    worst_D = None
    max_ratio = 0.0
    for D, support in column_support.items():
        delta = max(1, math.ceil(math.log(D / H) / math.log(2 * X)))
        bound = 1 + (len(centres) - 1) // delta
        assert len(support) <= bound, (D, sorted(support), delta, bound)
        if len(support) > max_support:
            max_support = len(support)
            worst_D = D
        max_ratio = max(max_ratio, len(support) / bound)

    payload = {
        "status": "PASS",
        "scope": "exact Vaughan identity and primorial-adapted fixed-complexity routing",
        "universal": {
            "cases": universal_cases,
            "max_error": universal_max_error,
            "cutoff_pairs": [[2, 3], [5, 7], [11, 13], [19, 29]],
        },
        "shifted_block": {
            "X": X,
            "N": len(centres),
            "H": H,
            "P0": P0,
            "Y_floor_cuberoot_P0": Y,
            "Y_exceeds_H": Y > H,
            "cases": shifted_cases,
            "max_error": shifted_max_error,
            "minimum_type1_routed_factor": type1_min,
            "minimum_subtraction_routed_factor": type2_min,
            "minimum_large_large_routed_factor": type4_min,
            "all_minima_exceed_H": min(type1_min, type2_min, type4_min) > H,
        },
        "routed_columns": {
            "active_column_count": len(column_support),
            "observed_max_centre_support": max_support,
            "worst_D": worst_D,
            "maximum_support_to_theorem_bound_ratio": max_ratio,
        },
        "boundary": (
            "The verifier checks exact decomposition and routing. It does not "
            "prove the signed trilinear dispersion estimate."
        ),
    }
    path = Path(__file__).with_name("orbit_routed_vaughan_results.json")
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
