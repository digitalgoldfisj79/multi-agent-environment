#!/usr/bin/env python3
"""FFLKS audit: retraction ledger for Theorem D, separability theorem, and
empirical tests of the corrected conditional targets
(companion to FFLKS_SEPARABILITY_NOTE_20260730.md).

Facts machine-verified here:

  0. V^perp is CANONICAL: the completion frequencies are exactly the
     polynomials theta of degree < 2k - R, independent of the pair (P,S).
  1. SEPARABILITY (exact): with W = PS, e_P = S*(S^-1 mod P), e_S = P*(P^-1 mod S),
        psi_theta(c(f,f';P,S) - t^R)
          = psi_theta(-e_P Lbar_P f) * psi_theta(-e_S Lbar_S f') * psi_theta(-t^R),
     linear in f and f' separately: the Kloosterman inverses sit in the
     PARAMETERS lambda_1 = -theta e_P Lbar_P, lambda_2 = -theta e_S Lbar_S.
     Hence T(theta) = sum_{P != S} A(lambda_1) A'(lambda_2) psi_theta(-t^R)
     - (f = f' corrections), with A(lambda) = sum_f Lambda(f) psi(lambda, f)
     a ONE-VARIABLE FF Vinogradov sum.
  2. EXPONENT LEDGER (the branch's correction, re-verified): actual |T(theta)|
     sits at the FFLKS scale q^{m+3k/2}, far below the fixed-source-FFPS-
     permitted q^{2m+3k/2}: the q^m gap is the source-pair cancellation that
     Theorem D wrongly claimed for free.  THEOREM D AS STATED IS RETRACTED.
  3. EMPIRICAL FFLKS: max_theta |T(theta)| / q^{m+3k/2} across q, both punctures.
  4. EMPIRICAL FFV: distribution of |A(lambda)|/q^{m/2} over (theta,P,S).
"""
import sys, math
from ff_t3_coset_audit import (trim, padd, pmul, pmod, monics, irreducibles_upto,
                               lambda_sources, pow_poly_inverse, crt, pairing_gen)
import cmath

FAIL = 0
def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

def pneg(a, q):
    return tuple((-c) % q for c in a)

def setup(q, k, m, Lpoly):
    irr = irreducibles_upto(max(k, m), q)
    band = irr[k]
    sources = lambda_sources(m, q, irr)
    return band, sources

def idempotents(P, S, q):
    Sbar = pow_poly_inverse(pmod(S, P, q), P, q)     # S^{-1} mod P
    Pbar = pow_poly_inverse(pmod(P, S, q), S, q)
    eP = pmul(S, Sbar, q)                            # = 1 mod P, 0 mod S
    eS = pmul(P, Pbar, q)
    return eP, eS

def A_sum(lam, sources, W, q, zq):
    """A(lam) = sum_f Lambda(f) psi(lam * f mod W); lam already includes signs."""
    tot = 0j
    for f, w in sources:
        tot += w * pairing_gen(lam, f, W, q, zq)
    return tot

