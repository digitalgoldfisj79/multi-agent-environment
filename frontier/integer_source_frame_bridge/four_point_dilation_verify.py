#!/usr/bin/env python3
from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path


def squarefree_divisors(primes: list[int]) -> list[int]:
    divisors = [1]
    for p in primes:
        divisors += [p * d for d in list(divisors)]
    return sorted(divisors)


def phi_dagger(n: int, primes: list[int]) -> int:
    value = 1
    for p in primes:
        if n % p == 0:
            value *= p - 2
    return value


def inverse_density(primes: list[int]) -> Fraction:
    value = Fraction(1)
    for p in primes:
        value *= Fraction(p - 1, p - 2)
    return value


def survivor_density(primes: list[int]) -> Fraction:
    return 1 / inverse_density(primes)


def residual_from_coordinates(
    centre: int,
    source: int,
    dilation: tuple[int, ...],
    primes: list[int],
) -> Fraction:
    survives = all(
        (centre + source * u) % p != 0
        for p, u in zip(primes, dilation, strict=True)
    )
    return (inverse_density(primes) if survives else Fraction(0)) - 1


def deterministic_residual(centre: int, source: int, primes: list[int]) -> Fraction:
    return residual_from_coordinates(centre, source, tuple(1 for _ in primes), primes)


def unit_group(primes: list[int]) -> list[tuple[int, ...]]:
    return list(product(*(range(1, p) for p in primes)))


def local_nonprincipal_sum(
    centre_left: int,
    source_left: int,
    centre_right: int,
    source_right: int,
    p: int,
) -> int:
    collision = (source_left * centre_right - source_right * centre_left) % p == 0
    return p - 2 if collision else -1


def conductor_diagonal_kernel(
    centre_left: int,
    source_left: int,
    centre_right: int,
    source_right: int,
    primes: list[int],
) -> Fraction:
    total = Fraction(0)
    for conductor in squarefree_divisors(primes):
        if conductor == 1:
            continue
        local = 1
        for p in primes:
            if conductor % p == 0:
                local *= local_nonprincipal_sum(
                    centre_left,
                    source_left,
                    centre_right,
                    source_right,
                    p,
                )
        total += Fraction(local, phi_dagger(conductor, primes) ** 2)
    return total


def collision_formula(
    centre_left: int,
    source_left: int,
    centre_right: int,
    source_right: int,
    primes: list[int],
) -> Fraction:
    value = Fraction(1)
    for p in primes:
        collision = (source_left * centre_right - source_right * centre_left) % p == 0
        if collision:
            value *= Fraction(p - 1, p - 2)
        else:
            value *= Fraction((p - 1) * (p - 3), (p - 2) ** 2)
    return value - 1


def common_dilation_average(
    centre_left: int,
    source_left: int,
    centre_right: int,
    source_right: int,
    primes: list[int],
) -> Fraction:
    omega = unit_group(primes)
    total = sum(
        (
            residual_from_coordinates(centre_left, source_left, u, primes)
            * residual_from_coordinates(centre_right, source_right, u, primes)
            for u in omega
        ),
        Fraction(0),
    )
    return total / len(omega)


def primes_upto(limit: int) -> list[int]:
    values = []
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, math.isqrt(n) + 1)):
            values.append(n)
    return values


def primitive_root(p: int) -> int:
    phi = p - 1
    factors = []
    n = phi
    q = 2
    while q * q <= n:
        if n % q == 0:
            factors.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        factors.append(n)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    raise ValueError(f"no primitive root for {p}")


def discrete_log_table(p: int) -> dict[int, int]:
    g = primitive_root(p)
    table = {}
    value = 1
    for exponent in range(p - 1):
        table[value] = exponent
        value = (value * g) % p
    return table


def local_character(p: int, index: int, value: int, logs: dict[int, int]) -> complex:
    angle = 2.0 * math.pi * index * logs[value] / (p - 1)
    return cmath.exp(1j * angle)


def character_value(
    character: tuple[int, ...],
    point: tuple[int, ...],
    primes: list[int],
    logs: list[dict[int, int]],
) -> complex:
    value = 1.0 + 0.0j
    for p, index, coordinate, table in zip(primes, character, point, logs, strict=True):
        value *= local_character(p, index, coordinate, table)
    return value


