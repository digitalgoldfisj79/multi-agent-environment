#!/usr/bin/env python3
"""Reproducible diagnostics for the primorial-centre zero-difference kernel."""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Iterable

import mpmath as mp
import numpy as np
from sympy import primerange

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)


def first_n_primes(n: int) -> np.ndarray:
    if n < 1:
        raise ValueError("n must be positive")
    upper = 20 if n < 6 else int(n * (math.log(n) + math.log(math.log(n))) + 50)
    while True:
        ps = list(primerange(1, upper + 1))
        if len(ps) >= n:
            return np.asarray(ps[:n], dtype=np.int64)
        upper *= 2


def sinc_limit(c: float) -> float:
    if c == 0:
        return 1.0
    return abs(2.0 * math.sin(c / 2.0) / c)


def normalized_zero_gaps(k_start: int = 50, k_stop: int = 250) -> list[dict[str, float]]:
    cached = DATA / "normalized_zero_gaps.csv"
    if cached.exists():
        with cached.open(newline="") as f:
            return [{
                "lower_zero_index": int(row["lower_zero_index"]),
                "gamma_lower": float(row["gamma_lower"]),
                "gamma_upper": float(row["gamma_upper"]),
                "normalized_gap_u": float(row["normalized_gap_u"]),
            } for row in csv.DictReader(f)]
    mp.mp.dps = 30
    zeros = [float(mp.im(mp.zetazero(k))) for k in range(k_start, k_stop + 1)]
    out: list[dict[str, float]] = []
    for idx, (a, b) in enumerate(zip(zeros[:-1], zeros[1:]), start=k_start):
        midpoint = (a + b) / 2.0
        u = (b - a) * math.log(midpoint / (2.0 * math.pi)) / (2.0 * math.pi)
        out.append({
            "lower_zero_index": idx,
            "gamma_lower": a,
            "gamma_upper": b,
            "normalized_gap_u": u,
        })
    return out


def kernel_metrics(N: int, gaps: Iterable[dict[str, float]]) -> dict:
    ps = first_n_primes(N)
    log_prefix = np.cumsum(np.log(ps.astype(float)))
    L = float(log_prefix[-1])

    fixed_u = [0.25, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0]
    fixed_rows = []
    for u in fixed_u:
        c = 2.0 * math.pi * u
        z = np.exp(1j * c * log_prefix / L).sum()
        fixed_rows.append({
            "u": u,
            "c": c,
            "abs_Z": float(abs(z)),
            "abs_Z_over_N": float(abs(z) / N),
            "abs_Z_over_sqrtN": float(abs(z) / math.sqrt(N)),
            "riemann_limit": sinc_limit(c),
        })

    gap_values = np.asarray([g["normalized_gap_u"] for g in gaps], dtype=float)
    observed = []
    predicted = []
    for u in gap_values:
        c = 2.0 * math.pi * float(u)
        observed.append(float(abs(np.exp(1j * c * log_prefix / L).sum()) / N))
        predicted.append(sinc_limit(c))
    observed_a = np.asarray(observed)
    predicted_a = np.asarray(predicted)

    ps_ext = first_n_primes(N + 2)
    sample_indices = sorted(set(i for i in [10, 30, 100, 300, 1000, 3000, N - 1] if 1 <= i < N))
    cutoff_ratios = []
    for n in sample_indices:
        p_np1 = int(ps_ext[n])
        p_np2 = int(ps_ext[n + 1])
        ratio = p_np1 * (p_np1 * p_np1 - 2) / (p_np2 * p_np2 - 2)
        cutoff_ratios.append({
            "n": n,
            "p_n_plus_1": p_np1,
            "p_n_plus_2": p_np2,
            "T_n_plus_1_over_T_n": ratio,
            "ratio_over_p_n_plus_1": ratio / p_np1,
        })

    return {
        "N": N,
        "p_N": int(ps[-1]),
        "log_P_N": L,
        "sqrt_N": math.sqrt(N),
        "fixed_normalized_gaps": fixed_rows,
        "actual_zero_gap_summary": {
            "count": len(observed),
            "u_mean": float(gap_values.mean()),
            "u_median": float(np.median(gap_values)),
            "kernel_abs_over_N_mean": float(observed_a.mean()),
            "kernel_abs_over_N_median": float(np.median(observed_a)),
            "kernel_abs_over_N_q90": float(np.quantile(observed_a, 0.9)),
            "limit_mean": float(predicted_a.mean()),
            "limit_median": float(np.median(predicted_a)),
            "observed_limit_correlation": float(np.corrcoef(observed_a, predicted_a)[0, 1]),
            "max_absolute_limit_error": float(np.max(np.abs(observed_a - predicted_a))),
        },
        "cutoff_migration": cutoff_ratios,
    }


def main() -> None:
    gaps = normalized_zero_gaps()
    with (DATA / "normalized_zero_gaps.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(gaps[0].keys()))
        writer.writeheader()
        writer.writerows(gaps)

    results = {
        "description": "Primorial-centre Fourier kernel at normalized zeta-zero spacings",
        "zero_gap_range": {"first": 50, "last": 250, "gap_count": len(gaps)},
        "panels": [kernel_metrics(N, gaps) for N in [100, 300, 1000, 3000, 10000]],
    }
    out = DATA / "primorial_zero_kernel_audit.json"
    out.write_text(json.dumps(results, indent=2) + "\n")
    print(out)


if __name__ == "__main__":
    main()
