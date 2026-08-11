#!/usr/bin/env python3
"""Exact finite-compression diagnostics for Fortune selected-centre occupancies.

This is a falsification-first diagnostic.  It reuses the already accepted exact
primorial panel generator and does not promote finite panels to asymptotic evidence.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PANEL_SCRIPT = ROOT / "fortune-int-aod-occupancy-dual" / "scripts" / "run_exact_primorial_panels.py"


def load_panel_module():
    spec = importlib.util.spec_from_file_location("fortune_exact_panels", PANEL_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PANEL_SCRIPT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def compression_stats(values: list[int]) -> dict:
    if not values:
        raise ValueError("empty row set")
    if any(z < 0 for z in values):
        raise ValueError("occupancies must be nonnegative")
    r = len(values)
    s1 = sum(values)
    s2 = sum(z * z for z in values)
    mean = s1 / r
    centered_ss = sum((z - mean) ** 2 for z in values)
    stable_rank = (s1 * s1 / s2) if s2 else 0.0
    threshold = r - 1
    if r == 1:
        variance_threshold = float("inf")
    else:
        variance_threshold = r * mean * mean / (r - 1)
    return {
        "rows": r,
        "sum": s1,
        "sum_squares": s2,
        "mean": mean,
        "centered_sum_squares": centered_ss,
        "stable_rank_diagonal": stable_rank,
        "full_occupancy_threshold": threshold,
        "stable_rank_margin": stable_rank - threshold,
        "variance_threshold": variance_threshold,
        "variance_margin": variance_threshold - centered_ss,
        "criterion_pass": (s1 * s1 > threshold * s2),
        "zero_rows": sum(z == 0 for z in values),
        "minimum": min(values),
        "maximum": max(values),
    }


def strata_by_terminal_width(rows: list[dict], x: int, exponent: float) -> list[dict]:
    width = max(1, int(x / (math.log(x) ** exponent)))
    groups: dict[int, list[int]] = {}
    for row in rows:
        key = (row["ell"] - x) // width
        groups.setdefault(key, []).append(row["occupancy"])
    return [
        {"key": key, "width": width, "values": groups[key]}
        for key in sorted(groups)
    ]


def exact_zero_control() -> dict:
    # Equality is attained when exactly one row is zero and all other rows are equal.
    vals = [0, 7, 7, 7, 7]
    st = compression_stats(vals)
    assert st["zero_rows"] == 1
    assert abs(st["stable_rank_diagonal"] - 4.0) < 1e-12
    assert not st["criterion_pass"]
    # Perturbing the nonzero rows cannot create a false positive by Cauchy.
    adversarial = [0, 1, 3, 8, 21, 55]
    st2 = compression_stats(adversarial)
    assert not st2["criterion_pass"]
    return {"equal_nonzero": st, "heterogeneous": st2}


def asymptotic_budget(delta: float = 0.25) -> dict:
    # Existing terminal-prime strata have prime-coordinate width
    # W = X / log(X)^(1+delta).  The number of prime-indexed rows is
    # n_b ~ W/log X = X/log(X)^(2+delta).
    # A block variance n_b*X*L excludes one failed row (cost ~X^2) when
    # L=o(X/n_b)=o(log(X)^(2+delta)).
    return {
        "delta": delta,
        "whole_block_rows": "X/log X",
        "whole_block_loss_budget": "L=o(log X)",
        "terminal_width": f"X/log(X)^{1+delta}",
        "stratum_rows": f"X/log(X)^{2+delta}",
        "stratified_loss_budget": f"L=o(log(X)^{2+delta})",
        "warning": "smaller row averaging range may cost at least this gain; this is the S5 analytic question",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--x", nargs="+", type=int, default=[50, 75, 100, 150, 200, 250, 300])
    ap.add_argument("--eta", type=float, default=0.5)
    ap.add_argument("--exponent", type=float, default=1.25)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    panel_mod = load_panel_module()
    controls = exact_zero_control()
    results = []
    for x in args.x:
        p = panel_mod.panel(x, args.eta, 4)
        zs = [row["occupancy"] for row in p["rows"]]
        global_stats = compression_stats(zs)
        strata = []
        for g in strata_by_terminal_width(p["rows"], x, args.exponent):
            st = compression_stats(g["values"])
            strata.append({"key": g["key"], "width": g["width"], **st})
        results.append({
            "X": x,
            "H": p["H"],
            "global": global_stats,
            "strata_count": len(strata),
            "strata": strata,
            "all_strata_pass": all(s["criterion_pass"] for s in strata),
            "worst_stratum_margin": min(s["stable_rank_margin"] for s in strata),
        })
        print(
            "X={x} R={r} zeros={z} global_margin={gm:.8g} strata={b} "
            "all_strata_pass={sp} worst_stratum_margin={wm:.8g}".format(
                x=x, r=global_stats["rows"], z=global_stats["zero_rows"],
                gm=global_stats["stable_rank_margin"], b=len(strata),
                sp=all(s["criterion_pass"] for s in strata),
                wm=min(s["stable_rank_margin"] for s in strata),
            )
        )

    payload = {
        "programme": "FORTUNE_ZETA23_TRANSFER_V0_1",
        "lane": "S",
        "identity": "(sum Z)^2 > (R-1) sum Z^2 implies zero_rows=0",
        "whole_block_classification": "SAME_DETERMINISTIC_CORE_AS_PAPER_II_2_4_AND_PAPER_III_9_1",
        "second_moment_classification": "EXPANDS_TO_PAPER_III_AGGREGATED_FOUR_PRIME_CORRELATION",
        "controls": controls,
        "asymptotic_budget": asymptotic_budget(args.exponent - 1.0),
        "panels": results,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")
    print("FORTUNE_ZETA23_STABLE_RANK_DIAGNOSTIC_PASS")


if __name__ == "__main__":
    main()
