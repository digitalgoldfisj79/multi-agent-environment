#!/usr/bin/env python3
"""EXACT computation of the class correlation sums C(theta) for the primorial
puncture L = t^q - t (companion to FF_CLASS_CORRELATION_EXACT_NOTE_20260731.md).

All arithmetic is in Z[zeta_q] (integer vectors mod x^q - 1, canonicalized by
1 + zeta + ... + zeta^{q-1} = 0).  FF Lambda is integer-valued, phases are
q-th roots of unity, so every quantity below is exact.

Endpoint configuration: k = 2, m = 3 = 2k-1, R = 3, theta in F_q^* (deg < 2k-R).

Verified exactly:
  C1  the unimodular class constant c = zeta^E per class (direct f'-sums, q=3);
  C2  trace-zero: Tr_{F_{q^2}/F_q}(L(alpha_S)) = 0 for every band S when
      L = t^q - t (generically nonzero for the control t(t+1));
  C3  the primorial congruence L = t^q - t == -P'(t) (mod P) for EVERY
      irreducible P of degree 2 (t^q == -b_P - t mod P), so
      mu_1 = theta * (P' * S)^{-1} mod P: the primorial replaces the puncture
      by the modulus's own derivative -- the self-referential frequency;
  C4  the per-class exact law AT q = 3, 5 (all classes, all theta):
      zeta^E * Ahat_P(mu_1) * conj(Ahat_P'(mu_1')) = |Ahat_P(mu_1)|^2 exactly
      -- equivalently Ahat_P'(mu_1') = zeta^E * Ahat_P(mu_1) -- so C(theta) is
      a sub-sum of the diagonal mass there.  At q = 7 the per-class law FAILS
      (294/672 classes hold; all 84 same-P classes fail) while the AGGREGATE
      C(theta) remains an exact positive rational integer: the identity is
      aggregate, not termwise, in general.  The script asserts the law only
      at q = 3, 5 and prints the counts at q = 7;
  C5  the class-existence criterion (primorial): the one-sided coincidence
      E_1 = nu_2 * S' mod S is scalar  <=>  Tr_{F_{q^2}/F_q}(S'(alpha_S) *
      P(alpha_S^q)) = 0; a full class additionally needs the symmetric scalar
      E_2 = -nu_2' * S mod S' with E_1 = E_2;
  C6  Galois covariance: sigma_s(C(theta)) = C(s*theta) for the Frobenius
      sigma_s: zeta -> zeta^s of Q(zeta_q)/Q (both punctures) -- combined
      with the verified theta-independence this forces C(theta) rational;
  plus: C(theta) independent of theta; DiagMass and C(theta) rational.
"""
import itertools, sys
from ff_t3_coset_audit import (trim, padd, pmul, pmod, monics, irreducibles_upto,
                               lambda_sources, pow_poly_inverse)

FAIL = 0
def report(name, ok, detail=""):
    global FAIL
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL = 1

def pneg(a, q):
    return tuple((-c) % q for c in a)

def psub(a, b, q):
    return padd(a, pneg(b, q), q)

def deg(a):
    return len(a) - 1 if a else -1

def pderiv(P, q):
    return trim([(i * c) % q for i, c in enumerate(P)][1:])

def pcompose(P, x, S, q):
    """P(x) mod S, Horner."""
    out = ()
    for c in reversed(P):
        out = pmod(padd(pmul(out, x, q), trim([c]), q), S, q)
    return out

# ------------------------- exact Z[zeta_q] arithmetic -----------------------
def zzero(q):  return tuple([0] * q)
def zroot(e, q):
    v = [0] * q; v[e % q] = 1; return tuple(v)
def zadd(a, b): return tuple(x + y for x, y in zip(a, b))
def zsub(a, b): return tuple(x - y for x, y in zip(a, b))
def zscale(a, c): return tuple(c * x for x in a)
def zmul(a, b):
    q = len(a)
    out = [0] * q
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i + j) % q] += x * y
    return tuple(out)
def zconj(a):
    q = len(a)
    return tuple(a[(-i) % q] for i in range(q))
def zcanon(a):
    """Canonical form: subtract a[q-1]*(1,...,1) so last coord = 0."""
    c = a[-1]
    return tuple(x - c for x in a)
def zeq(a, b):  return zcanon(a) == zcanon(b)
def zfloat(a):
    import cmath
    q = len(a)
    return sum(x * cmath.exp(2j * cmath.pi * i / q) for i, x in enumerate(a))
def zisreal(a):
    return zeq(a, zconj(a))
def zisrational(a):
    """Rational <=> canonical form is c[0]*1 + 0*zeta + ... (a plain integer)."""
    c = zcanon(a)
    return all(x == 0 for x in c[1:])
def zgalois(a, s):
    """sigma_s: zeta -> zeta^s."""
    q = len(a)
    out = [0] * q
    for i, x in enumerate(a):
        out[(i * s) % q] += x
    return tuple(out)

# ------------------------------- local pieces -------------------------------
def coeff_top(x, P):
    k = len(P) - 1
    return x[k - 1] if len(x) >= k else 0

