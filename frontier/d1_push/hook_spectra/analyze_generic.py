#!/usr/bin/env python3
"""
Generic hook-spectra analysis from cycle-type census files
cycle_counts_p{P}_j{j}_q{q}.json.

Computes: e_i tables for all partitions of p, ledger dims h_i,
power sums P_j(i) = Tr(F^j|H^1_c(U,V_i)), char polys where j-range suffices,
validation on extra j, factorization over Q, even/odd cancellation,
virtual E_j table.

Usage: analyze_generic.py p jmax [q ...]
"""
import json, os, sys
from fractions import Fraction
from collections import Counter
import sympy as sp

P = int(sys.argv[1])
JMAXA = int(sys.argv[2])
QL = [int(x) for x in sys.argv[3:]] or [q for q in range(1, P) if q != 2]
T = sp.symbols('T')

def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield (); return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

def build_etab(p):
    t = sp.symbols('t')
    tab = {}
    for typ in partitions(p):
        prod = 1
        for d in typ:
            prod *= (1 - (-t)**d)
        qpoly, r = sp.div(sp.Poly(sp.expand(prod), t), sp.Poly(1 + t, t))
        assert r.is_zero
        tab[typ] = tuple(int(qpoly.coeff_monomial(t**i)) for i in range(p))
    return tab

def ledger_dims(p):
    from math import comb
    h = []
    for i in range(p):
        r = comb(p - 1, i)
        a = (comb(p - 1, i) + (p - 1) * (-1)**i)
        assert a % p == 0
        a //= p
        s = Fraction(p - 3, p - 1) * (r - a)
        assert s.denominator == 1
        h.append(r + int(s) + (1 if i == 0 else 0))
    return h

ETAB = build_etab(P)
H = ledger_dims(P)
print(f"p={P}: ledger h_i = {H}  (even {sum(H[0::2])}, odd {sum(H[1::2])}, virtual {sum(H[0::2])-sum(H[1::2])})")

def newton_charpoly(s, h):
    c = [Fraction(1)] + [Fraction(0)] * h
    for j in range(1, h + 1):
        acc = Fraction(s[j])
        for m in range(1, j):
            acc += c[m] * s[j - m]
        c[j] = -acc / j
    return c

def main():
    for q in QL:
        data = {}
        for j in range(1, JMAXA + 1):
            fn = f"cycle_counts_p{P}_j{j}_q{q}.json"
            if not os.path.exists(fn): break
            data[j] = {tuple(map(int, k.split(","))): v
                       for k, v in json.load(open(fn)).items()}
        if not data:
            print(f"q={q}: no data"); continue
        jmax = max(data)
        Pj = {i: {} for i in range(P)}
        Ej = {}
        for j in sorted(data):
            Tv = [0] * P
            for typ, n in data[j].items():
                e = ETAB[typ]
                for i in range(P):
                    Tv[i] += n * e[i]
            for i in range(P):
                Pj[i][j] = (P**j if i == 0 else 0) - Tv[i]
            irr = data[j].get((P,), 0)
            Ej[j] = P**j - P * irr
            alt = sum((-1)**i * Pj[i][j] for i in range(P))
            assert alt == Ej[j], (q, j, alt, Ej[j])
        print(f"\n================ p={P} q={q} (jmax={jmax}) ================")
        Lfacs = {}
        for i in range(P):
            h = H[i]
            print(f"i={i} (h={h}): P_j = {[Pj[i][j] for j in sorted(Pj[i])]}")
            if jmax < h:
                continue
            c = newton_charpoly(Pj[i], h)
            if not all(x.denominator == 1 for x in c):
                print(f"   NON-INTEGER charpoly! {c}"); continue
            ci = [int(x) for x in c]
            # validate
            ok, bad = True, []
            svals = {j: Fraction(Pj[i][j]) for j in range(1, h + 1)}
            for j in range(h + 1, jmax + 1):
                pred = -sum(c[m] * svals[j - m] for m in range(1, h + 1))
                svals[j] = pred
                if pred != Pj[i][j]:
                    ok = False; bad.append(j)
            Lp = sum(ci[k] * T**k for k in range(h + 1))
            fac = sp.factor_list(sp.Poly(Lp, T))
            Lfacs[i] = fac
            facstr = " * ".join((f"({sp.expand(f.as_expr() if hasattr(f,'as_expr') else f)})" +
                                 (f"^{m}" if m > 1 else ""))
                                for f, m in fac[1])
            print(f"   L_{i}(T) = {facstr}   validated j={h+1}..{jmax}: {ok} {bad if bad else ''}")
        if len(Lfacs) == P:
            ev, od = Counter(), Counter()
            for i, fac in Lfacs.items():
                tgt = ev if i % 2 == 0 else od
                for f, m in fac[1]:
                    tgt[sp.expand(f.as_expr() if hasattr(f, 'as_expr') else f)] += m
            common = Counter()
            for f in set(ev) | set(od):
                cm = min(ev.get(f, 0), od.get(f, 0))
                if cm:
                    common[f] = cm; ev[f] -= cm; od[f] -= cm
            ev = +ev; od = +od
            print("--- even/odd cancellation ---")
            print("cancelled:", {str(f): m for f, m in common.items()})
            print("SURVIVING even:", {str(f): m for f, m in ev.items()})
            print("SURVIVING odd :", {str(f): m for f, m in od.items()})
            dev = sum(sp.degree(f, T) * m for f, m in ev.items())
            dod = sum(sp.degree(f, T) * m for f, m in od.items())
            print(f"surviving degree: even {dev}, odd {dod}, virtual {dev-dod} (ledger {4-P})")
        print("virtual E_j:", [Ej[j] for j in sorted(Ej)])

if __name__ == "__main__":
    main()
