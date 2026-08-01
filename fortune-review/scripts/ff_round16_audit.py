#!/usr/bin/env python3
"""Round 16 independent audit (companion to
ROUND16_LITERATURE_TRANSFER_AUDIT_20260804.md).

Audited state: branch gpt56/fortune-monodromy-trace-transfer-20260731,
head d807178 (draft PR #38), atop the TFP3 head e5ef12c.

Independent verifications (my own code; the branch's committed verifiers are
run separately as repository-internal checks):

  R1. The two q=97 normalized true-Frobenius records with rho = 1, FROM THE
      ORIGINAL LOCAL-FREQUENCY DEFINITIONS (mu = -theta (LS)^{-1} mod P
      etc., exactly as in my Round-13 counterexample check): four distinct
      irreducible cubics, witness constants c = -1, d = 1 (lambda = rho = 1
      gauge, theta = 1), all four divisibilities, nonzero common defect h of
      degree 89 <= q - 2k = 91 satisfying every BDD1 identity — WITH
      c + d = 0.  This falsifies the converse of BDD2's forward implication
      (h = 0 => rho = lambda <=> c + d = 0): my Round-13 note carried
      "h = 0 <=> c + d = 0 throughout" as a panel observation; the <= half
      is now dead at q = 97.  (My census enumerator never filtered on c + d,
      so my Round-13/14 counts are unaffected.)  Frobenius orientation of
      all four blocks is verified with my own eta^F and the four oriented
      equations; both records lie in the sigma = (1,1,1,1) class with
      kappa = +1.
  R2. The two-torsor statement, symbolically (sympy, my own derivation):
      (a) Res_t(F, N_e) - e^4 = -(e^2 - disc F) * Q / 8 with the stated Q;
      (b) the resultant elimination proving eta_A eta_D = eta_B eta_C on the
      cross-distinct separable locus; (c) the sixteen sign vectors split
      into two disjoint 8-element torsors indexed by kappa, with (1,1,1,1)
      only in kappa = +1.
  R3. kappa panel: on MY Round-14 enumeration of the irreducible
      nondegenerate V(F_q) points (q = 11, 13, 17), compute the actual
      Frobenius orientations eta^F, the relative signs sigma_X, and kappa;
      verify the q-free identity holds on this whole class, that
      sigma_A sigma_D = kappa sigma_B sigma_C at every point, that the true
      class is exactly sigma = (1,1,1,1) (count = census: 2, 0, 2), that
      true points have kappa = +1, and report the kappa split of the
      orientation-spurious points.
  R4. q-line falsification: my own irreducibility census for
      f = q z^p + z^3 - 3z - (q-2) t over F_p (t != +-1, q != 0, 2),
      E_1(q) = p (1 - I_1(q)); verify sum E_1 / p = -1, -1, -1, 3, 3, 1 at
      p = 5, 7, 11, 13, 17, 19 — the universal "-p" identity holds at
      5, 7, 11 and FAILS from 13 on.

Usage: python3 ff_round16_audit.py [q97|torsor|kappa|qline]
"""
import sys
from ff_t3_coset_audit import trim, padd, pmul, pmod, irreducibles_upto
from ff_class_correlation_exact import psub, deg, frobenius
from ff_round11_independent_audit import report, pscale, primorial, mu_of
from ff_round13_independent_audit import pdivmod, defect_of
from ff_round14_qfree_audit import (sqrts, cubic_tuple, disc_cubic, nf_tuple,
                                    monic_lift, solve_eta)

# The two committed q=97 rho=1 records (branch convention [a2,a1,a0], monic;
# block order A=P, B=S, C=P', D=S').
Q97_RECORDS = [
    {"q": 97, "rho": 1, "A": [0, 74, 40], "B": [57, 44, 61],
     "C": [43, 76, 71], "D": [83, 61, 67]},
    {"q": 97, "rho": 1, "A": [0, 28, 55], "B": [57, 90, 77],
     "C": [71, 27, 7], "D": [14, 10, 81]},
]

