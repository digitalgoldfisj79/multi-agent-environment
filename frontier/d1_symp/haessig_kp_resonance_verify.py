#!/usr/bin/env python3
"""
Verify the critical k=p resonance pattern in Haessig's cubic-Airy
effective-decomposition matrix.

This is a structural identity check, not a prime sweep for evidence.

For odd prime p, remove the common pi/a growth factors from Haessig's
connection matrix G_p and retain the integer coefficient matrix H_p:
    H_p q_i = (p-i) q_{i+1} + i q_{i-1}.

The script verifies:
  1. rank(H_p mod p) = p-1;
  2. v_p(det H_p) = 2;
  3. hence the p-local Smith form has exactly two elementary p-divisors;
  4. the only non-unit coefficients in the terminal Lemma 6.4 reductions
     occur at the final elimination step, once in each parity chain.

No third-party packages are required.
"""

from __future__ import annotations

from math import prod
from typing import Iterable


def odd_primes(limit: int) -> Iterable[int]:
    for n in range(3, limit + 1, 2):
        if all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            yield n


def coefficient_matrix(p: int) -> list[list[int]]:
    """Columns encode H_p(q_i) in the ordered basis q_0,...,q_p."""
    n = p + 1
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        if i < p:
            matrix[i + 1][i] = p - i
        if i > 0:
            matrix[i - 1][i] = i
    return matrix


def rank_mod_p(matrix: list[list[int]], p: int) -> int:
    a = [[entry % p for entry in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0

    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]

        inverse = pow(a[rank][col], -1, p)
        a[rank] = [(value * inverse) % p for value in a[rank]]

        for row in range(rows):
            if row == rank or not a[row][col]:
                continue
            factor = a[row][col]
            a[row] = [
                (a[row][j] - factor * a[rank][j]) % p
                for j in range(cols)
            ]

        rank += 1
        if rank == rows:
            break

    return rank


def determinant_mod_p(matrix: list[list[int]], p: int) -> int:
    """Exact determinant modulo p by fraction-free Gaussian elimination."""
    a = [[entry % p for entry in row] for row in matrix]
    n = len(a)
    determinant = 1

    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            determinant = -determinant

        pivot_value = a[col][col]
        determinant = (determinant * pivot_value) % p
        inverse = pow(pivot_value, -1, p)

        for row in range(col + 1, n):
            if not a[row][col]:
                continue
            factor = a[row][col] * inverse % p
            for j in range(col, n):
                a[row][j] = (a[row][j] - factor * a[col][j]) % p

    return determinant % p


def p_valuation(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("p-adic valuation of zero is not used here")
    n = abs(n)
    valuation = 0
    while n % p == 0:
        n //= p
        valuation += 1
    return valuation


def determinant_abs_formula(p: int) -> int:
    """
    Absolute determinant of H_p.

    The zero-diagonal tridiagonal matrix has a unique perfect matching:
    (q_0,q_1), (q_2,q_3), ..., (q_{p-1},q_p).
    """
    return prod(
        (p - 2 * j) * (2 * j + 1)
        for j in range((p + 1) // 2)
    )


def terminal_odd_denominator(p: int, j: int, m: int) -> int:
    """
    Integer part of 2^m (j+1/2)_m in Haessig Lemma 6.4:
        product_{t=0}^{m-1} (2j+1+2t).
    """
    return prod(2 * j + 1 + 2 * t for t in range(m))


def terminal_even_denominator(p: int, j: int, m: int) -> int:
    """
    Integer part of 2^(m+1) (p/2-j+1)_(m+1):
        product_{t=0}^{m} (p-2j+2+2t).
    """
    return prod(p - 2 * j + 2 + 2 * t for t in range(m + 1))


def verify_prime(p: int) -> None:
    if p < 3 or p % 2 == 0:
        raise ValueError(f"expected an odd prime, got {p}")

    matrix = coefficient_matrix(p)
    rank = rank_mod_p(matrix, p)
    assert rank == p - 1, (p, rank)

    internal_minor = [row[1:p] for row in matrix[1:p]]
    assert determinant_mod_p(internal_minor, p) == p - 1, p

    determinant = determinant_abs_formula(p)
    assert p_valuation(determinant, p) == 2, p

    # Odd-column high-degree branch: only the final m reaches the factor p.
    for j in range((p - 1) // 2 + 1):
        terminal_m = (p + 1) // 2 - j
        for m in range(1, terminal_m + 1):
            valuation = p_valuation(terminal_odd_denominator(p, j, m), p)
            assert valuation == (1 if m == terminal_m else 0), (
                "odd",
                p,
                j,
                m,
                valuation,
            )

    # Even-column branch: only the deepest backward reduction reaches p.
    for j in range(1, (p + 1) // 2 + 1):
        terminal_m = j - 1
        for m in range(0, terminal_m + 1):
            valuation = p_valuation(terminal_even_denominator(p, j, m), p)
            assert valuation == (1 if m == terminal_m else 0), (
                "even",
                p,
                j,
                m,
                valuation,
            )


def main() -> None:
    checked = list(odd_primes(199))
    for p in checked:
        verify_prime(p)

    print(
        "PASS: critical k=p resonance identities verified for "
        f"{len(checked)} odd primes through {checked[-1]}."
    )
    print(
        "Structural conclusion: rank mod p = p-1 and v_p(det)=2, "
        "so the p-local Smith form has p-1 unit factors and two "
        "elementary factors of valuation one."
    )


if __name__ == "__main__":
    main()
