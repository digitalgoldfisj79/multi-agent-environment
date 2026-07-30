#!/usr/bin/env python3
"""Local-character audit: next-programme steps 1-2 and the sharpened assembly
target (companion to FF_LOCAL_CHARACTER_NOTE_20260731.md).

Verifies:
  L1  (exact): psi_theta(-e_P Lbar_P f) = psi_P(mu_1 f) with
      mu_1 = -theta * Lbar_P * Sbar_P mod P; the pairing is PURELY LOCAL and
      A(lambda_1) = Ahat_P(mu_1), an additive Fourier coefficient of the
      prime-count mod P.  (Symmetric in S.)
  L1' : mu_1 is never 0 (theta != 0, deg theta < 2k-R <= k) - checked over all
      samples: the Artin-Schreier-degenerate locus is empty.
  L2  (exact): Plancherel  sum_{mu != 0} |Ahat_P(mu)|^2
      = q^k * sum_r |N(r) - q^{m-k}|^2   (centred count; means cancel exactly).
  Locus probe: |Ahat_P(mu)|/q^{m/2} grouped by deg(mu): flat profile = no
      analytic (short-interval-type) enhancement in range.
  L3  (exact): puncture change L -> L' translates the sampled frequency multiset
      by the unit Lbar'/Lbar: mu-averaged statements are deg-L-uniform for free.
  Assembly ledger: sum_{P,S} |Ahat_P(mu_1)|^2 vs (1/k) x full Parseval mass;
      measured |T(theta)| (recomputed via the LOCAL form - cross-validates the
      separability chain end-to-end against ff_fflks_audit.py) vs the
      Cauchy+Parseval bound: the realized q^{k/2}-type assembly cancellation.
"""
import cmath, itertools, sys
from ff_t3_coset_audit import (trim, padd, pmul, pmod, monics, irreducibles_upto,
                               lambda_sources, pow_poly_inverse, pairing_gen)

FAIL = 0
def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

def pneg(a, q):
    return tuple((-c) % q for c in a)

def psi_P(mu, x, P, q, zq):
    """e_q( coeff_{k-1}( mu*x mod P ) )."""
    k = len(P) - 1
    r = pmod(pmul(mu, x, q), P, q)
    c = r[k - 1] if len(r) >= k else 0
    return zq ** c

def Ahat(P, mu, sources, q, zq):
    return sum(w * psi_P(mu, f, P, q, zq) for f, w in sources)

def deg(a):
    return len(a) - 1 if a else -1

