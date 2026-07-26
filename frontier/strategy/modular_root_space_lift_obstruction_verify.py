#!/usr/bin/env python3
"""Exact p=11/p=13 certificate for the modular root-space lifting obstruction.

For W = ker(sum:F_p^p->F_p)/<1,...,1>, the p-cycle acts as one Jordan
block J_{p-2}.  At p=11 and p=13, hook-length enumeration shows that every
nonlinear ordinary irreducible S_p-representation has dimension at least p-1.
Hence an ordinary representation of dimension p-2 is a sum of trivial/sign
lines, on which an odd p-cycle acts trivially.  It cannot reduce to W.

The script also checks the integral obstruction to the naive three-term lift:
(sum) o (diagonal) = p, not zero.
"""
from __future__ import annotations

from math import factorial
from typing import Iterable, Tuple

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


def specht_dimension(shape: Tuple[int, ...]) -> int:
    hook_product = 1
    for row, width in enumerate(shape):
        for column in range(width):
            below = sum(1 for lower in range(row + 1, len(shape)) if shape[lower] > column)
            hook_product *= width - column + below
    return factorial(sum(shape)) // hook_product


def matmul(left, right, prime):
    rows, middle, columns = len(left), len(right), len(right[0])
    assert len(left[0]) == middle
    return [
        [sum(left[i][k] * right[k][j] for k in range(middle)) % prime for j in range(columns)]
        for i in range(rows)
    ]


def matrix_rank(matrix, prime):
    work = [row[:] for row in matrix]
    rows, columns = len(work), len(work[0]) if work else 0
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if work[row][column] % prime), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [(value * inverse) % prime for value in work[rank]]
        for row in range(rows):
            if row != rank and work[row][column] % prime:
                factor = work[row][column]
                work[row] = [
                    (work[row][j] - factor * work[rank][j]) % prime
                    for j in range(columns)
                ]
        rank += 1
    return rank


def quotient_cycle_matrix(prime: int):
    """Matrix of (0 1 ... p-1) on W in a concrete quotient basis."""
    # H basis v_i=e_i-e_{p-1}, i=0,...,p-2.  The diagonal is sum_i v_i.
    hdim = prime - 1
    action_h = [[0] * hdim for _ in range(hdim)]
    # Convert a vector in F_p^p of coordinate sum zero to H coordinates:
    # its first p-1 coordinates are the coefficients of v_i.
    for source in range(hdim):
        vector = [0] * prime
        vector[source] = 1
        vector[prime - 1] = -1
        shifted = [0] * prime
        for index, value in enumerate(vector):
            shifted[(index + 1) % prime] = value
        for target in range(hdim):
            action_h[target][source] = shifted[target] % prime

    # Quotient by d=sum v_i.  Use q_i=[v_i], i=0,...,p-3 and replace
    # [v_{p-2}]=-[v_0]-...-[v_{p-3}].
    qdim = prime - 2
    action_w = [[0] * qdim for _ in range(qdim)]
    for source in range(qdim):
        hcoords = [action_h[row][source] for row in range(hdim)]
        last = hcoords[-1]
        for target in range(qdim):
            action_w[target][source] = (hcoords[target] - last) % prime
    return action_w


def identity(size: int):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def subtract(left, right, prime):
    return [[(x - y) % prime for x, y in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def verify_prime(prime: int) -> None:
    action = quotient_cycle_matrix(prime)
    dimension = prime - 2
    nilpotent = subtract(action, identity(dimension), prime)
    power = identity(dimension)
    ranks = []
    for exponent in range(dimension + 1):
        ranks.append(matrix_rank(power, prime))
        power = matmul(power, nilpotent, prime)
    assert ranks == list(range(dimension, -1, -1)), (prime, ranks)

    nonlinear = [
        (shape, specht_dimension(shape))
        for shape in partitions(prime)
        if specht_dimension(shape) > 1
    ]
    minimum = min(dimension for _, dimension in nonlinear)
    assert minimum == prime - 1
    assert all(
        shape in ((prime,), (1,) * prime)
        for shape in partitions(prime)
        if specht_dimension(shape) < prime - 1
    )

    # Over Z, diagonal(1) followed by coordinate sum is multiplication by p.
    diagonal = [1] * prime
    assert sum(diagonal) == prime and sum(diagonal) != 0
    assert sum(value % prime for value in diagonal) % prime == 0

    print(
        f"p={prime}: W has Jordan ranks {ranks}; minimum nonlinear ordinary "
        f"degree {minimum}; sum o diagonal = {prime}: PASS"
    )


def main() -> None:
    for prime in PRIMES:
        verify_prime(prime)
    print("MODULAR_ROOT_SPACE_LIFT_OBSTRUCTION_VERIFY: PASS")


if __name__ == "__main__":
    main()
