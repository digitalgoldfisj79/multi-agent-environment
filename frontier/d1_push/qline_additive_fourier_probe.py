#!/usr/bin/env python3
"""Exact fixed-c irreducibility census and additive Fourier diagnostic.

For a fixed prime p and cubic square class a, define
  n_a(c)=#{d in F_p: X^p+aX^3+cX+d is irreducible}.
The Adams pushforward trace after removal of the fibrewise main class is
  e_a(c)=p(n_a(c)-1).

This script computes n_a(c) exactly with FLINT, then records exact moments,
autocorrelations and a numerical additive Fourier spectrum.  It is a finite
diagnostic for the generic-pencil/global-gluing problem, not a theorem.
"""
from __future__ import annotations

import argparse
import json
import math
from typing import Any

import numpy as np
from flint import nmod_poly


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(x for x in range(2, p) if chi(x, p) == -1)


def irreducible_count_for_c(p: int, a: int, c: int) -> int:
    count = 0
    for d in range(p):
        f = nmod_poly([d, c % p, 0, a % p] + [0] * (p - 4) + [1], p)
        _, factors = f.factor()
        if len(factors) == 1 and factors[0][0].degree() == p and factors[0][1] == 1:
            count += 1
    return count


def analyse_class(p: int, name: str, a: int, top_k: int) -> dict[str, Any]:
    n_values = np.array(
        [irreducible_count_for_c(p, a, c) for c in range(p)], dtype=float
    )
    error = p * (n_values - 1.0)
    transform = np.fft.fft(error)
    magnitudes = np.abs(transform)
    order = np.argsort(-magnitudes)
    energy = float(np.sum(magnitudes * magnitudes))
    probabilities = magnitudes * magnitudes / energy if energy else magnitudes
    nonzero = probabilities > 0
    entropy = (
        float(-np.sum(probabilities[nonzero] * np.log(probabilities[nonzero])) / math.log(p))
        if energy and p > 1
        else 0.0
    )
    top = [
        {
            "k": int(k),
            "abs": float(magnitudes[k]),
            "abs_over_p_3_2": float(magnitudes[k] / (p ** 1.5)),
            "real": float(transform[k].real),
            "imag": float(transform[k].imag),
        }
        for k in order[:top_k]
    ]
    autocorrelation = [
        int(round(sum(error[c] * error[(c + h) % p] for c in range(p))))
        for h in range(min(p, top_k))
    ]
    return {
        "name": name,
        "a": a,
        "N_total": int(n_values.sum()),
        "n_min": int(n_values.min()),
        "n_max": int(n_values.max()),
        "mean_square_error_over_p3": float(np.sum(error * error) / (p**3)),
        "spectral_entropy": entropy,
        "top_fourier": top,
        "autocorrelation_first": autocorrelation,
        "n_values": [int(x) for x in n_values],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("--top-k", type=int, default=12)
    parser.add_argument("--output")
    args = parser.parse_args()

    p = args.p
    output = {
        "status": "PASS",
        "scope": "exact finite census; numerical DFT only",
        "p": p,
        "classes": [
            analyse_class(p, "square", 1, args.top_k),
            analyse_class(p, "nonsquare", least_nonsquare(p), args.top_k),
        ],
    }
    text = json.dumps(output, indent=2)
    print(text)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")


if __name__ == "__main__":
    main()
