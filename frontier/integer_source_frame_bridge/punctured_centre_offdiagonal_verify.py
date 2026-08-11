#!/usr/bin/env python3
"""Exact finite audit of the punctured-centre full-band diagonal and determinant kernel."""
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


def mobius(n: int) -> int:
    x = n
    count = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def primorial(z: int, primes: list[int]) -> int:
    value = 1
    for p in primes:
        if p > z:
            break
        value *= p
    return value


def panel(X: int, eta_num: int = 4, eta_den: int = 5) -> dict:
    H = eta_num * X * X // eta_den
    Y = math.isqrt(H)
    if Y * Y < H:
        Y += 1
    primes = primes_upto(max(H, 3 * X))
    z_values = [p for p in primes if X <= p < 2 * X]
    K = max(1, min(len(z_values), math.ceil(math.log(X))))
    z_values = z_values[:K]
    Z = z_values[-1]
    centres = [primorial(z, primes) for z in z_values]
    band = [p for p in primes if Z < p <= min(2 * Z, H)]
    sources = [p for p in primes if Z < p <= H]
    small = [d for d in range(1, Y + 1) if mobius(d)]

    V = Fraction(1)
    for p in band:
        V *= Fraction(p - 2, p - 1)
    inverse_V = 1 / V
    survivor_value = inverse_V - 1
    assert 0 <= survivor_value < 1

    amplitude_energy = Fraction(0)
    source_diagonal = Fraction(0)
    source_offdiagonal = Fraction(0)
    maximum_row_ratio = 0.0
    punctured_checks = 0
    gram_checks = 0
    one_variable_checks = 0
    determinant_checks = 0
    maximum_fixed_p_multiplicity = 0

    for P in centres:
        values: list[Fraction] = []
        for n in sources:
            survived = all((P + n) % p != 0 for p in band)
            values.append(survivor_value if survived else Fraction(-1))
        amplitude = sum(values, Fraction())
        diagonal = sum((value * value for value in values), Fraction())
        offdiagonal = amplitude * amplitude - diagonal
        amplitude_energy += amplitude * amplitude
        source_diagonal += diagonal
        source_offdiagonal += offdiagonal
        if diagonal:
            maximum_row_ratio = max(maximum_row_ratio, float(amplitude * amplitude / diagonal))

        for d in small:
            assert P % d == 0
            for p in band:
                assert (d * pow(P, -1, p) - pow(P // d, -1, p)) % p == 0
                for m in range(1, Y + 1):
                    assert ((P + d * m) % p == 0) == ((P // d + m) % p == 0)
                    punctured_checks += 1

    for p in band:
        residue_multiplicity: dict[int, int] = {}
        for P in centres:
            for d in small:
                residue = (P // d) % p
                residue_multiplicity[residue] = residue_multiplicity.get(residue, 0) + 1
        maximum_fixed_p_multiplicity = max(
            maximum_fixed_p_multiplicity,
            max(residue_multiplicity.values(), default=0),
        )
        assert maximum_fixed_p_multiplicity <= K

        for P_j in centres:
            for P_k in centres:
                for d in small:
                    for d_prime in small:
                        same_residue = (P_j // d - P_k // d_prime) % p == 0
                        transported = (P_j * d_prime - P_k * d) % p == 0
                        assert same_residue == transported
                        gram_checks += 1

        # The critical balanced cell uses both factors below p.
        for d in range(1, Y + 1):
            if d % p == 0:
                continue
            for m in range(1, Y + 1):
                if m % p == 0:
                    continue
                for m_prime in range(1, Y + 1):
                    collision = (d * m - d * m_prime) % p == 0
                    assert collision == (m == m_prime)
                    one_variable_checks += 1
                for d_prime in range(1, Y + 1):
                    collision = (d * m - d_prime * m) % p == 0
                    assert collision == (d == d_prime)
                    one_variable_checks += 1

        # Exact weighted multiplicative residue energy for the Mobius/Mobius test cell.
        residue_weights = [Fraction(0) for _ in range(p)]
        alpha_total = sum((mobius(d) for d in range(1, Y + 1)), 0)
        gamma_total = alpha_total
        integer_product_diagonal = Fraction(0)
        for d in range(1, Y + 1):
            alpha = mobius(d)
            for m in range(1, Y + 1):
                gamma = mobius(m)
                residue_weights[(d * m) % p] += alpha * gamma
        for d in range(1, Y + 1):
            for m in range(1, Y + 1):
                weight = mobius(d) * mobius(m)
                if not weight:
                    continue
                product = d * m
                multiplicity_weight = sum(
                    mobius(d2) * mobius(m2)
                    for d2 in range(1, Y + 1)
                    for m2 in range(1, Y + 1)
                    if d2 * m2 == product
                )
                integer_product_diagonal += weight * multiplicity_weight

        mean = Fraction(alpha_total * gamma_total, p - 1)
        centred_energy = sum(
            ((residue_weights[a] - mean) ** 2 for a in range(1, p)),
            Fraction(),
        )
        congruence_energy = sum(
            (residue_weights[a] ** 2 for a in range(1, p)),
            Fraction(),
        )
        assert centred_energy == congruence_energy - Fraction(
            (alpha_total * gamma_total) ** 2,
            p - 1,
        )

        for d in range(1, Y + 1):
            for m in range(1, Y + 1):
                for d_prime in range(1, Y + 1):
                    for m_prime in range(1, Y + 1):
                        if d * m == d_prime * m_prime:
                            continue
                        collision_primes = [
                            q for q in band if (d * m - d_prime * m_prime) % q == 0
                        ]
                        assert len(collision_primes) <= 1
                        determinant_checks += 1

    return {
        "X": X,
        "H": H,
        "Y": Y,
        "K": K,
        "Z": Z,
        "source_count": len(sources),
        "band_moduli": band,
        "small_mobius_count": len(small),
        "punctured_centre_checks": punctured_checks,
        "punctured_gram_checks": gram_checks,
        "one_variable_collision_checks": one_variable_checks,
        "generic_determinant_checks": determinant_checks,
        "maximum_fixed_p_residue_multiplicity": maximum_fixed_p_multiplicity,
        "full_band_amplitude_energy": str(amplitude_energy),
        "full_band_source_diagonal": str(source_diagonal),
        "full_band_source_offdiagonal": str(source_offdiagonal),
        "maximum_empirical_row_to_diagonal_ratio": maximum_row_ratio,
        "diagonal_bounded_by_source_count": source_diagonal <= K * len(sources),
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact_scope": [
            "full-band source-product diagonal/off-diagonal split",
            "punctured-centre transport for the one small Mobius variable",
            "punctured-centre Gram collision transport",
            "one-variable collision strata reduce to the source diagonal",
            "generic collision kernel p divides dm-d'm'",
            "weighted multiplicative residue-energy identity",
        ],
        "panels": [panel(X) for X in (11, 17, 23)],
        "boundary": (
            "The complete source diagonal is Fortune-admissible.  In balanced cells below the "
            "first-band moduli, the one-variable collision strata contain only the removed product "
            "diagonal.  The remaining low-mode arithmetic is the genuinely off-diagonal weighted "
            "multiplicative congruence p | dm-d'm', followed by coherent cross-modulus and high-order "
            "survivor recombination."
        ),
    }
    output = Path(__file__).with_name("punctured_centre_offdiagonal_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
