#!/usr/bin/env python3
"""Verify exact zero-mode formulas and finite principal-term calibration."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import factorint, integer_nthroot, mobius, primerange


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def S_mu(T: int) -> float:
    return sum(float(mobius(n)) / n for n in range(1, T + 1))


def S_mulog(T: int) -> float:
    return sum(float(mobius(n)) * math.log(n) / n for n in range(1, T + 1))


def S_lambda(T: int) -> float:
    return sum(von_mangoldt(n) / n for n in range(1, T + 1))


def toy_exact(P: int, H: int, Y: int) -> dict:
    weights = {m: 1.0 + 0.2 * math.cos(m) for m in range(2, H + 1)}
    W = sum(weights.values())
    L = sum(weights[m] * math.log(P + m) for m in weights)
    Z = P + H
    direct_I = sum(float(mobius(d)) / d *
                   sum(weights[m] * math.log((P + m) / d) for m in weights)
                   for d in range(1, Y + 1))
    formula_I = L * S_mu(Y) - W * S_mulog(Y)
    direct_II = sum(-W * float(mobius(d)) * von_mangoldt(c) / (d * c)
                    for d in range(1, Y + 1) for c in range(1, Y + 1))
    formula_II = -W * S_mu(Y) * S_lambda(Y)
    direct_III = 0.0
    for c in range(Y + 1, Z // Y + 1):
        lc = von_mangoldt(c)
        if lc:
            direct_III += sum(W * float(mobius(a)) * lc / (a * c)
                              for a in range(Y + 1, Z // c + 1))
    SmuY = S_mu(Y)
    formula_III = sum(W * von_mangoldt(c) / c * (S_mu(Z // c) - SmuY)
                      for c in range(Y + 1, Z // Y + 1) if von_mangoldt(c))
    return {
        "P": P, "H": H, "Y": Y, "W": W,
        "type_I_error": abs(direct_I - formula_I),
        "type_II_error": abs(direct_II - formula_II),
        "type_III_error": abs(direct_III - formula_III),
        "combined_error": abs(direct_I + direct_II + direct_III -
                              formula_I - formula_II - formula_III),
    }


def block_row(X: int) -> dict:
    P0 = 1
    for p in primerange(2, X):
        P0 *= int(p)
    Y, _ = integer_nthroot(P0, 3)
    Y = int(Y)
    H = int(0.8 * X * X)
    W = H - 1
    L = sum(math.log(P0 + m) for m in range(2, H + 1))
    sm, sml, sl = S_mu(Y), S_mulog(Y), S_lambda(Y)
    type_I = L * sm - W * sml
    type_II = -W * sm * sl
    return {
        "X": X, "P0": P0, "H": H, "Y": Y, "Y_exceeds_H": Y > H,
        "S_mu_Y": sm, "S_mulog_Y": sml, "S_lambda_Y": sl,
        "type_I_plus_II_over_W": (type_I + type_II) / W,
        "type_I_over_W": type_I / W, "type_II_over_W": type_II / W,
    }


def main() -> None:
    toys = [toy_exact(10007, 10, 15), toy_exact(20011, 14, 20), toy_exact(50021, 18, 25)]
    for row in toys:
        assert row["type_I_error"] < 2e-12
        assert row["type_II_error"] < 2e-12
        assert row["type_III_error"] < 2e-12
        assert row["combined_error"] < 5e-12

    panel = [block_row(X) for X in (31, 37, 41, 43)]
    assert all(row["Y_exceeds_H"] for row in panel)
    payload = {
        "status": "PASS",
        "scope": "exact zero-frequency formulas and post-threshold Mertens calibration",
        "toy_exact_rows": toys,
        "primorial_panel": panel,
        "boundary": "Uniform asymptotic positivity uses the published zeta zero-free-region bound.",
    }
    Path(__file__).with_name("zero_frequency_principal_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