def blk(rec, q):
    a2, a1, a0 = rec
    return trim([a0 % q, a1 % q, a2 % q, 1])

def peval(f, x, q):
    out = 0
    for cf in reversed(f):
        out = (out * x + cf) % q
    return out

def irreducible_cubic(f, q):
    return len(f) == 4 and f[-1] == 1 and all(peval(f, x, q) for x in range(q))

def eta_frob(f, q):
    """Frobenius-oriented Vandermonde (x-x^q)(x-x^{q^2})(x^q-x^{q^2}) mod f,
    which must be the scalar eta^F with (eta^F)^2 = disc f."""
    x = (0, 1)
    xq = frobenius(x, f, q)
    xq2 = frobenius(xq, f, q)
    e = pmod(pmul(pmul(psub(x, xq, q), psub(x, xq2, q), q),
                  psub(xq, xq2, q), q), f, q)
    assert len(e) == 1, f"eta^F not scalar: {e}"
    assert e[0], "zero eta^F"
    return e[0]

def oriented_equations_hold(P, S, Pp, Sp, eP, eS, ePp, eSp, rho, q):
    """The four Frobenius-orientation equations (branch order, A=P B=S C=P'
    D=S'), with N from my Round-14 nf_tuple (symbolically verified there)."""
    def N(f, e):
        c2 = f[2] if len(f) > 2 else 0
        return nf_tuple(c2, f[1], f[0], e, q)
    eqs = [
        pmod(psub(pmul(N(P, eP), S, q), pscale(Pp, eP, q), q), P, q),
        pmod(padd(pmul(N(Pp, ePp), Sp, q), pscale(P, ePp, q), q), Pp, q),
        pmod(padd(pmul(N(S, eS), P, q), pscale(Sp, (rho * eS) % q, q), q),
             S, q),
        pmod(psub(pmul(N(Sp, eSp), Pp, q), pscale(S, (rho * eSp) % q, q), q),
             Sp, q),
    ]
    return not any(eqs)

# --------------------- R1. the q=97 rho=1 records ---------------------------
def check_q97():
    q, k, th = 97, 3, 1
    Lpoly = primorial(q)
    for i, row in enumerate(Q97_RECORDS, 1):
        P, S = blk(row["A"], q), blk(row["B"], q)
        Pp, Sp = blk(row["C"], q), blk(row["D"], q)
        rho = row["rho"]
        report(f"R1.{i} four DISTINCT irreducible cubics over F_97",
               all(irreducible_cubic(T, q) for T in (P, S, Pp, Sp))
               and len({P, S, Pp, Sp}) == 4)
        # normalized gauge lambda = rho = 1, theta = 1  =>  c = -1, d = 1
        c, d = (-th) % q, th % q
        mu_a = mu_of(P, S, Lpoly, th, q)
        mu_b = mu_of(Pp, Sp, Lpoly, th, q)
        nu_a = mu_of(S, P, Lpoly, th, q)
        nu_b = mu_of(Sp, Pp, Lpoly, th, q)
        Emu = psub(pmul(mu_a, Pp, q), pmul(mu_b, P, q), q)
        Enu = psub(pmul(nu_a, Sp, q), pmul(nu_b, S, q), q)
        report(f"R1.{i} ORIGINAL-DEFINITION incidence: mu_a P' - mu_b P = -1,"
               f" nu_a S' - nu_b S = 1  (c = -1, d = 1, c + d = 0)",
               Emu == (c,) and Enu == (d,))
        h = defect_of(P, S, Pp, Sp, c, d, q)
        report(f"R1.{i} common defect h != 0 with deg h = 89 <= q-2k = 91; "
               f"all BDD1 identities exact", h != () and deg(h) == 89)
        report(f"R1.{i} CONVERSE FALSIFIED: c + d = 0 (rho = lambda = 1) "
               f"yet h != 0 — 'h = 0 <=> c + d = 0' fails right-to-left",
               (c + d) % q == 0 and h != ())
        eP, eS = eta_frob(P, q), eta_frob(S, q)
        ePp, eSp = eta_frob(Pp, q), eta_frob(Sp, q)
        kappa = (eP * eSp * pow(eS * ePp % q, q - 2, q)) % q
        report(f"R1.{i} Frobenius orientation: all four oriented equations "
               f"hold with eta = eta^F (sigma = (1,1,1,1)) and kappa = +1",
               oriented_equations_hold(P, S, Pp, Sp, eP, eS, ePp, eSp,
                                       rho, q)
               and kappa == 1)

