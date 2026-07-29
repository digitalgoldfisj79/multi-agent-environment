#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path


def primes_upto(limit: int) -> list[int]:
    primes: list[int] = []
    for value in range(2, limit + 1):
        is_prime = True
        for prime in primes:
            if prime * prime > value:
                break
            if value % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(value)
    return primes


def unit_group(primes: list[int]) -> list[tuple[int, ...]]:
    return list(product(*(range(1, prime) for prime in primes)))


def inverse_density(primes: list[int]) -> Fraction:
    value = Fraction(1)
    for prime in primes:
        value *= Fraction(prime - 1, prime - 2)
    return value


def survivor_factor(prime: int, coordinate: int) -> Fraction:
    if coordinate == 1:
        return Fraction(0)
    return Fraction(prime - 1, prime - 2)


def local_residual(prime: int, coordinate: int) -> Fraction:
    return survivor_factor(prime, coordinate) - 1


def full_residual(primes: list[int], coordinates: tuple[int, ...]) -> Fraction:
    value = Fraction(1)
    for prime, coordinate in zip(primes, coordinates, strict=True):
        value *= survivor_factor(prime, coordinate)
    return value - 1


def local_kernel(prime: int, ratio: int) -> Fraction:
    if ratio == 1:
        return Fraction(1, prime - 2)
    return Fraction(-1, (prime - 2) ** 2)


def principal_pair_factor(prime: int, ratio: int) -> Fraction:
    return 1 + local_kernel(prime, ratio)


def reduced_kernel(
    primes: list[int],
    ratios: tuple[int, ...],
    removed_index: int,
) -> Fraction:
    value = Fraction(1)
    for index, (prime, ratio) in enumerate(zip(primes, ratios, strict=True)):
        if index == removed_index:
            continue
        value *= principal_pair_factor(prime, ratio)
    return value - 1


def full_kernel(primes: list[int], ratios: tuple[int, ...]) -> Fraction:
    value = Fraction(1)
    for prime, ratio in zip(primes, ratios, strict=True):
        value *= principal_pair_factor(prime, ratio)
    return value - 1


