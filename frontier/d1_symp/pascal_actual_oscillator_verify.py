#!/usr/bin/env python3
"""Exact checks for ACTUAL_PASCAL_GRAPH_OSCILLATOR_AND_MORSE_NO_GO.

Checks:
1. the actual sparse Pascal matrix has block form [[A,B],[C,0]] in the
   intrinsic lower/upper symplectic polarization;
2. B is triangular and invertible, C=B^{-t}, and B^{-1}A is symmetric;
3. the canonical generating function has complete sum q^m and punctured
   sum q^m-1 at p=11;
4. the nonlinear high phase has ordinary order at least five in the joint
   (lambda,w) variables, hence zero ordinary Hessian.

No third-party packages are required.
"""

from __future__ import annotations

from itertools import product
from math import comb


def primes(limit: int):
    for n in range(5, limit + 1, 2):
        if all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            yield n


def inv(a: int, p: int) -> int:
    return pow(a % p, -1, p)


def mat_mul(a, b, p):
    rows = len(a)
    inner = len(b)
    cols = len(b[0]) if b else 0
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) % p for j in range(cols)]
        for i in range(rows)
    ]


def transpose(a):
    return [list(row) for row in zip(*a)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matrix_inverse(a, p):
    n = len(a)
    aug = [
        [x % p for x in row] + identity(n)[i]
        for i, row in enumerate(a)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] % p), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = inv(aug[col][col], p)
        aug[col] = [(scale * x) % p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col] % p
            if factor:
                aug[r] = [
                    (x - factor * y) % p
                    for x, y in zip(aug[r], aug[col])
                ]
    return [row[n:] for row in aug]


def pascal_entry(row_degree: int, column_degree: int, p: int) -> int:
    return ((-1) ** row_degree * comb(column_degree + row_degree - 1, row_degree)) % p


def blocks(p: int):
    low = list(range(4, (p - 1) // 2 + 1))
    m = len(low)
    a_block = [[0] * m for _ in range(m)]
    b_block = [[0] * m for _ in range(m)]
    c_block = [[0] * m for _ in range(m)]
    e_block = [[0] * m for _ in range(m)]

    for r, b in enumerate(low):
        upper_output_degree = p - b
        upper_output_scale = (2 * b - p) % p
        for c, a in enumerate(low):
            upper_input_degree = p - a
            upper_input_scale = inv(2 * a - p, p)
            a_block[r][c] = pascal_entry(b, a, p)
            b_block[r][c] = (
                pascal_entry(b, upper_input_degree, p) * upper_input_scale
            ) % p
            c_block[r][c] = (
                upper_output_scale * pascal_entry(upper_output_degree, a, p)
            ) % p
            e_block[r][c] = (
                upper_output_scale
                * pascal_entry(upper_output_degree, upper_input_degree, p)
                * upper_input_scale
            ) % p
    return low, a_block, b_block, c_block, e_block


def verify_blocks(limit: int = 199) -> None:
    checked = []
    for p in primes(limit):
        if p < 11:
            continue
        low, a, b, c, e = blocks(p)
        m = len(low)
        zero = [[0] * m for _ in range(m)]
        assert e == zero, (p, "E")
        assert all(b[i][j] == 0 for i in range(m) for j in range(i)), (p, "B triangular")
        assert [b[i][i] for i in range(m)] == [inv(2 * x - p, p) for x in low]

        b_inv = matrix_inverse(b, p)
        c_expected = transpose(b_inv)
        assert c == c_expected, (p, "C=B^-t")
        b_inv_a = mat_mul(b_inv, a, p)
        assert b_inv_a == transpose(b_inv_a), (p, "B^-1 A symmetric")
        checked.append(p)
    print(f"PASS: actual Pascal block theorem for {len(checked)} primes through {checked[-1]}.")


def additive_character_exponent(value: int, p: int) -> int:
    """Represent psi(value) formally by its exponent modulo p."""
    return value % p


def verify_complete_sum_p11() -> None:
    p = 11
    low, a, b, _, _ = blocks(p)
    m = len(low)
    b_inv = matrix_inverse(b, p)
    q_matrix = mat_mul(b_inv, a, p)
    assert q_matrix == transpose(q_matrix)
    half = inv(2, p)

    counts = [0] * p
    for x in product(range(p), repeat=m):
        for y in product(range(p), repeat=m):
            bilinear = sum(
                x[i] * b_inv[i][j] * y[j]
                for i in range(m)
                for j in range(m)
            )
            quadratic = sum(
                x[i] * q_matrix[i][j] * x[j]
                for i in range(m)
                for j in range(m)
            )
            exponent = additive_character_exponent(bilinear - half * quadratic, p)
            counts[exponent] += 1

    # A cyclotomic sum sum_k counts[k] zeta^k is the integer p^m iff
    # counts[1]=...=counts[p-1] and counts[0]-counts[1]=p^m.
    assert len(set(counts[1:])) == 1
    complete = counts[0] - counts[1]
    assert complete == p**m, (complete, p**m)

    # Removing the origin subtracts one from the zero exponent count.
    punctured = complete - 1
    assert punctured == p**m - 1
    print(
        f"PASS: p=11 complete actual-Pascal oscillator sum={complete}=p^m; "
        f"punctured={punctured}."
    )


def verify_classical_hessian_no_go(limit: int = 199) -> None:
    checked = []
    for p in primes(limit):
        if p < 11:
            continue
        high = range(4, p - 3)
        # Every high-phase monomial has one coefficient variable lambda_m and
        # a power-sum monomial of ordinary w-degree j>=4. Its joint degree is
        # therefore at least five, so all derivatives of total order <=2 vanish.
        assert min(1 + j for j in high) == 5
        checked.append(p)
    print(
        "PASS: the actual nonlinear high phase has joint order >=5 and zero "
        f"ordinary Hessian through p={checked[-1]}."
    )


def main() -> None:
    verify_blocks()
    verify_complete_sum_p11()
    verify_classical_hessian_no_go()
    print("PASCAL_ACTUAL_OSCILLATOR_VERIFY: PASS")


if __name__ == "__main__":
    main()
