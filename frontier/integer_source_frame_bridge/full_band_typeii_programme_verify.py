#!/usr/bin/env python3
"""Exact finite scaffold for the full-band primorial-orbit Type-II programme."""
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
    if n == 1:
        return 1
    value = n
    prime_count = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            prime_count += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1 if p == 2 else 2
    if value > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def primorial_to(z: int, primes: list[int]) -> int:
    value = 1
    for p in primes:
        if p > z:
            break
        value *= p
    return value


def panel(X: int, eta_num: int = 4, eta_den: int = 5) -> dict:
    H = eta_num * X * X // eta_den
    primes = primes_upto(max(H, 4 * X))
    z_values = [p for p in primes if X <= p < 2 * X]
    K = max(1, min(len(z_values), math.ceil(math.log(X))))
    z_values = z_values[:K]
    Z = z_values[-1]
    centres = [primorial_to(z, primes) for z in z_values]
    moduli = [p for p in primes if Z < p <= min(2 * Z, H)]

    side = min(X - 1, math.isqrt(H))
    U = list(range(2, side + 1))
    V = list(range(2, side + 1))
    assert U and V
    assert max(U) < min(moduli)
    assert max(V) < min(moduli)
    assert max(U) * max(V) <= H

    alpha = {u: Fraction(mobius(u)) for u in U}
    gamma = {v: Fraction(1 if v % 2 else -1) for v in V}

    convolution: dict[int, Fraction] = {}
    representation_count: dict[int, int] = {}
    representation_square_mass: dict[int, Fraction] = {}
    for u in U:
        for v in V:
            n = u * v
            coefficient = alpha[u] * gamma[v]
            convolution[n] = convolution.get(n, Fraction()) + coefficient
            representation_count[n] = representation_count.get(n, 0) + 1
            representation_square_mass[n] = (
                representation_square_mass.get(n, Fraction()) + coefficient * coefficient
            )

    alpha_l2 = sum((value * value for value in alpha.values()), Fraction())
    gamma_l2 = sum((value * value for value in gamma.values()), Fraction())
    convolution_l2 = sum((value * value for value in convolution.values()), Fraction())
    max_representation_count = max(representation_count.values(), default=0)
    assert convolution_l2 <= max_representation_count * alpha_l2 * gamma_l2

    V_R = Fraction(1)
    for p in moduli:
        V_R *= Fraction(p - 2, p - 1)
    inverse_V_R = 1 / V_R

    rows: list[dict] = []
    total_square = Fraction()
    total_source_diagonal = Fraction()
    total_source_offdiagonal = Fraction()
    total_model_quadratic = Fraction()
    maximum_collision_count = 0
    collision_pair_count = 0
    noncollision_pair_count = 0

    products = sorted(convolution)
    for z, P in zip(z_values, centres, strict=True):
        g_values: dict[int, Fraction] = {}
        for n in products:
            survives = all((P + n) % p != 0 for p in moduli)
            g_values[n] = inverse_V_R - 1 if survives else Fraction(-1)

        direct = sum(
            alpha[u] * gamma[v] * g_values[u * v]
            for u in U
            for v in V
        )
        compressed = sum(
            convolution[n] * g_values[n]
            for n in products
        )
        assert direct == compressed

        source_diagonal = sum(
            convolution[n] * convolution[n] * g_values[n] * g_values[n]
            for n in products
        )
        full_square = compressed * compressed
        source_offdiagonal = full_square - source_diagonal

        model_quadratic = Fraction()
        row_collision_pairs = 0
        row_noncollision_pairs = 0
        row_max_collision_count = 0

        for n in products:
            for n_prime in products:
                if n == n_prime:
                    kernel = inverse_V_R - 1
                else:
                    collision_primes = [
                        p for p in moduli if (n - n_prime) % p == 0
                    ]
                    assert len(collision_primes) <= 1
                    row_max_collision_count = max(
                        row_max_collision_count, len(collision_primes)
                    )
                    if collision_primes:
                        row_collision_pairs += 1
                    else:
                        row_noncollision_pairs += 1

                    product_factor = Fraction(1)
                    for p in moduli:
                        if (n - n_prime) % p == 0:
                            product_factor *= Fraction(p - 1, p - 2)
                        else:
                            product_factor *= Fraction((p - 1) * (p - 3), (p - 2) ** 2)
                    kernel = product_factor - 1

                model_quadratic += (
                    convolution[n] * convolution[n_prime] * kernel
                )

        total_square += full_square
        total_source_diagonal += source_diagonal
        total_source_offdiagonal += source_offdiagonal
        total_model_quadratic += model_quadratic
        maximum_collision_count = max(maximum_collision_count, row_max_collision_count)
        collision_pair_count += row_collision_pairs
        noncollision_pair_count += row_noncollision_pairs

        rows.append(
            {
                "z": z,
                "full_band_sum": str(compressed),
                "full_band_square": str(full_square),
                "source_product_diagonal": str(source_diagonal),
                "source_product_offdiagonal": str(source_offdiagonal),
                "complete_model_quadratic": str(model_quadratic),
            }
        )

    assert total_square == total_source_diagonal + total_source_offdiagonal

    # The at-most-one-collision property follows asymptotically from pq > H.
    # Verify the exact finite parameter inequality used by the programme.
    pair_products_above_H = all(
        p * q > H
        for index, p in enumerate(moduli)
        for q in moduli[index + 1 :]
    )
    assert pair_products_above_H
    assert maximum_collision_count <= 1

    return {
        "X": X,
        "H": H,
        "K": K,
        "z_values": z_values,
        "Z": Z,
        "moduli": moduli,
        "U_length": len(U),
        "V_length": len(V),
        "product_count": len(products),
        "max_product": max(products),
        "max_representation_count": max_representation_count,
        "alpha_l2": str(alpha_l2),
        "gamma_l2": str(gamma_l2),
        "convolution_l2": str(convolution_l2),
        "convolution_energy_bound": str(max_representation_count * alpha_l2 * gamma_l2),
        "V_R": str(V_R),
        "pair_products_above_H": pair_products_above_H,
        "maximum_distinct_product_collision_primes": maximum_collision_count,
        "ordered_collision_pair_count": collision_pair_count,
        "ordered_noncollision_pair_count": noncollision_pair_count,
        "total_full_band_square": str(total_square),
        "total_source_product_diagonal": str(total_source_diagonal),
        "total_source_product_offdiagonal": str(total_source_offdiagonal),
        "total_complete_model_quadratic": str(total_model_quadratic),
        "empirical_full_square_to_source_diagonal_ratio": (
            float(total_square / total_source_diagonal)
            if total_source_diagonal
            else 0.0
        ),
        "rows": rows,
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact_scope": [
            "full-band Type-II direct/convolution compression",
            "source-product diagonal/off-diagonal square decomposition",
            "divisor-multiplicity convolution-energy bound",
            "at-most-one first-band collision prime for distinct source products",
            "complete-CRT two-source covariance kernel",
        ],
        "panels": [panel(X) for X in (11, 17, 23, 29, 37)],
        "boundary": (
            "These are exact finite scaffolding identities only. The next programme must "
            "construct the actual prime-source decomposition, prove the full-band off-source-"
            "diagonal Bessel estimate, retain signed cell recombination and then close the "
            "cross-band normalized-survivor transfer. Fortune's conjecture remains OPEN."
        ),
    }
    output = Path(__file__).with_name("full_band_typeii_programme_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
