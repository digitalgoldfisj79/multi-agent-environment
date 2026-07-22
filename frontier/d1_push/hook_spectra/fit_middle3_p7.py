#!/usr/bin/env python3
"""
FE-powered structured fits for p=7 middle hooks V_2 (23), V_3 (32), V_4 (23).

The weight-1 part of H^1_c is pure and self-dual (V_i self-dual), so its
L-factor W1 (degree 2m) satisfies c_{2m-k} = 7^{m-k} c_k. Fit:
  L_i = prod_d Phi_d^{e_d} * W1,   slots d per q (puncture products, x2 for twists)
Newton on residual power sums r_1..r_m gives c_1..c_m; FE gives the rest;
validate on r_{m+1}..r_{jmax} and |roots| = sqrt 7. Allows 2m up to 2*jmax-2ish
with real out-of-sample validation.
"""
import json, os, sys
from fractions import Fraction
from math import gcd
import numpy as np

P = 7
JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
MMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 6
H = {2: 23, 3: 32, 4: 23}
PHI_DEG = {1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 2, 8: 4, 10: 4, 12: 4}
SLOTS_PLAIN = {1: [1, 2, 5], 3: [1, 2, 3], 4: [1, 2, 4], 5: [1, 2, 3, 6], 6: [1, 2, 5]}
SLOTS_TWIST = {1: [1, 2, 5, 10], 3: [1, 2, 3, 6], 4: [1, 2, 4, 8],
               5: [1, 2, 3, 6], 6: [1, 2, 5, 10]}

def mobius(n):
    r, d = 1, 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0: return 0
            r = -r
        d += 1
    return -r if n > 1 else r

def phi_euler(n):
    r, d, m = n, 2, n
    while d * d <= m:
        if m % d == 0:
            while m % d == 0: m //= d
            r -= r // d
        d += 1
    if m > 1: r -= r // m
    return r

def ramanujan(d, j):
    g = gcd(d, j)
    return mobius(d // g) * phi_euler(d) // phi_euler(d // g)

def enum_exponents(slots, total):
    if not slots:
        if total == 0: yield ()
        return
    dd = PHI_DEG[slots[0]]
    for e in range(total // dd + 1):
        for rest in enum_exponents(slots[1:], total - e * dd):
            yield (e,) + rest

def fit(seq, h, slots, jmax, mmax):
    sols = []
    for m in range(0, mmax + 1):
        w0dim = h - 2 * m
        if w0dim < 0: break
        if m > jmax: break
        for evec in enum_exponents(slots, w0dim):
            r = {j: seq[j] - sum(e * ramanujan(d, j) for d, e in zip(slots, evec))
                 for j in range(1, jmax + 1)}
            if m == 0:
                if all(v == 0 for v in r.values()):
                    sols.append((dict(zip(slots, evec)), None))
                continue
            # Newton for c_1..c_m
            c = [Fraction(1)] + [Fraction(0)] * (2 * m)
            bad = False
            for j in range(1, m + 1):
                acc = Fraction(r[j])
                for k in range(1, j):
                    acc += c[k] * r[j - k]
                c[j] = -acc / j
                if c[j].denominator != 1:
                    bad = True; break
            if bad: continue
            for k in range(0, m):
                c[2 * m - k] = Fraction(7 ** (m - k)) * c[k]
            ci = [int(x) for x in c]
            # predict r_{m+1}..r_{jmax} via s_j = -(j c_j + sum_{k=1}^{j-1} c_k s_{j-k})
            rr = {j: Fraction(r[j]) for j in range(1, m + 1)}
            good = True
            for j in range(m + 1, jmax + 1):
                acc = Fraction(ci[j] * j) if j <= 2 * m else Fraction(0)
                for k in range(1, min(j - 1, 2 * m) + 1):
                    acc += Fraction(ci[k]) * rr[j - k]
                rr[j] = -acc
                if rr[j] != r[j]:
                    good = False; break
            if not good: continue
            rts = np.roots(ci[::-1])
            if not all(abs(abs(1 / z) - 7 ** 0.5) < 1e-5 for z in rts):
                continue
            sols.append((dict(zip(slots, evec)), ci))
    return sols

def main():
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
        qq, rr = sp.div(sp.Poly(sp.expand(prod), t), sp.Poly(1 + t, t))
        ETAB[typ] = tuple(int(qq.coeff_monomial(t**i)) for i in range(P))
    for q in [1, 3, 4, 5, 6]:
        data = {}
        for j in range(1, JMAX + 1):
            fn = f"cycle_counts_p7_j{j}_q{q}.json"
            if not os.path.exists(fn): break
            data[j] = {tuple(map(int, k.split(","))): v
                       for k, v in json.load(open(fn)).items()}
        if not data: continue
        jmax = max(data)
        print(f"\n===== q={q} (jmax={jmax}) =====")
        for i in (2, 3, 4):
            Pj = {j: -sum(n * ETAB[typ][i] for typ, n in data[j].items())
                  for j in sorted(data)}
            slots = (SLOTS_PLAIN if i == 2 else SLOTS_TWIST)[q]
            sols = fit(Pj, H[i], slots, jmax, MMAX)
            print(f"V_{i} (h={H[i]}): {len(sols)} solution(s)")
            for evec, c in sols:
                w0 = " ".join(f"Phi{d}^{e}" for d, e in evec.items() if e)
                nval = jmax - (len(c) - 1) // 2 if c else jmax
                print(f"   {w0}  W1={c}  [{nval} validation j's]")

if __name__ == "__main__":
    main()
