#!/usr/bin/env python3
"""Verify the exact zero/nonzero Vaughan decomposition on finite sources."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

from sympy import factorint, mobius


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def projector(P: int, q: int, weights: dict[int, float]) -> tuple[float, complex]:
    direct = sum(w for m, w in weights.items() if (P + m) % q == 0)
    W = sum(weights.values())
    nonzero = 0j
    for r in range(1, q):
        wh = sum(w * cmath.exp(2j * math.pi * r * m / q)
                 for m, w in weights.items())
        nonzero += wh * cmath.exp(2j * math.pi * r * P / q)
    nonzero /= q
    return direct - W / q, nonzero


def log_projector(P: int, d: int, weights: dict[int, float]) -> tuple[float, complex]:
    direct = sum(w * math.log((P + m) / d) for m, w in weights.items()
                 if (P + m) % d == 0)
    zero = sum(w * math.log((P + m) / d) for m, w in weights.items()) / d
    nonzero = 0j
    for r in range(1, d):
        gh = sum(w * math.log((P + m) / d) * cmath.exp(2j * math.pi * r * m / d)
                 for m, w in weights.items())
        nonzero += gh * cmath.exp(2j * math.pi * r * P / d)
    nonzero /= d
    return direct - zero, nonzero


def A(q: int, Y: int) -> float:
    return sum(float(mobius(d)) * von_mangoldt(q // d)
               for d in range(1, Y + 1) if q % d == 0 and q // d <= Y)


def C(q: int, Y: int) -> float:
    return sum(float(mobius(a)) * von_mangoldt(q // a)
               for a in range(Y + 1, q + 1) if q % a == 0 and q // a > Y)


def one_case(P: int, H: int, Y: int) -> dict:
    weights = {m: 1.0 + 0.1 * math.cos(m) for m in range(2, H + 1)}
    W = sum(weights.values())
    L = sum(w * math.log(P + m) for m, w in weights.items())
    direct = sum(w * von_mangoldt(P + m) for m, w in weights.items())

    S_mu = sum(float(mobius(n)) / n for n in range(1, Y + 1))
    S_mulog = sum(float(mobius(n)) * math.log(n) / n for n in range(1, Y + 1))
    S_lambda = sum(von_mangoldt(n) / n for n in range(1, Y + 1))
    MI = L * S_mu - W * S_mulog
    MII = -W * S_mu * S_lambda
    Z = P + H
    MIII = 0.0
    for c in range(Y + 1, Z // Y + 1):
        lc = von_mangoldt(c)
        if lc:
            inner = sum(float(mobius(a)) / a for a in range(Y + 1, Z // c + 1))
            MIII += W * lc * inner / c

    EI = sum(float(mobius(d)) * log_projector(P, d, weights)[0]
             for d in range(1, Y + 1))
    EII = -sum(A(q, Y) * projector(P, q, weights)[0]
               for q in range(1, Y * Y + 1))
    EIII = sum(C(q, Y) * projector(P, q, weights)[0]
                for q in range(Y * Y + 1, Z + 1))

    total = MI + MII + MIII + EI + EII + EIII
    projector_error = 0.0
    log_projector_error = 0.0
    for q in range(2, min(40, Z) + 1):
        a, b = projector(P, q, weights)
        projector_error = max(projector_error, abs(a - b))
    for d in range(2, min(Y, 30) + 1):
        a, b = log_projector(P, d, weights)
        log_projector_error = max(log_projector_error, abs(a - b))

    return {
        "P": P, "H": H, "Y": Y,
        "direct_source": direct,
        "reconstructed_source": total,
        "source_error": abs(direct - total),
        "projector_error": projector_error,
        "log_projector_error": log_projector_error,
        "zero_modes": {"I": MI, "II": MII, "III": MIII},
        "nonzero_modes": {"I": EI, "II": EII, "III": EIII},
    }


def main() -> None:
    rows = [one_case(10007, 10, 15), one_case(20011, 12, 18), one_case(50021, 14, 22)]
    for row in rows:
        assert row["source_error"] < 2e-10, row
        assert row["projector_error"] < 2e-10, row
        assert row["log_projector_error"] < 2e-10, row
    payload = {
        "status": "PASS",
        "scope": "exact finite zero/nonzero Vaughan source decomposition",
        "rows": rows,
        "boundary": "Finite identity verification only; no asymptotic nonzero-mode estimate.",
    }
    Path(__file__).with_name("exact_nonzero_mode_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
