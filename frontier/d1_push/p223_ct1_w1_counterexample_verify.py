#!/usr/bin/env python3
"""Independent exact verification of the p=223 CT1-w1 counterexample.

The witness was found by the randomized complementary-minor search. This
script does not reuse that search code. It verifies the two small complementary
minors and, independently, the original 213x213 Cauchy-Binet determinant
product over F_223.
"""
from __future__ import annotations

import json
from math import comb, factorial
from pathlib import Path

P = 223
E = [5, 7, 8, 12, 13, 14, 16, 17, 18]
R = [49, 71, 94, 119, 122, 126, 130, 141, 148, 220]


def inv(x: int) -> int:
    return pow(x % P, P - 2, P)


def det_mod(matrix: list[list[int]]) -> int:
    a = [[x % P for x in row] for row in matrix]
    n = len(a)
    out = 1
    for c in range(n):
        pivot = next((r for r in range(c, n) if a[r][c]), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            out = -out % P
        pv = a[c][c]
        out = out * pv % P
        ipv = inv(pv)
        for r in range(c + 1, n):
            if not a[r][c]:
                continue
            factor = a[r][c] * ipv % P
            row_r = a[r]
            row_c = a[c]
            for j in range(c, n):
                row_r[j] = (row_r[j] - factor * row_c[j]) % P
    return out


def falling(n: int, m: int) -> int:
    if m > n:
        return 0
    out = 1
    for j in range(m):
        out = out * (n - j) % P
    return out


def pinv_entry(r: int, s: int) -> int:
    if r < s:
        return 0
    value = inv(factorial(s) * factorial(r - s))
    return -value % P if (r - s) & 1 else value


def u_entry(r: int, s: int) -> int:
    if s == 0:
        return int(r == 0)
    if r < s or (r - s) & 1:
        return 0
    h = (r - s) // 2
    value = s * inv(r) % P
    value = value * (comb(r + h - 1, h) % P) % P
    return -value % P if h & 1 else value


def b_entry(q: int, m: int) -> int:
    # 1/m! [X^q](X+X^3)^m.
    if q < m or q > 3 * m or (q - m) & 1:
        return 0
    j = (q - m) // 2
    return inv(factorial(j) * factorial(m - j))


def main() -> None:
    omega = list(range(P))
    n_rows = [x for x in range(1, P) if x not in E]
    q_rows = sorted((set(n_rows) - {P - 3}) | {0})
    m_cols = sorted(set(omega) - set(R))
    c0 = sorted(E + [0])
    c1 = sorted(E + [P - 3])

    det_pinv = det_mod([[pinv_entry(r, s) for s in c0] for r in R])
    det_u = det_mod([[u_entry(r, s) for s in c1] for r in R])

    det_p_large = det_mod([[falling(n, m) for m in m_cols] for n in n_rows])
    det_b_large = det_mod([[b_entry(q, m) for m in m_cols] for q in q_rows])

    factorial_complement = 1
    for r in R:
        factorial_complement = factorial_complement * (factorial(r) % P) % P

    epsilon = -1 if (sum(n_rows) + sum(q_rows)) & 1 else 1
    complementary_product = (
        epsilon * factorial_complement * det_pinv * det_u
    ) % P
    direct_product = det_p_large * det_b_large % P

    sum_e = sum(E)
    sum_r = sum(R)
    gamma = 2 * (sum_e + 1) // (P - 1)
    beta = (sum_r - sum_e) // (P - 1)
    alpha = (P + 1 - 3 * beta - gamma) // 2
    cubic_degree = (sum_r - sum_e - (P - 3)) // 2
    c_degree = alpha * (P - 1)
    d_degree = beta * (P - 1)
    weight = c_degree + 2 * d_degree
    old_boundary = (P * P - 1) // 2
    corrected_boundary = (P - 1) * (P + 3) // 2

    result = {
        "status": "PASS",
        "prime": P,
        "E": E,
        "R": R,
        "sum_E": sum_e,
        "sum_R": sum_r,
        "gamma": gamma,
        "beta": beta,
        "alpha": alpha,
        "a_degree": cubic_degree,
        "c_degree": c_degree,
        "d_degree": d_degree,
        "weight": weight,
        "old_boundary": old_boundary,
        "corrected_one_level_boundary": corrected_boundary,
        "excess_over_corrected_boundary": weight - corrected_boundary,
        "det_P_inverse_small": det_pinv,
        "det_U_small": det_u,
        "factorial_complement": factorial_complement,
        "jacobi_sign": epsilon,
        "complementary_product": complementary_product,
        "det_P_large": det_p_large,
        "det_B_large": det_b_large,
        "direct_product": direct_product,
        "large_matrix_size": len(m_cols),
        "identity": direct_product == complementary_product != 0,
    }
    assert det_pinv == 86
    assert det_u == 169
    assert beta == gamma + 4
    assert weight == corrected_boundary + (P - 1)
    assert direct_product == complementary_product != 0

    output = Path(__file__).with_name(
        "p223_ct1_w1_counterexample_verify_results.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
