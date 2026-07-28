#!/usr/bin/env python3
"""Verify exact smooth-primitive centring and new-modulus residual."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

from sympy import factorint, mobius, primerange, totient


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def one_case(z: int, H: int) -> dict:
    P = primorial(z)
    Z = P + H
    weights = {m: 1.0 + 0.05 * math.cos(m) for m in range(2, H + 1)}
    W = sum(weights.values())
    direct = sum(w * von_mangoldt(P + m) for m, w in weights.items())
    zero = -W * sum(float(mobius(d)) * math.log(d) / d for d in range(1, Z + 1))

    smooth = 0j
    new = 0j
    all_primitive = 0j
    for q in range(2, Z + 1):
        gamma = -sum(
            float(mobius(q * u)) * math.log(q * u) / u
            for u in range(1, Z // q + 1)
        ) / q
        if gamma == 0.0:
            continue
        row = 0j
        for a in range(1, q):
            if math.gcd(a, q) != 1:
                continue
            wh = sum(w * cmath.exp(2j * math.pi * a * m / q)
                     for m, w in weights.items())
            row += wh * cmath.exp(2j * math.pi * a * P / q)
        term = gamma * row
        all_primitive += term
        if P % q == 0:
            smooth += term
        else:
            new += term

    exact_centring = zero + smooth.real
    candidate = P / int(totient(P)) * sum(
        w for m, w in weights.items() if math.gcd(m, P) == 1
    )
    return {
        "z": z,
        "P": P,
        "H": H,
        "Z": Z,
        "direct_source": direct,
        "zero_mode": zero,
        "smooth_primitive_real": smooth.real,
        "smooth_primitive_imag": smooth.imag,
        "exact_primitive_centring": exact_centring,
        "candidate_projector_principal": candidate,
        "centring_minus_candidate": exact_centring - candidate,
        "all_primitive_error": abs((direct - zero) - all_primitive),
        "new_residual_error": abs((direct - exact_centring) - new),
        "new_residual_imag": new.imag,
    }


def main() -> None:
    rows = [one_case(7, 20), one_case(11, 30), one_case(13, 36)]
    for row in rows:
        assert row["all_primitive_error"] < 3e-8, row
        assert row["new_residual_error"] < 3e-8, row
        assert abs(row["smooth_primitive_imag"]) < 3e-8, row
        assert abs(row["new_residual_imag"]) < 3e-8, row
    payload = {
        "status": "PASS",
        "scope": "exact smooth-primitive centring and new-modulus residual",
        "rows": rows,
        "boundary": "Finite exact identities only; convergence to the candidate principal is asymptotic.",
    }
    Path(__file__).with_name("exact_smooth_primitive_centring_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
