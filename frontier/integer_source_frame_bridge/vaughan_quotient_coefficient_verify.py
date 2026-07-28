#!/usr/bin/env python3
"""Verify the Vaughan quotient convolution identity and logarithmic bounds."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import divisors, factorint, mobius


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def full(q: int) -> float:
    return sum(float(mobius(d)) * von_mangoldt(q // int(d)) for d in divisors(q))


def A(q: int, Y: int) -> float:
    return sum(float(mobius(d)) * von_mangoldt(q // int(d))
               for d in divisors(q) if int(d) <= Y and q // int(d) <= Y)


def B(q: int, Y: int) -> float:
    return sum(von_mangoldt(int(c)) for c in divisors(q) if int(c) > Y)


def C(q: int, Y: int) -> float:
    return sum(float(mobius(a)) * von_mangoldt(q // int(a))
               for a in divisors(q) if int(a) > Y and q // int(a) > Y)


def main() -> None:
    max_identity_error = 0.0
    max_ratios = {"A": 0.0, "B": 0.0, "C": 0.0}
    support_errors = 0
    cases = 0
    for Y in (5, 11, 23, 47):
        for q in range(2, 5001):
            target = -float(mobius(q)) * math.log(q)
            err = abs(full(q) - target)
            max_identity_error = max(max_identity_error, err)
            assert err < 2e-11, (q, full(q), target)
            av, bv, cv = A(q, Y), B(q, Y), C(q, Y)
            assert abs(av) <= 2 * math.log(q) + 2e-12
            assert 0 <= bv <= math.log(q) + 2e-12
            assert abs(cv) <= 2 * math.log(q) + 2e-12
            max_ratios["A"] = max(max_ratios["A"], abs(av) / math.log(q))
            max_ratios["B"] = max(max_ratios["B"], bv / math.log(q))
            max_ratios["C"] = max(max_ratios["C"], abs(cv) / math.log(q))
            if q > Y * Y and abs(av) > 2e-12:
                support_errors += 1
            if q <= Y * Y and abs(cv) > 2e-12:
                support_errors += 1
            cases += 1
    assert support_errors == 0
    payload = {
        "status": "PASS",
        "scope": "full and truncated mu-Lambda convolution coefficients",
        "cases": cases,
        "max_identity_error": max_identity_error,
        "max_ratio_to_log_q": max_ratios,
        "support_errors": support_errors,
        "boundary": "Pointwise and support identities only; nonzero-mode dispersion remains open.",
    }
    Path(__file__).with_name("vaughan_quotient_coefficient_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
