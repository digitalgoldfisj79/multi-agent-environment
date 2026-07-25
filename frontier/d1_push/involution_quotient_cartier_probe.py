#!/usr/bin/env python3
"""Exact Cartier-cofactor probe for the involution quotient family.

For p=2n+1 and a != 0, the quotient family is

    G(Y)=Y(Y^n+aY+c)^2-e.

The general Cartier cofactor theorem gives

    C_3(G)=3 a^2 * 1_{G irreducible}  (mod p).

This script builds the selected cofactor as a polynomial in (c,e), sums it
over c in F_p and e in the nonzero square subgroup, and compares the result
with direct irreducibility counting.  It is intended for focused structural
experiments at small p; the subset-DP determinant is exponential in p.
"""
from __future__ import annotations

import argparse
from math import factorial

import numpy as np
from flint import nmod_poly


def poly_add(left: np.ndarray, right: np.ndarray, p: int) -> np.ndarray:
    rows = max(left.shape[0], right.shape[0])
    cols = max(left.shape[1], right.shape[1])
    out = np.zeros((rows, cols), dtype=np.int64)
    out[: left.shape[0], : left.shape[1]] += left
    out[: right.shape[0], : right.shape[1]] += right
    return out % p


def poly_multiply(left: np.ndarray, right: np.ndarray, p: int) -> np.ndarray:
    out = np.zeros(
        (left.shape[0] + right.shape[0] - 1,
         left.shape[1] + right.shape[1] - 1),
        dtype=np.int64,
    )
    left_rows, left_cols = np.nonzero(left)
    right_rows, right_cols = np.nonzero(right)
    if len(left_rows) > len(right_rows):
        left, right = right, left
        left_rows, left_cols = right_rows, right_cols
    for row, col in zip(left_rows, left_cols):
        out[
            row : row + right.shape[0],
            col : col + right.shape[1],
        ] += int(left[row, col]) * right
        out %= p
    return out % p


