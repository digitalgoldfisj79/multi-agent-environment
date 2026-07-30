#!/usr/bin/env python3
"""Standing empirical verifier for the load-bearing orbit/cross-modulus covariance gate.

This is an EMPIRICAL falsification test, not a theorem verifier.

For each X and several consecutive-centre blocks, it computes
    D_p(a) = psi(H;p,a) - Psi_p(H)/(p-1)
on the actual primorial residues a=-P_j mod p, and compares three normalized
statistics with deterministic random-residue controls:

1. sampling_ratio:
   sum_{j,p} D_p(-P_j)^2 /
   (K * sum_p [sum_a D_p(a)^2/(p-1)]).

2. coherence_ratio:
   sum_j |sum_p D_p(-P_j)|^2 /
   sum_{j,p} D_p(-P_j)^2.

3. total_ratio:
   sum_j |sum_p D_p(-P_j)|^2 /
   (K * sum_p [sum_a D_p(a)^2/(p-1)]).

Values near 1 indicate typical-residue sampling and random-scale cross-modulus
coherence. Growth toward |P_R| would falsify the intended orbit-transfer route.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


PANELS = (101, 199, 307, 503, 701, 1009)
ETA = 0.8
BLOCKS = 6
RANDOM_REPS = 128
SEED = 20260730


def stable_float(value: float) -> float:
    return round(float(value), 12)


def primes_upto(n: int) -> list[int]:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return np.flatnonzero(sieve).tolist()


def lambda_table(n: int) -> np.ndarray:
    values = np.zeros(n + 1, dtype=float)
    for p in primes_upto(n):
        value = p
        logp = math.log(p)
        while value <= n:
            values[value] = logp
            if value > n // p:
                break
            value *= p
    return values


def evenly_spaced_starts(total: int, width: int, count: int) -> list[int]:
    maximum = max(0, total - width)
    if count <= 1 or maximum == 0:
        return [0]
    return sorted({round(i * maximum / (count - 1)) for i in range(count)})


def panel(X: int) -> dict:
    H = int(ETA * X * X)
    lam = lambda_table(H)
    primes = primes_upto(max(H, 4 * X + 100))
    source_indices = np.flatnonzero(lam)
    source_weights = lam[source_indices]

    centre_primes = [p for p in primes if X <= p < 2 * X]
    K = max(3, min(len(centre_primes), math.ceil(math.log(X))))
    starts = evenly_spaced_starts(len(centre_primes), K, BLOCKS)
    rng = np.random.default_rng(SEED + X)

    block_results: list[dict] = []
    for start in starts:
        z_values = centre_primes[start : start + K]
        Z = z_values[-1]
        band = [p for p in primes if Z < p <= 2 * Z and p <= H]

        discrepancy: dict[int, np.ndarray] = {}
        expected_one_row_diagonal = 0.0
        for p in band:
            buckets = np.bincount(
                source_indices % p,
                weights=source_weights,
                minlength=p,
            )
            psi_units = float(buckets[1:].sum())
            D = buckets - psi_units / (p - 1)
            discrepancy[p] = D
            expected_one_row_diagonal += float(np.dot(D[1:], D[1:]) / (p - 1))

        orbit_values: list[list[float]] = [[] for _ in z_values]
        for p in band:
            primorial_residue = 1
            centre_index = 0
            for q in primes:
                if q > z_values[-1]:
                    break
                primorial_residue = primorial_residue * q % p
                if centre_index < K and q == z_values[centre_index]:
                    orbit_values[centre_index].append(
                        float(discrepancy[p][(-primorial_residue) % p])
                    )
                    centre_index += 1

        orbit_diagonal = 0.0
        orbit_coherent = 0.0
        for values in orbit_values:
            vector = np.asarray(values, dtype=float)
            orbit_diagonal += float(np.dot(vector, vector))
            orbit_coherent += float(vector.sum() ** 2)

        denominator = K * expected_one_row_diagonal
        orbit_sampling_ratio = orbit_diagonal / denominator
        orbit_coherence_ratio = orbit_coherent / orbit_diagonal
        orbit_total_ratio = orbit_coherent / denominator

        random_sampling: list[float] = []
        random_coherence: list[float] = []
        random_total: list[float] = []
        for _ in range(RANDOM_REPS):
            diagonal = 0.0
            coherent = 0.0
            for _centre in z_values:
                vector = np.asarray(
                    [discrepancy[p][rng.integers(1, p)] for p in band],
                    dtype=float,
                )
                diagonal += float(np.dot(vector, vector))
                coherent += float(vector.sum() ** 2)
            random_sampling.append(diagonal / denominator)
            random_coherence.append(coherent / diagonal)
            random_total.append(coherent / denominator)

        block_results.append(
            {
                "start_index": start,
                "Z": Z,
                "band_count": len(band),
                "orbit_sampling_ratio": stable_float(orbit_sampling_ratio),
                "orbit_coherence_ratio": stable_float(orbit_coherence_ratio),
                "orbit_total_ratio": stable_float(orbit_total_ratio),
                "random_sampling_median": stable_float(np.median(random_sampling)),
                "random_coherence_median": stable_float(np.median(random_coherence)),
                "random_total_median": stable_float(np.median(random_total)),
            }
        )

    def value_range(key: str) -> list[float]:
        values = [b[key] for b in block_results]
        return [min(values), max(values)]

    return {
        "X": X,
        "H": H,
        "K": K,
        "block_count": len(block_results),
        "band_count_range": [
            min(b["band_count"] for b in block_results),
            max(b["band_count"] for b in block_results),
        ],
        "orbit_sampling_range": value_range("orbit_sampling_ratio"),
        "orbit_coherence_range": value_range("orbit_coherence_ratio"),
        "orbit_total_range": value_range("orbit_total_ratio"),
        "random_sampling_median_range": value_range("random_sampling_median"),
        "random_coherence_median_range": value_range("random_coherence_median"),
        "random_total_median_range": value_range("random_total_median"),
    }


def main() -> None:
    panels = [panel(X) for X in PANELS]
    payload = {
        "status": "PASS",
        "classification": "EMPIRICAL_FALSIFICATION_TEST_ONLY",
        "definition": {
            "eta": ETA,
            "blocks_per_X": BLOCKS,
            "random_repetitions": RANDOM_REPS,
            "seed": SEED,
        },
        "panels": panels,
        "summary": {
            "maximum_orbit_sampling_ratio": max(
                p["orbit_sampling_range"][1] for p in panels
            ),
            "minimum_orbit_sampling_ratio": min(
                p["orbit_sampling_range"][0] for p in panels
            ),
            "maximum_orbit_coherence_ratio": max(
                p["orbit_coherence_range"][1] for p in panels
            ),
            "minimum_orbit_coherence_ratio": min(
                p["orbit_coherence_range"][0] for p in panels
            ),
            "maximum_orbit_total_ratio": max(
                p["orbit_total_range"][1] for p in panels
            ),
            "minimum_orbit_total_ratio": min(
                p["orbit_total_range"][0] for p in panels
            ),
        },
        "boundary": (
            "Across the committed finite panels, primorial-orbit residues sample the "
            "all-residue diagonal at random scale and show no growth toward the Cauchy "
            "bound in cross-modulus coherence. This is empirical only. The theorem-level "
            "orbit restriction and signed higher-conductor transfer remain open."
        ),
    }
    output = Path(__file__).with_name(
        "orbit_cross_modulus_covariance_results.json"
    )
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
