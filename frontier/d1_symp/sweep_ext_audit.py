#!/usr/bin/env python3
"""Independent statistical audit of a sweep_ext_results.csv file."""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.stats import norm, spearmanr


def audit(csv_path: Path) -> dict[str, object]:
    rows=[]
    with csv_path.open() as handle:
        for row in csv.DictReader(handle):
            rows.append({k:(int(v) if k == "p" else float(v)) for k,v in row.items()})
    primes=np.asarray([r["p"] for r in rows], dtype=float)
    sums=np.asarray([r["S"] if "S" in r else r["Sp"] for r in rows], dtype=float)
    z=np.asarray([r["z"] if "z" in r else r["Sp"]/math.sqrt((r["p"]-1)/2) for r in rows], dtype=float)
    n=len(rows)

    bins=np.logspace(np.log10(primes.min()), np.log10(primes.max()+1), 15)
    bx=[]; by=[]
    for i in range(14):
        mask=(primes >= bins[i]) & (primes < bins[i+1])
        if mask.sum() >= 5:
            bx.append(math.log(math.sqrt(bins[i]*bins[i+1])))
            by.append(math.log(float(np.sqrt(np.mean(sums[mask]**2)))))
    design=np.vstack([bx, np.ones(len(bx))]).T
    coefficient, residual, _, _ = np.linalg.lstsq(design, by, rcond=None)
    sigma2=(residual[0]/(len(bx)-2)) if len(residual) else 0.0
    standard_error=math.sqrt(sigma2*np.linalg.inv(design.T@design)[0,0])

    def maximum_cdf(x: float) -> float:
        return float((2*norm.cdf(x)-1)**n)

    expected_maximum=quad(lambda x: 1.0-maximum_cdf(x), 0, 10,
                          epsabs=1e-13, limit=300)[0]
    observed=float(np.max(np.abs(z)))
    record_index=int(np.argmax(np.abs(z)))
    rho, pvalue=spearmanr(np.abs(z), primes)
    return {
        "n": n,
        "rms_z": float(np.sqrt(np.mean(z*z))),
        "max_abs_z": observed,
        "record_p": int(primes[record_index]),
        "growth_exponent": float(coefficient[0]),
        "growth_95_halfwidth": float(1.96*standard_error),
        "spearman_absz_p": float(rho),
        "spearman_pvalue": float(pvalue),
        "iid_normal_expected_max_abs": float(expected_maximum),
        "iid_normal_percentile_of_observed_max": maximum_cdf(observed),
        "sqrt_2logn": float(math.sqrt(2*math.log(n))),
        "top5": [(int(r["p"]), float(r["z"]))
                 for r in sorted(rows, key=lambda row: -abs(row["z"]))[:5]],
    }


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("csv", type=Path, help="path to sweep_ext_results.csv")
    parser.add_argument("--output", type=Path, default=None)
    args=parser.parse_args()
    result=audit(args.csv)
    if args.output is not None:
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
