#!/usr/bin/env python3
"""Exact audit for NONSPLIT_K3_CM40_THEOREM.md.

For every prime in the requested range:
  1. compute U1(p)=sum_{q,r} chi(r q [r(r-q-3)^2-(q-2)^2]);
  2. compute the CM coefficient of discriminant -40 from the two reduced
     binary quadratic forms x^2+10y^2 and 2x^2+5y^2;
  3. verify U1(p)=2 chi_p(2) p+a_p(f_-40).

Integer modular arithmetic only. No floating point or fitting.
"""
from __future__ import annotations

import argparse
import json
from math import isqrt


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
    return [i for i, value in enumerate(sieve) if value]


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def f_qr(q: int, r: int, p: int) -> int:
    return (r * (r - q - 3) ** 2 - (q - 2) ** 2) % p


def u1_direct(p: int) -> int:
    return sum(
        chi(r * q * f_qr(q, r, p), p)
        for q in range(p)
        for r in range(p)
    )


def ap_cm40(p: int) -> tuple[int, str, tuple[int, int] | None]:
    """Return (a_p, representing form, (x,y)).  Assumes p>5 prime."""
    if chi(-10, p) == -1:
        return 0, "inert", None

    candidates: list[tuple[int, str, tuple[int, int]]] = []
    for x in range(isqrt(p) + 1):
        for y in range(isqrt(p // 5) + 2):
            if x * x + 10 * y * y == p:
                base = 2 * (x * x - 10 * y * y)
                candidates.append((chi(2, p) * base, "x^2+10y^2", (x, y)))
            if 2 * x * x + 5 * y * y == p:
                base = 2 * (2 * x * x - 5 * y * y)
                candidates.append((chi(2, p) * base, "2x^2+5y^2", (x, y)))

    if not candidates:
        raise AssertionError(f"split prime {p} has no discriminant-40 representation")
    values = {row[0] for row in candidates}
    if len(values) != 1:
        raise AssertionError((p, candidates))
    return candidates[0]


def audit_prime(p: int) -> dict[str, object]:
    u1 = u1_direct(p)
    ap, form, representation = ap_cm40(p)
    prediction = 2 * chi(2, p) * p + ap
    return {
        "p": p,
        "chi2": chi(2, p),
        "chi_minus10": chi(-10, p),
        "U1": u1,
        "a_p_cm40": ap,
        "form": form,
        "representation": representation,
        "prediction": prediction,
        "pass": u1 == prediction,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=499)
    parser.add_argument("--output")
    args = parser.parse_args()

    rows = [audit_prime(p) for p in primes_upto(args.max_prime) if p >= 7]
    result = {
        "status": "PASS" if all(bool(row["pass"]) for row in rows) else "FAIL",
        "method": "Exact exhaustive F_p character sums and exact binary quadratic forms; no floating point.",
        "prime_count": len(rows),
        "max_prime": max((int(row["p"]) for row in rows), default=None),
        "all_checks_pass": all(bool(row["pass"]) for row in rows),
        "inert_zero_checks_pass": all(
            int(row["a_p_cm40"]) == 0
            for row in rows
            if int(row["chi_minus10"]) == -1
        ),
        "rows": rows,
    }
    text = json.dumps(result, indent=2) + "\n"
    print(text, end="")
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)


if __name__ == "__main__":
    main()