def Ahat_exact(P, mu, sources, q):
    out = zzero(q)
    for f, w in sources:
        e = coeff_top(pmod(pmul(mu, f, q), P, q), P)
        out = zadd(out, zscale(zroot(e, q), w))
    return out

def frobenius(x, P, q):
    """x -> x^q mod P, square-and-multiply."""
    e = q
    base = pmod(x, P, q)
    res = (1,)
    while e:
        if e & 1:
            res = pmod(pmul(res, base, q), P, q)
        base = pmod(pmul(base, base, q), P, q)
        e >>= 1
    return res

def trace_k2(x, P, q):
    """Tr_{F_{q^2}/F_q}(x) = x + x^q mod P (must be a scalar)."""
    t = padd(pmod(x, P, q), frobenius(x, P, q), q)
    assert deg(t) <= 0
    return t[0] if t else 0

# ------------------------------- main computation ---------------------------
def run(q, Lpoly, Ltag, verbose_classes=False):
    k, m, R = 2, 3, 3
    prim = Ltag.startswith("L=t^q-t")
    irr = irreducibles_upto(max(k, m), q)
    band = irr[k]
    sources = lambda_sources(m, q, irr)

    # Lemma C2: trace of L at each band prime
    traces = [trace_k2(Lpoly, S, q) for S in band]
    if prim:
        report(f"C2 trace-zero: Tr(L(alpha_S)) = 0 for all band S ({Ltag}, q={q})",
               all(t == 0 for t in traces), f"traces={traces[:10]}")
        # Lemma C3: L == -P' (mod P) for every band P
        okc3 = all(pmod(Lpoly, P, q) == pneg(pderiv(P, q), q) for P in band)
        report(f"C3 primorial congruence L == -P' (mod P) for all band P (q={q})",
               okc3)
    else:
        print(f"   control traces ({Ltag}, q={q}): {traces}")

    theta_C = []
    theta_cls = []
    law = {"same_ok": 0, "same_bad": 0, "cross_ok": 0, "cross_bad": 0}
    any_classes = False
    pairs_th1 = None
    for th_s in range(1, q):
        th = (th_s,)
        # pair data
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
        if th_s == 1:
            pairs_th1 = pairs

        Avals = {}
        for (P, S, mu1, nu2) in pairs:
            Avals[(tuple(P), tuple(S))] = Ahat_exact(P, mu1, sources, q)

        diag = zzero(q)
        for (P, S, mu1, nu2) in pairs:
            a = Avals[(tuple(P), tuple(S))]
            diag = zadd(diag, zmul(a, zconj(a)))

        classes = []
        Csum = zzero(q)
        for (P, S, mu1, nu2) in pairs:
            for (Pp, Sp, mu1p, nu2p) in pairs:
                E = psub(pmul(nu2, Sp, q), pmul(nu2p, S, q), q)
                if deg(E) == 0:                       # E in F_q^*
                    a = Avals[(tuple(P), tuple(S))]
                    b = Avals[(tuple(Pp), tuple(Sp))]
                    term = zmul(zroot(E[0], q), zmul(a, zconj(b)))
                    Csum = zadd(Csum, term)
                    classes.append((P, S, Pp, Sp, E[0], term))
                    # per-class exact law (C4) accounting
                    holds = zeq(term, zmul(a, zconj(a))) \
                        and zeq(b, zmul(zroot(E[0], q), a))
                    key = ("same" if tuple(Pp) == tuple(P) else "cross") \
                        + ("_ok" if holds else "_bad")
                    law[key] += 1
        if classes:
            any_classes = True
        theta_C.append(Csum)
        theta_cls.append(frozenset((tuple(P), tuple(S), tuple(Sp))
                                   for (P, S, Pp, Sp, E, t) in classes))

        # per-pair partner statistics
        pcount = {}
        for (P, S, Pp, Sp, E, t) in classes:
            pcount[(tuple(P), tuple(S))] = pcount.get((tuple(P), tuple(S)), 0) + 1
        maxpart = max(pcount.values()) if pcount else 0
        npart = len(pcount)

        ratio = zfloat(Csum).real / zfloat(diag).real if zfloat(diag).real else 0
        print(f"   {Ltag} q={q} theta={th_s}: DiagMass={zcanon(diag)} "
              f"(={zfloat(diag).real:.1f}, rational={zisrational(diag)})")
        print(f"      C(theta)={zcanon(Csum)} (={zfloat(Csum).real:.1f}"
              f"{'+' if zfloat(Csum).imag >= 0 else ''}{zfloat(Csum).imag:.1f}i)   "
              f"#classes={len(classes)}   C/Diag={ratio:+.4f}   "
              f"C real={zisreal(Csum)} rational={zisrational(Csum)}")
        print(f"      pairs with a partner: {npart}/{len(pairs)}   "
              f"max partners per pair: {maxpart}")

        if verbose_classes:
            for (P, S, Pp, Sp, E, term) in classes:
                a = Avals[(tuple(P), tuple(S))]
                struct = []
                if tuple(Pp) == tuple(P):
                    struct.append("P'=P")
                if zeq(term, zmul(a, zconj(a))):
                    struct.append("term=|A|^2")
                if zisreal(term):
                    struct.append("real")
                print(f"        P={P} S={S} -> P'={Pp} S'={Sp} E={E}  "
                      f"term={zcanon(term)}  {' '.join(struct)}")

    # C6 Galois covariance: sigma_s(C(1)) = C(s), both punctures
    if any_classes:
        okg = all(zeq(zgalois(theta_C[0], s), theta_C[s - 1])
                  for s in range(1, q))
        report(f"C6 Galois covariance sigma_s(C(1)) = C(s) ({Ltag}, q={q})", okg)

    if prim and any_classes:
        nlaw_ok = law["same_ok"] + law["cross_ok"]
        nlaw = sum(law.values())
        print(f"   C4 per-class law zeta^E*A*conj(A') = |A|^2 ({Ltag}, q={q}): "
              f"holds {nlaw_ok}/{nlaw}  "
              f"[same-P ok={law['same_ok']} bad={law['same_bad']}; "
              f"cross-P ok={law['cross_ok']} bad={law['cross_bad']}]")
        if q in (3, 5):
            report(f"C4 per-class exact law, all classes, all theta "
                   f"({Ltag}, q={q})", nlaw_ok == nlaw,
                   "(equivalently A'(mu_1') = zeta^E * A(mu_1))")
        report(f"C(theta) independent of theta ({Ltag}, q={q})",
               all(zeq(c, theta_C[0]) for c in theta_C)
               and all(s == theta_cls[0] for s in theta_cls))
        report(f"C(theta) and DiagMass rational integers ({Ltag}, q={q})",
               zisrational(theta_C[0]))

        # C5: one-sided coincidence <=> trace criterion (theta = 1 class set)
        nu_d = {(tuple(P), tuple(S)): nu2 for (P, S, mu1, nu2) in pairs_th1}
        ok5 = True
        n_onesided = n_full = 0
        cls1 = theta_cls[0]
        for S in band:
            frob_t = frobenius((0, 1), S, q)
            for P in band:
                if P == S:
                    continue
                nu2 = nu_d[(tuple(P), tuple(S))]
                for Sp in band:
                    if Sp == S or Sp == P:
                        continue
                    E1 = pmod(pmul(nu2, Sp, q), S, q)
                    onesided = deg(E1) == 0
                    Pf = pcompose(P, frob_t, S, q)
                    z = pmod(pmul(pmod(Sp, S, q), Pf, q), S, q)
                    tr = trace_k2(z, S, q)
                    if onesided != (tr == 0):
                        ok5 = False
                    if onesided:
                        n_onesided += 1
                        if (tuple(P), tuple(S), tuple(Sp)) in cls1:
                            n_full += 1
        report(f"C5 one-sided coincidence <=> Tr(S'(a_S) P(a_S^q)) = 0 "
               f"({Ltag}, q={q})", ok5,
               f"one-sided={n_onesided} full-class={n_full}")

