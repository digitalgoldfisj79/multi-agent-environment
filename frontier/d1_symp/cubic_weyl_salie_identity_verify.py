#!/usr/bin/env python3
"""Exact F_(5^5) verification of the cubic Weyl--Salié identity.

The field is F_5[t]/(t^5-t-1). Cyclotomic values are represented exactly in
Z[zeta_5] by coefficient vectors modulo 1+zeta+...+zeta^4=0.

The verifier checks

    |T_5|^2
      = 5^4
        + 5^2 S_reg
        - 5^2 G_5 S_deg,

which is the p=5 specialization of
CUBIC_WEYL_DIFFERENCING_TO_RECIPROCAL_SALIE_SUMS_20260725.md.
"""

from __future__ import annotations

from itertools import product
from typing import Tuple

P = 5
Q = P**5
FieldElement = Tuple[int, int, int, int, int]
Cyclotomic = Tuple[int, int, int, int, int]
ZERO: FieldElement = (0, 0, 0, 0, 0)
ONE: FieldElement = (1, 0, 0, 0, 0)
ELEMENTS = [tuple(values) for values in product(range(P), repeat=5)]


# ---------------------------------------------------------------------------
# Exact cyclotomic arithmetic
# ---------------------------------------------------------------------------


def cyc_canonical(vector: Cyclotomic) -> Cyclotomic:
    final = vector[-1]
    return tuple(value - final for value in vector[:-1]) + (0,)  # type: ignore[return-value]


def cyc_add(left: Cyclotomic, right: Cyclotomic) -> Cyclotomic:
    return tuple(x + y for x, y in zip(left, right))  # type: ignore[return-value]


def cyc_scale(vector: Cyclotomic, scalar: int) -> Cyclotomic:
    return tuple(scalar * value for value in vector)  # type: ignore[return-value]


def cyc_multiply(left: Cyclotomic, right: Cyclotomic) -> Cyclotomic:
    output = [0] * P
    for i, x in enumerate(left):
        if x:
            for j, y in enumerate(right):
                if y:
                    output[(i + j) % P] += x * y
    return cyc_canonical(tuple(output))


def cyc_conjugate(vector: Cyclotomic) -> Cyclotomic:
    output = [0] * P
    for exponent, coefficient in enumerate(vector):
        output[(-exponent) % P] += coefficient
    return cyc_canonical(tuple(output))


def cyc_integer(value: int) -> Cyclotomic:
    return (value, 0, 0, 0, 0)


def additive_character(value: int) -> Cyclotomic:
    output = [0] * P
    output[value % P] = 1
    return cyc_canonical(tuple(output))


# ---------------------------------------------------------------------------
# F_(5^5) arithmetic modulo t^5-t-1
# ---------------------------------------------------------------------------


def field_add(left: FieldElement, right: FieldElement) -> FieldElement:
    return tuple((x + y) % P for x, y in zip(left, right))  # type: ignore[return-value]


def field_multiply(left: FieldElement, right: FieldElement) -> FieldElement:
    coefficients = [0] * 9
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            coefficients[i + j] = (coefficients[i + j] + x * y) % P

    # t^5=t+1, so t^k=t^(k-4)+t^(k-5) for k>=5.
    for degree in range(8, 4, -1):
        coefficient = coefficients[degree] % P
        if coefficient:
            coefficients[degree] = 0
            coefficients[degree - 4] = (
                coefficients[degree - 4] + coefficient
            ) % P
            coefficients[degree - 5] = (
                coefficients[degree - 5] + coefficient
            ) % P
    return tuple(coefficients[:5])  # type: ignore[return-value]


def field_power(base: FieldElement, exponent: int) -> FieldElement:
    result = ONE
    while exponent:
        if exponent & 1:
            result = field_multiply(result, base)
        base = field_multiply(base, base)
        exponent >>= 1
    return result


def field_inverse(value: FieldElement) -> FieldElement:
    if value == ZERO:
        raise ZeroDivisionError
    return field_power(value, Q - 2)


def field_trace(value: FieldElement) -> int:
    total = ZERO
    current = value
    for _ in range(5):
        total = field_add(total, current)
        current = field_power(current, P)
    assert total[1:] == (0, 0, 0, 0)
    return total[0]


def extension_quadratic_character(value: FieldElement) -> int:
    if value == ZERO:
        return 0
    result = field_power(value, (Q - 1) // 2)
    if result == ONE:
        return 1
    assert result == (P - 1, 0, 0, 0, 0)
    return -1


def base_quadratic_character(value: int) -> int:
    value %= P
    if value == 0:
        return 0
    return 1 if pow(value, (P - 1) // 2, P) == 1 else -1


# ---------------------------------------------------------------------------
# Identity
# ---------------------------------------------------------------------------


def main() -> None:
    trace_zero = [value for value in ELEMENTS if field_trace(value) == 0]
    assert len(trace_zero) == P**4

    inverse_four = pow(4, -1, P)
    three = (3, 0, 0, 0, 0)

    t_value = cyc_integer(0)
    s_regular = cyc_integer(0)
    s_degenerate = cyc_integer(0)
    regular_count = 0
    degenerate_count = 0

    for value in trace_zero:
        value_cubed = field_multiply(field_multiply(value, value), value)
        phase = field_trace(value_cubed) * inverse_four % P

        # T_5 uses phase x^3, not x^3/4.
        t_value = cyc_add(
            t_value,
            additive_character(field_trace(value_cubed)),
        )

        if value == ZERO:
            continue

        inverse = field_inverse(value)
        delta = field_trace(inverse)
        character_extension = extension_quadratic_character(value)
        term = cyc_scale(additive_character(phase), character_extension)

        if delta == 0:
            degenerate_count += 1
            s_degenerate = cyc_add(s_degenerate, term)
        else:
            regular_count += 1
            term = cyc_scale(term, base_quadratic_character(delta))
            s_regular = cyc_add(s_regular, term)

    gauss = cyc_integer(0)
    for scalar in range(P):
        gauss = cyc_add(gauss, additive_character(scalar * scalar))

    left = cyc_multiply(t_value, cyc_conjugate(t_value))

    chi_minus_one = base_quadratic_character(-1)
    chi_three = base_quadratic_character(3)
    right = cyc_integer(P**4)
    right = cyc_add(
        right,
        cyc_scale(s_regular, chi_minus_one * P**2),
    )
    right = cyc_add(
        right,
        cyc_scale(
            cyc_multiply(gauss, s_degenerate),
            chi_minus_one * chi_three * P**2,
        ),
    )
    right = cyc_canonical(right)

    assert left == right
    assert t_value == cyc_integer(0)
    assert s_regular == cyc_integer(-50)
    assert cyc_multiply(gauss, s_degenerate) == cyc_integer(-25)
    assert regular_count + degenerate_count == P**4 - 1

    print("CUBIC_WEYL_SALIE_IDENTITY_VERIFY: PASS")
    print("trace-zero points:", len(trace_zero))
    print("regular nonzero points:", regular_count)
    print("degenerate nonzero points:", degenerate_count)
    print("T_5:", t_value)
    print("S_reg:", s_regular)
    print("G_5*S_deg:", cyc_multiply(gauss, s_degenerate))
    print("|T_5|^2 = RHS:", left)


if __name__ == "__main__":
    main()