def character_coefficient(character: tuple[int, ...], primes: list[int]) -> Fraction:
    if all(index == 0 for index in character):
        return Fraction(0)
    value = Fraction(1)
    for p, index in zip(primes, character, strict=True):
        if index != 0:
            value *= Fraction(-1, p - 2)
    return value


def universal_residual(point: tuple[int, ...], primes: list[int]) -> Fraction:
    survives = all(value != 1 for value in point)
    return (inverse_density(primes) if survives else Fraction(0)) - 1


def multiply_points(
    left: tuple[int, ...],
    right: tuple[int, ...],
    primes: list[int],
) -> tuple[int, ...]:
    return tuple((a * b) % p for a, b, p in zip(left, right, primes, strict=True))


def wigner_panel(primes: list[int]) -> dict:
    omega = unit_group(primes)
    characters = list(product(*(range(p - 1) for p in primes)))
    logs = [discrete_log_table(p) for p in primes]
    coefficients = {chi: float(character_coefficient(chi, primes)) for chi in characters}

    max_reconstruction_error = 0.0
    max_kernel_error = 0.0
    max_parseval_error = 0.0

    for r in omega:
        d_theta: dict[tuple[int, ...], complex] = {}
        for theta in characters:
            total = 0.0 + 0.0j
            for chi in characters:
                shifted = tuple(
                    (chi_i - theta_i) % (p - 1)
                    for chi_i, theta_i, p in zip(chi, theta, primes, strict=True)
                )
                total += (
                    coefficients[chi]
                    * coefficients[shifted]
                    * character_value(chi, r, primes, logs)
                )
            d_theta[theta] = total

        direct_kernel = sum(
            (
                universal_residual(multiply_points(r, y, primes), primes)
                * universal_residual(y, primes)
                for y in omega
            ),
            Fraction(0),
        ) / len(omega)
        max_kernel_error = max(
            max_kernel_error,
            abs(d_theta[tuple(0 for _ in primes)] - float(direct_kernel)),
        )

        direct_fourth = sum(
            (
                universal_residual(multiply_points(r, y, primes), primes) ** 2
                * universal_residual(y, primes) ** 2
                for y in omega
            ),
            Fraction(0),
        ) / len(omega)
        spectral_fourth = sum(abs(value) ** 2 for value in d_theta.values())
        max_parseval_error = max(max_parseval_error, abs(spectral_fourth - float(direct_fourth)))

        for y in omega:
            reconstructed = sum(
                d_theta[theta] * character_value(theta, y, primes, logs)
                for theta in characters
            )
            direct = float(
                universal_residual(multiply_points(r, y, primes), primes)
                * universal_residual(y, primes)
            )
            max_reconstruction_error = max(max_reconstruction_error, abs(reconstructed - direct))

    assert max_reconstruction_error < 1e-9
    assert max_kernel_error < 1e-9
    assert max_parseval_error < 1e-9
    return {
        "primes": primes,
        "group_size": len(omega),
        "character_count": len(characters),
        "max_reconstruction_error": max_reconstruction_error,
        "max_kernel_error": max_kernel_error,
        "max_parseval_error": max_parseval_error,
        "status": "PASS",
    }


def joint_survival_probability(r: tuple[int, ...], primes: list[int]) -> Fraction:
    value = Fraction(1)
    for coordinate, p in zip(r, primes, strict=True):
        if coordinate == 1:
            value *= Fraction(p - 2, p - 1)
        else:
            value *= Fraction(p - 3, p - 1)
    return value


def universal_kernel(r: tuple[int, ...], primes: list[int]) -> Fraction:
    density = survivor_density(primes)
    return joint_survival_probability(r, primes) / (density * density) - 1


def fourth_energy_formula(r: tuple[int, ...], primes: list[int]) -> Fraction:
    density = survivor_density(primes)
    delta = inverse_density(primes) - 1
    joint = joint_survival_probability(r, primes)
    return 1 - 2 * density * (1 - delta * delta) + joint * (1 - delta * delta) ** 2


def simplified_fourth_energy(r: tuple[int, ...], primes: list[int]) -> Fraction:
    delta = inverse_density(primes) - 1
    kernel = universal_kernel(r, primes)
    return delta * delta + kernel * (1 - delta) ** 2


