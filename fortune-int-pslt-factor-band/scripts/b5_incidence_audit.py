#!/usr/bin/env python3
"""Finite incidence and asymptotic band-resolution audit."""

from __future__ import annotations

import math
from collections import Counter, defaultdict


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


def lpf(n: int) -> int:
    if n % 2 == 0:
        return 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return p
        p += 2
    return n


def primorial(ell: int) -> int:
    out = 1
    for p in primes_up_to(ell):
        out *= p
    return out


def finite_check() -> None:
    for ell in (13, 17, 19):
        pcentre = primorial(ell)
        h = int(0.7 * ell * ell)
        by_band: Counter[int] = Counter()
        large_factor_offsets: dict[int, list[int]] = defaultdict(list)
        composite_count = 0

        for m in [q for q in primes_up_to(h) if q > ell]:
            n = pcentre + m
            if is_prime(n):
                continue
            composite_count += 1
            r = lpf(n)
            band = int(math.log2(r / ell)) if r > ell else -1
            by_band[band] += 1
            if r > h:
                large_factor_offsets[r].append(m)

        assert sum(by_band.values()) == composite_count
        assert all(len(offsets) == 1 for offsets in large_factor_offsets.values())
        print(
            f"ell={ell} H={h} composite_candidates={composite_count} "
            f"occupied_bands={len(by_band)} large_factor_matches={len(large_factor_offsets)}"
        )


def asymptotic_check() -> None:
    for x in (10**2, 10**3, 10**4, 10**5, 10**6):
        log_p = 1.5 * x
        kmax = int(log_p / math.log(2.0))
        harmonic = math.fsum(1.0 / k for k in range(2, kmax + 1))
        gamma = 2.0 * harmonic
        bands = max(1.0, (0.5 * log_p - math.log(x)) / math.log(2.0))
        ratio = gamma / bands
        assert ratio < 1.0
        print(
            f"X={x} factor_bands~{bands:.8g} count_margin~{gamma:.8g} "
            f"margin_per_band={ratio:.8g}"
        )


def main() -> None:
    finite_check()
    asymptotic_check()
    print("FORTUNE_INT_PSLT_B5_CRITICAL_INCIDENCE_PASS")


if __name__ == "__main__":
    main()
