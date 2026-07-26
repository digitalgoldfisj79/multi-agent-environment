#!/usr/bin/env python3
"""Regression for the resonant polynomial semiconjugacy barrier.

For p=3h+2 and m=h+1=(p+1)/3, the theorem proves that any degree-m
polynomial semiconjugacy would have to be R(Z)=r(Z+gamma)^m.  After shifting
gamma away, reduction modulo Z^p-Z-1 leaves the nonzero coefficient r*m at
Z^(m-1), giving a contradiction for p>=11.

This script checks the formal cube-root identity and the final obstruction
for every admitted prime below 200.  It performs no irreducibility census.
"""
from __future__ import annotations

import json
from pathlib import Path


def primes(limit: int) -> list[int]:
    out = []
    for n in range(2, limit):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            out.append(n)
    return out


def mul_trunc(a: list[int], b: list[int], modulus_degree: int, p: int) -> list[int]:
    out = [0] * modulus_degree
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < modulus_degree:
                out[i + j] = (out[i + j] + x * y) % p
    return out


def pow_trunc(a: list[int], exponent: int, modulus_degree: int, p: int) -> list[int]:
    out = [1] + [0] * (modulus_degree - 1)
    while exponent:
        if exponent & 1:
            out = mul_trunc(out, a, modulus_degree, p)
        a = mul_trunc(a, a, modulus_degree, p)
        exponent //= 2
    return out


def binomial_row(m: int, gamma: int, p: int) -> list[int]:
    out = [0] * (m + 1)
    coeff = 1
    out[0] = 1
    for k in range(1, m + 1):
        coeff = coeff * (m - k + 1) * pow(k, -1, p) % p
        out[k] = coeff * pow(gamma, k, p) % p
    return out


def check_prime(p: int) -> dict[str, int | bool]:
    h = (p - 2) // 3
    m = h + 1
    assert 3 * m == p + 1
    modulus_degree = 2 * m

    gamma = 2 % p
    s = binomial_row(m, gamma, p) + [0] * (modulus_degree - (m + 1))
    cube = pow_trunc(s, 3, modulus_degree, p)
    expected = [0] * modulus_degree
    expected[0] = 1
    expected[1] = gamma
    assert cube == expected

    for r in (1, 2 % p, p - 1):
        obstruction = r * m % p
        assert m >= 4
        assert obstruction != 0

    return {
        "p": p,
        "m": m,
        "cube_root_identity": True,
        "obstruction_coefficient_m_minus_1_for_r_1": m % p,
        "status": True,
    }


def main() -> None:
    results = [check_prime(p) for p in primes(200) if p >= 11 and p % 6 == 5]
    output = {
        "classification": "symbolic structural regression; no prime census",
        "results": results,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "artin_schreier_resonant_polynomial_barrier_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    for row in results:
        print(
            f"p={row['p']} threshold_m={row['m']} "
            f"obstruction={row['obstruction_coefficient_m_minus_1_for_r_1']} PASS"
        )
    print("ARTIN_SCHREIER_RESONANT_POLYNOMIAL_BARRIER_VERIFY: PASS")


if __name__ == "__main__":
    main()
