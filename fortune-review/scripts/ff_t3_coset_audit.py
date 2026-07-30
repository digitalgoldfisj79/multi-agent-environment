#!/usr/bin/env python3
"""Function-field T3/PORC audit: exact structure theorems + empirical bounds
for the punctured coset centre family (companion to FF_T3_COSET_NOTE_20260730.md).

Setting: F_q[t], band = monic irreducibles P of degree k, sources = monic prime
powers f of degree m (Lambda_FF(f) = deg P if f = P^e, an INTEGER - exact
arithmetic throughout), centres = L*M with L a fixed "puncture" (product of
low-degree irreducibles) and M ranging over ALL monic polys of degree R
(k <= R <= 2k-1: the family is sparse mod PS, covering q^{R-2k} < 1 of the
residue pairs).

Checks:
  A. Within-modulus fairness IDENTITY (exact, Fractions):
     sum_M D_P(-LM)^2 = q^{R-k} * sum_{all residues a} D_P(a)^2.
  B. Same-modulus character orthogonality over the M-family (R >= k):
     sum_{deg M = R} (chibar_i chi_j)(M) = 0 exactly for i != j
     (the [u^R] coefficient of a degree <= k-1 L-polynomial).
  C. Coset cross/diagonal ratio across growing q at fixed (k, R, m):
     CROSS = sum_M sum_{P != S} D_P D_S vs DIAG = sum_M sum_P D_P^2,
     for both a fixed puncture L = t(t+1) and the true degree-1 FF primorial
     L = t^q - t (the q-coupled case).
  D. Subspace-completion identity (exact): the indicator that a residue class
     c mod PS contains a monic of degree R equals
     q^{R-2k} sum_{theta in V^perp} psi_theta(c - t^R),
     V = {deg < R}: the FF interval is an F_q-subspace, so completion is EXACT.
  E. theta != 0 saving: |sum_{P != S} psi_theta(c(P,S) - t^R)| / #pairs
     for the CRT points c of a fixed source pair - the object the conditional
     power-saving bound controls.
"""
import cmath, itertools, math, sys
from fractions import Fraction

FAIL = 0
def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

# ---------------- F_q[t] arithmetic: polys = tuples, little-endian, trimmed --
def trim(a):
    i = len(a)
    while i > 0 and a[i-1] == 0:
        i -= 1
    return tuple(a[:i])

