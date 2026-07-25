#!/usr/bin/env python3
"""Exact verification of T_71 from local Airy traces and Dickson recurrence."""

from __future__ import annotations

from fractions import Fraction

P = 71
Vector = tuple[int, ...]
EXPECTED_SUM = -2607645185442448528174099331904108712984617191997478594165081742864
EXPECTED_T = 36727396978062655326395765238086038211050946366161670340353263984


def canonical(vector: Vector) -> Vector:
    final = vector[-1]
    return tuple(value - final for value in vector[:-1]) + (0,)


def add(left: Vector, right: Vector) -> Vector:
    return tuple(x + y for x, y in zip(left, right))


def negate(vector: Vector) -> Vector:
    return tuple(-x for x in vector)


def scale(vector: Vector, scalar: int) -> Vector:
    return tuple(scalar * x for x in vector)


def multiply(left: Vector, right: Vector) -> Vector:
    output = [0] * P
    for i, x in enumerate(left):
        if x:
            for j, y in enumerate(right):
                if y:
                    output[(i + j) % P] += x * y
    return canonical(tuple(output))


def integer(value: int) -> Vector:
    return (value,) + (0,) * (P - 1)


def airy_trace(parameter: int) -> Vector:
    output = [0] * P
    for x in range(P):
        output[(x**3 + parameter * x) % P] -= 1
    return canonical(tuple(output))


def dickson_value(trace: Vector) -> Vector:
    previous = integer(2)
    current = trace
    for _ in range(2, P + 1):
        previous, current = current, add(
            multiply(trace, current),
            negate(scale(previous, P)),
        )
    return canonical(current)


def hasse_residue() -> int:
    h = (P - 2) // 3
    # Rayleigh recurrence in F_p.
    r = [(-pow(36, -1, P)) % P]
    for n in range(1, h):
        convolution = sum(r[i] * r[n - 1 - i] for i in range(n)) % P
        r.append((-3 * convolution * pow(3 * n + 4, -1, P)) % P)

    factorial_h = 1
    for value in range(1, h + 1):
        factorial_h = factorial_h * value % P

    factorial_2h1 = 1
    for value in range(1, 2 * h + 2):
        factorial_2h1 = factorial_2h1 * value % P

    first = (
        factorial_h
        * pow(6, -1, P)
        * pow(factorial_2h1, -2, P)
    ) % P
    log_coefficient = r[h - 1] * pow(h, -1, P) % P
    second = log_coefficient * pow(factorial_h, -1, P) % P
    h_coefficient = (first + second) % P
    return (-h_coefficient) % P


def main() -> None:
    total = integer(0)
    for parameter in range(P):
        total = add(total, dickson_value(airy_trace(parameter)))

    assert total[1:] == (0,) * (P - 1)
    assert total[0] == EXPECTED_SUM
    assert total[0] == -P * EXPECTED_T

    valuation = 0
    quotient = EXPECTED_T
    while quotient % P == 0:
        valuation += 1
        quotient //= P
    assert valuation == 25
    assert quotient == 1921017986668211984
    assert quotient % P == 32
    assert hasse_residue() == 32

    target_ratio = Fraction(EXPECTED_T, P**35)
    assert target_ratio == Fraction(
        1921017986668211984,
        3255243551009881201,
    )
    weight_two_ratio = Fraction(EXPECTED_T, P**34)
    assert weight_two_ratio == Fraction(
        1921017986668211984,
        45848500718449031,
    )

    print("EXACT_T71_AIRY_DICKSON_VERIFY: PASS")
    print("sum f_71(u) =", total[0])
    print("T_71 =", EXPECTED_T)
    print("v_71(T_71) =", valuation)
    print("normalized residue =", quotient % P)
    print("T_71 / 71^35 =", float(target_ratio))


if __name__ == "__main__":
    main()
