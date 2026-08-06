#!/usr/bin/env python3
"""Finite diagnostic for the M5 prime-divisor-band main coefficient."""
from __future__ import annotations

import math


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def main() -> None:
    epsilon = 0.08
    delta = 1 / 3 - epsilon
    for x in (200, 500, 1000, 3000, 10000):
        qmax = int(x ** (1 + delta))
        primes = primes_upto(qmax)
        value = sum(math.log(q) / (q - 1) for q in primes if 2 * x < q <= qmax)
        ratio = value / math.log(x)
        print(
            f"X={x} Q={qmax} target_delta={delta:.8g} "
            f"band_ratio={ratio:.8g}"
        )
        assert value >= 0
    print("FORTUNE_INT_SCME_M5_DIVISOR_BAND_DIAGNOSTIC_COMPLETE")


if __name__ == "__main__":
    main()
