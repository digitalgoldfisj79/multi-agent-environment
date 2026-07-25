#!/usr/bin/env python3
"""Checks for PASCAL_SPARSE_BLOCK_ANTI_SYMPLECTIC_THEOREM_20260725.md."""

from __future__ import annotations

from math import comb, isqrt


def primes_below(limit: int):
    for value in range(11, limit, 2):
        if all(value % divisor for divisor in range(3, isqrt(value) + 1, 2)):
            yield value


def matmul(left, right, p):
    rows = len(left)
    middle = len(right)
    cols = len(right[0])
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(middle)) % p
            for j in range(cols)
        ]
        for i in range(rows)
    ]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def verify_prime(p: int) -> None:
    indices = list(range(4, p - 3))
    dimension = p - 7
    assert len(indices) == dimension

    pascal = [
        [((-1) ** j * comb(m + j - 1, j)) % p for m in indices]
        for j in indices
    ]
    symplectic = [
        [((a - b) if a + b == p else 0) % p for b in indices]
        for a in indices
    ]

    # Lucas support and unit antidiagonal.
    for row, j in enumerate(indices):
        for column, m in enumerate(indices):
            assert (pascal[row][column] == 0) == (j + m > p)
            if j + m == p:
                assert pascal[row][column] == 1

    transformed = matmul(
        matmul(transpose(pascal), symplectic, p), pascal, p
    )
    expected = [[(-value) % p for value in row] for row in symplectic]
    assert transformed == expected

    # The graph is isotropic in W direct-sum W.
    for i in range(dimension):
        for j in range(dimension):
            assert (symplectic[i][j] + transformed[i][j]) % p == 0

    print(f"p={p}: dimension={dimension}, D^t W D=-W: PASS")


def main() -> None:
    checked = []
    for p in primes_below(200):
        verify_prime(p)
        checked.append(p)
    print(
        f"PASCAL_SPARSE_ANTISYMPLECTIC_VERIFY: PASS ({len(checked)} primes)"
    )


if __name__ == "__main__":
    main()
