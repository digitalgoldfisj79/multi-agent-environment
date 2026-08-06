#!/usr/bin/env python3
"""Small exact output profiles for the divisor-band/parity-tail decomposition.

Diagnostic only. No finite panel is promoted.
"""
from __future__ import annotations

import argparse
import math
from sympy import isprime, primerange


def primorial_to(p: int) -> int:
    value = 1
    for q in primerange(2, p + 1):
        value *= int(q)
    return value


def von_mangoldt_near_primorial(n: int) -> float:
    if isprime(n):
        return math.log(n)
    root = math.isqrt(n)
    if root * root == n and isprime(root):
        return math.log(root)
    return 0.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=40)
    parser.add_argument("--epsilon", type=float, default=0.08)
    args = parser.parse_args()

    x = args.x
    h = x * x // 2
    upper = 2 * x
    qmax = int(x ** (4 / 3 - args.epsilon))
    rows = list(primerange(x, 2 * x))
    candidates = list(primerange(upper + 1, h + 1))
    band_primes = list(primerange(2 * x + 1, qmax + 1))

    prime_outputs = 0
    band_composites = 0
    no_band_composites = 0
    total_lambda = 0.0
    total_band = 0.0

    for ell in rows:
        centre = primorial_to(int(ell))
        for m in candidates:
            n = centre + int(m)
            weight = math.log(int(m))
            lam = von_mangoldt_near_primorial(n)
            band = sum(math.log(q) for q in band_primes if n % q == 0)
            total_lambda += weight * lam
            total_band += weight * band
            if isprime(n):
                prime_outputs += 1
                assert band == 0.0
            elif band > 0:
                band_composites += 1
            else:
                no_band_composites += 1

    tail = total_lambda - total_band
    print(
        f"X={x} rows={len(rows)} candidates={len(candidates)} Q={qmax} "
        f"prime_outputs={prime_outputs} band_composites={band_composites} "
        f"no_band_composites={no_band_composites}"
    )
    print(
        f"weighted_lambda={total_lambda:.12g} weighted_band={total_band:.12g} "
        f"weighted_tail={tail:.12g} identity_error={total_lambda-(total_band+tail):.3g}"
    )
    assert abs(total_lambda - (total_band + tail)) < 1e-8
    print("FORTUNE_INT_SCME_M8_FACTOR_PROFILE_DIAGNOSTIC_COMPLETE")


if __name__ == "__main__":
    main()
