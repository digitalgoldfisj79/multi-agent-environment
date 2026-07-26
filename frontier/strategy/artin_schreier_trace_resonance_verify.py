#!/usr/bin/env python3
"""Structural regression for the Artin--Schreier trace-resonance theorem.

For alpha^p-alpha=1, Tr(alpha^j)=0 for 0<=j<=p-2 and
Tr(alpha^(p-1))=-1.  If R has degree n|p-1 and leading coefficient r,
then for m=(p-1)/n, Tr(R(alpha)^m)=-r^m.  A cubic-tail degree-p minimal
polynomial requires this trace to vanish whenever m<=p-4.

This script checks the arithmetic inequalities and the coefficient-level
trace calculation for every admitted prime p<300.  It performs no
irreducibility census.
"""
from __future__ import annotations

import json
from math import isqrt
from pathlib import Path


def primes_below(limit: int) -> list[int]:
    out: list[int] = []
    for n in range(2, limit):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            out.append(n)
    return out


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_pow(a: list[int], exponent: int, p: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = poly_mul(out, a, p)
    return out


def trace_low_degree(poly: list[int], p: int) -> int:
    """Trace of P(alpha) when deg P<=p-1."""
    assert len(poly) <= p
    return (-poly[p - 1]) % p if len(poly) == p else 0


def check_prime(p: int) -> dict[str, object]:
    forbidden = []
    for n in divisors(p - 1):
        if n < 2:
            continue
        m = (p - 1) // n
        assert m <= p - 4

        # Deterministic non-monomial polynomial with leading coefficient r.
        r = (n + 1) % p or 1
        R = [1, 2 % p] + [0] * max(0, n - 2) + [r]
        power = poly_pow(R, m, p)
        assert len(power) == p
        expected = (-pow(r, m, p)) % p
        assert trace_low_degree(power, p) == expected
        assert expected != 0
        forbidden.append({"degree": n, "moment": m})

    lower = (p + 1) // 2
    upper = p - 2
    assert lower <= upper
    assert (p - 1) // 2 in [x["degree"] for x in forbidden]
    return {
        "p": p,
        "forbidden_divisor_degrees": forbidden,
        "surviving_polynomial_corridor": [lower, upper],
    }


def main() -> None:
    rows = [check_prime(p) for p in primes_below(300) if p >= 11 and p % 6 == 5]
    output = {
        "classification": "symbolic structural regression; no prime census",
        "number_of_primes": len(rows),
        "rows": rows,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "artin_schreier_trace_resonance_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"checked {len(rows)} admitted primes below 300")
    print("ARTIN_SCHREIER_TRACE_RESONANCE_VERIFY: PASS")


if __name__ == "__main__":
    main()
