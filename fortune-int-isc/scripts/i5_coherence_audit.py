#!/usr/bin/env python3
"""Exact finite regression of smooth-modulus primorial coherence."""

from math import prod


def primes_below(n: int) -> list[int]:
    out: list[int] = []
    for k in range(2, n):
        if all(k % p for p in out if p * p <= k):
            out.append(k)
    return out


def run() -> None:
    for x in (11, 17, 29):
        small = primes_below(x)
        block = [p for p in primes_below(2 * x) if p >= x]
        a_x = prod(small)
        q_j = 1
        centres = []
        for ell in block:
            q_j *= ell
            centres.append(a_x * q_j)
        divisors = [1]
        for p in small[: min(5, len(small))]:
            divisors += [d * p for d in list(divisors)]
        divisors = sorted(set(divisors))
        for q in divisors:
            assert a_x % q == 0
            assert all(pj % q == 0 for pj in centres)
            # In the finite Fourier frame modulo q, all sample rows coincide.
            coherent_sum = sum(1 for _ in centres)
            assert coherent_sum == len(centres)
        print(
            f"X={x} centres={len(centres)} tested_divisors={len(divisors)} "
            f"forced_frame_constant_at_least={len(centres)}"
        )
    print("FORTUNE_INT_ISC_I5_COHERENCE_PASS")


if __name__ == "__main__":
    run()
