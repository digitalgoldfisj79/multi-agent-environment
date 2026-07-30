#!/usr/bin/env python3
"""Theta-independence theorem and the q=7 defect-orbit classification
(companion to FF_THETA_INDEPENDENCE_AND_DEFECT_ORBITS_NOTE_20260801.md).

The engine is the affine symmetry of the primorial: L = t^q - t is the unique
monic degree-q polynomial with

    L(t + a) = L(t)  (a in F_q)      and      L(lambda*t) = lambda * L(t),

i.e. it is the equation of the F_q-points of the affine line, so the group
AGL(1,q) = {t -> lambda*t + a} acts on the whole endpoint configuration
(band, sources, puncture), Lambda-equivariantly.  Everything below is exact
(Z[zeta_q] arithmetic from ff_class_correlation_exact).

Verified (endpoint k=2, m=3, theta in F_q^*, L = t^q - t, q = 3, 5, 7):
  T1  A-covariance: Ahat_{gP}(mu_1(theta; gP, gS)) = Ahat_P(mu_1(lam*theta;
      P, S)) for every g = (lam, a) in AGL(1,q) -- hence C(theta) = C(lam
      theta) = const and DiagMass likewise (theta-independence PROVED).
  T2  at fixed theta: the class set is AGL(1,q)-stable with E(g cls) = lam*E;
      translations preserve every class term; homotheties Galois-twist:
      term(g cls) = sigma_lam(term(cls)); the transpose (swap the two pairs)
      is a class involution with E -> -E, term -> conj(term).
      Consequences (PROVED, machine-checked): C(theta) is a sum of Galois
      orbit-traces => a rational integer, real; translations act freely on
      quadratics (q odd) => q | C(theta) and q | DiagMass.
  O   orbit decomposition at theta = 1: q(q-1)-regular (free) orbits --
      1, 3, 16 orbits at q = 3, 5, 7; the per-class law and all listed
      invariants are constant on orbits; free-orbit sum = q * Tr(term_rep);
      the 16-orbit classification table at q = 7 (law status, integer traces,
      resultant-character signature, transpose pairing).
  K3  k = 3 (q = 3, m = 5 = 2k-1): T1 A-covariance and theta-independence
      hold as predicted by the general proof (no C3 collapse available);
      exact C(theta) and Diag reported for t^q - t and the control.
"""
import sys
from ff_t3_coset_audit import (trim, padd, pmul, pmod, monics, irreducibles_upto,
                               lambda_sources, pow_poly_inverse)
from ff_class_correlation_exact import (pneg, psub, deg, zzero, zroot, zadd,
    zscale, zmul, zconj, zcanon, zeq, zfloat, zisreal, zisrational, zgalois,
    Ahat_exact)

FAIL = 0
def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

# --------------------------- the affine action ------------------------------
def affine(T, lam, a, q):
    """g = (lam, a): T -> lam^{-deg T} * T(lam*t + a), monic-preserving."""
    x = trim([a % q, lam % q])
    out = ()
    for c in reversed(T):
        out = padd(pmul(out, x, q), trim([c]), q)
    d = len(T) - 1
    inv = pow(pow(lam, d, q), q - 2, q)
    return tuple((ci * inv) % q for ci in out)

def ztrace(x, q):
    t = zzero(q)
    for s in range(1, q):
        t = zadd(t, zgalois(x, s))
    return t

def zint(x):
    c = zcanon(x)
    assert all(v == 0 for v in c[1:]), f"not rational: {c}"
    return c[0]

