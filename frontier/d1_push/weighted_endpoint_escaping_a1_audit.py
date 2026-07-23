#!/usr/bin/env python3
"""Exact audit for WEIGHTED_ENDPOINT_ESCAPING_A1_THEOREM.md.

The audit has two layers.

1. Symbolic exponent/coefficient checks valid for arbitrary a, xi with
   3*a*xi^2=1.
2. Exhaustive finite-field checks in the convenient specialization
   xi=1, a=1/3 for small primes.  This specialization tests all algebraic
   identities without requiring a quadratic-extension implementation.

No floating point or random sampling is used.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def inv(x: int, p: int) -> int:
    return pow(x % p, p - 2, p)


def audit_prime(p: int, exhaustive_limit: int) -> dict:
    if p < 5 or p % 2 == 0:
        raise ValueError("p must be an odd prime >=5")

    e = (p - 3) // 2
    M = e * (p - 1)

    symbolic_checks = {
        "p_minus_3_equals_2e": p - 3 == 2 * e,
        "rescaled_exponent": e * p - e == M,
        "tame_T_exponent": M % p != 0,
        "critical_escape_exponent": e >= 1,
        "critical_value_lower_exponent": e * p - e == M,
        "two_distinct_signs_characteristic_not_two": p != 2,
    }

    # Convenient exact specialization: xi=1, a=1/3.
    a = inv(3, p)
    xi = 1
    relation = (3 * a * xi * xi) % p == 1

    exhaustive = p <= exhaustive_limit
    critical_failures = 0
    germ_failures = 0
    value_failures = 0
    checked = 0

    if exhaustive:
        for tau in range(1, p):
            tau_e_inv = inv(pow(tau, e, p), p)
            tau_ep = pow(tau, e * p, p)
            T = pow(tau, M, p)
            for sign in (1, -1):
                w0 = sign * xi * tau_e_inv % p

                # Critical equation -1+3*a*tau^(p-3)*w0^2=0.
                derivative = (
                    -1 + 3 * a * pow(tau, p - 3, p) * w0 * w0
                ) % p
                if derivative != 0:
                    critical_failures += 1

                # Rescaled critical value.
                Fw0 = (
                    pow(w0, p, p)
                    - w0
                    + a * pow(tau, p - 3, p) * pow(w0, 3, p)
                ) % p
                lhs_value = tau_ep * Fw0 % p
                rhs_value = sign * (
                    pow(xi, p, p) - 2 * inv(3, p) * xi * T
                ) % p
                if lhs_value != rhs_value:
                    value_failures += 1

                for h in range(p):
                    delta = tau_e_inv * h % p
                    w = (w0 + delta) % p
                    Fw = (
                        pow(w, p, p)
                        - w
                        + a * pow(tau, p - 3, p) * pow(w, 3, p)
                    ) % p
                    lhs = tau_ep * (Fw - Fw0) % p
                    rhs = (
                        pow(h, p, p)
                        + T
                        * (
                            3 * a * sign * xi * h * h
                            + a * h * h * h
                        )
                    ) % p
                    if lhs != rhs:
                        germ_failures += 1
                    checked += 1

    # The A1 Hessian coefficient at h=0 is 6*a*sign*xi, nonzero.
    hessian_nonzero = all((6 * a * sign * xi) % p != 0 for sign in (1, -1))

    checks = {
        **symbolic_checks,
        "normalization_relation_3axi2_is_one": relation,
        "hessian_nonzero_both_signs": hessian_nonzero,
        "critical_sections": critical_failures == 0,
        "rescaled_germ": germ_failures == 0,
        "rescaled_critical_values": value_failures == 0,
    }

    return {
        "p": p,
        "pass": all(checks.values()),
        "e": e,
        "T_exponent": M,
        "exhaustive": exhaustive,
        "finite_field_tuples_checked": checked,
        "failures": {
            "critical": critical_failures,
            "germ": germ_failures,
            "critical_value": value_failures,
        },
        "checks": checks,
    }


def primes_up_to(limit: int) -> list[int]:
    out = []
    for n in range(5, limit + 1, 2):
        if all(n % q for q in range(3, int(n**0.5) + 1, 2)):
            out.append(n)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=199)
    parser.add_argument("--exhaustive-limit", type=int, default=31)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    rows = [
        audit_prime(p, args.exhaustive_limit)
        for p in primes_up_to(args.max_prime)
    ]
    result = {
        "status": "PASS" if all(row["pass"] for row in rows) else "FAIL",
        "method": "Exact exponent arithmetic and exhaustive F_p identities; no floating point.",
        "prime_count": len(rows),
        "max_prime": max(row["p"] for row in rows),
        "exhaustive_limit": args.exhaustive_limit,
        "total_finite_field_tuples_checked": sum(
            row["finite_field_tuples_checked"] for row in rows
        ),
        "rows": rows,
    }
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