def exact_energy_panel(primes: list[int]) -> dict:
    omega = unit_group(primes)
    max_difference = Fraction(0)
    rows = []
    for r in omega:
        exact = fourth_energy_formula(r, primes)
        simplified = simplified_fourth_energy(r, primes)
        assert exact == simplified
        direct = sum(
            (
                universal_residual(multiply_points(r, y, primes), primes) ** 2
                * universal_residual(y, primes) ** 2
                for y in omega
            ),
            Fraction(0),
        ) / len(omega)
        assert direct == exact
        difference = abs(direct - simplified)
        max_difference = max(max_difference, difference)
        if len(rows) < 4:
            kernel = universal_kernel(r, primes)
            rows.append({
                "r": list(r),
                "kernel": str(kernel),
                "fourth_energy": str(exact),
                "nontrivial_mode_energy": str(exact - kernel * kernel),
            })
    return {
        "primes": primes,
        "ratios_checked": len(omega),
        "max_exact_difference": str(max_difference),
        "sample_rows": rows,
        "status": "PASS",
    }


def local_mode_energy_sum(p: int, collision: bool, kappa_without_p: Fraction) -> Fraction:
    if collision:
        numerator = p - 3 - (p - 1) * kappa_without_p
        return Fraction(p - 2) * numerator * numerator / (p - 2) ** 4
    numerator = 1 + (p - 1) * kappa_without_p
    return Fraction(2 * (p - 3)) * numerator * numerator / (p - 2) ** 4


def low_conductor_energy_panel(primes: list[int]) -> dict:
    omega = unit_group(primes)
    rows = []
    for r in omega[: min(30, len(omega))]:
        total = Fraction(0)
        for index, p in enumerate(primes):
            reduced_primes = primes[:index] + primes[index + 1 :]
            reduced_r = r[:index] + r[index + 1 :]
            kappa = universal_kernel(reduced_r, reduced_primes) if reduced_primes else Fraction(0)
            energy = local_mode_energy_sum(p, r[index] == 1, kappa)
            assert energy >= 0
            total += energy
        rows.append({
            "r": list(r),
            "single_prime_mode_energy": str(total),
        })
    return {
        "primes": primes,
        "ratios_checked": len(rows),
        "sample_rows": rows[:5],
        "status": "PASS",
    }


def collision_reduction_panel() -> dict:
    primes = [13, 17, 19]
    centres = [30, 210, 2310]
    sources = [23, 29, 31, 37, 41, 43, 47]
    checked = 0
    collisions = 0
    for left_index in range(len(centres)):
        for right_index in range(left_index, len(centres)):
            left = centres[left_index]
            right = centres[right_index]
            assert right % left == 0
            multiplier = right // left
            for m, n, p in product(sources, sources, primes):
                direct = (m * right - n * left) % p == 0
                reduced = (m * multiplier - n) % p == 0
                assert direct == reduced
                checked += 1
                collisions += int(direct)
    return {
        "primes": primes,
        "centres": centres,
        "sources": sources,
        "tests": checked,
        "collisions": collisions,
        "status": "PASS",
    }


def four_point_kernel_panel() -> dict:
    primes = [13, 17, 19]
    centres = [30, 210, 2310]
    sources = [23, 29, 31, 37, 41, 43, 47]
    tuples = []
    for left, right, m, n in product(centres, centres, sources, sources):
        spectral = conductor_diagonal_kernel(left, m, right, n, primes)
        formula = collision_formula(left, m, right, n, primes)
        assert spectral == formula
        tuples.append((left, m, right, n))

    dilation_checks = 0
    for left, m, right, n in tuples[::37]:
        model = common_dilation_average(left, m, right, n, primes)
        formula = collision_formula(left, m, right, n, primes)
        assert model == formula
        dilation_checks += 1

    return {
        "primes": primes,
        "centres": centres,
        "sources": sources,
        "conductor_formula_checks": len(tuples),
        "complete_dilation_checks": dilation_checks,
        "group_size": math.prod(p - 1 for p in primes),
        "status": "PASS",
    }


