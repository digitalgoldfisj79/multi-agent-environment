#!/usr/bin/env python3
"""Gate 2 opening: the correspondence form of the bilateral endpoint incidence
(companion to FF_GATE2_CORRESPONDENCE_NOTE_20260802.md).

Theorem C12-1 (proved in the note). Fix theta in F_q^* and c, d in F_q^*.
In IFA1's inverse-free system the partner primes are UNIQUELY determined:

    P | cLS + theta P'  ==>  P' = P + r1,  r1 = (-theta^{-1} c * LS) mod P,
    S | dLP + theta S'  ==>  S' = S + r2,  r2 = (-theta^{-1} d * LP) mod S,

(the only monic degree-k lift of the forced residue), so the simultaneous
bilateral incidence is the locus in (P, S, c, d)-space cut out by the TWO
residual divisibilities

    P' | cLS' - theta P     and     S' | dLP' - theta S,

with no quotient variables.  Corollaries: same-modulus contact P'=P or S'=S is
impossible for c,d != 0; classification cost drops from #pairs^2 to
#pairs*(q-1)^2.

This verifier:
  A. checks the correspondence enumeration against ground-truth pair-squared
     scans on the Round-11 panels (3,2),(5,2),(7,2),(3,3),(3,4) — exact set
     equality of {(P,S,P',S',c,d)};
  B. runs NEW deep classification panels (3,5),(3,6),(3,7),(5,3),(5,4),(5,5),
     (7,3),(7,4): components = transpose / resonant (q=3) / OTHER;
  C. tests Conjecture C12-2: c + d = 0 on every incidence, every panel;
  D. k=6 Delta panel on the resonant family (Gate-3 measurement): involution
     invariance and exact aggregates XX/XD/DX/DD/BB at k=6, m=11.

Usage: python3 ff_gate2_correspondence_audit.py [corr|delta6]
"""
import itertools, sys
from ff_t3_coset_audit import (trim, padd, pmul, pmod, irreducibles_upto,
                               lambda_sources, pow_poly_inverse)
from ff_class_correlation_exact import (pneg, psub, deg, zzero, zadd, zscale,
                                        zmul, zconj, zeq, Ahat_exact)
from ff_round11_independent_audit import (report, zint, pscale, primorial,
                                          mu_of, resonant_points, delta_exact)
import ff_round11_independent_audit as r11

def corr_enumerate(q, k):
    """All cross-distinct simultaneous bilateral incidences via C12-1.
    Returns set of (P, S, P', S', c, d); theta = 1."""
    Lpoly = primorial(q)
    irr = irreducibles_upto(k, q)
    band = irr[k]
    bset = set(band)
    out = set()
    for P in band:
        for S in band:
            if S == P:
                continue
            LSmP = pmod(pmul(Lpoly, S, q), P, q)
            LPmS = pmod(pmul(Lpoly, P, q), S, q)
            cands_c = []
            for c in range(1, q):
                r1 = pscale(LSmP, -c, q)
                assert r1, "r1 = 0 impossible for c != 0"
                Pp = padd(P, r1, q)
                if Pp in bset:
                    cands_c.append((c, Pp))
            if not cands_c:
                continue
            cands_d = []
            for d in range(1, q):
                r2 = pscale(LPmS, -d, q)
                assert r2, "r2 = 0 impossible for d != 0"
                Sp = padd(S, r2, q)
                if Sp in bset:
                    cands_d.append((d, Sp))
            for (c, Pp) in cands_c:
                for (d, Sp) in cands_d:
                    if Pp == Sp:
                        continue
                    if pmod(psub(pscale(pmul(Lpoly, Sp, q), c, q), P, q), Pp, q):
                        continue
                    if pmod(psub(pscale(pmul(Lpoly, Pp, q), d, q), S, q), Sp, q):
                        continue
                    out.add((P, S, Pp, Sp, c, d))
    return out

def ground_truth(q, k):
    """Pair-squared scan: cross-distinct simultaneous incidences with their
    scalar witnesses (theta = 1)."""
    Lpoly = primorial(q)
    irr = irreducibles_upto(k, q)
    band = irr[k]
    pairs = []
    for P in band:
        for S in band:
            if S == P:
                continue
            pairs.append((P, S, mu_of(P, S, Lpoly, 1, q),
                          mu_of(S, P, Lpoly, 1, q)))
    out = set()
    for (P, S, mu_a, nu_a) in pairs:
        for (Pp, Sp, mu_b, nu_b) in pairs:
            if Pp == P or Sp == S:
                continue
            Emu = psub(pmul(mu_a, Pp, q), pmul(mu_b, P, q), q)
            Enu = psub(pmul(nu_a, Sp, q), pmul(nu_b, S, q), q)
            if deg(Emu) == 0 and deg(Enu) == 0:
                out.add((P, S, Pp, Sp, Emu[0], Enu[0]))
    return out

