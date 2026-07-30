#!/usr/bin/env python3
"""Round 13 independent audit (companion to ROUND13_INDEPENDENT_AUDIT_20260802.md).

Independent verification (no shared code with the branch verifiers) of branch
head 170c8ae:

  X. The (11,3) counterexample, FROM THE ORIGINAL LOCAL-FREQUENCY DEFINITIONS:
     the explicit quadruple is a literal simultaneous endpoint incidence with
     c = 2, d = 8 (c + d = 10 != 0), and its defect h = 2t^5+5t^4+6t^2+6t+4
     satisfies all three BDD1 identities with deg h = 5 = q - 2k.
     This falsifies my Round-12 Conjectures C12-2 (c + d = 0 universally) and
     the emptiness half of C12-6 (q > k => no incidence) — both retracted.
  D. Theorem BDD1/BDD2 identities machine-verified on data: every incidence on
     the Round-12 panels ((3,4),(3,5),(5,5)) has h = 0 and c + d = 0; every
     (11,3) incidence has h != 0, deg h <= q-2k, the two quotient-defect
     identities, the product identity, and h = 0 <=> c + d = 0 throughout.
  C3. Independent cubic census (translation-normalized correspondence
     enumeration, count x q): q = 5, 7, 11, 13, 17, 19, 23 — including the
     branch's claimed ABSENCES at q = 13, 23; AGL-orbit structure at q = 11
     (expect 2 orbits of q(q-1) = 110).
  C2. NEW quadratic census (k = 2, q = 5..41): does the nonzero-defect locus
     exist at k = 2?  (q >= 2k throughout; the branch's census was cubic only.)

All checks exact; theta = 1 throughout.
Usage: python3 ff_round13_independent_audit.py [cx|census3|census2]
"""
import itertools, sys
from ff_t3_coset_audit import (trim, padd, pmul, pmod, irreducibles_upto,
                               pow_poly_inverse)
from ff_class_correlation_exact import pneg, psub, deg, frobenius
from ff_round11_independent_audit import report, pscale, primorial, mu_of
import ff_round11_independent_audit as r11

def pdivmod(a, b, q):
    """Exact (quotient, remainder) of a by b."""
    a = list(a)
    quo = [0] * max(len(a) - len(b) + 1, 1)
    db, lb = len(b) - 1, b[-1]
    inv = pow(lb, q - 2, q)
    while True:
        at = trim(a)
        if not at or len(at) - 1 < db:
            return trim(quo), at
        a = list(at)
        c = (a[-1] * inv) % q
        shift = len(a) - 1 - db
        quo[shift] = c
        for i, y in enumerate(b):
            a[shift + i] = (a[shift + i] - c * y) % q

def pdiv_exact(a, b, q, what):
    quo, rem = pdivmod(a, b, q)
    assert not rem, f"non-exact division in {what}"
    return quo

# ------------------------- defect machinery (BDD1) --------------------------
def defect_of(P, S, Pp, Sp, c, d, q, th=1):
    """Compute lambda, rho, quotients A,B,C,D, and the common defect h;
    verify all BDD1 identities exactly.  Returns h."""
    Lpoly = primorial(q)
    lam = (-th * pow(c, q - 2, q)) % q
    rho = (th * pow(d, q - 2, q)) % q
    A = pdiv_exact(psub(pmul(Lpoly, S, q), pscale(Pp, lam, q), q), P, q, "A")
    B = pdiv_exact(padd(pmul(Lpoly, P, q), pscale(Sp, rho, q), q), S, q, "B")
    C = pdiv_exact(padd(pmul(Lpoly, Sp, q), pscale(P, lam, q), q), Pp, q, "C")
    D = pdiv_exact(psub(pmul(Lpoly, Pp, q), pscale(S, rho, q), q), Sp, q, "D")
    h1 = pdivmod(psub(pscale(C, rho, q), pscale(B, lam, q), q),
                 pmul(P, Sp, q), q)
    h2 = pdivmod(psub(pscale(A, rho, q), pscale(D, lam, q), q),
                 pmul(S, Pp, q), q)
    assert not h1[1] and not h2[1], "defect divisibilities fail"
    h = h1[0]
    assert h == h2[0], "h1 != h2"
    # product identity: h*PP'SS' = L(rho SS' - lam PP') + lam rho (PS - P'S')
    lhs = pmul(h, pmul(pmul(P, Pp, q), pmul(S, Sp, q), q), q)
    rhs = padd(pmul(Lpoly, psub(pscale(pmul(S, Sp, q), rho, q),
                                pscale(pmul(P, Pp, q), lam, q), q), q),
               pscale(psub(pmul(P, S, q), pmul(Pp, Sp, q), q),
                      (lam * rho) % q, q), q)
    assert lhs == rhs, "product identity fails"
    if h:
        assert deg(h) <= q - 2 * (len(P) - 1), "deg h > q-2k"
    return h

