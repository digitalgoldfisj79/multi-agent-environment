#!/usr/bin/env python3
"""Independent audit of the full-source completion sequence
(FULL_SOURCE_COMPLETION_AND_CENTERED_DETERMINANT_20260730.md, PR #33 head 7237374).

Independent implementation; no code shared with the branch verifiers.

Sections:
  A. (1.2)  Lambda = sum_{d|n, d<=Y} mu(d) c_Y(n/d), exact (formal prime-exponent
            vectors), all n <= H, panels X = 11, 17, 23.
  B. (2.2)  Completion: sum_d mu(d) sum_{m<=H/d, dm=a mod p} c_Y(m) = psi(H;p,a),
            exact, every residue a, two band primes per panel.
  C. (2.5)  Character collapse to the ordinary Lambda character sum, every chi mod p.
  D. (3.1)  A_{j,p} = -w_p D_p(-P_j) + log p/(p-2) vs direct survivor evaluation
            at actual primorial centres.
  E. (4.2)  Centred determinant reordering, direct pair-sum vs variance, X = 11, 17.
  F.        Actual-source diagnostics through X ~ 300: V/(HX), R_R/H^2
            (independent reproduction of the branch's 0.36-0.69 and 0.06-0.12).
  G.        Formal falsity exhibit for the reviewer's own uncentred SDD(X) box:
            D = 1 cell with gamma = Lambda on (M, 2M], and a mid-D Mobius cell;
            E/(DM) grows like a power of X (the density main term).  RETRACTION.
  H.        NEW: cross-modulus covariance diagnostic for {D_p(-P_j)}_p over the
            centre block, against a random-residue control.  Tests whether the
            Cauchy-over-p loss is real for the orbit samples.  EMPIRICAL ONLY.
"""
import cmath, math, sys
import numpy as np

FAIL = 0
def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = False
    return np.nonzero(s)[0].tolist()

def spf_table(n):
    spf = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf

def lambda_table(n):
    """Lambda(k) for k <= n (float)."""
    spf = spf_table(n)
    lam = np.zeros(n + 1)
    for k in range(2, n + 1):
        p = spf[k]
        m = k
        while m % p == 0:
            m //= p
        if m == 1:
            lam[k] = math.log(p)
    return lam

def factorize(n):
    f = {}
    x, p = n, 2
    while p * p <= x:
        while x % p == 0:
            f[p] = f.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f

def mobius(n):
    f = factorize(n)
    if any(e > 1 for e in f.values()):
        return 0
    return -1 if len(f) % 2 else 1

def divisors(n):
    ds = [1]
    for p, e in factorize(n).items():
        ds = [d * p ** a for d in ds for a in range(e + 1)]
    return ds

def vec_add(t, n, c):
    for p, e in factorize(n).items():
        t[p] = t.get(p, 0) + c * e
        if t[p] == 0:
            del t[p]

