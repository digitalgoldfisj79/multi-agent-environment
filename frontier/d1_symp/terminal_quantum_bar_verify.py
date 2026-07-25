#!/usr/bin/env python3
"""Exact finite-field checks for the terminal order-p quantum bar theorem.

For p=3,5,7,11, choose an auxiliary prime ell congruent to 1 mod p and a
primitive p-th root zeta in F_ell. Build the weight-p quantum-shuffle bar
complex on compositions of p and compute every differential rank exactly.
The only homology must occur at composition lengths 1 and 2, with dimension 1.
"""

from __future__ import annotations

from itertools import combinations


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, int(n**0.5) + 1, 2))


def auxiliary_prime(p: int) -> int:
    k = 1
    while True:
        ell = k * p + 1
        if is_prime(ell):
            return ell
        k += 1


def primitive_root_of_order_p(p: int, ell: int) -> int:
    for zeta in range(2, ell):
        if pow(zeta, p, ell) == 1 and all(
            pow(zeta, d, ell) != 1 for d in range(1, p)
        ):
            return zeta
    raise AssertionError("no primitive p-th root found")


def q_integer(n: int, zeta: int, ell: int) -> int:
    return sum(pow(zeta, j, ell) for j in range(n)) % ell


def q_factorial(n: int, zeta: int, ell: int) -> int:
    value = 1
    for j in range(1, n + 1):
        value = value * q_integer(j, zeta, ell) % ell
    return value


def q_binomial(n: int, k: int, zeta: int, ell: int) -> int:
    numerator = q_factorial(n, zeta, ell)
    denominator = q_factorial(k, zeta, ell) * q_factorial(n - k, zeta, ell) % ell
    if denominator == 0:
        raise AssertionError("denominator vanished below the first resonance")
    return numerator * pow(denominator, -1, ell) % ell


def compositions(n: int, length: int):
    for cuts in combinations(range(1, n), length - 1):
        previous = 0
        parts = []
        for cut in cuts + (n,):
            parts.append(cut - previous)
            previous = cut
        yield tuple(parts)


def rank_mod(matrix: list[list[int]], ell: int) -> int:
    if not matrix:
        return 0
    a = [[entry % ell for entry in row] for row in matrix]
    rows = len(a)
    columns = len(a[0])
    rank = 0
    for column in range(columns):
        pivot = next((r for r in range(rank, rows) if a[r][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = pow(a[rank][column], -1, ell)
        a[rank] = [(scale * x) % ell for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][column]:
                factor = a[r][column]
                a[r] = [
                    (x - factor * y) % ell
                    for x, y in zip(a[r], a[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def homology_dimensions(p: int):
    ell = auxiliary_prime(p)
    zeta = primitive_root_of_order_p(p, ell)
    basis = {length: list(compositions(p, length)) for length in range(1, p + 1)}
    differential_rank = {1: 0}

    for length in range(2, p + 1):
        target_index = {
            composition: index
            for index, composition in enumerate(basis[length - 1])
        }
        matrix = [
            [0] * len(basis[length])
            for _ in range(len(basis[length - 1]))
        ]
        for column, composition in enumerate(basis[length]):
            for position in range(length - 1):
                left = composition[position]
                right = composition[position + 1]
                merged = (
                    composition[:position]
                    + (left + right,)
                    + composition[position + 2 :]
                )
                coefficient = q_binomial(left + right, left, zeta, ell)
                sign = 1 if position % 2 == 0 else -1
                row = target_index[merged]
                matrix[row][column] = (
                    matrix[row][column] + sign * coefficient
                ) % ell
        differential_rank[length] = rank_mod(matrix, ell)

    homology = {}
    for length in range(1, p + 1):
        homology[length] = (
            len(basis[length])
            - differential_rank.get(length, 0)
            - differential_rank.get(length + 1, 0)
        )
    return ell, zeta, homology


def verify() -> None:
    for p in (3, 5, 7, 11):
        ell, zeta, homology = homology_dimensions(p)
        nonzero = {length: dim for length, dim in homology.items() if dim}
        assert nonzero == {1: 1, 2: 1}, (p, nonzero)
        print(
            f"PASS: p={p}, auxiliary ell={ell}, zeta={zeta}, "
            "terminal homology={1:1, 2:1}."
        )
    print("TERMINAL_QUANTUM_BAR_VERIFY: PASS")


if __name__ == "__main__":
    verify()
