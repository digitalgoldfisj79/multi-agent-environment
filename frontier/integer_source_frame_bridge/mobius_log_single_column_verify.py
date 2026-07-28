#!/usr/bin/env python3
"""Verify the minimal Möbius-log source, zero mode and large-column form."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

from sympy import divisors, factorint, mobius


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def fourier_incidence(P: int, H: int, d: int, weights: dict[int, float]) -> complex:
    total = 0j
    for r in range(d):
        wh = sum(w * cmath.exp(2j * math.pi * r * m / d)
                 for m, w in weights.items())
        total += wh * cmath.exp(2j * math.pi * r * P / d)
    return total / d


def one_case(P: int, H: int) -> dict:
    weights = {m: 1.0 + 0.1 * math.cos(m) for m in range(2, H + 1)}
    W = sum(weights.values())
    Z = P + H
    direct_source = sum(w * von_mangoldt(P + m) for m, w in weights.items())

    divisor_source = 0.0
    zero_mode = 0.0
    nonzero_direct = 0.0
    large_one_point_error = 0.0
    for d in range(1, Z + 1):
        coeff = -float(mobius(d)) * math.log(d)
        if coeff == 0.0:
            continue
        incidence = sum(w for m, w in weights.items() if (P + m) % d == 0)
        divisor_source += coeff * incidence
        zero_mode += coeff * W / d
        nonzero_direct += coeff * (incidence - W / d)
        if d > H:
            q = (P + d - 1) // d
            routed_m = d * q - P
            routed = weights.get(routed_m, 0.0)
            large_one_point_error = max(large_one_point_error, abs(incidence - routed))

    universal_max_error = 0.0
    for n in range(2, 5001):
        got = -sum(float(mobius(d)) * math.log(int(d)) for d in divisors(n))
        universal_max_error = max(universal_max_error, abs(got - von_mangoldt(n)))

    completion_error = 0.0
    for d in range(2, min(40, Z) + 1):
        direct = sum(w for m, w in weights.items() if (P + m) % d == 0)
        completion_error = max(completion_error, abs(direct - fourier_incidence(P, H, d, weights)))

    return {
        "P": P, "H": H, "Z": Z,
        "direct_source": direct_source,
        "divisor_source": divisor_source,
        "source_error": abs(direct_source - divisor_source),
        "centred_reconstruction_error": abs(direct_source - zero_mode - nonzero_direct),
        "universal_max_error": universal_max_error,
        "completion_error": completion_error,
        "large_one_point_error": large_one_point_error,
        "zero_mode_over_weight": zero_mode / W,
    }


def main() -> None:
    rows = [one_case(10007, 10), one_case(20011, 12), one_case(50021, 14)]
    for row in rows:
        assert row["source_error"] < 2e-10, row
        assert row["centred_reconstruction_error"] < 2e-10, row
        assert row["universal_max_error"] < 2e-11, row
        assert row["completion_error"] < 2e-10, row
        assert row["large_one_point_error"] < 2e-12, row
    payload = {
        "status": "PASS",
        "scope": "minimal Möbius-log source, principal subtraction and large-column routing",
        "rows": rows,
        "boundary": "Exact finite identities only; signed variance estimate remains open.",
    }
    Path(__file__).with_name("mobius_log_single_column_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
