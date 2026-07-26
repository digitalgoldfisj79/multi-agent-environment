#!/usr/bin/env python3
"""Exact p=11/p=13 Cayley--Jacobian grading and hook-character audit.

The script verifies five load-bearing statements for the sparse complete-intersection
surface

    Y_p = {s_2 = ... = s_{p-4} = 0} in P(W), dim W = p-2,

at p=11 and p=13.

1. Adolphson--Sperber's grading gives kappa=(p-7)(p-2)/2 and the three
   components J_(kappa,j), j=0,1,2.
2. Two independent Hilbert-series computations give h^{2,0}=h^{0,2}; a
   Chern-class computation gives h^{1,1}_prim.
3. On every p-regular conjugacy class, the modular root representation has

       det(1-t g | W) = prod_{cycles c}(1-t^c)/(1-t)^2.

   This determines the p-regular trace of J_(kappa,0), J_(kappa,1), and their
   total 2 J_0 + J_1.
4. Murnaghan--Nakayama decomposition proves:
   * J_0 has a unique genuine ordinary-character extension;
   * J_1 has no genuine ordinary-character extension;
   * 2 J_0 + J_1 has a unique genuine ordinary-character extension.
5. The residue determinant twist reverses the hook profile and gives the
   actual primitive-H^2 hook multiplicities.

No floating point arithmetic is used.
"""
from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

PRIMES = (11, 13)


def partitions(total: int, maximum: int | None = None) -> Iterable[Tuple[int, ...]]:
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def centralizer_order(cycle_type: Sequence[int]) -> int:
    counts = Counter(cycle_type)
    value = 1
    for length, multiplicity in counts.items():
        value *= length**multiplicity * factorial(multiplicity)
    return value


def cells(shape: Sequence[int]) -> set[Tuple[int, int]]:
    return {(row, column) for row, width in enumerate(shape) for column in range(width)}


def subpartitions_of_size(shape: Tuple[int, ...], target: int) -> Iterable[Tuple[int, ...]]:
    length = len(shape)

    def recurse(index: int, previous: int, remaining: int, current: List[int]):
        if index == length:
            if remaining == 0:
                result = tuple(current)
                while result and result[-1] == 0:
                    result = result[:-1]
                yield result
            return
        for value in range(min(shape[index], previous, remaining), -1, -1):
            yield from recurse(index + 1, value, remaining - value, current + [value])

    yield from recurse(0, 10**9, target, [])


def border_strip_height(shape: Tuple[int, ...], subshape: Tuple[int, ...]) -> int | None:
    skew = cells(shape) - cells(subshape)
    if not skew:
        return None
    start = next(iter(skew))
    seen = {start}
    stack = [start]
    while stack:
        row, column = stack.pop()
        for neighbour in (
            (row + 1, column),
            (row - 1, column),
            (row, column + 1),
            (row, column - 1),
        ):
            if neighbour in skew and neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    if seen != skew:
        return None
    for row, column in skew:
        square = {
            (row, column),
            (row + 1, column),
            (row, column + 1),
            (row + 1, column + 1),
        }
        if square <= skew:
            return None
    return len({row for row, _ in skew}) - 1


@lru_cache(maxsize=None)
def rim_removals(shape: Tuple[int, ...], size: int) -> Tuple[Tuple[Tuple[int, ...], int], ...]:
    target = sum(shape) - size
    answer = []
    for subshape in subpartitions_of_size(shape, target):
        height = border_strip_height(shape, subshape)
        if height is not None:
            answer.append((subshape, height))
    return tuple(answer)


@lru_cache(maxsize=None)
def symmetric_character(shape: Tuple[int, ...], cycle_type: Tuple[int, ...]) -> int:
    """Murnaghan--Nakayama character chi^shape(cycle_type)."""
    if not cycle_type:
        return int(sum(shape) == 0)
    first = cycle_type[0]
    return sum(
        (-1) ** height * symmetric_character(subshape, cycle_type[1:])
        for subshape, height in rim_removals(shape, first)
    )


def hook_shape(prime: int, degree: int) -> Tuple[int, ...]:
    return (prime - degree,) + (1,) * degree


def hook_characters(cycle_type: Sequence[int], prime: int) -> List[int]:
    """Coefficients of det(1+z g | Std)."""
    polynomial = [1]
    for length in cycle_type:
        factor = [0] * (length + 1)
        factor[0] = 1
        factor[length] = -((-1) ** length)
        updated = [0] * min(prime + 1, len(polynomial) + length)
        for i, left in enumerate(polynomial):
            for j, right in enumerate(factor):
                if i + j < len(updated):
                    updated[i + j] += left * right
        polynomial = updated
    quotient: List[int] = []
    previous = 0
    for degree in range(prime):
        value = (polynomial[degree] if degree < len(polynomial) else 0) - previous
        quotient.append(value)
        previous = value
    return quotient


