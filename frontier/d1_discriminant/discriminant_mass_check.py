#!/usr/bin/env python3
"""Independent checks for the d=1 discriminant/local-mass note.

Standard library only.

Checks:
  1. Pointwise discriminant formula against Sylvester determinants.
  2. Complete-slice character-mass and zero-count formulas.
  3. Correct local convention: a*x^3 + (c+1)*x + d.
  4. Local admissibility implies nonzero discriminant.
  5. Exact fixed-u count of irreducible depressed cubics.
  6. Exact restricted-mass decomposition LA.3.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


def primes_upto(limit: int) -> list[int]:
    return [
        n
        for n in range(2, limit + 1)
        if all(n % q for q in range(2, isqrt(n) + 1))
    ]


def chi(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(a for a in range(2, p) if chi(a, p) == -1)


def discriminant_formula(p: int, a: int, c: int, d: int) -> int:
    """DM.1, represented by an integer in 0..p-1."""
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
class MassAndZeros:
    mass: int
    zero_count: int


def predicted_full_mass(p: int, a: int) -> MassAndZeros:
    delta = chi(2 * a, p)
    if p % 4 == 1:
        return MassAndZeros(p * chi(3 * a, p), p - delta)
    if delta == 1:
        return MassAndZeros(-2 * p * chi(3 * a, p), p)
    return MassAndZeros(0, p)


def brute_full_mass(p: int, a: int) -> MassAndZeros:
    mass = 0
    zero_count = 0
    for c in range(p):
        for d in range(p):
            value = chi(discriminant_formula(p, a, c, d), p)
            mass += value
            zero_count += value == 0
    return MassAndZeros(mass, zero_count)


def phi_image(p: int, u: int) -> set[int]:
    return {(x**3 + u * x) % p for x in range(p)}


def irreducible_v_values(p: int, u: int) -> list[int]:
    """v such that x^3+u*x+v has no F_p root, hence is irreducible."""
    image = phi_image(p, u)
    return [v for v in range(p) if (-v) % p not in image]


def predicted_fixed_u_count(p: int, u: int) -> int:
    rho = chi(-3, p)
    if u % p:
        return (p - rho) // 3
    return ((1 + rho) * (p - 1)) // 3


def local_mass(p: int, a: int) -> tuple[int, int, int]:
    """count, discriminant mass, zero count under the correct +1 convention."""
    count = 0
    mass = 0
    zero_count = 0
    for u in range(p):
        for v in irreducible_v_values(p, u):
            c = (a * u - 1) % p
            d = (a * v) % p
            value = chi(discriminant_formula(p, a, c, d), p)
            count += 1
            mass += value
            zero_count += value == 0
    return count, mass, zero_count


def tail_discriminant(p: int, u: int, v: int) -> int:
    return (-4 * u**3 - 27 * v * v) % p


def restricted_components(p: int, a: int) -> tuple[int, int, int, int, int]:
    """Return S, C, R, tau, and (2S+C-R-tau)/3."""
    s_term = 0
    cross = 0
    root_incidence = 0

    for u in range(p):
        for v in range(p):
            c = (a * u - 1) % p
            d = (a * v) % p
            disc_char = chi(discriminant_formula(p, a, c, d), p)
            s_term += disc_char
            cross += chi(tail_discriminant(p, u, v), p) * disc_char

    for x in range(p):
        for u in range(p):
            v = (-x**3 - u * x) % p
            c = (a * u - 1) % p
            d = (a * v) % p
            root_incidence += chi(discriminant_formula(p, a, c, d), p)

    tau = chi(discriminant_formula(p, a, -1, 0), p)
    numerator = 2 * s_term + cross - root_incidence - tau
    assert numerator % 3 == 0
    return s_term, cross, root_incidence, tau, numerator // 3


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


def verify_full_mass(limit: int = 199) -> None:
    for p in primes_upto(limit):
        if p < 5:
            continue
        for a in (1, least_nonsquare(p)):
            actual = brute_full_mass(p, a)
            expected = predicted_full_mass(p, a)
            assert actual == expected, (p, a, actual, expected)
    print(f"PASS complete mass and zero-count formulas, p <= {limit}")


def verify_fixed_u(limit: int = 199) -> None:
    for p in primes_upto(limit):
        if p < 5:
            continue
        total = 0
        for u in range(p):
            actual = len(irreducible_v_values(p, u))
            expected = predicted_fixed_u_count(p, u)
            assert actual == expected, (p, u, actual, expected)
            total += actual
        assert total == (p * p - 1) // 3
    print(f"PASS fixed-u and total admissible-cubic counts, p <= {limit}")


def verify_local_squarefree_and_identity(limit: int = 79) -> None:
    print("\nCorrect locally admissible masses:")
    print("p class a count mass zero_count S C R tau")
    for p in primes_upto(limit):
        if p < 5:
            continue
        r = least_nonsquare(p)
        for label, a in (("square", 1), ("nonsquare", r)):
            count, mass, zeros = local_mass(p, a)
            assert count == (p * p - 1) // 3
            assert zeros == 0, (p, a, zeros)
            s_term, cross, root_incidence, tau, reconstructed = restricted_components(
                p, a
            )
            assert reconstructed == mass, (
                p,
                a,
                mass,
                reconstructed,
                s_term,
                cross,
                root_incidence,
                tau,
            )
            assert s_term == predicted_full_mass(p, a).mass
            print(
                p,
                label,
                a,
                count,
                mass,
                zeros,
                s_term,
                cross,
                root_incidence,
                tau,
            )
    print(f"PASS local squarefreeness and LA.3 identity, p <= {limit}")


def main() -> None:
    verify_pointwise()
    verify_full_mass()
    verify_fixed_u()
    verify_local_squarefree_and_identity()
    print("\nALL PROVED FORMULA CHECKS PASSED")


if __name__ == "__main__":
    main()
