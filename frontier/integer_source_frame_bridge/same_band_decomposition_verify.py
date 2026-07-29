#!/usr/bin/env python3
"""Exact finite audit of the frozen rough-quotient and dyadic same-band decomposition."""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import divisors, mobius, primerange


def primorial(z: int) -> int:
    value = 1
    for p in primerange(2, z + 1):
        value *= int(p)
    return value


def rough_quotient_count(P: int, Z: int, H: int, q: int) -> int:
    lo = (P + Z) // q + 1
    hi = (P + H) // q
    return sum(1 for k in range(lo, hi + 1) if math.gcd(k, P) == 1)


def mobius_floor_count(P: int, Z: int, H: int, q: int) -> int:
    return sum(
        int(mobius(d)) * ((P + H) // (q * d) - (P + Z) // (q * d))
        for d in map(int, divisors(P))
    )


def dyadic_bands(Z: int, H: int, moduli: list[int]) -> list[dict]:
    bands: list[dict] = []
    low = Z
    index = 0
    covered: list[int] = []
    while low < H:
        high = min(2 * low, H)
        members = [q for q in moduli if low < q <= high]
        bands.append({"index": index, "low_open": low, "high_closed": high, "moduli": members})
        covered.extend(members)
        low = high
        index += 1
    assert covered == moduli
    return bands


def panel(X: int, eta_num: int = 4, eta_den: int = 5) -> dict:
    H = eta_num * X * X // eta_den
    z_values = [int(p) for p in primerange(X, 2 * X)]
    K = max(1, math.isqrt(X))
    blocks = []
    global_max_ratio = 0.0

    for start in range(0, len(z_values), K):
        local_z = z_values[start : start + K]
        Z = local_z[-1]
        candidates = [int(p) for p in primerange(Z + 1, H + 1)]
        M = len(candidates)
        bands = dyadic_bands(Z, H, candidates)

        rows = []
        full_energy = Fraction(0)
        band_energy_sum = Fraction(0)
        diagonal_total = Fraction(0)

        for z in local_z:
            P = primorial(z)
            entries: dict[int, Fraction] = {}
            direct_entries: dict[int, int] = {}
            for q in candidates:
                direct = sum(1 for m in candidates if (P + m) % q == 0)
                quotient = rough_quotient_count(P, Z, H, q)
                floor_value = mobius_floor_count(P, Z, H, q)
                assert direct == quotient == floor_value
                direct_entries[q] = direct
                delta = Fraction(quotient, 1) - Fraction(M - 1, q - 1)
                entries[q] = Fraction(q - 1, q - 2) * delta

            full_sum = sum(entries.values(), Fraction(0))
            band_sums = [sum((entries[q] for q in band["moduli"]), Fraction(0)) for band in bands]
            assert full_sum == sum(band_sums, Fraction(0))

            row_full_energy = full_sum * full_sum
            row_band_energy = sum((value * value for value in band_sums), Fraction(0))
            row_diagonal = sum((value * value for value in entries.values()), Fraction(0))
            full_energy += row_full_energy
            band_energy_sum += row_band_energy
            diagonal_total += row_diagonal

            rows.append(
                {
                    "z": z,
                    "P": P,
                    "full_sum_num": full_sum.numerator,
                    "full_sum_den": full_sum.denominator,
                    "direct_total_hits": sum(direct_entries.values()),
                    "band_sums": [
                        {"num": value.numerator, "den": value.denominator} for value in band_sums
                    ],
                }
            )

        L = len(bands)
        assert full_energy <= L * band_energy_sum

        band_records = []
        for band in bands:
            lhs = Fraction(0)
            diagonal = Fraction(0)
            for z in local_z:
                P = primorial(z)
                row_values = []
                for q in band["moduli"]:
                    N = rough_quotient_count(P, Z, H, q)
                    delta = Fraction(N, 1) - Fraction(M - 1, q - 1)
                    row_values.append(Fraction(q - 1, q - 2) * delta)
                row_sum = sum(row_values, Fraction(0))
                lhs += row_sum * row_sum
                diagonal += sum((value * value for value in row_values), Fraction(0))
            ratio = float(lhs / diagonal) if diagonal else 0.0
            global_max_ratio = max(global_max_ratio, ratio)
            band_records.append(
                {
                    "index": band["index"],
                    "low_open": band["low_open"],
                    "high_closed": band["high_closed"],
                    "modulus_count": len(band["moduli"]),
                    "lhs_num": lhs.numerator,
                    "lhs_den": lhs.denominator,
                    "diagonal_num": diagonal.numerator,
                    "diagonal_den": diagonal.denominator,
                    "empirical_lhs_to_diagonal_ratio": ratio,
                }
            )

        blocks.append(
            {
                "start_index": start,
                "block_size": len(local_z),
                "Z": Z,
                "candidate_count": M,
                "band_count": L,
                "outer_cauchy_exact": True,
                "full_energy_num": full_energy.numerator,
                "full_energy_den": full_energy.denominator,
                "band_energy_sum_num": band_energy_sum.numerator,
                "band_energy_sum_den": band_energy_sum.denominator,
                "diagonal_total_num": diagonal_total.numerator,
                "diagonal_total_den": diagonal_total.denominator,
                "rows": rows,
                "bands": band_records,
            }
        )

    return {
        "X": X,
        "H": H,
        "K": K,
        "centre_count": len(z_values),
        "maximum_empirical_same_band_ratio": global_max_ratio,
        "blocks": blocks,
    }


def main() -> None:
    panels = [panel(X) for X in (7, 11, 13, 17)]
    payload = {
        "status": "PASS",
        "scope": (
            "general-cutoff quotient bijection, Mobius-floor identity, exact dyadic partition, "
            "same-band recombination and outer Cauchy"
        ),
        "panels": panels,
        "boundary": (
            "The same-band ratios are empirical diagnostics only. The uniform same-band Bessel "
            "estimate and Fortune's conjecture remain OPEN."
        ),
    }
    output = Path(__file__).with_name("same_band_decomposition_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
