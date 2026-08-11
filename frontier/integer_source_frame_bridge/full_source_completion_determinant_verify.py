#!/usr/bin/env python3
"""Exact and finite audit of the repaired long-cell / determinant sequence.

Checks:
1. The one-small-variable source coefficient reconstructs Lambda exactly as a
   formal linear combination of log primes.
2. Completion of every true long m-cell modulo p, followed by summation in d,
   reconstructs the direct Lambda residue class and character sum.
3. The prime-modulus residue variance equals the centred determinant kernel;
   band-prime source points n=p are the only non-unit Lambda terms.
4. Empirical panels compare the uncentred hit form, centred prime-band
   variance and complete all-Euler survivor amplitude.
"""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path
from typing import Dict

Vector = Dict[int, int]


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def factorize(n: int, primes: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out[p] = e
        if x == 1:
            break
    if x > 1:
        out[x] = 1
    return out


def mobius(n: int, primes: list[int]) -> int:
    fac = factorize(n, primes)
    if any(e > 1 for e in fac.values()):
        return 0
    return -1 if len(fac) % 2 else 1


def divisors(n: int, primes: list[int]) -> list[int]:
    values = [1]
    for p, e in factorize(n, primes).items():
        values = [d * (p**a) for d in values for a in range(e + 1)]
    return values


def add_scaled(target: Vector, source: Vector, scale: int) -> None:
    if scale == 0:
        return
    for p, value in source.items():
        target[p] = target.get(p, 0) + scale * value
        if target[p] == 0:
            del target[p]


def log_vector(n: int, primes: list[int]) -> Vector:
    return factorize(n, primes)


def one_convolve_log_vector(n: int, primes: list[int]) -> Vector:
    out: Vector = {}
    for d in divisors(n, primes):
        add_scaled(out, log_vector(d, primes), 1)
    return out


def c_y_vector(m: int, Y: int, primes: list[int]) -> Vector:
    """Formal vector for log(m) + (mu_{>Y} * 1 * log)(m)."""
    out = log_vector(m, primes)
    for a in divisors(m, primes):
        if a <= Y:
            continue
        mu = mobius(a, primes)
        if mu:
            add_scaled(out, one_convolve_log_vector(m // a, primes), mu)
    return out


def lambda_vector(n: int, primes: list[int]) -> Vector:
    fac = factorize(n, primes)
    if len(fac) == 1:
        p = next(iter(fac))
        return {p: 1}
    return {}


def vector_float(v: Vector) -> float:
    return sum(coeff * math.log(p) for p, coeff in v.items())


def primitive_root(p: int, primes: list[int]) -> int:
    factors = list(factorize(p - 1, primes))
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError("primitive root not found")


def primorial(z: int, primes: list[int]) -> int:
    value = 1
    for p in primes:
        if p > z:
            break
        value *= p
    return value


def formal_panel(X: int, eta_num: int = 4, eta_den: int = 5) -> dict:
    H = eta_num * X * X // eta_den
    Y = math.isqrt(H)
    if Y * Y < H:
        Y += 1
    primes = primes_upto(max(H, 4 * X))
    assert Y < X and H <= Y * Y

    cvec = {m: c_y_vector(m, Y, primes) for m in range(1, H + 1)}
    reconstructed: dict[int, Vector] = {}
    source_checks = 0
    for n in range(1, H + 1):
        value: Vector = {}
        for d in divisors(n, primes):
            if d <= Y:
                mu = mobius(d, primes)
                if mu:
                    add_scaled(value, cvec[n // d], mu)
        assert value == lambda_vector(n, primes)
        reconstructed[n] = value
        source_checks += 1

    z_values = [p for p in primes if X <= p < 2 * X]
    K = max(1, min(len(z_values), math.ceil(math.log(X))))
    z_values = z_values[:K]
    Z = z_values[-1]
    centres = [primorial(z, primes) for z in z_values]
    band = [p for p in primes if Z < p <= min(2 * Z, H)]

    residue_completion_checks = 0
    character_completion_checks = 0
    max_character_error = 0.0
    long_cell_aliases = 0
    first_alias = None
    nonunit_checks = 0

    for p in band:
        left: list[Vector] = [dict() for _ in range(p)]
        right: list[Vector] = [dict() for _ in range(p)]
        for d in range(1, Y + 1):
            mu = mobius(d, primes)
            if not mu:
                continue
            top = H // d
            for m in range(1, top + 1):
                add_scaled(left[(d * m) % p], cvec[m], mu)
                if m + p <= top:
                    long_cell_aliases += 1
                    if first_alias is None:
                        first_alias = [p, d, m, m + p]
        for n in range(1, H + 1):
            add_scaled(right[n % p], lambda_vector(n, primes), 1)
        for a in range(p):
            assert left[a] == right[a]
            residue_completion_checks += 1

        nonunits = [n for n in range(p, H + 1, p) if reconstructed[n]]
        assert nonunits == [p]
        assert reconstructed[p] == {p: 1}
        nonunit_checks += 1

        g = primitive_root(p, primes)
        dlog: dict[int, int] = {}
        x = 1
        for t in range(p - 1):
            dlog[x] = t
            x = x * g % p
        cnum = {m: vector_float(cvec[m]) for m in range(1, H + 1)}
        lnum = {n: vector_float(reconstructed[n]) for n in range(1, H + 1)}

        for k in range(1, p - 1):
            lhs = 0j
            for d in range(1, Y + 1):
                mu = mobius(d, primes)
                if not mu:
                    continue
                chi_d = cmath.exp(2j * math.pi * k * dlog[d % p] / (p - 1))
                inner = 0j
                for m in range(1, H // d + 1):
                    if m % p:
                        chi_m = cmath.exp(2j * math.pi * k * dlog[m % p] / (p - 1))
                        inner += cnum[m] * chi_m
                lhs += mu * chi_d * inner
            rhs = 0j
            for n in range(1, H + 1):
                if n % p and lnum[n]:
                    chi_n = cmath.exp(2j * math.pi * k * dlog[n % p] / (p - 1))
                    rhs += lnum[n] * chi_n
            error = abs(lhs - rhs)
            max_character_error = max(max_character_error, error)
            assert error < 1e-8 * max(1.0, abs(rhs))
            character_completion_checks += 1

        for P in centres:
            a = (-P) % p
            assert a
            direct = vector_float(right[a]) - sum(
                vector_float(right[r]) for r in range(1, p)
            ) / (p - 1)
            spectral = 0j
            for k in range(1, p - 1):
                psi_chi = 0j
                for n in range(1, H + 1):
                    if n % p and lnum[n]:
                        chi_n = cmath.exp(2j * math.pi * k * dlog[n % p] / (p - 1))
                        psi_chi += lnum[n] * chi_n
                chi_a_bar = cmath.exp(-2j * math.pi * k * dlog[a] / (p - 1))
                spectral += chi_a_bar * psi_chi / (p - 1)
            error = abs(direct - spectral)
            max_character_error = max(max_character_error, error)
            assert error < 1e-8 * max(1.0, abs(direct))
            character_completion_checks += 1

    return {
        "X": X,
        "H": H,
        "Y": Y,
        "K": K,
        "Z": Z,
        "band_moduli": band,
        "source_identity_checks": source_checks,
        "exact_residue_completion_checks": residue_completion_checks,
        "character_completion_checks": character_completion_checks,
        "maximum_character_error": max_character_error,
        "long_cell_alias_count": long_cell_aliases,
        "first_long_cell_alias": first_alias,
        "nonunit_lambda_checks": nonunit_checks,
    }


def lambda_array(H: int, primes: list[int]) -> list[float]:
    values = [0.0] * (H + 1)
    for p in primes:
        if p > H:
            break
        value = p
        weight = math.log(p)
        while value <= H:
            values[value] = weight
            if value > H // p:
                break
            value *= p
    return values


def primorial_mod(z: int, p: int, primes: list[int]) -> int:
    value = 1
    for q in primes:
        if q > z:
            break
        value = value * q % p
    return value


def numeric_panel(X: int, eta_num: int = 4, eta_den: int = 5) -> dict:
    H = eta_num * X * X // eta_den
    primes = primes_upto(max(H, 4 * X))
    z_values = [p for p in primes if X <= p < 2 * X]
    K = max(1, min(len(z_values), math.ceil(math.log(X))))
    z_values = z_values[:K]
    Z = z_values[-1]
    band = [p for p in primes if Z < p <= min(2 * Z, H)]
    lam = lambda_array(H, primes)
    support = [n for n in range(2, H + 1) if lam[n]]

    full_residue_variance = 0.0
    raw_congruence_total = 0.0
    diagonal = 0.0
    selected_residue_energy = 0.0
    residue_data: dict[int, tuple[list[float], float, list[int]]] = {}

    for p in band:
        residues = [0.0] * p
        for n in support:
            if n % p:
                residues[n % p] += lam[n]
        unit_total = sum(residues)
        mean = unit_total / (p - 1)
        full_residue_variance += sum((residues[a] - mean) ** 2 for a in range(1, p))
        raw_congruence_total += sum(residues[a] ** 2 for a in range(1, p))
        unit_square_mass = sum(lam[n] ** 2 for n in support if n % p)
        diagonal += (1.0 - 1.0 / (p - 1)) * unit_square_mass
        centre_moduli = [primorial_mod(z, p, primes) for z in z_values]
        for P_mod in centre_moduli:
            selected_residue_energy += (residues[(-P_mod) % p] - mean) ** 2
        residue_data[p] = (residues, mean, centre_moduli)

    centred_offdiagonal = full_residue_variance - diagonal
    raw_offdiagonal = raw_congruence_total - sum(
        sum(lam[n] ** 2 for n in support if n % p) for p in band
    )

    determinant_check = None
    if X <= 53:
        direct = 0.0
        for p in band:
            for n in support:
                if n % p == 0:
                    continue
                for m in support:
                    if m % p == 0:
                        continue
                    direct += lam[n] * lam[m] * (
                        (1.0 if (n - m) % p == 0 else 0.0) - 1.0 / (p - 1)
                    )
        assert abs(direct - full_residue_variance) < 1e-8 * max(1.0, full_residue_variance)
        determinant_check = direct
        for i, n in enumerate(support):
            for m in support[i + 1 :]:
                assert sum((n - m) % p == 0 for p in band) <= 1

    V = 1.0
    for p in band:
        V *= (p - 2) / (p - 1)
    inverse_V = 1.0 / V if band else 1.0
    full_rows: list[float] = []
    first_rows: list[float] = []
    for j, _z in enumerate(z_values):
        full_value = 0.0
        first_value = 0.0
        for p in band:
            residues, mean, centre_moduli = residue_data[p]
            discrepancy = residues[(-centre_moduli[j]) % p] - mean
            first_value += -(p - 1) / (p - 2) * discrepancy + math.log(p) / (p - 2)
        for n in support:
            hit = any((residue_data[p][2][j] + n) % p == 0 for p in band)
            coordinate = inverse_V * (0.0 if hit else 1.0) - 1.0
            full_value += lam[n] * coordinate
        full_rows.append(full_value)
        first_rows.append(first_value)
    higher_rows = [full - first for full, first in zip(full_rows, first_rows)]
    full_energy = sum(value * value for value in full_rows)
    first_energy = sum(value * value for value in first_rows)
    higher_energy = sum(value * value for value in higher_rows)
    cross = 2.0 * sum(first * higher for first, higher in zip(first_rows, higher_rows))
    assert abs(full_energy - (first_energy + higher_energy + cross)) < 1e-8 * max(1.0, full_energy)

    scale = H * X
    return {
        "X": X,
        "H": H,
        "K": K,
        "Z": Z,
        "band_moduli": band,
        "source_support_size": len(support),
        "prime_band_residue_variance": full_residue_variance,
        "prime_band_variance_over_HX": full_residue_variance / scale,
        "selected_centre_residue_energy": selected_residue_energy,
        "selected_energy_over_HX": selected_residue_energy / scale,
        "raw_uncentred_offdiagonal": raw_offdiagonal,
        "raw_uncentred_over_H2": raw_offdiagonal / (H * H),
        "centred_offdiagonal": centred_offdiagonal,
        "centred_offdiagonal_over_HX": centred_offdiagonal / scale,
        "centred_diagonal": diagonal,
        "centred_diagonal_over_HX": diagonal / scale,
        "determinant_reordering_check": determinant_check,
        "full_survivor_energy": full_energy,
        "first_order_energy": first_energy,
        "higher_order_energy": higher_energy,
        "first_higher_cross_term": cross,
        "full_survivor_energy_over_HX": full_energy / scale,
        "first_order_energy_over_HX": first_energy / scale,
    }


def main() -> None:
    formal = [formal_panel(X) for X in (11, 17, 23)]
    numeric = [numeric_panel(X) for X in (11, 17, 23, 29, 37, 53, 79, 113, 163, 233, 337)]
    payload = {
        "status": "PASS",
        "proved_algebra_checked": [
            "one-small-variable c_Y source reconstructs Lambda exactly",
            "long m-cell residue completion resums to direct Lambda progressions",
            "multiplicative-character completion resums to the ordinary Lambda character sum",
            "the only non-unit Lambda source for p>X and H<X^2 is n=p",
            "prime-band residue variance equals the centred determinant quadratic form",
            "nonzero source differences have at most one first-band prime divisor",
            "full survivor energy equals first + higher + signed cross term",
        ],
        "formal_panels": formal,
        "numeric_panels": numeric,
        "boundary": (
            "The unbalanced-cell repair closes exactly after full source recombination: the apparent "
            "Mobius-weighted character family is the ordinary Lambda progression discrepancy.  The "
            "uncentred determinant hit form retains a density main term of order H^2/log X and is not "
            "the correct theorem.  The corrected physical target is a centred prime-band BDH estimate "
            "at H asymp X^2, while the full Fortune coordinate still requires signed recombination with "
            "the higher Euler conductor terms."
        ),
    }
    output = Path(__file__).with_name("full_source_completion_determinant_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
