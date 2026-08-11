#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


def squarefree_divisors(primes: list[int]) -> list[int]:
    divisors = [1]
    for p in primes:
        divisors += [p * d for d in list(divisors)]
    return sorted(divisors)


def omega_on_support(n: int, primes: list[int]) -> int:
    return sum(1 for p in primes if n % p == 0)


def mu_on_support(n: int, primes: list[int]) -> int:
    return -1 if omega_on_support(n, primes) % 2 else 1


def phi_dagger(n: int, primes: list[int]) -> int:
    value = 1
    for p in primes:
        if n % p == 0:
            value *= p - 2
    return value


def phi_on_support(n: int, primes: list[int]) -> int:
    value = 1
    for p in primes:
        if n % p == 0:
            value *= p - 1
    return value


def inverse_survivor_density(primes: list[int]) -> Fraction:
    value = Fraction(1)
    for p in primes:
        value *= Fraction(p - 1, p - 2)
    return value


def primitive_character_orthogonality_sum(
    centre: int,
    source: int,
    conductor: int,
    primes: list[int],
) -> int:
    value = 1
    for p in primes:
        if conductor % p != 0:
            continue
        value *= p - 2 if (centre + source) % p == 0 else -1
    return value


def character_expansion(
    centre: int,
    source: int,
    primes: list[int],
) -> Fraction:
    total = Fraction(0)
    for conductor in squarefree_divisors(primes):
        total += (
            Fraction(mu_on_support(conductor, primes), phi_dagger(conductor, primes))
            * primitive_character_orthogonality_sum(
                centre,
                source,
                conductor,
                primes,
            )
        )
    return total


def normalized_survivor(
    centre: int,
    source: int,
    primes: list[int],
) -> Fraction:
    if any((centre + source) % p == 0 for p in primes):
        return Fraction(0)
    return inverse_survivor_density(primes)


def expansion_panel(primes: list[int], centre: int) -> dict:
    modulus = math.prod(primes)
    checked = 0
    survivors = 0
    for source in range(1, modulus + 1):
        if any(source % p == 0 for p in primes):
            continue
        spectral = character_expansion(centre, source, primes)
        physical = normalized_survivor(centre, source, primes)
        assert spectral == physical
        checked += 1
        if physical:
            survivors += 1

    divisors = squarefree_divisors(primes)
    quadratic_mass = sum(
        (Fraction(1, phi_dagger(conductor, primes)) for conductor in divisors),
        Fraction(0),
    )
    assert quadratic_mass == inverse_survivor_density(primes)

    nontrivial_mass = quadratic_mass - 1
    assert nontrivial_mass == inverse_survivor_density(primes) - 1

    character_l1_mass = sum(
        (
            Fraction(phi_dagger(conductor, primes), phi_dagger(conductor, primes))
            for conductor in divisors
        ),
        Fraction(0),
    )
    assert character_l1_mass == 2 ** len(primes)

    return {
        "primes": primes,
        "centre": centre,
        "modulus": modulus,
        "unit_sources_checked": checked,
        "survivors": survivors,
        "inverse_density": str(inverse_survivor_density(primes)),
        "quadratic_character_mass": str(quadratic_mass),
        "nontrivial_quadratic_mass": str(nontrivial_mass),
        "character_l1_mass": str(character_l1_mass),
        "status": "PASS",
    }


def factorization_no_go_panel(primes: list[int]) -> dict:
    rows = []
    for label, centre_local, source_local in (
        ("all_weight_on_centre", lambda p: Fraction(1, p - 2), lambda p: Fraction(1)),
        (
            "overweight_centre",
            lambda p: Fraction(1, (p - 2) ** 2),
            lambda p: Fraction(p - 2),
        ),
        ("all_weight_on_source", lambda p: Fraction(1), lambda p: Fraction(1, p - 2)),
    ):
        centre_mass = Fraction(1)
        source_mass = Fraction(1)
        local_products = []
        for p in primes:
            a = centre_local(p)
            b = source_local(p)
            assert a * b == Fraction(1, p - 2)
            x = Fraction(p - 2) * a * a
            y = Fraction(p - 2) * b * b
            assert x * y == 1
            centre_mass *= 1 + x
            source_mass *= 1 + y
            local_products.append((1 + x) * (1 + y))
        product_mass = centre_mass * source_mass
        assert all(value >= 4 for value in local_products)
        assert product_mass >= 4 ** len(primes)
        rows.append({
            "split": label,
            "centre_diagonal_mass": str(centre_mass),
            "source_diagonal_mass": str(source_mass),
            "product_mass": str(product_mass),
            "lower_bound": str(4 ** len(primes)),
        })

    balanced_mass = 2 ** len(primes)
    return {
        "primes": primes,
        "multiplicative_splits": rows,
        "square_root_split_centre_mass": balanced_mass,
        "square_root_split_source_mass": balanced_mass,
        "square_root_product": balanced_mass * balanced_mass,
        "status": "PASS",
    }


def high_conductor_source_bound_panel(
    primes: list[int],
    interval_length: int,
) -> dict:
    divisors = squarefree_divisors(primes)
    high = [q for q in divisors if q > interval_length]
    weighted_total = sum(
        (
            Fraction(phi_on_support(q, primes), phi_dagger(q, primes) ** 2)
            for q in high
        ),
        Fraction(0),
    )
    all_nontrivial = sum(
        (
            Fraction(phi_on_support(q, primes), phi_dagger(q, primes) ** 2)
            for q in divisors
            if q > 1
        ),
        Fraction(0),
    )
    euler_total = Fraction(1)
    for p in primes:
        euler_total *= 1 + Fraction(p - 1, (p - 2) ** 2)
    assert all_nontrivial == euler_total - 1
    assert weighted_total <= all_nontrivial

    low = [q for q in divisors if 1 < q <= interval_length]
    return {
        "primes": primes,
        "interval_length": interval_length,
        "low_conductors": low,
        "high_conductor_count": len(high),
        "high_weighted_character_bound": str(weighted_total),
        "all_nontrivial_euler_bound": str(all_nontrivial),
        "status": "PASS",
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "primitive_character_survivor_expansion": expansion_panel([5, 7, 11], 6),
            "multiplicative_factorization_no_go": factorization_no_go_panel([5, 7, 11]),
            "high_conductor_source_bound": high_conductor_source_bound_panel(
                [11, 13, 17],
                100,
            ),
        },
        "boundary": (
            "The survivor band has an exact primitive-character expansion and small "
            "quadratic coefficient mass. High-conductor source energy is separately "
            "controlled, but every multiplicative scalar Cauchy split creates an "
            "exponential centre/source diagonal product. A signed joint hybrid "
            "character estimate is still required."
        ),
    }
    output = Path(__file__).with_name("multiplicative_character_survivor_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
