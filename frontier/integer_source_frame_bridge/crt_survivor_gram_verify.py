#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path

from sympy import primerange


def primorial(z: int) -> int:
    value = 1
    for p in primerange(2, z + 1):
        value *= int(p)
    return value


def squarefree_divisors(primes: list[int]) -> list[int]:
    divisors = [1]
    for p in primes:
        divisors += [p * d for d in list(divisors)]
    return sorted(divisors)


def phi_on_support(n: int, primes: list[int]) -> int:
    value = 1
    for p in primes:
        if n % p == 0:
            value *= p - 1
    return value


def mu_on_support(n: int, primes: list[int]) -> int:
    omega = sum(1 for p in primes if n % p == 0)
    return -1 if omega % 2 else 1


def dot(x: tuple[Fraction, ...], y: tuple[Fraction, ...]) -> Fraction:
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def complement_divisor_identity_panel(primes: list[int]) -> dict:
    divisors = squarefree_divisors(primes)
    coefficients = {
        d: (
            Fraction((d % 7) - 3),
            Fraction((d % 5) - 2),
            Fraction((d % 11) - 5),
        )
        for d in divisors
    }

    lhs = Fraction(0)
    for d in divisors:
        tail = tuple(
            sum(
                (coefficients[m][i] / m for m in divisors if m % d == 0),
                Fraction(0),
            )
            for i in range(3)
        )
        lhs += phi_on_support(d, primes) * dot(tail, tail)

    density = Fraction(1)
    for p in primes:
        density *= Fraction(p - 1, p)

    rhs = Fraction(0)
    for delta in divisors:
        lower_sum = tuple(
            sum(
                (coefficients[m][i] for m in divisors if delta % m == 0),
                Fraction(0),
            )
            for i in range(3)
        )
        rhs += dot(lower_sum, lower_sum) / phi_on_support(delta, primes)
    rhs *= density

    assert lhs == rhs

    mobius_coefficients = {d: Fraction(mu_on_support(d, primes)) for d in divisors}
    mobius_lhs = Fraction(0)
    for d in divisors:
        tail = sum(
            (mobius_coefficients[m] / m for m in divisors if m % d == 0),
            Fraction(0),
        )
        mobius_lhs += phi_on_support(d, primes) * tail * tail
    assert mobius_lhs == density

    normalized_mobius_lhs = mobius_lhs / (density * density)
    assert normalized_mobius_lhs == 1 / density

    return {
        "primes": primes,
        "divisor_count": len(divisors),
        "hilbert_lhs": str(lhs),
        "hilbert_rhs": str(rhs),
        "mobius_energy": str(mobius_lhs),
        "density": str(density),
        "normalized_mobius_energy": str(normalized_mobius_lhs),
        "status": "PASS",
    }


def inverse_band_density(primes: list[int]) -> Fraction:
    value = Fraction(1)
    for p in primes:
        if p <= 3:
            raise ValueError("survivor band requires primes at least 5")
        value *= Fraction(p - 1, p - 2)
    return value


def centered_survivor(
    centre: int,
    residues: tuple[int, ...],
    primes: list[int],
) -> Fraction:
    survives = all((centre + residue) % p != 0 for residue, p in zip(residues, primes))
    return (inverse_band_density(primes) if survives else Fraction(0)) - 1


def survivor_covariance_formula(
    centre_a: int,
    centre_b: int,
    primes: list[int],
) -> Fraction:
    if centre_a == centre_b:
        return inverse_band_density(primes) - 1

    second_moment = Fraction(1)
    for p in primes:
        if (centre_a - centre_b) % p == 0:
            second_moment *= Fraction(p - 1, p - 2)
        else:
            second_moment *= Fraction((p - 1) * (p - 3), (p - 2) * (p - 2))
    return second_moment - 1


def matrix_quadratic_form(
    matrix: list[list[Fraction]],
    vector: list[Fraction],
) -> Fraction:
    return sum(
        (
            vector[i] * matrix[i][j] * vector[j]
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        Fraction(0),
    )


def survivor_gram_panel(
    centre_cutoffs: list[int],
    band_primes: list[int],
) -> dict:
    centres = [primorial(z) for z in centre_cutoffs]
    if min(band_primes) <= max(centre_cutoffs):
        raise ValueError("band primes must exceed every primorial cutoff")

    sample_space = list(product(*(range(1, p) for p in band_primes)))
    sample_size = len(sample_space)

    values: list[list[Fraction]] = []
    means: list[Fraction] = []
    for centre in centres:
        row = [centered_survivor(centre, residues, band_primes) for residues in sample_space]
        values.append(row)
        means.append(sum(row, Fraction(0)) / sample_size)
    assert all(mean == 0 for mean in means)

    formula_covariance: list[list[Fraction]] = []
    for i, centre_a in enumerate(centres):
        formula_row: list[Fraction] = []
        for j, centre_b in enumerate(centres):
            empirical = sum(
                (values[i][t] * values[j][t] for t in range(sample_size)),
                Fraction(0),
            ) / sample_size
            formula = survivor_covariance_formula(centre_a, centre_b, band_primes)
            formula_row.append(formula)
            assert empirical == formula
        formula_covariance.append(formula_row)

    diagonal = inverse_band_density(band_primes) - 1
    assert all(formula_covariance[i][i] == diagonal for i in range(len(centres)))

    collision_sets = {
        f"{i},{j}": [
            p for p in band_primes if (centres[i] - centres[j]) % p == 0
        ]
        for i in range(len(centres))
        for j in range(i + 1, len(centres))
    }

    row_sums = [
        sum((abs(entry) for entry in row), Fraction(0))
        for row in formula_covariance
    ]
    schur_bound = max(row_sums)

    test_vector = [Fraction(2), Fraction(-1), Fraction(3)]
    if len(centres) != len(test_vector):
        test_vector = [Fraction(i + 1) for i in range(len(centres))]
    quadratic_form = matrix_quadratic_form(formula_covariance, test_vector)
    schur_rhs = schur_bound * dot(tuple(test_vector), tuple(test_vector))
    assert quadratic_form <= schur_rhs

    noncollision_product = Fraction(1)
    for p in band_primes:
        noncollision_product *= Fraction((p - 1) * (p - 3), (p - 2) ** 2)

    return {
        "centre_cutoffs": centre_cutoffs,
        "centres": centres,
        "band_primes": band_primes,
        "sample_size": sample_size,
        "means": [str(value) for value in means],
        "inverse_density": str(inverse_band_density(band_primes)),
        "diagonal_covariance": str(diagonal),
        "noncollision_product": str(noncollision_product),
        "collision_sets": collision_sets,
        "covariance_matrix": [
            [str(entry) for entry in row] for row in formula_covariance
        ],
        "absolute_row_sums": [str(value) for value in row_sums],
        "schur_bound": str(schur_bound),
        "test_vector": [str(value) for value in test_vector],
        "test_quadratic_form": str(quadratic_form),
        "test_schur_rhs": str(schur_rhs),
        "status": "PASS",
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "complement_divisor_identity": complement_divisor_identity_panel([5, 7, 11]),
            "survivor_gram": survivor_gram_panel([5, 7, 11], [13, 17, 19]),
        },
        "boundary": (
            "The complete-CRT normalized-survivor centre Gram is exact and bounded. "
            "The arithmetic candidate-prime source still requires a deterministic "
            "sampling transfer preserving prior-band weights and cross-offset covariance."
        ),
    }
    output = Path(__file__).with_name("crt_survivor_gram_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
