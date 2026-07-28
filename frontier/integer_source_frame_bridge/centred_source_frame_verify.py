#!/usr/bin/env python3
"""Finite regression checks for the centred source-to-frame identities.

This is a numerical regression of exact finite identities.  It does not test
any prime asymptotic or source-to-frame estimate.
"""
from __future__ import annotations

import cmath
import json
import math
import random
from pathlib import Path


TAU = 2.0 * math.pi


def ee(x: float) -> complex:
    return cmath.exp(1j * TAU * x)


def max_abs(values):
    return max((abs(v) for v in values), default=0.0)


def source_projection_case(seed: int) -> dict:
    rng = random.Random(seed)
    modulus = 257
    centres = sorted(rng.sample(range(10, 90), 7))
    H = 9
    max_n = max(centres) + H + 8
    b = [rng.randrange(-5, 6) for _ in range(max_n + 1)]
    baselines = [rng.randrange(-7, 8) / 3.0 for _ in centres]

    # One-sided shifted source: U = D_H B.
    psi = [sum(b[P + m] for m in range(2, H + 1)) for P in centres]
    residuals = [psi[j] - baselines[j] for j in range(len(centres))]

    U = []
    M = []
    R = []
    for t in range(modulus):
        theta = t / modulus
        D = sum(ee(-m * theta) for m in range(2, H + 1))
        B = sum(b[n] * ee(n * theta) for n in range(len(b)))
        u = D * B
        mval = sum(baselines[j] * ee(centres[j] * theta)
                   for j in range(len(centres)))
        U.append(u)
        M.append(mval)
        R.append(u - mval)

    recovered = []
    for P in centres:
        recovered.append(
            sum(R[t] * ee(-P * t / modulus) for t in range(modulus))
            / modulus
        )

    C = []
    C_conv = []
    for ell in range(modulus):
        theta = ell / modulus
        C.append(sum(residuals[j] * ee(centres[j] * theta)
                     for j in range(len(centres))))
        conv = 0j
        for t in range(modulus):
            alpha = t / modulus
            conv += R[t] * sum(
                ee(centres[j] * (theta - alpha))
                for j in range(len(centres))
            )
        C_conv.append(conv / modulus)

    variance = sum(abs(c) ** 2 for c in residuals)
    parseval = sum(abs(z) ** 2 for z in C) / modulus

    return {
        "seed": seed,
        "coefficient_recovery_error": max_abs(
            recovered[j] - residuals[j] for j in range(len(centres))
        ),
        "convolution_error": max_abs(
            C[j] - C_conv[j] for j in range(modulus)
        ),
        "parseval_error": abs(variance - parseval),
        "centres": centres,
        "variance": variance,
    }


