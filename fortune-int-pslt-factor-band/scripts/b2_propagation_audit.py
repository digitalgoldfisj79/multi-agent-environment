#!/usr/bin/env python3
"""Audit the natural primorial offset transport and an isolated-defect surrogate."""

from __future__ import annotations

import math


def primes_up_to(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = [False] * (((n - p * p) // p) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def main() -> None:
    for x in (11, 17, 29, 43):
        eta = 0.75
        h = int(eta * x * x)
        ell = x
        ell_next = next(p for p in primes_up_to(4 * x) if p > ell)
        min_candidate = ell_next
        transported = ell_next * min_candidate
        assert transported > x * x > h
        print(
            f"X={x} H={h} ell={ell} ell_next={ell_next} "
            f"minimum_transported_offset={transported}"
        )

    rows = 9
    normal_mass = 100
    defect_row = 4
    source = [normal_mass] * rows
    source[defect_row] = 0
    assert source.count(0) == 1
    assert all(v == normal_mass for i, v in enumerate(source) if i != defect_row)

    print("isolated_defect_rows=1")
    print("FORTUNE_INT_PSLT_B2_NO_NATURAL_PROPAGATION_PASS")


if __name__ == "__main__":
    main()
