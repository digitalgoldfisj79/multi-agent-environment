#!/usr/bin/env python3
"""
Analysis of p=5 cycle-type census:
  cycle counts -> T_j(V_i) -> P_j(i) = Tr(F^j | H^1_c(U,V_i)) -> char polys L_i(T)
  (Newton identities, exact rationals) -> factor over Q -> even/odd cancellation.

L_i(T) = det(1 - T Frob | H^1_c) has degree h_i = (2,6,8,6,1) for i = 0..4.
Validation: j beyond h_i must satisfy the linear recurrence from L_i.
"""
import json, sys
from fractions import Fraction
import sympy as sp

P = 5
H = [2, 6, 8, 6, 1]              # ledger dims h_i, i = 0..4
ETAB = {
    (1,1,1,1,1): (1, 4, 6, 4, 1),
    (2,1,1,1):   (1, 2, 0,-2,-1),
    (2,2,1):     (1, 0,-2, 0, 1),
    (3,1,1):     (1, 1, 0, 1, 1),
    (3,2):       (1,-1, 0, 1,-1),
    (4,1):       (1, 0, 0, 0,-1),
    (5,):        (1,-1, 1,-1, 1),
}

def load_files(qlist, jmax):
    import os
    out = {}
    for q in qlist:
        out[q] = {}
        for j in range(1, jmax + 1):
            fn = f"cycle_counts_p5_j{j}_q{q}.json"
            if not os.path.exists(fn):
                break
            cts = json.load(open(fn))
            out[q][j] = {tuple(map(int, k.split(","))): v for k, v in cts.items()}
    return out

def trace_sums(counts_j):
    """T_j(V_i) for i=0..4 from one census dict."""
    T = [0]*5
    for typ, n in counts_j.items():
        e = ETAB[typ]
        for i in range(5):
            T[i] += n * e[i]
    return T

def newton_charpoly(s, h):
    """L(T)=1+c1 T+...+ch T^h from power sums s[1..h] of reciprocal roots."""
    c = [Fraction(1)] + [Fraction(0)]*h
    for j in range(1, h+1):
        acc = Fraction(s[j])
        for m in range(1, j):
            acc += c[m] * s[j-m]
        c[j] = -acc / j
    return c

def predict(s_known, c, jmax):
    """Extend power sums via recurrence s_j = -(c1 s_{j-1}+...+ch s_{j-h})."""
    h = len(c) - 1
    s = dict(s_known)
    for j in range(h+1, jmax+1):
        acc = Fraction(0)
        for m in range(1, h+1):
            acc += c[m] * s[j-m]
        # exact Newton for j>h: s_j = -(sum_{m=1}^{h} c_m s_{j-m})  (c_j=0 for j>h)
        s[j] = -acc
    return s

def main():
    jmax_arg = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    data = load_files([1, 3, 4], jmax_arg)
    T = sp.symbols('T')
    results = {}
    for q in sorted(data):
        per_j = data[q]
        jmax = max(per_j)
        # power sums P_j(i)
        Pj = {i: {} for i in range(5)}
        Ej = {}
        for j in sorted(per_j):
            Ts = trace_sums(per_j[j])
            for i in range(5):
                Pj[i][j] = (P**j if i == 0 else 0) - Ts[i]
            # virtual (even - odd) trace = 5^j - 5*#irred
            irr = per_j[j].get((5,), 0)
            Ej[j] = P**j - P*irr
            # consistency: sum_i (-1)^i P_j(i) == Ej
            alt = sum((-1)**i * Pj[i][j] for i in range(5))
            assert alt == Ej[j], (q, j, alt, Ej[j])
        print(f"\n================ q = {q} ================")
        Lpolys = {}
        for i in range(5):
            h = H[i]
            if jmax < h:
                print(f"i={i}: need j up to {h}, have {jmax}; skipping")
                continue
            c = newton_charpoly(Pj[i], h)
            assert all(x.denominator == 1 for x in c), (q, i, c)
            ci = [int(x) for x in c]
            # validation on j = h+1..jmax
            spred = predict({j: Fraction(Pj[i][j]) for j in range(1, h+1)}, c, jmax)
            ok = all(spred[j] == Pj[i][j] for j in range(h+1, jmax+1))
            Lp = sum(ci[k]*T**k for k in range(h+1))
            fac = sp.factor_list(sp.Poly(Lp, T))
            Lpolys[i] = (ci, fac)
            facstr = " * ".join(f"({sp.factor(f)})^{m}" if m > 1 else f"({sp.factor(f)})"
                                for f, m in fac[1])
            const = fac[0]
            print(f"i={i} (h={h}): L_{i}(T) = {sp.expand(Lp)}")
            print(f"    factored: {const} * {facstr}")
            print(f"    recurrence validated on j={h+1}..{jmax}: {ok}")
            if not ok:
                bad = [j for j in range(h+1, jmax+1) if spred[j] != Pj[i][j]]
                print(f"    MISMATCH at j={bad}")
                print("    observed:", {j: Pj[i][j] for j in bad})
                print("    predicted:", {j: int(spred[j]) for j in bad})
        # even/odd multiset comparison via factorizations
        if all(i in Lpolys for i in range(5)):
            from collections import Counter
            ev, od = Counter(), Counter()
            for i, (ci, fac) in Lpolys.items():
                tgt = ev if i % 2 == 0 else od
                for f, m in fac[1]:
                    tgt[sp.Poly(f, T).as_expr()] += m
            common = {}
            for f in set(ev) | set(od):
                cmn = min(ev.get(f, 0), od.get(f, 0))
                if cmn:
                    common[f] = cmn
                    ev[f] -= cmn; od[f] -= cmn
            ev = +ev; od = +od
            print("--- even/odd cancellation (irreducible factors over Q) ---")
            print("cancelled (in both):", {str(f): m for f, m in common.items()})
            print("SURVIVING even:", {str(f): m for f, m in ev.items()})
            print("SURVIVING odd :", {str(f): m for f, m in od.items()})
            dev = sum(sp.degree(f, T)*m for f, m in ev.items())
            dod = sum(sp.degree(f, T)*m for f, m in od.items())
            print(f"surviving degrees: even {dev}, odd {dod}  (virtual {dev-dod}, ledger 4-p = -1)")
            results[q] = dict(
                L={i: Lpolys[i][0] for i in Lpolys},
                cancelled={str(f): m for f, m in common.items()},
                surv_even={str(f): m for f, m in ev.items()},
                surv_odd={str(f): m for f, m in od.items()})
        # virtual power-sum table
        print("virtual E_j = Tr_even - Tr_odd (= 5^j - 5*#irred):",
              {j: Ej[j] for j in sorted(Ej)})
    with open("spectra_p5.json", "w") as fh:
        json.dump({str(k): v for k, v in results.items()}, fh, indent=1, default=str)

if __name__ == "__main__":
    main()
