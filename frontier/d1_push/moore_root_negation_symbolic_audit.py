#!/usr/bin/env python3
"""Exact symbolic and finite audit for MRN.4 and MRN.6.

Requires sympy and python-flint.
"""
from __future__ import annotations

import argparse
import json
from math import isqrt

import sympy as sp
from flint import nmod_poly


def symbolic_audit() -> dict:
    x, u, v, w, a, c, d, X = sp.symbols("x u v w a c d X")
    x0 = x
    x1 = x + u
    x2 = x + u + v
    y0 = x1 + a * x0**3
    y1 = x2 + a * x1**3
    y2 = x + u + v + w + a * x2**3
    det = sp.expand(u * (y2 - y0) - (u + v) * (y1 - y0))
    expected = sp.expand(
        3 * a * u * v * (u + v) * x
        + a * u * v * (2 * u**2 + 3 * u * v + v**2)
        + u * w
        - v**2
    )
    m = sp.symbols("m", integer=True, positive=True)
    # The root-negation composition is audited with an abstract H(X^2).
    H = sp.symbols("H")
    product = sp.expand((X * H + d) * (X * H - d))
    composition = sp.expand(X**2 * H**2 - d**2)
    return {
        "moore_expansion_pass": sp.expand(det - expected) == 0,
        "root_negation_product_pass": sp.expand(product - composition) == 0,
        "determinant": str(sp.factor(det)),
        "xi_numerator": str(
            sp.expand(v**2 - u * w - a * u * v * (2 * u**2 + 3 * u * v + v**2))
        ),
        "xi_denominator": str(3 * a * u * v * (u + v)),
    }


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * (((n - i * i) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def chi(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def least_nonsquare(p: int) -> int:
    return next(a for a in range(2, p) if chi(a, p) == -1)


def irreducible(f: nmod_poly) -> bool:
    _, fac = f.factor()
    return len(fac) == 1 and fac[0][1] == 1 and fac[0][0].degree() == f.degree()


def finite_case(p: int, a: int) -> dict:
    m = (p - 1) // 2
    mismatches = []
    n_f = 0
    n_g_square = 0
    squares = sorted({d * d % p for d in range(1, p)})
    y = nmod_poly([0, 1], p)
    for c in range(p):
        coeffs = [c, a] + [0] * max(0, m - 2) + [1]
        if m == 1:
            coeffs = [c, a + 1]
        h = nmod_poly(coeffs, p)
        for e in squares:
            g = y * h * h - e
            if irreducible(g):
                n_g_square += 1
        for d in range(1, p):
            f = nmod_poly([d, c, 0, a] + [0] * (p - 4) + [1], p)
            fm = nmod_poly([-d, c, 0, a] + [0] * (p - 4) + [1], p)
            g = y * h * h - (d * d % p)
            vals = (irreducible(f), irreducible(fm), irreducible(g))
            n_f += int(vals[0])
            if not (vals[0] == vals[1] == vals[2]):
                mismatches.append({"c": c, "d": d, "values": vals})
                if len(mismatches) >= 5:
                    break
        if mismatches:
            break
    return {
        "p": p,
        "a": a,
        "N_F": n_f,
        "N_G_square": n_g_square,
        "pass": not mismatches and n_f == 2 * n_g_square,
        "mismatches": mismatches,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=43)
    args = parser.parse_args()
    symbolic = symbolic_audit()
    rows = []
    for p in primes_upto(args.max_prime):
        if p < 5:
            continue
        for a in (1, least_nonsquare(p)):
            row = finite_case(p, a)
            rows.append(row)
            print(json.dumps(row), flush=True)
    out = {
        "status": "PASS"
        if symbolic["moore_expansion_pass"]
        and symbolic["root_negation_product_pass"]
        and all(row["pass"] for row in rows)
        else "FAIL",
        "symbolic": symbolic,
        "finite_rows": rows,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
