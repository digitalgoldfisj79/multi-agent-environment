#!/usr/bin/env python3
"""Exact checks for LOCAL_AIRY_ADAMS_CYCLOTOMIC_INITIAL_TERM_20260725.md.

The script represents elements of Z[zeta_p] by coefficient vectors modulo
1+zeta+...+zeta^(p-1)=0.  Expansion at pi=zeta-1 is exact modulo p.

It checks, for each requested prime p=5 mod 6 and every u in F_p^*:

    t_u = (u/h!) pi^e + O(pi^(e+1)),
    f_p(u)/p^e = (u/h!) pi^e + O(pi^(e+1)),

where e=(p+1)/3 and f_p=D_p(t_u,p).  It also checks pairwise
separation of all local values by this initial coefficient.
"""

from __future__ import annotations

import argparse
from math import comb, factorial
from typing import Tuple

Vector = Tuple[int, ...]


def canonical(vector: Vector) -> Vector:
    final = vector[-1]
    return tuple(value - final for value in vector[:-1]) + (0,)


def add(left: Vector, right: Vector) -> Vector:
    return tuple(x + y for x, y in zip(left, right))


def negate(vector: Vector) -> Vector:
    return tuple(-value for value in vector)


def scale(vector: Vector, scalar: int) -> Vector:
    return tuple(scalar * value for value in vector)


def multiply(left: Vector, right: Vector, p: int) -> Vector:
    output = [0] * p
    for i, left_value in enumerate(left):
        if left_value:
            for j, right_value in enumerate(right):
                if right_value:
                    output[(i + j) % p] += left_value * right_value
    return canonical(tuple(output))


def integer(value: int, p: int) -> Vector:
    return (value,) + (0,) * (p - 1)


def airy_trace(p: int, parameter: int) -> Vector:
    output = [0] * p
    for x in range(p):
        output[(x**3 + parameter * x) % p] -= 1
    return canonical(tuple(output))


def dickson_value(p: int, trace: Vector) -> Vector:
    previous = integer(2, p)
    current = trace
    for _ in range(2, p + 1):
        previous, current = current, add(
            multiply(trace, current, p),
            negate(scale(previous, p)),
        )
    return canonical(current)


def pi_coefficients_mod_p(vector: Vector, p: int) -> list[int]:
    # zeta^a=(1+pi)^a.  Only coefficients below p are needed.
    return [
        sum(vector[exponent] * comb(exponent, degree)
            for exponent in range(degree, p)) % p
        for degree in range(p)
    ]


def verify_prime(p: int) -> None:
    if p % 6 != 5:
        raise ValueError("p must be 5 modulo 6")

    h = (p - 2) // 3
    e = h + 1
    expected_scalar = pow(factorial(h), -1, p)
    p_power = p**e

    initial_coefficients = []
    values = []

    for u in range(1, p):
        trace = airy_trace(p, u)
        trace_coefficients = pi_coefficients_mod_p(trace, p)
        assert all(value == 0 for value in trace_coefficients[:e])
        assert trace_coefficients[e] == expected_scalar * u % p

        adams = dickson_value(p, trace)
        assert all(coordinate % p_power == 0 for coordinate in adams)
        normalized = tuple(coordinate // p_power for coordinate in adams)
        normalized_coefficients = pi_coefficients_mod_p(normalized, p)
        assert all(value == 0 for value in normalized_coefficients[:e])
        assert normalized_coefficients[e] == expected_scalar * u % p

        initial_coefficients.append(normalized_coefficients[e])
        values.append(adams)

    assert len(set(initial_coefficients)) == p - 1
    assert len(set(values)) == p - 1

    print(
        f"p={p}: h={h}, e={e}, initial scalar={expected_scalar}, "
        "all local values separated: PASS"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--primes",
        nargs="*",
        type=int,
        default=[5, 11, 17, 23, 29, 41, 47, 53],
    )
    arguments = parser.parse_args()
    for prime in arguments.primes:
        verify_prime(prime)
    print("LOCAL_AIRY_ADAMS_INITIAL_VERIFY: PASS")


if __name__ == "__main__":
    main()