def deterministic_defect_panel() -> dict:
    primes = [13, 17, 19]
    centres = [30, 210, 2310]
    sources = [p for p in primes_upto(97) if p > 19]
    points = [(centre, source) for centre in centres for source in sources]
    weights = [1 for _ in points]

    deterministic_linear = sum(
        (
            weight * deterministic_residual(centre, source, primes)
            for weight, (centre, source) in zip(weights, points, strict=True)
        ),
        Fraction(0),
    )
    deterministic_square = deterministic_linear * deterministic_linear
    diagonal_form = sum(
        (
            weights[a] * weights[b]
            * collision_formula(
                points[a][0], points[a][1], points[b][0], points[b][1], primes
            )
            for a in range(len(points))
            for b in range(len(points))
        ),
        Fraction(0),
    )
    defect = deterministic_square - diagonal_form

    survivor_witness = {
        "centre": 30,
        "source": 23,
        "deterministic_square": str(deterministic_residual(30, 23, primes) ** 2),
        "conductor_diagonal": str(collision_formula(30, 23, 30, 23, primes)),
    }
    killed_witness = {
        "centre": 210,
        "source": 37,
        "deterministic_square": str(deterministic_residual(210, 37, primes) ** 2),
        "conductor_diagonal": str(collision_formula(210, 37, 210, 37, primes)),
    }
    assert deterministic_residual(30, 23, primes) != -1
    assert deterministic_residual(210, 37, primes) == -1
    assert defect != 0

    return {
        "primes": primes,
        "centres": centres,
        "source_primes": sources,
        "point_count": len(points),
        "all_ones_deterministic_square": str(deterministic_square),
        "all_ones_conductor_diagonal_form": str(diagonal_form),
        "all_ones_cross_conductor_defect": str(defect),
        "survivor_single_point_witness": survivor_witness,
        "killed_single_point_witness": killed_witness,
        "status": "PASS",
    }


def self_coordinate_panel() -> dict:
    primes = [13, 17, 19]
    centre = 30
    checked = 0
    for self_prime in primes:
        reduced = [p for p in primes if p != self_prime]
        factor = Fraction(self_prime - 1, self_prime - 2)
        drift = Fraction(1, self_prime - 2)
        for dilation_reduced in unit_group(reduced):
            full_dilation = []
            iterator = iter(dilation_reduced)
            for p in primes:
                full_dilation.append(1 if p == self_prime else next(iterator))
            direct = residual_from_coordinates(
                centre, self_prime, tuple(full_dilation), primes
            )
            reduced_value = residual_from_coordinates(
                centre, self_prime, dilation_reduced, reduced
            )
            assert direct == factor * reduced_value + drift
            checked += 1
    return {
        "primes": primes,
        "centre": centre,
        "checks": checked,
        "status": "PASS",
    }


def evaluation_no_go_panel(primes: list[int]) -> dict:
    group_size = math.prod(p - 1 for p in primes)
    point_value_square = (group_size - 1) ** 2
    mean_square = group_size - 1
    ratio = Fraction(point_value_square, mean_square)
    assert ratio == group_size - 1
    nontrivial_fourier_support = sum(
        (
            phi_dagger(q, primes)
            for q in squarefree_divisors(primes)
            if q > 1
        )
    )
    assert nontrivial_fourier_support == group_size - 1
    return {
        "primes": primes,
        "group_size": group_size,
        "nontrivial_fourier_support": nontrivial_fourier_support,
        "sharp_point_evaluation_ratio": str(ratio),
        "status": "PASS",
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "four_point_common_dilation_kernel": four_point_kernel_panel(),
            "primorial_collision_reduction": collision_reduction_panel(),
            "self_coordinate_reduction": self_coordinate_panel(),
            "fourth_and_nontrivial_mode_energy": exact_energy_panel([5, 7, 11]),
            "single_prime_dilation_mode_energy": low_conductor_energy_panel([5, 7, 11]),
            "point_evaluation_no_go": evaluation_no_go_panel([13, 17, 19]),
            "deterministic_cross_conductor_defect": deterministic_defect_panel(),
        },
        "numerical_cyclotomic": {
            "dilation_wigner_reconstruction": wigner_panel([5, 7]),
        },
        "boundary": (
            "The collision kernel is exact, but it is the common-dilation average and "
            "the Q=Q' conductor diagonal. The deterministic square contains a nontrivial "
            "dilation spectrum encoding all Q!=Q' cross-conductor terms. The low "
            "single-prime modes localize sharply at collision primes, but transferring "
            "their small model energy to the rigid prime-candidate sample remains open."
        ),
    }
    output = Path(__file__).with_name("four_point_dilation_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
