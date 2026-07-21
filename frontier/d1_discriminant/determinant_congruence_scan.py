#!/usr/bin/env python3
"""Scan the exact irreducible slice counts modulo p.

Requires python-flint.

For each odd prime p in a requested range, the script counts irreducible
polynomials

    X^p + a X^3 + c X + d

for one square and one nonsquare value of a. Counts depend only on the square
class of a. It records N_a(p) mod p, which is the canonical top coefficient of
the exact Frobenius determinant indicator divided by 3a.

The local cubic rootless condition is used as an exact prefilter: an
irreducible member cannot have a root in F_p, and on F_p the degree-p family
agrees with its local cubic tail.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from math import isqrt

from flint import nmod_poly


def primes_between(lo: int, hi: int) -> list[int]:
    return [
        m
        for m in range(max(2, lo), hi + 1)
        if all(m % d for d in range(2, isqrt(m) + 1))
    ]


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(x for x in range(2, p) if chi(x, p) < 0)


def is_irreducible(p: int, a: int, c: int, d: int) -> bool:
    coefficients = [0] * (p + 1)
    coefficients[0] = d % p
    coefficients[1] = c % p
    coefficients[3] = a % p
    coefficients[p] = 1
    _, factors = nmod_poly(coefficients, p).factor()
    return (
        len(factors) == 1
        and factors[0][0].degree() == p
        and factors[0][1] == 1
    )


def count_slice(task: tuple[int, int]) -> dict[str, int | float]:
    p, a = task
    started = time.time()
    count = 0
    tested = 0
    cubes = [(x * x % p) * x % p for x in range(p)]

    for c in range(p):
        forbidden_d = {
            (-a * cubes[x] - (c + 1) * x) % p
            for x in range(p)
        }
        for d in range(1, p):
            if d in forbidden_d:
                continue
            tested += 1
            count += int(is_irreducible(p, a, c, d))

    return {
        "p": p,
        "a": a,
        "chi_a": chi(a, p),
        "count": count,
        "residue": count % p,
        "tested": tested,
        "seconds": time.time() - started,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lo", type=int, default=5)
    parser.add_argument("--hi", type=int, default=199)
    parser.add_argument("--workers", type=int, default=os.cpu_count() or 8)
    args = parser.parse_args()

    primes = [p for p in primes_between(args.lo, args.hi) if p >= 5]
    tasks: list[tuple[int, int]] = []
    for p in primes:
        tasks.extend([(p, 1), (p, least_nonsquare(p))])

    rows: list[dict[str, int | float]] = []
    with ProcessPoolExecutor(max_workers=min(args.workers, len(tasks))) as pool:
        futures = {pool.submit(count_slice, task): task for task in tasks}
        for future in as_completed(futures):
            row = future.result()
            rows.append(row)
            print("ROW", json.dumps(row), flush=True)

    rows.sort(key=lambda row: (row["p"], row["chi_a"]))
    grouped: dict[int, list[dict[str, int | float]]] = {}
    for row in rows:
        grouped.setdefault(int(row["p"]), []).append(row)

    both_zero: list[int] = []
    one_zero: list[tuple[int, int]] = []
    for p, prime_rows in sorted(grouped.items()):
        zero_classes = [
            int(row["chi_a"])
            for row in prime_rows
            if int(row["residue"]) == 0
        ]
        if len(zero_classes) == 2:
            both_zero.append(p)
        elif len(zero_classes) == 1:
            one_zero.append((p, zero_classes[0]))

    summary = {
        "lo": args.lo,
        "hi": args.hi,
        "prime_count": len(primes),
        "both_zero": both_zero,
        "one_zero": one_zero,
        "rows": rows,
    }
    print("SUMMARY", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
