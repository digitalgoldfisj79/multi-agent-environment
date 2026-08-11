#!/usr/bin/env python3
"""Exact support audit for balanced versus unbalanced punctured-centre cells.

This verifier records the scope correction identified by the hostile Fable review:
for fixed d=d' and (d,p)=1, p | d(m-m') implies only m == m' mod p.
Equality follows only when the m interval has length below p.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def mobius(n: int) -> int:
    x = n
    count = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def panel(X: int, eta_num: int = 4, eta_den: int = 5) -> dict:
    H = eta_num * X * X // eta_den
    Y = math.isqrt(H)
    if Y * Y < H:
        Y += 1

    primes = primes_upto(max(H, 4 * X))
    z_values = [p for p in primes if X <= p < 2 * X]
    K = max(1, min(len(z_values), math.ceil(math.log(X))))
    z_values = z_values[:K]
    Z = z_values[-1]
    band = [p for p in primes if Z < p <= min(2 * Z, H)]
    small = [d for d in range(1, Y + 1) if mobius(d)]

    balanced_collisions = 0
    unbalanced_collisions = 0
    first_unbalanced_collision = None
    long_range_multiples_of_band_primes = 0

    for p in band:
        for d in small:
            assert math.gcd(d, p) == 1

            # On the committed balanced slice m,m' <= Y < p, congruence forces equality.
            for m in range(1, Y + 1):
                balanced_collisions += max(0, (Y - m) // p)

            # On the true source range m,m' <= H/d, distinct pairs m'=m+kp occur.
            top = H // d
            long_range_multiples_of_band_primes += top // p
            if top > p:
                for m in range(1, top + 1):
                    count = (top - m) // p
                    unbalanced_collisions += count
                    if count and first_unbalanced_collision is None:
                        first_unbalanced_collision = {
                            "p": p,
                            "d": d,
                            "m": m,
                            "m_prime": m + p,
                            "top": top,
                        }

    assert balanced_collisions == 0
    assert unbalanced_collisions > 0
    assert first_unbalanced_collision is not None

    example = first_unbalanced_collision
    assert example["m"] != example["m_prime"]
    assert example["m_prime"] <= example["top"]
    assert example["d"] * (example["m"] - example["m_prime"]) % example["p"] == 0

    return {
        "X": X,
        "H": H,
        "Y": Y,
        "K": K,
        "Z": Z,
        "band_moduli": band,
        "small_mobius_count": len(small),
        "balanced_one_variable_collision_count": balanced_collisions,
        "unbalanced_one_variable_collision_count": unbalanced_collisions,
        "first_unbalanced_collision": first_unbalanced_collision,
        "long_range_multiples_of_band_primes": long_range_multiples_of_band_primes,
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact_scope": [
            "one-variable collision collapse on intervals shorter than p",
            "failure of the unscoped collapse on the true ranges m <= H/d",
            "existence of non-unit long-source terms p divides m",
        ],
        "panels": [panel(X) for X in (11, 17, 23, 29, 37)],
        "boundary": (
            "The balanced collision collapse is exact only on source intervals shorter than p. "
            "True unbalanced cells contain distinct congruent pairs m'=m+kp and multiples of p. "
            "They require exact residue completion and a separate dual-kernel ledger."
        ),
    }
    output = Path(__file__).with_name("punctured_centre_unbalanced_support_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
