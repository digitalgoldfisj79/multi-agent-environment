#!/usr/bin/env python3
"""Exact finite audit of the primorial inverse-orbit Type-II and high-conductor frames."""
from __future__ import annotations

import cmath
import itertools
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


def cis_mod(n: int, p: int) -> complex:
    return cmath.exp(2j * math.pi * (n % p) / p)


def panel(X: int, eta_num: int = 4, eta_den: int = 5) -> dict:
    H = eta_num * X * X // eta_den
    primes = primes_upto(max(H, 4 * X))
    z_values = [p for p in primes if X <= p < 2 * X]
    K = max(1, min(len(z_values), math.ceil(math.log(X))))
    z_values = z_values[:K]
    Z = z_values[-1]
    moduli = [p for p in primes if Z < p <= min(2 * Z, H)]

    # Critical balanced finite Type-II panel.  Every u,v is below every modulus.
    U = list(range(2, X + 1))
    V = list(range(2, X + 1))
    alpha = {
        u: Fraction((1 if u % 2 == 0 else -1) * (1 + u % 3))
        for u in U
    }
    gamma = {
        v: Fraction((1 if v % 2 else -1) * (1 + v % 4))
        for v in V
    }
    alpha_total = sum(alpha.values(), Fraction())
    gamma_total = sum(gamma.values(), Fraction())
    centres = [primorial_to(z, primes) for z in z_values]

    max_fourier_error = 0.0
    max_inverse_orbit_error = 0.0
    direct_values: list[str] = []
    per_modulus_values: list[list[Fraction]] = []

    for P in centres:
        direct_additive = Fraction()
        row_values: list[Fraction] = []
        fourier_value = 0j
        inverse_orbit_value = 0j

        for p in moduli:
            hit_sum = sum(
                alpha[u] * gamma[v]
                for u in U
                for v in V
                if (u * v + P) % p == 0
            )
            additive_discrepancy = hit_sum - Fraction(alpha_total * gamma_total, p)
            unit_discrepancy = hit_sum - Fraction(alpha_total * gamma_total, p - 1)
            assert unit_discrepancy == additive_discrepancy - Fraction(
                alpha_total * gamma_total, p * (p - 1)
            )

            direct_additive += additive_discrepancy
            row_values.append(additive_discrepancy)

            gamma_hat = {
                ell: sum(
                    float(gamma[v]) * cis_mod(ell * v, p)
                    for v in V
                )
                for ell in range(1, p)
            }

            # Original additive-character representation.
            for h in range(1, p):
                source = sum(
                    float(alpha[u]) * gamma_hat[(h * u) % p]
                    for u in U
                )
                fourier_value += cis_mod(h * (P % p), p) * source / p

            # Change ell=hu: one Type-II variable joins the primorial orbit.
            for u in U:
                inverse_u = pow(u, -1, p)
                inner = sum(
                    cis_mod(ell * (P % p) * inverse_u, p)
                    * gamma_hat[ell]
                    / p
                    for ell in range(1, p)
                )
                inverse_orbit_value += float(alpha[u]) * inner

        max_fourier_error = max(
            max_fourier_error,
            abs(fourier_value - complex(float(direct_additive), 0.0)),
        )
        max_inverse_orbit_error = max(
            max_inverse_orbit_error,
            abs(inverse_orbit_value - complex(float(direct_additive), 0.0)),
        )
        direct_values.append(str(direct_additive))
        per_modulus_values.append(row_values)

    assert max_fourier_error < 1e-9
    assert max_inverse_orbit_error < 1e-9

    # Exact inverse-orbit Gram and the fixed-p multiplicity bound.
    row_indices = [(j, u) for j in range(K) for u in U]
    inverse_orbit_gram_checks = 0
    maximum_residue_multiplicity = 0

    for p in moduli:
        residue_multiplicities: dict[int, int] = {}
        for j, P in enumerate(centres):
            for u in U:
                residue = (P % p) * pow(u, -1, p) % p
                residue_multiplicities[residue] = residue_multiplicities.get(residue, 0) + 1

        fixed_p_maximum = max(residue_multiplicities.values(), default=0)
        assert fixed_p_maximum <= K
        maximum_residue_multiplicity = max(
            maximum_residue_multiplicity,
            fixed_p_maximum,
        )

        for j, u in row_indices:
            for k, u_prime in row_indices:
                inverse_collision = (
                    (centres[j] % p) * pow(u, -1, p)
                    - (centres[k] % p) * pow(u_prime, -1, p)
                ) % p == 0
                transported_collision = (
                    centres[j] * u_prime - centres[k] * u
                ) % p == 0
                assert inverse_collision == transported_collision
                inverse_orbit_gram_checks += 1

    combined_frame_norm_upper = sum(
        (Fraction(K, p) for p in moduli),
        Fraction(),
    )

    # High-conductor candidate collision frame.
    high_conductors: list[tuple[int, Fraction]] = []
    for order in range(2, len(moduli) + 1):
        for subset in itertools.combinations(moduli, order):
            Q = math.prod(subset)
            assert Q > H
            weight = Fraction(1, math.prod(p - 2 for p in subset))
            high_conductors.append((Q, weight))

    high_diagonal_mass = sum((weight for _, weight in high_conductors), Fraction())
    high_collision_checks = 0
    offdiagonal_mass_ratios: list[float] = []
    high_row_bounds: list[Fraction] = []

    for j, P_j in enumerate(centres):
        row_bound = high_diagonal_mass
        for k, P_k in enumerate(centres):
            if j == k:
                continue

            L = max(P_j, P_k) // min(P_j, P_k)
            collision_mass = Fraction()
            for Q, weight in high_conductors:
                rho_j = Z + 1 + ((-P_j - (Z + 1)) % Q)
                rho_k = Z + 1 + ((-P_k - (Z + 1)) % Q)
                same_candidate = rho_j == rho_k
                difference_divisibility = (P_k - P_j) % Q == 0
                prefix_divisibility = (L - 1) % Q == 0
                assert same_candidate == difference_divisibility == prefix_divisibility
                high_collision_checks += 1
                if same_candidate:
                    collision_mass += weight

            selected_primes = [p for p in moduli if (L - 1) % p == 0]
            S = sum((Fraction(1, p - 2) for p in selected_primes), Fraction())
            product = Fraction(1)
            for p in selected_primes:
                product *= 1 + Fraction(1, p - 2)
            product_formula = product - 1 - S
            assert collision_mass == product_formula

            if S:
                offdiagonal_mass_ratios.append(float(collision_mass / (S * S)))
            row_bound += collision_mass

        high_row_bounds.append(row_bound)

    coherent_energy = sum(
        sum(row, Fraction()) ** 2
        for row in per_modulus_values
    )
    diagonal_energy = sum(
        value * value
        for row in per_modulus_values
        for value in row
    )

    return {
        "X": X,
        "H": H,
        "K": K,
        "z_values": z_values,
        "Z": Z,
        "moduli": moduli,
        "typeii_direct_additive": direct_values,
        "max_fourier_error": max_fourier_error,
        "max_inverse_orbit_error": max_inverse_orbit_error,
        "unit_baseline_drift_checked": True,
        "inverse_orbit_gram_checks": inverse_orbit_gram_checks,
        "max_fixed_modulus_residue_multiplicity": maximum_residue_multiplicity,
        "combined_frame_norm_upper": str(combined_frame_norm_upper),
        "high_conductor_collision_checks": high_collision_checks,
        "high_conductor_diagonal_mass": str(high_diagonal_mass),
        "high_conductor_max_schur_row": str(max(high_row_bounds, default=Fraction())),
        "max_offdiagonal_mass_over_S_squared": max(
            offdiagonal_mass_ratios,
            default=0.0,
        ),
        "empirical_typeii_coherent_to_diagonal_ratio": (
            float(coherent_energy / diagonal_energy)
            if diagonal_energy
            else 0.0
        ),
        "generic_frame_cauchy_to_fortune_ratio_scale": X / math.log(X),
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact_scope": [
            "additive and unit-centred Type-II drift",
            "direct/Fourier/inverse-orbit Type-II identity",
            "combined inverse-orbit Gram collision transport",
            "fixed-modulus residue multiplicity bound",
            "high-conductor candidate collision criterion",
            "high-conductor Euler-product mass formula",
        ],
        "panels": [panel(X) for X in (11, 17, 23)],
        "boundary": (
            "The logarithmic-block inverse-orbit frame and the high-conductor complete-model "
            "candidate frame pass exactly.  Generic Cauchy in the remaining Type-II variable "
            "still misses the Fortune scale by X/log X up to subpolynomial factors.  POTD(X), "
            "deterministic one-point conductor sampling and Fortune's conjecture remain OPEN."
        ),
    }
    output = Path(__file__).with_name("primorial_orbit_typeii_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