def resonant_points_gen(q, k):
    """GENERALIZED resonant family (this audit): exists iff k >= q.
    Q with leading coefficient 2 and deg Q = k - q, so J_Q(T) = LQ - T is
    monic-degree-k-preserving in EVERY characteristic; S = P + eps*Q,
    P' = LQ - P, S' = LQ - S.  Reduces to the branch's char-3 family at q=3
    (2 = -1 mod 3)."""
    if k < q:
        return []
    Lpoly = primorial(q)
    irr = irreducibles_upto(k, q)
    band = set(irr[k])
    pts = []
    for P in irr[k]:
        for lowQ in itertools.product(range(q), repeat=k - q):
            Q = trim(list(lowQ) + [2 % q])
            LQ = pmul(Lpoly, Q, q)
            Pp = psub(LQ, P, q)
            for eps in range(1, q):
                S = padd(P, pscale(Q, eps, q), q)
                Sp = psub(LQ, S, q)
                if all(f in band for f in (P, S, Pp, Sp)) \
                        and P != S and Pp != Sp and P != Pp and S != Sp:
                    pts.append((P, S, Pp, Sp, Q, eps))
    return pts

def translation_points(q, k):
    """NEW translation family (this audit): exists iff k > q.
    R nonzero with deg R < k - q, gamma in F_q^*:
        S = P + gamma*R,  P' = P + L*R,  S' = S + L*R,
    all four prime.  Predicted witnesses c = -theta*gamma^{-1}, d = -c
    (S' - P' = S - P, against the reflection family's S' - P' = -(S - P))."""
    if k <= q:
        return []
    Lpoly = primorial(q)
    irr = irreducibles_upto(k, q)
    band = set(irr[k])
    pts = []
    for P in irr[k]:
        for Rc in itertools.product(range(q), repeat=k - q):
            R = trim(Rc)
            if not R:
                continue
            LR = pmul(Lpoly, R, q)
            Pp = padd(P, LR, q)
            if Pp not in band:
                continue
            for gam in range(1, q):
                S = padd(P, pscale(R, gam, q), q)
                Sp = padd(S, LR, q)
                if S in band and Sp in band and Pp != Sp and S != Sp:
                    pts.append((P, S, Pp, Sp, R, gam))
    return pts

def classify_panel(q, k, inc):
    """Split incidences: transpose / reflection (generalized resonant) /
    translation (new) / other."""
    n_t = n_r = n_tr = 0
    others = []
    res = {(P, S, Pp, Sp) for (P, S, Pp, Sp, Q, e) in resonant_points_gen(q, k)}
    tra = {(P, S, Pp, Sp): (R, g) for (P, S, Pp, Sp, R, g)
           in translation_points(q, k)}
    incset = {(P, S, Pp, Sp) for (P, S, Pp, Sp, c, d) in inc}
    # every generated translation point must be an actual incidence with the
    # predicted witnesses c = -gamma^{-1}, d = -c (theta = 1)
    ok_tra = all(key in incset for key in tra)
    wit = {(P, S, Pp, Sp): (c, d) for (P, S, Pp, Sp, c, d) in inc}
    for key, (R, g) in tra.items():
        if key in wit:
            c_pred = (-pow(g, q - 2, q)) % q
            if wit[key] != (c_pred, (-c_pred) % q):
                ok_tra = False
    for (P, S, Pp, Sp, c, d) in inc:
        if (Pp, Sp) == (S, P):
            n_t += 1
        elif (P, S, Pp, Sp) in res:
            n_r += 1
        elif (P, S, Pp, Sp) in tra:
            n_tr += 1
        else:
            others.append((P, S, Pp, Sp, c, d))
    return n_t, n_r, n_tr, others, res, tra, ok_tra