def cY_vec(m, Y):
    """Formal prime-exponent vector of c_Y(m) = log m + (mu_{>Y}*1*log)(m)."""
    v = {}
    vec_add(v, m, 1)
    for a in divisors(m):
        if a <= Y or not mobius(a):
            continue
        rem = m // a
        for e in divisors(rem):
            vec_add(v, rem // e, mobius(a))
    return v

def cY_float(m, Y):
    s = math.log(m) if m > 1 else 0.0
    for a in divisors(m):
        if a <= Y or not mobius(a):
            continue
        rem = m // a
        for e in divisors(rem):
            c = rem // e
            if c > 1:
                s += mobius(a) * math.log(c)
    return s

def lam_vec(n):
    f = factorize(n)
    return {next(iter(f)): 1} if len(f) == 1 else {}

def panel_params(X, eta_num=4, eta_den=5):
    H = eta_num * X * X // eta_den
    Y = math.isqrt(H)
    if Y * Y < H:
        Y += 1
    return H, Y

# ------------------------------------------------------------------ A
def check_A(X):
    H, Y = panel_params(X)
    ok = True
    for n in range(1, H + 1):
        v = {}
        for d in divisors(n):
            if d <= Y and mobius(d):
                cv = cY_vec(n // d, Y)
                for p, e in cv.items():
                    v[p] = v.get(p, 0) + mobius(d) * e
                    if v[p] == 0:
                        del v[p]
        if v != lam_vec(n):
            ok = False
            break
    report(f"(1.2) Lambda = mu_<=Y * c_Y, all n <= H   (X={X}, H={H}, Y={Y})", ok)

# ------------------------------------------------------------------ B
def check_B(X):
    H, Y = panel_params(X)
    band = [p for p in primes_upto(2 * X) if p > X][:2]
    for p in band:
        ok = True
        for a in range(p):
            lhs = {}
            for d in range(1, Y + 1):
                if not mobius(d):
                    continue
                dinv_a = None
                for m in range(1, H // d + 1):
                    if (d * m) % p == a % p:
                        cv = cY_vec(m, Y)
                        for q, e in cv.items():
                            lhs[q] = lhs.get(q, 0) + mobius(d) * e
                            if lhs[q] == 0:
                                del lhs[q]
            rhs = {}
            for n in range(1, H + 1):
                if n % p == a % p:
                    lv = lam_vec(n)
                    for q, e in lv.items():
                        rhs[q] = rhs.get(q, 0) + e
                        if rhs[q] == 0:
                            del rhs[q]
            if lhs != rhs:
                ok = False
                break
        report(f"(2.2) completion = psi(H;p,a), all residues   (X={X}, p={p})", ok)

# ------------------------------------------------------------------ C
def check_C(X):
    H, Y = panel_params(X)
    p = next(q for q in primes_upto(2 * X) if q > X)
    g = next(g for g in range(2, p) if all(pow(g, (p - 1) // q, p) != 1
             for q in factorize(p - 1)))
    dlog = {}
    x = 1
    for t in range(p - 1):
        dlog[x] = t
        x = x * g % p
    lam = lambda_table(H)
    cfl = {}
    ok = True
    for k in range(p - 1):          # all characters incl. principal
        def chi(n):
            if n % p == 0:
                return 0.0
            return cmath.exp(2j * cmath.pi * k * dlog[n % p] / (p - 1))
        lhs = 0.0
        for d in range(1, Y + 1):
            md = mobius(d)
            if not md:
                continue
            for m in range(1, H // d + 1):
                if m % p == 0:
                    continue
                if (m, Y) not in cfl:
                    cfl[(m, Y)] = cY_float(m, Y)
                lhs += md * chi(d) * cfl[(m, Y)] * chi(m)
        rhs = sum(lam[n] * chi(n) for n in range(2, H + 1))
        if abs(lhs - rhs) > 1e-7 * max(1.0, abs(rhs)):
            ok = False
            break
    report(f"(2.5) character collapse, all chi mod p   (X={X}, p={p})", ok)

# ------------------------------------------------------------------ D
def check_D(X):
    H, Y = panel_params(X)
    ps = primes_upto(max(H, 4 * X))
    zs = [q for q in ps if X <= q < 2 * X]
    K = max(1, min(len(zs), math.ceil(math.log(X))))
    zs = zs[:K]
    centres = []
    for z in zs:
        P = 1
        for q in ps:
            if q > z:
                break
            P *= q
        centres.append(P)
    Z = zs[-1]
    band = [q for q in ps if Z < q <= min(2 * Z, H)]
    lam = lambda_table(H)
    psi_H = float(lam.sum())
    ok = True
    worst = 0.0
    for P in centres:
        for p in band:
            wp = (p - 1) / (p - 2)
            # direct evaluation
            direct = 0.0
            for n in range(2, H + 1):
                if lam[n]:
                    hit = (P + n) % p == 0
                    direct += lam[n] * (1.0 / (p - 2) - (wp if hit else 0.0))
            # formula
            a = (-P) % p
            psi_a = sum(lam[n] for n in range(2, H + 1) if n % p == a)
            Psi_p = sum(lam[n] for n in range(2, H + 1) if n % p != 0)
            Dp = psi_a - Psi_p / (p - 1)
            formula = -wp * Dp + (math.log(p) / (p - 2) if p <= H else 0.0)
            worst = max(worst, abs(direct - formula))
            if abs(direct - formula) > 1e-8 * max(1.0, abs(direct)):
                ok = False
    report(f"(3.1) A_jp formula vs direct survivor sum   (X={X}, K={K}, "
           f"|band|={len(band)})", ok, f"max dev={worst:.2e}")

# ------------------------------------------------------------------ E
def check_E(X):
    H, Y = panel_params(X)
    band = [p for p in primes_upto(2 * X) if p > X]
    lam = lambda_table(H)
    V = 0.0
    RHS = 0.0
    for p in band:
        Psi_p = sum(lam[n] for n in range(2, H + 1) if n % p != 0)
        for a in range(1, p):
            psi_a = sum(lam[n] for n in range(2, H + 1) if n % p == a)
            V += (psi_a - Psi_p / (p - 1)) ** 2
        for n in range(2, H + 1):
            if not lam[n] or n % p == 0:
                continue
            for n2 in range(2, H + 1):
                if not lam[n2] or n2 % p == 0:
                    continue
                RHS += lam[n] * lam[n2] * ((1.0 if (n - n2) % p == 0 else 0.0)
                                           - 1.0 / (p - 1))
    ok = abs(V - RHS) < 1e-6 * max(1.0, abs(V))
    report(f"(4.2) centred determinant reordering   (X={X})", ok,
           f"V={V:.6f} RHS={RHS:.6f}")

# ------------------------------------------------------------------ F
def diagnostics(X):
    H, Y = panel_params(X)
    band = [p for p in primes_upto(2 * X) if p > X]
    lam = lambda_table(H)
    V = 0.0
    R = 0.0
    diag = 0.0
    for p in band:
        buckets = np.zeros(p)
        for n in range(2, H + 1):
            if lam[n]:
                buckets[n % p] += lam[n]
        Psi_p = buckets[1:].sum()
        V += float(((buckets[1:] - Psi_p / (p - 1)) ** 2).sum())
        R += float((buckets[1:] ** 2).sum())
        d_p = sum(lam[n] ** 2 for n in range(2, H + 1) if n % p != 0)
        R -= d_p
        diag += d_p
    print(f"   X={X:4d} H={H:6d} |band|={len(band):3d}:  "
          f"V/(HX)={V/(H*X):.3f}   R_uncentred/H^2={R/(H*H):.4f}   "
          f"diag/(HX)={diag/(H*X):.3f}")
    return V, R

# ------------------------------------------------------------------ G
def sdd_falsity(X):
    H, Y = panel_params(X)
    band = [p for p in primes_upto(2 * X) if p > X]
    # D = 1 cell, gamma = Lambda on (M, 2M], M = H//2  (divisor-bounded coefficient)
    M = H // 2
    lam = lambda_table(2 * M)
    g = lam[M + 1 : 2 * M + 1].copy()          # gamma(m), m in (M, 2M]
    E = 0.0
    for p in band:                             # at most one band prime per difference
        for k in range(1, (M - 1) // p + 1):
            E += 2.0 * float(np.dot(g[: M - k * p], g[k * p :]))
    DM = 1 * M
    dens = sum(1.0 / (p - 1) for p in band)
    print(f"   X={X:4d}: D=1, gamma=Lambda cell:  E/(DM)={E/DM:9.2f}   "
          f"E/(dens*(sum gamma)^2)={E/(dens*float(g.sum())**2):.3f}   "
          f"target O(X^o(1))")
    # mid-D Mobius cell: alpha = mu on (D,2D], gamma = Lambda on (M,2M], 4DM ~ H
    D = max(2, int(math.sqrt(H)) // 4)
    M2 = H // (4 * D)
    if M2 > 4:
        lam2 = lambda_table(4 * D * M2 + 1)
        f = np.zeros(4 * D * M2 + 1)
        for d in range(D + 1, 2 * D + 1):
            md = mobius(d)
            if not md:
                continue
            for m in range(M2 + 1, 2 * M2 + 1):
                if lam2[m]:
                    f[d * m] += md * lam2[m]
        E2 = 0.0
        N = len(f) - 1
        for p in band:
            for k in range(1, N // p + 1):
                E2 += 2.0 * float(np.dot(f[: N + 1 - k * p], f[k * p :]))
        # remove pairs with equal products?  f is indexed by the product n = dm,
        # so the Delta = 0 (product-diagonal) terms are excluded by k >= 1 already.
        print(f"   X={X:4d}: mid-D mu cell (D={D}, M={M2}):  E/(DM)={E2/(D*M2):9.2f}")
    return E

# ------------------------------------------------------------------ H
def covariance_diag(X, seed=7):
    H, Y = panel_params(X)
    ps = primes_upto(max(H, 4 * X))
    zs = [q for q in ps if X <= q < 2 * X]
    K = max(2, min(len(zs), math.ceil(math.log(X))))
    zs = zs[:K]
    centres = []
    for z in zs:
        P = 1
        for q in ps:
            if q > z:
                break
            P *= q
        centres.append(P)
    Z = zs[-1]
    band = [q for q in ps if Z < q <= min(2 * Z, H)]
    lam = lambda_table(H)
    rng = np.random.default_rng(seed)
    Dvals = np.zeros((K, len(band)))
    Rvals = np.zeros((K, len(band)))
    for i, p in enumerate(band):
        buckets = np.zeros(p)
        for n in range(2, H + 1):
            if lam[n]:
                buckets[n % p] += lam[n]
        Psi_p = buckets[1:].sum()
        mean = Psi_p / (p - 1)
        for j, P in enumerate(centres):
            Dvals[j, i] = buckets[(-P) % p] - mean
            Rvals[j, i] = buckets[1 + rng.integers(0, p - 1)] - mean
    def stats(A, label):
        row_sq = (A.sum(axis=1)) ** 2            # |sum_p D_p|^2 per centre
        indep = (A ** 2).sum(axis=1)             # sum_p D_p^2 per centre
        cauchy = len(band) * indep               # Cauchy bound
        print(f"   X={X:4d} {label}: mean |sum_p D|^2 / sum_p D^2 = "
              f"{row_sq.mean()/indep.mean():6.2f}   (independence=1, "
              f"Cauchy bound={len(band)});  per-centre ratios "
              f"{np.round(row_sq/indep, 2)}")
    stats(Dvals, "orbit  ")
    stats(Rvals, "random ")

def main():
    print("== A. Reduced-source resummation (exact) ==")
    for X in (11, 17, 23):
        check_A(X)
    print("\n== B. Completion to psi(H;p,a) (exact) ==")
    for X in (11, 17, 23):
        check_B(X)
    print("\n== C. Character collapse (2.5) ==")
    for X in (11, 17, 23):
        check_C(X)
    print("\n== D. First-order coordinate (3.1) ==")
    for X in (11, 17, 23):
        check_D(X)
    print("\n== E. Centred determinant reordering (4.2) ==")
    for X in (11, 17):
        check_E(X)
    print("\n== F. Actual-source diagnostics (EMPIRICAL) ==")
    for X in (101, 149, 199, 251, 307):
        diagnostics(X)
    print("\n== G. Falsity exhibit for the reviewer's uncentred SDD box (RETRACTION) ==")
    for X in (101, 199, 307):
        sdd_falsity(X)
    print("\n== H. Cross-modulus covariance of D_p(-P_j) (EMPIRICAL, new) ==")
    for X in (101, 199, 307):
        covariance_diag(X)
    sys.exit(FAIL)

if __name__ == "__main__":
    main()