# --------------------- R2. two-torsor statement, symbolic -------------------
def check_torsor_symbolic():
    import itertools
    import sympy as sp
    a, b, c, e, t = sp.symbols("a b c e t")
    F = t**3 + a*t**2 + b*t + c
    disc = sp.discriminant(F, t)
    i2 = sp.Rational(1, 2)
    N = ((a*a - 3*b)*t**2 + (a**3 - 7*i2*a*b + 9*i2*c - 3*i2*e)*t
         + i2*a*a*b + 3*i2*a*c - 2*b*b - i2*a*e)
    R = sp.expand(sp.resultant(F, N, t))
    Qcof = sp.Rational(-1, 8) * (4*a**3*c - 2*a**3*e - a**2*b**2 - 18*a*b*c
                                 + 9*a*b*e + 4*b**3 + 27*c*c - 27*c*e
                                 + 8*e*e)
    report("R2 resultant identity Res(F, N_e) - e^4 = -(e^2 - disc F) Q/8 "
           "(my own expansion)",
           sp.expand(R - e**4 - (e**2 - disc)*Qcof) == 0)
    eA, eB, eC, eD, RAB, RAC, RCD, RBD, rho = sp.symbols(
        "eA eB eC eD RAB RAC RCD RBD rho")
    rels = [eA*RAB - RAC, eC*RCD - RAC, eB*RAB - rho**3*RBD,
            eD*RCD - rho**3*RBD]
    G = sp.groebner(rels, RAC, RBD, RAB, RCD, eA, eB, eC, eD, rho)
    report("R2 elimination: (eA eD - eB eC) * RAB * RCD lies in the ideal of "
           "the four block relations — the identity holds where the "
           "resultants are nonzero",
           G.reduce((eA*eD - eB*eC)*RAB*RCD)[1] == 0)
    signs = list(itertools.product((-1, 1), repeat=4))
    tors = {k: [s for s in signs if s[0]*s[3] == k*s[1]*s[2]]
            for k in (-1, 1)}
    report("R2 sixteen sign vectors = two DISJOINT 8-element torsors "
           "indexed by kappa; (1,1,1,1) only in kappa = +1",
           len(tors[1]) == 8 and len(tors[-1]) == 8
           and not set(tors[1]) & set(tors[-1])
           and (1, 1, 1, 1) in tors[1] and (1, 1, 1, 1) not in tors[-1])

# --------------------- R3. kappa panel on my Round-14 points ----------------
def irred_nondegen_points(q):
    """Irreducible nondegenerate V(F_q) points via my Round-14
    interpolation-correspondence parametrization, yielding
    (A, B, C, D, eA, eB, eC, eD, rho)."""
    irr = irreducibles_upto(3, q)
    band3 = set(irr[3])
    out = []
    for A1 in range(q):
        for A0 in range(q):
            dA = disc_cubic(0, A1, A0, q)
            for eA in sqrts(dA, q):
                if eA == 0:
                    continue
                Apoly = cubic_tuple(A0, A1, 0)
                NA = nf_tuple(0, A1, A0, eA, q)
                for B2 in range(q):
                    for B1 in range(q):
                        for B0 in range(q):
                            dB = disc_cubic(B2, B1, B0, q)
                            eBs = [x for x in sqrts(dB, q) if x]
                            if not eBs:
                                continue
                            Bpoly = cubic_tuple(B0, B1, B2)
                            NAB = pmod(pmul(NA, Bpoly, q), Apoly, q)
                            for eB in eBs:
                                NB = nf_tuple(B2, B1, B0, eB, q)
                                NBA = pmod(pmul(NB, Apoly, q), Bpoly, q)
                                for rho in range(1, q):
                                    out += fiber_points(q, Apoly, Bpoly,
                                                        NAB, NBA, eA, eB,
                                                        rho, band3)
    return out

