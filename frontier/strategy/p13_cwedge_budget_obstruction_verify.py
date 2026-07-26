#!/usr/bin/env python3
"""Exact p=13 obstruction to the literal C_wedge terminal Betti budget.

The script computes the kernel of

    Omega_{1,12}(-zeta_13^{-1}) = sum_{j=1}^{13} eta^(j-1) (j ... 1)

on hook modules wedge^h Std_13. In --exact mode it Galois-interpolates
canonical modular kernels, combines auxiliary primes by CRT, rationally
reconstructs vectors over Q(zeta_13), verifies them symbolically modulo
Phi_13, and matches their dimension with a nonzero modular maximal minor.

Exact results used by the theorem:
    h=3: nullity 2
    h=4: nullity 5
    h=5: nullity 5
    h=6: nullity 5
Their sum is 17 > 12 = p-1, before the sign hook.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
from itertools import combinations, product
from math import comb, gcd
from typing import Dict, List, Sequence, Tuple

import numpy as np

from p11_cwedge_cyclotomic_lift_verify import (
    crt_pair,
    matrix_inverse_mod,
    primitive_root_mod,
    rational_reconstruct,
    right_nullspace,
)

P = 13
EXPECTED = {3: 2, 4: 5, 5: 5, 6: 5}
AUXILIARY = {
    3: (1093, 1171, 1223, 1249, 1301, 1327),
    4: (1093, 1171, 1223, 1249, 1301, 1327),
    5: (1093, 1171, 1223, 1249, 1301, 1327, 1483, 1613),
    6: (1093, 1171, 1223, 1249, 1301, 1327, 1483, 1613, 1847, 1873),
}
EXPECTED_DENOMINATOR = {3: 7787, 4: 6071, 5: 27659567, 6: 53205883679}


def cycle_permutation(length: int) -> List[int]:
    permutation = list(range(P))
    if length >= 2:
        permutation[0] = length - 1
        for position in range(1, length):
            permutation[position] = position - 1
    return permutation


def standard_matrix_mod(permutation: Sequence[int], modulus: int) -> np.ndarray:
    dimension = P - 1
    matrix = np.zeros((dimension, dimension), dtype=np.int64)
    for column in range(dimension):
        positive = permutation[column]
        negative = permutation[dimension]
        if positive < dimension:
            matrix[positive, column] = (matrix[positive, column] + 1) % modulus
        if negative < dimension:
            matrix[negative, column] = (matrix[negative, column] - 1) % modulus
    return matrix


def wedge_columns_mod(matrix: np.ndarray, degree: int, modulus: int):
    dimension = matrix.shape[0]
    subsets = list(combinations(range(dimension), degree))
    index = {subset: i for i, subset in enumerate(subsets)}
    columns = []
    for source in subsets:
        partial: Dict[Tuple[int, ...], int] = {(): 1}
        for column in source:
            updated: Dict[Tuple[int, ...], int] = {}
            for rows, coefficient in partial.items():
                for row in range(dimension):
                    value = int(matrix[row, column]) % modulus
                    if value:
                        key = rows + (row,)
                        updated[key] = (updated.get(key, 0) + coefficient * value) % modulus
            partial = updated
        output: Dict[int, int] = {}
        for rows, coefficient in partial.items():
            if len(set(rows)) != degree:
                continue
            inversions = sum(
                rows[i] > rows[j]
                for i in range(degree)
                for j in range(i + 1, degree)
            )
            target = index[tuple(sorted(rows))]
            value = coefficient if inversions % 2 == 0 else -coefficient
            output[target] = (output.get(target, 0) + value) % modulus
        columns.append(output)
    return columns


def omega_mod(degree: int, modulus: int, zeta: int) -> np.ndarray:
    eta = (-pow(zeta, -1, modulus)) % modulus
    dimension = comb(P - 1, degree)
    operator = np.zeros((dimension, dimension), dtype=np.int64)
    for length in range(1, P + 1):
        columns = wedge_columns_mod(
            standard_matrix_mod(cycle_permutation(length), modulus),
            degree,
            modulus,
        )
        scalar = pow(eta, length - 1, modulus)
        for column, terms in enumerate(columns):
            for row, value in terms.items():
                operator[row, column] = (
                    operator[row, column] + scalar * value
                ) % modulus
    return operator


def interpolation(values: np.ndarray, roots: Sequence[int], modulus: int) -> np.ndarray:
    vandermonde = np.array(
        [[pow(int(root), degree, modulus) for degree in range(P - 1)] for root in roots],
        dtype=np.int64,
    )
    inverse = matrix_inverse_mod(vandermonde, modulus)
    _, basis_size, coordinates = values.shape
    result = np.zeros((basis_size, coordinates, P - 1), dtype=np.int64)
    for basis_index in range(basis_size):
        result[basis_index] = (inverse.dot(values[:, basis_index, :]) % modulus).T
    return result


def embedding_task(arguments):
    degree, modulus, exponent = arguments
    generator = primitive_root_mod(modulus)
    zeta = pow(generator, (modulus - 1) // P, modulus)
    root = pow(zeta, exponent, modulus)
    operator = omega_mod(degree, modulus, root)
    kernel, free, rank = right_nullspace(operator.T, modulus)
    return exponent, root, kernel, free, rank


def reconstruct_kernel(degree: int):
    residues = None
    combined_modulus = 1
    free_reference = None
    modular_rank = None
    for modulus in AUXILIARY[degree]:
        with ProcessPoolExecutor(max_workers=P - 1) as executor:
            results = list(
                executor.map(
                    embedding_task,
                    [(degree, modulus, exponent) for exponent in range(1, P)],
                )
            )
        results.sort()
        kernels, roots = [], []
        for exponent, root, kernel, free, rank in results:
            if free_reference is None:
                free_reference = free
            assert free == free_reference
            if modulus == AUXILIARY[degree][0] and exponent == 1:
                modular_rank = rank
            kernels.append(kernel)
            roots.append(root)
        coefficients = interpolation(np.stack(kernels), roots, modulus)
        if residues is None:
            residues = coefficients.astype(object)
            combined_modulus = modulus
        else:
            updated = np.empty_like(residues, dtype=object)
            for index, value in np.ndenumerate(coefficients):
                updated[index] = crt_pair(
                    int(residues[index]),
                    combined_modulus,
                    int(value),
                    modulus,
                )
            residues = updated
            combined_modulus *= modulus
        print(f"hook {degree}: auxiliary prime {modulus}: PASS")

    assert residues is not None and free_reference is not None and modular_rank is not None
    rational = np.empty(residues.shape, dtype=object)
    for index, value in np.ndenumerate(residues):
        rational[index] = rational_reconstruct(int(value), combined_modulus)
    denominator = 1
    for value in rational.flat:
        denominator = denominator * value.denominator // gcd(denominator, value.denominator)
    integral = np.empty(rational.shape, dtype=object)
    for index, value in np.ndenumerate(rational):
        integral[index] = value.numerator * (denominator // value.denominator)
    return integral, denominator, free_reference, modular_rank


def standard_matrix_int(permutation: Sequence[int]) -> List[List[int]]:
    dimension = P - 1
    matrix = [[0] * dimension for _ in range(dimension)]
    for column in range(dimension):
        positive = permutation[column]
        negative = permutation[dimension]
        if positive < dimension:
            matrix[positive][column] += 1
        if negative < dimension:
            matrix[negative][column] -= 1
    return matrix


def wedge_columns_int(matrix: List[List[int]], degree: int):
    dimension = len(matrix)
    subsets = list(combinations(range(dimension), degree))
    index = {subset: i for i, subset in enumerate(subsets)}
    column_terms = [
        [(row, matrix[row][column]) for row in range(dimension) if matrix[row][column]]
        for column in range(dimension)
    ]
    columns = []
    for source in subsets:
        output: Dict[int, int] = {}
        for choices in product(*(column_terms[column] for column in source)):
            rows = tuple(choice[0] for choice in choices)
            if len(set(rows)) != degree:
                continue
            inversions = sum(
                rows[i] > rows[j]
                for i in range(degree)
                for j in range(i + 1, degree)
            )
            coefficient = 1
            for _, value in choices:
                coefficient *= value
            if inversions % 2:
                coefficient = -coefficient
            target = index[tuple(sorted(rows))]
            output[target] = output.get(target, 0) + coefficient
        columns.append(output)
    return columns


def multiply_mod_phi(left: Sequence[int], right: Sequence[int]) -> List[int]:
    raw = [0] * (2 * (P - 1) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            raw[i + j] += int(x) * int(y)
    cyclic = [0] * P
    for exponent, coefficient in enumerate(raw):
        cyclic[exponent % P] += coefficient
    final = cyclic[P - 1]
    return [cyclic[i] - final for i in range(P - 1)]


def eta_power(exponent: int) -> List[int]:
    zeta_exponent = (-exponent) % P
    sign = -1 if exponent % 2 else 1
    if zeta_exponent < P - 1:
        result = [0] * (P - 1)
        result[zeta_exponent] = sign
        return result
    return [-sign] * (P - 1)


def verify_exact_kernel(degree: int, kernel: np.ndarray) -> None:
    kernel_size, dimension, _ = kernel.shape
    result = [[[0] * (P - 1) for _ in range(dimension)] for _ in range(kernel_size)]
    for length in range(1, P + 1):
        columns = wedge_columns_int(
            standard_matrix_int(cycle_permutation(length)), degree
        )
        scalar = eta_power(length - 1)
        for column, terms in enumerate(columns):
            for row, integer in terms.items():
                for basis_index in range(kernel_size):
                    entry = kernel[basis_index, row]
                    if any(entry):
                        product_coefficients = multiply_mod_phi(entry, scalar)
                        target = result[basis_index][column]
                        for coefficient_index in range(P - 1):
                            target[coefficient_index] += (
                                integer * product_coefficients[coefficient_index]
                            )
    assert all(
        not any(result[basis_index][column])
        for basis_index in range(kernel_size)
        for column in range(dimension)
    )


def quick_modular_check() -> None:
    profiles = []
    for modulus in (1093, 1171, 2081):
        generator = primitive_root_mod(modulus)
        zeta = pow(generator, (modulus - 1) // P, modulus)
        profile = {}
        for degree in EXPECTED:
            operator = omega_mod(degree, modulus, zeta)
            _, _, rank = right_nullspace(operator.T, modulus)
            profile[degree] = operator.shape[0] - rank
        profiles.append(profile)
    assert all(profile == EXPECTED for profile in profiles)
    print("stable modular profile at three auxiliary primes: PASS")


def exact_check() -> None:
    total = 0
    for degree, expected_nullity in EXPECTED.items():
        kernel, denominator, free, modular_rank = reconstruct_kernel(degree)
        verify_exact_kernel(degree, kernel)
        nullity = kernel.shape[0]
        dimension = comb(P - 1, degree)
        assert nullity == expected_nullity
        assert modular_rank == dimension - nullity
        assert denominator == EXPECTED_DENOMINATOR[degree]
        for basis_index, coordinate in enumerate(free):
            assert int(kernel[basis_index, coordinate, 0]) == denominator
            assert all(
                int(kernel[basis_index, coordinate, power]) == 0
                for power in range(1, P - 1)
            )
        total += nullity
        print(
            f"hook {degree}: exact nullity {nullity}, "
            f"certificate denominator {denominator}: PASS"
        )
    assert total == 17
    assert total > P - 1
    print("exact hooks 3--6 total 17 > 12 = p-1: PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--exact",
        action="store_true",
        help="run the full cyclotomic certificate reconstruction",
    )
    arguments = parser.parse_args()
    quick_modular_check()
    if arguments.exact:
        exact_check()
    print("P13_CWEDGE_BUDGET_OBSTRUCTION_VERIFY: PASS")


if __name__ == "__main__":
    main()
