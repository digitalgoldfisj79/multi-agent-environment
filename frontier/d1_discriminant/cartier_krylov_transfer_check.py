#!/usr/bin/env python3
"""Verify the Cartier--Krylov--Frobenius similarity.

This is a standard-library verifier.  It checks, for small primes and all
coefficient triples in the requested ranges, that

    H = G^{-1} Q G,

where H is the full Cartier matrix, Q is Frobenius on F_p[X]/(F) in the
signed power basis, and G is the sparse residue-pairing Gram matrix.
"""

from __future__ import annotations

from itertools import product


def matmul(a: list[list[int]], b: list[list[int]], p: int) -> list[list[int]]:
    n, m, r = len(a), len(b), len(b[0])
    out = [[0] * r for _ in range(n)]
    for i in range(n):
        for k in range(m):
            aik = a[i][k] % p
            if aik:
                for j in range(r):
                    out[i][j] = (out[i][j] + aik * b[k][j]) % p
    return out


def inverse(a: list[list[int]], p: int) -> list[list[int]]:
    n = len(a)
    aug = [
        [x % p for x in row] + [int(i == j) for j in range(n)]
        for i, row in enumerate(a)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] % p), None)
        if pivot is None:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        inv = pow(aug[col][col], -1, p)
        aug[col] = [(x * inv) % p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col] % p
            if factor:
                aug[r] = [
                    (aug[r][j] - factor * aug[col][j]) % p
                    for j in range(2 * n)
                ]
    return [row[n:] for row in aug]


def determinant(a: list[list[int]], p: int) -> int:
    m = [[x % p for x in row] for row in a]
    n = len(m)
    det = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col] % p), None)
        if pivot is None:
            return 0
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            det = -det
        value = m[col][col] % p
        det = det * value % p
        inv = pow(value, -1, p)
        for r in range(col + 1, n):
            factor = m[r][col] * inv % p
            if factor:
                for j in range(col, n):
                    m[r][j] = (m[r][j] - factor * m[col][j]) % p
    return det % p


def polynomial_power(base: list[int], exponent: int, p: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        nxt = [0] * (len(out) + len(base) - 1)
        for i, x in enumerate(out):
            if x:
                for j, y in enumerate(base):
                    if y:
                        nxt[i + j] = (nxt[i + j] + x * y) % p
        out = nxt
    return out


def cartier_matrix(p: int, a: int, c: int, d: int) -> list[list[int]]:
    f = [d % p, c % p, 0, a % p] + [0] * (p - 4) + [1]
    power = polynomial_power(f, p - 1, p)
    h = []
    for u in range(1, p + 1):
        row = []
        for v in range(1, p + 1):
            index = p * u - v
            row.append(power[index] % p if 0 <= index < len(power) else 0)
        h.append(row)
    return h


def multiply_by_x(vec: list[int], p: int, a: int, c: int, d: int) -> list[int]:
    """Multiply a degree < p representative by X modulo F."""
    out = [0] * p
    for i, value in enumerate(vec):
        if not value:
            continue
        if i + 1 < p:
            out[i + 1] = (out[i + 1] + value) % p
        else:
            out[3] = (out[3] - a * value) % p
            out[1] = (out[1] - c * value) % p
            out[0] = (out[0] - d * value) % p
    return out


def x_power_remainder(n: int, p: int, a: int, c: int, d: int) -> list[int]:
    out = [1] + [0] * (p - 1)
    for _ in range(n):
        out = multiply_by_x(out, p, a, c, d)
    return out


def gram_matrix(p: int, a: int, c: int, d: int) -> list[list[int]]:
    """G_(m,v)=ell((-X)^m X^(v-1)); d cancels identically."""
    g = []
    for m in range(p):
        sign = -1 if m % 2 else 1
        row = []
        for v in range(1, p + 1):
            coeff = x_power_remainder(m + v - 1, p, a, c, d)[p - 1]
            row.append(sign * coeff % p)
        g.append(row)
    return g


def explicit_gram(p: int, a: int, c: int) -> list[list[int]]:
    g = [[0] * p for _ in range(p)]
    for m in range(p):
        sign = -1 if m % 2 else 1
        for v in range(1, p + 1):
            value = 0
            if m + v == p:
                value += 1
            if m + v == 2 * p - 3:
                value -= a
            if m + v == 2 * p - 1:
                value -= c
            g[m][v - 1] = sign * value % p
    return g


def frobenius_matrix(p: int, a: int, c: int, d: int) -> list[list[int]]:
    """Row-action matrix of Frobenius in e_m=(-1)^m X^m."""
    q = []
    for m in range(p):
        remainder = x_power_remainder(p * m, p, a, c, d)
        row = []
        for n, coeff in enumerate(remainder):
            sign = -1 if (m - n) % 2 else 1
            row.append(sign * coeff % p)
        q.append(row)
    return q


def check_case(p: int, a: int, c: int, d: int) -> None:
    h = cartier_matrix(p, a, c, d)
    g = gram_matrix(p, a, c, d)
    g_explicit = explicit_gram(p, a, c)
    q = frobenius_matrix(p, a, c, d)

    assert g == g_explicit, (p, a, c, d, "Gram formula")
    assert determinant(g, p) == 1, (p, a, c, d, "det G")
    rhs = matmul(matmul(inverse(g, p), q, p), g, p)
    assert h == rhs, (p, a, c, d, "H=G^-1 Q G")


def verify() -> None:
    # Exhaustive at p=5,7 and a representative grid at p=11.
    for p in (5, 7):
        for a, c, d in product(range(1, p), range(p), range(p)):
            check_case(p, a, c, d)
        print(f"PASS exhaustive p={p}")

    p = 11
    for a in (1, 2, 5, 10):
        for c in (0, 1, 3, 7, 10):
            for d in (0, 1, 4, 9, 10):
                check_case(p, a, c, d)
    print("PASS grid p=11")
    print("ALL CARTIER--KRYLOV TRANSFER CHECKS PASSED")


if __name__ == "__main__":
    verify()
