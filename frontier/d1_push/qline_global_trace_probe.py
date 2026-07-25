#!/usr/bin/env python3
"""Exact generic q-line trace census for the normal-form family.

For Q=p^r and q in F_Q\{0,2}, let I_r(q) be the number of t in F_Q for
which

    q z^p + z^3 - 3 z - (q-2)t

is irreducible of degree p over F_Q.  The hook p-cycle detector gives

    E_r(q)=Q-p I_r(q),

so the complete split generic q-line trace is

    S_r=(Q-2)Q-p sum_q I_r(q).

The script performs exact finite-field factorisation.  It is intended for
focused low-power structural tests, not large blind prime sweeps.
"""
from __future__ import annotations

import argparse

import flint


def enumerate_field(context, p: int, degree: int):
    generator = context.gen()
    elements = [context(value) for value in range(p)]
    power = context(1)
    for _ in range(1, degree):
        power *= generator
        block = [context(value) * power for value in range(p)]
        elements = [left + right for left in elements for right in block]
    return elements


def is_irreducible(polynomial, p: int) -> bool:
    _, factors = polynomial.factor()
    return (
        len(factors) == 1
        and factors[0][1] == 1
        and factors[0][0].degree() == p
    )


def trace_sum(p: int, degree: int) -> tuple[int, int, int]:
    context = flint.fq_default_ctx(p, degree)
    polynomial_context = flint.fq_default_poly_ctx(context)
    elements = enumerate_field(context, p, degree)
    cardinality = p**degree
    zero = context(0)
    two = context(2)
    three = context(3)

    irreducible_total = 0
    for q in elements:
        if q == zero or q == two:
            continue
        for t in elements:
            coefficients = [context(0)] * (p + 1)
            coefficients[0] = -(q - two) * t
            coefficients[1] = -three
            coefficients[3] = context(1)
            coefficients[p] = q
            if is_irreducible(polynomial_context(coefficients), p):
                irreducible_total += 1

    trace = (cardinality - 2) * cardinality - p * irreducible_total
    return cardinality, irreducible_total, trace


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("--max-degree", type=int, default=2)
    arguments = parser.parse_args()

    for degree in range(1, arguments.max_degree + 1):
        cardinality, count, trace = trace_sum(arguments.p, degree)
        print(
            f"p={arguments.p} r={degree} Q={cardinality} "
            f"irreducible_total={count} qline_trace={trace}"
        )


if __name__ == "__main__":
    main()
