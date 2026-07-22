#!/usr/bin/env python3
"""
Spectra of the degenerate q=2 slice at p=5: X^5+2X^3+X+d (cover of the d-line,
branch locus {0, oo} only). h^1_c dims unknown a priori (different inertia);
determined empirically: minimal h with integral Newton char poly that validates
all remaining j.
"""
import json
from fractions import Fraction
import sympy as sp

P = 5
ETAB = {
    (1,1,1,1,1): (1, 4, 6, 4, 1),
    (2,1,1,1):   (1, 2, 0,-2,-1),
    (2,2,1):     (1, 0,-2, 0, 1),
    (3,1,1):     (1, 1, 0, 1, 1),
    (3,2):       (1,-1, 0, 1,-1),
    (4,1):       (1, 0, 0, 0,-1),
    (5,):        (1,-1, 1,-1, 1),
}
T = sp.symbols('T')
data = {int(j): {tuple(map(int, k.split(','))): v for k, v in cts.items()}
        for j, cts in json.load(open('cycle_counts_p5_q2slice.json')).items()}
jmax = max(data)
for i in range(5):
    Pj = {}
    for j in sorted(data):
        Tv = sum(n * ETAB[typ][i] for typ, n in data[j].items())
        Pj[j] = (P**j if i == 0 else 0) - Tv
    print(f"i={i}: P_j = {[Pj[j] for j in sorted(Pj)]}")
    for h in range(0, jmax):
        c = [Fraction(1)] + [Fraction(0)] * h
        ok = True
        for j in range(1, h + 1):
            acc = Fraction(Pj[j])
            for m in range(1, j):
                acc += c[m] * Pj[j - m]
            c[j] = -acc / j
            if c[j].denominator != 1: ok = False; break
        if not ok: continue
        s = {j: Fraction(Pj[j]) for j in range(1, h + 1)}
        good = True
        for j in range(h + 1, jmax + 1):
            pred = -sum(c[m] * s[j - m] for m in range(1, h + 1))
            s[j] = pred
            if pred != Pj[j]: good = False; break
        if good:
            L = sum(int(c[k]) * T**k for k in range(h + 1))
            print(f"   h={h}: L = {sp.factor(L)}")
            break
    else:
        print("   no h < jmax fits")