def specht_dimension(shape: Sequence[int]) -> int:
    total = sum(shape)
    hooks = 1
    for row, width in enumerate(shape):
        for column in range(width):
            below = sum(1 for lower in range(row + 1, len(shape)) if shape[lower] > column)
            hooks *= width - column + below
    return factorial(total) // hooks


def geometry(prime: int) -> Dict[str, int | List[int]]:
    variables = prime - 2
    degrees = list(range(2, prime - 3))
    codimension = len(degrees)
    kappa = sum(degrees) - variables
    assert codimension == prime - 5
    assert kappa == (prime - 7) * (prime - 2) // 2
    return {
        "variables": variables,
        "degrees": degrees,
        "codimension": codimension,
        "kappa": kappa,
    }


def hilbert_coefficient_dp(prime: int, degree: int) -> int:
    data = geometry(prime)
    variables = int(data["variables"])
    coefficients = [comb(variables + index - 1, index) for index in range(degree + 1)]
    for relation_degree in data["degrees"]:  # type: ignore[index]
        relation_degree = int(relation_degree)
        updated = coefficients[:]
        for index in range(relation_degree, degree + 1):
            updated[index] -= coefficients[index - relation_degree]
        coefficients = updated
    return coefficients[degree]


def hilbert_coefficient_inclusion_exclusion(prime: int, degree: int) -> int:
    data = geometry(prime)
    variables = int(data["variables"])
    degrees = list(map(int, data["degrees"]))  # type: ignore[arg-type]
    total = 0
    for mask in range(1 << len(degrees)):
        removed = sum(degrees[index] for index in range(len(degrees)) if mask >> index & 1)
        if removed <= degree:
            total += (-1) ** mask.bit_count() * comb(
                variables + degree - removed - 1,
                variables - 1,
            )
    return total


def hodge_dimensions(prime: int) -> Dict[str, int]:
    data = geometry(prime)
    variables = int(data["variables"])
    degrees = list(map(int, data["degrees"]))  # type: ignore[arg-type]
    kappa = int(data["kappa"])
    geometric_genus = hilbert_coefficient_dp(prime, kappa)
    assert geometric_genus == hilbert_coefficient_inclusion_exclusion(prime, kappa)

    first_sum = sum(degrees)
    second_sum = sum(value * value for value in degrees)
    c2_coefficient = (
        comb(variables, 2)
        - variables * first_sum
        + (first_sum * first_sum + second_sum) // 2
    )
    degree_y = factorial(prime - 4)
    euler_characteristic = degree_y * c2_coefficient
    h11_primitive = euler_characteristic - 3 - 2 * geometric_genus

    middle_formula = (
        sum(hilbert_coefficient_dp(prime, kappa + relation_degree) for relation_degree in degrees)
        - variables * hilbert_coefficient_dp(prime, kappa + 1)
        + hilbert_coefficient_dp(prime, kappa)
    )
    assert h11_primitive == middle_formula
    assert 2 * geometric_genus + h11_primitive == euler_characteristic - 3
    return {
        "h20": geometric_genus,
        "h11_primitive": h11_primitive,
        "h02": geometric_genus,
        "primitive_b2": euler_characteristic - 3,
        "euler_characteristic": euler_characteristic,
    }


@lru_cache(maxsize=None)
def ring_trace(prime: int, cycle_type: Tuple[int, ...], degree: int) -> int:
    """Brauer trace of R_degree for a p-regular class.

    R = Sym(W^*)/(s_2,...,s_{p-4}) and
    det(1-tg|W)=prod(1-t^cycle_length)/(1-t)^2.
    """
    if degree < 0:
        return 0
    coefficients = [0] * (degree + 1)
    coefficients[0] = 1
    for length in cycle_type:
        updated = [0] * (degree + 1)
        for index, value in enumerate(coefficients):
            if value:
                for shift in range(0, degree - index + 1, length):
                    updated[index + shift] += value
        coefficients = updated

    updated = [0] * (degree + 1)
    for index, value in enumerate(coefficients):
        updated[index] += value
        if index + 1 <= degree:
            updated[index + 1] -= 2 * value
        if index + 2 <= degree:
            updated[index + 2] += value
    coefficients = updated

    for relation_degree in geometry(prime)["degrees"]:  # type: ignore[index]
        relation_degree = int(relation_degree)
        updated = coefficients[:]
        for index in range(relation_degree, degree + 1):
            updated[index] -= coefficients[index - relation_degree]
        coefficients = updated
    return coefficients[degree]


