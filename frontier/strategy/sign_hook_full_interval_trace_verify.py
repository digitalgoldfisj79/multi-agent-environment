#!/usr/bin/env python3
"""Verify the exact sign/discriminant trace in the d=1 four-parameter interval.

For odd primes p>3, put

    f = X^p + a X^3 + b X^2 + u X + d,

where (a,b,u,d) ranges over F_p^4, and extend the quadratic character by
chi(0)=0. The sign factorization-function sum is

    S_sgn(p) = sum chi(Disc(f)).

The proved formula is

    S_sgn(p) = ((1-chi(-1))/2) * chi(-6) * p^2 * (p-1).
"""
from __future__ import annotations

from math import isqrt
from typing import Iterable, List

import numpy as np

try:
    from numba import njit
except ImportError:  # pragma: no cover
    njit = None


def quadratic_character(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    return 1 if pow(value, (prime - 1) // 2, prime) == 1 else -1


def predicted_trace(prime: int) -> int:
    return (
        (1 - quadratic_character(-1, prime))
        // 2
        * quadratic_character(-6, prime)
        * prime
        * prime
        * (prime - 1)
    )


def collision_count_for_a(prime: int, a: int) -> int:
    assert a % prime
    count = 0
    delta_plus = (9 * a * pow(2, -1, prime)) % prime
    if quadratic_character(delta_plus, prime) == 1:
        count += 1
    delta_minus = (-delta_plus) % prime
    if quadratic_character(delta_minus, prime) == -1:
        count += 1
    return count


def trace_from_collision_formula(prime: int) -> int:
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    total = 0
    for a in range(1, prime):
        total += (
            prime
            * prime
            * quadratic_character(epsilon * 3 * a, prime)
            * collision_count_for_a(prime, a)
        )
    return total


if njit is not None:

    @njit(cache=True)
    def _pow_mod(base: int, exponent: int, modulus: int) -> int:
        result = 1
        base %= modulus
        while exponent:
            if exponent & 1:
                result = result * base % modulus
            base = base * base % modulus
            exponent //= 2
        return result

    @njit(cache=True)
    def _determinant_mod(matrix: np.ndarray, modulus: int) -> int:
        working = matrix.copy() % modulus
        size = working.shape[0]
        determinant = 1
        for column in range(size):
            pivot = -1
            for row in range(column, size):
                if working[row, column] % modulus:
                    pivot = row
                    break
            if pivot < 0:
                return 0
            if pivot != column:
                temporary = working[column].copy()
                working[column] = working[pivot]
                working[pivot] = temporary
                determinant = (-determinant) % modulus
            pivot_value = working[column, column] % modulus
            determinant = determinant * pivot_value % modulus
            inverse = _pow_mod(pivot_value, modulus - 2, modulus)
            for j in range(column, size):
                working[column, j] = working[column, j] * inverse % modulus
            for row in range(column + 1, size):
                factor = working[row, column] % modulus
                if factor:
                    for j in range(column, size):
                        working[row, j] = (
                            working[row, j]
                            - factor * working[column, j]
                        ) % modulus
        return determinant

else:  # pragma: no cover

    def _determinant_mod(matrix: np.ndarray, modulus: int) -> int:
        working = matrix.copy() % modulus
        size = working.shape[0]
        determinant = 1
        for column in range(size):
            pivot = next(
                (
                    row
                    for row in range(column, size)
                    if working[row, column] % modulus
                ),
                None,
            )
            if pivot is None:
                return 0
            if pivot != column:
                working[[column, pivot]] = working[[pivot, column]]
                determinant = -determinant
            pivot_value = int(working[column, column]) % modulus
            determinant = determinant * pivot_value % modulus
            inverse = pow(pivot_value, -1, modulus)
            working[column] = working[column] * inverse % modulus
            for row in range(column + 1, size):
                factor = int(working[row, column]) % modulus
                if factor:
                    working[row] = (
                        working[row] - factor * working[column]
                    ) % modulus
        return determinant % modulus


def resultant_mod(first: List[int], second: List[int], prime: int) -> int:
    while len(first) > 1 and first[0] % prime == 0:
        first = first[1:]
    while len(second) > 1 and second[0] % prime == 0:
        second = second[1:]
    first_degree = len(first) - 1
    second_degree = len(second) - 1
    if second_degree == 0:
        return pow(second[0] % prime, first_degree, prime)
    if first_degree == 0:
        return pow(first[0] % prime, second_degree, prime)
    sylvester = np.zeros(
        (first_degree + second_degree, first_degree + second_degree),
        dtype=np.int64,
    )
    for row in range(second_degree):
        sylvester[row, row : row + first_degree + 1] = (
            np.array(first, dtype=np.int64) % prime
        )
    for row in range(first_degree):
        sylvester[
            second_degree + row, row : row + second_degree + 1
        ] = np.array(second, dtype=np.int64) % prime
    return int(_determinant_mod(sylvester, prime))


def brute_trace(prime: int) -> int:
    epsilon = -1 if ((prime - 1) // 2) % 2 else 1
    total = 0
    for a in range(prime):
        for b in range(prime):
            for u in range(prime):
                derivative = [3 * a % prime, 2 * b % prime, u]
                for d in range(prime):
                    polynomial = [1] + [0] * prime
                    polynomial[prime - 3] = a
                    polynomial[prime - 2] = b
                    polynomial[prime - 1] = u
                    polynomial[prime] = d
                    resultant = resultant_mod(polynomial, derivative, prime)
                    total += quadratic_character(epsilon * resultant, prime)
    return total


def primes_up_to(limit: int) -> Iterable[int]:
    for candidate in range(5, limit + 1, 2):
        if all(
            candidate % divisor
            for divisor in range(3, isqrt(candidate) + 1, 2)
        ):
            yield candidate


def main() -> None:
    for prime in primes_up_to(499):
        collision = trace_from_collision_formula(prime)
        predicted = predicted_trace(prime)
        assert collision == predicted, (prime, collision, predicted)
    print("collision derivation through p=499: PASS")

    for prime in (5, 7, 11, 13, 17, 19, 23):
        brute = brute_trace(prime)
        predicted = predicted_trace(prime)
        assert brute == predicted, (prime, brute, predicted)
        print(f"p={prime}: brute sign trace {brute}: PASS")

    admitted = {
        5: 0,
        11: 11 * 11 * 10,
        17: 0,
        23: -(23 * 23 * 22),
    }
    for prime, expected in admitted.items():
        assert predicted_trace(prime) == expected
    print("admitted residue-class calibration modulo 24: PASS")
    print("SIGN_HOOK_FULL_INTERVAL_TRACE_VERIFY: PASS")


if __name__ == "__main__":
    main()
