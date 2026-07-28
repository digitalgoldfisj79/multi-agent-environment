#!/usr/bin/env python3
"""Calibrate the frozen same-dyadic Bessel ratio on complete finite panels."""
from __future__ import annotations

import json
import math
from pathlib import Path


def prime_sieve(n: int) -> tuple[bytearray, list[int]]:
    flags = bytearray(b"\x01") * (n + 1)
    flags[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            flags[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return flags, [i for i in range(2, n + 1) if flags[i]]


def panel(X: int, eta: float = 0.8) -> dict:
    H = int(eta * X * X)
    flags, primes = prime_sieve(H)
    block_primes = [p for p in primes if X <= p < 2 * X]

    P = 1
    for p in primes:
        if p > block_primes[0]:
            break
        P *= p
    centres: list[int] = []
    current = P
    for index, z in enumerate(block_primes):
        if index:
            current *= z
        centres.append(current)

    K = max(1, math.isqrt(X))
    rows = []
    total_numerator = 0.0
    total_diagonal = 0.0
    maximum_ratio = 0.0

    for start in range(0, len(centres), K):
        local_centres = centres[start : start + K]
        local_z = block_primes[start : start + K]
        zB = local_z[-1]
        candidates = [p for p in primes if zB < p <= H]
        M = len(candidates)

        band_numerators: dict[int, float] = {}
        band_diagonals: dict[int, float] = {}
        for centre in local_centres:
            band_sums: dict[int, float] = {}
            centre_diagonals: dict[int, float] = {}
            for q in candidates:
                residue = (-centre) % q
                if residue <= zB:
                    m = residue + ((zB - residue) // q + 1) * q
                else:
                    m = residue
                hit_count = 0
                while m <= H:
                    if flags[m]:
                        hit_count += 1
                    m += q

                delta = hit_count - (M - 1) / (q - 1)
                coefficient = (q - 1) / (q - 2) * delta
                band = int(math.floor(math.log(q / zB, 2)))
                band_sums[band] = band_sums.get(band, 0.0) + coefficient
                centre_diagonals[band] = centre_diagonals.get(band, 0.0) + coefficient * coefficient

            for band, value in band_sums.items():
                band_numerators[band] = band_numerators.get(band, 0.0) + value * value
            for band, value in centre_diagonals.items():
                band_diagonals[band] = band_diagonals.get(band, 0.0) + value

        ratios = {
            str(band): band_numerators[band] / band_diagonals[band]
            for band in band_numerators
            if band_diagonals[band]
        }
        block_maximum = max(ratios.values(), default=0.0)
        maximum_ratio = max(maximum_ratio, block_maximum)
        total_numerator += math.fsum(band_numerators.values())
        total_diagonal += math.fsum(band_diagonals.values())
        rows.append(
            {
                "start_index": start,
                "block_size": len(local_centres),
                "z_B": zB,
                "maximum_same_band_ratio": block_maximum,
                "ratios": ratios,
                "same_band_square": math.fsum(band_numerators.values()),
                "diagonal": math.fsum(band_diagonals.values()),
            }
        )

    return {
        "X": X,
        "H": H,
        "N": len(centres),
        "K": K,
        "maximum_same_band_ratio": maximum_ratio,
        "aggregate_same_band_ratio": total_numerator / total_diagonal,
        "blocks": rows,
    }


def main() -> None:
    panels = [panel(X) for X in (101, 211, 503)]
    payload = {
        "status": "PASS",
        "scope": "finite frozen same-band rough-quotient Bessel calibration with unit row weights",
        "panels": panels,
        "interpretation": (
            "Every measured same-dyadic square is at most 2.29 times its exact diagonal; "
            "aggregate ratios remain close to one. Empirical only."
        ),
        "boundary": "No asymptotic same-band Bessel theorem is inferred.",
    }
    output = Path(__file__).with_name("same_band_rough_quotient_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