def fiber_points(q, Apoly, Bpoly, NAB, NBA, eA, eB, rho, band3):
    rC = pscale(NAB, pow(eA, q - 2, q), q)
    Cpoly = monic_lift(rC, Apoly, q)
    rD = pscale(NBA, (-pow(rho * eB % q, q - 2, q)) % q, q)
    Dpoly = monic_lift(rD, Bpoly, q)
    if Cpoly == Apoly or Dpoly == Bpoly:
        return []
    if not all(T in band3 for T in (Apoly, Bpoly, Cpoly, Dpoly)):
        return []
    C2 = Cpoly[2] if len(Cpoly) > 2 else 0
    D2 = Dpoly[2] if len(Dpoly) > 2 else 0
    dC = disc_cubic(C2, Cpoly[1], Cpoly[0], q)
    dD = disc_cubic(D2, Dpoly[1], Dpoly[0], q)
    pts = []
    for eC in sqrts(dC, q):
        NC = nf_tuple(C2, Cpoly[1], Cpoly[0], eC, q)
        if pmod(padd(pmul(NC, Dpoly, q),
                     pscale(pmod(Apoly, Cpoly, q), eC, q), q), Cpoly, q):
            continue
        for eD in sqrts(dD, q):
            ND = nf_tuple(D2, Dpoly[1], Dpoly[0], eD, q)
            if pmod(psub(pmul(ND, Cpoly, q),
                         pscale(pmod(Bpoly, Dpoly, q), (rho * eD) % q, q),
                         q), Dpoly, q):
                continue
            pts.append((Apoly, Bpoly, Cpoly, Dpoly, eA, eB, eC, eD, rho))
    return pts

def check_kappa_panel():
    census_true = {11: 2, 13: 0, 17: 2}
    for q in (11, 13, 17):
        pts = irred_nondegen_points(q)
        id_ok = rel_ok = 0
        true_pts, spurious_kappa = [], []
        for (A, B, C, D, eA, eB, eC, eD, rho) in pts:
            if (eA * eD - eB * eC) % q == 0:
                id_ok += 1
            fA, fB = eta_frob(A, q), eta_frob(B, q)
            fC, fD = eta_frob(C, q), eta_frob(D, q)
            sig = tuple((e * pow(f, q - 2, q)) % q
                        for e, f in ((eA, fA), (eB, fB), (eC, fC), (eD, fD)))
            assert all(s in (1, q - 1) for s in sig), "sigma not +-1"
            sgn = tuple(1 if s == 1 else -1 for s in sig)
            kappa_raw = (fA * fD * pow(fB * fC % q, q - 2, q)) % q
            assert kappa_raw in (1, q - 1), "kappa not +-1"
            kappa = 1 if kappa_raw == 1 else -1
            if sgn[0] * sgn[3] == kappa * sgn[1] * sgn[2]:
                rel_ok += 1
            if sgn == (1, 1, 1, 1):
                true_pts.append((rho, kappa))
            else:
                spurious_kappa.append(kappa)
        n = len(pts)
        report(f"R3 q={q}: q-free identity eta_A eta_D = eta_B eta_C holds "
               f"on ALL {n} irreducible nondegenerate points",
               id_ok == n, f"held at {id_ok}/{n}")
        report(f"R3 q={q}: relative-sign equation sigma_A sigma_D = "
               f"kappa sigma_B sigma_C holds at every point", rel_ok == n)
        report(f"R3 q={q}: true class sigma = (1,1,1,1) has "
               f"{census_true[q]} points (= census), every one with "
               f"kappa = +1",
               len(true_pts) == census_true[q]
               and all(kp == 1 for (_, kp) in true_pts),
               f"true rho values {sorted(r for (r, _) in true_pts)}")
        kp = sorted(set(spurious_kappa))
        print(f"   q={q}: spurious points {len(spurious_kappa)}, "
              f"kappa values occurring among them: {kp} "
              f"(+1 count {spurious_kappa.count(1)}, "
              f"-1 count {spurious_kappa.count(-1)})")

