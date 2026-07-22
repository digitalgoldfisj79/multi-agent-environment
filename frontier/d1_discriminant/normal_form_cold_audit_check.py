#!/usr/bin/env python3
"""Independent finite-field checks for NORMAL_FORM_COLD_AUDIT.md.

The script uses only the Python standard library. It verifies, for a range of
small odd primes and all nonsingular q,t pairs, that the Sylvester-determinant
resultant agrees with the corrected closed discriminant formula.

It also checks the split/nonsplit coefficient transformations and the fixed-a
quadratic-character selection rules.
"""

from __future__ import annotations

from itertools import product


def primes_upto(n: int) -> list[int]:
    out: list[int] = []
    for m in range(2, n + 1):
        if all(m % d for d in range(2, int(m**0.5) + 1)):
            out.append(m)
    return out


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    return 1 if z == 1 else -1


def inv(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def det_mod(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    n = len(a)
    det = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pv = a[col][col]
        det = det * pv % p
        ip = inv(pv, p)
        for r in range(col + 1, n):
            if not a[r][col]:
                continue
            factor = a[r][col] * ip % p
            for c in range(col, n):
                a[r][c] = (a[r][c] - factor * a[col][c]) % p
    return det % p


def sylvester_resultant(f_desc: list[int], g_desc: list[int], p: int) -> int:
    """Resultant from descending coefficient lists."""
    n = len(f_desc) - 1
    m = len(g_desc) - 1
    size = n + m
    mat = [[0] * size for _ in range(size)]
    for row in range(m):
        for j, coeff in enumerate(f_desc):
            mat[row][row + j] = coeff
    for row in range(n):
        for j, coeff in enumerate(g_desc):
            mat[m + row][row + j] = coeff
    return det_mod(mat, p)


def polynomial_coefficients(p: int, q: int, t: int) -> list[int]:
    coeffs = [0] * (p + 1)
    coeffs[0] = q                    # X^p
    coeffs[p - 3] = 1               # X^3
    coeffs[p - 1] = -3              # X
    coeffs[p] = -(q - 2) * t        # constant
    return coeffs


def check_discriminant_formula(max_prime: int = 23) -> None:
    for p in primes_upto(max_prime):
        if p < 5:
            continue
        sign = -1 if ((p * (p - 1) // 2) & 1) else 1
        derivative = [3, 0, -3]  # 3X^2-3 in characteristic p
        for q, t in product(range(1, p), range(p)):
            f = polynomial_coefficients(p, q, t)
            res = sylvester_resultant(f, derivative, p)
            expected_res = pow(3, p, p) * pow(q - 2, 2, p) * (t * t - 1)
            assert res % p == expected_res % p, (p, q, t, res, expected_res)

            disc = sign * inv(q, p) * res
            expected_disc = (
                sign
                * pow(3, p, p)
                * inv(q, p)
                * pow(q - 2, 2, p)
                * (t * t - 1)
            )
            assert disc % p == expected_disc % p

            if q != 2 and t not in (1, p - 1):
                # Remove the known square factors. The remaining character is
                # chi(kappa_p*q*(t^2-1)).
                kappa = sign * 3
                lhs = legendre(disc, p)
                rhs = legendre(kappa * q * (t * t - 1), p)
                assert lhs == rhs, (p, q, t, lhs, rhs)


def least_nonsquare(p: int) -> int:
    return next(a for a in range(2, p) if legendre(a, p) == -1)


def check_normal_form_signs(max_prime: int = 101) -> None:
    for p in primes_upto(max_prime):
        if p < 5:
            continue
        eta = least_nonsquare(p)
        delta = legendre(-1, p)
        for a in range(1, p):
            A = legendre(a, p)
            for c in range(1, p):
                eps = legendre(-c * inv(3 * a, p), p)
                q = (-3 * eps * inv(c, p)) % p
                assert q != 0
                if eps == 1:
                    assert legendre(q, p) == A
                    # Representative coefficients after F_p scaling.
                    assert (-3 * inv(q, p)) % p == c % p
                else:
                    assert legendre(q, p) == -delta * A
                    assert (3 * inv(q, p)) % p == c % p
                    # The representative cubic coefficient has the declared
                    # nonsplit square class.
                    a_rep = (-inv(eta * q, p)) % p
                    assert legendre(-c * inv(3 * a_rep, p), p) == -1


def main() -> None:
    check_discriminant_formula()
    check_normal_form_signs()
    print("PASS: corrected discriminant and normal-form sign checks")


if __name__ == "__main__":
    main()
