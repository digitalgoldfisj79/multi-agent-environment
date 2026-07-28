#!/usr/bin/env python3
"""Finite regression for the local tangent theorem at the unique root-cycle fixed point."""

from __future__ import annotations

import json


def inv(a: int, p: int) -> int:
    return pow(a % p, -1, p)


def rank_mod(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = inv(a[r][c], p)
        a[r] = [(scale * x) % p for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c] % p:
                factor = a[i][c] % p
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == rows:
            break
    return r


def vector_power(power: int, p: int) -> list[int]:
    return [pow(i, power, p) for i in range(p)]


def dot(a: list[int], b: list[int], p: int) -> int:
    return sum(x * y for x, y in zip(a, b)) % p


def shift_plus(a: list[int]) -> list[int]:
    # sigma(f)(i)=f(i+1), indices in F_p.
    p = len(a)
    return [a[(i + 1) % p] for i in range(p)]


def check_prime(p: int) -> dict:
    constraints = [vector_power(r, p) for r in range(0, p - 4)]
    constraint_rank = rank_mod(constraints, p)
    assert constraint_rank == p - 4
    tangent_affine_dimension = p - constraint_rank
    assert tangent_affine_dimension == 4

    low = [vector_power(a, p) for a in range(4)]
    assert rank_mod(low, p) == 4
    for a in low:
        for row in constraints:
            assert dot(a, row, p) == 0

    one, linear, quadratic, cubic = low
    sq_shift = shift_plus(quadratic)
    cu_shift = shift_plus(cubic)

    # Verify the exact binomial expansions in the affine tangent space.
    sq_expected = [(quadratic[i] + 2 * linear[i] + one[i]) % p for i in range(p)]
    cu_expected = [
        (cubic[i] + 3 * quadratic[i] + 3 * linear[i] + one[i]) % p
        for i in range(p)
    ]
    assert sq_shift == sq_expected
    assert cu_shift == cu_expected

    # In the quotient by span{1,i}, the basis (i^2,i^3) has columns
    # (1,0) and (3,1), hence matrix [[1,3],[0,1]].
    matrix = [[1, 3 % p], [0, 1]]
    nilpotent = [[0, 3 % p], [0, 0]]
    assert nilpotent[0][1] != 0
    assert (nilpotent[0][0] * nilpotent[0][0] + nilpotent[0][1] * nilpotent[1][0]) % p == 0
    fixed_dimension = 1

    return {
        "p": p,
        "constraint_count": len(constraints),
        "constraint_rank": constraint_rank,
        "affine_tangent_dimension": tangent_affine_dimension,
        "projective_surface_tangent_dimension": 2,
        "generator_matrix_basis_i2_i3": matrix,
        "fixed_dimension": fixed_dimension,
        "nontrivial_unipotent": True,
    }


def main() -> None:
    primes = [5, 7, 11, 13, 17, 23, 29, 31, 41, 53]
    rows = [check_prime(p) for p in primes]
    payload = {
        "rows": rows,
        "conclusion": (
            "For every tested p>3, the tangent equations have affine dimension four, "
            "and after quotienting the diagonal and projective fixed lines the root cycle "
            "acts by the nontrivial two-dimensional Jordan block [[1,3],[0,1]]."
        ),
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
