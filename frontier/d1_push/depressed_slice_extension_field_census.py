#!/usr/bin/env sage-python
"""Exact extension-field census for the depressed d=1 slice.

For fixed characteristic prime p and q=p^r, count
  N_a(q)=#{(c,d) in F_q^2 : X^p+aX^3+cX+d irreducible over F_q}.

The cohomological trace normalization is
  A_r = p*N_a(q)-q^2.

Run under Sage, e.g.
  sage -python depressed_slice_extension_field_census.py 5 --max-r 5 --workers 56

All arithmetic and irreducibility tests are exact.
"""
from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import time
from sage.all import GF, PolynomialRing, is_prime

F = R = x = ELS = AA = None
P = Q = 0


def init_worker(p: int, r: int, a_int: int) -> None:
    global F, R, x, ELS, AA, P, Q
    P = p
    Q = p ** r
    F = GF(Q, name="z")
    R = PolynomialRing(F, "x")
    x = R.gen()
    ELS = list(F)
    AA = F.fetch_int(a_int) if r > 1 else F(a_int)


def count_for_c(i: int) -> int:
    c = ELS[i]
    n = 0
    base = x ** P + AA * x ** 3 + c * x
    for d in ELS:
        if (base + d).is_irreducible():
            n += 1
    return n


def nonsquare_mod_p(p: int) -> int:
    for a in range(2, p):
        if pow(a, (p - 1) // 2, p) == p - 1:
            return a
    raise RuntimeError("no nonsquare found")


def count_case(p: int, r: int, a_int: int, workers: int) -> dict:
    q = p ** r
    started = time.time()
    ctx = mp.get_context("fork")
    with ctx.Pool(workers, initializer=init_worker, initargs=(p, r, a_int)) as pool:
        n = sum(pool.imap_unordered(count_for_c, range(q), chunksize=1))
    trace = p * n - q * q
    row = {
        "p": p,
        "r": r,
        "q": q,
        "a_int": a_int,
        "N": int(n),
        "main_numerator_q2": int(q * q),
        "trace_A_r_pN_minus_q2": int(trace),
        "abs_trace_over_q_3_2": float(abs(trace) / (q ** 1.5)),
        "elapsed_seconds": time.time() - started,
    }
    print(json.dumps(row), flush=True)
    return row


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("p", type=int)
    ap.add_argument("--max-r", type=int, default=4)
    ap.add_argument("--workers", type=int, default=48)
    ap.add_argument("--classes", choices=("square", "both"), default="both")
    args = ap.parse_args()
    if not is_prime(args.p) or args.p < 5:
        raise SystemExit("p must be a prime >=5")
    representatives = [(1, "square")]
    if args.classes == "both":
        representatives.append((nonsquare_mod_p(args.p), "nonsquare_over_Fp"))
    rows = []
    for r in range(1, args.max_r + 1):
        for a_int, label in representatives:
            row = count_case(args.p, r, a_int, args.workers)
            row["base_class"] = label
            row["class_over_Fq"] = (
                "square" if label == "square" or r % 2 == 0 else "nonsquare"
            )
            rows.append(row)
    print(json.dumps({
        "status": "PASS",
        "method": "exact Sage finite-field enumeration and irreducibility certification",
        "p": args.p,
        "max_r": args.max_r,
        "workers": args.workers,
        "rows": rows,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
