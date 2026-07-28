#!/usr/bin/env python3
"""Compute the exact logarithmic depth requirement on finite primorial blocks."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import primerange

ETA = 0.8
TARGETS = (23, 53, 131, 257, 503, 1009, 5003)


def row(X: int) -> dict:
    block = [int(p) for p in primerange(X, 2 * X)]
    all_primes = [int(p) for p in primerange(2, 2 * X)]
    # Largest standard block centre before multiplying by the last block prime.
    excluded = block[-1]
    logP = sum(math.log(p) for p in all_primes if p != excluded)
    H = int(ETA * X * X)
    logH = math.log(H)
    # H is negligible relative to P at these targets, but use a stable exact-log correction.
    logPplusH = logP + math.log1p(H * math.exp(-logP))
    depth_H = math.ceil(logPplusH / logH)
    depth_H2 = math.ceil(logPplusH / (2 * logH))
    fixed_depth_cutoff_log = logPplusH / 10
    return {
        "X": X,
        "N": len(block),
        "H": H,
        "log_largest_centre": logP,
        "natural_cutoff_depth_U_equals_H": depth_H,
        "polynomial_cutoff_depth_U_equals_H_squared": depth_H2,
        "depth_over_N": depth_H / len(block),
        "asymptotic_proxy_X_over_2logX": X / (2 * math.log(X)),
        "required_log_cutoff_at_fixed_depth_10": fixed_depth_cutoff_log,
        "log_H": logH,
        "log_cutoff_over_log_H_at_depth_10": fixed_depth_cutoff_log / logH,
    }


def main() -> None:
    rows = [row(X) for X in TARGETS]
    for r in rows:
        assert r["natural_cutoff_depth_U_equals_H"] >= 2
        assert r["log_cutoff_over_log_H_at_depth_10"] > 1
    payload = {
        "status": "PASS",
        "scope": "finite exact-log calibration of the Heath-Brown depth inequality",
        "parameters": {"eta": ETA, "targets": list(TARGETS)},
        "rows": rows,
        "boundary": (
            "The asymptotic barrier is proved from log P asymp X and log H asymp log X; "
            "the finite table only calibrates its onset."
        ),
    }
    path = Path(__file__).with_name("heath_brown_depth_results.json")
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
