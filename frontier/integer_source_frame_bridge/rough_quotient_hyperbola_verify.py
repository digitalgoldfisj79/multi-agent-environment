#!/usr/bin/env python3
"""Verify the exact rough-quotient collapse with a frozen lower cutoff Z >= z."""
from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import divisors, mobius, nextprime, primerange


def primorial(z: int) -> int:
    value = 1
    for p in primerange(2, z + 1):
        value *= int(p)
    return value


def candidate_set(P: int, Z: int, H: int) -> list[int]:
    return [m for m in range(Z + 1, H + 1) if math.gcd(m, P) == 1]


def quotient_set(P: int, Z: int, H: int, q: int) -> list[int]:
    lo = (P + Z) // q + 1
    hi = (P + H) // q
    return [k for k in range(lo, hi + 1) if math.gcd(k, P) == 1]


def floor_count(P: int, Z: int, H: int, q: int) -> int:
    return sum(
        int(mobius(d)) * ((P + H) // (q * d) - (P + Z) // (q * d))
        for d in map(int, divisors(P))
    )


def sawtooth(num: int, den: int) -> Fraction:
    return Fraction(num % den, den) - Fraction(1, 2)


def phi_over_P(P: int, z: int) -> Fraction:
    value = Fraction(1, 1)
    for p in primerange(2, z + 1):
        value *= Fraction(int(p) - 1, int(p))
    return value


def one_case(z: int, Z: int, H: int) -> dict:
    P = primorial(z)
    zp = int(nextprime(z))
    assert z <= Z < H < zp * zp

    candidates = candidate_set(P, Z, H)
    primes = list(map(int, primerange(Z + 1, H + 1)))
    assert candidates == primes

    weights = {m: 1.0 + 0.07 * math.cos(m) + 0.03 * math.sin(2 * m) for m in candidates}
    beta = 1.0 + 0.01 * z
    M = len(candidates)
    density = phi_over_P(P, z)

    maximum_transport_error = 0
    maximum_weighted_error = 0.0
    maximum_floor_error = 0
    maximum_sawtooth_error = Fraction(0, 1)
    maximum_discrepancy_error = 0.0
    maximum_phase_error = 0.0
    total_direct_hits = 0
    total_quotient_hits = 0
    total_hyperbola_hits = 0
    rows: list[dict] = []

    P_divisors = list(map(int, divisors(P)))
    for q in candidates:
        direct_ms = [m for m in candidates if (P + m) % q == 0]
        quotient_ks = quotient_set(P, Z, H, q)
        transported_ms = [q * k - P for k in quotient_ks]
        assert direct_ms == transported_ms

        for k in range((P + Z) // q + 1, (P + H) // q + 1):
            m = q * k - P
            lhs = math.gcd(m, P) == 1
            rhs = math.gcd(k, P) == 1
            maximum_transport_error = max(maximum_transport_error, int(lhs != rhs))
            assert lhs == rhs

        direct_weight = math.fsum(weights[m] for m in direct_ms)
        quotient_weight = math.fsum(weights[q * k - P] for k in quotient_ks)
        maximum_weighted_error = max(maximum_weighted_error, abs(direct_weight - quotient_weight))

        N = len(quotient_ks)
        N_floor = floor_count(P, Z, H, q)
        maximum_floor_error = max(maximum_floor_error, abs(N - N_floor))
        assert N == N_floor

        N_saw = Fraction(H - Z, q) * density + sum(
            Fraction(int(mobius(d)), 1)
            * (sawtooth(P + Z, q * d) - sawtooth(P + H, q * d))
            for d in P_divisors
        )
        maximum_sawtooth_error = max(maximum_sawtooth_error, abs(Fraction(N, 1) - N_saw))
        assert N_saw == N

        direct_delta = beta * N - beta * (M - 1) / (q - 1)
        quotient_delta = beta * (N_floor - (M - 1) / (q - 1))
        maximum_discrepancy_error = max(maximum_discrepancy_error, abs(direct_delta - quotient_delta))

        for d in P_divisors:
            Pd = P // d
            for h in (1, 2, 3):
                for t in (Z, H):
                    lhs = cmath.exp(2j * math.pi * ((h * (P + t)) % (q * d)) / (q * d))
                    rhs = (
                        cmath.exp(2j * math.pi * ((h * Pd) % q) / q)
                        * cmath.exp(2j * math.pi * ((h * t) % (q * d)) / (q * d))
                    )
                    maximum_phase_error = max(maximum_phase_error, abs(lhs - rhs))

        total_direct_hits += len(direct_ms)
        total_quotient_hits += N
        rows.append(
            {
                "q": q,
                "direct_hit_count": len(direct_ms),
                "quotient_hit_count": N,
                "mobius_floor_count": N_floor,
                "weighted_error": abs(direct_weight - quotient_weight),
                "centred_discrepancy": quotient_delta,
                "quotient_interval_length": max(0, (P + H) // q - (P + Z) // q),
            }
        )

    for q in range(Z + 1, H + 1):
        for k in range((P + Z) // q + 1, (P + H) // q + 1):
            if math.gcd(q * k, P) == 1:
                total_hyperbola_hits += 1

    assert total_direct_hits == total_quotient_hits == total_hyperbola_hits
    assert maximum_transport_error == 0
    assert maximum_weighted_error < 2e-12
    assert maximum_floor_error == 0
    assert maximum_sawtooth_error == 0
    assert maximum_discrepancy_error < 2e-12
    assert maximum_phase_error < 2e-12

    return {
        "z": z,
        "Z": Z,
        "P": P,
        "H": H,
        "next_prime_after_z": zp,
        "candidate_count": M,
        "total_hit_count": total_direct_hits,
        "maximum_transport_error": maximum_transport_error,
        "maximum_weighted_error": maximum_weighted_error,
        "maximum_floor_error": maximum_floor_error,
        "maximum_sawtooth_error": float(maximum_sawtooth_error),
        "maximum_discrepancy_error": maximum_discrepancy_error,
        "maximum_phase_error": maximum_phase_error,
        "rows": rows,
    }


def main() -> None:
    panels = [
        one_case(7, 11, 20),
        one_case(11, 17, 30),
        one_case(13, 19, 36),
        one_case(17, 23, 80),
    ]
    payload = {
        "status": "PASS",
        "scope": (
            "general-cutoff rough quotient bijection, Mobius-floor and sawtooth identities, "
            "centred discrepancy and reciprocal phase"
        ),
        "panels": panels,
        "boundary": (
            "Finite exact verification only; cancellation in the signed smooth-divisor "
            "sawtooth and the same-band Bessel theorem remain OPEN."
        ),
    }
    output = Path(__file__).with_name("rough_quotient_hyperbola_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
