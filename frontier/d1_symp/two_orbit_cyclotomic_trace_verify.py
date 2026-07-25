#!/usr/bin/env python3
"""Checks for TWO_ORBIT_REAL_CYCLOTOMIC_TRACE_REDUCTION_20260725.md."""

from __future__ import annotations

from math import factorial

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


def galois(vector: Vector, multiplier: int, p: int) -> Vector:
    output = [0] * p
    for exponent, coefficient in enumerate(vector):
        output[exponent * multiplier % p] += coefficient
    return canonical(tuple(output))


def quadratic_character(value: int, p: int) -> int:
    if value % p == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def choose_nonsquare_not_minus_one(p: int) -> int:
    for value in range(2, p):
        if value != p - 1 and quadratic_character(value, p) == -1:
            return value
    raise AssertionError(p)


def verify_prime(p: int) -> None:
    values = {u: dickson_value(p, airy_trace(p, u)) for u in range(p)}
    assert values[0] == integer(0, p)

    eta = choose_nonsquare_not_minus_one(p)
    squares = {value * value % p for value in range(1, p)}
    nonsquares = {eta * value % p for value in squares}
    assert len(squares) == len(nonsquares) == (p - 1) // 2
    assert squares.isdisjoint(nonsquares)

    # Representatives for Gal(K^+/Q)=F_p^*/{+-1}.
    representatives = []
    seen = set()
    for multiplier in range(1, p):
        key = min(multiplier, (-multiplier) % p)
        if key not in seen:
            seen.add(key)
            representatives.append(multiplier)

    square_orbit = {galois(values[1], a, p) for a in representatives}
    nonsquare_orbit = {galois(values[eta], a, p) for a in representatives}
    assert square_orbit == {values[u] for u in squares}
    assert nonsquare_orbit == {values[u] for u in nonsquares}

    gamma = add(values[1], values[eta])
    gamma_orbit = {galois(gamma, a, p) for a in representatives}
    assert len(gamma_orbit) == (p - 1) // 2

    trace_gamma = integer(0, p)
    for conjugate in gamma_orbit:
        trace_gamma = add(trace_gamma, conjugate)
    total = integer(0, p)
    for value in values.values():
        total = add(total, value)
    assert trace_gamma == total

    # Initial coefficient argument for maximal gamma orbit.
    h = (p - 2) // 3
    scalar = pow(factorial(h), -1, p)
    initial = {s * (1 + eta) * scalar % p for s in squares}
    assert len(initial) == (p - 1) // 2

    assert total[1:] == (0,) * (p - 1)
    print(
        f"p={p}: eta={eta}, two full orbits, gamma degree={(p-1)//2}, "
        f"p*T_p={total[0]}: PASS"
    )


def main() -> None:
    for p in (11, 17, 23, 29, 41, 47, 53):
        verify_prime(p)
    print("TWO_ORBIT_CYCLOTOMIC_TRACE_VERIFY: PASS")


if __name__ == "__main__":
    main()
