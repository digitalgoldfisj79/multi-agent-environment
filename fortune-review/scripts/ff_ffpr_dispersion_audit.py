#!/usr/bin/env python3
"""FFPR via the pair-family second moment: audit of the dispersion attempt
(companion to FFPR_DISPERSION_NOTE_20260731.md).

Objects (endpoint configuration k=2, m=3=2k-1, R=3, both punctures):

  W(f') = sum_{P != S} Ahat_P(mu_1(P,S)) psi_S(nu_2(P,S) f')
  D2nd  = sum_{f' monic, deg m} |W(f')|^2          (the pair-family second moment)

Checks:
  D1 (exact completion dichotomy): for pairs of pairs ((P,S),(P',S')),
      sum_{f' monic deg m} psi_S(nu f') conj(psi_S'(nu' f'))
        = q^m * unimodular   if deg(nu S' - nu' S) <= 2k-m-1,
        = 0                  otherwise.
      Verified for every pair of pairs.
  D2 (coincidence classification at the endpoint m = 2k-1): coincident
      pairs-of-pairs have nu S' - nu' S = E in F_q; E = 0 forces the full
      diagonal (P,S) = (P',S'); E != 0 forces the multiplicative relation
      S' = c_E * P (mod S) (class size <= q^2 per (P,S,E)).  Verified by
      enumeration.
  D3 ledger: D2nd computed directly equals q^m * (diagonal mass) + (E != 0
      class mass); measure the class/diagonal ratio (oscillation test) and
      the dispersion chain |T| <= sqrt(m q^m D2nd) against measured |T| and
      the FFPR target q^{m+3k/2}.
"""
import cmath, itertools, sys
from ff_t3_coset_audit import (trim, padd, pmul, pmod, monics, irreducibles_upto,
                               lambda_sources, pow_poly_inverse, pairing_gen)
from ff_local_character_audit import psi_P, Ahat, pneg

FAIL = 0
def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

def deg(a):
    return len(a) - 1 if a else -1

def psub(a, b, q):
    return padd(a, pneg(b, q), q)

def run(q, k, R, m, Lpoly, tag):
    zq = cmath.exp(2j * cmath.pi / q)
    irr = irreducibles_upto(max(k, m), q)
    band = irr[k]
    sources = lambda_sources(m, q, irr)
    th = trim([1])                                   # one nonzero theta (deg < 2k-R)
    # pair data: (P, S) -> (mu1, nu2)
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

    # ---- D1: completion dichotomy ------------------------------------------
    ok1 = True
    coincident = []                                  # indices of coincident pairs
    thresh = 2 * k - m - 1
    for i, (P, S, mu1, nu2) in enumerate(pairs):
        for j, (Pp, Sp, mu1p, nu2p) in enumerate(pairs):
            E = psub(pmul(nu2, Sp, q), pmul(nu2p, S, q), q)
            pred_coincident = deg(E) <= thresh
            tot = 0j
            for fp in monics(m, q):
                tot += psi_P(nu2, fp, S, q, zq) * psi_P(nu2p, fp, Sp, q, zq).conjugate()
            if pred_coincident:
                if abs(abs(tot) - q ** m) > 1e-6:
                    ok1 = False
                coincident.append((i, j, E))
            else:
                if abs(tot) > 1e-6:
                    ok1 = False
    report(f"D1 completion dichotomy ({tag}, q={q}, all {len(pairs)}^2 pairs of pairs)",
           ok1, f"coincident={len(coincident)} of {len(pairs)**2}")

    # ---- D2: endpoint classification ---------------------------------------
    assert m == 2 * k - 1
    ok2 = True
    n_diag = n_off = 0
    for (i, j, E) in coincident:
        P, S, mu1, nu2 = pairs[i]
        Pp, Sp, mu1p, nu2p = pairs[j]
        if deg(E) <= -1:                             # E = 0
            if (P, S) != (Pp, Sp):
                ok2 = False
            n_diag += 1
        else:                                        # E in F_q^*
            n_off += 1
            # claim: S' = c_E * P (mod S) for the unit c_E determined by
            # -theta Lbar_S Pbar_S * S' = E (mod S)  =>  S' = -E * thetabar * L * P / 1 (mod S)
            LS = pmod(Lpoly, S, q)
            thS = pmod(th, S, q)
            thbar = pow_poly_inverse(thS, S, q)
            cE = pmod(pmul(pmul(pneg(E, q), thbar, q), LS, q), S, q)
            lhs = pmod(Sp, S, q)
            rhs = pmod(pmul(cE, P, q), S, q)
            if lhs != rhs:
                ok2 = False
    report(f"D2 endpoint classification ({tag}, q={q})", ok2,
           f"diagonal={n_diag} multiplicative-class={n_off}")

    # ---- D3: second moment and dispersion ledger ---------------------------
    Adict = {}
    for (P, S, mu1, nu2) in pairs:
        Adict[(tuple(P), tuple(S))] = Ahat(P, mu1, sources, q, zq)
    D2nd = 0.0
    for fp in monics(m, q):
        Wv = 0j
        for (P, S, mu1, nu2) in pairs:
            Wv += Adict[(tuple(P), tuple(S))] * psi_P(nu2, fp, S, q, zq)
        D2nd += abs(Wv) ** 2
    diag_mass = q ** m * sum(abs(v) ** 2 for v in Adict.values())
    class_mass = D2nd - diag_mass
    # dispersion chain vs measured T (Lambda-weighted, no diagonal correction)
    T = 0j
    for fp, w in sources:
        Wv = 0j
        for (P, S, mu1, nu2) in pairs:
            Wv += Adict[(tuple(P), tuple(S))] * psi_P(nu2, fp, S, q, zq)
        T += w * Wv
    lam2 = sum(w * w for _, w in sources)
    chain = (lam2 * D2nd) ** 0.5
    target = q ** (m + 1.5 * k)
    print(f"   D3 ({tag}, q={q}): D2nd={D2nd:12.1f}  q^m*diag={diag_mass:12.1f}  "
          f"class/diag={class_mass/diag_mass:+7.3f}")
    print(f"      |T|={abs(T):10.1f}  dispersion bound={chain:10.1f}  "
          f"Cauchy ceiling~{q**(m+2*k):10.1f}  FFPR target={target:10.1f}  "
          f"bound/target={chain/target:6.2f}")

def main():
    for Ltag, Lmk in (("L=t(t+1)", lambda q: pmul((0, 1), (1, 1), q)),
                      ("L=t^q-t ", lambda q: trim([0, q - 1] + [0] * (q - 2) + [1]))):
        for q in (3, 5):
            run(q, 2, 3, 3, Lmk(q), Ltag)
    sys.exit(FAIL)

if __name__ == "__main__":
    main()
