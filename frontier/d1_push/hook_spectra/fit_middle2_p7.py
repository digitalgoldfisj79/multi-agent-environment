#!/usr/bin/env python3
"""
Generalized structured spectral fits for p=7 middle hooks V_2, V_3, V_4.

L_i = prod_d Phi_d(T)^{e_d}  *  W1(T),
with per-q cyclotomic slots d (from puncture eigenvalue products, x(-1) for
sgn-twisted hooks), and W1 an arbitrary integer Weil-q polynomial of degree
2m = h_i - sum_d e_d deg(Phi_d), reconstructed by Newton from the residual
power sums (needs 2m <= jmax), then checked: functional equation
c_{2m-k} = 7^{m-k} c_k and all reciprocal roots |.| = sqrt(7), plus match on
every remaining j.
"""
import json, os, sys
from fractions import Fraction
from math import gcd
import numpy as np

P = 7
JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7
H = {2: 23, 3: 32, 4: 23}
PHI_DEG = {1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 2, 8: 4, 10: 4, 12: 4}

SLOTS_PLAIN = {1: [1, 2, 5], 3: [1, 2, 3], 4: [1, 2, 4], 5: [1, 2, 3, 6], 6: [1, 2, 5]}
SLOTS_TWIST = {1: [1, 2, 5, 10], 3: [1, 2, 3, 6], 4: [1, 2, 4, 8],
               5: [1, 2, 3, 6], 6: [1, 2, 5, 10]}

def mobius(n):
    r = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0: return 0
            r = -r
        d += 1
    if n > 1: r = -r
    return r

def phi_euler(n):
    r = n; d = 2; m = n
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

def newton_poly(r, deg):
    """char poly coeffs c[0..deg] (c0=1) from power sums r[1..deg]; None if non-integer."""
    c = [Fraction(1)] + [Fraction(0)] * deg
    for j in range(1, deg + 1):
        acc = Fraction(r[j])
        for m in range(1, j):
            acc += c[m] * r[j - m]
        c[j] = -acc / j
    if not all(x.denominator == 1 for x in c): return None
    return [int(x) for x in c]

def weil_check(c, m):
    """c: coeffs of degree 2m poly. functional eq + |roots| = sqrt7."""
    for k in range(0, m + 1):
        if c[2 * m - k] != 7 ** (m - k) * c[k]: return False
    rts = np.roots(c[::-1])
    return all(abs(abs(1 / r) - 7 ** 0.5) < 1e-6 for r in rts if r != 0)

def predict(r_known, c, jmax):
    s = dict(r_known)
    h = len(c) - 1
    for j in range(max(r_known) + 1, jmax + 1):
        s[j] = -sum(c[m] * s[j - m] for m in range(1, min(h, j - 1) + 1) if j - m >= 1) \
               - (c[j] * j if j <= h else 0)
    return s

def enum_exponents(slots, total):
    """all nonneg integer vectors e with sum e_d*deg_d = total"""
    if not slots:
        if total == 0: yield ()
        return
    d = slots[0]
    dd = PHI_DEG[d]
    for e in range(total // dd + 1):
        for rest in enum_exponents(slots[1:], total - e * dd):
            yield (e,) + rest

def fit(seq, h, slots, jmax):
    sols = []
    for m in range(0, min(4, jmax // 2) + 1):
        w0dim = h - 2 * m
        if w0dim < 0: break
        for evec in enum_exponents(slots, w0dim):
            res = {j: seq[j] - sum(e * ramanujan(d, j)
                                   for d, e in zip(slots, evec))
                   for j in range(1, jmax + 1)}
            if m == 0:
                if all(res[j] == 0 for j in res):
                    sols.append((dict(zip(slots, evec)), None))
                continue
            c = newton_poly(res, 2 * m)
            if c is None: continue
            if not weil_check(c, m): continue
            pred = predict({j: Fraction(res[j]) for j in range(1, 2 * m + 1)},
                           [Fraction(x) for x in c], jmax)
            if all(pred[j] == res[j] for j in range(2 * m + 1, jmax + 1)):
                sols.append((dict(zip(slots, evec)), c))
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
        qq, r = sp.div(sp.Poly(sp.expand(prod), t), sp.Poly(1 + t, t))
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
            sols = fit(Pj, H[i], slots, jmax)
            print(f"V_{i} (h={H[i]}, slots {slots}): {len(sols)} solution(s)")
            for evec, c in sols:
                w0 = " ".join(f"Phi{d}^{e}" for d, e in evec.items() if e)
                w1 = "" if c is None else f"  W1 = {c}"
                print(f"   {w0}{w1}")

if __name__ == "__main__":
    main()
