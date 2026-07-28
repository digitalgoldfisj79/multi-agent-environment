#!/usr/bin/env python3
"""Verify unique least-factor certificates and prime-power bounds on finite panels."""
from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from pathlib import Path

from sympy import factorint, isprime, nextprime, primerange


def primorial_to(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def one_case(z: int, H: int) -> dict:
    P = primorial_to(z)
    assert H < int(nextprime(z)) ** 2
    prime_offsets = list(map(int, primerange(z + 1, H + 1)))
    direct_prime_weight = 0.0
    total_weight = sum(1.0 + 0.05 * math.cos(p) for p in prime_offsets)
    small = 0.0
    balanced = 0.0
    type_counts: Counter[str] = Counter()
    omega_counts: Counter[int] = Counter()
    q_support = defaultdict(int)

    for p in prime_offsets:
        b = 1.0 + 0.05 * math.cos(p)
        n = P + p
        if isprime(n):
            type_counts["prime"] += 1
            direct_prime_weight += b
            continue
        fs = factorint(n)
        primes = sorted(map(int, fs))
        q = primes[0]
        k = n // q
        assert q > z
        assert q <= math.isqrt(n)
        if q * q > n:
            raise AssertionError((z, H, p, n, fs))
        if k > 1:
            least_k = min(map(int, factorint(k)))
            assert least_k >= q
        omega_counts[sum(int(e) for e in fs.values())] += 1
        if q <= H:
            type_counts["small"] += 1
            small += b
        else:
            type_counts["balanced"] += 1
            balanced += b
            q2 = math.isqrt(n)
            assert H < q <= q2
            kj = (P + q - 1) // q
            pj = q * kj - P
            assert kj == k and pj == p
            q_support[q] += 1

    error = abs(direct_prime_weight - (total_weight - small - balanced))
    assert error < 2e-10
    assert max(q_support.values(), default=0) <= 1

    proper_power_weight = 0.0
    exponents = []
    for a in range(2, int(math.log(P + H, z + 1)) + 2):
        lo = int(round(P ** (1 / a)))
        hits = []
        for r in range(max(z + 1, lo - 3), lo + 5):
            n = r ** a
            if P < n <= P + H:
                hits.append((r, n))
        assert len(hits) <= 1
        if hits:
            r, _ = hits[0]
            proper_power_weight += math.log(r)
            exponents.append(a)

    return {
        "z": z,
        "P": P,
        "H": H,
        "prime_offset_count": len(prime_offsets),
        "type_counts": dict(type_counts),
        "omega_counts": {str(k): v for k, v in sorted(omega_counts.items())},
        "weighted_identity_error": error,
        "balanced_distinct_q_count": len(q_support),
        "balanced_max_q_support_single_centre": max(q_support.values(), default=0),
        "proper_power_weight": proper_power_weight,
        "proper_power_exponents": exponents,
    }


def main() -> None:
    rows = [one_case(11, 150), one_case(13, 200), one_case(17, 350), one_case(19, 400)]
    for row in rows:
        assert row["weighted_identity_error"] < 2e-10
        assert row["balanced_max_q_support_single_centre"] <= 1
    payload = {
        "status": "PASS",
        "scope": "unique least-factor certificate and balanced one-point routing",
        "rows": rows,
        "boundary": "Finite identity verification only; balanced certificate asymptotics remain open.",
    }
    Path(__file__).with_name("balanced_least_factor_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
