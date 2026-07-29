#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def primes_upto(n: int) -> list[int]:
    out: list[int] = []
    for x in range(2, n + 1):
        is_prime = True
        for p in out:
            if p * p > x:
                break
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            out.append(x)
    return out


def local_xi(prime: int, coordinate: int) -> Fraction:
    return Fraction(-1) if coordinate % prime == 1 else Fraction(1, prime - 2)


def exact_identification_panel() -> dict:
    cutoff = 11
    band_primes = [13, 17, 19]
    centres = [30, 210, 2310]
    betas = [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13)]
    source_primes = [p for p in primes_upto(97) if p > cutoff]

    rows = []
    local_energy = Fraction(0)
    established_diagonal = Fraction(0)

    for centre, beta in zip(centres, betas, strict=True):
        for prime in band_primes:
            ordinary_sources = [m for m in source_primes if m != prime]
            centre_inverse = pow(centre, -1, prime)

            low_mode_discrepancy = sum(
                (
                    beta
                    * local_xi(prime, (-m * centre_inverse) % prime)
                    for m in ordinary_sources
                ),
                Fraction(0),
            )

            residue_count = sum(
                1 for m in ordinary_sources if (centre + m) % prime == 0
            )
            frozen_discrepancy = (
                Fraction(residue_count)
                - Fraction(len(source_primes) - 1, prime - 1)
            )
            same_band_coordinate = (
                beta
                * Fraction(prime - 1, prime - 2)
                * frozen_discrepancy
            )

            assert low_mode_discrepancy == -same_band_coordinate

            local_energy += low_mode_discrepancy * low_mode_discrepancy
            established_diagonal += same_band_coordinate * same_band_coordinate

            rows.append(
                {
                    "centre": centre,
                    "prime": prime,
                    "beta": str(beta),
                    "ordinary_source_count": len(ordinary_sources),
                    "residue_count": residue_count,
                    "one_residue_low_mode": str(low_mode_discrepancy),
                    "same_band_coordinate": str(same_band_coordinate),
                    "sum": str(low_mode_discrepancy + same_band_coordinate),
                }
            )

    assert local_energy == established_diagonal

    return {
        "cutoff": cutoff,
        "band_primes": band_primes,
        "centres": centres,
        "source_prime_count": len(source_primes),
        "coordinate_checks": len(rows),
        "rows": rows,
        "low_mode_diagonal_energy": str(local_energy),
        "same_band_diagonal_energy": str(established_diagonal),
        "status": "PASS",
    }


def later_weight_qualification() -> dict:
    centre = 30
    prime = 13
    source_primes = [p for p in primes_upto(59) if p > 11]
    centre_inverse = pow(centre, -1, prime)

    weights = {
        m: Fraction((m % 7) + 1, (m % 5) + 2)
        for m in source_primes
        if m != prime
    }

    weighted_low_mode = sum(
        (
            weight * local_xi(prime, (-m * centre_inverse) % prime)
            for m, weight in weights.items()
        ),
        Fraction(0),
    )

    constant_weight = Fraction(3, 5)
    constant_low_mode = sum(
        (
            constant_weight
            * local_xi(prime, (-m * centre_inverse) % prime)
            for m in source_primes
            if m != prime
        ),
        Fraction(0),
    )
    residue_count = sum(
        1
        for m in source_primes
        if m != prime and (centre + m) % prime == 0
    )
    constant_same_band = (
        constant_weight
        * Fraction(prime - 1, prime - 2)
        * (
            Fraction(residue_count)
            - Fraction(len(source_primes) - 1, prime - 1)
        )
    )
    assert constant_low_mode == -constant_same_band

    return {
        "centre": centre,
        "prime": prime,
        "nonconstant_weighted_low_mode": str(weighted_low_mode),
        "constant_weight_identification_check": str(
            constant_low_mode + constant_same_band
        ),
        "qualification": (
            "The exact identification with the established frozen diagonal uses "
            "the actual constant source weight beta_j on the first physical band. "
            "A later-band survivor-weighted extension is a different theorem."
        ),
        "status": "PASS",
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "first_band_low_mode_equals_existing_diagonal": (
                exact_identification_panel()
            ),
            "later_weight_qualification": later_weight_qualification(),
        },
        "boundary": (
            "For the frozen first physical band, the proposed SW1BDH diagonal is "
            "exactly the already-established same-band diagonal coordinate, with "
            "opposite sign. The open theorem is the coherent square of the sum "
            "over physical primes, not the sum of the individual squares. Later "
            "bands carrying previous-survivor weights remain distinct."
        ),
    }
    output = Path(__file__).with_name(
        "single_prime_diagonal_consistency_results.json"
    )
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
