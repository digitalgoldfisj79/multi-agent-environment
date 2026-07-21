#!/usr/bin/env python3
"""Independent checks for DISCRIMINANT_MASS.md.

Standard library only.

Checks:
  1. Pointwise discriminant formula against a Sylvester determinant.
  2. Full-slice character-mass and discriminant-zero formulas.
  3. Rootless-tail restricted masses as diagnostics only.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


def primes_upto(limit: int) -> list[int]:
    out: list[int] = []
    for n in range(2, limit + 1):
        if all(n % q for q in range(2, isqrt(n) + 1)):
            out.append(n)
    return out


def chi(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(a for a in range(2, p) if chi(a, p) == -1)


def discriminant_formula(p: int, a: int, c: int, d: int) -> int:
    """DM.1, returned as an element of F_p represented by 0..p-1."""
    a %= p
    c %= p
    d %= p
    if p < 5 or a == 0:
        raise ValueError("requires prime p >= 5 and a != 0")

    s = -1 if ((p - 1) // 2) % 2 else 1
    if c == 0:
        return (s * 3 * a * d * d) % p

    eps = chi((-c * pow(3 * a, -1, p)) % p, p)
    inv3 = pow(3, -1, p)
    linear = (eps + 2 * c * inv3) % p
    return (s * (3 * a * d * d + c * linear * linear)) % p


def det_mod(matrix: list[list[int]], p: int) -> int:
    a = [[entry % p for entry in row] for row in matrix]
    n = len(a)
    det = 1
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pivot_value = a[col][col]
        det = det * pivot_value % p
        inv_pivot = pow(pivot_value, -1, p)
        for row in range(col + 1, n):
            if not a[row][col]:
                continue
            factor = a[row][col] * inv_pivot % p
            for j in range(col, n):
                a[row][j] = (a[row][j] - factor * a[col][j]) % p
    return det % p


def sylvester_resultant(
    f_descending: list[int], g_descending: list[int], p: int
) -> int:
    """Resultant by the determinant of the Sylvester matrix."""
    n = len(f_descending) - 1
    m = len(g_descending) - 1
    size = n + m
    matrix: list[list[int]] = []

    for shift in range(m):
        row = [0] * size
        row[shift : shift + n + 1] = f_descending
        matrix.append(row)

    for shift in range(n):
        row = [0] * size
        row[shift : shift + m + 1] = g_descending
        matrix.append(row)

    return det_mod(matrix, p)


def discriminant_sylvester(p: int, a: int, c: int, d: int) -> int:
    """Independent discriminant calculation from Res(f,f')."""
    f = [0] * (p + 1)  # descending coefficients, degree p to 0
    f[0] = 1
    f[p - 3] = a % p
    f[p - 1] = c % p
    f[p] = d % p
    derivative = [(3 * a) % p, 0, c % p]
    resultant = sylvester_resultant(f, derivative, p)
    sign = -1 if (p * (p - 1) // 2) % 2 else 1
    return sign * resultant % p


@dataclass(frozen=True)
class PredictedMass:
    mass: int
    zero_count: int


def predicted_mass(p: int, a: int) -> PredictedMass:
    delta = chi(2 * a, p)
    if p % 4 == 1:
        return PredictedMass(p * chi(3 * a, p), p - delta)
    if delta == 1:
        return PredictedMass(-2 * p * chi(3 * a, p), p)
    return PredictedMass(0, p)


def brute_mass(p: int, a: int) -> PredictedMass:
    mass = 0
    zero_count = 0
    for c in range(p):
        for d in range(p):
            value = chi(discriminant_formula(p, a, c, d), p)
            mass += value
            zero_count += value == 0
    return PredictedMass(mass, zero_count)


def tail_is_rootless(p: int, a: int, c: int, d: int) -> bool:
    return all((a * x**3 + c * x + d) % p for x in range(p))


def restricted_rootless_mass(p: int, a: int) -> tuple[int, int, int]:
    count = 0
    mass = 0
    zero_count = 0
    for c in range(p):
        for d in range(p):
            if not tail_is_rootless(p, a, c, d):
                continue
            count += 1
            value = chi(discriminant_formula(p, a, c, d), p)
            mass += value
            zero_count += value == 0
    return count, mass, zero_count


def verify_pointwise() -> None:
    for p in (5, 7, 11, 13):
        checked = 0
        for a in range(1, p):
            for c in range(p):
                for d in range(p):
                    expected = discriminant_formula(p, a, c, d)
                    actual = discriminant_sylvester(p, a, c, d)
                    assert actual == expected, (p, a, c, d, actual, expected)
                    checked += 1
        print(f"PASS pointwise p={p}: {checked} tuples")


def verify_mass(limit: int = 199) -> None:
    for p in primes_upto(limit):
        if p < 5:
            continue
        for a in (1, least_nonsquare(p)):
            actual = brute_mass(p, a)
            expected = predicted_mass(p, a)
            assert actual == expected, (p, a, actual, expected)
    print(f"PASS mass and zero-count formulas for both square classes, p <= {limit}")


def print_restricted_diagnostics(limit: int = 47) -> None:
    print("\nRootless-tail restricted diagnostics (not a theorem):")
    print("p class a rootless_count restricted_mass disc_zero_count")
    for p in primes_upto(limit):
        if p < 5:
            continue
        r = least_nonsquare(p)
        for label, a in (("square", 1), ("nonsquare", r)):
            count, mass, zeros = restricted_rootless_mass(p, a)
            assert count == (p * p - 1) // 3
            print(p, label, a, count, mass, zeros)


def main() -> None:
    verify_pointwise()
    verify_mass()
    print_restricted_diagnostics()
    print("\nALL PROVED FORMULA CHECKS PASSED")


if __name__ == "__main__":
    main()