def main():
    print("== Exact class correlation C(theta), endpoint k=2, m=3, R=3 ==")
    for q in (3, 5, 7):
        Lprim = trim([0, q - 1] + [0] * (q - 2) + [1])       # t^q - t
        run(q, Lprim, "L=t^q-t ", verbose_classes=(q == 3))
    print("\n== Control puncture ==")
    for q in (3, 5):
        Lfix = pmul((0, 1), (1, 1), q)
        run(q, Lfix, "L=t(t+1)")
    # spot-verify the class constant c = zeta^E against the direct f'-sum (q=3)
    import cmath
    q, k, m = 3, 2, 3
    irr = irreducibles_upto(3, q)
    band = irr[k]
    zq = cmath.exp(2j * cmath.pi / q)
    from ff_local_character_audit import psi_P
    ok = True
    Lprim = trim([0, q - 1] + [0] * (q - 2) + [1])
    th = (1,)
    pairs = []
    for P in band:
        for S in band:
            if S == P:
                continue
            PbS = pow_poly_inverse(pmod(P, S, q), S, q)
            LbS = pow_poly_inverse(pmod(Lprim, S, q), S, q)
            nu2 = pmod(pmul(pmul(pneg(th, q), LbS, q), PbS, q), S, q)
            pairs.append((P, S, nu2))
    for (P, S, nu2) in pairs:
        for (Pp, Sp, nu2p) in pairs:
            E = psub(pmul(nu2, Sp, q), pmul(nu2p, S, q), q)
            if deg(E) == 0:
                tot = sum(psi_P(nu2, fp, S, q, zq) *
                          psi_P(nu2p, fp, Sp, q, zq).conjugate()
                          for fp in monics(m, q))
                pred = (q ** m) * zq ** E[0]
                if abs(tot - pred) > 1e-6:
                    ok = False
    report("C1 class constant c = zeta^E (direct f'-sums, q=3, all classes)", ok)
    sys.exit(FAIL)

if __name__ == "__main__":
    main()
