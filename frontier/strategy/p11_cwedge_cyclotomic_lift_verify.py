#!/usr/bin/env python3
"""Exact p=11 cyclotomic lift for the terminal C_wedge H_1 profile.

The order-11 terminal indecomposable quotient is reduced to the one-sided
quantum-shuffle operator

    Omega = sum_{j=1}^{11} eta^(j-1) (1 j j-1 ... 2),
    eta = -zeta_11^(-1),

on hook modules wedge^h Std_11. The verifier proves the exact nullity profile
over Q(zeta_11) by exact modular Galois interpolation, CRT, rational
reconstruction, symbolic verification modulo Phi_11, and a matching nonzero
modular minor.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb, gcd, isqrt
from typing import List, Sequence

import numpy as np

try:
    from numba import njit
except ImportError:  # pragma: no cover
    njit = None

P = 11
AUXILIARY_PRIMES = (1013, 2003, 3037, 4027, 4049)
EXPECTED = {
    0: 0,
    1: 0,
    2: 1,
    3: 1,
    4: 1,
    5: 3,
    6: 3,
    7: 1,
    8: 0,
    9: 0,
    10: 1,
}


def primitive_root_mod(prime: int) -> int:
    n = prime - 1
    factors: List[int] = []
    x, d = n, 2
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        factors.append(x)
    for generator in range(2, prime):
        if all(pow(generator, n // factor, prime) != 1 for factor in factors):
            return generator
    raise RuntimeError("primitive root not found")


if njit is not None:

    @njit(cache=True)
    def _inverse_mod(value: int, modulus: int) -> int:
        t, new_t, r, new_r = 0, 1, modulus, value % modulus
        while new_r:
            quotient = r // new_r
            t, new_t = new_t, t - quotient * new_t
            r, new_r = new_r, r - quotient * new_r
        return t % modulus

    @njit(cache=True)
    def _rref_mod(matrix: np.ndarray, modulus: int):
        a = matrix.copy() % modulus
        rows, columns = a.shape
        pivots = np.empty(min(rows, columns), dtype=np.int64)
        pivots[:] = -1
        rank = 0
        for column in range(columns):
            pivot = -1
            for row in range(rank, rows):
                if a[row, column] % modulus:
                    pivot = row
                    break
            if pivot < 0:
                continue
            if pivot != rank:
                temporary = a[rank].copy()
                a[rank] = a[pivot]
                a[pivot] = temporary
            inverse = _inverse_mod(int(a[rank, column]), modulus)
            for j in range(column, columns):
                a[rank, j] = a[rank, j] * inverse % modulus
            for row in range(rows):
                if row == rank:
                    continue
                factor = a[row, column] % modulus
                if factor:
                    for j in range(column, columns):
                        a[row, j] = (
                            a[row, j] - factor * a[rank, j]
                        ) % modulus
            pivots[rank] = column
            rank += 1
            if rank == rows:
                break
        return a, rank, pivots

else:  # pragma: no cover

    def _rref_mod(matrix: np.ndarray, modulus: int):
        a = matrix.copy() % modulus
        rows, columns = a.shape
        pivot_list = []
        rank = 0
        for column in range(columns):
            pivot = next(
                (row for row in range(rank, rows) if a[row, column] % modulus),
                None,
            )
            if pivot is None:
                continue
            if pivot != rank:
                a[[rank, pivot]] = a[[pivot, rank]]
            a[rank] = (
                a[rank] * pow(int(a[rank, column]), -1, modulus)
            ) % modulus
            for row in range(rows):
                if row != rank and a[row, column] % modulus:
                    a[row] = (
                        a[row] - a[row, column] * a[rank]
                    ) % modulus
            pivot_list.append(column)
            rank += 1
        pivots = np.full(min(rows, columns), -1, dtype=np.int64)
        pivots[: len(pivot_list)] = pivot_list
        return a, rank, pivots


def right_nullspace(matrix: np.ndarray, modulus: int):
    rref, rank, raw_pivots = _rref_mod(matrix, modulus)
    pivots = tuple(map(int, raw_pivots[:rank]))
    pivot_set = set(pivots)
    free = tuple(
        column for column in range(matrix.shape[1]) if column not in pivot_set
    )
    kernel = np.zeros((len(free), matrix.shape[1]), dtype=np.int64)
    for basis_index, free_column in enumerate(free):
        kernel[basis_index, free_column] = 1
        for row, pivot_column in enumerate(pivots):
            kernel[basis_index, pivot_column] = (-rref[row, free_column]) % modulus
    return kernel, free, rank


def matrix_inverse_mod(matrix: np.ndarray, modulus: int) -> np.ndarray:
    size = matrix.shape[0]
    augmented = np.concatenate(
        [matrix % modulus, np.eye(size, dtype=np.int64)], axis=1
    )
    rref, rank, pivots = _rref_mod(augmented, modulus)
    assert rank == size
    assert tuple(map(int, pivots[:size])) == tuple(range(size))
    return rref[:, size:] % modulus


def cycle_permutation(n: int, length: int) -> List[int]:
    permutation = list(range(n))
    if length >= 2:
        permutation[0] = length - 1
        for position in range(1, length):
            permutation[position] = position - 1
    return permutation


def standard_matrix_mod(
    permutation: Sequence[int], modulus: int
) -> np.ndarray:
    dimension = len(permutation) - 1
    matrix = np.zeros((dimension, dimension), dtype=np.int64)
    for column in range(dimension):
        positive = permutation[column]
        negative = permutation[dimension]
        if positive < dimension:
            matrix[positive, column] = (
                matrix[positive, column] + 1
            ) % modulus
        if negative < dimension:
            matrix[negative, column] = (
                matrix[negative, column] - 1
            ) % modulus
    return matrix


def wedge_matrix_mod(
    matrix: np.ndarray, degree: int, modulus: int
) -> np.ndarray:
    dimension = matrix.shape[0]
    if degree == 0:
        return np.array([[1]], dtype=np.int64)
    subsets = list(combinations(range(dimension), degree))
    index = {subset: i for i, subset in enumerate(subsets)}
    wedge = np.zeros((len(subsets), len(subsets)), dtype=np.int64)
    column_terms = [
        [
            (row, int(matrix[row, column]))
            for row in range(dimension)
            if matrix[row, column] % modulus
        ]
        for column in range(dimension)
    ]
    for column, source in enumerate(subsets):
        for choices in product(*(column_terms[c] for c in source)):
            rows = tuple(choice[0] for choice in choices)
            if len(set(rows)) != degree:
                continue
            inversions = sum(
                rows[a] > rows[b]
                for a in range(degree)
                for b in range(a + 1, degree)
            )
            value = -1 if inversions % 2 else 1
            for _, coefficient in choices:
                value = value * coefficient % modulus
            target = tuple(sorted(rows))
            wedge[index[target], column] = (
                wedge[index[target], column] + value
            ) % modulus
    return wedge


def omega_mod(degree: int, modulus: int, zeta: int) -> np.ndarray:
    eta = (-pow(zeta, -1, modulus)) % modulus
    dimension = comb(10, degree)
    operator = np.zeros((dimension, dimension), dtype=np.int64)
    for length in range(1, 12):
        standard = standard_matrix_mod(
            cycle_permutation(11, length), modulus
        )
        wedge = wedge_matrix_mod(standard, degree, modulus)
        operator = (
            operator + pow(eta, length - 1, modulus) * wedge
        ) % modulus
    return operator


def interpolate(
    values: np.ndarray, roots: Sequence[int], modulus: int
) -> np.ndarray:
    vandermonde = np.array(
        [
            [pow(int(root), degree, modulus) for degree in range(10)]
            for root in roots
        ],
        dtype=np.int64,
    )
    inverse = matrix_inverse_mod(vandermonde, modulus)
    embeddings, basis_size, coordinates = values.shape
    assert embeddings == 10
    result = np.zeros((basis_size, coordinates, 10), dtype=np.int64)
    for basis_index in range(basis_size):
        result[basis_index] = (
            inverse.dot(values[:, basis_index, :]) % modulus
        ).T
    return result


def crt_pair(a: int, m: int, b: int, n: int) -> int:
    return a + ((b - a) * pow(m, -1, n) % n) * m


def rational_reconstruct(value: int, modulus: int) -> Fraction:
    bound = isqrt(modulus // 2)
    value %= modulus
    r0, r1, s0, s1 = modulus, value, 0, 1
    while r1 > bound:
        quotient = r0 // r1
        r0, r1 = r1, r0 - quotient * r1
        s0, s1 = s1, s0 - quotient * s1
    if s1 == 0:
        raise AssertionError("rational reconstruction failed")
    numerator, denominator = r1, s1
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    common = gcd(numerator, denominator)
    numerator //= common
    denominator //= common
    assert abs(numerator) <= bound and denominator <= bound
    assert (numerator - denominator * value) % modulus == 0
    return Fraction(numerator, denominator)


def reconstruct_kernel(degree: int):
    residues = None
    combined_modulus = 1
    free_reference = None
    modular_rank = None
    for modulus in AUXILIARY_PRIMES:
        generator = primitive_root_mod(modulus)
        zeta = pow(generator, (modulus - 1) // 11, modulus)
        kernels, roots = [], []
        for exponent in range(1, 11):
            root = pow(zeta, exponent, modulus)
            operator = omega_mod(degree, modulus, root)
            kernel, free, rank = right_nullspace(operator.T, modulus)
            if free_reference is None:
                free_reference = free
            assert free == free_reference
            if modulus == AUXILIARY_PRIMES[0] and exponent == 1:
                modular_rank = rank
            kernels.append(kernel)
            roots.append(root)
        coefficients = interpolate(np.stack(kernels), roots, modulus)
        if residues is None:
            residues = coefficients.astype(object)
            combined_modulus = modulus
        else:
            updated = np.empty_like(residues, dtype=object)
            for index, coefficient in np.ndenumerate(coefficients):
                updated[index] = crt_pair(
                    int(residues[index]),
                    combined_modulus,
                    int(coefficient),
                    modulus,
                )
            residues = updated
            combined_modulus *= modulus
    assert residues is not None and modular_rank is not None
    rational = np.empty(residues.shape, dtype=object)
    for index, coefficient in np.ndenumerate(residues):
        rational[index] = rational_reconstruct(
            int(coefficient), combined_modulus
        )
    denominator = 1
    for coefficient in rational.flat:
        denominator = (
            denominator
            * coefficient.denominator
            // gcd(denominator, coefficient.denominator)
        )
    integral = np.empty(rational.shape, dtype=object)
    for index, coefficient in np.ndenumerate(rational):
        integral[index] = coefficient.numerator * (
            denominator // coefficient.denominator
        )
    return integral, denominator, free_reference, modular_rank


def standard_matrix_int(permutation: Sequence[int]) -> List[List[int]]:
    dimension = len(permutation) - 1
    matrix = [[0] * dimension for _ in range(dimension)]
    for column in range(dimension):
        positive = permutation[column]
        negative = permutation[dimension]
        if positive < dimension:
            matrix[positive][column] += 1
        if negative < dimension:
            matrix[negative][column] -= 1
    return matrix


def determinant_small(matrix: List[List[int]]) -> int:
    dimension = len(matrix)
    if dimension == 0:
        return 1
    working = [row[:] for row in matrix]
    sign, previous = 1, 1
    for pivot_index in range(dimension - 1):
        if working[pivot_index][pivot_index] == 0:
            swap = next(
                (
                    row
                    for row in range(pivot_index + 1, dimension)
                    if working[row][pivot_index]
                ),
                None,
            )
            if swap is None:
                return 0
            working[pivot_index], working[swap] = (
                working[swap],
                working[pivot_index],
            )
            sign = -sign
        pivot = working[pivot_index][pivot_index]
        for row in range(pivot_index + 1, dimension):
            for column in range(pivot_index + 1, dimension):
                working[row][column] = (
                    working[row][column] * pivot
                    - working[row][pivot_index]
                    * working[pivot_index][column]
                ) // previous
        previous = pivot
    return sign * working[-1][-1]


def wedge_matrix_int(
    matrix: List[List[int]], degree: int
) -> List[List[int]]:
    if degree == 0:
        return [[1]]
    subsets = list(combinations(range(len(matrix)), degree))
    return [
        [
            determinant_small(
                [[matrix[row][column] for column in source] for row in target]
            )
            for source in subsets
        ]
        for target in subsets
    ]


def multiply_mod_phi(
    left: Sequence[int], right: Sequence[int]
) -> List[int]:
    raw = [0] * 19
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            raw[i + j] += int(x) * int(y)
    cyclic = [0] * 11
    for degree, coefficient in enumerate(raw):
        cyclic[degree % 11] += coefficient
    final = cyclic[10]
    return [cyclic[i] - final for i in range(10)]


def eta_power(exponent: int) -> List[int]:
    zeta_exponent = (-exponent) % 11
    sign = -1 if exponent % 2 else 1
    result = [0] * 10
    if zeta_exponent < 10:
        result[zeta_exponent] = sign
    else:
        result = [-sign] * 10
    return result


def verify_exact_left_kernel(degree: int, kernel: np.ndarray) -> None:
    basis_size, dimension, power_degree = kernel.shape
    assert power_degree == 10
    result = [
        [[0] * 10 for _ in range(dimension)]
        for _ in range(basis_size)
    ]
    for length in range(1, 12):
        wedge = wedge_matrix_int(
            standard_matrix_int(cycle_permutation(11, length)), degree
        )
        scalar = eta_power(length - 1)
        for basis_index in range(basis_size):
            for row in range(dimension):
                vector_entry = kernel[basis_index, row]
                if not any(vector_entry):
                    continue
                product_coefficients = multiply_mod_phi(
                    vector_entry, scalar
                )
                for column, integer in enumerate(wedge[row]):
                    if integer:
                        target = result[basis_index][column]
                        for coefficient_index in range(10):
                            target[coefficient_index] += (
                                integer
                                * product_coefficients[coefficient_index]
                            )
    assert all(
        not any(result[basis_index][column])
        for basis_index in range(basis_size)
        for column in range(dimension)
    )


def main() -> None:
    exact_profile = {0: 0, 10: 1}
    modulus = AUXILIARY_PRIMES[0]
    generator = primitive_root_mod(modulus)
    zeta = pow(generator, (modulus - 1) // 11, modulus)

    # Full modular rank proves characteristic-zero invertibility.
    for degree in (1, 8, 9):
        operator = omega_mod(degree, modulus, zeta)
        _, _, rank = right_nullspace(operator.T, modulus)
        assert rank == operator.shape[0]
        exact_profile[degree] = 0

    for degree in range(2, 8):
        kernel, denominator, free, modular_rank = reconstruct_kernel(degree)
        verify_exact_left_kernel(degree, kernel)
        nullity = kernel.shape[0]
        dimension = comb(10, degree)
        assert modular_rank == dimension - nullity
        for basis_index, coordinate in enumerate(free):
            assert int(kernel[basis_index, coordinate, 0]) == denominator
            assert all(
                int(kernel[basis_index, coordinate, power]) == 0
                for power in range(1, 10)
            )
        exact_profile[degree] = nullity
        print(
            f"hook {degree}: exact nullity {nullity}, "
            f"certificate denominator {denominator}"
        )

    # Trivial hook: sum eta^e = 2/(1-eta), nonzero.
    # Sign hook: eta^e sign(sigma_{e+1}) = zeta^(-e), sum zero.
    assert exact_profile == EXPECTED
    multiplicity_one_total = sum(exact_profile.values())
    even_total = sum(
        value for degree, value in exact_profile.items() if degree % 2 == 0
    )
    odd_total = sum(
        value for degree, value in exact_profile.items() if degree % 2 == 1
    )
    doubled_total = 2 * multiplicity_one_total
    assert (
        multiplicity_one_total,
        even_total,
        odd_total,
        doubled_total,
    ) == (11, 6, 5, 22)
    assert multiplicity_one_total - exact_profile[10] == 10

    print("exact hook-nullity profile:", exact_profile)
    print("multiplicity-one total = 11 = 6 even + 5 odd")
    print("full C_wedge H_1 total = 22")
    print("removing the unique sign-hook class leaves 10 = p-1")
    print("P11_CWEDGE_CYCLOTOMIC_LIFT_VERIFY: PASS")


if __name__ == "__main__":
    main()
