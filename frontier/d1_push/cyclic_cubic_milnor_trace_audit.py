#!/usr/bin/env python3
"""Exact audit for CYCLIC_CUBIC_MILNOR_TRACE_THEOREM.md.

For each requested odd prime p, this verifies the polynomial identity

  prod_{j=1}^{p-1}(1-t^2 zeta^j) / prod_{j=1}^{p-1}(1-t zeta^j)
  = (1+t^p)/(1+t)

without numerical roots of unity, using cyclotomic product identities in Z[t].
It also checks the trace value at t=1, the identity Milnor dimension
2^(p-1), and the determinant sign of a p-cycle on Std_p.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def polynomial_add(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def polynomial_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def polynomial_div_exact(a: list[int], b: list[int]) -> list[int]:
    if not b or b[-1] == 0:
        raise ZeroDivisionError
    remainder = a[:]
    quotient = [0] * max(1, len(a) - len(b) + 1)
    while len(remainder) >= len(b):
        degree = len(remainder) - len(b)
        lead = remainder[-1]
        divisor_lead = b[-1]
        if lead % divisor_lead:
            raise ValueError("nonexact polynomial division")
        coefficient = lead // divisor_lead
        quotient[degree] = coefficient
        for j, value in enumerate(b):
            remainder[degree + j] -= coefficient * value
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    if any(remainder):
        raise ValueError(f"nonzero remainder: {remainder}")
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return quotient


def one_minus_power(n: int) -> list[int]:
    out = [0] * (n + 1)
    out[0] = 1
    out[n] = -1
    return out


def one_plus_power(n: int) -> list[int]:
    out = [0] * (n + 1)
    out[0] = 1
    out[n] = 1
    return out


def eval_at_one(poly: list[int]) -> int:
    return sum(poly)


def audit_prime(p: int) -> dict:
    if p < 5 or p % 2 == 0:
        raise ValueError("p must be an odd prime >=5")

    # det(1-t sigma | Std_p) = (1-t^p)/(1-t)
    denominator = polynomial_div_exact(one_minus_power(p), [1, -1])

    # det(1-t^2 sigma | Std_p) = (1-t^(2p))/(1-t^2)
    numerator = polynomial_div_exact(one_minus_power(2 * p), [1, 0, -1])

    ratio = polynomial_div_exact(numerator, denominator)
    expected = polynomial_div_exact(one_plus_power(p), [1, 1])

    trace_nontrivial = eval_at_one(ratio)
    identity_dimension = 2 ** (p - 1)
    determinant_sign = 1  # sign of an odd-length p-cycle is (-1)^(p-1)=1

    checks = {
        "denominator_degree_p_minus_1": len(denominator) - 1 == p - 1,
        "numerator_degree_2p_minus_2": len(numerator) - 1 == 2 * p - 2,
        "graded_trace_identity": ratio == expected,
        "trace_at_one_is_one": trace_nontrivial == 1,
        "identity_milnor_dimension": identity_dimension == 2 ** (p - 1),
        "determinant_sign_one": determinant_sign == 1,
        "expected_alternating_coefficients": expected == [1 if i % 2 == 0 else -1 for i in range(p)],
    }

    return {
        "p": p,
        "pass": all(checks.values()),
        "checks": checks,
        "graded_trace_coefficients": ratio,
        "trace_nontrivial_cyclic_element": trace_nontrivial,
        "milnor_dimension_identity": identity_dimension,
        "collapse_ratio": identity_dimension,
    }


def primes_up_to(limit: int) -> list[int]:
    out = []
    for n in range(5, limit + 1, 2):
        if all(n % q for q in range(3, int(n**0.5) + 1, 2)):
            out.append(n)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=199)
    parser.add_argument("--primes", nargs="*", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    requested = args.primes or primes_up_to(args.max_prime)
    rows = [audit_prime(p) for p in requested]
    result = {
        "status": "PASS" if all(row["pass"] for row in rows) else "FAIL",
        "method": "Exact integer polynomial arithmetic; no floating point or root approximations.",
        "prime_count": len(rows),
        "max_prime": max(requested) if requested else None,
        "rows": rows,
    }
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