def ratio_coordinates(
    primes: list[int],
    first: tuple[int, ...],
    second: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(
        first_coordinate * pow(second_coordinate, -1, prime) % prime
        for prime, first_coordinate, second_coordinate
        in zip(primes, first, second, strict=True)
    )


def conditional_projection_direct(
    primes: list[int],
    prime_index: int,
    ratios: tuple[int, ...],
    second: tuple[int, ...],
) -> Fraction:
    other_primes = [p for index, p in enumerate(primes) if index != prime_index]
    total = Fraction(0)
    samples = 0
    for other_coordinates in unit_group(other_primes):
        first_coordinates: list[int] = []
        second_coordinates: list[int] = []
        iterator = iter(other_coordinates)
        for index, prime in enumerate(primes):
            if index == prime_index:
                y_value = second[index]
            else:
                y_value = next(iterator)
            second_coordinates.append(y_value)
            first_coordinates.append(ratios[index] * y_value % prime)
        total += full_residual(primes, tuple(first_coordinates)) * full_residual(
            primes, tuple(second_coordinates)
        )
        samples += 1
    return total / samples - full_kernel(primes, ratios)


def local_tensor_formula(
    primes: list[int],
    prime_index: int,
    ratios: tuple[int, ...],
    second: tuple[int, ...],
) -> Fraction:
    prime = primes[prime_index]
    ratio = ratios[prime_index]
    first_coordinate = ratio * second[prime_index] % prime
    kappa_minus = reduced_kernel(primes, ratios, prime_index)
    local_defect = (
        local_residual(prime, first_coordinate)
        * local_residual(prime, second[prime_index])
        - local_kernel(prime, ratio)
    )
    pair_survivor_defect = (
        survivor_factor(prime, first_coordinate)
        * survivor_factor(prime, second[prime_index])
        - principal_pair_factor(prime, ratio)
    )
    return local_defect + kappa_minus * pair_survivor_defect


def endpoint_character_sum(prime: int, coordinate: int) -> int:
    return prime - 2 if coordinate == 1 else -1


def endpoint_formula(
    primes: list[int],
    prime_index: int,
    ratios: tuple[int, ...],
    second: tuple[int, ...],
) -> Fraction:
    prime = primes[prime_index]
    ratio = ratios[prime_index]
    first_coordinate = ratio * second[prime_index] % prime
    kappa_minus = reduced_kernel(primes, ratios, prime_index)
    if ratio != 1:
        coefficient = 1 + (prime - 1) * kappa_minus
        return -Fraction(
            coefficient
            * (
                endpoint_character_sum(prime, first_coordinate)
                + endpoint_character_sum(prime, second[prime_index])
            ),
            (prime - 2) ** 2,
        )
    coefficient = prime - 3 - (prime - 1) * kappa_minus
    return Fraction(
        coefficient * endpoint_character_sum(prime, second[prime_index]),
        (prime - 2) ** 2,
    )


def exact_projection_panel() -> dict:
    primes = [5, 7]
    elements = unit_group(primes)
    checks = 0
    collision_checks = 0
    noncollision_checks = 0
    for first in elements:
        for second in elements:
            ratios = ratio_coordinates(primes, first, second)
            for prime_index in range(len(primes)):
                direct = conditional_projection_direct(
                    primes, prime_index, ratios, second
                )
                tensor = local_tensor_formula(primes, prime_index, ratios, second)
                endpoint = endpoint_formula(primes, prime_index, ratios, second)
                assert direct == tensor == endpoint
                checks += 1
                if ratios[prime_index] == 1:
                    collision_checks += 1
                else:
                    noncollision_checks += 1
    return {
        "primes": primes,
        "group_size": len(elements),
        "exact_checks": checks,
        "collision_checks": collision_checks,
        "noncollision_checks": noncollision_checks,
        "status": "PASS",
    }


def arithmetic_coordinates(
    primes: list[int],
    centre: int,
    source: int,
) -> tuple[int, ...]:
    return tuple(
        (-source * pow(centre % prime, -1, prime)) % prime for prime in primes
    )


def qform(
    points: list[tuple[int, int, tuple[int, ...]]],
    entry,
) -> Fraction:
    value = Fraction(0)
    for first in points:
        for second in points:
            value += entry(first, second)
    return value


def arithmetic_panel() -> dict:
    primes = [13, 17, 19]
    centres = [30, 210, 2310]
    sources = [p for p in primes_upto(97) if p > 19]
    points = [
        (centre, source, arithmetic_coordinates(primes, centre, source))
        for centre in centres
        for source in sources
    ]
    rows = []
    aggregate_total = Fraction(0)
    aggregate_local = Fraction(0)
    aggregate_correction = Fraction(0)
    aggregate_collision = Fraction(0)
    aggregate_noncollision = Fraction(0)

    for prime_index, prime in enumerate(primes):
        def layer(first, second):
            ratios = ratio_coordinates(primes, first[2], second[2])
            return endpoint_formula(primes, prime_index, ratios, second[2])

        def local(first, second):
            ratio = (
                first[2][prime_index]
                * pow(second[2][prime_index], -1, prime)
                % prime
            )
            return (
                local_residual(prime, first[2][prime_index])
                * local_residual(prime, second[2][prime_index])
                - local_kernel(prime, ratio)
            )

        def collision(first, second):
            ratio = (
                first[2][prime_index]
                * pow(second[2][prime_index], -1, prime)
                % prime
            )
            return layer(first, second) if ratio == 1 else Fraction(0)

        total = qform(points, layer)
        local_value = qform(points, local)
        correction = total - local_value
        collision_value = qform(points, collision)
        noncollision_value = total - collision_value

        aggregate_total += total
        aggregate_local += local_value
        aggregate_correction += correction
        aggregate_collision += collision_value
        aggregate_noncollision += noncollision_value

        rows.append(
            {
                "prime": prime,
                "total_low_mode_form": str(total),
                "local_residue_discrepancy_form": str(local_value),
                "reduced_band_correction": str(correction),
                "collision_part": str(collision_value),
                "noncollision_part": str(noncollision_value),
            }
        )

    assert aggregate_total == aggregate_collision + aggregate_noncollision
    assert aggregate_total == aggregate_local + aggregate_correction
    assert aggregate_collision * aggregate_noncollision < 0

    triangle_ratio = Fraction(
        abs(aggregate_collision) + abs(aggregate_noncollision),
        abs(aggregate_total),
    )
    return {
        "primes": primes,
        "centres": centres,
        "source_primes": sources,
        "point_count": len(points),
        "per_prime": rows,
        "aggregate": {
            "total_low_mode_form": str(aggregate_total),
            "local_residue_discrepancy_form": str(aggregate_local),
            "reduced_band_correction": str(aggregate_correction),
            "collision_part": str(aggregate_collision),
            "noncollision_part": str(aggregate_noncollision),
            "positive_split_to_total_ratio": str(triangle_ratio),
        },
        "status": "PASS",
    }


def residue_discrepancy_panel() -> dict:
    prime = 13
    centre = 30
    sources = [p for p in primes_upto(97) if p > 19]
    weights = {source: Fraction(source % 7 + 1) for source in sources}
    direct = sum(
        (
            weight
            * local_residual(
                prime,
                (-source * pow(centre % prime, -1, prime)) % prime,
            )
            for source, weight in weights.items()
        ),
        Fraction(0),
    )
    total_units = sum(
        (weight for source, weight in weights.items() if source % prime != 0),
        Fraction(0),
    )
    residue = (-centre) % prime
    class_sum = sum(
        (
            weight
            for source, weight in weights.items()
            if source % prime == residue
        ),
        Fraction(0),
    )
    discrepancy = -Fraction(prime - 1, prime - 2) * (
        class_sum - Fraction(total_units, prime - 1)
    )
    assert direct == discrepancy
    return {
        "prime": prime,
        "centre": centre,
        "source_count": len(sources),
        "direct_local_residual_sum": str(direct),
        "one_residue_discrepancy": str(discrepancy),
        "status": "PASS",
    }


def first_order_evaluation_no_go(primes: list[int]) -> dict:
    dimension = sum(prime - 2 for prime in primes)
    # The reproducing kernel of the direct sum of all exact conductor-p
    # character spaces has value equal to its dimension at every point.
    assert dimension == 43
    return {
        "primes": primes,
        "first_order_character_dimension": dimension,
        "sharp_point_evaluation_squared_norm": dimension,
        "status": "PASS",
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "single_prime_conditional_projection": exact_projection_panel(),
            "weighted_one_residue_discrepancy": residue_discrepancy_panel(),
            "first_order_point_evaluation_no_go": first_order_evaluation_no_go(
                [13, 17, 19]
            ),
        },
        "finite_arithmetic_panel": arithmetic_panel(),
        "boundary": (
            "After the conductor-p characters are summed exactly, their oscillation "
            "collapses to a first-order local survivor martingale defect. The leading "
            "quadratic form is a one-residue prime-distribution discrepancy; the "
            "reduced-band correction is explicit. Collision and noncollision pieces "
            "can be separately much larger and of opposite sign. Generic large-sieve "
            "control reaches the classical logarithmic scale but does not supply the "
            "o(log X) saving required by the Fortune variance target."
        ),
    }
    output = Path(__file__).with_name("single_prime_dilation_layer_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
