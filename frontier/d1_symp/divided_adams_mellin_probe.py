#!/usr/bin/env python3
"""Exact multiplicative Mellin-support probe for the local Airy Adams trace.

For p=2 mod 3, put

    t_u = -sum_x zeta_p^(x^3+u*x),
    f_p(u) = D_p(t_u,p).

The script represents f_p(u) exactly in Z[zeta_p].  If g generates F_p^*
and chi_k(g)=xi_(p-1)^k, then M_p(k)=sum_j chi_k(g^j)f_p(g^j).
Writing d=(p-1)/gcd(k,p-1), M_p(k)=0 exactly when every cyclotomic
coordinate polynomial sum_j f_p(g^j)_r X^j is divisible by Phi_d(X).
No floating-point Fourier transform is used.
"""
from __future__ import annotations

import argparse
from math import gcd

import sympy as sp

Vector = tuple[int, ...]


def canonical(vector: Vector) -> Vector:
    """Use 1+zeta+...+zeta^(p-1)=0 and set the final coordinate to zero."""
    final = vector[-1]
    return tuple(value - final for value in vector[:-1]) + (0,)


def add(left: Vector, right: Vector) -> Vector:
    return tuple(x + y for x, y in zip(left, right))


def negate(vector: Vector) -> Vector:
    return tuple(-value for value in vector)


def scale(vector: Vector, scalar: int) -> Vector:
    return tuple(scalar * value for value in vector)


def multiply(left: Vector, right: Vector, p: int) -> Vector:
    out = [0] * p
    for i, left_value in enumerate(left):
        if left_value:
            for j, right_value in enumerate(right):
                if right_value:
                    out[(i + j) % p] += left_value * right_value
    return canonical(tuple(out))


def integer(value: int, p: int) -> Vector:
    return (value,) + (0,) * (p - 1)


def airy_trace(p: int, parameter: int) -> Vector:
    out = [0] * p
    for x in range(p):
        out[(x**3 + parameter * x) % p] -= 1
    return canonical(tuple(out))


def dickson_value(p: int, trace: Vector) -> Vector:
    previous = integer(2, p)
    current = trace
    for _ in range(2, p + 1):
        previous, current = current, add(
            multiply(trace, current, p),
            negate(scale(previous, p)),
        )
    return canonical(current)


def mellin_is_zero(values: list[Vector], p: int, exponent: int) -> bool:
    order = 1 if exponent == 0 else (p - 1) // gcd(exponent, p - 1)
    variable = sp.Symbol("X")
    cyclotomic = sp.Poly(sp.cyclotomic_poly(order, variable), variable, domain=sp.ZZ)
    for coordinate in range(p - 1):
        polynomial = sp.Poly(
            sum(values[index][coordinate] * variable**index for index in range(p - 1)),
            variable,
            domain=sp.ZZ,
        )
        if polynomial.rem(cyclotomic).as_expr() != 0:
            return False
    return True


def analyse(p: int) -> None:
    if not sp.isprime(p) or p % 3 != 2:
        raise ValueError("p must be prime and 2 modulo 3")
    generator = int(sp.primitive_root(p))
    parameters = [pow(generator, exponent, p) for exponent in range(p - 1)]
    values = [dickson_value(p, airy_trace(p, parameter)) for parameter in parameters]

    zero_exponents = [
        exponent
        for exponent in range(p - 1)
        if mellin_is_zero(values, p, exponent)
    ]
    support = [exponent for exponent in range(p - 1) if exponent not in zero_exponents]

    order_histogram: dict[int, int] = {}
    for exponent in support:
        order = 1 if exponent == 0 else (p - 1) // gcd(exponent, p - 1)
        order_histogram[order] = order_histogram.get(order, 0) + 1

    periods: list[int] = []
    antiperiods: list[int] = []
    for shift in range(1, p - 1):
        if all(values[(index + shift) % (p - 1)] == values[index] for index in range(p - 1)):
            periods.append(shift)
        if all(values[(index + shift) % (p - 1)] == negate(values[index]) for index in range(p - 1)):
            antiperiods.append(shift)

    matrix = sp.Matrix(
        [[values[column][row] for column in range(p - 1)] for row in range(p - 1)]
    )
    print(
        f"p={p} generator={generator} support={len(support)}/{p-1} "
        f"zeros={zero_exponents} order_histogram={order_histogram}"
    )
    print(f"periods={periods} antiperiods={antiperiods}")
    print(f"value_matrix_rank={matrix.rank()} expected_real_degree={(p-1)//2}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", nargs="*", type=int, default=[11, 17, 23, 29])
    arguments = parser.parse_args()
    for prime in arguments.primes:
        analyse(prime)