def padd(a, b, q):
    n = max(len(a), len(b))
    return trim([( (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % q
                 for i in range(n)])

def pmul(a, b, q):
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % q
    return trim(out)

def pmod(a, b, q):
    a = list(a)
    db, lb = len(b) - 1, b[-1]
    inv = pow(lb, q - 2, q)
    while len(trim(a)) - 1 >= db and trim(a):
        a = list(trim(a))
        if len(a) - 1 < db:
            break
        c = (a[-1] * inv) % q
        shift = len(a) - 1 - db
        for i, y in enumerate(b):
            a[shift + i] = (a[shift + i] - c * y) % q
        a = list(trim(a))
    return trim(a)

def monics(deg, q):
    for lo in itertools.product(range(q), repeat=deg):
        yield trim(list(lo) + [1]) if deg > 0 else (1,)

def irreducibles_upto(dmax, q):
    irr = {d: [] for d in range(1, dmax + 1)}
    for d in range(1, dmax + 1):
        for f in monics(d, q):
            reducible = False
            for e in range(1, d // 2 + 1):
                for P in irr[e]:
                    if not pmod(f, P, q):
                        reducible = True
                        break
                if reducible:
                    break
            if not reducible:
                irr[d].append(f)
    return irr

def lambda_sources(m, q, irr):
    """[(f, Lambda(f))] for monic f of degree m; Lambda integer-valued."""
    out = []
    for d in range(1, m + 1):
        if m % d == 0:
            e = m // d
            for P in irr[d]:
                f = (1,)
                for _ in range(e):
                    f = pmul(f, P, q)
                out.append((f, d))
    return out

# ---------------------------------------------------------------- residues
def residue_index(f, P, q):
    """Index of f mod P in [0, q^k): coefficient base-q encoding."""
    r = pmod(f, P, q)
    idx = 0
    for i in range(len(P) - 1):
        idx += (r[i] if i < len(r) else 0) * q ** i
    return idx

def D_table(P, sources, q):
    """D_P(a) for every residue index a (Fractions), plus Psi_P."""
    k = len(P) - 1
    Qk = q ** k
    psi = [0] * Qk
    for f, lam in sources:
        psi[residue_index(f, P, q)] += lam
    # residue index 0 <=> f = 0 mod P: non-unit class
    Psi_units = sum(psi) - psi[0]
    mean = Fraction(Psi_units, Qk - 1)
    return [Fraction(v) - mean for v in psi], psi

# ------------------------------------------------------------------ checks
def check_A(q, k, R, m, Lpoly, tag):
    irr = irreducibles_upto(max(k, m), q)
    sources = lambda_sources(m, q, irr)
    band = irr[k]
    ok = True
    for P in band[:3]:
        D, _ = D_table(P, sources, q)
        lhs = Fraction(0)
        Lm = pmod(Lpoly, P, q)
        for M in monics(R, q):
            LM = pmul(Lm, pmod(M, P, q), q)
            a = residue_index(tuple((-c) % q for c in LM) if LM else (), P, q) if LM else 0
            lhs += D[a] ** 2
        rhs = Fraction(q ** (R - k)) * sum(d * d for d in D)
        if lhs != rhs:
            ok = False
            break
    report(f"A fairness identity sum_M D_P(-LM)^2 = q^(R-k) sum_a D_P(a)^2 "
           f"({tag}, q={q}, k={k}, R={R}, m={m})", ok)

def char_table(P, q):
    """Multiplicative character values on units mod P via discrete log."""
    k = len(P) - 1
    Qk = q ** k
    # find a generator of (F_q[t]/P)^*
    def idx_to_poly(a):
        return trim([ (a // q**i) % q for i in range(k)])
    def polpow_ord(g):
        seen = 1
        x = g
        order = 1
        while True:
            xi = residue_index(x, P, q)
            if xi == 1:  # x == 1
                return order
            x = pmod(pmul(x, g, q), P, q)
            order += 1
            if order > Qk:
                return -1
    for a in range(2, Qk):
        g = idx_to_poly(a)
        if not g:
            continue
        if polpow_ord(g) == Qk - 1:
            break
    dlog = {}
    x = (1,)
    for tpow in range(Qk - 1):
        dlog[residue_index(x, P, q)] = tpow
        x = pmod(pmul(x, g, q), P, q)
    return dlog

def check_B(q, k, R):
    irr = irreducibles_upto(k, q)
    P = irr[k][0]
    Qk = q ** k
    dlog = char_table(P, q)
    # characters chi_j(x) = exp(2 pi i j dlog(x)/(Qk-1)); test a few pairs j1 != j2
    ok = True
    for (j1, j2) in [(1, 2), (1, Qk - 3), (5 % (Qk-1), 7 % (Qk-1))]:
        if j1 == j2:
            continue
        tot = 0j
        for M in monics(R, q):
            r = residue_index(M, P, q)
            if r == 0:
                continue
            tot += cmath.exp(2j * cmath.pi * ((j2 - j1) * dlog[r]) / (Qk - 1))
        if abs(tot) > 1e-7 * q ** R:
            ok = False
    report(f"B same-modulus character orthogonality over deg-R monics "
           f"(q={q}, k={k}, R={R})", ok)

def check_C(q, k, R, m, Lpoly, tag):
    irr = irreducibles_upto(max(k, m), q)
    sources = lambda_sources(m, q, irr)
    band = irr[k]
    Dt = {}
    Lmod = {}
    for P in band:
        Dt[P], _ = D_table(P, sources, q)
        Lmod[P] = pmod(Lpoly, P, q)
    diag = Fraction(0)
    cross = Fraction(0)
    for M in monics(R, q):
        vals = []
        for P in band:
            LM = pmul(Lmod[P], pmod(M, P, q), q)
            neg = tuple((-c) % q for c in LM)
            a = residue_index(neg, P, q) if neg else 0
            vals.append(Dt[P][a])
        srow = sum(vals)
        sq = sum(v * v for v in vals)
        diag += sq
        cross += srow * srow - sq
    print(f"   C {tag}: q={q:3d} k={k} R={R} m={m} |band|={len(band):3d}: "
          f"cross/diag = {float(cross/diag) if diag else float('nan'):+8.4f}   "
          f"diag/q^(R+m) = {float(diag) / q**(R+m):8.4f}")

# --------- D/E: subspace completion mod W = PS, additive characters ----------
def check_DE(q, k, R, m):
    irr = irreducibles_upto(max(k, m), q)
    band = irr[k]
    sources = lambda_sources(m, q, irr)
    P, S = band[0], band[1]
    W = pmul(P, S, q)
    dW = len(W) - 1                      # = 2k
    zq = cmath.exp(2j * cmath.pi / q)
    def pairing(theta, x):
        """psi_theta(x) = zq^( coeff_{dW-1}(theta*x mod W) )"""
        prod = pmod(pmul(theta, x, q), W, q)
        c = prod[dW - 1] if len(prod) >= dW else 0
        return zq ** c
    # V = {deg < R} as span of t^0..t^{R-1}; V^perp = {theta: coeff_{dW-1}(theta t^i mod W)=0, i<R}
    Vperp = []
    for theta in itertools.product(range(q), repeat=dW):
        th = trim(theta)
        okp = True
        for i in range(R):
            ti = tuple([0]*i + [1])
            prod = pmod(pmul(th, ti, q), W, q) if th else ()
            c = prod[dW - 1] if len(prod) >= dW else 0
            if c:
                okp = False
                break
        if okp:
            Vperp.append(th)
    exp_size = q ** (dW - R)
    report(f"D dim(V^perp) = 2k - R  (q={q}, k={k}, R={R})", len(Vperp) == exp_size,
           f"|Vperp|={len(Vperp)} expected {exp_size}")
    # completion identity on sample residues c
    tR = tuple([0]*R + [1])
    ok = True
    count = 0
    for c in itertools.islice(itertools.product(range(q), repeat=dW), 0, None, max(1, q**dW // 60)):
        cpoly = trim(c)
        x = padd(cpoly, tuple((-v) % q for v in tR), q)
        four = sum(pairing(th, x) for th in Vperp) * (q ** (R - dW))
        direct = 1.0 if (cpoly and len(cpoly) - 1 == R and cpoly[-1] == 1) else 0.0
        if abs(four.real - direct) > 1e-8 or abs(four.imag) > 1e-8:
            ok = False
            break
        count += 1
    report(f"D subspace completion identity ({count} samples)", ok)
    # E: theta != 0 sums over prime pairs at CRT points of one source pair
    f = sources[0][0]
    fp = sources[1][0]
    # need L for CRT points: use L = t(t+1)
    L = pmul((0,1), (1,1), q)
    pairs = [(Pa, Sb) for Pa in band for Sb in band if Pa != Sb]
    print(f"   E theta!=0 normalized pair sums (q={q}, k={k}, R={R}): ", end="")
    vals = []
    for th in Vperp:
        if not th:
            continue
        tot = 0j
        for (Pa, Sb) in pairs:
            # c = -f * L^{-1} mod Pa, -f' * L^{-1} mod Sb, via CRT
            def res_neg(g, Q):
                Linv = pow_poly_inverse(pmod(L, Q, q), Q, q)
                r = pmod(pmul(pmod(g, Q, q), Linv, q), Q, q)
                return tuple((-v) % q for v in r)
            rp = res_neg(f, Pa)
            rs = res_neg(fp, Sb)
            # CRT
            c = crt(rp, Pa, rs, Sb, q)
            x = padd(c, tuple((-v) % q for v in tuple([0]*R + [1])), q)
            tot += pairing_gen(th, x, pmul(Pa, Sb, q), q, zq)
        vals.append(abs(tot) / len(pairs))
    print(f"max={max(vals):.4f} mean={sum(vals)/len(vals):.4f} "
          f"(q^(-k/2)={q**(-k/2):.4f})")

def pow_poly_inverse(a, Q, q):
    """a^{-1} mod Q via a^(q^k - 2)."""
    k = len(Q) - 1
    e = q ** k - 2
    result = (1,)
    base = pmod(a, Q, q)
    while e:
        if e & 1:
            result = pmod(pmul(result, base, q), Q, q)
        base = pmod(pmul(base, base, q), Q, q)
        e >>= 1
    return result

def crt(rp, P, rs, S, q):
    """x with x = rp mod P, x = rs mod S."""
    Sinv = pow_poly_inverse(pmod(S, P, q), P, q)
    t = pmod(pmul(padd(rp, tuple((-v) % q for v in rs), q), Sinv, q), P, q)
    return padd(rs, pmul(S, t, q), q)

def pairing_gen(theta, x, W, q, zq):
    dW = len(W) - 1
    prod = pmod(pmul(theta, x, q), W, q)
    c = prod[dW - 1] if len(prod) >= dW else 0
    return zq ** c

def main():
    print("== A. Within-modulus fairness identity (EXACT, Fractions) ==")
    for q in (3, 5, 7):
        Lfix = pmul((0, 1), (1, 1), q)          # t(t+1)
        check_A(q, 2, 3, 3, Lfix, "L=t(t+1)")
    # true degree-1 primorial L = t^q - t
    for q in (3, 5):
        Lprim = trim([0] * 1 + [q - 1] + [0] * (q - 2) + [1])   # t^q - t
        check_A(q, 2, 3, 3, Lprim, "L=t^q-t")

    print("\n== B. Same-modulus character orthogonality over the M-family ==")
    for q in (3, 5, 7):
        check_B(q, 2, 3)

    print("\n== C. Coset cross/diag across q (EMPIRICAL; k=2, R=3, m=3) ==")
    for q in (3, 5, 7, 11, 13):
        Lfix = pmul((0, 1), (1, 1), q)
        check_C(q, 2, 3, 3, Lfix, "L=t(t+1) ")
    for q in (3, 5, 7, 11, 13):
        Lprim = trim([0] * 1 + [q - 1] + [0] * (q - 2) + [1])
        check_C(q, 2, 3, 3, Lprim, "L=t^q-t  ")

    print("\n== D/E. Subspace completion (EXACT) and theta!=0 pair sums ==")
    for q in (3, 5):
        check_DE(q, 2, 3, 3)

    sys.exit(FAIL)

if __name__ == "__main__":
    main()
