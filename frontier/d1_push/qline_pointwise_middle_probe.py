#!/usr/bin/env python3
"""Exact pointwise primitive q-line trace diagnostic.

For every generic normal-form cell q != 0,2, compute the split and nonsplit
irreducible-fibre Adams traces, subtract the exact Kummer, pair and D traces
pointwise, and retain the primitive middle functions m_+(q), m_-(q).

The selected sums reproduce E_middle for the two cubic square classes.  The
moments and additive Fourier spectra are finite diagnostics for the global
localization/effective-degree problem; they are not asymptotic theorems.
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


def inv(x: int, p: int) -> int:
    return pow(x % p, p - 2, p)


def irreducible_count(p: int, a3: int, a1: int) -> int:
    count = 0
    for d in range(p):
        polynomial = nmod_poly(
            [d, a1 % p, 0, a3 % p] + [0] * (p - 4) + [1], p
        )
        _, factors = polynomial.factor()
        if (
            len(factors) == 1
            and factors[0][0].degree() == p
            and factors[0][1] == 1
        ):
            count += 1
    return count


def pair_anti_trace(p: int, q: int) -> int:
    """Trace on H^1(B_q)^- from the curve and its d -> -d quotient."""
    inv3 = inv(3, p)
    leading = (-4 * q * inv3) % p

    total_sum = 0
    for d in range(p):
        value = (12 - d * d - 4 * q * pow(d, p - 1, p)) * inv3 % p
        total_sum += chi(value, p)
    total_trace = -total_sum - chi(leading, p)  # even degree p-1

    m = (p - 1) // 2
    quotient_sum = 0
    for r in range(p):
        value = (12 - r - 4 * q * pow(r, m, p)) * inv3 % p
        quotient_sum += chi(value, p)
    quotient_trace = -quotient_sum
    if m % 2 == 0:
        quotient_trace -= chi(leading, p)

    return total_trace - quotient_trace


def split_d_trace(p: int, q: int) -> int:
    m = (p - 1) // 2
    kappa = (3 * (-1 if m & 1 else 1)) % p
    character_sum = 0
    for z in range(p):
        gp = (q * pow((z - 1) % p, p - 2, p) + z + 2) % p
        gm = (q * pow((z + 1) % p, p - 2, p) + z - 2) % p
        character_sum += chi(kappa * q * gp * gm, p)
    return -character_sum - chi(kappa * q, p)


def nonsplit_d_trace(p: int, q: int) -> int:
    m = (p - 1) // 2
    epsilon = chi(((-1) ** m) * 3, p)
    delta = chi(-1, p)
    subtotal = 0
    for r in range(1, p):
        if chi(r, p) != -1:
            continue
        value = (r * (r - q - 3) ** 2 - (q - 2) ** 2) % p
        subtotal += chi(value, p)
    return epsilon * chi(q, p) * ((1 - delta) - 2 * subtotal)


def primitive_rows(p: int) -> list[dict[str, int]]:
    eta = least_nonsquare(p)
    m = (p - 1) // 2
    epsilon = chi(((-1) ** m) * 3, p)
    rows = []
    for q in range(1, p):
        if q == 2:
            continue
        n_plus = irreducible_count(p, inv(q, p), -3 * inv(q, p))
        n_minus = irreducible_count(
            p, -inv(eta * q, p), 3 * inv(q, p)
        )
        e_plus = p - p * n_plus
        e_minus = p - p * n_minus
        pair = pair_anti_trace(p, q)
        d_plus = split_d_trace(p, q)
        d_minus = nonsplit_d_trace(p, q)
        k_plus = epsilon * chi(q, p)
        k_minus = -k_plus
        middle_plus = e_plus - (k_plus + pair - d_plus)
        middle_minus = e_minus - (k_minus + pair - d_minus)
        rows.append(
            {
                "q": q,
                "chi_q": chi(q, p),
                "n_plus": n_plus,
                "n_minus": n_minus,
                "E_plus": e_plus,
                "E_minus": e_minus,
                "K_plus": k_plus,
                "K_minus": k_minus,
                "B": pair,
                "D_plus": d_plus,
                "D_minus": d_minus,
                "middle_plus": middle_plus,
                "middle_minus": middle_minus,
            }
        )
    return rows


def spectrum(values: list[int], p: int, top_k: int) -> dict[str, Any]:
    # Missing q=0,2 values are extended by zero for the additive DFT.
    array = np.zeros(p, dtype=float)
    for q, value in values:
        array[q] = value
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
        "max_abs_over_p": float(np.max(np.abs(array)) / p),
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("--top-k", type=int, default=12)
    parser.add_argument("--output")
    args = parser.parse_args()

    p = args.p
    delta = chi(-1, p)
    rows = primitive_rows(p)
    selections = []
    for A in (1, -1):
        selected_plus = [r for r in rows if r["chi_q"] == A]
        selected_minus = [r for r in rows if r["chi_q"] == -delta * A]
        value = sum(r["middle_plus"] for r in selected_plus) + sum(
            r["middle_minus"] for r in selected_minus
        )
        selections.append(
            {
                "A": A,
                "selected_middle_sum": value,
                "selected_middle_over_p_3_2": value / (p ** 1.5),
                "split_cells": len(selected_plus),
                "nonsplit_cells": len(selected_minus),
            }
        )

    output = {
        "status": "PASS",
        "scope": "exact finite pointwise subtraction; numerical DFT only",
        "p": p,
        "rows": rows,
        "selections": selections,
        "middle_plus_spectrum": spectrum(
            [(r["q"], r["middle_plus"]) for r in rows], p, args.top_k
        ),
        "middle_minus_spectrum": spectrum(
            [(r["q"], r["middle_minus"]) for r in rows], p, args.top_k
        ),
    }
    text = json.dumps(output, indent=2)
    print(text)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")


if __name__ == "__main__":
    main()