def legendre(x, q):
    x %= q
    if x == 0:
        return 0
    return 1 if pow(x, (q - 1) // 2, q) == 1 else -1

def res_quad(T, U, q):
    """Res(T, U) for monic quadratics: N_T(U mod T)."""
    r = pmod(U, T, q)
    r0 = r[0] if len(r) > 0 else 0
    r1 = r[1] if len(r) > 1 else 0
    c, b = T[0], T[1]
    return (r0 * r0 - r0 * r1 * b + r1 * r1 * c) % q

# ------------------------------ family data ---------------------------------
def build(q, band, Lpoly, th):
    pairs = []
    for P in band:
        LbP = pow_poly_inverse(pmod(Lpoly, P, q), P, q)
        for S in band:
            if S == P:
                continue
            SbP = pow_poly_inverse(pmod(S, P, q), P, q)
            PbS = pow_poly_inverse(pmod(P, S, q), S, q)
            LbS = pow_poly_inverse(pmod(Lpoly, S, q), S, q)
            mu1 = pmod(pmul(pmul(pneg(th, q), LbP, q), SbP, q), P, q)
            nu2 = pmod(pmul(pmul(pneg(th, q), LbS, q), PbS, q), S, q)
            pairs.append((P, S, mu1, nu2))
    return pairs

def classes_of(pairs, q):
    cl = {}
    for (P, S, mu1, nu2) in pairs:
        for (Pp, Sp, mu1p, nu2p) in pairs:
            E = psub(pmul(nu2, Sp, q), pmul(nu2p, S, q), q)
            if deg(E) == 0:
                cl[(P, S, Pp, Sp)] = E[0]
    return cl

def family(q, k, m, band, Lpoly, sources):
    """Per theta: A-values, class dict, term dict, diagonal."""
    A, CL, TERM, DIAG = {}, {}, {}, {}
    for th_s in range(1, q):
        pairs = build(q, band, Lpoly, (th_s,))
        A[th_s] = {(P, S): Ahat_exact(P, mu1, sources, q)
                   for (P, S, mu1, nu2) in pairs}
        d = zzero(q)
        for v in A[th_s].values():
            d = zadd(d, zmul(v, zconj(v)))
        DIAG[th_s] = d
        CL[th_s] = classes_of(pairs, q)
        TERM[th_s] = {cls: zmul(zroot(E, q),
                                zmul(A[th_s][(cls[0], cls[1])],
                                     zconj(A[th_s][(cls[2], cls[3])])))
                      for cls, E in CL[th_s].items()}
    return A, CL, TERM, DIAG

def law_holds(cls, E, A1, q):
    a = A1[(cls[0], cls[1])]
    b = A1[(cls[2], cls[3])]
    t = zmul(zroot(E, q), zmul(a, zconj(b)))
    return zeq(t, zmul(a, zconj(a))) and zeq(b, zmul(zroot(E, q), a))

# ------------------------------ k = 2 analysis ------------------------------
def analyze_k2(q, table=False):
    k, m = 2, 3
    Lpoly = trim([0, q - 1] + [0] * (q - 2) + [1])
    irr = irreducibles_upto(m, q)
    band = irr[k]
    sources = lambda_sources(m, q, irr)
    A, CL, TERM, DIAG = family(q, k, m, band, Lpoly, sources)
    G = [(lam, a) for lam in range(1, q) for a in range(q)]

    # T1: A-covariance A(1; gP, gS) = A(lam; P, S)
    ok1 = all(zeq(A[1][(affine(P, lam, a, q), affine(S, lam, a, q))],
                  A[lam][(P, S)])
              for (P, S) in A[1] for (lam, a) in G)
    report(f"T1 A-covariance A(1; gP,gS) = A(lam; P,S), all pairs x AGL(1,q) "
           f"(q={q})", ok1)
    report(f"T1 corollaries: C(theta), Diag independent of theta (q={q})",
           all(zeq(DIAG[s], DIAG[1]) for s in range(1, q))
           and all(set(CL[s]) == set(CL[1]) for s in range(1, q))
           and all(zeq(sum_terms(TERM[s], q), sum_terms(TERM[1], q))
                   for s in range(1, q)))

    # T2: class-set stability, E-scaling, translation/homothety term action
    ok_stab = ok_E = ok_tr = ok_hom = True
    for cls, E in CL[1].items():
        for (lam, a) in G:
            gcls = tuple(affine(T, lam, a, q) for T in cls)
            if gcls not in CL[1]:
                ok_stab = False
                continue
            if CL[1][gcls] != (lam * E) % q:
                ok_E = False
            if lam == 1 and not zeq(TERM[1][gcls], TERM[1][cls]):
                ok_tr = False
            if not zeq(TERM[1][gcls], zgalois(TERM[1][cls], lam)):
                ok_hom = False
    report(f"T2 class set AGL(1,q)-stable, E(g cls) = lam*E (q={q})",
           ok_stab and ok_E)
    report(f"T2 translations preserve terms; homotheties Galois-twist: "
           f"term(g cls) = sigma_lam(term) (q={q})", ok_tr and ok_hom)
    ok_x = all(zeq(TERM[s][cls], zgalois(TERM[1][cls], s))
               for s in range(1, q) for cls in CL[1])
    report(f"theta-covariance per term: term(s) = sigma_s(term(1)) (q={q})",
           ok_x)
    ok_t = True
    for cls, E in CL[1].items():
        tcls = (cls[2], cls[3], cls[0], cls[1])
        if tcls not in CL[1] or CL[1][tcls] != (-E) % q \
           or not zeq(TERM[1][tcls], zconj(TERM[1][cls])):
            ok_t = False
    report(f"transpose involution: E -> -E, term -> conj(term) (q={q})", ok_t)

    # orbits at theta = 1
    orbits, seen = [], set()
    for cls in CL[1]:
        if cls in seen:
            continue
        orb = sorted({tuple(affine(T, lam, a, q) for T in cls)
                      for (lam, a) in G})
        orbits.append(orb)
        seen |= set(orb)
    Csum = sum_terms(TERM[1], q)
    ok_o = True
    osum_total = zzero(q)
    odata = []
    for oi, orb in enumerate(orbits):
        osum = zzero(q)
        for c in orb:
            osum = zadd(osum, TERM[1][c])
        rep = orb[0]
        laws = {law_holds(c, CL[1][c], A[1], q) for c in orb}
        samePs = {c[0] == c[2] for c in orb}
        tr = ztrace(TERM[1][rep], q)
        free = len(orb) == q * (q - 1)
        if len(laws) != 1 or len(samePs) != 1:
            ok_o = False
        if free and not zeq(osum, zscale(tr, q)):
            ok_o = False
        osum_total = zadd(osum_total, osum)
        odata.append((oi, orb, rep, laws.pop(), samePs.pop(), tr, osum, free))
    ok_o = ok_o and zeq(osum_total, Csum)
    sizes = sorted(len(o[1]) for o in odata)
    report(f"O orbit decomposition: {len(odata)} orbits, law/same-P constant "
           f"per orbit, free-orbit sum = q*Tr(rep), total = C (q={q})", ok_o,
           f"sizes={sizes}")
    Cint = zint(Csum)
    Dint = zint(DIAG[1])
    report(f"O integrality + q-divisibility: C = {Cint} = {q}*{Cint//q}, "
           f"Diag = {Dint} = {q}*{Dint//q} (q={q})",
           Cint % q == 0 and Dint % q == 0)

    if table:
        # classification table with invariants + transpose pairing
        def chi_sig(cls):
            P, S, Pp, Sp = cls
            prs = [(P, S), (Pp, Sp), (P, Pp), (S, Sp), (P, Sp), (S, Pp)]
            return tuple(legendre(res_quad(T, U, q), q) for (T, U) in prs)
        idx_of = {}
        for oi, orb, *_ in odata:
            for c in orb:
                idx_of[c] = oi
        print(f"   -- q={q} orbit classification "
              f"(chi signature order: (P,S) (P',S') (P,P') (S,S') (P,S') (S,P')) --")
        for (oi, orb, rep, law, sameP, tr, osum, free) in odata:
            sigs = {chi_sig(c) for c in orb}
            sig = sigs.pop() if len(sigs) == 1 else "NOT-CONSTANT"
            trep = (rep[2], rep[3], rep[0], rep[1])
            partner = idx_of[trep]
            trA = ztrace(zmul(A[1][(rep[0], rep[1])],
                              zconj(A[1][(rep[0], rep[1])])), q)
            print(f"   orbit {oi:2d}: size={len(orb):3d} same-P={str(sameP):5s} "
                  f"law={str(law):5s} Tr(term)={zint(tr):7d} "
                  f"Tr|A|^2={zint(trA):7d} transpose->orbit {partner:2d} "
                  f"chi={sig}")
            if len(sigs):
                report(f"chi signature constant on orbit {oi} (q={q})", False)
        law_or = sum(1 for o in odata if o[3])
        print(f"   summary q={q}: {len(odata)} orbits = {law_or} law-orbits + "
              f"{len(odata)-law_or} defect-orbits; "
              f"C = {q} * (sum of {len(odata)} integer traces) = {Cint}")
    return Cint, Dint

def sum_terms(term_dict, q):
    s = zzero(q)
    for v in term_dict.values():
        s = zadd(s, v)
    return s

# ------------------------------ k = 3 analysis ------------------------------
def analyze_k3():
    q, k, m = 3, 3, 5
    irr = irreducibles_upto(m, q)
    band = irr[k]
    sources = lambda_sources(m, q, irr)
    print(f"   k=3 endpoint: q={q}, band size {len(band)}, "
          f"pairs {len(band)*(len(band)-1)}, sources {len(sources)}")
    for Ltag, Lpoly in (("L=t^3-t ", trim([0, q - 1, 0, 1])),
                        ("L=t(t+1)", pmul((0, 1), (1, 1), q))):
        prim = Ltag.startswith("L=t^3-t")
        A, CL, TERM, DIAG = family(q, k, m, band, Lpoly, sources)
        Cv = {s: sum_terms(TERM[s], q) for s in (1, 2)}
        r1 = zfloat(Cv[1]).real / zfloat(DIAG[1]).real
        print(f"   {Ltag} k=3 q=3: Diag={zcanon(DIAG[1])} "
              f"(={zfloat(DIAG[1]).real:.1f})  C(1)={zcanon(Cv[1])} "
              f"(={zfloat(Cv[1]).real:.1f})  C/Diag={r1:+.4f}  "
              f"#classes={len(CL[1])}")
        report(f"C6 Galois covariance sigma_2(C(1)) = C(2) (k=3, {Ltag})",
               zeq(zgalois(Cv[1], 2), Cv[2]))
        if prim:
            G = [(lam, a) for lam in (1, 2) for a in range(q)]
            ok1 = all(zeq(A[1][(affine(P, lam, a, q), affine(S, lam, a, q))],
                          A[lam][(P, S)])
                      for (P, S) in A[1] for (lam, a) in G)
            report("K3 T1 A-covariance at k=3 (general-k proof check)", ok1)
            report("K3 theta-independence C(1) = C(2), Diag(1) = Diag(2) "
                   "(k=3, primorial)",
                   zeq(Cv[1], Cv[2]) and zeq(DIAG[1], DIAG[2]))
            report("K3 C(theta) rational (k=3, primorial)",
                   zisrational(Cv[1]) and zisrational(DIAG[1]),
                   f"C={zint(Cv[1])} Diag={zint(DIAG[1])}")
    # spot-check the completed-sum class constant zeta^E at k=3 (float)
    import cmath
    from ff_local_character_audit import psi_P
    zq = cmath.exp(2j * cmath.pi / q)
    Lpoly = trim([0, q - 1, 0, 1])
    pairs = build(q, band, Lpoly, (1,))
    checked, ok = 0, True
    for (P, S, mu1, nu2) in pairs:
        if checked >= 3:
            break
        for (Pp, Sp, mu1p, nu2p) in pairs:
            E = psub(pmul(nu2, Sp, q), pmul(nu2p, S, q), q)
            if deg(E) == 0 and (P, S) != (Pp, Sp):
                tot = sum(psi_P(nu2, fp, S, q, zq) *
                          psi_P(nu2p, fp, Sp, q, zq).conjugate()
                          for fp in monics(m, q))
                if abs(tot - (q ** m) * zq ** E[0]) > 1e-6:
                    ok = False
                checked += 1
                break
    report(f"K3 class constant = zeta^E at k=3 (direct f'-sums, "
           f"{checked} classes)", ok)

def main():
    print("== Theta-independence (T1/T2) and orbit structure, k=2 ==")
    for q in (3, 5, 7):
        analyze_k2(q, table=(q == 7))
    print("\n== k=3 endpoint: generality of T1 and first resonance data ==")
    analyze_k3()
    sys.exit(FAIL)

if __name__ == "__main__":
    main()
