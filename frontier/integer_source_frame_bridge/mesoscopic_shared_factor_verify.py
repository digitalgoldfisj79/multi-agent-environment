#!/usr/bin/env python3
"""Verify shared-factor transport and reciprocal bounds on finite mesoscopic panels."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import factorint, primerange


def prime_sieve(n: int) -> list[int]:
    return list(map(int, primerange(2, n + 1)))


def panel(X: int, eta: float = 0.8) -> dict:
    H = int(eta * X * X)
    primes = prime_sieve(H)
    block_primes = [p for p in primes if X <= p < 2 * X]
    K = max(1, math.isqrt(X))
    local_z = block_primes[:K]
    zB = local_z[-1]

    P = 1
    for p in primes:
        if p > local_z[0]:
            break
        P *= p
    centres = [P]
    current = P
    for z in local_z[1:]:
        current *= z
        centres.append(current)

    candidates = [p for p in primes if zB < p <= H]
    if len(candidates) > 12:
        indices = sorted(set([0, 1, 2, len(candidates)//3, len(candidates)//2,
                              2*len(candidates)//3, len(candidates)-3,
                              len(candidates)-2, len(candidates)-1]))
        offsets = [candidates[i] for i in indices]
    else:
        offsets = candidates

    checked = 0
    maximum_count_ratio = 0.0
    maximum_reciprocal_ratio = 0.0
    maximum_transport_error = 0
    minimum_gap = None

    for j in range(len(centres)):
        Q = 1
        for k in range(j + 1, len(centres)):
            Q *= local_z[k]
            h = k - j
            for m in offsets:
                for n in offsets:
                    transported = n - Q * m
                    assert transported != 0
                    minimum_gap = abs(transported) if minimum_gap is None else min(minimum_gap, abs(transported))
                    g = math.gcd(centres[j] + m, centres[k] + n)
                    shared = [int(r) for r in factorint(g) if int(r) > zB]
                    for r in shared:
                        maximum_transport_error = max(maximum_transport_error, transported % r)
                        assert transported % r == 0
                    count_bound = math.log(abs(transported)) / math.log(zB)
                    reciprocal = math.fsum(1 / r for r in shared)
                    assert len(shared) <= count_bound + 1e-12
                    assert reciprocal <= len(shared) / zB + 1e-15
                    if count_bound:
                        maximum_count_ratio = max(maximum_count_ratio, len(shared) / count_bound)
                    explicit_reciprocal_bound = count_bound / zB
                    if explicit_reciprocal_bound:
                        maximum_reciprocal_ratio = max(
                            maximum_reciprocal_ratio,
                            reciprocal / explicit_reciprocal_bound,
                        )
                    # The theorem's simpler O(h+1) scale.
                    coarse = (h * math.log(2 * X) + math.log(H) + 1) / math.log(X)
                    assert len(shared) <= coarse + 1e-12
                    checked += 1

    return {
        "X": X,
        "H": H,
        "K": K,
        "z_B": zB,
        "offset_sample_size": len(offsets),
        "checked_tuples": checked,
        "minimum_transported_gap": minimum_gap,
        "maximum_transport_error": maximum_transport_error,
        "maximum_count_to_log_bound_ratio": maximum_count_ratio,
        "maximum_reciprocal_to_log_bound_ratio": maximum_reciprocal_ratio,
    }


def main() -> None:
    panels = [panel(X) for X in (31, 53, 101)]
    for row in panels:
        assert row["maximum_transport_error"] == 0
        assert row["minimum_transported_gap"] > 0
        assert row["maximum_count_to_log_bound_ratio"] <= 1 + 1e-12
        assert row["maximum_reciprocal_to_log_bound_ratio"] <= 1 + 1e-12
    payload = {
        "status": "PASS",
        "scope": "shared-factor transport, nonvanishing, prime-count and reciprocal-mass bounds",
        "panels": panels,
        "boundary": "Finite sampled verification only; coherent summation over all source offset pairs remains open.",
    }
    output = Path(__file__).with_name("mesoscopic_shared_factor_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
