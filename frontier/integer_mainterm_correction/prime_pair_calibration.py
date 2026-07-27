#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import mpmath as mp
from sympy import isprime, nextprime, primerange


def twin_prime_constant(limit: int = 2_000_000) -> mp.mpf:
    mp.mp.dps = 50
    logc = mp.mpf("0")
    for p in primerange(3, limit + 1):
        logc += mp.log(mp.mpf(p * (p - 2)) / mp.mpf((p - 1) ** 2))
    return mp.e ** logc


def primorial_singular_series(p: int, c2: mp.mpf) -> mp.mpf:
    value = 2 * c2
    for q in primerange(3, p + 1):
        value *= mp.mpf(q - 1) / mp.mpf(q - 2)
    return value


def calibrate_at_prime(p: int, primorial: int, eta: float, c2: mp.mpf) -> dict:
    p_next = int(nextprime(p))
    H = min(int(math.floor(eta * p_next * p_next)), p_next * p_next - 1)
    candidate_primes = list(primerange(p + 1, H + 1))

    successful_offsets = []
    weighted = mp.mpf("0")
    for m in candidate_primes:
        value = primorial + m
        if isprime(value):
            successful_offsets.append(m)
            weighted += mp.log(value)

    singular = primorial_singular_series(p, c2)
    lambda_main = singular * mp.quad(
        lambda t: 1 / (mp.log(t) * mp.log(mp.mpf(primorial) + t)),
        [mp.mpf(p + 1), mp.mpf(H)],
    )
    mu_main = singular * (mp.li(H) - mp.li(p + 1))
    z = len(successful_offsets)

    return {
        "p": p,
        "p_next": p_next,
        "eta": eta,
        "H": H,
        "primorial_digits": len(str(primorial)),
        "candidate_prime_count": len(candidate_primes),
        "successful_pair_count_Z": z,
        "first_successful_offset": successful_offsets[0] if successful_offsets else None,
        "singular_series": float(singular),
        "singular_series_over_log_p": float(singular / mp.log(p)),
        "lambda_main": float(lambda_main),
        "Z_over_lambda": float(mp.mpf(z) / lambda_main),
        "weighted_pair_sum": float(weighted),
        "mu_main": float(mu_main),
        "weighted_over_mu": float(weighted / mu_main),
        "weighted_over_H": float(weighted / H),
        "e_gamma_over_2": float(mp.e ** mp.euler / 2),
        "logP": float(mp.log(primorial)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--eta", type=float, default=0.9)
    parser.add_argument(
        "--targets",
        default="29,43,59,79,101,131,167,211,263,331,419",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("prime_pair_calibration_results.json"),
    )
    args = parser.parse_args()

    targets = sorted({int(x) for x in args.targets.split(",") if x.strip()})
    if any(not isprime(p) for p in targets):
        raise SystemExit("Every target must be prime")

    c2 = twin_prime_constant()
    primorial = 1
    rows = []
    for p in primerange(2, max(targets) + 1):
        primorial *= int(p)
        if p in set(targets):
            row = calibrate_at_prime(int(p), primorial, args.eta, c2)
            rows.append(row)
            print(json.dumps(row, sort_keys=True))

    payload = {
        "status": "finite exact calibration; no asymptotic inference",
        "method": {
            "candidate_collapse": "Only prime offsets can yield prime outputs below p_next^2; proper output prime powers are excluded from the measured weighted pair sum.",
            "lambda_main": "S(P) integral dt/(log t log(P+t))",
            "mu_main": "S(P) integral dt/log t",
            "twin_prime_constant_cutoff": 2_000_000,
        },
        "rows": rows,
    }
    args.out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    csv_path = args.out.with_suffix(".csv")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {args.out} and {csv_path}")


if __name__ == "__main__":
    main()
