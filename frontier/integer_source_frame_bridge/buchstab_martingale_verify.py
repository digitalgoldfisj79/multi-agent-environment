#!/usr/bin/env python3
"""Verify the exact ordered Buchstab identity and quadratic variation."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import isprime, primerange


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def xi(r: int, n: int) -> float:
    return 1.0 / (r - 2) - (r - 1.0) / (r - 2) * (1.0 if n % r == 0 else 0.0)


def one_case(z: int, H: int) -> dict:
    P = primorial(z)
    Y = math.isqrt(P + H)
    physical = list(map(int, primerange(z + 1, H + 1)))
    tail = list(map(int, primerange(H + 1, Y + 1)))
    v = {r: (r - 2) / (r - 1) for r in tail}
    V_all = math.prod(v.values())

    # Exact quadratic-variation identity.
    survival_before = 1.0
    qv = 0.0
    suffix = {}
    current = 1.0
    for r in reversed(tail):
        current *= v[r]
        suffix[r] = current
    for r in tail:
        qv += suffix[r] ** 2 * survival_before / (r - 2)
        survival_before *= v[r]
    qv_error = abs(qv - V_all * (1 - V_all))

    rows = []
    maximum_identity_error = 0.0
    maximum_prime_indicator_error = 0.0
    maximum_negative_hits = 0
    for m0 in primerange(z + 1, H + 1):
        m = int(m0)
        n = P + m
        R_H = 1.0 if all(n % r for r in physical) else 0.0
        product_tail = math.prod(1.0 + xi(r, n) for r in tail)
        left = V_all * product_tail

        ordered = V_all
        R_before = 1.0
        negative_hits = 0
        increments = []
        for r in tail:
            inc = suffix[r] * R_before * xi(r, n)
            increments.append({"r": r, "increment": inc, "hit": n % r == 0})
            if n % r == 0:
                negative_hits += 1
                R_before = 0.0
        right = ordered + sum(item["increment"] for item in increments)
        identity_error = abs(left - right)
        maximum_identity_error = max(maximum_identity_error, identity_error)
        maximum_negative_hits = max(maximum_negative_hits, negative_hits)

        prime_indicator = 1.0 if isprime(n) else 0.0
        detector = R_H * right
        prime_error = abs(detector - prime_indicator)
        maximum_prime_indicator_error = max(maximum_prime_indicator_error, prime_error)

        least_tail_factor = None
        for r in tail:
            if n % r == 0:
                least_tail_factor = r
                break
        if least_tail_factor is not None and R_H:
            hit_rows = [item for item in increments if item["hit"] and abs(item["increment"]) > 0]
            assert len(hit_rows) == 1
            assert hit_rows[0]["r"] == least_tail_factor
        rows.append({
            "m": m,
            "n": n,
            "is_prime": bool(isprime(n)),
            "R_H": R_H,
            "least_tail_factor": least_tail_factor,
            "ordered_identity_error": identity_error,
            "prime_indicator_error": prime_error,
        })

    candidate_count = len(rows)
    logP = math.log(P)
    coefficient_budget_bound = candidate_count * (logP + 1) ** 2 * V_all
    return {
        "z": z,
        "P": P,
        "H": H,
        "Y": Y,
        "physical_prime_count": len(physical),
        "tail_prime_count": len(tail),
        "V_tail": V_all,
        "quadratic_variation": qv,
        "quadratic_variation_target": V_all * (1 - V_all),
        "quadratic_variation_error": qv_error,
        "candidate_count": candidate_count,
        "coefficient_budget_bound": coefficient_budget_bound,
        "coefficient_budget_over_HX": coefficient_budget_bound / (H * z),
        "maximum_ordered_identity_error": maximum_identity_error,
        "maximum_prime_indicator_error": maximum_prime_indicator_error,
        "maximum_negative_hits": maximum_negative_hits,
        "rows": rows,
    }


def main() -> None:
    cases = [one_case(7, 20), one_case(11, 30), one_case(13, 36)]
    for case in cases:
        assert case["quadratic_variation_error"] < 2e-12, case
        assert case["maximum_ordered_identity_error"] < 2e-12, case
        assert case["maximum_prime_indicator_error"] < 2e-12, case
        assert case["maximum_negative_hits"] <= 1, case
    payload = {
        "status": "PASS",
        "scope": "exact Buchstab martingale, one-hit structure and quadratic variation",
        "cases": cases,
        "boundary": "Finite exact identities only; deterministic martingale sampling remains open.",
    }
    Path(__file__).with_name("buchstab_martingale_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
