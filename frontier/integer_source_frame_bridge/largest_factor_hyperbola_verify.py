#!/usr/bin/env python3
"""Verify the grouped mu*log identity and its one-point primorial routing."""
from __future__ import annotations

import json
import math
import random
from pathlib import Path

from sympy import divisors, factorint, mobius, primerange

ETA = 0.8
SEED = 20260728


def von_mangoldt(n: int) -> float:
    factors = factorint(n)
    if len(factors) == 1:
        p = next(iter(factors))
        return math.log(int(p))
    return 0.0


def W(D: int, E: int) -> float:
    if D > E:
        return float(mobius(D)) * math.log(E) + float(mobius(E)) * math.log(D)
    return float(mobius(D)) * math.log(D)


def grouped_hyperbola(n: int) -> float:
    total = 0.0
    for E in divisors(n):
        D = n // E
        if D < E:
            continue
        total += W(int(D), int(E))
    return total


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


def main() -> None:
    max_error = 0.0
    for n in range(2, 5001):
        err = abs(grouped_hyperbola(n) - von_mangoldt(n))
        max_error = max(max_error, err)
        assert err < 2e-12, (n, grouped_hyperbola(n), von_mangoldt(n))

    X = 23
    block, centres, P0, H = block_data(X)
    assert P0 > H * H

    rng = random.Random(SEED)
    offsets = sorted({2, 3, 5, 7, 11, X, X + 1, H - 1, H} | {
        rng.randrange(2, H + 1) for _ in range(80)
    })

    shifted_checks = 0
    shifted_max_error = 0.0
    all_largest_factors_above_H = True
    for P in centres:
        for m in offsets:
            n = P + m
            value = grouped_hyperbola(n)
            target = von_mangoldt(n)
            err = abs(value - target)
            shifted_max_error = max(shifted_max_error, err)
            assert err < 2e-11, (P, m, value, target)
            for E in divisors(n):
                D = n // E
                if D < E:
                    continue
                all_largest_factors_above_H &= D > H
                assert D >= math.isqrt(n)
            shifted_checks += 1
    assert all_largest_factors_above_H

    one_point_checks = 0
    max_column_support = 0
    worst_D = None
    delta = math.ceil(math.log(math.sqrt(P0) / H) / math.log(2 * X))
    theorem_bound = 1 + (len(centres) - 1) // max(1, delta)
    for D in range(H + 1, H + 20001):
        support = []
        for j, P in enumerate(centres):
            E = (P + D - 1) // D
            m = D * E - P
            direct = [u for u in range(1, H + 1) if (P + u) % D == 0]
            assert len(direct) <= 1
            if 1 <= m <= H:
                assert direct == [m]
            else:
                assert direct == []
            if X < m <= H and E <= D:
                support.append(j)
            one_point_checks += 1
        if len(support) > max_column_support:
            max_column_support = len(support)
            worst_D = D
        # The exact D-specific theorem is at least as strong as the threshold bound.
        d_delta = max(1, math.ceil(math.log(D / H) / math.log(2 * X)))
        assert len(support) <= 1 + (len(centres) - 1) // d_delta
    assert max_column_support <= theorem_bound

    payload = {
        "status": "PASS",
        "scope": "finite verification of largest-factor hyperbola and one-point orbit identities",
        "universal_range": [2, 5000],
        "universal_max_error": max_error,
        "shifted_block": {
            "X": X,
            "N": len(centres),
            "H": H,
            "P0": P0,
            "sqrt_P0_exceeds_H": P0 > H * H,
            "offset_count_per_centre": len(offsets),
            "shifted_checks": shifted_checks,
            "shifted_max_error": shifted_max_error,
            "all_routed_largest_factors_above_H": all_largest_factors_above_H,
        },
        "one_point_routing": {
            "D_range": [H + 1, H + 20000],
            "checks": one_point_checks,
            "threshold_delta": delta,
            "threshold_multiplicity_bound": theorem_bound,
            "observed_max_column_support": max_column_support,
            "worst_D": worst_D,
        },
        "boundary": (
            "These finite checks verify exact algebraic identities and routing. "
            "They do not prove the signed hyperbola-energy estimate."
        ),
    }
    path = Path(__file__).with_name("largest_factor_hyperbola_results.json")
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
