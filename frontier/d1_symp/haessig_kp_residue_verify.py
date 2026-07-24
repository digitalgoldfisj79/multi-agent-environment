#!/usr/bin/env python3
"""Exact regression checks for the critical k=p inverse-residue formula.

For unit specializations A,B modulo an odd prime p, form

    G_p q_i = A(p-i)q_(i+1) + B i q_(i-1).

The proved formula predicts that p*G_p^(-1) modulo p has only two
nonzero rows:

    row q_0, column q_(2j+1): B^j/A^(j+1),
    row q_p, column q_(2j):   A^(n-1-j)/B^(n-j),

where n=(p+1)/2.

The script uses only Python's exact Fraction arithmetic. Numerical
specializations are regression checks of the symbolic proof, not a
replacement for it.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable


def odd_primes(limit: int) -> Iterable[int]:
    for n in range(5, limit + 1, 2):
        if all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            yield n


def connection_matrix(p: int, a_value: int, b_value: int) -> list[list[int]]:
    size = p + 1
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        if i < p:
            matrix[i + 1][i] = a_value * (p - i)
        if i > 0:
            matrix[i - 1][i] = b_value * i
    return matrix


def inverse_fraction(matrix: list[list[int]]) -> list[list[Fraction]]:
    size = len(matrix)
    augmented = [
        [Fraction(matrix[i][j]) for j in range(size)]
        + [Fraction(int(i == j)) for j in range(size)]
        for i in range(size)
    ]

    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]),
            None,
        )
        if pivot is None:
            raise ValueError("matrix is singular over the rationals")

        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        pivot_value = augmented[column][column]
        augmented[column] = [entry / pivot_value for entry in augmented[column]]

        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if not factor:
                continue
            augmented[row] = [
                augmented[row][j] - factor * augmented[column][j]
                for j in range(2 * size)
            ]

    return [row[size:] for row in augmented]


def fraction_mod_p(value: Fraction, p: int) -> int:
    denominator = value.denominator % p
    if denominator == 0:
        raise ValueError(
            f"expected p-integrality after multiplying by p; got {value} at p={p}"
        )
    return value.numerator % p * pow(denominator, -1, p) % p


def predicted_entry(
    p: int,
    a_value: int,
    b_value: int,
    row: int,
    column: int,
) -> int:
    n = (p + 1) // 2
    a_value %= p
    b_value %= p

    if row == 0 and column % 2 == 1:
        j = (column - 1) // 2
        return (
            pow(b_value, j, p)
            * pow(pow(a_value, j + 1, p), -1, p)
            % p
        )

    if row == p and column % 2 == 0:
        j = column // 2
        return (
            pow(a_value, n - 1 - j, p)
            * pow(pow(b_value, n - j, p), -1, p)
            % p
        )

    return 0


def invariant_support_count(p: int) -> int:
    n = (p + 1) // 2
    odd_chain = sum(1 for j in range(n) if j % 3 == 0)
    even_chain = sum(1 for j in range(n) if j % 3 == 2)
    return odd_chain + even_chain


def verify_specialization(p: int, a_value: int, b_value: int) -> None:
    if a_value % p == 0 or b_value % p == 0:
        raise ValueError("A and B must be units modulo p")

    matrix = connection_matrix(p, a_value, b_value)
    inverse = inverse_fraction(matrix)

    for row in range(p + 1):
        for column in range(p + 1):
            actual = fraction_mod_p(Fraction(p) * inverse[row][column], p)
            expected = predicted_entry(
                p,
                a_value,
                b_value,
                row,
                column,
            )
            assert actual == expected, (
                p,
                a_value,
                b_value,
                row,
                column,
                actual,
                expected,
            )

    if p % 3 == 2:
        assert invariant_support_count(p) == (p + 1) // 3, p


def main() -> None:
    specializations = ((1, 1), (2, 3), (3, 5))
    checked = []

    for p in odd_primes(43):
        for a_value, b_value in specializations:
            if a_value % p and b_value % p:
                verify_specialization(p, a_value, b_value)
                checked.append((p, a_value, b_value))

    print(
        "PASS: inverse-residue factorization verified by exact rational "
        f"inversion in {len(checked)} prime/specialization cases."
    )
    print(
        "PASS: for every checked p == 2 mod 3, invariant Laurent support "
        "equals (p+1)/3."
    )


if __name__ == "__main__":
    main()
