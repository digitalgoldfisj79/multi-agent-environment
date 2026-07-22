#!/usr/bin/env python3
"""Estimate the effective growing-cutoff Bonferroni bounds.

The script implements the explicit quantities in GROWING_CUTOFF_BONFERRONI.md.
It does not test the finite good-reduction condition.  It reports the geometric
point-count threshold after that condition has been verified.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class CutoffData:
    K: int
    harmonic_tail: float
    L: int
    tuple_count: int
    log_degree_bound: float
    log_point_count_threshold: float


def harmonic_tail(K: int) -> float:
    return math.fsum(1.0 / k for k in range(2, K + 1))


def least_odd_at_least(x: float) -> int:
    value = math.ceil(x)
    return value if value % 2 else value + 1


def log_binomial(n: int, k: int) -> float:
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def cutoff_data(K: int) -> CutoffData:
    if K < 2:
        raise ValueError("K must be at least 2")

    lam = harmonic_tail(K)
    L = least_odd_at_least(6.0 * lam)
    tuple_count = math.comb(K - 1 + L, L)

    # Every mixed marked twist of total order at most L can be placed in an
    # affine model of degree at most
    #
    #   Delta = 12 (L^2 K + 1) 3^{K(L+1)}.
    #
    # The polynomial factor accounts conservatively for diagonals, branch
    # removal, local-rootlessness and the discriminant Kummer cover.
    log_delta = (
        math.log(12.0)
        + math.log(L * L * K + 1.0)
        + K * (L + 1) * math.log(3.0)
    )
    log_n = log_binomial(K - 1 + L, L)

    # Sufficient conditions from the Cafure--Matera error bound after summing
    # all mixed moments:
    #   p > 6 Delta^2,
    #   sqrt(p) >= 192 K N Delta^3,
    #   p >= 960 K N Delta^(13/3).
    log_threshold = max(
        math.log(6.0) + 2.0 * log_delta,
        2.0 * (math.log(192.0 * K) + log_n + 3.0 * log_delta),
        math.log(960.0 * K) + log_n + (13.0 / 3.0) * log_delta,
    )

    return CutoffData(
        K=K,
        harmonic_tail=lam,
        L=L,
        tuple_count=tuple_count,
        log_degree_bound=log_delta,
        log_point_count_threshold=log_threshold,
    )


def taylor_lower_bound(lam: float, L: int) -> tuple[float, float, float]:
    """Return partial sum, exp(-lam), and next-term error bound."""
    term = 1.0
    partial = 1.0
    for j in range(1, L + 1):
        term *= -lam / j
        partial += term
    next_term = abs(term) * lam / (L + 1)
    return partial, math.exp(-lam), next_term


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("K", type=int, nargs="*", default=[5, 10, 20, 50, 100])
    args = parser.parse_args()

    for K in args.K:
        data = cutoff_data(K)
        partial, exact, remainder = taylor_lower_bound(
            data.harmonic_tail, data.L
        )
        print(f"K={K}")
        print(f"  lambda_K={data.harmonic_tail:.16g}")
        print(f"  odd Bonferroni order L={data.L}")
        print(f"  mixed tuples N={data.tuple_count}")
        print(f"  P_L(lambda)={partial:.16g}")
        print(f"  exp(-lambda)={exact:.16g}")
        print(f"  next-term bound={remainder:.16g}")
        print(f"  log Delta <= {data.log_degree_bound:.16g}")
        print(f"  log p threshold <= {data.log_point_count_threshold:.16g}")
        print(
            "  decimal digits of p threshold <= "
            f"{data.log_point_count_threshold / math.log(10.0):.3f}"
        )
        if K >= 3:
            ratio = data.log_point_count_threshold / (K * math.log(K))
            print(f"  log-threshold/(K log K)={ratio:.6f}")
        assert data.L % 2 == 1
        assert partial > 0.0
        assert partial >= 0.5 * exact
        print()


if __name__ == "__main__":
    main()
