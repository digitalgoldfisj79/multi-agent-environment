#!/usr/bin/env python3
"""Exact cubic-slice count and first-c-moment scanner.

For primes p == 5 (mod 6), and representatives of the two square classes of
nonzero a, count irreducible polynomials

    X^p + a X^3 + c X + d

over F_p and compute M_a = sum_irr c mod p.

Correctness architecture:
* d -> -d halves the exact search; d=0 is reducible.
* the root-image test rejects only fibres with an exhibited F_p root.
* Frobenius-iterate gcd tests reject only fibres with an exhibited proper
  factor of degree dividing k, 2 <= k <= cutoff.
* every survivor is fully factored by python-flint, so neither prefilter can
  create a false irreducible.
"""

from __future__ import annotations

import argparse
import json
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from math import isqrt

from flint import nmod_poly


def primes_5_mod_6(lo: int, hi: int) -> list[int]:
    return [
        n
        for n in range(lo, hi + 1)
        if n % 6 == 5 and all(n % d for d in range(2, isqrt(n) + 1))
    ]


def quadratic_character(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def smallest_nonsquare(p: int) -> int:
    return next(a for a in range(2, p) if quadratic_character(a, p) == -1)


def scan_class(task: tuple[int, int, int]) -> dict[str, int]:
    p, a, cutoff = task
    count = 0
    moment = 0
    rootless_half = 0
    prefiltered = 0
    factored = 0
    x = nmod_poly([0, 1], p)

    for c in range(p):
        # A root z in F_p satisfies d = -(a z^3 + (c+1)z).
        root_values = {(a * z * z * z + (c + 1) * z) % p for z in range(p)}
        for d in range(1, (p + 1) // 2):
            if (-d) % p in root_values:
                continue

            rootless_half += 1
            f = nmod_poly([d, c, 0, a] + [0] * (p - 4) + [1], p)

            # x^p == -(a x^3 + c x + d) mod f.
            frob_image = nmod_poly([-d, -c, 0, -a], p)
            h = frob_image
            reducible = False
            for _k in range(2, cutoff + 1):
                h = h.compose_mod(frob_image, f)
                if (h - x).gcd(f).degree() > 0:
                    reducible = True
                    prefiltered += 1
                    break
            if reducible:
                continue

            factored += 1
            factors = f.factor()[1]
            irreducible = (
                len(factors) == 1
                and factors[0][1] == 1
                and factors[0][0].degree() == p
            )
            if irreducible:
                count += 2
                moment = (moment + 2 * c) % p

    return {
        "p": p,
        "a": a,
        "class": quadratic_character(a, p),
        "N": count,
        "M": moment,
        "rootless_half": rootless_half,
        "prefiltered": prefiltered,
        "factored": factored,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lo", type=int, default=383)
    parser.add_argument("--hi", type=int, default=683)
    parser.add_argument("--cutoff", type=int, default=12)
    parser.add_argument("--workers", type=int, default=min(16, os.cpu_count() or 8))
    parser.add_argument("--output", default="")
    args = parser.parse_args()

    primes = primes_5_mod_6(args.lo, args.hi)
    tasks = [
        (p, a, args.cutoff)
        for p in primes
        for a in (1, smallest_nonsquare(p))
    ]

    rows: list[dict[str, int]] = []
    with ProcessPoolExecutor(max_workers=min(args.workers, len(tasks))) as executor:
        futures = [executor.submit(scan_class, task) for task in tasks]
        for future in as_completed(futures):
            row = future.result()
            rows.append(row)
            print("ROW", json.dumps(row, sort_keys=True), flush=True)

    by_prime: dict[int, dict[str, dict[str, int]]] = {}
    for row in rows:
        sign = "+" if row["class"] == 1 else "-"
        by_prime.setdefault(row["p"], {})[sign] = row

    output = {str(p): by_prime[p] for p in sorted(by_prime)}
    for p in sorted(by_prime):
        plus = by_prime[p]["+"]
        minus = by_prime[p]["-"]
        mode = "difference" if p % 12 == 5 else "sum"
        active = (
            (plus["N"] - minus["N"]) % p
            if mode == "difference"
            else (plus["N"] + minus["N"]) % p
        )
        print(
            "PAIR",
            p,
            plus["N"],
            minus["N"],
            "M",
            plus["M"],
            minus["M"],
            "mode",
            mode,
            active,
            flush=True,
        )

    payload = json.dumps(output, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(payload + "\n")
    else:
        print(payload)


if __name__ == "__main__":
    main()
