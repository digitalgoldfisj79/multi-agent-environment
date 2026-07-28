#!/usr/bin/env python3
"""Verify the exact primorial Ramanujan projector and its truncation bound."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import divisors, mobius, primerange, totient


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def ramanujan_sum(q: int, n: int) -> int:
    return sum(
        1 if (a * n) % q == 0 else 0
        for a in []
    ) if False else int(
        sum(
            complex(math.cos(2 * math.pi * a * n / q), math.sin(2 * math.pi * a * n / q))
            for a in range(1, q + 1)
            if math.gcd(a, q) == 1
        ).real.__round__()
    )


def ramanujan_exact(q: int, n: int) -> int:
    g = math.gcd(q, n)
    return int(mobius(q // g)) * int(totient(q)) // int(totient(q // g))


def one_case(z: int, H: int, delta: float) -> dict:
    P = primorial(z)
    ds = list(map(int, divisors(P)))
    Q = int(P ** (1 - delta))
    maximum_exact_error = 0.0
    maximum_candidate_error = 0.0
    maximum_tail = 0.0
    maximum_bound_ratio = 0.0
    candidate_matches = 0

    for m in range(2, H + 1):
        full = 0.0
        truncated = 0.0
        for q in ds:
            term = float(mobius(q)) * ramanujan_exact(q, m) / int(totient(q))
            full += term
            if q <= Q:
                truncated += term
        expected = P / int(totient(P)) if math.gcd(m, P) == 1 else 0.0
        maximum_exact_error = max(maximum_exact_error, abs(full - expected))
        is_candidate = all(m % p for p in primerange(2, z + 1))
        candidate_expected = 1.0 if is_candidate else 0.0
        maximum_candidate_error = max(
            maximum_candidate_error,
            abs(int(totient(P)) * full / P - candidate_expected),
        )
        if is_candidate:
            candidate_matches += 1
        tail = abs(full - truncated)
        bound = H * (2 ** len(list(primerange(2, z + 1)))) * (math.log(math.log(P + 3)) + 2) / max(Q, 1)
        maximum_tail = max(maximum_tail, tail)
        if bound > 0:
            maximum_bound_ratio = max(maximum_bound_ratio, tail / bound)
        assert tail <= bound + 1e-12

    local_formula_error = 0
    for q in ds[: min(100, len(ds))]:
        for m in range(1, min(H, 30) + 1):
            direct = ramanujan_sum(q, m)
            formula = ramanujan_exact(q, m)
            local_formula_error = max(local_formula_error, abs(direct - formula))

    return {
        "z": z,
        "P": P,
        "H": H,
        "delta": delta,
        "Q": Q,
        "divisor_count": len(ds),
        "candidate_matches": candidate_matches,
        "maximum_exact_projector_error": maximum_exact_error,
        "maximum_normalized_candidate_error": maximum_candidate_error,
        "maximum_truncation_tail": maximum_tail,
        "maximum_tail_to_crude_bound_ratio": maximum_bound_ratio,
        "local_ramanujan_formula_error": local_formula_error,
    }


def main() -> None:
    rows = [one_case(11, 150, 0.35), one_case(13, 200, 0.35), one_case(17, 350, 0.35)]
    for row in rows:
        assert row["maximum_exact_projector_error"] < 2e-10
        assert row["maximum_normalized_candidate_error"] < 2e-10
        assert row["local_ramanujan_formula_error"] == 0
    payload = {
        "status": "PASS",
        "scope": "exact primorial Ramanujan projector and finite truncation check",
        "rows": rows,
        "boundary": "The finite bound is deliberately crude; the theorem's asymptotic tail is P^{-1+delta+o(1)}.",
    }
    Path(__file__).with_name("primorial_ramanujan_projector_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
