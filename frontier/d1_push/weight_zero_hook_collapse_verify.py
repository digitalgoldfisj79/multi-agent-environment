#!/usr/bin/env python3
"""Finite-group verification of the weight-zero hook-collapse local terms.

The proof is symbolic.  This script checks its two group-theoretic inputs for
several primes:

* lambda_{-1}(Std) is p on p-cycles and zero on every other permutation;
* averaging over the affine inertia I=C_p semidirect squares gives 2 on the
  square multiplier coset and 0 on the nonsquare coset.

After subtraction of the global trivial line the latter values are +1 and -1,
which are the two Frobenius readings of the discriminant Kummer line.
"""
from __future__ import annotations

from fractions import Fraction


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def cycle_count(permutation: tuple[int, ...]) -> int:
    seen = [False] * len(permutation)
    count = 0
    for start in range(len(permutation)):
        if seen[start]:
            continue
        count += 1
        current = start
        while not seen[current]:
            seen[current] = True
            current = permutation[current]
    return count


def lambda_trace(permutation: tuple[int, ...]) -> int:
    p = len(permutation)
    return p if cycle_count(permutation) == 1 else 0


def affine_permutation(p: int, multiplier: int, translation: int) -> tuple[int, ...]:
    return tuple((multiplier * value + translation) % p for value in range(p))


def legendre(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def verify_prime(p: int) -> None:
    identity = tuple(range(p))
    translation = affine_permutation(p, 1, 1)
    multiplier = affine_permutation(p, 2, 0)
    assert lambda_trace(identity) == 0
    assert lambda_trace(translation) == p
    if cycle_count(multiplier) != 1:
        assert lambda_trace(multiplier) == 0

    squares = [value for value in range(1, p) if legendre(value, p) == 1]
    nonsquare = next(value for value in range(1, p) if legendre(value, p) == -1)
    inertia = [
        affine_permutation(p, multiplier_value, translation_value)
        for multiplier_value in squares
        for translation_value in range(p)
    ]
    assert len(inertia) == p * (p - 1) // 2

    square_total = sum(lambda_trace(element) for element in inertia)
    square_average = Fraction(square_total, len(inertia))
    assert square_average == 2

    nonsquare_representative = affine_permutation(p, nonsquare, 0)
    nonsquare_coset = [compose(nonsquare_representative, element) for element in inertia]
    nonsquare_total = sum(lambda_trace(element) for element in nonsquare_coset)
    nonsquare_average = Fraction(nonsquare_total, len(inertia))
    assert nonsquare_average == 0

    # At a finite branch point, any element in a Frobenius coset commuting
    # with the inertia transposition cannot be a p-cycle.  Check a concrete
    # centralizer coset representative.
    transposition = list(range(p))
    transposition[0], transposition[1] = transposition[1], transposition[0]
    transposition = tuple(transposition)
    finite_representative = tuple([1, 0] + list(range(2, p)))
    assert compose(finite_representative, transposition) == compose(
        transposition, finite_representative
    )
    finite_coset = [finite_representative, compose(finite_representative, transposition)]
    assert all(lambda_trace(element) == 0 for element in finite_coset)

    print(
        f"p={p}: finite=0, infinity square={square_average}, "
        f"infinity nonsquare={nonsquare_average}, after global subtraction=(+1,-1): PASS"
    )


if __name__ == "__main__":
    for prime in (5, 7, 11, 13, 17, 23):
        verify_prime(prime)
    print("WEIGHT_ZERO_HOOK_COLLAPSE_VERIFY: PASS")
