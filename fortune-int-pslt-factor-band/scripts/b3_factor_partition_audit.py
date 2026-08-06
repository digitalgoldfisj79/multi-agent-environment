#!/usr/bin/env python3
"""Finite exact verifier for the least-prime-factor partition."""

from __future__ import annotations

import math
from collections import Counter


def primes_up_to(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = [False] * (((n - p * p) // p) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            return n == p
    return True


def least_prime_factor(n: int) -> int:
    if n % 2 == 0:
        return 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return p
        p += 2
    return n


def primorial(ell: int) -> int:
    value = 1
    for p in primes_up_to(ell):
        value *= p
    return value


def main() -> None:
    for ell in (11, 13, 17, 19):
        pcentre = primorial(ell)
        h = int(0.6 * ell * ell)
        candidates = [m for m in primes_up_to(h) if m > ell]
        prime_outputs = 0
        factors: Counter[int] = Counter()

        for m in candidates:
            output = pcentre + m
            if is_prime(output):
                prime_outputs += 1
            else:
                r = least_prime_factor(output)
                assert r > ell
                assert r <= math.isqrt(output)
                factors[r] += 1

        assert len(candidates) == prime_outputs + sum(factors.values())
        assert ell > math.sqrt(h)
        print(
            f"ell={ell} H={h} candidates={len(candidates)} "
            f"prime_outputs={prime_outputs} composite_outputs={sum(factors.values())} "
            f"distinct_least_factors={len(factors)}"
        )

    print("FORTUNE_INT_PSLT_B3_LEAST_FACTOR_PARTITION_PASS")


if __name__ == "__main__":
    main()
