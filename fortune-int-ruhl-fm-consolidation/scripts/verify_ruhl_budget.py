#!/usr/bin/env python3
"""Deterministic certificate for the RUHL-FM truncation budget.

The asymptotic exponent gate is authoritative.  The finite crossing search is
only a diagnostic and may legitimately lie beyond the configured cap.
"""

from __future__ import annotations

import argparse
import math


def exponent(epsilon: float, ratio: float, beta: float) -> float:
    """Return beta*log(beta/(e*(1+3 epsilon)*ratio))."""
    scale = math.e * (1.0 + 3.0 * epsilon) * ratio
    if beta <= scale:
        raise ValueError(
            "beta must exceed e*(1+3*epsilon)*ratio for a decaying bound"
        )
    return beta * math.log(beta / scale)


def first_margin_scale(
    epsilon: float, ratio: float, beta: float, limit: int = 10_000_000
) -> int | None:
    """Return the first tested integer M with the registered margin, if found.

    Failure to find a crossing below ``limit`` is not failure of an asymptotic
    certificate.  It is reported as ``None`` and the exponent gate remains the
    pass/fail criterion.
    """
    alpha = exponent(epsilon, ratio, beta)
    for m in range(2, limit + 1):
        model = m ** (-(1.0 + 3.0 * epsilon))
        tail = m ** (-alpha)
        aggregate_error = m ** (-(1.0 + 2.0 * epsilon))
        if model + tail + aggregate_error < 1.0 / m:
            return m
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon", type=float, default=0.10)
    parser.add_argument("--ratio", type=float, default=1.10)
    parser.add_argument("--beta", type=float, default=5.0)
    parser.add_argument("--diagnostic-limit", type=int, default=10_000_000)
    args = parser.parse_args()

    if args.epsilon <= 0:
        raise SystemExit("epsilon must be positive")
    if args.ratio < 1:
        raise SystemExit("ratio must be at least one")
    if args.beta <= 0:
        raise SystemExit("beta must be positive")
    if args.diagnostic_limit < 2:
        raise SystemExit("diagnostic limit must be at least two")

    alpha = exponent(args.epsilon, args.ratio, args.beta)
    target = 1.0 + 2.0 * args.epsilon
    exponent_pass = alpha >= target
    first = first_margin_scale(
        args.epsilon, args.ratio, args.beta, args.diagnostic_limit
    )

    print(f"epsilon={args.epsilon:.12g}")
    print(f"U/L ratio={args.ratio:.12g}")
    print(f"beta={args.beta:.12g}")
    print(f"tail exponent alpha={alpha:.12f}")
    print(f"required exponent={target:.12f}")
    print(f"exponent gate={'PASS' if exponent_pass else 'FAIL'}")
    if first is None:
        print(
            "finite margin crossing not found within diagnostic cap "
            f"M={args.diagnostic_limit}; asymptotic exponent gate is authoritative"
        )
    else:
        print(f"first tested M=n_b*B with registered total margin PASS: {first}")

    if not exponent_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
