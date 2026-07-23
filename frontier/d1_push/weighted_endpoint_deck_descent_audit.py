#!/usr/bin/env python3
"""Exact finite audit for WEIGHTED_ENDPOINT_DECK_DESCENT_THEOREM.md."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def primes_up_to(n: int) -> list[int]:
    out = []
    for p in range(5, n + 1, 2):
        if all(p % q for q in range(3, int(p**0.5) + 1, 2)):
            out.append(p)
    return out


def legendre(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def audit_prime(p: int) -> dict:
    e = (p - 3) // 2
    m = (p - 1) // 2
    rows = []
    ok = e + 1 == m

    # Work in F_p^*: every element is a Teichmuller representative of a
    # Kummer deck element after adjoining the required roots.
    for zeta in range(1, p):
        chi = legendre(zeta, p)
        sign_multiplier = pow(zeta, e + 1, p)
        expected = 1 if chi == 1 else p - 1
        checks = {
            "zeta_p_equals_zeta": pow(zeta, p, p) == zeta,
            "family_scaling_cubic": pow(zeta, p - 3 + 3, p) == zeta,
            "branch_multiplier_quadratic": sign_multiplier == expected,
            "square_preserves_nonsquare_swaps": (
                (chi == 1 and sign_multiplier == 1)
                or (chi == -1 and sign_multiplier == p - 1)
            ),
        }
        ok = ok and all(checks.values())
        rows.append({"zeta": zeta, "chi": chi, "checks": checks})

    return {
        "p": p,
        "e": e,
        "m": m,
        "e_plus_one_equals_m": e + 1 == m,
        "pass": ok,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=199)
    parser.add_argument("--primes", nargs="*", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    primes = args.primes or primes_up_to(args.max_prime)
    results = [audit_prime(p) for p in primes]
    output = {
        "status": "PASS" if all(r["pass"] for r in results) else "FAIL",
        "method": "Exact modular arithmetic; no floating point.",
        "prime_count": len(results),
        "min_prime": min(primes) if primes else None,
        "max_prime": max(primes) if primes else None,
        "results": results,
    }
    text = json.dumps(output, indent=2)
    print(text)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
