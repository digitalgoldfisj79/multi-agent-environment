#!/usr/bin/env python3
"""Deterministic certificate for the RUHL-FM truncation budget."""

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
) -> int:
    """Find the first integer M where the registered three-term bound is < 1/M."""
    alpha = exponent(epsilon, ratio, beta)
    for m in range(2, limit + 1):
        model = m ** (-(1.0 + 3.0 * epsilon))
        tail = m ** (-alpha)
        aggregate_error = m ** (-(1.0 + 2.0 * epsilon))
        if model + tail + aggregate_error < 1.0 / m:
            return m
    raise RuntimeError(f"no margin crossing found up to M={limit}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon", type=float, default=0.10)
    parser.add_argument("--ratio", type=float, default=1.10)
    parser.add_argument("--beta", type=float, default=5.0)
    args = parser.parse_args()

    if args.epsilon <= 0:
        raise SystemExit("epsilon must be positive")
    if args.ratio < 1:
        raise SystemExit("ratio must be at least one")
    if args.beta <= 0:
        raise SystemExit("beta must be positive")

    alpha = exponent(args.epsilon, args.ratio, args.beta)
    target = 1.0 + 2.0 * args.epsilon
    first = first_margin_scale(args.epsilon, args.ratio, args.beta)

    print(f"epsilon={args.epsilon:.12g}")
    print(f"U/L ratio={args.ratio:.12g}")
    print(f"beta={args.beta:.12g}")
    print(f"tail exponent alpha={alpha:.12f}")
    print(f"required exponent={target:.12f}")
    print(f"exponent gate={'PASS' if alpha >= target else 'FAIL'}")
    print(f"first M=n_b*B with registered total margin PASS: {first}")

    if alpha < target:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