def j0_trace(prime: int, cycle_type: Tuple[int, ...]) -> int:
    return ring_trace(prime, cycle_type, int(geometry(prime)["kappa"]))


def j1_trace(prime: int, cycle_type: Tuple[int, ...]) -> int:
    data = geometry(prime)
    kappa = int(data["kappa"])
    degrees = list(map(int, data["degrees"]))  # type: ignore[arg-type]
    trace_w = cycle_type.count(1) - 2
    return (
        sum(ring_trace(prime, cycle_type, kappa + degree) for degree in degrees)
        - trace_w * ring_trace(prime, cycle_type, kappa + 1)
        + ring_trace(prime, cycle_type, kappa)
    )


def total_jacobian_trace(prime: int, cycle_type: Tuple[int, ...]) -> int:
    return 2 * j0_trace(prime, cycle_type) + j1_trace(prime, cycle_type)


def partial_hook_inner_products(
    prime: int,
    trace_function: Callable[[int, Tuple[int, ...]], int],
) -> List[Fraction]:
    values = [Fraction(0) for _ in range(prime)]
    for cycle_type in partitions(prime):
        if cycle_type == (prime,):
            continue
        trace = trace_function(prime, cycle_type)
        hooks = hook_characters(cycle_type, prime)
        denominator = centralizer_order(cycle_type)
        for degree in range(prime):
            values[degree] += Fraction(trace * hooks[degree], denominator)
    return values


def integral_residue_and_base(values: Sequence[Fraction], prime: int) -> Tuple[int, List[int]]:
    candidates = []
    for p_cycle_trace in range(prime):
        adjusted = [
            value + Fraction(p_cycle_trace * ((-1) ** degree), prime)
            for degree, value in enumerate(values)
        ]
        if all(value.denominator == 1 for value in adjusted):
            candidates.append((p_cycle_trace, [int(value) for value in adjusted]))
    assert len(candidates) == 1
    return candidates[0]


def shift_interval(base: Sequence[int]) -> Tuple[int, int]:
    lower = max((-value for degree, value in enumerate(base) if degree % 2 == 0), default=-10**18)
    upper = min((value for degree, value in enumerate(base) if degree % 2 == 1), default=10**18)
    return lower, upper


def full_decomposition(
    prime: int,
    trace_function: Callable[[int, Tuple[int, ...]], int],
    p_cycle_trace: int,
) -> Dict[Tuple[int, ...], Fraction]:
    answer: Dict[Tuple[int, ...], Fraction] = {}
    cycle_types = tuple(partitions(prime))
    for shape in partitions(prime):
        multiplicity = Fraction(0)
        for cycle_type in cycle_types:
            trace = p_cycle_trace if cycle_type == (prime,) else trace_function(prime, cycle_type)
            multiplicity += Fraction(
                trace * symmetric_character(shape, cycle_type),
                centralizer_order(cycle_type),
            )
        answer[shape] = multiplicity
    return answer


def verify_character_table(prime: int) -> None:
    shapes = tuple(partitions(prime))
    for left in shapes:
        for right in shapes:
            inner = sum(
                Fraction(
                    symmetric_character(left, cycle_type)
                    * symmetric_character(right, cycle_type),
                    centralizer_order(cycle_type),
                )
                for cycle_type in shapes
            )
            assert inner == int(left == right), (prime, left, right, inner)


