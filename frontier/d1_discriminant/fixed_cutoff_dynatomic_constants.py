#!/usr/bin/env python3
"""Constants for the fixed-cutoff dynatomic sieve.

For a fixed cutoff K the positive and negative discriminant sectors rough
through K have main-term density

    (1/6) product_{k=2}^K E_k,

where E_k=sum_{j=0}^{r_k}(-1/k)^j/j! and r_k is the number of generic
period-k cycles of a cubic polynomial.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


def divisors(n: int) -> list[int]:
    out: list[int] = []
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def mobius(n: int) -> int:
    value = n
    factors = 0
    q = 2
    while q * q <= value:
        if value % q == 0:
            value //= q
            factors += 1
            if value % q == 0:
                return 0
            while value % q == 0:
                value //= q
        q += 1
    if value > 1:
        factors += 1
    return -1 if factors % 2 else 1


def cycle_count(k: int) -> int:
    return sum(3**d * mobius(k // d) for d in divisors(k)) // k


def exact_e(k: int) -> Fraction:
    r = cycle_count(k)
    total = Fraction(0, 1)
    term = Fraction(1, 1)
    for j in range(r + 1):
        if j:
            term *= Fraction(-1, k * j)
        total += term
    return total


def float_e(k: int) -> float:
    r = cycle_count(k)
    # For large r the omitted tail of exp(-1/k) is far below double
    # precision. Avoid constructing enormous factorials.
    if r > 100:
        return math.exp(-1.0 / k)
    return float(exact_e(k))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("K", type=int, nargs="?", default=10)
    parser.add_argument(
        "--exact-through",
        type=int,
        default=5,
        help="print exact rational E_k through this period",
    )
    args = parser.parse_args()
    if args.K < 2:
        raise SystemExit("K must be at least 2")

    product_value = 1.0
    for k in range(2, args.K + 1):
        r = cycle_count(k)
        value = float_e(k)
        product_value *= value
        line = (
            f"k={k:2d} r_k={r} E_k={value:.16g} "
            f"positive_density={product_value / 6:.16g}"
        )
        if k <= args.exact_through:
            line += f" exact_E={exact_e(k)}"
        print(line)

    # The correction product converges extremely rapidly because r_k grows
    # exponentially.  Beyond k=10, E_k and exp(-1/k) agree far beyond the
    # displayed precision.
    correction = 1.0
    for k in range(2, max(args.K, 200) + 1):
        correction *= float_e(k) * math.exp(1.0 / k)
    euler_gamma = 0.577215664901532860606512090082402431
    asymptotic = math.exp(1.0 - euler_gamma) * correction
    print(f"K*product_E asymptotic constant ~= {asymptotic:.16g}")
    print(f"positive-sector constant ~= {asymptotic / 6:.16g}/K")


if __name__ == "__main__":
    main()