def reciprocal_frame_case(seed: int) -> dict:
    rng = random.Random(seed)
    centres = sorted(rng.sample(range(20, 170), 8))
    residuals = [
        complex(rng.randrange(-5, 6), rng.randrange(-4, 5))
        for _ in centres
    ]

    # Positive harmonics.  The total positive-harmonic mass is normalised to 1/2,
    # matching the symmetric row convention in Paper II.
    moduli = [101, 103, 107, 109]
    harmonics = [1, 2, 3]
    raw = {
        a: [rng.randrange(1, 10) for _ in moduli]
        for a in harmonics
    }
    raw_total = sum(sum(v) for v in raw.values())
    p = {
        a: [w / (2.0 * raw_total) for w in raw[a]]
        for a in harmonics
    }
    m = {a: sum(p[a]) for a in harmonics}
    assert abs(sum(m.values()) - 0.5) < 1e-15

    def C(theta: float) -> complex:
        return sum(
            residuals[j] * ee(centres[j] * theta)
            for j in range(len(centres))
        )

    def theta_a(a: int, L: int) -> complex:
        return sum(
            p[a][i] * ee(a * L / moduli[i])
            for i in range(len(moduli))
        )

    def kernel(L: int) -> float:
        return 2.0 * sum(
            abs(theta_a(a, L)) ** 2 / m[a]
            for a in harmonics
        )

    variance = sum(abs(c) ** 2 for c in residuals)

    frame_direct = 0.0
    for a in harmonics:
        for iq, q in enumerate(moduli):
            for ir, r in enumerate(moduli):
                frame_direct += (
                    2.0 * p[a][iq] * p[a][ir] / m[a]
                    * abs(C(a * (1.0 / q - 1.0 / r))) ** 2
                )

    frame_gram = 0j
    for j, Pj in enumerate(centres):
        for k, Pk in enumerate(centres):
            frame_gram += (
                residuals[j] * residuals[k].conjugate()
                * kernel(Pj - Pk)
            )

    # Literal square lift and canonically normalised symmetric-square lift.
    literal_pairs = []
    symmetric_pairs = []
    pair_sums = []
    for j in range(len(centres)):
        for k in range(j, len(centres)):
            mult = 1 if j == k else 2
            pair_sums.append(centres[j] + centres[k])
            literal_pairs.append(mult * residuals[j] * residuals[k])
            symmetric_pairs.append(
                math.sqrt(mult) * residuals[j] * residuals[k]
            )

    def pair_poly(coeffs, theta):
        return sum(
            coeffs[u] * ee(pair_sums[u] * theta)
            for u in range(len(coeffs))
        )

    def pair_frame_direct(coeffs):
        out = 0.0
        for a in harmonics:
            for iq, q in enumerate(moduli):
                for ir, r in enumerate(moduli):
                    out += (
                        2.0 * p[a][iq] * p[a][ir] / m[a]
                        * abs(pair_poly(
                            coeffs, a * (1.0 / q - 1.0 / r)
                        )) ** 2
                    )
        return out

    def pair_frame_gram(coeffs):
        out = 0j
        for u in range(len(coeffs)):
            for v in range(len(coeffs)):
                out += (
                    coeffs[u] * coeffs[v].conjugate()
                    * kernel(pair_sums[u] - pair_sums[v])
                )
        return out

    literal_direct = pair_frame_direct(literal_pairs)
    literal_gram = pair_frame_gram(literal_pairs)
    symmetric_direct = pair_frame_direct(symmetric_pairs)
    symmetric_gram = pair_frame_gram(symmetric_pairs)

    literal_diagonal = sum(abs(z) ** 2 for z in literal_pairs)
    literal_formula = (
        2.0 * variance ** 2
        - sum(abs(c) ** 4 for c in residuals)
    )
    symmetric_diagonal = sum(abs(z) ** 2 for z in symmetric_pairs)

    # Baseline-before-square expansion at every sampled dual-row phase.
    baseline = [rng.randrange(1, 9) / 2.0 for _ in centres]
    source = [residuals[j] + baseline[j] for j in range(len(centres))]
    expansion_errors = []
    for a in harmonics:
        for q in moduli:
            for r in moduli:
                theta = a * (1.0 / q - 1.0 / r)
                src = sum(source[j] * ee(centres[j] * theta)
                          for j in range(len(centres)))
                base = sum(baseline[j] * ee(centres[j] * theta)
                           for j in range(len(centres)))
                lhs = abs(src - base) ** 2
                rhs = (
                    abs(src) ** 2
                    - 2.0 * (src * base.conjugate()).real
                    + abs(base) ** 2
                )
                expansion_errors.append(lhs - rhs)

    return {
        "seed": seed,
        "kernel_at_zero_error": abs(kernel(0) - 1.0),
        "kernel_range_min": min(
            kernel(L) for L in range(-200, 201)
        ),
        "kernel_range_max": max(
            kernel(L) for L in range(-200, 201)
        ),
        "single_frame_error": abs(frame_direct - frame_gram),
        "single_frame_imaginary_residue": abs(frame_gram.imag),
        "literal_pair_frame_error": abs(literal_direct - literal_gram),
        "symmetric_pair_frame_error": abs(
            symmetric_direct - symmetric_gram
        ),
        "literal_diagonal_error": abs(
            literal_diagonal - literal_formula
        ),
        "symmetric_diagonal_error": abs(
            symmetric_diagonal - variance ** 2
        ),
        "baseline_before_square_error": max_abs(expansion_errors),
        "variance": variance,
        "frame_energy": frame_direct,
    }


def main() -> None:
    source_cases = [source_projection_case(s) for s in (17, 29, 41)]
    frame_cases = [reciprocal_frame_case(s) for s in (53, 67, 79)]

    tolerance = 2e-8
    for row in source_cases:
        assert row["coefficient_recovery_error"] < tolerance, row
        assert row["convolution_error"] < tolerance, row
        assert row["parseval_error"] < tolerance, row
    for row in frame_cases:
        assert row["kernel_at_zero_error"] < tolerance, row
        assert row["kernel_range_min"] > -tolerance, row
        assert row["kernel_range_max"] < 1.0 + tolerance, row
        assert row["single_frame_error"] < tolerance, row
        assert row["single_frame_imaginary_residue"] < tolerance, row
        assert row["literal_pair_frame_error"] < tolerance, row
        assert row["symmetric_pair_frame_error"] < tolerance, row
        assert row["literal_diagonal_error"] < tolerance, row
        assert row["symmetric_diagonal_error"] < tolerance, row
        assert row["baseline_before_square_error"] < tolerance, row

    payload = {
        "status": "PASS",
        "scope": (
            "finite numerical regressions of exact centred source, "
            "single-walk frame, and weighted pair-lift identities"
        ),
        "source_projection_cases": source_cases,
        "reciprocal_frame_cases": frame_cases,
        "theorem_boundary": (
            "No prime asymptotic, lower frame bound, or Fortune theorem "
            "is inferred from these finite checks."
        ),
    }
    out = Path(__file__).with_name(
        "centred_source_frame_results.json"
    )
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
