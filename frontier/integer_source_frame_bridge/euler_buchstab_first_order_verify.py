#!/usr/bin/env python3
"""Verify the exact Euler detector and first-order progression/Gram identities."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

from sympy import isprime, primerange, primitive_root


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def xi(r: int, n: int) -> float:
    return 1.0 / (r - 2) - (r - 1.0) / (r - 2) * (1.0 if n % r == 0 else 0.0)


def characters_prime(r: int):
    g = int(primitive_root(r))
    logs = {}
    value = 1
    for k in range(r - 1):
        logs[value] = k
        value = value * g % r
    for t in range(r - 1):
        def chi(n: int, t=t):
            n %= r
            if n == 0:
                return 0j
            return cmath.exp(2j * math.pi * t * logs[n] / (r - 1))
        yield t, chi


def one_centre(z: int, H: int) -> dict:
    P = primorial(z)
    Y = math.isqrt(P + H)
    candidate = list(map(int, primerange(z + 1, H + 1)))
    local_primes = list(map(int, primerange(z + 1, Y + 1)))
    physical = [r for r in local_primes if r <= H]
    V = math.prod((r - 2) / (r - 1) for r in local_primes)
    b = {m: math.log(P + m) * V for m in candidate}

    exact_detector = sum(math.log(P + m) for m in candidate if isprime(P + m))
    product_detector = 0.0
    zero = sum(b.values())
    first = 0.0
    for m in candidate:
        prod = math.prod(1.0 + xi(r, P + m) for r in local_primes)
        product_detector += b[m] * prod
        first += b[m] * sum(xi(r, P + m) for r in local_primes)

    first_physical = 0.0
    centred_physical = 0.0
    exceptional = 0.0
    local_errors = []
    char_errors = []
    local_values = []
    for r in physical:
        X = sum(b[m] * xi(r, P + m) for m in candidate)
        A = sum(b[m] for m in candidate if (P + m) % r == 0)
        Bstar = sum(b[m] for m in candidate if m != r)
        discrepancy = A - Bstar / (r - 1)
        exc = b[r] / (r - 2) if r in b else 0.0
        centred = -(r - 1) / (r - 2) * discrepancy
        local_errors.append(abs(X - exc - centred))
        first_physical += X
        centred_physical += centred
        exceptional += exc

        # Independent multiplicative-character reconstruction of the discrepancy.
        char_sum = 0j
        for t, chi in characters_prime(r):
            if t == 0:
                continue
            source = sum(b[m] * chi(m) for m in candidate if m != r)
            char_sum += chi(-P).conjugate() * source
        char_delta = char_sum / (r - 1)
        char_errors.append(abs(char_delta - discrepancy))
        local_values.append({
            "r": r,
            "X": X,
            "A": A,
            "Bstar": Bstar,
            "discrepancy": discrepancy,
            "centred": centred,
            "exceptional": exc,
        })

    return {
        "z": z,
        "P": P,
        "H": H,
        "Y": Y,
        "candidate_count": len(candidate),
        "local_prime_count": len(local_primes),
        "physical_prime_count": len(physical),
        "V": V,
        "maximum_b": max(b.values(), default=0.0),
        "exact_detector": exact_detector,
        "product_detector": product_detector,
        "product_error": abs(exact_detector - product_detector),
        "zero_term": zero,
        "first_term_all": first,
        "first_term_physical": first_physical,
        "centred_physical": centred_physical,
        "exceptional_physical": exceptional,
        "first_split_error": abs(first_physical - centred_physical - exceptional),
        "maximum_local_error": max(local_errors, default=0.0),
        "maximum_character_error": max(char_errors, default=0.0),
        "local_values": local_values,
    }


def main() -> None:
    rows = [one_centre(7, 20), one_centre(11, 30), one_centre(13, 36)]
    for row in rows:
        assert row["product_error"] < 2e-10, row
        assert row["first_split_error"] < 2e-10, row
        assert row["maximum_local_error"] < 2e-10, row
        assert row["maximum_character_error"] < 2e-8, row

    # Exact diagonal/off-diagonal Gram check over the finite centre panel.
    centred_vectors = []
    for row in rows:
        centred_vectors.append([entry["centred"] for entry in row["local_values"]])
    direct_energy = sum(sum(v) ** 2 for v in centred_vectors)
    diagonal = sum(sum(x * x for x in v) for v in centred_vectors)
    off_diagonal = sum(
        sum(v[a] * v[b] for a in range(len(v)) for b in range(len(v)) if a != b)
        for v in centred_vectors
    )
    assert abs(direct_energy - diagonal - off_diagonal) < 2e-10

    payload = {
        "status": "PASS",
        "scope": "exact Euler detector, local prime-progression centring, character reconstruction and Gram identity",
        "rows": rows,
        "gram": {
            "direct_energy": direct_energy,
            "diagonal": diagonal,
            "off_diagonal": off_diagonal,
            "error": abs(direct_energy - diagonal - off_diagonal),
        },
        "boundary": "Finite exact identities only; the asymptotic primorial-orbit Gram estimate remains open.",
    }
    Path(__file__).with_name("euler_buchstab_first_order_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
