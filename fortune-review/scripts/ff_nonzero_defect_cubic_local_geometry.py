#!/usr/bin/env python3
"""Exact local-geometry audit at the canonical q=11,k=3 defect point.

This script is independent of Singular.  It constructs F_(11^3), embeds the
four canonical irreducible cubics in one splitting field, evaluates the twelve
bounded-degree root equations plus the affine gauge, computes the exact
Jacobian rank, and tests recursive formal lifting along the unique tangent
through order 12.

A finite formal jet is not promoted to a positive-dimensional component.  The
script records only machine-verified local geometry; the saturated global
ideal remains the theorem-level discriminator.
"""
from __future__ import annotations
import json
from itertools import product
from typing import Iterable

Q = 11
K = 3
ORDER = 12
Element = tuple[int, int, int]
ZERO: Element = (0, 0, 0)
ONE: Element = (1, 0, 0)
# Canonical P=x^3+8x+5 is used as the common field modulus.
MODULUS = (5, 8, 0, 1)


def scalar(value: int) -> Element:
    return (value % Q, 0, 0)


def add(left: Element, right: Element) -> Element:
    return tuple((left[i] + right[i]) % Q for i in range(3))  # type: ignore[return-value]


def neg(value: Element) -> Element:
    return tuple((-entry) % Q for entry in value)  # type: ignore[return-value]


def sub(left: Element, right: Element) -> Element:
    return add(left, neg(right))


def mul(left: Element, right: Element) -> Element:
    temporary = [0] * 5
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            temporary[i + j] = (temporary[i + j] + x * y) % Q
    for degree in (4, 3):
        coefficient = temporary[degree] % Q
        if coefficient:
            temporary[degree] = 0
            temporary[degree - 3] = (temporary[degree - 3] - coefficient * MODULUS[0]) % Q
            temporary[degree - 2] = (temporary[degree - 2] - coefficient * MODULUS[1]) % Q
            temporary[degree - 1] = (temporary[degree - 1] - coefficient * MODULUS[2]) % Q
    return tuple(temporary[:3])  # type: ignore[return-value]


def power(value: Element, exponent: int) -> Element:
    result = ONE
    base = value
    while exponent:
        if exponent & 1:
            result = mul(result, base)
        base = mul(base, base)
        exponent >>= 1
    return result


def inverse(value: Element) -> Element:
    if value == ZERO:
        raise ZeroDivisionError
    return power(value, Q**K - 2)


def divide(left: Element, right: Element) -> Element:
    return mul(left, inverse(right))


def evaluate_polynomial(coefficients: tuple[int, ...], value: Element) -> Element:
    result = ZERO
    for coefficient in reversed(coefficients):
        result = add(mul(result, value), scalar(coefficient))
    return result


def product_elements(values: Iterable[Element]) -> Element:
    result = ONE
    for value in values:
        result = mul(result, value)
    return result


POLYNOMIALS = {
    "a": (5, 8, 0, 1),
    "b": (1, 2, 10, 1),
    "c": (9, 1, 10, 1),
    "d": (9, 9, 0, 1),
}
ALL_ELEMENTS = [(x, y, z) for x in range(Q) for y in range(Q) for z in range(Q)]
ROOTS: dict[str, list[Element]] = {}
for name, polynomial in POLYNOMIALS.items():
    roots = [value for value in ALL_ELEMENTS if evaluate_polynomial(polynomial, value) == ZERO]
    assert len(roots) == K
    start = roots[0]
    cycle = [start, power(start, Q), power(start, Q * Q)]
    assert len(set(cycle)) == K
    ROOTS[name] = cycle

BASE_VALUES = ROOTS["a"] + ROOTS["b"] + ROOTS["c"] + ROOTS["d"] + [scalar(8)]
assert len(BASE_VALUES) == 13


# Generic truncated-series arithmetic over F_(11^3).
def series_add(left: list[Element], right: list[Element], order: int) -> list[Element]:
    return [add(left[i], right[i]) for i in range(order + 1)]


def series_neg(value: list[Element], order: int) -> list[Element]:
    return [neg(value[i]) for i in range(order + 1)]


def series_sub(left: list[Element], right: list[Element], order: int) -> list[Element]:
    return series_add(left, series_neg(right, order), order)


def series_mul(left: list[Element], right: list[Element], order: int) -> list[Element]:
    result = [ZERO] * (order + 1)
    for i in range(order + 1):
        for j in range(order + 1 - i):
            result[i + j] = add(result[i + j], mul(left[i], right[j]))
    return result


def series_product(values: Iterable[list[Element]], order: int) -> list[Element]:
    result = [ONE] + [ZERO] * order
    for value in values:
        result = series_mul(result, value, order)
    return result