def section_corr():
    # A. ground-truth cross-checks on the Round-11 panels
    for (q, k) in ((3, 2), (5, 2), (7, 2), (3, 3), (3, 4)):
        gt = ground_truth(q, k)
        ce = corr_enumerate(q, k)
        report(f"A C12-1 correspondence = pair-squared scan, exact set equality "
               f"(q={q},k={k})", ce == gt, f"incidences={len(ce)}")
    # B. classification panels (correspondence only) + C. c+d=0 test
    print("   panel classification (cross-distinct simultaneous incidences):")
    all_cd_zero = ok_exhaust = ok_law = ok_wit = True
    for (q, k) in ((3, 2), (5, 2), (7, 2), (3, 3), (3, 4), (3, 5), (3, 6),
                   (3, 7), (5, 3), (5, 4), (5, 5), (7, 3), (7, 4)):
        inc = corr_enumerate(q, k)
        n_t, n_r, n_tr, others, res, tra, ok_tra = classify_panel(q, k, inc)
        cd = all((c + d) % q == 0 for (_, _, _, _, c, d) in inc)
        all_cd_zero = all_cd_zero and cd
        ok_exhaust = ok_exhaust and not others
        ok_wit = ok_wit and ok_tra
        if (len(inc) > 0) != (k >= q):
            ok_law = False
        print(f"     (q={q},k={k}): incidences={len(inc):5d}  "
              f"transpose={n_t:3d}  reflection={n_r:5d}  "
              f"translation={n_tr:5d}  OTHER={len(others):4d}  "
              f"[gen refl={len(res)}, gen tra={len(tra)}]  c+d=0: {cd}")
        for o in others[:4]:
            print(f"        OTHER: P={o[0]} S={o[1]} P'={o[2]} S'={o[3]} "
                  f"c={o[4]} d={o[5]}")
    report("B EXHAUSTION: every incidence is diagonal-excluded transpose / "
           "reflection / translation — OTHER = 0 on all 13 panels", ok_exhaust)
    report("B k>=q law: incidences nonempty exactly when k >= q "
           "(all 13 panels)", ok_law)
    report("B translation family: every generated point is an incidence with "
           "witnesses c = -gamma^{-1}, d = -c (all panels)", ok_wit)
    report("C Conjecture C12-2: c + d = 0 on EVERY incidence, EVERY panel",
           all_cd_zero)
    # explicit corollary check: no same-modulus contact ever occurred
    report("A corollary: P'=P and S'=S never occur for c,d != 0 "
           "(asserted in construction; no assertion fired)", True)

def section_delta6():
    q, k = 3, 6
    m = 2 * k - 1
    L = primorial(3)
    irr = irreducibles_upto(m, 3)
    sources = lambda_sources(m, 3, irr)
    pts = resonant_points(k)
    print(f"   k=6 Delta panel: {len(pts)} resonant points, m={m}, "
          f"{len(sources)} sources")
    cache = {}
    def val(P, S):
        key = (P, S)
        if key not in cache:
            mu = mu_of(P, S, L, 1, 3)
            nu = mu_of(S, P, L, 1, 3)
            X = zmul(Ahat_exact(P, mu, sources, 3),
                     Ahat_exact(S, nu, sources, 3))
            D = delta_exact(P, S, L, sources, 3)
            cache[key] = (X, D, zadd(X, zscale(D, -1)))
        return cache[key]
    ok_inv = True
    XX = XD = DX = DD = BB = zzero(3)
    for (P, S, Pp, Sp, Q, eps) in pts:
        Xa, Da, Ba = val(P, S)
        Xb, Db, Bb = val(Pp, Sp)
        if not (zeq(Xa, Xb) and zeq(Da, Db) and zeq(Ba, Bb)):
            ok_inv = False
        XX = zadd(XX, zmul(Xa, zconj(Xb)))
        XD = zadd(XD, zmul(Xa, zconj(Db)))
        DX = zadd(DX, zmul(Da, zconj(Xb)))
        DD = zadd(DD, zmul(Da, zconj(Db)))
        BB = zadd(BB, zmul(Ba, zconj(Bb)))
    report(f"D involution invariance X_a=X_b, Delta_a=Delta_b, B_a=B_b "
           f"(k=6, all {len(pts)} points)", ok_inv)
    vals = (zint(XX), zint(XD), zint(DX), zint(DD), zint(BB))
    okbb = vals[4] == vals[0] - vals[1] - vals[2] + vals[3]
    ratio = vals[4] / 3 ** (2 * m + 3 * k)
    report(f"D exact aggregates rational; BB = XX-XD-DX+DD; BB >= 0 (k=6)",
           okbb and vals[4] >= 0,
           f"XX={vals[0]} XD={vals[1]} DX={vals[2]} DD={vals[3]} BB={vals[4]}")
    print(f"   k=6: BB/3^(2m+3k) = {ratio:.10f}   "
          f"(k=3,4,5 were 0.00132049, 0.00008933, 0.00009504; "
          f"raw dimension bound 2m^2 3^(-k-3) = {2*m*m*3**(-k-3):.6f})")

def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("corr", "all"):
        print("== A-C. correspondence form, classification panels, c+d=0 ==")
        section_corr()
    if which in ("delta6", "all"):
        print("== D. k=6 Delta panel ==")
        section_delta6()
    sys.exit(r11.FAIL)

if __name__ == "__main__":
    main()
