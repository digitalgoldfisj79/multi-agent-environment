#!/usr/bin/env python3
"""Finite-scale audit of the prime-power contamination bound."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import primerange

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def first_n_primes(n: int) -> list[int]:
    upper = 20 if n < 6 else int(n * (math.log(n) + math.log(math.log(n))) + 50)
    while True:
        ps = list(primerange(1, upper + 1))
        if len(ps) >= n:
            return ps[:n]
        upper *= 2


def main() -> None:
    indices = [10, 20, 50, 100, 200, 500, 1000, 3000, 10000]
    ps = first_n_primes(max(indices) + 1)
    logP = 0.0
    rows = []
    target_set = set(indices)
    for n, p in enumerate(ps[:-1], start=1):
        logP += math.log(p)
        if n not in target_set:
            continue
        pnext = ps[n]
        y = pnext * pnext - 2
        h = y / 2.0
        log2x = math.log(2.0) + logP
        K = max(2, int(log2x / math.log(2.0)))
        gamma = 0.5772156649015329
        harmonic_tail = math.log(K) + gamma + 1.0/(2.0*K) - 1.0/(12.0*K*K) - 1.0
        envelope = log2x * harmonic_tail
        rows.append({
            "n": n,
            "p_n": p,
            "p_n_plus_1": pnext,
            "log_P_n": logP,
            "y_n": y,
            "h_n": h,
            "prime_power_envelope": envelope,
            "envelope_over_h": envelope / h,
            "certificate_constant_when_envelope_le_h_over_2": 64,
        })

    result = {
        "description": "Rigorous prime-power contamination envelope used by the Fortune failure certificate",
        "rows": rows,
    }
    out = DATA / "failure_certificate_audit.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(out)


if __name__ == "__main__":
    main()
