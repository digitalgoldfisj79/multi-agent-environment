#!/usr/bin/env python3
"""Verify exact grouping of Möbius-log modes by reduced rational frequency."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

from sympy import factorint, mobius, totient


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def one_case(P: int, H: int) -> dict:
    weights = {m: 1.0 + 0.1 * math.cos(m) for m in range(2, H + 1)}
    W = sum(weights.values())
    Z = P + H
    direct = sum(w * von_mangoldt(P + m) for m, w in weights.items())
    principal = -W * sum(float(mobius(d)) * math.log(d) / d for d in range(1, Z + 1))
    residual = direct - principal

    unreduced = 0j
    for d in range(2, Z + 1):
        coeff = -float(mobius(d)) * math.log(d) / d
        if coeff == 0.0:
            continue
        for r in range(1, d):
            wh = sum(w * cmath.exp(2j * math.pi * r * m / d)
                     for m, w in weights.items())
            unreduced += coeff * wh * cmath.exp(2j * math.pi * r * P / d)

    primitive = 0j
    gamma_rows = []
    for q in range(2, Z + 1):
        gamma = -sum(
            float(mobius(q * u)) * math.log(q * u) / u
            for u in range(1, Z // q + 1)
        ) / q
        if mobius(q) == 0:
            assert abs(gamma) < 2e-14
        row = 0j
        for a in range(1, q):
            if math.gcd(a, q) != 1:
                continue
            wh = sum(w * cmath.exp(2j * math.pi * a * m / q)
                     for m, w in weights.items())
            row += wh * cmath.exp(2j * math.pi * a * P / q)
        primitive += gamma * row
        if q <= 12:
            gamma_rows.append({
                "q": q,
                "gamma": gamma,
                "ramanujan_coefficient": (
                    float(mobius(q)) / int(totient(q)) if mobius(q) != 0 else 0.0
                ),
                "complementary_length": Z // q,
            })

    return {
        "P": P,
        "H": H,
        "Z": Z,
        "direct_source": direct,
        "principal": principal,
        "residual": residual,
        "unreduced_real": unreduced.real,
        "unreduced_imag": unreduced.imag,
        "primitive_real": primitive.real,
        "primitive_imag": primitive.imag,
        "unreduced_error": abs(unreduced - residual),
        "primitive_error": abs(primitive - residual),
        "grouping_error": abs(primitive - unreduced),
        "gamma_rows": gamma_rows,
    }


def main() -> None:
    rows = [one_case(210, 12), one_case(330, 14), one_case(462, 16)]
    for row in rows:
        assert row["unreduced_error"] < 3e-9, row
        assert row["primitive_error"] < 3e-9, row
        assert row["grouping_error"] < 3e-9, row
        assert abs(row["primitive_imag"]) < 3e-9, row
    payload = {
        "status": "PASS",
        "scope": "exact Möbius-log reduction to primitive rational frequencies",
        "rows": rows,
        "boundary": "Finite exact grouping only; the uniform asymptotic for Gamma uses the classical zero-free region.",
    }
    Path(__file__).with_name("primitive_rational_frequency_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
