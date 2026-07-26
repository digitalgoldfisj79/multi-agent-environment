#!/usr/bin/env python3
"""Exact cyclotomic checks for the Hayes quartic dichotomy.

No floating point arithmetic is used.  A cyclotomic integer is represented by
its coefficient vector in Z[zeta_p]; equality is tested modulo
1+zeta+...+zeta^(p-1)=0.
"""

from __future__ import annotations

from itertools import product
from typing import Iterable


def chi(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def canonical(vector: list[int]) -> tuple[int, ...]:
    """Canonical coordinates modulo the all-ones cyclotomic relation."""
    tail = vector[-1]
    return tuple(value - tail for value in vector[:-1])


def add_scaled(left: list[int], right: list[int], scale: int) -> list[int]:
    return [a + scale * b for a, b in zip(left, right)]


def integer_vector(value: int, p: int) -> list[int]:
    result = [0] * p
    result[0] = value
    return result


def coefficient_vector(
    p: int, degree: int, u: int, w: int, v: int
) -> list[int]:
    counts = [0] * p
    for prefix in product(range(p), repeat=degree - 1):
        for constant in range(1, p):
            coefficients = list(prefix) + [constant]
            c1 = coefficients[0]
            c2 = coefficients[1] if degree >= 2 else 0
            c3 = coefficients[2] if degree >= 3 else 0
            c_nm1 = coefficients[-2] if degree >= 2 else 1

            s1 = -c1
            s3 = -c1**3 + 3 * c1 * c2 - 3 * c3
            if degree == 1:
                r1 = -pow(constant, -1, p)
            else:
                r1 = -c_nm1 * pow(constant, -1, p)
            norm = ((-1) ** degree) * constant
            phase = (u * s1 + w * s3 + v * r1) % p
            counts[phase] += chi(norm, p)
    return counts


def equal(left: list[int], right: list[int]) -> bool:
    return canonical(add_scaled(left, right, -1)) == (0,) * (len(left) - 1)


def verify_parameters(p: int, parameters: Iterable[tuple[int, int, int]]) -> None:
    for u, w, v in parameters:
        if w % p == 0 or v % p == 0:
            continue
        coefficients = {
            degree: coefficient_vector(p, degree, u, w, v)
            for degree in range(1, 5)
        }
        a = chi(v * pow(3 * w, -1, p), p)
        b = chi(-1, p)

        assert equal(
            coefficients[3],
            [p * a * value for value in coefficients[1]],
        )
        assert equal(coefficients[4], integer_vector(p * p * a * b, p))

        if a == -b:
            assert equal(coefficients[2], [0] * p)

        # Coefficient-level scaling law.  A constant quadratic twist by
        # chi(lambda) multiplies the degree-n coefficient by chi(lambda)^n.
        for lam in (1, 2, p - 1):
            transformed = (
                u * lam % p,
                w * pow(lam, 3, p) % p,
                v * pow(lam, -1, p) % p,
            )
            twist = chi(lam, p)
            for degree in range(1, 5):
                transformed_vector = coefficient_vector(
                    p, degree, *transformed
                )
                expected = [
                    (twist**degree) * value
                    for value in transformed_vector
                ]
                assert equal(coefficients[degree], expected)


def verify_degree_five_vanishing(p: int) -> None:
    selected = [
        (1, 1, 1),
        (2 % p, 1, 2 % p),
        (1, 2 % p, 1),
    ]
    for u, w, v in selected:
        vector = coefficient_vector(p, 5, u, w, v)
        assert equal(vector, [0] * p)


def verify_selected_sector(p: int) -> None:
    b = chi(-1, p)
    assert chi(3, p) == -b
    for v in range(1, p):
        a = chi(v * pow(3, -1, p), p)
        if chi(v, p) == -1:
            assert a == b
        else:
            assert a == -b


def main() -> None:
    # Exhaust all nonzero (w,v) and all u at p=5 and p=7.
    for p in (5, 7):
        parameters = (
            (u, w, v)
            for u in range(p)
            for w in range(1, p)
            for v in range(1, p)
        )
        verify_parameters(p, parameters)
        verify_degree_five_vanishing(p)
        if p % 6 == 5:
            verify_selected_sector(p)
        print(f"p={p}: exhaustive quartic checks PASS")

    # Selected higher-prime checks.
    for p in (11, 17):
        parameters = [
            (1, 1, 1),
            (2, 1, 2),
            (1, 2, 1),
            (3, 4, 5),
        ]
        verify_parameters(p, parameters)
        verify_degree_five_vanishing(p)
        verify_selected_sector(p)
        print(f"p={p}: selected quartic checks PASS")

    print("HAYES_QUARTIC_DICHOTOMY_VERIFY: PASS")


if __name__ == "__main__":
    main()
