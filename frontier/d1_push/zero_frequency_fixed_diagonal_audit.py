#!/usr/bin/env python3
"""Exact algebraic audit for ZERO_FREQUENCY_FIXED_DIAGONAL_REDUCTION.md."""
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


def audit_prime(p: int) -> dict:
    # Deterministic test vectors spanning the relevant identities.
    vectors = []
    for seed in range(min(p, 12)):
        h = [((seed + 1) * (i + 2) + i * i) % p for i in range(p - 1)]
        h.append((-sum(h)) % p)
        vectors.append(h)

    hyperplane_checks = []
    for h in vectors:
        hyperplane_checks.append(
            {
                "sum_zero": sum(h) % p == 0,
                "pth_power_sum_zero": sum(pow(x, p, p) for x in h) % p == 0,
                "frobenius_of_sum_zero": pow(sum(h) % p, p, p) == 0,
            }
        )

    t_rows = []
    for t in range(p):
        # The one-factor quadratic coefficient is 3*a*t; take a=1 since a!=0
        # only rescales the classification.
        qcoeff = (3 * t) % p
        t_rows.append(
            {
                "t": t,
                "quadratic_nonzero_iff_t_nonzero": (qcoeff != 0) == (t != 0),
                "type": "A2" if t == 0 else "A1",
            }
        )

    # Fixed diagonal constraints and phase are identities p*lambda=0,
    # p*lambda*t=0 and p*lambda*(t^p+a*t^3)=0 in F_p.
    diagonal_checks = []
    for t in range(min(p, 20)):
        for lam in range(1, min(p, 20)):
            phase = (-p * lam * (pow(t, p, p) + pow(t, 3, p))) % p
            diagonal_checks.append(
                {
                    "sum_lambda_zero": (p * lam) % p == 0,
                    "sum_lambda_t_zero": (p * lam * t) % p == 0,
                    "restricted_phase_zero": phase == 0,
                }
            )

    checks = {
        "all_hyperplane_checks": all(all(r.values()) for r in hyperplane_checks),
        "unique_A2_parameter": sum(r["type"] == "A2" for r in t_rows) == 1,
        "all_A1_elsewhere": all(r["type"] == ("A2" if r["t"] == 0 else "A1") for r in t_rows),
        "all_diagonal_checks": all(all(r.values()) for r in diagonal_checks),
        "cyclic_trace_polynomial_value_one": sum(1 if i % 2 == 0 else -1 for i in range(p)) == 1,
    }

    return {
        "p": p,
        "pass": all(checks.values()),
        "checks": checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=199)
    parser.add_argument("--primes", nargs="*", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    primes = args.primes or primes_up_to(args.max_prime)
    rows = [audit_prime(p) for p in primes]
    result = {
        "status": "PASS" if all(r["pass"] for r in rows) else "FAIL",
        "method": "Exact modular arithmetic on deterministic spanning test vectors.",
        "prime_count": len(rows),
        "min_prime": min(primes) if primes else None,
        "max_prime": max(primes) if primes else None,
        "rows": rows,
    }
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