# --------------------- R4. the q-line falsification -------------------------
def poly_irreducible_deg_p(f, p):
    """f monic degree p over F_p irreducible <=> x^(p^p) = x mod f and
    gcd(x^p - x, f) = 1 (n = p prime).  Valid for arbitrary f."""
    x = (0, 1)
    xp = frobenius(x, f, p)                 # x^p mod f
    # gcd(x^p - x, f) must be 1
    g = poly_gcd(psub(xp, x, p), f, p)
    if deg(g) != 0:
        return False
    y = xp
    for _ in range(len(f) - 2):             # p-1 more Frobenius steps
        y = frobenius(y, f, p)
    return y == x

def poly_gcd(a, b, q):
    a, b = trim(list(a)), trim(list(b))
    while b:
        _, r = pdivmod(a, b, q)
        a, b = b, r
    return a

def qline(p):
    total = 0
    for u in range(1, p):
        if u == 2:
            continue
        count = 0
        for tv in range(p):
            if tv in (1, p - 1):
                continue
            f = [(-(u - 2) * tv) % p, (-3) % p, 0, 1] + [0] * (p - 4) + [u]
            f = trim([x % p for x in f])
            if poly_irreducible_deg_p(tuple(f), p):
                count += 1
        total += p * (1 - count)
    assert total % p == 0
    return total // p

def check_qline():
    expected = {5: -1, 7: -1, 11: -1, 13: 3, 17: 3, 19: 1, 23: 3, 29: -7}
    got = {p: qline(p) for p in expected}
    report("R4 q-line sums: sum E_1 / p = -1, -1, -1 at p = 5, 7, 11 "
           "(the '-p' identity) but 3, 3, 1, 3, -7 at p = 13..29 — the "
           "universal Tate identity is FALSIFIED at 13 and keeps varying, "
           "including a sign flip at 29",
           got == expected, f"got {got}")

# --------------------- R5. committed panel internal consistency -------------
def check_panel(path):
    """Arithmetic consistency of the committed extended panel JSON:
    incidences = orbits * q(q-1) and the rho multiset is invariant under
    rho -> rho^{-1} (the transpose symmetry), every row."""
    import json
    from collections import Counter
    doc = json.load(open(path))
    ok_orbit = ok_rho = True
    for row in doc["fields"]:
        q, n = row["q"], row["true_orbits"]
        if row["incidences"] != n * q * (q - 1):
            ok_orbit = False
        rhos = Counter(row["normalized_rho"])
        if rhos != Counter(pow(r, q - 2, q) for r in row["normalized_rho"]):
            ok_rho = False
    report("R5 committed panel: every row has incidences = orbits * q(q-1)",
           ok_orbit)
    report("R5 committed panel: every rho multiset is invariant under "
           "rho -> rho^{-1} (transpose symmetry), including the two rho = 1 "
           "entries at q = 97", ok_rho)

def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("q97", "all"):
        check_q97()
    if which in ("torsor", "all"):
        check_torsor_symbolic()
    if which in ("kappa", "all"):
        check_kappa_panel()
    if which in ("qline", "all"):
        check_qline()
    if which in ("panel", "all"):
        import os
        here = os.path.dirname(os.path.abspath(__file__))
        check_panel(os.path.join(here, "..", "data",
                                 "ff_tfp3_true_panel_through_101.json"))

if __name__ == "__main__":
    main()
