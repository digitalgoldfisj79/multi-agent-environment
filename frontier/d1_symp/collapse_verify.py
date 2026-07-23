#!/usr/bin/env python3
"""Exact verification of the collapse identity (Lemma 1, p = 2 mod 3).

Claim: for p = 2 (mod 3), with T_p := sum_{x in F_{p^p}, Tr x = 0} psi(Tr x^3),
    D_b = -T_p / p   for every b != 0,      D_0 = (p-1) T_p / p,
equivalently  p*D_b = -T_p  and  p*D_0 = (p-1)*T_p,  so D_0 = -(p-1)*D_b.

T_p is computed INDEPENDENTLY of the double-sum probe via
    sum_{u in F_p} S_p(u,1) = p * T_p
(S_p by the same degree-2 L-function recurrence, but only the p pairs
(u,1) instead of all p(p-1) pairs (u,v)).

For p = 5, 11, 17, 23 the full double-sum deviations(p) is recomputed and
both identities are asserted for every b.  For p = 29 the committed exact
value D_b = 27522246495265849219 (HALF_THEOREM_PROBE.md) is used and
p*D_b = -T_p is asserted.  All arithmetic exact in Z[zeta_p].
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'd1_halftheorem'))
from halftheorem_probe import (cyc_mul, S1_vec, S2_vec, halve, build_fp2,
                               deviations)

def sum_Sp_u_line(p):
    """Exact sum_{u in F_p} S_p(u,1) as a rational integer (asserts rationality)."""
    n_, elems, cubes = build_fp2(p)
    acc = [0]*(p-1)
    for u in range(p):
        P1 = [-c for c in S1_vec(u, 1, p)]
        P2 = [-c for c in S2_vec(u, 1, p, elems, cubes)]
        E2 = halve([a - b for a, b in zip(cyc_mul(P1, P1, p), P2)])
        Pm2, Pm1 = P1, P2
        for _ in range(3, p+1):
            Pr = [a - b for a, b in zip(cyc_mul(P1, Pm1, p),
                                        cyc_mul(E2, Pm2, p))]
            Pm2, Pm1 = Pm1, Pr
        Sp = [-c for c in Pm1]          # S_p(u,1) = -(alpha^p + beta^p)
        acc = [a + s for a, s in zip(acc, Sp)]
    assert all(c == 0 for c in acc[1:]), f"sum_u S_p(u,1) not rational at p={p}: {acc}"
    return acc[0]

COMMITTED_DB = {29: 27522246495265849219}   # HALF_THEOREM_PROBE.md, exact

if __name__ == "__main__":
    for p in (5, 11, 17, 23, 29):
        assert p % 3 == 2
        total = sum_Sp_u_line(p)
        assert total % p == 0, f"sum_u S_p(u,1) not divisible by p at p={p}"
        T = total // p                      # T_p = (1/p) sum_u S_p(u,1)
        if p in COMMITTED_DB:
            Db = COMMITTED_DB[p]
            assert p*Db == -T, f"p*D_b != -T_p at p={p}: {p*Db} vs {-T}"
            print(f"p={p}: T_p = {T};  p*D_b = -T_p OK (committed D_b);"
                  f"  => D_0 = -(p-1)*D_b by Lemma 1")
        else:
            D = deviations(p)               # independent full double sum
            for b in range(1, p):
                assert p*D[b] == -T, f"p*D_{b} != -T_p at p={p}"
            assert p*D[0] == (p-1)*T, f"p*D_0 != (p-1)*T_p at p={p}"
            print(f"p={p}: T_p = {T};  all b!=0: p*D_b = -T_p OK;"
                  f"  p*D_0 = (p-1)*T_p OK  (D_0 = {D[0]})")
    print("ALL COLLAPSE IDENTITIES VERIFIED EXACTLY")
