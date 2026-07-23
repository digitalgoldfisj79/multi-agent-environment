#!/usr/bin/env python3
"""Symbolic and cycle-character audit for WCE.1--WCE.2."""
from __future__ import annotations

import argparse
import json
from math import isqrt

import sympy as sp


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def adams_defect_from_cycles(cycles: list[int], p: int) -> int:
    fixed = sum(1 for length in cycles if length == 1)
    fixed_p = sum(length for length in cycles if p % length == 0)
    return fixed_p - fixed


def audit_prime(p: int) -> dict:
    R, S, z, x = sp.symbols("R S z x")
    exceptional = R * z**p - S * z ** (p - 1) - R * S
    r_endpoint = sp.expand(exceptional.subs(S, 1))
    s_endpoint = sp.expand(exceptional.subs(R, 1))

    # Cross-multiplied exact chart equations, written with the same sign.
    r_identity = sp.expand((z**p - 1) * R - z ** (p - 1))
    s_identity = sp.expand(z**p - (1 + z ** (p - 1)) * S)
    reciprocal = sp.expand((s_endpoint * x**p).subs(z, 1 / x))

    r_pass = sp.expand(r_endpoint - r_identity) == 0
    s_pass = sp.expand(s_endpoint - s_identity) == 0
    reciprocal_pass = sp.simplify(reciprocal - (1 - S * x - S * x**p)) == 0

    tame_cycle_value = adams_defect_from_cycles([p - 1, 1], p)
    translation_value = adams_defect_from_cycles([p], p)
    identity_value = adams_defect_from_cycles([1] * p, p)

    return {
        "p": p,
        "R_endpoint_identity_pass": r_pass,
        "S_endpoint_identity_pass": s_pass,
        "reciprocal_AS_pass": reciprocal_pass,
        "tame_cycle_adams_value": tame_cycle_value,
        "translation_adams_value": translation_value,
        "identity_adams_value": identity_value,
        "pass": r_pass
        and s_pass
        and reciprocal_pass
        and tame_cycle_value == 0
        and translation_value == p
        and identity_value == 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=101)
    args = parser.parse_args()
    rows = [audit_prime(p) for p in primes_upto(args.max_prime) if p >= 5]
    for row in rows:
        print(json.dumps(row), flush=True)
    print(json.dumps({"status": "PASS" if all(r["pass"] for r in rows) else "FAIL", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
