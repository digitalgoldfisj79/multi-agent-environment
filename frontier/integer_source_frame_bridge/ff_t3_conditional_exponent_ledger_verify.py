#!/usr/bin/env python3
"""Exact symbolic exponent audit for the conditional FF T3 coset bound.

This verifier does not test an asymptotic theorem. It checks the exponent ledger
following from:

- q^(R-2k) completion factor;
- q^(2k-R) nonzero dual frequencies;
- q^(2m) absolute von Mangoldt source-pair mass;
- q^(2k) prime-pair count;
- q^(-k/2) fixed-source FFPS saving;
- q^(R+m) diagonal scale.

The resulting fixed-source-FFPS ratio exponent is m+3k/2-R. Obtaining the
claimed 3k/2-R exponent requires an additional q^(-m) saving from the signed
source-pair sum.
"""
from __future__ import annotations

import json
from pathlib import Path


PANELS = (
    (2, 3, 3),
    (3, 5, 5),
    (4, 7, 7),
    (5, 8, 8),
    (6, 11, 11),
)


def panel(k: int, R: int, m: int) -> dict:
    # Store doubled exponents to avoid floating arithmetic.
    completion_twice = 2 * (R - 2 * k)
    frequency_twice = 2 * (2 * k - R)
    source_mass_twice = 4 * m
    prime_pair_twice = 4 * k
    ffps_saving_twice = -k

    fixed_residual_twice = (
        completion_twice
        + frequency_twice
        + source_mass_twice
        + prime_pair_twice
        + ffps_saving_twice
    )
    assert fixed_residual_twice == 4 * m + 3 * k

    diagonal_twice = 2 * (R + m)
    fixed_ratio_twice = fixed_residual_twice - diagonal_twice
    assert fixed_ratio_twice == 2 * m + 3 * k - 2 * R

    lambda_signed_residual_twice = fixed_residual_twice - 2 * m
    assert lambda_signed_residual_twice == 2 * m + 3 * k

    lambda_signed_ratio_twice = lambda_signed_residual_twice - diagonal_twice
    assert lambda_signed_ratio_twice == 3 * k - 2 * R

    return {
        "k": k,
        "R": R,
        "m": m,
        "fixed_source_ffps_residual_exponent": fixed_residual_twice / 2,
        "diagonal_exponent": diagonal_twice / 2,
        "fixed_source_ffps_ratio_exponent": fixed_ratio_twice / 2,
        "lambda_signed_target_residual_exponent": lambda_signed_residual_twice / 2,
        "lambda_signed_target_ratio_exponent": lambda_signed_ratio_twice / 2,
        "missing_exponent_saving": m,
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "classification": "EXACT_EXPONENT_LEDGER",
        "identity": {
            "fixed_source_FFPS_ratio_exponent": "m + 3k/2 - R",
            "claimed_ratio_exponent": "3k/2 - R",
            "missing_saving": "q^{-m}",
            "required_strengthening": (
                "Lambda-signed cancellation across the source-pair sum"
            ),
        },
        "panels": [panel(*values) for values in PANELS],
        "boundary": (
            "The fixed-source prime-pair square-root bound FFPS does not imply "
            "the claimed Theorem D. The claimed ratio requires an additional "
            "q^{-m} saving from the signed von Mangoldt source-pair sum."
        ),
    }
    output = Path(__file__).with_name("ff_t3_conditional_exponent_ledger_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
