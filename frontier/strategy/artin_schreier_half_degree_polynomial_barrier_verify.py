#!/usr/bin/env python3
"""Regression for the half-degree polynomial semiconjugacy barrier.

For p=6k+5, m=(p+1)/3=2k+2. The proof excludes every degree
n=m+s-1 with 1<=s<=k, hence every n<(p-1)/2.

The script checks the load-bearing degree inequalities and one classified
candidate identity for each s at every admitted prime below 200. It performs
no irreducibility census.
"""
from __future__ import annotations

import json
from pathlib import Path


def primes(limit: int) -> list[int]:
    return [
        n for n in range(2, limit)
        if all(n % d for d in range(2, int(n**0.5) + 1))
    ]


def mul_trunc(a: list[int], b: list[int], length: int, p: int) -> list[int]:
    out = [0] * length
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < length:
                out[i + j] = (out[i + j] + x * y) % p
    return out


def pow_trunc(a: list[int], exponent: int, length: int, p: int) -> list[int]:
    out = [1] + [0] * (length - 1)
    while exponent:
        if exponent & 1:
            out = mul_trunc(out, a, length, p)
        a = mul_trunc(a, a, length, p)
        exponent //= 2
    return out


def check_prime(p: int) -> dict[str, int | bool]:
    k = (p - 5) // 6
    m = (p + 1) // 3
    assert m == 2 * k + 2
    first_allowed = (p - 1) // 2

    for s in range(1, k + 1):
        n = m + s - 1
        q = 3 * s - 2
        assert 3 * n == p + q
        assert q < n
        assert q + 1 < n - 1
        assert 2 * n < p
        assert n < first_allowed

        # Classified candidate S=A*(1+gamma*T)^m has
        # S^3=A^3*(1+gamma*T) modulo T^(2n).
        length = 2 * n
        gamma = 2 % p
        A = [1] + [((j + 1) * (s + 1)) % p for j in range(s - 1)]
        A += [0] * (length - len(A))
        L = [1, gamma] + [0] * (length - 2)
        S = mul_trunc(A, pow_trunc(L, m, length, p), length, p)
        P = mul_trunc(pow_trunc(A, 3, length, p), L, length, p)
        assert pow_trunc(S, 3, length, p) == P
        assert n % p != 0

    return {
        "p": p,
        "m": m,
        "checked_s_count": k,
        "excluded_max_degree": first_allowed - 1,
        "first_not_excluded_degree": first_allowed,
        "status": True,
    }


def main() -> None:
    results = [check_prime(p) for p in primes(200) if p >= 17 and p % 6 == 5]
    # At p=11 the remaining degree-five endpoint is excluded separately:
    # the elimination discriminant is 6, a nonsquare modulo 11.
    assert pow(6, 5, 11) == 10
    output = {
        "classification": "symbolic structural regression; no prime census",
        "p11_endpoint_discriminant_6_nonsquare": True,
        "results": results,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "artin_schreier_half_degree_polynomial_barrier_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    for row in results:
        print(
            f"p={row['p']} checked_s={row['checked_s_count']} "
            f"excluded_degree<={row['excluded_max_degree']} "
            f"first_open={row['first_not_excluded_degree']} PASS"
        )
    print("ARTIN_SCHREIER_HALF_DEGREE_POLYNOMIAL_BARRIER_VERIFY: PASS")


if __name__ == "__main__":
    main()
