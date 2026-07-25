#!/usr/bin/env python3
"""Exact cyclotomic verification of the Laurent--Airy fibre dichotomy.

For each selected (p,u,s), compute the four Frobenius power traces directly
from finite-field exponential sums and reconstruct the degree-four fibre
polynomial by Newton identities.  No floating-point eigenvalues are used.

Requires python-flint.
"""
from __future__ import annotations

from itertools import product

from flint import fq_default_ctx

Vector = tuple[int, ...]


def canonical(vector: Vector) -> Vector:
    final = vector[-1]
    return tuple(value - final for value in vector[:-1]) + (0,)


def add(left: Vector, right: Vector) -> Vector:
    return tuple(x + y for x, y in zip(left, right))


def negate(vector: Vector) -> Vector:
    return tuple(-x for x in vector)


def scale(vector: Vector, scalar: int) -> Vector:
    return tuple(scalar * x for x in vector)


def multiply(left: Vector, right: Vector, p: int) -> Vector:
    output = [0] * p
    for i, x in enumerate(left):
        if x:
            for j, y in enumerate(right):
                if y:
                    output[(i + j) % p] += x * y
    return canonical(tuple(output))


def integer(p: int, value: int = 1) -> Vector:
    return (value,) + (0,) * (p - 1)


def quadratic_character(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def field_elements(context, p: int, degree: int):
    for coefficients in product(range(p), repeat=degree):
        yield context(list(coefficients))


def power_trace(p: int, u: int, s: int, degree: int) -> Vector:
    context = fq_default_ctx(p, degree, "a")
    parameter_u = context(u)
    parameter_s = context(s)
    output = [0] * p

    for x in field_elements(context, p, degree):
        if x.is_zero():
            continue
        character = 1 if x.is_square() else -1
        phase = int(
            (x**3 + parameter_u * x + parameter_s * x.inverse()).trace()
        ) % p
        # H_c^1 trace is minus the rank-one exponential sum.
        output[phase] -= character

    return canonical(tuple(output))


def characteristic_coefficients(p: int, u: int, s: int) -> list[Vector]:
    traces = [None] + [power_trace(p, u, s, degree) for degree in range(1, 5)]
    elementary = [integer(p)]

    for k in range(1, 5):
        total = (0,) * p
        for i in range(1, k + 1):
            term = multiply(elementary[k - i], traces[i], p)
            if i % 2 == 0:
                term = negate(term)
            total = add(total, term)

        assert all(value % k == 0 for value in total), (p, u, s, k, total)
        elementary.append(tuple(value // k for value in total))

    return elementary[1:]


def verify_fibre(p: int, u: int, s: int) -> None:
    e1, e2, e3, e4 = characteristic_coefficients(p, u, s)
    character_s = quadratic_character(s, p)

    assert e3 == scale(e1, -quadratic_character(-1, p) * character_s * p), (
        p,
        u,
        s,
        "e3",
        e1,
        e3,
    )
    assert e4 == integer(p, -character_s * p * p), (p, u, s, "e4", e4)

    if character_s == 1:
        assert e2 == (0,) * p, (p, u, s, "e2", e2)


def verify_prime(p: int, complete: bool) -> None:
    if p % 6 != 5:
        raise ValueError("the theorem is restricted to p congruent 5 modulo 6")

    if complete:
        parameters_u = range(p)
        parameters_s = range(1, p)
    else:
        nonsquare = next(
            value for value in range(2, p) if quadratic_character(value, p) == -1
        )
        parameters_u = (0, 1)
        parameters_s = (1, nonsquare)

    checked = 0
    for u in parameters_u:
        for s in parameters_s:
            verify_fibre(p, u, s)
            checked += 1

    print(
        f"p={p}: {checked} fibres PASS; "
        "square fibres are arithmetic orientation-reversing"
    )


def main() -> None:
    verify_prime(5, complete=True)
    verify_prime(11, complete=False)
    verify_prime(17, complete=False)
    print("ARITHMETIC_ORIENTATION_FIBRE_VERIFY: PASS")


if __name__ == "__main__":
    main()
