#!/usr/bin/env python3
"""Structural regression for the uniform degree-(p+1)/2 endpoint no-go.

The proof is algebraic. At n=(p+1)/2 the reciprocal semiconjugacy gives

  C + 3*s3 + 3*s4 = -lambda^(-1)*binom(n,2),
  lambda^(-1)=4*s3.

The Artin--Schreier trace filtration gives

  Tr(R(alpha)^4)=-(C+3*s3+3*s4)=-s3/2.

A cubic-tail minimal polynomial forces Tr(beta^4)=0, while s3 is nonzero.
The script checks the modular scalar identities below p=500 and evaluates
the exact p=11,17 cube-gap candidates.
"""
from __future__ import annotations

import json
from math import isqrt
from pathlib import Path


def primes_below(limit: int) -> list[int]:
    return [
        n for n in range(2, limit)
        if all(n % d for d in range(2, isqrt(n) + 1))
    ]


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def power(a: list[int], exponent: int, p: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = mul(out, a, p)
    return out


def trace_alpha_power(exponent: int, p: int) -> int:
    vec = [0] * p
    vec[0] = 1
    for _ in range(exponent):
        nxt = [0] * p
        for degree, value in enumerate(vec):
            if degree + 1 < p:
                nxt[degree + 1] = (nxt[degree + 1] + value) % p
            else:
                nxt[0] = (nxt[0] + value) % p
                nxt[1] = (nxt[1] + value) % p
        vec = nxt
    return (-vec[p - 1]) % p


def direct_trace_four(s: list[int], p: int) -> int:
    R = list(reversed(s))
    fourth = power(R, 4, p)
    return sum(
        coefficient * trace_alpha_power(degree, p)
        for degree, coefficient in enumerate(fourth)
    ) % p


def main() -> None:
    checked_primes = []
    for p in primes_below(500):
        if p < 11 or p % 6 != 5:
            continue
        n = (p + 1) // 2
        inv2 = pow(2, -1, p)
        choose_n_2 = n * (n - 1) * inv2 % p
        assert choose_n_2 == -pow(8, -1, p) % p
        for s3 in (1, 2, p - 1):
            lambda_inverse = 4 * s3 % p
            forced_trace = lambda_inverse * choose_n_2 % p
            assert forced_trace == -s3 * inv2 % p
            assert forced_trace != 0
        checked_primes.append(p)

    candidates = {
        11: [(4, 10, 4, 2), (7, 2, 6, 4)],
        17: [(1, 10, 5, 8, 13, 7, 9), (16, 9, 0, 7, 14, 9, 1)],
    }
    finite = {}
    for p, values_list in candidates.items():
        records = []
        for values in values_list:
            s = [1, 0, 0] + list(values)
            trace = direct_trace_four(s, p)
            assert trace != 0
            records.append({"s3_to_sn": list(values), "trace_four": trace})
        finite[str(p)] = records

    output = {
        "classification": "symbolic structural regression with exact finite candidates",
        "checked_primes": checked_primes,
        "number_of_primes": len(checked_primes),
        "identity": {
            "binom_n_2": "-1/8 mod p",
            "forced_trace_four": "-s3/2 mod p",
        },
        "finite_candidate_checks": finite,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "artin_schreier_dense_endpoint_trace4_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"checked {len(checked_primes)} admitted primes below 500")
    print("ARTIN_SCHREIER_DENSE_ENDPOINT_TRACE4_VERIFY: PASS")


if __name__ == "__main__":
    main()
