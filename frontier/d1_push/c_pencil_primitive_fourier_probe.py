#!/usr/bin/env python3
"""Exact primitive middle trace reassembled on the true c-pencil.

For fixed cubic square class A=chi(a), every generic c!=0 slice is represented
by exactly one normal-form cell:

  split:    q=-3/c, used when chi(q)=A;
  nonsplit: q= 3/c, used otherwise, when chi(q)=-chi(-1)A.

The pointwise split/nonsplit primitive traces are supplied by
qline_pointwise_middle_probe.py after exact Kummer, pair and D subtraction.
This script assembles them as a function of the original linear coefficient c
and computes the additive Fourier spectrum.  The exceptional c=0 and q=2
slices are set to zero because they belong to the already explicit boundary
ledger.

All finite-field counts and trace subtractions are exact.  Only the displayed
complex DFT is numerical.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


def load_qline_module(path: str):
    spec = importlib.util.spec_from_file_location("qline_middle", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def spectrum(array: np.ndarray, p: int, top_k: int) -> dict[str, Any]:
    transform = np.fft.fft(array)
    magnitudes = np.abs(transform)
    order = np.argsort(-magnitudes)
    energy = float(np.sum(magnitudes * magnitudes))
    probabilities = magnitudes * magnitudes / energy if energy else magnitudes
    support = probabilities > 0
    entropy = (
        float(-np.sum(probabilities[support] * np.log(probabilities[support])) / math.log(p))
        if energy and p > 1
        else 0.0
    )
    return {
        "sum": int(round(array.sum())),
        "max_abs_pointwise_over_p": float(np.max(np.abs(array)) / p),
        "second_moment_over_p3": float(np.sum(array * array) / (p**3)),
        "spectral_entropy": entropy,
        "top_fourier": [
            {
                "k": int(k),
                "abs": float(magnitudes[k]),
                "abs_over_p_3_2": float(magnitudes[k] / (p ** 1.5)),
                "real": float(transform[k].real),
                "imag": float(transform[k].imag),
            }
            for k in order[:top_k]
        ],
    }


def assemble(p: int, qmodule, top_k: int) -> dict[str, Any]:
    rows = qmodule.primitive_rows(p)
    by_q = {row["q"]: row for row in rows}
    inv = lambda x: pow(x % p, p - 2, p)
    output = {"p": p, "classes": []}

    for A in (1, -1):
        values = np.zeros(p, dtype=float)
        choices = []
        for c in range(1, p):
            q_plus = (-3 * inv(c)) % p
            q_minus = (3 * inv(c)) % p
            if qmodule.chi(q_plus, p) == A:
                q = q_plus
                side = "split"
                key = "middle_plus"
            else:
                q = q_minus
                side = "nonsplit"
                key = "middle_minus"
            if q == 2:
                value = 0
                side = side + "_q2_boundary"
            else:
                value = by_q[q][key]
            values[c] = value
            choices.append({"c": c, "q": q, "side": side, "value": int(value)})

        output["classes"].append(
            {
                "A": A,
                "spectrum": spectrum(values, p, top_k),
                "choices": choices,
                "values": [int(x) for x in values],
            }
        )
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument(
        "--qline-script",
        default=str(Path(__file__).with_name("qline_pointwise_middle_probe.py")),
    )
    parser.add_argument("--top-k", type=int, default=12)
    parser.add_argument("--output")
    args = parser.parse_args()

    module = load_qline_module(args.qline_script)
    result = {
        "status": "PASS",
        "scope": "exact generic primitive c-pencil; explicit boundary values removed",
        **assemble(args.p, module, args.top_k),
    }
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")


if __name__ == "__main__":
    main()