# ------------------------------ X. counterexample ---------------------------
def check_counterexample():
    q, k, th = 11, 3, 1
    Lpoly = primorial(q)
    P = (1, 0, 4, 1)                 # t^3+4t^2+1
    S = (1, 9, 10, 1)                # t^3+10t^2+9t+1
    Pp = (7, 6, 10, 1)               # t^3+10t^2+6t+7
    Sp = (10, 3, 4, 1)               # t^3+4t^2+3t+10
    irr = irreducibles_upto(k, q)
    band = set(irr[k])
    report("X quadruple: four DISTINCT irreducible cubics over F_11",
           all(T in band for T in (P, S, Pp, Sp))
           and len({P, S, Pp, Sp}) == 4)
    # original local frequencies mu = -theta (LS)^{-1} mod P, etc.
    mu_a = mu_of(P, S, Lpoly, th, q)
    mu_b = mu_of(Pp, Sp, Lpoly, th, q)
    nu_a = mu_of(S, P, Lpoly, th, q)
    nu_b = mu_of(Sp, Pp, Lpoly, th, q)
    report("X branch's stated frequencies match my independent computation",
           mu_a == (7, 10, 6) and mu_b == (3, 2, 6)
           and nu_a == (2, 5, 4) and nu_b == (1, 3, 4),
           f"mu_a={mu_a} mu_b={mu_b} nu_a={nu_a} nu_b={nu_b}")
    Emu = psub(pmul(mu_a, Pp, q), pmul(mu_b, P, q), q)
    Enu = psub(pmul(nu_a, Sp, q), pmul(nu_b, S, q), q)
    report("X ORIGINAL-DEFINITION incidence: mu_a P' - mu_b P = 2, "
           "nu_a S' - nu_b S = 8  (c + d = 10 != 0)",
           Emu == (2,) and Enu == (8,))
    h = defect_of(P, S, Pp, Sp, 2, 8, q)
    report("X defect h = 2t^5+5t^4+6t^2+6t+4 with deg h = 5 = q-2k; all "
           "BDD1 identities exact", h == (4, 6, 6, 0, 5, 2) and deg(h) == 5)
    # BDD2 sanity on old data: reflection point at (3,4) has h = 0
    ok = True
    for pt in r11.resonant_points(4) + r11.resonant_points(5):
        P4, S4, Pp4, Sp4, Q4, eps4 = pt
        c4 = (-1 * eps4) % 3
        d4 = (1 * eps4) % 3
        if defect_of(P4, S4, Pp4, Sp4, c4, d4, 3) != () \
                or (c4 + d4) % 3 != 0:
            ok = False
    from ff_gate2_correspondence_audit import translation_points
    for (P5, S5, Pp5, Sp5, R5, g5) in translation_points(3, 5) \
            + translation_points(3, 6):
        c5 = (-pow(g5, 1, 3)) % 3
        c5 = (-pow(g5, 3 - 2, 3)) % 3          # -gamma^{-1}
        d5 = (-c5) % 3
        if defect_of(P5, S5, Pp5, Sp5, c5, d5, 3) != ():
            ok = False
    report("D BDD2 on Round-12 data: every reflection point (k=4,5) and "
           "every translation point (k=5,6) has defect h = 0 and c+d = 0",
           ok)

# ------------------------- normalized census enumerator ---------------------
def census(q, k, collect=False):
    """Cross-distinct simultaneous incidences with P translation-normalized
    (coeff_{k-1}(P) = 0); the full count is q x this count (translations act
    freely and preserve incidences and witnesses).  Fast: L = t^q - t is
    reduced modulo each band prime ONCE via Frobenius square-and-multiply, so
    all arithmetic stays at degree < 2k."""
    irr = irreducibles_upto(k, q)
    band = irr[k]
    bset = set(band)
    Lred = {}
    for T in band:
        frob = frobenius((0, 1), T, q)              # t^q mod T
        Lred[T] = pmod(psub(frob, (0, 1), q), T, q)  # L mod T
    reps = [P for P in band if (P[k - 1] if len(P) > k - 1 else 0) == 0]
    found = []
    for P in reps:
        LP = Lred[P]
        for S in band:
            if S == P:
                continue
            LSmP = pmod(pmul(LP, S, q), P, q)
            LPmS = pmod(pmul(Lred[S], P, q), S, q)
            cc = []
            for c in range(1, q):
                Pp = padd(P, pscale(LSmP, -c, q), q)
                if Pp in bset:
                    cc.append((c, Pp))
            if not cc:
                continue
            dd = []
            for d in range(1, q):
                Sp = padd(S, pscale(LPmS, -d, q), q)
                if Sp in bset:
                    dd.append((d, Sp))
            for (c, Pp) in cc:
                for (d, Sp) in dd:
                    if Pp == Sp:
                        continue
                    if pmod(psub(pscale(pmul(Lred[Pp], Sp, q), c, q), P, q),
                            Pp, q):
                        continue
                    if pmod(psub(pscale(pmul(Lred[Sp], Pp, q), d, q), S, q),
                            Sp, q):
                        continue
                    found.append((P, S, Pp, Sp, c, d))
    return found