def entry_dictionary(p: int, u: int, v: int, a: int) -> dict[tuple[int, int], int]:
    """Return H_(u,v) as a sparse polynomial in c and e.

    The six nonleading terms have coefficient/exponent data

      2a Y^(n+2), 2c Y^(n+1), a^2 Y^3,
      2ac Y^2, c^2 Y, -e.

    If their occupation numbers are (i,j,k,l,r,s), coefficient extraction
    reduces to the displayed weighted equation in the accompanying note.
    """
    n = (p - 1) // 2
    target = p * (p - 1 - u) + v
    weights = (n - 1, n, p - 3, p - 2, p - 1, p)
    values = [0] * 6
    facts = [factorial(index) for index in range(p)]
    out: dict[tuple[int, int], int] = {}

    def recurse(position: int, remainder: int, total: int) -> None:
        if position == 6:
            if remainder != 0:
                return
            i, j, k, ell, r, s = values
            multinomial = facts[total]
            for value in values:
                multinomial //= facts[value]
            coefficient = multinomial * (-1 if total % 2 else 1)
            coefficient *= pow(2 * a, i, p)
            coefficient *= pow(2, j, p)
            coefficient *= pow(a * a, k, p)
            coefficient *= pow(2 * a, ell, p)
            if s % 2:
                coefficient = -coefficient
            c_degree = j + ell + 2 * r
            e_degree = s
            key = (c_degree, e_degree)
            out[key] = (out.get(key, 0) + coefficient) % p
            return

        weight = weights[position]
        maximum = min(p - 1 - total, remainder // weight)
        for value in range(maximum + 1):
            values[position] = value
            recurse(position + 1, remainder - value * weight, total + value)
        values[position] = 0

    recurse(0, target, 0)
    return {key: value for key, value in out.items() if value % p}


def dictionary_to_array(data: dict[tuple[int, int], int], p: int) -> np.ndarray:
    if not data:
        return np.zeros((1, 1), dtype=np.int64)
    out = np.zeros(
        (max(key[0] for key in data) + 1,
         max(key[1] for key in data) + 1),
        dtype=np.int64,
    )
    for (row, col), value in data.items():
        out[row, col] = value % p
    return out


def determinant_polynomial(matrix: list[list[np.ndarray]], p: int) -> np.ndarray:
    """Subset-DP determinant of a matrix of bivariate polynomials."""
    size = len(matrix)
    states: dict[int, np.ndarray] = {0: np.array([[1]], dtype=np.int64)}
    for row in range(size):
        next_states: dict[int, np.ndarray] = {}
        for mask, polynomial in states.items():
            for col in range(size):
                if mask & (1 << col):
                    continue
                position = (mask & ((1 << col) - 1)).bit_count()
                term = poly_multiply(polynomial, matrix[row][col], p)
                if (row + position) % 2:
                    term = (-term) % p
                new_mask = mask | (1 << col)
                if new_mask in next_states:
                    next_states[new_mask] = poly_add(next_states[new_mask], term, p)
                else:
                    next_states[new_mask] = term
        states = next_states
    return states[(1 << size) - 1]


def is_irreducible(polynomial: nmod_poly, p: int) -> bool:
    _, factors = polynomial.factor()
    return (
        len(factors) == 1
        and factors[0][1] == 1
        and factors[0][0].degree() == p
    )


def quotient_polynomial(p: int, a: int, c: int, e: int) -> nmod_poly:
    n = (p - 1) // 2
    coefficients = [(-e) % p, c * c % p, 2 * a * c % p, a * a % p]
    coefficients += [0] * (p + 1 - len(coefficients))
    coefficients[n + 1] = (coefficients[n + 1] + 2 * c) % p
    coefficients[n + 2] = (coefficients[n + 2] + 2 * a) % p
    coefficients[p] = 1
    return nmod_poly(coefficients, p)


def direct_counts(p: int, a: int) -> tuple[int, int]:
    squares = {value * value % p for value in range(1, p)}
    square_count = 0
    nonsquare_count = 0
    for c in range(p):
        for e in range(1, p):
            if is_irreducible(quotient_polynomial(p, a, c, e), p):
                if e in squares:
                    square_count += 1
                else:
                    nonsquare_count += 1
    return square_count, nonsquare_count


def run(p: int, a: int) -> None:
    if p < 5 or p % 2 == 0:
        raise ValueError("p must be an odd prime at least 5")
    a %= p
    if a == 0:
        raise ValueError("a must be nonzero")

    columns = [v for v in range(1, p + 1) if v != 3]
    matrix: list[list[np.ndarray]] = []
    for u in range(1, p):
        row: list[np.ndarray] = []
        for v in columns:
            entry = (-dictionary_to_array(entry_dictionary(p, u, v, a), p)) % p
            if u == v:
                entry[0, 0] = (entry[0, 0] + 1) % p
            row.append(entry)
        matrix.append(row)

    determinant = determinant_polynomial(matrix, p)
    nonzero = np.nonzero(determinant)
    c_degree = int(max(nonzero[0]))
    e_degree = int(max(nonzero[1]))
    subgroup_order = (p - 1) // 2

    square_survivors: list[tuple[int, int, int]] = []
    quadratic_survivors: list[tuple[int, int, int]] = []
    coefficient_sum = 0
    for c_exp in range(p - 1, c_degree + 1, p - 1):
        for e_exp in range(0, e_degree + 1, subgroup_order):
            if c_exp >= determinant.shape[0] or e_exp >= determinant.shape[1]:
                continue
            value = int(determinant[c_exp, e_exp]) % p
            if value:
                square_survivors.append((c_exp, e_exp, value))
                coefficient_sum = (coefficient_sum + value) % p
                if e_exp % (p - 1) != 0:
                    quadratic_survivors.append((c_exp, e_exp, value))

    # Sum_c c^K=-1 for positive K divisible by p-1.
    # Sum_{e in QR*} e^L=(p-1)/2 for L divisible by (p-1)/2.
    certificate = (-subgroup_order * coefficient_sum) % p
    square_count, nonsquare_count = direct_counts(p, a)
    target = (3 * a * a * square_count) % p

    print(
        f"p={p} a={a} degree=({c_degree},{e_degree}) "
        f"monomials={len(nonzero[0])} square_survivors={len(square_survivors)}"
    )
    print(f"square_survivors={square_survivors}")
    print(f"quadratic_e_survivors={quadratic_survivors}")
    print(
        f"irreducible_counts(square,nonsquare)=({square_count},{nonsquare_count}) "
        f"certificate={certificate} target={target} "
        f"check={'PASS' if certificate == target else 'FAIL'}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("a", type=int, nargs="?", default=1)
    arguments = parser.parse_args()
    run(arguments.p, arguments.a)