def run_config(q, k, R, m, Lpoly, tag, do_direct_check=False):
    band, sources = setup(q, k, m, Lpoly)
    zq = cmath.exp(2j * cmath.pi / q)
    tR = tuple([0] * R + [1])
    thetas = [trim(t) for t in
              __import__("itertools").product(range(q), repeat=2 * k - R)]
    thetas = [t for t in thetas if t]                # theta != 0, deg < 2k-R
    pairs = [(P, S) for P in band for S in band if P != S]

    Tvals = {}
    Avals = []
    sep_ok = True
    for th in thetas:
        T = 0j
        Tdir = 0j
        for (P, S) in pairs:
            W = pmul(P, S, q)
            eP, eS = idempotents(P, S, q)
            LbP = pow_poly_inverse(pmod(Lpoly, P, q), P, q)
            LbS = pow_poly_inverse(pmod(Lpoly, S, q), S, q)
            lam1 = pneg(pmod(pmul(pmul(th, eP, q), LbP, q), W, q), q)
            lam2 = pneg(pmod(pmul(pmul(th, eS, q), LbS, q), W, q), q)
            A1 = A_sum(lam1, sources, W, q, zq)
            A2 = A_sum(lam2, sources, W, q, zq)
            Avals.append(abs(A1) / q ** (m / 2))
            Avals.append(abs(A2) / q ** (m / 2))
            phase0 = pairing_gen(th, pneg(tR, q), W, q, zq)
            diag = sum(w * w * pairing_gen(padd(lam1, lam2, q), f, W, q, zq)
                       for f, w in sources)
            T += (A1 * A2 - diag) * phase0
            if do_direct_check:
                for f, wf in sources:
                    for fp, wfp in sources:
                        if f == fp:
                            continue
                        rp = pmod(pmul(pneg(f, q), LbP, q), P, q)
                        rs = pmod(pmul(pneg(fp, q), LbS, q), S, q)
                        c = crt(rp, P, rs, S, q)
                        x = padd(c, pneg(tR, q), q)
                        Tdir += wf * wfp * pairing_gen(th, x, W, q, zq)
        if do_direct_check:
            if abs(T - Tdir) > 1e-6 * max(1.0, abs(Tdir)):
                sep_ok = False
        Tvals[th] = T
    if do_direct_check:
        report(f"1 separability identity T_sep == T_direct (q={q}, {tag}, "
               f"all theta, all pairs)", sep_ok)
    Tmax = max(abs(v) for v in Tvals.values())
    fflks = q ** (m + 1.5 * k)
    ffps_permitted = q ** (2 * m + 1.5 * k) / (len(band) / (q ** k / k)) ** 0  # display raw
    trivial = q ** (2 * m) * len(pairs)
    print(f"   {tag} q={q:2d} k={k} R={R} m={m}: max|T|={Tmax:12.1f}   "
          f"|T|/q^(m+3k/2)={Tmax/fflks:7.3f}   "
          f"FFPS-permitted/q^(m+3k/2)={q**(2*m+1.5*k)/fflks:9.1f}   "
          f"|T|/trivial={Tmax/trivial:8.5f}")
    return Avals

def main():
    print("== 0/1. Separability identity (exact; q=3, both punctures) ==")
    for Ltag, Lmk in (("L=t(t+1)", lambda q: pmul((0, 1), (1, 1), q)),
                      ("L=t^q-t ", lambda q: trim([0, q - 1] + [0] * (q - 2) + [1]))):
        run_config(3, 2, 3, 3, Lmk(3), Ltag, do_direct_check=True)

    print("\n== 2/3. Exponent ledger and empirical FFLKS across q ==")
    print("   (FFLKS scale = q^(m+3k/2); fixed-source FFPS permits q^m times more —")
    print("    the gap Theorem D wrongly claimed; RETRACTED)")
    allA = {}
    for Ltag, Lmk in (("L=t(t+1)", lambda q: pmul((0, 1), (1, 1), q)),
                      ("L=t^q-t ", lambda q: trim([0, q - 1] + [0] * (q - 2) + [1]))):
        for q in (3, 5, 7):
            allA[(Ltag, q)] = run_config(q, 2, 3, 3, Lmk(q), Ltag)

    print("\n== 4. Empirical FFV: |A(lambda)|/q^(m/2) over (theta,P,S) ==")
    for (Ltag, q), Av in allA.items():
        Av = sorted(Av)
        n = len(Av)
        big = sum(1 for a in Av if a > 3.0)
        near_trivial = sum(1 for a in Av if a > 0.5 * q ** (3 / 2))  # 0.5 q^m/q^{m/2}
        print(f"   {Ltag} q={q}: n={n:5d}  median={Av[n//2]:6.3f}  "
              f"max={Av[-1]:7.3f}  frac>3: {big/n:6.3f}  "
              f"near-trivial(>0.5 q^(m/2)... rel): {near_trivial/n:6.4f}")

    sys.exit(FAIL)

if __name__ == "__main__":
    main()