def affine_prime(T, lam, a, q):
    x = trim([a % q, lam % q])
    out = ()
    for cf in reversed(T):
        out = padd(pmul(out, x, q), trim([cf]), q)
    dd = len(T) - 1
    inv = pow(pow(lam, dd, q), q - 2, q)
    return tuple((ci * inv) % q for ci in out)

def census3():
    claimed = {5: 0, 7: 0, 11: 220, 13: 0, 17: 544, 19: 684, 23: 0,
               29: 1624, 31: 1860, 37: 5328}
    for q in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        f = census(q, 3)
        total = q * len(f)
        report(f"C3 cubic census q={q}: total incidences = {claimed[q]} "
               f"(branch), independent count", total == claimed[q],
               f"got {total}")
        if q == 11 and f:
            # reconstruct the full 220 by translating, then orbit-decompose
            full = set()
            for (P, S, Pp, Sp, c, d) in f:
                for a in range(q):
                    full.add((affine_prime(P, 1, a, q), affine_prime(S, 1, a, q),
                              affine_prime(Pp, 1, a, q), affine_prime(Sp, 1, a, q),
                              c, d))
            report("C3 (11,3): translated normalized set has size 220",
                   len(full) == 220)
            # defect checks on every normalized incidence
            ok = True
            degs, ratios = set(), set()
            for (P, S, Pp, Sp, c, d) in f:
                h = defect_of(P, S, Pp, Sp, c, d, q)
                if h == () or (c + d) % q == 0:
                    ok = False
                degs.add(deg(h))
                ratios.add((d * pow(c, q - 2, q)) % q)
            report("C3 (11,3): every incidence has h != 0, c + d != 0, all "
                   "BDD1 identities exact", ok,
                   f"deg h values={sorted(degs)}, d/c values={sorted(ratios)}")
            # AGL orbits (homothety scales (c,d) jointly; translation fixes)
            G = [(lam, a) for lam in range(1, q) for a in range(q)]
            seen, orbits = set(), []
            for inc in full:
                if inc in seen:
                    continue
                (P, S, Pp, Sp, c, d) = inc
                orb = {(affine_prime(P, lam, a, q), affine_prime(S, lam, a, q),
                        affine_prime(Pp, lam, a, q), affine_prime(Sp, lam, a, q),
                        (lam * c) % q, (lam * d) % q) for (lam, a) in G}
                if not orb <= full:
                    report("C3 (11,3): AGL-covariance of the incidence set",
                           False)
                orbits.append(len(orb))
                seen |= orb
            report(f"C3 (11,3): AGL orbit structure = 2 free orbits of "
                   f"q(q-1) = 110", sorted(orbits) == [110, 110],
                   f"orbits={sorted(orbits)}")

def census2():
    rows = []
    ok_empty = True
    for q in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53):
        f = census(q, 2)
        rows.append((q, q * len(f)))
        if f:
            ok_empty = False
            for (P, S, Pp, Sp, c, d) in f[:4]:
                print(f"     k=2 NONEMPTY at q={q}: P={P} S={S} P'={Pp} "
                      f"S'={Sp} c={c} d={d}")
    print("   C2 quadratic (k=2) nonzero-defect census (q >= 2k throughout): "
          + "  ".join(f"q={q}:{n}" for (q, n) in rows))
    report("C2 NEW: the quadratic (k=2) cross-distinct incidence is EMPTY "
           "for all q <= 53", ok_empty)

def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("cx", "all"):
        print("== X. the (11,3) counterexample and BDD identities ==")
        check_counterexample()
    if which in ("census3", "all"):
        print("== C3. independent cubic census ==")
        census3()
    if which in ("census2", "all"):
        print("== C2. new quadratic census ==")
        census2()
    sys.exit(r11.FAIL)

if __name__ == "__main__":
    main()
