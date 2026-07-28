#!/usr/bin/env python3
"""Verify exact grouping by the genuinely new squarefree modulus part."""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

from sympy import factorint, mobius, primerange, totient


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def ramanujan(q: int, n: int) -> int:
    g = math.gcd(q, n)
    return int(mobius(q // g)) * int(totient(q)) // int(totient(q // g))


def gamma(Z: int, q: int) -> float:
    return -sum(
        float(mobius(q * u)) * math.log(q * u) / u
        for u in range(1, Z // q + 1)
    ) / q


def one_case(z: int, H: int) -> dict:
    P = primorial(z)
    Z = P + H
    weights = {m: 1.0 + 0.05 * math.cos(m) for m in range(2, H + 1)}

    direct_new = 0.0
    grouped = 0.0
    first_order = 0.0
    higher_order = 0.0
    active_new_parts: set[int] = set()

    by_new: dict[int, dict[int, float]] = defaultdict(lambda: defaultdict(float))
    for q in range(2, Z + 1):
        gq = gamma(Z, q)
        if abs(gq) < 1e-18:
            continue
        if P % q == 0:
            continue
        q0 = math.gcd(q, P)
        q1 = q // q0
        assert q1 > 1 and math.gcd(q1, P) == 1
        assert mobius(q) != 0
        for m, w in weights.items():
            term = gq * w * ramanujan(q, P + m)
            direct_new += term
            by_new[q1][m] += gq * ramanujan(q0, m)

    for q1, rows in by_new.items():
        active_new_parts.add(q1)
        factors = list(map(int, factorint(q1)))
        assert all(p > z for p in factors)
        if q1 <= H:
            assert len(factors) == 1 and len(factorint(q1)) == 1
        for m, coefficient in rows.items():
            term = weights[m] * ramanujan(q1, P + m) * coefficient
            grouped += term
            if q1 <= H:
                first_order += term
            else:
                higher_order += term

    local_error = 0.0
    for r0 in primerange(z + 1, H + 1):
        r = int(r0)
        for m in range(2, H + 1):
            n = P + m
            lam = 1 / (r - 1) - r / (r - 1) * (1 if n % r == 0 else 0)
            rhs = float(mobius(r)) * ramanujan(r, n) / int(totient(r))
            local_error = max(local_error, abs(lam - rhs))

    return {
        "z": z,
        "P": P,
        "H": H,
        "Z": Z,
        "active_new_part_count": len(active_new_parts),
        "active_first_order_count": sum(1 for q in active_new_parts if q <= H),
        "active_higher_order_count": sum(1 for q in active_new_parts if q > H),
        "direct_new_residual": direct_new,
        "grouped_new_residual": grouped,
        "grouping_error": abs(direct_new - grouped),
        "first_order_component": first_order,
        "higher_order_component": higher_order,
        "component_sum_error": abs(grouped - first_order - higher_order),
        "local_lambda_error": local_error,
    }


def main() -> None:
    rows = [one_case(7, 20), one_case(11, 30), one_case(13, 36)]
    for row in rows:
        assert row["grouping_error"] < 3e-8, row
        assert row["component_sum_error"] < 3e-8, row
        assert row["local_lambda_error"] < 2e-14, row
    payload = {
        "status": "PASS",
        "scope": "exact new-part Ramanujan grouping and first/higher chaos split",
        "rows": rows,
        "boundary": "Finite exact identities only; the joint signed covariance theorem remains open.",
    }
    Path(__file__).with_name("new_part_ramanujan_chaos_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
