#!/usr/bin/env python3
"""Diagnostic comparison of global and stratified connected quantities."""

from __future__ import annotations

import argparse
import math

from run_exact_primorial_panels import factorial_cumulants, nearest_zero_modulus, panel, pgf


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

    print("PROGRAMME=FORTUNE_INT_AOD_OCCUPANCY_DUAL_V0_1 GATE=O4,O8 LANE=STRATIFIED_EXACT_PANELS")
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
            q = min(0.95, 2.0 * math.log(len(zs) * bcount) / mean)
            g = pgf(zs, q)
            contribution = len(zs) * g
            total += contribution
            order = min(12, max(zs))
            _, cumulants = factorial_cumulants(zs, order)
            first = q * cumulants[1]
            remainder = sum(
                q**k * abs(cumulants[k]) / math.factorial(k)
                for k in range(2, order + 1)
            )
            margin = first - remainder - math.log(len(zs) * bcount)
            radius = nearest_zero_modulus(zs)
            ratio = q / radius if radius else 0.0
            worst_ratio = max(worst_ratio, ratio)
            worst_abs_margin = min(worst_abs_margin, margin)
            detail.append((len(zs), min(zs), mean, max(zs), q, contribution, ratio, margin))
        print(
            f"X={x} strata={bcount} total_detector={total:.8g} "
            f"worst_q_over_zero_radius={worst_ratio:.8g} "
            f"worst_truncated_abs_margin={worst_abs_margin:.8g}"
        )
        for i, d in enumerate(detail):
            print(
                "  b={i} n={n} minZ={mn} meanZ={av:.6g} maxZ={mx} q={q:.6g} "
                "contribution={c:.6g} q_over_radius={r:.6g} abs_margin={m:.6g}".format(
                    i=i, n=d[0], mn=d[1], av=d[2], mx=d[3], q=d[4], c=d[5], r=d[6], m=d[7]
                )
            )
    print("FORTUNE_INT_AOD_O8_STRATIFIED_PANEL_PASS")


if __name__ == "__main__":
    main()
