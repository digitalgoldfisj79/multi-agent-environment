#!/usr/bin/env python3
"""Exhaustively verify the reduced Frobenius determinant criterion.

Standard library only. The default run checks both square classes of a for
p = 5, 7, 11, 13.
"""

from __future__ import annotations


def chi(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(a for a in range(2, p) if chi(a, p) == -1)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add_poly(f: list[int], g: list[int], p: int) -> list[int]:
    size = max(len(f), len(g))
    out = [0] * size
    for i in range(size):
        out[i] = (
            (f[i] if i < len(f) else 0)
            + (g[i] if i < len(g) else 0)
        ) % p
    return trim(out)


def mul_mod(
    f: list[int], g: list[int], modulus: list[int], p: int
) -> list[int]:
    out = [0] * (len(f) + len(g) - 1)
    for i, fi in enumerate(f):
        for j, gj in enumerate(g):
            out[i + j] = (out[i + j] + fi * gj) % p

    degree = len(modulus) - 1
    for k in range(len(out) - 1, degree - 1, -1):
        coefficient = out[k] % p
        if coefficient == 0:
            continue
        for j in range(degree):
            out[k - degree + j] = (
                out[k - degree + j] - coefficient * modulus[j]
            ) % p

    reduced = out[:degree]
    reduced += [0] * (degree - len(reduced))
    return reduced


def pow_mod(
    base: list[int], exponent: int, modulus: list[int], p: int
) -> list[int]:
    result = [1]
    while exponent:
        if exponent & 1:
            result = mul_mod(result, base, modulus, p)
        base = mul_mod(base, base, modulus, p)
        exponent >>= 1
    return trim(result)


def divmod_poly(
    dividend: list[int], divisor: list[int], p: int
) -> tuple[list[int], list[int]]:
    dividend = trim([value % p for value in dividend])
    divisor = trim([value % p for value in divisor])
    if divisor == [0]:
        raise ZeroDivisionError

    if len(dividend) < len(divisor):
        return [0], dividend

    quotient = [0] * (len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, p)

    while dividend != [0] and len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        coefficient = dividend[-1] * inverse % p
        quotient[shift] = coefficient
        for j, value in enumerate(divisor):
            dividend[shift + j] = (
                dividend[shift + j] - coefficient * value
            ) % p
        trim(dividend)

    return trim(quotient), trim(dividend)


def gcd_poly(f: list[int], g: list[int], p: int) -> list[int]:
    f = trim(f[:])
    g = trim(g[:])
    while g != [0]:
        _, remainder = divmod_poly(f, g, p)
        f, g = g, remainder
    inverse = pow(f[-1], -1, p)
    return [(value * inverse) % p for value in f]


def determinant_mod(matrix: list[list[int]], p: int) -> int:
    matrix = [[value % p for value in row] for row in matrix]
    size = len(matrix)
    determinant = 1

    for column in range(size):
        pivot = next(
            (
                row
                for row in range(column, size)
                if matrix[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            return 0

        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            determinant = -determinant

        pivot_value = matrix[column][column]
        determinant = determinant * pivot_value % p
        inverse = pow(pivot_value, -1, p)

        for row in range(column + 1, size):
            factor = matrix[row][column] * inverse % p
            if factor == 0:
                continue
            for j in range(column, size):
                matrix[row][j] = (
                    matrix[row][j] - factor * matrix[column][j]
                ) % p

    return determinant % p


def modulus_polynomial(p: int, a: int, c: int, d: int) -> list[int]:
    # Low-to-high coefficients of X^p + aX^3 + cX + d.
    return [d % p, c % p, 0, a % p] + [0] * (p - 4) + [1]


def frobenius_matrix(p: int, a: int, c: int, d: int) -> list[list[int]]:
    modulus = modulus_polynomial(p, a, c, d)
    cubic = [(-d) % p, (-c) % p, 0, (-a) % p] + [0] * (p - 4)

    columns: list[list[int]] = []
    current = [1] + [0] * (p - 1)

    for power in range(p):
        if power == 0:
            column = current[:]
        elif power == 1:
            current = cubic[:]
            column = current[:]
        else:
            current = mul_mod(current, cubic, modulus, p)
            column = current[:]
        columns.append(column)

    return [
        [
            (columns[column][row] - int(row == column)) % p
            for column in range(p)
        ]
        for row in range(p)
    ]


def reduced_determinant(p: int, a: int, c: int, d: int) -> int:
    matrix = frobenius_matrix(p, a, c, d)
    deleted_row = p - 3
    minor = [
        [matrix[row][column] for column in range(1, p)]
        for row in range(p)
        if row != deleted_row
    ]
    return determinant_mod(minor, p)


def is_irreducible(p: int, a: int, c: int, d: int) -> bool:
    modulus = modulus_polynomial(p, a, c, d)
    x_poly = [0, 1]

    # For prime degree p, all factor degrees divide p iff X^(p^p) = X mod F.
    final_frobenius = pow_mod(x_poly, p**p, modulus, p)
    difference = add_poly(final_frobenius, [0, -1], p)
    if difference != [0]:
        return False

    # The only proper divisor degree of p is 1.
    first_frobenius = pow_mod(x_poly, p, modulus, p)
    linear_test = add_poly(first_frobenius, [0, -1], p)
    return len(gcd_poly(modulus, linear_test, p)) == 1


def verify() -> None:
    expected_counts = {
        5: (4, 6),
        7: (10, 8),
        11: (14, 14),
        13: (10, 6),
    }

    for p in (5, 7, 11, 13):
        classes = (1, least_nonsquare(p))
        observed: list[int] = []

        for a in classes:
            determinant_nonzero = 0
            irreducible_count = 0

            for c in range(p):
                for d in range(p):
                    determinant_test = reduced_determinant(p, a, c, d) != 0
                    irreducible_test = is_irreducible(p, a, c, d)
                    assert determinant_test == irreducible_test, (
                        p,
                        a,
                        c,
                        d,
                        determinant_test,
                        irreducible_test,
                    )
                    determinant_nonzero += int(determinant_test)
                    irreducible_count += int(irreducible_test)

            assert determinant_nonzero == irreducible_count
            observed.append(irreducible_count)

        assert tuple(observed) == expected_counts[p], (p, observed)
        print(f"PASS p={p}: counts={tuple(observed)}")

    print("ALL REDUCED FROBENIUS DETERMINANT CHECKS PASSED")


if __name__ == "__main__":
    verify()
