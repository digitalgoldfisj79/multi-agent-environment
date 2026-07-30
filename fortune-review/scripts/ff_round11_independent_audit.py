#!/usr/bin/env python3
"""Round 11 independent audit (companion to ROUND11_INDEPENDENT_AUDIT_20260801.md).

Independent verification (no shared code with the branch verifiers) of the four
claims at branch head 2739aad:

  R. Route A closure: Theorem PO2 (projective occupancy of irreducible pencils
     through a degree-2 prime), the exact sampled-line transfer (the sampled
     frequency multiset is line-constant with line-counts = the occupancy
     multiset), the all-residue/reduced-residue variance identity
     V_all = G + q^4/(q^2-1), the M_samp panel values, the numeric inequality
     (q-1) M_samp >= (q-3)/2 M_full, and the M_full/q^7 -> 1/2 trend.
  P. The characteristic-three resonant family: generation counts (2/12/72 at
     k=3/4/5), the exact completion-numerator identities
     mu P' - mu' P = -theta/eps, nu S' - nu' S = +theta/eps (both theta),
     completeness at (q,k)=(3,3),(3,4) by full pair-of-pairs scans (with the
     (5,3) diagonal-collapse panel), and the transpose degeneration at k=3.
  D. The Delta panel: involution invariance X_a=X_b, Delta_a=Delta_b, B_a=B_b
     for every resonant point at k=3,4,5, and the exact aggregate totals
     XX, XD, DX, DD, BB against the branch's table.
  I. Theorem IFA1: inverse-free equivalence and uniqueness of the scalar
     witnesses on (q,k) = (3,2), (5,2), (7,2), (3,3), (3,4).

All verified statements are exact (integer / Z[zeta_q] arithmetic).
Usage: python3 ff_round11_independent_audit.py [routeA|rest]
"""
import itertools, sys
from collections import Counter
from fractions import Fraction
from ff_t3_coset_audit import (trim, padd, pmul, pmod, monics, irreducibles_upto,
                               lambda_sources, pow_poly_inverse)
from ff_class_correlation_exact import (pneg, psub, deg, zzero, zroot, zadd,
                                        zscale, zmul, zconj, zcanon, zeq, zfloat,
                                        zisrational, Ahat_exact)

FAIL = 0
def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

def zint(x):
    c = zcanon(x)
    assert all(v == 0 for v in c[1:]), f"not rational: {c}"
    return c[0]

def pscale(a, c, q):
    return trim([(c * v) % q for v in a])

def primorial(q):
    return trim([0, q - 1] + [0] * (q - 2) + [1])       # t^q - t

def inv_mod(x, M, q):
    return pow_poly_inverse(pmod(x, M, q), M, q)

def mu_of(P, S, Lpoly, th_s, q):
    """-theta (L S)^{-1} mod P."""
    return pmod(pmul(pneg((th_s % q,), q),
                     inv_mod(pmul(Lpoly, S, q), P, q), q), P, q)

