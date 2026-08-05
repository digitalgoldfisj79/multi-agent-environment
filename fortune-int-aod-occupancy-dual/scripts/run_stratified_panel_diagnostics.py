#!/usr/bin/env python3
"""Diagnostic comparison of global and stratified ordinary cumulants."""

from __future__ import annotations

import argparse
import cmath
import math

import numpy as np

from run_exact_primorial_panels import panel, q_polynomial_coeffs


def ordinary_cumulants(values: list[int], order: int) -> list[float]:
    moments = [1.0]
    for k in range(1, order + 1):
        moments.append(sum(z**k for z in values) / len(values))
    cumulants = [0.0] * (order + 1)
    for k in range(1, order + 1):
        cumulants[k] = moments[k] - sum(
            math.comb(k - 1, r - 1) * cumulants[r] * moments[k - r]
            for r in range(1, k)
        )
    return cumulants


def laplace(values: list[int], tau: float) -> float:
    return sum(math.exp(-tau * z) for z in values) / len(values)


def nearest_tau_zero_modulus(values: list[int]) -> float | None:
    # G(tau)=G_q(1-exp(-tau)). Convert every numerical q-root to the nearest
    # logarithmic branch of tau=-log(1-q).
    coeffs = q_polynomial_coeffs(values)
    while len(coeffs) > 1 and abs(coeffs[-1]) < 1e-14:
        coeffs = coeffs[:-1]
    if len(coeffs) <= 1:
        return None
    q_roots = np.roots(coeffs[::-1])
    best = float("inf")
    for q_root in q_roots:
        s = 1.0 - complex(q_root)
        if abs(s) < 1e-14:
            continue
        principal = -cmath.log(s)
        for branch in range(-3, 4):
            tau = principal + 2j * math.pi * branch
            best = min(best, abs(tau))
    return None if not math.isfinite(best) else float(best)


def strata_by_terminal_width(rows: list[dict], x: int, exponent: float) -> list[list[int]]:
    width = max(1, int(x / (math.log(x) ** exponent)))
    groups: dict[int, list[int]] = {}
    for row in rows:
        key = (row["ell"] - x) // width
        groups.setdefault(key, []).append(row["occupancy"])
    return [groups[k] for k in sorted(groups)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", nargs="+", type=int, default=[100, 150, 200, 250])
    parser.add_argument("--eta", type=float, default=0.5)
    parser.add_argument("--exponent", type=float, default=1.25)
    args = parser.parse_args()

    print("PROGRAMME=FORTUNE_INT_AOD_OCCUPANCY_DUAL_V0_1 GATE=O4,O8 LANE=STRATIFIED_ORDINARY_CUMULANTS")
    for x in args.x:
        result = panel(x, args.eta, 12)
        groups = strata_by_terminal_width(result["rows"], x, args.exponent)
        bcount = len(groups)
        total = 0.0
        worst_ratio = 0.0
        worst_abs_margin = float("inf")
        detail = []
        for zs in groups:
            mean = sum(zs) / len(zs)
            tau = 2.0 * math.log(len(zs) * bcount) / mean
            g = laplace(zs, tau)
            contribution = len(zs) * g
            total += contribution
            order = min(12, max(zs))
            cumulants = ordinary_cumulants(zs, order)
            first = tau * cumulants[1]
            remainder = sum(
                tau**k * abs(cumulants[k]) / math.factorial(k)
                for k in range(2, order + 1)
            )
            margin = first - remainder - math.log(len(zs) * bcount)
            radius = nearest_tau_zero_modulus(zs)
            ratio = tau / radius if radius else 0.0
            worst_ratio = max(worst_ratio, ratio)
            worst_abs_margin = min(worst_abs_margin, margin)
            detail.append((len(zs), min(zs), mean, max(zs), tau, contribution, ratio, margin))
        print(
            f"X={x} strata={bcount} total_detector={total:.8g} "
            f"worst_tau_over_zero_radius={worst_ratio:.8g} "
            f"worst_order12_abs_margin={worst_abs_margin:.8g}"
        )
        for i, d in enumerate(detail):
            print(
                "  b={i} n={n} minZ={mn} meanZ={av:.6g} maxZ={mx} tau={tau:.6g} "
                "contribution={c:.6g} tau_over_radius={r:.6g} abs_margin={m:.6g}".format(
                    i=i,
                    n=d[0],
                    mn=d[1],
                    av=d[2],
                    mx=d[3],
                    tau=d[4],
                    c=d[5],
                    r=d[6],
                    m=d[7],
                )
            )
    print("FORTUNE_INT_AOD_O8_STRATIFIED_ORDINARY_PANEL_PASS")


if __name__ == "__main__":
    main()
