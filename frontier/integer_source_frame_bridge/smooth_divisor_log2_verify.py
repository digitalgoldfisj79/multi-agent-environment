#!/usr/bin/env python3
"""Verify the exact smooth-sector formula and calibrate its log-two limit."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import factorint, nextprime, primerange, primepi


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def exact_formula(z: int, H: int) -> float:
    total = 0.0
    piz = int(primepi(z))
    for r0 in primerange(2, z + 1):
        r = int(r0)
        pure = int(math.log(H, r)) if H >= r else 0
        mixed = 0
        power = r
        while power <= H:
            mixed += max(0, int(primepi(H // power)) - piz)
            if power > H // r:
                break
            power *= r
        total += math.log(r) * (pure + mixed)
    return total


def direct(z: int, H: int) -> float:
    P = primorial(z)
    return sum(von_mangoldt(math.gcd(m, P)) for m in range(2, H + 1))


def main() -> None:
    exact_rows = []
    for z in (11, 13, 17, 19):
        H = int(0.8 * z * z)
        assert H < int(nextprime(z)) ** 2
        a = direct(z, H)
        b = exact_formula(z, H)
        exact_rows.append({"z": z, "H": H, "direct": a, "formula": b, "error": abs(a - b)})
        assert abs(a - b) < 3e-10

    calibration = []
    for z in (101, 251, 503, 1009, 2003, 5003):
        H = int(0.8 * z * z)
        value = exact_formula(z, H)
        predicted = math.log(math.log(H) / math.log(z))
        calibration.append({
            "z": z, "H": H, "G_over_H": value / H,
            "predicted_log_ratio": predicted,
            "difference": value / H - predicted,
            "difference_from_log2": value / H - math.log(2),
        })

    payload = {
        "status": "PASS",
        "scope": "exact smooth-sector formula and finite log-two calibration",
        "exact_rows": exact_rows,
        "calibration": calibration,
        "log_two": math.log(2),
        "one_minus_log_two": 1 - math.log(2),
        "boundary": "Finite calibration is corroborative; the asymptotic theorem uses the PNT proof in the note.",
    }
    Path(__file__).with_name("smooth_divisor_log2_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
