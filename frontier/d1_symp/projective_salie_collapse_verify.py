#!/usr/bin/env python3
"""Exact F_(5^5) verification of the projective Salié collapse."""

from __future__ import annotations

from itertools import product
from typing import Tuple

P = 5
Q = P**5
FieldElement = Tuple[int, int, int, int, int]
ZERO: FieldElement = (0, 0, 0, 0, 0)
ONE: FieldElement = (1, 0, 0, 0, 0)
ELEMENTS = [tuple(values) for values in product(range(P), repeat=5)]


def add(left: FieldElement, right: FieldElement) -> FieldElement:
    return tuple((x + y) % P for x, y in zip(left, right))  # type: ignore[return-value]


def multiply(left: FieldElement, right: FieldElement) -> FieldElement:
    coefficients = [0] * 9
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            coefficients[i + j] = (coefficients[i + j] + x * y) % P
    for degree in range(8, 4, -1):
        coefficient = coefficients[degree]
        if coefficient:
            coefficients[degree] = 0
            coefficients[degree - 4] = (
                coefficients[degree - 4] + coefficient
            ) % P
            coefficients[degree - 5] = (
                coefficients[degree - 5] + coefficient
            ) % P
    return tuple(coefficients[:5])  # type: ignore[return-value]


def power(base: FieldElement, exponent: int) -> FieldElement:
    result = ONE
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent >>= 1
    return result


def inverse(value: FieldElement) -> FieldElement:
    if value == ZERO:
        raise ZeroDivisionError
    return power(value, Q - 2)


def trace(value: FieldElement) -> int:
    total = ZERO
    current = value
    for _ in range(5):
        total = add(total, current)
        current = power(current, P)
    assert total[1:] == (0, 0, 0, 0)
    return total[0]


def extension_chi(value: FieldElement) -> int:
    if value == ZERO:
        return 0
    result = power(value, (Q - 1) // 2)
    if result == ONE:
        return 1
    assert result == (P - 1, 0, 0, 0, 0)
    return -1


def base_chi(value: int) -> int:
    value %= P
    if value == 0:
        return 0
    return 1 if pow(value, (P - 1) // 2, P) == 1 else -1


def scalar_multiply(scalar: int, value: FieldElement) -> FieldElement:
    return tuple(scalar * coordinate % P for coordinate in value)  # type: ignore[return-value]


def canonical_line(value: FieldElement) -> FieldElement:
    index = next(i for i, coordinate in enumerate(value) if coordinate)
    return scalar_multiply(pow(value[index], -1, P), value)


def main() -> None:
    trace_zero = [value for value in ELEMENTS if trace(value) == 0]
    seen = set()

    r_all = 0
    r_zero = 0
    d_sum = 0
    regular_lines = 0
    degenerate_lines = 0

    for value in trace_zero:
        if value == ZERO:
            continue
        line = canonical_line(value)
        if line in seen:
            continue
        seen.add(line)

        delta = trace(inverse(value))
        cubic = trace(multiply(multiply(value, value), value))
        if delta != 0:
            regular_lines += 1
            weight = extension_chi(value) * base_chi(delta)
            r_all += weight
            if cubic == 0:
                r_zero += weight
        else:
            degenerate_lines += 1
            if cubic != 0:
                d_sum += extension_chi(value) * base_chi(cubic)

    assert len(seen) == (P**4 - 1) // (P - 1) == 156
    assert regular_lines + degenerate_lines == 156
    assert r_all == 25
    assert r_zero == -5
    assert d_sum == -5

    s_regular = P * r_zero - r_all
    gauss_times_s_degenerate = base_chi(-1) * P * d_sum
    assert s_regular == -50
    assert gauss_times_s_degenerate == -25

    second_moment = (
        P ** (P - 1)
        + base_chi(-1) * P ** ((P - 1) // 2) * s_regular
        + base_chi(3) * P ** ((P + 1) // 2) * d_sum
    )
    assert second_moment == 0

    print("PROJECTIVE_SALIE_COLLAPSE_VERIFY: PASS")
    print("projective lines:", len(seen))
    print("regular lines:", regular_lines)
    print("degenerate lines:", degenerate_lines)
    print("R_all:", r_all)
    print("R_0:", r_zero)
    print("D:", d_sum)
    print("S_reg=5R_0-R_all:", s_regular)
    print("G_5*S_deg=5D:", gauss_times_s_degenerate)
    print("|T_5|^2:", second_moment)


if __name__ == "__main__":
    main()
