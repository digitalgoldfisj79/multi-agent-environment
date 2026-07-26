#!/usr/bin/env python3
"""Exact endpoint regression for degree (p+1)/2 polynomial semiconjugacy.

After leading normalization, input translation, and the second Newton trace,
write R(Z)=Z^n S(1/Z), where S=1+s3*T^3+...+sn*T^n and n=(p+1)/2.
The high coefficient ledger forces

  [T^j]S^3=0       for n+2 <= j <= 2n-3,
  [T^(2n-2)]S^3=-1,
  [T^(2n-1)]S^3=-1.

The remaining semiconjugacy equations force 8*s4+3*s3=0.  This script
exhausts the cube-gap solutions at p=11 and p=17 and proves that none
satisfies the final constraint.  It performs no irreducibility census.
"""
from __future__ import annotations

import json
from itertools import product
from pathlib import Path


def cube_coeff(s: tuple[int, ...], degree: int, p: int) -> int:
    n = len(s) - 1
    total = 0
    for i in range(max(0, degree - 2 * n), min(n, degree) + 1):
        for j in range(max(0, degree - i - n), min(n, degree - i) + 1):
            k = degree - i - j
            if 0 <= k <= n:
                total = (total + s[i] * s[j] * s[k]) % p
    return total


def candidate_record(p: int, values: tuple[int, ...]) -> dict[str, object]:
    n = (p + 1) // 2
    s = (1, 0, 0) + values
    assert len(s) == n + 1
    assert all(cube_coeff(s, j, p) == 0 for j in range(n + 2, 2 * n - 2))
    assert cube_coeff(s, 2 * n - 2, p) == p - 1
    assert cube_coeff(s, 2 * n - 1, p) == p - 1

    ratio_residual = (8 * s[4] + 3 * s[3]) % p
    assert ratio_residual != 0

    # W=3 P S'-P'S, P the truncation of S^3 through degree n+1.
    cube = [cube_coeff(s, j, p) for j in range(3 * n + 1)]
    P = cube[: n + 2]
    S_prime = [(j * s[j]) % p for j in range(1, n + 1)]
    P_prime = [(j * P[j]) % p for j in range(1, n + 2)]

    def mul(a: list[int], b: list[int]) -> list[int]:
        out = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
        return out

    left = mul(P, S_prime)
    right = mul(P_prime, list(s))
    size = max(len(left), len(right))
    W = [
        (3 * (left[j] if j < len(left) else 0)
         - (right[j] if j < len(right) else 0)) % p
        for j in range(size)
    ]
    support = [[j, value] for j, value in enumerate(W) if value]
    assert support[0] == [p - 2, 1]
    assert all(j in (p - 2, p) for j, _ in support)

    return {
        "s3_to_sn": list(values),
        "ratio_residual_8s4_plus_3s3": ratio_residual,
        "wronskian_support": support,
    }


def solve_p11() -> list[tuple[int, ...]]:
    p = 11
    n = 6
    solutions: list[tuple[int, ...]] = []
    for values in product(range(p), repeat=n - 2):
        s = (1, 0, 0) + values
        if not all(cube_coeff(s, j, p) == 0 for j in range(n + 2, 2 * n - 2)):
            continue
        if cube_coeff(s, 2 * n - 2, p) != p - 1:
            continue
        if cube_coeff(s, 2 * n - 1, p) != p - 1:
            continue
        solutions.append(values)
    return solutions


def solve_p17() -> list[tuple[int, ...]]:
    """Solve the seven cube-gap equations by two exact linear eliminations."""
    p = 17
    inv = [0] + [pow(x, -1, p) for x in range(1, p)]
    solutions: list[tuple[int, ...]] = []

    # a,b,c,d,e are s3,...,s7.  The first two equations solve s8,s9
    # whenever possible; degenerate cases are enumerated exactly.
    for a, b, c, d, e in product(range(p), repeat=5):
        first = (3*a*a*c + 3*a*b*b + 6*b*e + 6*c*d) % p
        pairs: list[tuple[int, int]] = []
        if a:
            f = (-first * inv[(6*a) % p]) % p
            second = (
                3*a*a*d + 6*a*b*c + b**3 + 6*b*f + 6*c*e + 3*d*d
            ) % p
            g = (-second * inv[(6*a) % p]) % p
            pairs = [(f, g)]
        elif first == 0:
            second = (b**3 + 6*c*e + 3*d*d) % p
            if b:
                f = (-second * inv[(6*b) % p]) % p
                pairs = [(f, g) for g in range(p)]
            elif second == 0:
                pairs = list(product(range(p), repeat=2))

        for f, g in pairs:
            values = (a, b, c, d, e, f, g)
            s = (1, 0, 0) + values
            if not all(cube_coeff(s, j, p) == 0 for j in range(11, 16)):
                continue
            if cube_coeff(s, 16, p) != 16 or cube_coeff(s, 17, p) != 16:
                continue
            solutions.append(values)
    return solutions


def main() -> None:
    raw = {11: solve_p11(), 17: solve_p17()}
    expected = {
        11: [(4, 10, 4, 2), (7, 2, 6, 4)],
        17: [(1, 10, 5, 8, 13, 7, 9), (16, 9, 0, 7, 14, 9, 1)],
    }
    assert raw == expected

    results = {
        str(p): {
            "cube_gap_solution_count": len(values),
            "candidates": [candidate_record(p, value) for value in values],
            "degree_half_endpoint_exists": False,
        }
        for p, values in raw.items()
    }
    output = {
        "classification": "exact computer-assisted finite theorem; no irreducibility census",
        "results": results,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "artin_schreier_first_dense_endpoint_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    for p in (11, 17):
        print(f"p={p}: two cube-gap candidates, both fail 8*s4+3*s3=0")
    print("ARTIN_SCHREIER_FIRST_DENSE_ENDPOINT_VERIFY: PASS")


if __name__ == "__main__":
    main()
