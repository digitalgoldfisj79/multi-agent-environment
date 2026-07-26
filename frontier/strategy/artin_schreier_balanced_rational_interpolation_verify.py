#!/usr/bin/env python3
"""Regression for universal balanced rational interpolation in F_p[Z]/(Z^p-Z-1).

For m=(p-1)/2 and any beta, the m high-coefficient constraints on a
denominator B of degree <=m form an m by (m+1) homogeneous system.  A
nonzero B exists, and A=beta*B has degree <=m.  Since the quotient is a
field, B is invertible.

The script constructs such A,B for deterministic coefficient vectors at
small primes and verifies beta=A/B.  It is a structural regression, not an
irreducibility census.
"""
from __future__ import annotations

import json
from pathlib import Path


def trim(a: list[int], p: int) -> list[int]:
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out, p)


def reduce_as(a: list[int], p: int) -> list[int]:
    a = a[:] + [0]
    for degree in range(len(a) - 1, p - 1, -1):
        value = a[degree] % p
        if value:
            a[degree] = 0
            a[degree - p] = (a[degree - p] + value) % p
            a[degree - p + 1] = (a[degree - p + 1] + value) % p
    return trim(a[:p], p)


def null_vector(matrix: list[list[int]], p: int) -> list[int] | None:
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 1
    a = [[x % p for x in row] for row in matrix]
    rank = 0
    pivots: list[int] = []
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(inv * x) % p for x in a[rank]]
        for row in range(rows):
            if row != rank and a[row][col]:
                factor = a[row][col]
                a[row] = [
                    (a[row][j] - factor * a[rank][j]) % p
                    for j in range(cols)
                ]
        pivots.append(col)
        rank += 1
    if rank == cols:
        return None
    free = next(col for col in range(cols) if col not in pivots)
    vector = [0] * cols
    vector[free] = 1
    for row in range(rank - 1, -1, -1):
        col = pivots[row]
        vector[col] = -sum(a[row][j] * vector[j] for j in range(col + 1, cols)) % p
    return vector


def deterministic_beta(p: int, seed: int) -> list[int]:
    value = seed
    out = []
    for index in range(p):
        value = (value * (index + 7) + 3 * seed + 11 * index + 5) % p
        out.append(value)
    if not any(out):
        out[0] = 1
    return out


def balanced_representation(beta: list[int], p: int) -> tuple[list[int], list[int]]:
    m = (p - 1) // 2
    columns = []
    for power in range(m + 1):
        product = reduce_as(mul(beta, [0] * power + [1], p), p)
        columns.append(product + [0] * (p - len(product)))
    matrix = [
        [columns[col][degree] for col in range(m + 1)]
        for degree in range(m + 1, p)
    ]
    denominator = null_vector(matrix, p)
    assert denominator is not None and any(denominator)
    numerator = reduce_as(mul(beta, denominator, p), p)
    assert len(numerator) - 1 <= m
    assert len(trim(denominator, p)) - 1 <= m
    return numerator, trim(denominator, p)


def main() -> None:
    rows = []
    for p in (5, 7, 11, 13, 17, 19, 23, 29):
        m = (p - 1) // 2
        cases = []
        for seed in range(1, 6):
            beta = deterministic_beta(p, seed)
            numerator, denominator = balanced_representation(beta, p)
            assert reduce_as(mul(beta, denominator, p), p) == numerator
            cases.append({
                "seed": seed,
                "numerator_degree": len(numerator) - 1,
                "denominator_degree": len(denominator) - 1,
            })
        rows.append({"p": p, "m": m, "cases": cases})

    output = {
        "classification": "linear-algebra structural regression; no irreducibility census",
        "rows": rows,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "artin_schreier_balanced_rational_interpolation_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print("ARTIN_SCHREIER_BALANCED_RATIONAL_INTERPOLATION_VERIFY: PASS")


if __name__ == "__main__":
    main()
