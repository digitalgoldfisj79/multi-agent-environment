#!/usr/bin/env python3
"""Verify the primorial-index shrinking-target separation theorem."""
from __future__ import annotations

import json
import math
import random
from pathlib import Path

from sympy import primerange

ETA = 0.8
EXHAUSTIVE_TARGETS = (11, 17, 23, 29, 37)
SCALE_TARGETS = (23, 37, 53, 101)
ASYMPTOTIC_TARGETS = (53, 101, 257, 503, 1009)
DEPTHS = (2, 3, 5, 10)
SEED = 20260728


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


def visit_list(centres: list[int], X: int, H: int, d: int):
    out = []
    for j, P in enumerate(centres):
        residue = (-P) % d
        if residue == 0:
            residue = d
        if X < residue <= H:
            out.append((j, residue))
    return out


def check_visit_pairs(
    X: int,
    block: list[int],
    H: int,
    d: int,
    visits: list[tuple[int, int]],
) -> int:
    delta = max(1, math.ceil(math.log(d / H) / math.log(2 * X)))
    for u in range(len(visits)):
        j, m = visits[u]
        for v in range(u + 1, len(visits)):
            k, n = visits[v]
            Q = 1
            for t in range(j, k):
                Q *= block[t]
            assert d <= H * Q, (X, d, j, k, m, n, H, Q)
            assert k - j >= delta, (X, d, j, k, delta)
    assert len(visits) <= 1 + (len(block) - 1) // delta
    return delta


def exhaustive_row(X: int) -> dict:
    block, centres, _, H = block_data(X)
    stop = min(120_000, H * 100)
    max_visits = 0
    worst = None
    pair_count = 0
    for d in range(H + 1, stop + 1):
        visits = visit_list(centres, X, H, d)
        check_visit_pairs(X, block, H, d, visits)
        pair_count += len(visits) * (len(visits) - 1) // 2
        if len(visits) > max_visits:
            max_visits = len(visits)
            worst = (d, visits)
    return {
        "X": X,
        "N": len(block),
        "H": H,
        "d_start": H + 1,
        "d_stop": stop,
        "max_visits": max_visits,
        "worst_d": worst[0] if worst else None,
        "worst_visit_indices": [j for j, _ in worst[1]] if worst else [],
        "verified_visit_pairs": pair_count,
    }


def scale_rows(X: int, samples: int = 2000) -> dict:
    block, centres, _, H = block_data(X)
    rng = random.Random(SEED + X)
    rows = []
    for s in range(1, len(block) + 1):
        D = H * (2 * X) ** s
        max_visits = 0
        worst_indices: list[int] = []
        min_delta = None
        for _ in range(samples):
            d = rng.randrange(D, 2 * D)
            visits = visit_list(centres, X, H, d)
            delta = check_visit_pairs(X, block, H, d, visits)
            min_delta = delta if min_delta is None else min(min_delta, delta)
            if len(visits) > max_visits:
                max_visits = len(visits)
                worst_indices = [j for j, _ in visits]
        rows.append(
            {
                "s": s,
                "D_decimal_digits": len(str(D)),
                "sample_count": samples,
                "minimum_delta_seen": min_delta,
                "theorem_bound": 1 + (len(block) - 1) // s,
                "sample_max_visits": max_visits,
                "sample_worst_indices": worst_indices,
            }
        )
    return {"X": X, "N": len(block), "H": H, "rows": rows}


def depth_row(X: int) -> dict:
    block, _, _, H = block_data(X)
    log_P0 = sum(math.log(p) for p in primerange(2, X))
    rows = []
    for R in DEPTHS:
        denominator = log_P0 / R - math.log(H)
        if denominator <= 0:
            delta = 0
            bound = None
        else:
            delta = max(1, math.ceil(denominator / math.log(2 * X)))
            bound = 1 + (len(block) - 1) // delta
        rows.append(
            {
                "R": R,
                "log_P0_over_R_minus_log_H": denominator,
                "delta_at_largest_factor_threshold": delta,
                "centre_multiplicity_bound": bound,
            }
        )
    return {
        "X": X,
        "N": len(block),
        "H": H,
        "log_P0": log_P0,
        "rows": rows,
    }


def main() -> None:
    full = {
        "status": "PASS",
        "scope": (
            "exact finite verification of primorial shrinking-target separation "
            "and fixed-depth multiplicity formula"
        ),
        "parameters": {"eta": ETA, "seed": SEED},
        "exhaustive_rows": [exhaustive_row(X) for X in EXHAUSTIVE_TARGETS],
        "scale_sampling": [scale_rows(X) for X in SCALE_TARGETS],
        "fixed_depth_tables": [depth_row(X) for X in ASYMPTOTIC_TARGETS],
        "boundary": (
            "Finite checks verify the exact inequalities; the asymptotic O(R) "
            "corollary follows from log P0 asymp X and N asymp X/log X, not "
            "from sampling."
        ),
    }
    compact = {
        "status": full["status"],
        "parameters": full["parameters"],
        "exhaustive_rows": full["exhaustive_rows"],
        "scale_summary": [
            {
                "X": item["X"],
                "N": item["N"],
                "H": item["H"],
                "first_scale": item["rows"][0],
                "second_scale": item["rows"][1],
                "last_scale": item["rows"][-1],
            }
            for item in full["scale_sampling"]
        ],
        "fixed_depth_tables": full["fixed_depth_tables"],
        "boundary": full["boundary"],
    }
    root = Path(__file__).resolve().parent
    (root / "primorial_shrinking_target_results_full.json").write_text(
        json.dumps(full, indent=2) + "\n", encoding="utf-8"
    )
    (root / "primorial_shrinking_target_results.json").write_text(
        json.dumps(compact, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(compact, indent=2))


if __name__ == "__main__":
    main()