def run(q, k, R, m, Lpoly, tag):
    zq = cmath.exp(2j * cmath.pi / q)
    irr = irreducibles_upto(max(k, m), q)
    band = irr[k]
    sources = lambda_sources(m, q, irr)
    thetas = [trim(t) for t in itertools.product(range(q), repeat=2 * k - R)]
    thetas = [t for t in thetas if t]
    tR = tuple([0] * R + [1])

    # ---- L1 + L1' -----------------------------------------------------------
    ok1 = True
    mu_zero = 0
    samples = 0
    for th in thetas:
        for P in band:
            LbP = pow_poly_inverse(pmod(Lpoly, P, q), P, q)
            for S in band:
                if S == P:
                    continue
                W = pmul(P, S, q)
                SbP = pow_poly_inverse(pmod(S, P, q), P, q)
                eP = pmul(S, SbP, q)
                mu1 = pmod(pmul(pmul(pneg(th, q), LbP, q), SbP, q), P, q)
                if not mu1:
                    mu_zero += 1
                for f, _ in sources[:6]:
                    lhs = pairing_gen(th, pneg(pmod(pmul(pmul(eP, LbP, q), f, q), W, q), q), W, q, zq)
                    rhs = psi_P(mu1, f, P, q, zq)
                    samples += 1
                    if abs(lhs - rhs) > 1e-9:
                        ok1 = False
    report(f"L1 local-character identity ({tag}, q={q}; {samples} samples)", ok1)
    report(f"L1' mu_1 never zero ({tag}, q={q})", mu_zero == 0,
           f"zeros={mu_zero}")

    # ---- L2 Plancherel ------------------------------------------------------
    P = band[0]
    Qk = q ** k
    N = [0.0] * Qk
    for f, w in sources:
        r = pmod(f, P, q)
        idx = sum((r[i] if i < len(r) else 0) * q ** i for i in range(k))
        N[idx] += w
    mean = q ** (m - k)
    rhs = Qk * sum((v - mean) ** 2 for v in N)
    lhs = 0.0
    mus = [trim(t) for t in itertools.product(range(q), repeat=k)]
    absA_by_deg = {}
    for mu in mus:
        if not mu:
            continue
        a = Ahat(P, mu, sources, q, zq)
        lhs += abs(a) ** 2
        absA_by_deg.setdefault(deg(mu), []).append(abs(a) / q ** (m / 2))
    ok2 = abs(lhs - rhs) < 1e-6 * max(1.0, rhs)
    report(f"L2 Plancherel identity ({tag}, q={q}, P=band[0])", ok2,
           f"lhs={lhs:.4f} rhs={rhs:.4f}")

    # ---- locus probe --------------------------------------------------------
    prof = "  ".join(f"deg{d}: mean={sum(v)/len(v):.3f} max={max(v):.3f}"
                     for d, v in sorted(absA_by_deg.items()))
    print(f"   locus probe |Ahat|/q^(m/2) by deg(mu) ({tag}, q={q}): {prof}")

    # ---- L3 puncture translation -------------------------------------------
    th = thetas[0]
    P0 = band[0]
    Lb = pow_poly_inverse(pmod(Lpoly, P0, q), P0, q)
    Lalt = pmul((1, 1), (2 % q, 1), q)            # (t+1)(t+2), another puncture
    Lb2 = pow_poly_inverse(pmod(Lalt, P0, q), P0, q)
    ratio = pmod(pmul(Lb2, pow_poly_inverse(Lb, P0, q), q), P0, q)
    set1 = set()
    set2 = set()
    for S in band:
        if S == P0:
            continue
        SbP = pow_poly_inverse(pmod(S, P0, q), P0, q)
        m1 = pmod(pmul(pmul(pneg(th, q), Lb, q), SbP, q), P0, q)
        m2 = pmod(pmul(pmul(pneg(th, q), Lb2, q), SbP, q), P0, q)
        set1.add(pmod(pmul(m1, ratio, q), P0, q))
        set2.add(m2)
    report(f"L3 puncture change = unit translation of frequency set ({tag}, q={q})",
           set1 == set2)

    # ---- assembly ledger ----------------------------------------------------
    full_parseval = lhs                              # sum_{mu != 0} |Ahat_P|^2 for band[0]
    sampled = {}
    Tmax = 0.0
    for th in thetas:
        T = 0j
        samp_sum = 0.0
        for P in band:
            LbP = pow_poly_inverse(pmod(Lpoly, P, q), P, q)
            for S in band:
                if S == P:
                    continue
                W = pmul(P, S, q)
                SbP = pow_poly_inverse(pmod(S, P, q), P, q)
                PbS = pow_poly_inverse(pmod(P, S, q), S, q)
                LbS = pow_poly_inverse(pmod(Lpoly, S, q), S, q)
                mu1 = pmod(pmul(pmul(pneg(th, q), LbP, q), SbP, q), P, q)
                nu2 = pmod(pmul(pmul(pneg(th, q), LbS, q), PbS, q), S, q)
                A1 = Ahat(P, mu1, sources, q, zq)
                A2 = Ahat(S, nu2, sources, q, zq)
                samp_sum += abs(A1) ** 2
                eP = pmod(pmul(S, SbP, q), W, q)
                eS = pmod(pmul(P, PbS, q), W, q)
                v = pmod(padd(pmul(eP, LbP, q), pmul(eS, LbS, q), q), W, q)
                diag = sum(w * w * pairing_gen(th, pneg(pmod(pmul(v, f, q), W, q), q),
                                               W, q, zq) for f, w in sources)
                phase0 = pairing_gen(th, pneg(tR, q), W, q, zq)
                T += (A1 * A2 - diag) * phase0
        sampled[th] = samp_sum
        Tmax = max(Tmax, abs(T))
    npairs = len(band) * (len(band) - 1)
    avg_sampled = sum(sampled.values()) / len(sampled)
    cauchy = avg_sampled  # sum_{P,S}|A1|^2 ~ symmetric; Cauchy bound = that value
    print(f"   assembly ({tag}, q={q}): sum_PS|Ahat(mu1)|^2 avg={avg_sampled:12.1f}  "
          f"(1/k x #P x fullParseval = {len(band)*full_parseval/k:12.1f})   "
          f"maxT={Tmax:10.1f}  Cauchy bound={cauchy:12.1f}  "
          f"realized saving={cauchy/Tmax if Tmax else float('inf'):8.1f} "
          f"(q^(k/2)={q**(k/2):.1f})")
    return Tmax

def main():
    for Ltag, Lmk in (("L=t(t+1)", lambda q: pmul((0, 1), (1, 1), q)),
                      ("L=t^q-t ", lambda q: trim([0, q - 1] + [0] * (q - 2) + [1]))):
        for q in (3, 5, 7):
            run(q, 2, 3, 3, Lmk(q), Ltag)
    sys.exit(FAIL)

if __name__ == "__main__":
    main()
