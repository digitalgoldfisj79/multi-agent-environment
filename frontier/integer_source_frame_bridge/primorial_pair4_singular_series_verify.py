#!/usr/bin/env python3
"""Verify local pair-of-pairs factors and finite truncated averages."""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import primerange

ETA = 0.8
TARGETS = (7, 11, 17, 23)
TRUNCATION_MULTIPLE = 4


def local_ratio(p: int, P: int, h: int) -> Fraction:
    nu2 = len({0, P % p})
    nu4 = len({0, P % p, h % p, (P + h) % p})
    pair = Fraction(p - nu2, p) / Fraction(p - 1, p) ** 2
    four = Fraction(p - nu4, p) / Fraction(p - 1, p) ** 4
    return four / pair**2


def exact_local_checks() -> list[dict]:
    rows = []
    for p in primerange(2, 100):
        p = int(p)
        # Dividing-P case.
        P0 = p
        values0 = [local_ratio(p, P0, h) for h in range(p)]
        mean0 = sum(values0, Fraction(0, 1)) / p
        assert mean0 == 1
        if p == 2:
            assert values0 == [Fraction(2, 1), Fraction(0, 1)]
        else:
            assert values0[0] == Fraction(p, p - 1)
            assert all(v == Fraction(p * (p - 2), (p - 1) ** 2) for v in values0[1:])

        # Nondividing-P case; only relevant for p>2.
        mean1 = None
        if p > 2:
            P1 = 1
            values1 = [local_ratio(p, P1, h) for h in range(p)]
            mean1 = sum(values1, Fraction(0, 1)) / p
            assert mean1 == 1
            assert values1[0] == Fraction(p, p - 2)
            assert values1[1] == Fraction(p * (p - 3), (p - 2) ** 2)
            assert values1[p - 1] == Fraction(p * (p - 3), (p - 2) ** 2)
            generic = Fraction(p * (p - 4), (p - 2) ** 2)
            assert all(values1[h] == generic for h in range(2, p - 1))

        rows.append(
            {
                "p": p,
                "dividing_P_mean": [mean0.numerator, mean0.denominator],
                "nondividing_P_mean": (
                    [mean1.numerator, mean1.denominator] if mean1 is not None else None
                ),
            }
        )
    return rows


def truncated_average(X: int) -> dict:
    P = 1
    for p in primerange(2, X + 1):
        P *= int(p)
    H = int(ETA * X * X)
    cutoff = TRUNCATION_MULTIPLE * H
    primes = [int(p) for p in primerange(2, cutoff + 1)]

    weighted_sum = 0.0
    total_weight = 0
    for h in range(-(H - 1), H):
        if h == 0:
            continue
        weight = H - abs(h)
        ratio = 1.0
        for p in primes:
            ratio *= float(local_ratio(p, P, h))
        weighted_sum += weight * ratio
        total_weight += weight

    relative_to_H2 = weighted_sum / (H * H)
    error = abs(relative_to_H2 - 1.0)
    scale = math.log(X) / H
    return {
        "X": X,
        "H": H,
        "primorial_digits": len(str(P)),
        "prime_cutoff": cutoff,
        "primes_in_truncation": len(primes),
        "total_nonzero_triangular_weight": total_weight,
        "normalised_truncated_average": relative_to_H2,
        "absolute_error_from_one": error,
        "logX_over_H": scale,
        "error_divided_by_logX_over_H": error / scale,
    }


def main() -> None:
    local = exact_local_checks()
    averages = [truncated_average(X) for X in TARGETS]
    for row in averages:
        assert row["absolute_error_from_one"] < 5 * row["logX_over_H"]

    payload = {
        "status": "PASS",
        "scope": "exact local mean-one identities and finite truncated triangular averages",
        "parameters": {
            "eta": ETA,
            "targets": list(TARGETS),
            "prime_truncation_multiple_of_H": TRUNCATION_MULTIPLE,
        },
        "local_checks": local,
        "truncated_averages": averages,
        "boundary": (
            "The finite truncated averages validate the local formulas only. "
            "The asymptotic full-product theorem is proved analytically in the note."
        ),
    }
    path = Path(__file__).with_name("primorial_pair4_singular_series_results.json")
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
