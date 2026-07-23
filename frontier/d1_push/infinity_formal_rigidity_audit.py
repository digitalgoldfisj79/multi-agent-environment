#!/usr/bin/env python3
"""Exact truncated-series audit of the formal infinity rigidity theorem.

Solve uniquely for U(z)=1+z^2 V(z) in F_p[[z]] such that

 U^p(1+a z^(p-3))
 =1+a z^(p-3)U^(p-3)+c z^(p-1)U^(p-1).

The construction is coefficient-by-coefficient.  At each step the new
coefficient occurs with invertible coefficient 3a.  No floating point or
symbolic approximation is used.
"""
from __future__ import annotations

import argparse
import json
from math import isqrt


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(x for x in range(2, p) if chi(x, p) == -1)


def series_mul(a: list[int], b: list[int], length: int, p: int) -> list[int]:
    out = [0] * length
    for i, ai in enumerate(a[:length]):
        if ai == 0:
            continue
        for j, bj in enumerate(b[: length - i]):
            if bj:
                out[i + j] = (out[i + j] + ai * bj) % p
    return out


def series_pow(a: list[int], exponent: int, length: int, p: int) -> list[int]:
    out = [0] * length
    out[0] = 1
    base = (a + [0] * length)[:length]
    e = exponent
    while e:
        if e & 1:
            out = series_mul(out, base, length, p)
        e >>= 1
        if e:
            base = series_mul(base, base, length, p)
    return out


def raw_coordinate_equation(
    v: list[int], p: int, a: int, c: int, length: int
) -> list[int]:
    """Return coefficients of equation (2.1), truncated to `length`."""
    u = [0] * length
    u[0] = 1
    for i, vi in enumerate(v):
        if i + 2 < length:
            u[i + 2] = vi % p

    # Frobenius is coefficientwise and sends z^i to z^(pi).
    up = [0] * length
    for i, ui in enumerate(u):
        if i * p < length:
            up[i * p] = ui % p

    up_minus_3 = series_pow(u, p - 3, length, p)
    up_minus_1 = series_pow(u, p - 1, length, p)

    out = [0] * length
    for i in range(length):
        out[i] = (up[i] - (1 if i == 0 else 0)) % p

    shift = p - 3
    for i in range(length - shift):
        out[i + shift] = (
            out[i + shift] + a * (up[i] - up_minus_3[i])
        ) % p

    shift = p - 1
    for i in range(length - shift):
        out[i + shift] = (out[i + shift] - c * up_minus_1[i]) % p

    return out


def solve_v(p: int, a: int, c: int, order: int) -> list[int]:
    v = [0] * order
    inverse_linear = pow((3 * a) % p, p - 2, p)
    for n in range(order):
        length = p - 1 + n + 1
        coefficient = raw_coordinate_equation(v, p, a, c, length)[p - 1 + n]
        v[n] = (-coefficient * inverse_linear) % p
    return v


def audit_case(p: int, a: int, c: int, order: int) -> dict:
    v = solve_v(p, a, c, order)
    raw = raw_coordinate_equation(v, p, a, c, p - 1 + order)
    nonzero = [i for i, coefficient in enumerate(raw) if coefficient % p]
    return {
        "p": p,
        "a": a,
        "c": c,
        "order": order,
        "v0": v[0],
        "expected_v0": (c * pow((3 * a) % p, p - 2, p)) % p,
        "odd_v_coefficients_zero": all(v[i] == 0 for i in range(1, order, 2)),
        "first_coefficients": v[: min(12, order)],
        "nonzero_equation_coefficients": nonzero[:10],
        "pass": not nonzero
        and v[0] == (c * pow((3 * a) % p, p - 2, p)) % p,
    }


def selected_c_values(p: int, exhaustive: bool) -> list[int]:
    if exhaustive:
        return list(range(p))
    return sorted({0, 1, 2 % p, 3 % p, (p - 1) % p, p // 2})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=43)
    parser.add_argument("--order-factor", type=int, default=3)
    parser.add_argument(
        "--exhaustive-through",
        type=int,
        default=43,
        help="audit every c through this prime; sample c above it",
    )
    args = parser.parse_args()

    results = []
    for p in primes_upto(args.max_prime):
        if p < 5:
            continue
        order = args.order_factor * p + 8
        for a in (1, least_nonsquare(p)):
            for c in selected_c_values(p, p <= args.exhaustive_through):
                row = audit_case(p, a, c, order)
                results.append(row)
                if not row["pass"]:
                    print(json.dumps(row), flush=True)

    output = {
        "status": "PASS" if all(row["pass"] for row in results) else "FAIL",
        "method": "exact coefficient recursion in F_p[[z]]",
        "max_prime": args.max_prime,
        "exhaustive_through": args.exhaustive_through,
        "cases": len(results),
        "max_order": max(row["order"] for row in results),
        "failures": sum(not row["pass"] for row in results),
        "all_odd_v_coefficients_zero": all(
            row["odd_v_coefficients_zero"] for row in results
        ),
        "results": results,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
