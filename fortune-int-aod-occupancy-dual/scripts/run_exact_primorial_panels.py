#!/usr/bin/env python3
"""Exact small-panel diagnostics for the INT-AOD occupancy programme.

These computations are diagnostic only. They use actual primorial centres p#,
prime candidate offsets m in (p,H], and exact primality testing through sympy.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from sympy import isprime, primerange


def falling(z: int, k: int) -> int:
    out = 1
    for r in range(k):
        out *= z - r
    return out


def factorial_cumulants(values: list[int], order: int) -> tuple[list[float], list[float]]:
    n = len(values)
    moments = [1.0]
    for k in range(1, order + 1):
        moments.append(sum(falling(z, k) for z in values) / n)
    cumulants = [0.0] * (order + 1)
    for k in range(1, order + 1):
        subtotal = 0.0
        for r in range(1, k):
            subtotal += math.comb(k - 1, r - 1) * cumulants[r] * moments[k - r]
        cumulants[k] = moments[k] - subtotal
    return moments, cumulants


def pgf(values: list[int], q: float) -> float:
    return sum((1.0 - q) ** z for z in values) / len(values)


def q_polynomial_coeffs(values: list[int]) -> np.ndarray:
    """Coefficients c_k of G(1-q)=sum c_k q^k in ascending order."""
    degree = max(values, default=0)
    coeffs = np.zeros(degree + 1, dtype=float)
    for z in values:
        for k in range(z + 1):
            coeffs[k] += ((-1.0) ** k) * math.comb(z, k)
    coeffs /= len(values)
    return coeffs


def nearest_zero_modulus(values: list[int]) -> float | None:
    coeffs = q_polynomial_coeffs(values)
    while len(coeffs) > 1 and abs(coeffs[-1]) < 1e-14:
        coeffs = coeffs[:-1]
    if len(coeffs) <= 1:
        return None
    roots = np.roots(coeffs[::-1])
    if len(roots) == 0:
        return None
    return float(min(abs(r) for r in roots))


def panel(x: int, eta: float, cumulant_order: int) -> dict:
    h = int(math.floor(eta * x * x))
    block_primes = list(primerange(x, 2 * x))
    all_primes_to_2x = list(primerange(2, 2 * x))
    primorial = 1
    prime_to_primorial: dict[int, int] = {}
    for p in all_primes_to_2x:
        primorial *= p
        if p in block_primes:
            prime_to_primorial[p] = primorial

    rows = []
    occupancies: list[int] = []
    column_degrees: Counter[int] = Counter()
    candidate_union = sorted(set(primerange(min(block_primes) + 1, h + 1))) if block_primes else []

    for ell in block_primes:
        candidates = list(primerange(ell + 1, h + 1))
        centre = prime_to_primorial[ell]
        hits = [m for m in candidates if isprime(centre + m)]
        occupancies.append(len(hits))
        for m in hits:
            column_degrees[m] += 1
        rows.append(
            {
                "ell": ell,
                "centre_digits": len(str(centre)),
                "candidate_count": len(candidates),
                "occupancy": len(hits),
                "first_hits": hits[:12],
            }
        )

    n = len(rows)
    if n == 0:
        raise RuntimeError(f"empty block at X={x}")
    mean = sum(occupancies) / n
    max_order = min(cumulant_order, max(occupancies, default=0))
    moments, cumulants = factorial_cumulants(occupancies, max_order)

    logn = math.log(n)
    q_choices = {
        "q_logN_over_mean": min(0.95, logn / mean) if mean > 0 else 0.95,
        "q_2logN_over_mean": min(0.95, 2.0 * logn / mean) if mean > 0 else 0.95,
        "q_0_1": 0.1,
        "q_0_25": 0.25,
        "q_0_5": 0.5,
    }
    detector = {}
    for name, q in q_choices.items():
        g = pgf(occupancies, q)
        detector[name] = {
            "q": q,
            "sum": n * g,
            "minus_log_mean_pgf": -math.log(g),
            "first_connected_term": q * cumulants[1] if max_order >= 1 else 0.0,
            "truncated_abs_connected_remainder": sum(
                (q**k) * abs(cumulants[k]) / math.factorial(k)
                for k in range(2, max_order + 1)
            ),
        }

    degree_hist = Counter(column_degrees.values())
    overlap_pairs = 0
    hit_sets = []
    for row in rows:
        centre = prime_to_primorial[row["ell"]]
        hits = {m for m in primerange(row["ell"] + 1, h + 1) if isprime(centre + m)}
        hit_sets.append(hits)
    pair_overlaps = []
    for i in range(n):
        for j in range(i + 1, n):
            ov = len(hit_sets[i] & hit_sets[j])
            pair_overlaps.append(ov)
            overlap_pairs += ov

    return {
        "X": x,
        "eta": eta,
        "H": h,
        "row_count": n,
        "candidate_union_count": len(candidate_union),
        "occupancy_histogram": dict(sorted(Counter(occupancies).items())),
        "minimum_occupancy": min(occupancies),
        "maximum_occupancy": max(occupancies),
        "mean_occupancy": mean,
        "zero_rows": sum(z == 0 for z in occupancies),
        "factorial_moments": moments,
        "factorial_cumulants": cumulants,
        "nearest_q_zero_modulus_numeric": nearest_zero_modulus(occupancies),
        "detectors": detector,
        "column_count_with_hits": len(column_degrees),
        "column_degree_histogram": dict(sorted(degree_hist.items())),
        "pair_overlap_total": overlap_pairs,
        "pair_overlap_max": max(pair_overlaps, default=0),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", nargs="+", type=int, default=[10, 20, 30, 50, 75, 100])
    parser.add_argument("--eta", type=float, default=0.5)
    parser.add_argument("--cumulant-order", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    results = [panel(x, args.eta, args.cumulant_order) for x in args.x]
    payload = {"programme": "FORTUNE_INT_AOD_OCCUPANCY_DUAL_V0_1", "panels": results}
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text)
    print("FORTUNE_INT_AOD_EXACT_PANEL_JSON_BEGIN")
    print(text)
    print("FORTUNE_INT_AOD_EXACT_PANEL_JSON_END")
    print("FORTUNE_INT_AOD_O8_EXACT_PANEL_PASS")


if __name__ == "__main__":
    main()
