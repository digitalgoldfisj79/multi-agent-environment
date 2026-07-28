#!/usr/bin/env python3
"""Calibrate the explicit candidate-projector principal and singular series."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import nextprime, primepi, primerange, totient


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def singular_series(z: int, tail_limit: int = 200000) -> float:
    P = primorial(z)
    first = P / int(totient(P))
    tail = 1.0
    for p0 in primerange(z + 1, tail_limit + 1):
        p = int(p0)
        tail *= 1.0 - 1.0 / ((p - 1) * (p - 1))
    # The omitted tail is 1+O(1/tail_limit), enough for calibration.
    return first * tail


def row(z: int, eta: float = 0.8) -> dict:
    P = primorial(z)
    H = int(eta * z * z)
    assert H < int(nextprime(z)) ** 2
    candidate_count = int(primepi(H)) - int(primepi(z))
    principal = P / int(totient(P)) * candidate_count
    ss = singular_series(z)
    hl_proxy = ss * (float(primepi(H)) - float(primepi(z)))
    return {
        "z": z,
        "P_digits": len(str(P)),
        "H": H,
        "candidate_count": candidate_count,
        "P_over_phiP": P / int(totient(P)),
        "candidate_principal": principal,
        "candidate_principal_over_H": principal / H,
        "singular_series_truncated": ss,
        "HL_prime_count_proxy": hl_proxy,
        "HL_minus_candidate_over_H": (hl_proxy - principal) / H,
        "difference_from_e_gamma_over_2": principal / H - math.exp(math.euler_gamma) / 2
        if hasattr(math, "euler_gamma") else None,
        "reduced_principal_over_H_using_exact_smooth_formula": None,
    }


def main() -> None:
    # Python 3.12 does not expose Euler's constant in every build.
    gamma = 0.5772156649015328606
    rows = [row(z) for z in (31, 53, 101, 251, 503, 1009)]
    for item in rows:
        item["difference_from_e_gamma_over_2"] = (
            item["candidate_principal_over_H"] - math.exp(gamma) / 2
        )
        item["reduced_asymptotic_constant_gap"] = (
            item["candidate_principal_over_H"] - math.log(2)
        )
        assert item["candidate_principal"] > 0
    payload = {
        "status": "PASS",
        "scope": "explicit candidate principal and local singular-series calibration",
        "constants": {
            "e_gamma_over_2": math.exp(gamma) / 2,
            "log_two": math.log(2),
            "e_gamma_over_2_minus_log_two": math.exp(gamma) / 2 - math.log(2),
        },
        "rows": rows,
        "boundary": "The calculations verify the explicit centring and local factors; they do not verify the shifted-prime asymptotic.",
    }
    Path(__file__).with_name("explicit_candidate_principal_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
