#!/usr/bin/env python3
"""
Structured spectral fits for the p=7 middle hooks V_2, V_3, V_4 (dims 23, 32, 23).

Ansatz: L_i = (1-T)^a (1+T)^b Phi3^c Phi4^d Phi5^e * prod_{k=1}^m (1 - a_k T + 7 T^2),
with a..e >= 0, a+b+2c+2d+4e+2m = h_i, |a_k| <= 5 (Weil), m <= 4.

Method: enumerate weight-1 multisets {a_k}; subtract their power sums from the
census power sums; solve the 5 cyclotomic multiplicities linearly from j=1..5;
demand nonnegative integers, correct dimension, and match on all remaining j.
Report every solution (unique solution across j<=jmax = strong candidate).
"""
import json, os, sys
from itertools import combinations_with_replacement
from fractions import Fraction

P = 7
JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7
H = {2: 23, 3: 32, 4: 23}

def cyc_sums(jmax):
    rows = {}
    for j in range(1, jmax + 1):
        c1 = 1
        cm1 = (-1)**j
        c3 = -1 + (3 if j % 3 == 0 else 0)
        c4 = 0 if j % 2 else (2 if j % 4 == 0 else -2)
        c5 = -1 + (5 if j % 5 == 0 else 0)
        rows[j] = (c1, cm1, c3, c4, c5)
    return rows

def quad_powersums(a, jmax):
    """power sums of reciprocal roots of 1 - a T + 7 T^2"""
    s = {0: 2, 1: a}
    for j in range(2, jmax + 1):
        s[j] = a * s[j - 1] - 7 * s[j - 2]
    return s

def fit(seq, h, jmax):
    sols = []
    CY = cyc_sums(jmax)
    qs_cache = {a: quad_powersums(a, jmax) for a in range(-5, 6)}
    for m in range(0, 5):
        w0dim = h - 2 * m
        if w0dim < 0: break
        for combo in combinations_with_replacement(range(-5, 6), m):
            res = [seq[j] - sum(qs_cache[a][j] for a in combo)
                   for j in range(1, jmax + 1)]
            # solve alpha..eps from j=1..5 (5x5 linear system)
            import numpy as np
            A = np.array([CY[j] for j in range(1, 6)], dtype=float)
            rhs = np.array(res[:5], dtype=float)
            try:
                x = np.linalg.solve(A, rhs)
            except np.linalg.LinAlgError:
                continue
            xi = [round(v) for v in x]
            if any(abs(x[k] - xi[k]) > 1e-6 for k in range(5)): continue
            if any(v < 0 for v in xi): continue
            if xi[0] + xi[1] + 2*xi[2] + 2*xi[3] + 4*xi[4] != w0dim: continue
            ok = all(sum(c * v for c, v in zip(CY[j], xi)) == res[j - 1]
                     for j in range(6, jmax + 1))
            if ok:
                sols.append((tuple(xi), combo))
    return sols

def main():
    for q in [1, 3, 4, 5, 6]:
        data = {}
        for j in range(1, JMAX + 1):
            fn = f"cycle_counts_p7_j{j}_q{q}.json"
            if not os.path.exists(fn): break
            data[j] = {tuple(map(int, k.split(","))): v
                       for k, v in json.load(open(fn)).items()}
        if not data: continue
        jmax = max(data)
        # rebuild P_j(i) via e_i tables
        sys.path.insert(0, '.')
        import sympy as sp
        t = sp.symbols('t')
        def partitions(n, mx=None):
            if mx is None: mx = n
            if n == 0:
                yield (); return
            for k in range(min(n, mx), 0, -1):
                for rest in partitions(n - k, k):
                    yield (k,) + rest
        ETAB = {}
        for typ in partitions(P):
            prod = 1
            for d in typ:
                prod *= (1 - (-t)**d)
            qq, r = sp.div(sp.Poly(sp.expand(prod), t), sp.Poly(1 + t, t))
            ETAB[typ] = tuple(int(qq.coeff_monomial(t**i)) for i in range(P))
        print(f"\n===== q={q} (jmax={jmax}) =====")
        for i in (2, 3, 4):
            Pj = {}
            for j in sorted(data):
                Tv = sum(n * ETAB[typ][i] for typ, n in data[j].items())
                Pj[j] = -Tv
            sols = fit(Pj, H[i], jmax)
            print(f"V_{i} (h={H[i]}): {len(sols)} structured solution(s)")
            for (xi, combo) in sols:
                a, b, c, d, e = xi
                parts = []
                if a: parts.append(f"(1-T)^{a}")
                if b: parts.append(f"(1+T)^{b}")
                if c: parts.append(f"Phi3^{c}")
                if d: parts.append(f"Phi4^{d}")
                if e: parts.append(f"Phi5^{e}")
                for ak in combo:
                    parts.append(f"(1{'-' if ak>=0 else '+'}{abs(ak)}T+7T^2)")
                print("   L = " + " ".join(parts))

if __name__ == "__main__":
    main()