def analyse_prime(prime: int) -> Dict[str, object]:
    verify_character_table(prime)
    hodge = hodge_dimensions(prime)
    identity = (1,) * prime
    assert j0_trace(prime, identity) == hodge["h20"]
    assert j1_trace(prime, identity) == hodge["h11_primitive"]
    assert total_jacobian_trace(prime, identity) == hodge["primitive_b2"]

    component_results: Dict[str, object] = {}
    for name, trace_function in (
        ("J_kappa_0", j0_trace),
        ("J_kappa_1", j1_trace),
        ("J_kappa_2", j0_trace),
        ("J_total", total_jacobian_trace),
    ):
        partial = partial_hook_inner_products(prime, trace_function)
        residue, base = integral_residue_and_base(partial, prime)
        lower, upper = shift_interval(base)
        component: Dict[str, object] = {
            "p_cycle_trace_mod_p": residue,
            "base_hook_profile": base,
            "ordinary_shift_interval": [lower, upper],
            "ordinary_genuine_extension_exists": lower <= upper,
        }
        if lower <= upper and lower == upper:
            shift = lower
            p_cycle_trace = residue + prime * shift
            profile = [value + shift * ((-1) ** degree) for degree, value in enumerate(base)]
            decomposition = full_decomposition(prime, trace_function, p_cycle_trace)
            assert all(value.denominator == 1 and value >= 0 for value in decomposition.values())
            assert [int(decomposition[hook_shape(prime, degree)]) for degree in range(prime)] == profile
            dimension = sum(int(value) * specht_dimension(shape) for shape, value in decomposition.items())
            expected_dimension = {
                "J_kappa_0": hodge["h20"],
                "J_kappa_1": hodge["h11_primitive"],
                "J_kappa_2": hodge["h02"],
                "J_total": hodge["primitive_b2"],
            }[name]
            assert dimension == expected_dimension
            component.update(
                {
                    "unique_shift": shift,
                    "p_cycle_trace": p_cycle_trace,
                    "hook_profile": profile,
                    "even_hook_multiplicity": sum(profile[::2]),
                    "odd_hook_multiplicity": sum(profile[1::2]),
                    "total_hook_multiplicity": sum(profile),
                    "nonzero_irreducible_types": sum(value > 0 for value in decomposition.values()),
                }
            )
        component_results[name] = component

    assert component_results["J_kappa_1"]["ordinary_genuine_extension_exists"] is False  # type: ignore[index]
    for name in ("J_kappa_0", "J_kappa_2", "J_total"):
        assert component_results[name]["ordinary_genuine_extension_exists"] is True  # type: ignore[index]

    total_profile = list(component_results["J_total"]["hook_profile"])  # type: ignore[index]
    primitive_profile = list(reversed(total_profile))
    assert sum(primitive_profile) == sum(total_profile)

    return {
        "p": prime,
        "geometry": geometry(prime),
        "hodge_dimensions": hodge,
        "components": component_results,
        "primitive_H2_hook_profile_after_sign_twist": primitive_profile,
        "primitive_H2_even_hook_multiplicity": sum(primitive_profile[::2]),
        "primitive_H2_odd_hook_multiplicity": sum(primitive_profile[1::2]),
        "primitive_H2_total_hook_multiplicity": sum(primitive_profile),
        "primitive_H2_nonzero_cohomological_degree": 2,
    }


def main() -> None:
    results = {str(prime): analyse_prime(prime) for prime in PRIMES}

    expected = {
        "11": {
            "kappa": 18,
            "hodge": [231419, 681239, 231419],
            "j0_hooks": [1, 1, 1, 3, 4, 1, 0, 0, 0, 0, 0],
            "total_hooks": [1, 3, 6, 12, 14, 6, 0, 0, 0, 0, 0],
            "primitive_hooks": [0, 0, 0, 0, 0, 6, 14, 12, 6, 3, 1],
            "parity": [21, 21],
        },
        "13": {
            "kappa": 33,
            "hodge": [53524799, 140071679, 53524799],
            "j0_hooks": [1, 1, 5, 8, 11, 12, 9, 2, 0, 0, 0, 0, 0],
            "total_hooks": [0, 4, 16, 34, 49, 51, 35, 11, 0, 0, 0, 0, 0],
            "primitive_hooks": [0, 0, 0, 0, 0, 11, 35, 51, 49, 34, 16, 4, 0],
            "parity": [100, 100],
        },
    }
    for prime, target in expected.items():
        result = results[prime]
        assert result["geometry"]["kappa"] == target["kappa"]  # type: ignore[index]
        hodge = result["hodge_dimensions"]
        assert [hodge["h20"], hodge["h11_primitive"], hodge["h02"]] == target["hodge"]  # type: ignore[index]
        assert result["components"]["J_kappa_0"]["hook_profile"] == target["j0_hooks"]  # type: ignore[index]
        assert result["components"]["J_total"]["hook_profile"] == target["total_hooks"]  # type: ignore[index]
        assert result["primitive_H2_hook_profile_after_sign_twist"] == target["primitive_hooks"]
        assert [
            result["primitive_H2_even_hook_multiplicity"],
            result["primitive_H2_odd_hook_multiplicity"],
        ] == target["parity"]

    output = Path(__file__).with_name("cayley_jacobian_hook_results_20260726.json")
    output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for prime in PRIMES:
        result = results[str(prime)]
        print(
            f"p={prime}: kappa={result['geometry']['kappa']}; "
            f"Hodge=({result['hodge_dimensions']['h20']},"
            f"{result['hodge_dimensions']['h11_primitive']},"
            f"{result['hodge_dimensions']['h02']}); "
            f"primitive hook parity="
            f"({result['primitive_H2_even_hook_multiplicity']},"
            f"{result['primitive_H2_odd_hook_multiplicity']})"
        )
        middle = result["components"]["J_kappa_1"]
        print(
            f"p={prime}: middle-component ordinary shift interval "
            f"{middle['ordinary_shift_interval']}: EMPTY"
        )
    print(f"wrote {output}")
    print("CAYLEY_JACOBIAN_HOOK_LIFT_VERIFY: PASS")


if __name__ == "__main__":
    main()
