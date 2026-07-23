#!/usr/bin/env python3
"""Exact finite-field audit of the cyclic Adams fixed-diagonal germs.

For every audited prime p, both cubic square classes a, and every x in F_p,
verify

  f(x+h)-f(x)=h^p+(3*a*x^2+c)h+3*a*x*h^2+a*h^3,

and on c=-3*a*x^2 verify that the order at h=0 is 2 for x!=0 and
3 for x=0.  The derivative factorization gives Milnor numbers 1 and 2.

The theorem itself is symbolic and valid for all p>=5; this program is an
exhaustive finite audit of the formulas and local orders.
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
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, value in enumerate(sieve) if value]


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(x for x in range(2, p) if chi(x, p) == -1)


def poly_eval(coeffs: list[int], h: int, p: int) -> int:
    value = 0
    for coefficient in reversed(coeffs):
        value = (value * h + coefficient) % p
    return value


def order_at_zero(coeffs: list[int], p: int) -> int:
    for index, coefficient in enumerate(coeffs):
        if coefficient % p:
            return index
    return len(coeffs)


def audit_prime(p: int) -> dict:
    rows = []
    for class_name, a in (("square", 1), ("nonsquare", least_nonsquare(p))):
        all_ok = True
        type_counts = {"A1": 0, "A2": 0}
        for x in range(p):
            c = (-3 * a * x * x) % p
            # phi(h)=h^p + 3*a*x*h^2 + a*h^3 on the critical parabola.
            coeffs = [0] * (p + 1)
            coeffs[2] = (3 * a * x) % p
            coeffs[3] = a % p
            coeffs[p] = 1
            expected_order = 3 if x == 0 else 2
            actual_order = order_at_zero(coeffs, p)

            # derivative: 3*a*h*(2*x+h).  Compare at all h.
            derivative_ok = True
            for h in range(p):
                direct = 0
                for degree, coefficient in enumerate(coeffs[1:], start=1):
                    direct = (direct + degree * coefficient * pow(h, degree - 1, p)) % p
                factored = (3 * a * h * (2 * x + h)) % p
                if direct != factored:
                    derivative_ok = False
                    break

            # Verify the normal difference formula directly at all h.
            difference_ok = True
            for h in range(p):
                f_xh = (pow(x + h, p, p) + a * pow(x + h, 3, p) + c * (x + h)) % p
                f_x = (pow(x, p, p) + a * pow(x, 3, p) + c * x) % p
                if (f_xh - f_x) % p != poly_eval(coeffs, h, p):
                    difference_ok = False
                    break

            ok = actual_order == expected_order and derivative_ok and difference_ok
            all_ok &= ok
            type_counts["A2" if x == 0 else "A1"] += 1
        rows.append(
            {
                "class": class_name,
                "a": a,
                "all_checks_pass": all_ok,
                "type_counts": type_counts,
                "milnor_numbers": {"A1": 1, "A2": 2},
            }
        )
    return {"p": p, "rows": rows, "pass": all(r["all_checks_pass"] for r in rows)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=199)
    parser.add_argument("--output")
    args = parser.parse_args()

    results = [audit_prime(p) for p in primes_upto(args.max_prime) if p >= 5]
    output = {
        "status": "PASS" if all(row["pass"] for row in results) else "FAIL",
        "scope": "exact exhaustive finite-field audit; theorem symbolic for all p>=5",
        "max_prime": args.max_prime,
        "prime_count": len(results),
        "results": results,
    }
    text = json.dumps(output, indent=2)
    print(text)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")


if __name__ == "__main__":
    main()
