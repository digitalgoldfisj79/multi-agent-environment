#!/usr/bin/env python3
"""Exact finite checks for the Fortune mainline obstruction examples.

These checks validate algebraic countermodels used in INTEGER_FRONTIER.md.
They do not simulate primes and do not claim an asymptotic theorem.
"""

from __future__ import annotations

from fractions import Fraction
import json


def first_moment_countermodel(n: int, baseline: int) -> dict[str, str | int]:
    if n <= 1 or baseline <= 0:
        raise ValueError("require n > 1 and baseline > 0")
    lam = Fraction(baseline)
    values = [Fraction(0)] + [lam + lam / (n - 1)] * (n - 1)
    first = sum(values)
    variance = sum((z - lam) ** 2 for z in values)
    expected_variance = lam**2 * (1 + Fraction(1, n - 1))
    assert first == n * lam
    assert variance == expected_variance
    assert values[0] == 0
    return {
        "n": n,
        "baseline": baseline,
        "sum": str(first),
        "target_sum": str(n * lam),
        "variance": str(variance),
        "failed_centres": 1,
    }


def dense_average_invisibility(x: int) -> dict[str, str | int]:
    """Use the model scales N=floor(X/log X), H=X^2, Y=2^X.

    The exact rational ratio N*H/Y demonstrates polynomial selected volume
    inside an exponential ambient range.
    """
    if x < 4:
        raise ValueError("require x >= 4")
    # A deterministic lower-complexity proxy for X/log X is enough here.
    n = max(1, x // max(1, x.bit_length()))
    h = x * x
    y = 2**x
    ratio = Fraction(n * h, y)
    return {
        "X": x,
        "N_proxy": n,
        "H": h,
        "Y": y,
        "selected_to_ambient_ratio": str(ratio),
    }


def main() -> int:
    results = {
        "first_moment_countermodels": [
            first_moment_countermodel(n, baseline)
            for n, baseline in [(2, 5), (10, 100), (100, 1000)]
        ],
        "dense_average_invisibility": [
            dense_average_invisibility(x) for x in [16, 32, 64, 128]
        ],
        "conclusion": (
            "Exact first moments permit a failed centre, and polynomially many "
            "selected windows are asymptotically invisible in an exponential "
            "ambient average. A selected-centre covariance theorem is required."
        ),
    }
    print(json.dumps(results, indent=2))
    print("FORTUNE_MAINLINE_FINITE_OBSTRUCTION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
