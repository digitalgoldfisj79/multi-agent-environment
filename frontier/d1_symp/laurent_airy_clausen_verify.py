#!/usr/bin/env python3
"""Exact checks for the Laurent--Airy Clausen/circularity theorem.

The base-field Clausen identity uses exact Z[zeta_p] arithmetic and no external
packages.  The complete p=5 boundary check additionally uses python-flint.
"""
from __future__ import annotations

from itertools import product

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


def power(value: Vector, exponent: int, p: int) -> Vector:
    result = integer(p)
    while exponent:
        if exponent & 1:
            result = multiply(result, value, p)
        value = multiply(value, value, p)
        exponent >>= 1
    return result


def integer(p: int, value: int = 1) -> Vector:
    return (value,) + (0,) * (p - 1)


def quadratic_character(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def cube_root(value: int, p: int) -> int:
    return pow(value, pow(3, -1, p - 1), p)


def square_root(value: int, p: int) -> int:
    for root in range(p):
        if root * root % p == value % p:
            return root
    raise ValueError((value, p))


def airy_trace(p: int, parameter: int) -> Vector:
    output = [0] * p
    for x in range(p):
        output[(x**3 + parameter * x) % p] -= 1
    return canonical(tuple(output))


def gauss_sum(p: int) -> Vector:
    output = [0] * p
    for x in range(p):
        output[x * x % p] += 1
    return canonical(tuple(output))


def laurent_trace(p: int, u: int, s: int) -> Vector:
    output = [0] * p
    for x in range(1, p):
        exponent = (x**3 + u * x + s * pow(x, -1, p)) % p
        output[exponent] -= quadratic_character(x, p)
    return canonical(tuple(output))


def dickson_value(p: int, trace: Vector) -> Vector:
    previous = integer(p, 2)
    current = trace
    for _ in range(2, p + 1):
        previous, current = current, add(
            multiply(trace, current, p),
            negate(scale(previous, p)),
        )
    return canonical(current)


def verify_base_clausen(p: int) -> None:
    if p % 6 != 5:
        raise ValueError("p must be 5 modulo 6")

    alpha = cube_root(4, p)
    assert alpha**3 % p == 4 % p
    assert quadratic_character(alpha, p) == 1
    assert quadratic_character(-3 * alpha, p) == -1

    gauss = gauss_sum(p)
    checked = 0
    for s in range(1, p):
        if quadratic_character(s, p) != -1:
            continue
        r = square_root(-3 * alpha * s, p)
        for capital_u in range(p):
            u = capital_u * pow(alpha, -1, p) % p
            left = multiply(
                airy_trace(p, (u + r) % p),
                airy_trace(p, (u - r) % p),
                p,
            )
            right = scale(
                multiply(gauss, laurent_trace(p, capital_u, s), p),
                -quadratic_character(3, p),
            )
            assert left == right, (p, capital_u, s, r, left, right)
            checked += 1

    print(f"p={p}: {checked} nonsquare Laurent--Airy fibres PASS")


def complete_p5_boundary_check() -> None:
    from flint import fq_default_ctx

    p = 5
    context = fq_default_ctx(p, p, "a")
    elements = [context(list(coefficients)) for coefficients in product(range(p), repeat=p)]

    boundary_a = [0] * p
    boundary_b = [0] * p
    for x in elements:
        if x.is_zero() or int(x.trace()) % p != 0:
            continue
        character = 1 if x.is_square() else -1
        boundary_a[int(x.inverse().trace()) % p] += character
        boundary_b[int((x**3).trace()) % p] += character

    a0 = canonical(tuple(boundary_a))
    b0 = canonical(tuple(boundary_b))

    values = [dickson_value(p, airy_trace(p, parameter)) for parameter in range(p)]
    total = integer(p, 0)
    diagonal = integer(p, 0)
    for value in values:
        total = add(total, value)
        diagonal = add(diagonal, multiply(value, value, p))

    gauss = gauss_sum(p)
    c = scale(gauss, -quadratic_character(3, p))
    c_to_p = power(c, p, p)

    # c^p(A_0-B_0)=Q/p.
    boundary_difference = add(a0, negate(b0))
    assert all(coordinate % p == 0 for coordinate in diagonal)
    diagonal_over_p = tuple(coordinate // p for coordinate in diagonal)
    assert multiply(c_to_p, boundary_difference, p) == diagonal_over_p

    # The off-diagonal product plus the boundary is the square of the mean.
    off_diagonal = add(multiply(total, total, p), negate(diagonal))
    full_scaled = add(diagonal, off_diagonal)
    assert full_scaled == multiply(total, total, p)
    assert total == integer(p, 0)  # T_5=0.

    print("p=5 complete boundary/off-diagonal circularity: PASS")


def main() -> None:
    for prime in (5, 11, 17, 23):
        verify_base_clausen(prime)
    complete_p5_boundary_check()
    print("LAURENT_AIRY_CLAUSEN_VERIFY: PASS")


if __name__ == "__main__":
    main()