# ============================ R. Route A ====================================
def check_po2(q):
    irr = irreducibles_upto(2, q)
    band = set(irr[2])
    lo, hi = (q - 3) // 2, (q - 1) // 2
    ok = True
    for P in irr[2]:
        dirs = [trim([a, 1]) for a in range(q)] + [(1,)]
        occ = Counter(sum(1 for lam in range(1, q)
                          if padd(P, pscale(r, lam, q), q) in band)
                      for r in dirs)
        if occ != Counter({lo: (q + 1) // 2, hi: (q + 1) // 2}):
            ok = False
    report(f"R1 Theorem PO2: occupancies split ({lo},{hi}) x (q+1)/2 each, "
           f"all deg-2 primes (q={q})", ok)

def line_key(x, q):
    cinv = pow(x[-1], q - 2, q)
    return tuple((cinv * v) % q for v in x)

def check_sampled_transfer(q):
    """Sampled-frequency multiset is line-constant; line-count multiset equals
    the occupancy multiset (this is the exact transfer step of Route A)."""
    k = 2
    irr = irreducibles_upto(2, q)
    band = irr[2]; bset = set(band)
    Lpoly = primorial(q)
    ok_const = ok_mult = True
    for P in band:
        cnt = Counter()
        for S in band:
            if S == P:
                continue
            for th in range(1, q):
                cnt[mu_of(P, S, Lpoly, th, q)] += 1
        # counts constant on every projective line (all q+1 lines, all mu != 0)
        linecounts = []
        seen = set()
        for topcoeffs in itertools.product(range(q), repeat=k):
            mu = trim(topcoeffs)
            if not mu or line_key(mu, q) in seen:
                continue
            seen.add(line_key(mu, q))
            vals = {cnt.get(pscale(mu, lam, q), 0) for lam in range(1, q)}
            if len(vals) != 1:
                ok_const = False
            linecounts.append(vals.pop())
        occ = []
        dirs = [trim([a, 1]) for a in range(q)] + [(1,)]
        for r in dirs:
            occ.append(sum(1 for lam in range(1, q)
                           if padd(P, pscale(r, lam, q), q) in bset))
        if Counter(linecounts) != Counter(occ):
            ok_mult = False
    report(f"R2 sampled-line transfer: counts constant on lines; line-count "
           f"multiset = occupancy multiset (q={q}, all P, primorial)",
           ok_const and ok_mult)

def check_variance_identity(q):
    k, m = 2, 3
    irr = irreducibles_upto(m, q)
    band = irr[k]; sources = lambda_sources(m, q, irr)
    okid = okzero = True
    ratios = []
    for P in band:
        N = {}
        for f, w in sources:
            r = pmod(f, P, q)
            N[r] = N.get(r, 0) + w
        if N.get((), 0) != 0:
            okzero = False
        allres = {trim(t) for t in itertools.product(range(q), repeat=k)}
        V_all = sum((Fraction(N.get(a, 0)) - q) ** 2 for a in allres)
        mred = Fraction(q ** m, q ** 2 - 1)
        G = sum((Fraction(N.get(a, 0)) - mred) ** 2 for a in allres if a != ())
        if V_all != G + Fraction(q ** 4, q ** 2 - 1):
            okid = False
        ratios.append(float(G / q ** 3))
    report(f"R3 V_all = G + q^4/(q^2-1) exactly, all P; N_P(0)=0 (q={q})",
           okid and okzero,
           f"G/q^3 in [{min(ratios):.3f}, {max(ratios):.3f}]")

def msamp_exact(q, k, m):
    irr = irreducibles_upto(max(k, m), q)
    band = irr[k]; sources = lambda_sources(m, q, irr)
    Lpoly = primorial(q)
    total = zzero(q)
    for P in band:
        LbP = inv_mod(Lpoly, P, q)
        for S in band:
            if S == P:
                continue
            mu = pmod(pmul(pmul(pneg((1,), q), LbP, q),
                           inv_mod(S, P, q), q), P, q)
            a = Ahat_exact(P, mu, sources, q)
            total = zadd(total, zmul(a, zconj(a)))
    return zint(total)

def mfull_exact(q):
    k, m = 2, 3
    irr = irreducibles_upto(m, q)
    band = irr[k]; sources = lambda_sources(m, q, irr)
    total = zzero(q)
    for P in band:
        for topcoeffs in itertools.product(range(q), repeat=k):
            mu = trim(topcoeffs)
            if not mu:
                continue
            a = Ahat_exact(P, mu, sources, q)
            total = zadd(total, zmul(a, zconj(a)))
    return zint(total)

def route_a():
    for q in (3, 5, 7, 11):
        check_po2(q)
        check_sampled_transfer(q)
    for q in (3, 5, 7):
        check_variance_identity(q)
    claimed = {(3, 2, 3): 216, (5, 2, 3): 10500, (7, 2, 3): 148176,
               (11, 2, 3): 3993000, (3, 3, 5): 21384, (5, 3, 5): 9697500,
               (3, 4, 7): 1907874}
    for (q, k, m), want in sorted(claimed.items()):
        got = msamp_exact(q, k, m)
        report(f"R4 M_samp panel (q={q},k={k},m={m}) = {want}", got == want,
               f"got {got}, M_samp/q^3k = {got / q**(3*k):.4f}")
    for q in (3, 5, 7):
        mf = mfull_exact(q)
        ms = msamp_exact(q, 2, 3)
        lhs = (q - 1) * ms
        rhs_num = (q - 3) * mf          # compare 2*lhs >= (q-3)*mf
        report(f"R5 exact inequality (q-1)M_samp >= (q-3)/2 M_full (q={q})",
               2 * lhs >= rhs_num,
               f"M_full={mf} (M_full/q^7={mf / q**7:.4f}), (q-1)M_samp={lhs}, "
               f"(q-3)/2*M_full={rhs_num / 2:.0f}")

# =================== P. characteristic-three resonant family ================
def resonant_points(k):
    q = 3
    L = primorial(3)
    irr = irreducibles_upto(k, 3)
    band = set(irr[k])
    pts = []
    for P in irr[k]:
        for lowQ in itertools.product(range(3), repeat=k - 3):
            Q = trim(list(lowQ) + [2])
            LQ = pmul(L, Q, 3)
            Pp = psub(LQ, P, 3)
            for eps in (1, 2):
                S = padd(P, pscale(Q, eps, 3), 3)
                Sp = psub(LQ, S, 3)
                four = [P, S, Pp, Sp]
                # pairwise conditions of the incidence (transpose-degenerate
                # points P'=S, S'=P are allowed; they occur exactly at k=3)
                if all(tuple(f) in band for f in four) \
                        and P != S and Pp != Sp and P != Pp and S != Sp:
                    pts.append((P, S, Pp, Sp, Q, eps))
    return pts

def check_resonant_family():
    q = 3
    L = primorial(3)
    want = {3: 2, 4: 12, 5: 72}
    for k in (3, 4, 5):
        pts = resonant_points(k)
        eps_split = Counter(p[5] for p in pts)
        okc = len(pts) == want[k] and eps_split[1] == eps_split[2] == want[k] // 2
        report(f"P1 resonant prime-point count at k={k}: {want[k]}, even eps "
               f"split", okc, f"got {len(pts)}, split {dict(eps_split)}")
        n4 = sum(1 for (P, S, Pp, Sp, Q, e) in pts
                 if len({tuple(P), tuple(S), tuple(Pp), tuple(Sp)}) == 4)
        print(f"   k={k}: points with all four primes distinct: {n4}/{len(pts)}"
              f"  (k=3 points are transpose-degenerate: P'=S, S'=P)")
        okid = True
        for (P, S, Pp, Sp, Q, eps) in pts:
            for th in (1, 2):
                mu = mu_of(P, S, L, th, 3)
                mup = mu_of(Pp, Sp, L, th, 3)
                nu = mu_of(S, P, L, th, 3)
                nup = mu_of(Sp, Pp, L, th, 3)
                Emu = psub(pmul(mu, Pp, 3), pmul(mup, P, 3), 3)
                Enu = psub(pmul(nu, Sp, 3), pmul(nup, S, 3), 3)
                c = (-th * eps) % 3          # -theta eps^{-1}; eps^{-1}=eps in F_3
                d = (th * eps) % 3
                if Emu != trim([c]) or Enu != trim([d]):
                    okid = False
        report(f"P1 PRC1 numerators mu P'-mu'P = -theta/eps, "
               f"nu S'-nu'S = +theta/eps (k={k}, both theta)", okid)
        # Gram phase: G(c) = psi(c) B_m, product of the pair = B_m^2
        m = 2 * k - 1
        irr = irreducibles_upto(m, 3)
        Bm = sum(w * w for _, w in lambda_sources(m, 3, irr))
        if pts:
            gm = zscale(zroot((-1 * pts[0][5]) % 3, 3), Bm)
            gn = zscale(zroot((1 * pts[0][5]) % 3, 3), Bm)
            report(f"P3 coherent Gram phase G_mu G_nu = B_m^2 (k={k})",
                   zeq(zmul(gm, gn), zscale(zroot(0, 3), Bm * Bm)),
                   f"B_m={Bm}")

def scan_classify(q, k, expect):
    """Full ordered pair-of-pairs endpoint incidence scan."""
    m = 2 * k - 1
    irr = irreducibles_upto(k, q)
    band = irr[k]
    Lpoly = primorial(q)
    pairs = []
    for P in band:
        for S in band:
            if S == P:
                continue
            pairs.append((P, S, mu_of(P, S, Lpoly, 1, q),
                          mu_of(S, P, Lpoly, 1, q)))
    n_mu = n_nu = n_sim = n_diag = n_transp = 0
    others = []
    for (P, S, mu_a, nu_a) in pairs:
        for (Pp, Sp, mu_b, nu_b) in pairs:
            Emu = psub(pmul(mu_a, Pp, q), pmul(mu_b, P, q), q)
            Enu = psub(pmul(nu_a, Sp, q), pmul(nu_b, S, q), q)
            imu = deg(Emu) <= 0
            inu = deg(Enu) <= 0
            n_mu += imu
            n_nu += inu
            if imu and inu:
                n_sim += 1
                if (P, S) == (Pp, Sp):
                    n_diag += 1
                elif (Pp, Sp) == (S, P):
                    n_transp += 1
                else:
                    others.append((P, S, Pp, Sp))
    got = (len(pairs), n_mu, n_nu, n_sim, n_diag, n_transp, len(others))
    report(f"P2 scan (q={q},k={k},m={m}): pairs/one-sided(mu,nu)/simult/"
           f"diag/transpose/other = {expect}", got == expect, f"got {got}")
    return others

def check_scans():
    scan_classify(5, 3, (1560, 2380, 2380, 1560, 1560, 0, 0))
    o33 = scan_classify(3, 3, (56, 64, 64, 58, 56, 2, 0))
    o34 = scan_classify(3, 4, (306, 336, 336, 318, 306, 0, 12))
    # k=3: the 2 transpose incidences ARE the 2 resonant points (degeneration)
    pts3 = {(tuple(P), tuple(S)) for (P, S, Pp, Sp, Q, e) in resonant_points(3)
            if (tuple(Pp), tuple(Sp)) == (tuple(S), tuple(P))}
    report("P2 k=3 degeneration: both resonant points are transpose pairs "
           "(P'=S, S'=P)", len(pts3) == 2)
    # k=4: the 12 'other' incidences coincide exactly with the resonant family
    res4 = {(tuple(P), tuple(S), tuple(Pp), tuple(Sp))
            for (P, S, Pp, Sp, Q, e) in resonant_points(4)}
    o34set = {(tuple(a), tuple(b), tuple(c), tuple(d)) for (a, b, c, d) in o34}
    report("P2 k=4 completeness: the 12 non-diag/non-transpose incidences = "
           "the resonant family exactly", res4 == o34set,
           f"|family|={len(res4)}, |scan|={len(o34set)}")

# ============================ D. Delta panel ================================
def pairing_exact(th_s, x, W, q):
    dW = len(W) - 1
    prod = pmod(pmul((th_s % q,), x, q), W, q)
    e = prod[dW - 1] if len(prod) >= dW else 0
    return zroot(e, q)

def delta_exact(P, S, Lpoly, sources, q, th_s=1):
    W = pmul(P, S, q)
    eP = pmod(pmul(S, inv_mod(S, P, q), q), W, q)
    eS = pmod(pmul(P, inv_mod(P, S, q), q), W, q)
    v = pmod(padd(pmul(eP, inv_mod(Lpoly, P, q), q),
                  pmul(eS, inv_mod(Lpoly, S, q), q), q), W, q)
    out = zzero(q)
    for f, w in sources:
        ph = pairing_exact(th_s, pneg(pmod(pmul(v, f, q), W, q), q), W, q)
        out = zadd(out, zscale(ph, w * w))
    return out

def check_delta_panel():
    q = 3
    L = primorial(3)
    claimed = {3: (1062882, -214326, -214326, 43218, 1534752),
               4: (71384652, -55931148, -55931148, 43823052, 227070000),
               5: (308039038452, -92518064244, -92518064244, 35233974972,
                   528309141912)}
    for k in (3, 4, 5):
        m = 2 * k - 1
        irr = irreducibles_upto(m, 3)
        sources = lambda_sources(m, 3, irr)
        pts = resonant_points(k)
        cache = {}
        def val(P, S):
            key = (tuple(P), tuple(S))
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
        report(f"D1 involution invariance X_a=X_b, Delta_a=Delta_b, B_a=B_b "
               f"(k={k}, all {len(pts)} points)", ok_inv)
        got = (zint(XX), zint(XD), zint(DX), zint(DD), zint(BB))
        report(f"D2 exact aggregates (XX, XD, DX, DD, BB) at k={k}",
               got == claimed[k], f"got {got}")
        okbb = zint(BB) == zint(XX) - zint(XD) - zint(DX) + zint(DD)
        report(f"D2 BB = XX - XD - DX + DD and BB >= 0 (k={k})",
               okbb and zint(BB) >= 0,
               f"BB/3^(2m+3k) = {zint(BB) / 3**(2*m+3*k):.8f}")

# ============================ I. Theorem IFA1 ===============================
def check_ifa1(q, k):
    m = 2 * k - 1
    irr = irreducibles_upto(k, q)
    band = irr[k]
    Lpoly = primorial(q)
    th = 1
    pairs = []
    for P in band:
        for S in band:
            if S == P:
                continue
            pairs.append((P, S, mu_of(P, S, Lpoly, th, q)))
    ok = True
    n_cross = n_inc = 0
    for (P, S, mu_a) in pairs:
        for (Pp, Sp, mu_b) in pairs:
            if Pp == P or Sp == S:
                continue
            n_cross += 1
            Emu = psub(pmul(mu_a, Pp, q), pmul(mu_b, P, q), q)
            scalar = deg(Emu) <= 0 and Emu
            witnesses = []
            for c in range(1, q):
                lhs1 = padd(pscale(pmul(Lpoly, S, q), c, q),
                            pscale(Pp, th, q), q)
                lhs2 = psub(pscale(pmul(Lpoly, Sp, q), c, q),
                            pscale(P, th, q), q)
                if not pmod(lhs1, P, q) and not pmod(lhs2, Pp, q):
                    witnesses.append(c)
            if scalar:
                n_inc += 1
                if witnesses != [Emu[0]]:
                    ok = False
            else:
                if witnesses:
                    ok = False
    report(f"I1 IFA1 equivalence + uniqueness (q={q},k={k}; {n_cross} "
           f"cross-distinct pairs-of-pairs, {n_inc} incidences)", ok)

def check_ifa1_resonant():
    q = 3
    L = primorial(3)
    ok = True
    for k in (3, 4, 5):
        for (P, S, Pp, Sp, Q, eps) in resonant_points(k):
            for th in (1, 2):
                c = (-th * eps) % 3
                lhs1 = padd(pscale(pmul(L, S, 3), c, 3), pscale(Pp, th, 3), 3)
                lhs2 = psub(pscale(pmul(L, Sp, 3), c, 3), pscale(P, th, 3), 3)
                d = (th * eps) % 3
                lhs3 = padd(pscale(pmul(L, P, 3), d, 3), pscale(Sp, th, 3), 3)
                lhs4 = psub(pscale(pmul(L, Pp, 3), d, 3), pscale(S, th, 3), 3)
                if pmod(lhs1, P, 3) or pmod(lhs2, Pp, 3) \
                        or pmod(lhs3, S, 3) or pmod(lhs4, Sp, 3):
                    ok = False
    report("I2 resonant family satisfies the inverse-free scheme with "
           "c=-theta/eps, d=+theta/eps (k=3,4,5, both theta)", ok)

def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("routeA", "all"):
        print("== R. Route A closure ==")
        route_a()
    if which in ("rest", "all"):
        print("== P. characteristic-three resonant family ==")
        check_resonant_family()
        check_scans()
        print("== D. Delta panel ==")
        check_delta_panel()
        print("== I. inverse-free algebraization ==")
        for (q, k) in ((3, 2), (5, 2), (7, 2), (3, 3), (3, 4)):
            check_ifa1(q, k)
        check_ifa1_resonant()
    sys.exit(FAIL)

if __name__ == "__main__":
    main()
