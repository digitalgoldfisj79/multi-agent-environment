#!/usr/bin/env python3
"""Verify the exact rough-quotient hyperbola collapse on finite panels."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

from sympy import divisors, mobius, nextprime, primerange


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def candidate_set(P: int, z: int, H: int) -> list[int]:
    return [m for m in range(z + 1, H + 1) if math.gcd(m, P) == 1]


def quotient_set(P: int, z: int, H: int, q: int) -> list[int]:
    lo = (P + z) // q + 1
    hi = (P + H) // q
    return [k for k in range(lo, hi + 1) if math.gcd(k, P) == 1]


def floor_count(P: int, z: int, H: int, q: int) -> int:
    return sum(
        int(mobius(d)) * ((P + H) // (q * d) - (P + z) // (q * d))
        for d in map(int, divisors(P))
    )


def one_case(z: int, H: int) -> dict:
    P = primorial(z)
    zp = int(nextprime(z))
    assert z < H < zp * zp

    candidates = candidate_set(P, z, H)
    primes = list(map(int, primerange(z + 1, H + 1)))
    assert candidates == primes

    weights = {m: 1.0 + 0.07 * math.cos(m) + 0.03 * math.sin(2 * m) for m in candidates}
    beta = 1.0 + 0.01 * z
    M = len(candidates)

    maximum_transport_error = 0
    maximum_weighted_error = 0.0
    maximum_floor_error = 0
    maximum_discrepancy_error = 0.0
    maximum_phase_error = 0.0
    total_direct_hits = 0
    total_quotient_hits = 0
    total_hyperbola_hits = 0
    rows: list[dict] = []

    for q in candidates:
        direct_ms = [m for m in candidates if (P + m) % q == 0]
        quotient_ks = quotient_set(P, z, H, q)
        transported_ms = [q * k - P for k in quotient_ks]
        assert direct_ms == transported_ms

        for k in range((P + z) // q + 1, (P + H) // q + 1):
            m = q * k - P
            lhs = math.gcd(m, P) == 1
            rhs = math.gcd(k, P) == 1
            maximum_transport_error = max(maximum_transport_error, int(lhs != rhs))
            assert lhs == rhs

        direct_weight = math.fsum(weights[m] for m in direct_ms)
        quotient_weight = math.fsum(weights[q * k - P] for k in quotient_ks)
        maximum_weighted_error = max(maximum_weighted_error, abs(direct_weight - quotient_weight))

        N = len(quotient_ks)
        N_floor = floor_count(P, z, H, q)
        maximum_floor_error = max(maximum_floor_error, abs(N - N_floor))
        assert N == N_floor

        direct_delta = beta * N - beta * (M - 1) / (q - 1)
        quotient_delta = beta * (N_floor - (M - 1) / (q - 1))
        maximum_discrepancy_error = max(maximum_discrepancy_error, abs(direct_delta - quotient_delta))

        # Check reciprocal phase separation for a representative bounded set.
        for d in map(int, divisors(P)):
            Pd = P // d
            for h in (1, 2, 3):
                for t in (z, H):
                    lhs = cmath.exp(2j * math.pi * ((h * (P + t)) % (q * d)) / (q * d))
                    rhs = (
                        cmath.exp(2j * math.pi * ((h * Pd) % q) / q)
                        * cmath.exp(2j * math.pi * ((h * t) % (q * d)) / (q * d))
                    )
                    maximum_phase_error = max(maximum_phase_error, abs(lhs - rhs))

        total_direct_hits += len(direct_ms)
        total_quotient_hits += N
        rows.append({
            "q": q,
            "direct_hit_count": len(direct_ms),
            "quotient_hit_count": N,
            "mobius_floor_count": N_floor,
            "weighted_error": abs(direct_weight - quotient_weight),
            "centred_discrepancy": quotient_delta,
            "quotient_interval_length": max(0, (P + H) // q - (P + z) // q),
        })

    # Symmetric rough hyperbola count.
    for q in range(z + 1, H + 1):
        for k in range((P + z) // q + 1, (P + H) // q + 1):
            if math.gcd(q * k, P) == 1:
                total_hyperbola_hits += 1

    assert total_direct_hits == total_quotient_hits == total_hyperbola_hits
    assert maximum_transport_error == 0
    assert maximum_weighted_error < 2e-12
    assert maximum_floor_error == 0
    assert maximum_discrepancy_error < 2e-12
    assert maximum_phase_error < 2e-12

    return {
        "z": z,
        "P": P,
        "H": H,
        "next_prime": zp,
        "candidate_count": M,
        "total_hit_count": total_direct_hits,
        "maximum_transport_error": maximum_transport_error,
        "maximum_weighted_error": maximum_weighted_error,
        "maximum_floor_error": maximum_floor_error,
        "maximum_discrepancy_error": maximum_discrepancy_error,
        "maximum_phase_error": maximum_phase_error,
        "rows": rows,
    }


def main() -> None:
    panels = [one_case(7, 20), one_case(11, 30), one_case(13, 36), one_case(17, 80)]
    payload = {
        "status": "PASS",
        "scope": "rough quotient bijection, Möbius-floor identity, centred discrepancy and reciprocal phase",
        "panels": panels,
        "boundary": "Finite exact verification only; cancellation in the signed smooth-divisor sawtooth remains open.",
    }
    output = Path(__file__).with_name("rough_quotient_hyperbola_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
