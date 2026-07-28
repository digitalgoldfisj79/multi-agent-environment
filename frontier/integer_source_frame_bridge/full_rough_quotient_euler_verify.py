#!/usr/bin/env python3
"""Verify the complete Euler-to-rough-quotient identity on finite panels."""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

from sympy import factorint, isprime, nextprime, primerange


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def candidate_set(P: int, z: int, H: int) -> list[int]:
    return [m for m in range(z + 1, H + 1) if math.gcd(m, P) == 1]


def admissible_divisors(n: int, z: int, Y: int) -> list[int]:
    factors = [int(p) for p in factorint(n) if z < int(p) <= Y]
    result = [1]
    for p in factors:
        result += [p * q for q in result]
    return sorted(result)


def one_case(z: int, H: int) -> dict:
    P = primorial(z)
    zp = int(nextprime(z))
    assert z < H < zp * zp
    Y = math.isqrt(P + H)
    if (Y + 1) * (Y + 1) <= P + H:
        Y += 1

    candidates = candidate_set(P, z, H)
    assert candidates == list(map(int, primerange(z + 1, H + 1)))
    weights = {m: 1.0 + 0.04 * math.cos(m) for m in candidates}

    direct = math.fsum(weights[m] for m in candidates if isprime(P + m))
    offset_expansion = 0.0
    active_Q: set[int] = set()
    maximum_local_euler_error = 0
    factor_cluster_rows = []

    for m in candidates:
        n = P + m
        divisors = admissible_divisors(n, z, Y)
        local = sum((-1) ** len(factorint(Q)) for Q in divisors)
        expected = 1 if isprime(n) else 0
        maximum_local_euler_error = max(maximum_local_euler_error, abs(local - expected))
        assert local == expected
        offset_expansion += weights[m] * local
        active_Q.update(divisors)

        t = len([p for p in factorint(n) if z < int(p) <= Y])
        if t:
            layer_sum = sum((-1) ** r * math.comb(t, r) for r in range(t + 1))
            assert layer_sum == 0
            factor_cluster_rows.append({"m": m, "t": t, "layer_sum": layer_sum})

    quotient_expansion = 0.0
    maximum_bijection_error = 0
    maximum_tail_support = 0
    layer_counts = {"principal": 0, "single_prime": 0, "higher_order": 0}
    rows = []

    for Q in sorted(active_Q):
        lo = (P + z) // Q + 1
        hi = (P + H) // Q
        ks = [k for k in range(lo, hi + 1) if math.gcd(k, P) == 1]
        ms = [Q * k - P for k in ks]
        direct_ms = [m for m in candidates if (P + m) % Q == 0]
        maximum_bijection_error = max(maximum_bijection_error, int(ms != direct_ms))
        assert ms == direct_ms

        omega = len(factorint(Q))
        coefficient = (-1) ** omega
        quotient_expansion += coefficient * math.fsum(weights[m] for m in ms)

        if Q == 1:
            layer = "principal"
        elif Q <= H:
            assert isprime(Q)
            assert omega == 1
            layer = "single_prime"
        else:
            assert omega >= 2
            assert len(ks) <= 1
            maximum_tail_support = max(maximum_tail_support, len(ks))
            layer = "higher_order"
        layer_counts[layer] += 1
        rows.append({"Q": Q, "omega": omega, "layer": layer, "support": len(ks)})

    assert maximum_local_euler_error == 0
    assert maximum_bijection_error == 0
    assert maximum_tail_support <= 1
    assert abs(direct - offset_expansion) < 2e-12
    assert abs(direct - quotient_expansion) < 2e-12

    return {
        "z": z,
        "P": P,
        "H": H,
        "Y": Y,
        "candidate_count": len(candidates),
        "active_Q_count": len(active_Q),
        "layer_counts": layer_counts,
        "direct_weighted_prime_output": direct,
        "offset_expansion_error": abs(direct - offset_expansion),
        "quotient_expansion_error": abs(direct - quotient_expansion),
        "maximum_local_euler_error": maximum_local_euler_error,
        "maximum_bijection_error": maximum_bijection_error,
        "maximum_higher_order_support": maximum_tail_support,
        "factor_cluster_count": len(factor_cluster_rows),
        "rows": rows,
    }


def main() -> None:
    panels = [one_case(7, 20), one_case(11, 30), one_case(13, 36), one_case(17, 80)]
    payload = {
        "status": "PASS",
        "scope": "complete Euler divisor cancellation and full rough-quotient geometry",
        "panels": panels,
        "boundary": "Finite exact verification only; deterministic centred sampling of the full quotient system remains open.",
    }
    output = Path(__file__).with_name("full_rough_quotient_euler_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