def evaluate_equations(values: list[list[Element]], order: int) -> list[list[Element]]:
    a = values[0:3]
    b = values[3:6]
    c = values[6:9]
    d = values[9:12]
    rho = values[12]
    equations: list[list[Element]] = []
    for index in range(3):
        nxt = (index + 1) % 3
        equations.append(
            series_sub(
                series_mul(
                    series_sub(a[nxt], a[index], order),
                    series_product([series_sub(a[index], root, order) for root in b], order),
                    order,
                ),
                series_product([series_sub(a[index], root, order) for root in c], order),
                order,
            )
        )
        equations.append(
            series_add(
                series_mul(
                    series_sub(c[nxt], c[index], order),
                    series_product([series_sub(c[index], root, order) for root in d], order),
                    order,
                ),
                series_product([series_sub(c[index], root, order) for root in a], order),
                order,
            )
        )
        equations.append(
            series_add(
                series_mul(
                    series_sub(b[nxt], b[index], order),
                    series_product([series_sub(b[index], root, order) for root in a], order),
                    order,
                ),
                series_mul(
                    rho,
                    series_product([series_sub(b[index], root, order) for root in d], order),
                    order,
                ),
                order,
            )
        )
        equations.append(
            series_sub(
                series_mul(
                    series_sub(d[nxt], d[index], order),
                    series_product([series_sub(d[index], root, order) for root in c], order),
                    order,
                ),
                series_mul(
                    rho,
                    series_product([series_sub(d[index], root, order) for root in b], order),
                    order,
                ),
                order,
            )
        )
    gauge = [ZERO] * (order + 1)
    for root in a:
        gauge = series_add(gauge, root, order)
    equations.append(gauge)
    return equations


# Exact Jacobian by dual-number evaluation.
JACOBIAN: list[list[Element]] = [[ZERO] * 13 for _ in range(13)]
for column in range(13):
    dual_values = []
    for index, value in enumerate(BASE_VALUES):
        dual_values.append([value, ONE if index == column else ZERO])
    evaluated = evaluate_equations(dual_values, 1)
    for row in range(13):
        assert evaluated[row][0] == ZERO
        JACOBIAN[row][column] = evaluated[row][1]


def rref(matrix: list[list[Element]]) -> tuple[list[list[Element]], list[int]]:
    result = [row[:] for row in matrix]
    row = 0
    pivots: list[int] = []
    for column in range(len(result[0])):
        pivot = next((index for index in range(row, len(result)) if result[index][column] != ZERO), None)
        if pivot is None:
            continue
        result[pivot], result[row] = result[row], result[pivot]
        pivot_inverse = inverse(result[row][column])
        result[row] = [mul(entry, pivot_inverse) for entry in result[row]]
        for index in range(len(result)):
            if index != row and result[index][column] != ZERO:
                factor = result[index][column]
                result[index] = [
                    sub(result[index][j], mul(factor, result[row][j]))
                    for j in range(len(result[index]))
                ]
        pivots.append(column)
        row += 1
        if row == len(result):
            break
    return result, pivots


RREF, PIVOTS = rref(JACOBIAN)
RANK = len(PIVOTS)
assert RANK == 12
assert PIVOTS == list(range(12))
TANGENT = [ZERO] * 13
TANGENT[12] = ONE
for row, pivot in enumerate(PIVOTS):
    TANGENT[pivot] = neg(RREF[row][12])


def solve_linear(right_hand_side: list[Element]) -> list[Element] | None:
    augmented = [JACOBIAN[i][:] + [right_hand_side[i]] for i in range(13)]
    reduced, pivots = rref(augmented)
    for row in reduced:
        if all(entry == ZERO for entry in row[:13]) and row[13] != ZERO:
            return None
    solution = [ZERO] * 13
    for row, pivot in enumerate(pivots):
        if pivot < 13:
            solution[pivot] = reduced[row][13]
    return solution


COEFFICIENTS = [[BASE_VALUES[index], TANGENT[index]] for index in range(13)]
FORMAL_ORDERS: list[int] = [1]
for order in range(2, ORDER + 1):
    trial = [series + [ZERO] * (order + 1 - len(series)) for series in COEFFICIENTS]
    residuals = [equation[order] for equation in evaluate_equations(trial, order)]
    correction = solve_linear([neg(value) for value in residuals])
    if correction is None:
        break
    # The free rho coefficient is fixed to zero after the first-order parameter.
    assert correction[12] == ZERO
    for index in range(13):
        COEFFICIENTS[index].append(correction[index])
    FORMAL_ORDERS.append(order)

assert FORMAL_ORDERS == list(range(1, ORDER + 1))

RESULT = {
    "status": "MACHINE-VERIFIED LOCAL GEOMETRY",
    "q": Q,
    "k": K,
    "normalized_lambda": 1,
    "normalized_rho": 8,
    "jacobian_equations": 13,
    "jacobian_variables": 13,
    "jacobian_rank": RANK,
    "tangent_dimension": 1,
    "root_variable_columns_are_pivots": True,
    "formal_lift_verified_through_order": ORDER,
    "boundary": (
        "A one-dimensional tangent and a finite formal jet do not prove a positive-dimensional "
        "component; the saturated global ideal remains open until a certified standard basis is obtained."
    ),
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
