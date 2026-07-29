#!/usr/bin/env python3
"""Exact audit of the primorial-shift Titchmarsh compression and the first-band all-order interface."""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def primorial_to(z: int, primes: list[int]) -> int:
    value = 1
    for p in primes:
        if p > z:
            break
        value *= p
    return value


def panel(X: int, eta_num: int = 4, eta_den: int = 5) -> dict:
    H = eta_num * X * X // eta_den
    primes = primes_upto(H)
    z_values = [p for p in primes if X <= p < 2 * X]
    K = max(1, math.isqrt(X))
    centres = z_values[:K]
    Z = centres[-1]
    sources = [p for p in primes if Z < p <= H]
    moduli = [p for p in sources if p <= min(2 * Z, H)]
    source_count = len(sources)

    lambda_R = sum((Fraction(1, p - 2) for p in moduli), Fraction(0))
    V_R = Fraction(1)
    for p in moduli:
        V_R *= Fraction(p - 2, p - 1)
    inverse_V_R = 1 / V_R

    same_band_lhs = Fraction(0)
    same_band_diagonal = Fraction(0)
    first_order_energy = Fraction(0)
    full_band_energy = Fraction(0)
    correction_energy = Fraction(0)
    first_correction_cross = Fraction(0)
    pair_residue_candidates_total = 0
    prime_pair_hits_total = 0
    rows = []

    for z in centres:
        P = primorial_to(z, primes)
        counts: dict[int, int] = {}
        coordinates: dict[int, Fraction] = {}

        for p in moduli:
            direct = sum(1 for m in sources if m != p and (P + m) % p == 0)
            included = sum(1 for m in sources if (P + m) % p == 0)
            # The self source m=p never hits because p does not divide P.
            assert direct == included
            counts[p] = direct
            coordinates[p] = Fraction(p - 1, p - 2) * (
                Fraction(direct) - Fraction(source_count - 1, p - 1)
            )

        same_band_sum = sum(coordinates.values(), Fraction(0))
        weighted_divisor_sum = Fraction(0)
        first_order_sum = Fraction(0)
        full_band_sum = Fraction(0)
        hit_multiplicities: list[int] = []

        for m in sources:
            hit_primes: list[int] = []
            weighted_hits = Fraction(0)
            local_product = Fraction(1)
            for p in moduli:
                hit = (P + m) % p == 0
                if hit:
                    hit_primes.append(p)
                    weighted_hits += Fraction(p - 1, p - 2)
                    xi = Fraction(-1)
                else:
                    xi = Fraction(1, p - 2)
                first_order_sum += xi
                local_product *= 1 + xi

            weighted_divisor_sum += weighted_hits
            full_band_sum += local_product - 1
            hit_multiplicities.append(len(hit_primes))

        # Exact primorial-shift Titchmarsh compression.
        assert same_band_sum == weighted_divisor_sum - Fraction(source_count - 1) * lambda_R

        # Exact self/zeroth drift relation.
        assert first_order_sum == lambda_R - same_band_sum

        union_hits = sum(1 for multiplicity in hit_multiplicities if multiplicity > 0)
        assert full_band_sum == inverse_V_R * Fraction(source_count - union_hits) - source_count

        higher_order_correction = full_band_sum - first_order_sum
        correction_formula = (
            (inverse_V_R - 1 - lambda_R) * source_count
            + sum(
                (
                    sum(
                        Fraction(p - 1, p - 2)
                        for p in moduli
                        if (P + m) % p == 0
                    )
                    - inverse_V_R
                )
                for m, multiplicity in zip(sources, hit_multiplicities, strict=True)
                if multiplicity > 0
            )
        )
        assert higher_order_correction == correction_formula

        pair_incidence_count = sum(
            multiplicity * (multiplicity - 1) // 2
            for multiplicity in hit_multiplicities
        )
        extra_hits = sum(max(multiplicity - 1, 0) for multiplicity in hit_multiplicities)
        assert extra_hits <= pair_incidence_count <= math.comb(len(moduli), 2)

        pair_residue_candidates = 0
        prime_pair_hits = 0
        for index, p in enumerate(moduli):
            for s in moduli[index + 1 :]:
                Q = p * s
                assert Q > H

                integers = [m for m in range(Z + 1, H + 1) if (P + m) % Q == 0]
                assert len(integers) <= 1

                # Unique representative of -P mod Q in (Z, Z+Q].
                candidate = Z + 1 + ((-P - (Z + 1)) % Q)
                if candidate <= H:
                    assert integers == [candidate]
                    pair_residue_candidates += 1
                    if candidate in sources:
                        prime_pair_hits += 1
                else:
                    assert not integers

        assert prime_pair_hits == pair_incidence_count

        row_diagonal = sum((value * value for value in coordinates.values()), Fraction(0))
        same_band_lhs += same_band_sum * same_band_sum
        same_band_diagonal += row_diagonal
        first_order_energy += first_order_sum * first_order_sum
        full_band_energy += full_band_sum * full_band_sum
        correction_energy += higher_order_correction * higher_order_correction
        first_correction_cross += 2 * first_order_sum * higher_order_correction
        pair_residue_candidates_total += pair_residue_candidates
        prime_pair_hits_total += prime_pair_hits

        rows.append(
            {
                "z": z,
                "same_band_sum": str(same_band_sum),
                "first_order_sum": str(first_order_sum),
                "full_band_sum": str(full_band_sum),
                "higher_order_correction": str(higher_order_correction),
                "union_hits": union_hits,
                "pair_incidence_count": pair_incidence_count,
                "pair_residue_candidates": pair_residue_candidates,
                "prime_pair_hits": prime_pair_hits,
                "max_hit_multiplicity": max(hit_multiplicities, default=0),
            }
        )

    assert full_band_energy == first_order_energy + correction_energy + first_correction_cross

    return {
        "X": X,
        "H": H,
        "K": K,
        "centres": centres,
        "Z": Z,
        "source_count": source_count,
        "first_band_moduli": moduli,
        "modulus_count": len(moduli),
        "product_above_source_length": all(
            p * s > H
            for index, p in enumerate(moduli)
            for s in moduli[index + 1 :]
        ),
        "abstract_pair_saturation_fits_source_capacity": math.comb(len(moduli), 2)
        <= source_count,
        "same_band_lhs": str(same_band_lhs),
        "same_band_diagonal": str(same_band_diagonal),
        "same_band_ratio": float(same_band_lhs / same_band_diagonal)
        if same_band_diagonal
        else 0.0,
        "first_order_energy": str(first_order_energy),
        "full_band_energy": str(full_band_energy),
        "correction_energy": str(correction_energy),
        "first_correction_cross": str(first_correction_cross),
        "pair_residue_candidates_total": pair_residue_candidates_total,
        "prime_pair_hits_total": prime_pair_hits_total,
        "rows": rows,
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "panels": [panel(X) for X in (11, 17, 23, 29, 37)],
        },
        "boundary": (
            "The first physical same-band sum is exactly a centred weighted truncated "
            "Titchmarsh divisor sum with primorial shift. Recombining all Euler orders "
            "turns every order at least two into a one-point shrinking-target test because "
            "the product of two first-band primes exceeds H. Pair injectivity alone permits "
            "quadratically many incidences and is therefore not a Fortune-scale estimate. "
            "MRPMD/SBD and the signed semiprime interface remain open."
        ),
    }
    output = Path(__file__).with_name("primorial_shift_titchmarsh_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
