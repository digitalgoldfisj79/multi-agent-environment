#!/usr/bin/env python3
"""
p=5, generic q in F_25 \ F_5: compute L(D_q) (genus-2 twist curve) and the
weight-1 factor of the pair curve B_q over the base field F_25, and check
whether they share factors (the q=1 accidental cancellation) generically.

D_q: w^2 = u_q g_+ g_-,  u_q = 3 q (q-2)^2,  g_+- residual cubics over F_25.
B_q: q h4(z1,z2) + h2 - 3 = 0; weight-1 part from N_j(B) = 25^j + c - tr_j.

Genus-2 L via j=1,2 + functional equation; validated j=3.
Pair-curve rank-2 part via N_1, N_2 (c = +-1 pattern checked on j=3).
"""
import flint
from fractions import Fraction
import sympy as sp

P5 = 5
T = sp.symbols('T')

def enumerate_field(ctx, deg_over_base, base_gen_pow):
    # enumerate F_{5^(2*j)} via absolute degree
    els = [ctx(c) for c in range(P5)]
    g = ctx.gen()
    pw = ctx(1)
    for k in range(1, deg_over_base):
        pw = pw * g
        base = [ctx(c) * pw for c in range(P5)]
        els = [e + b for e in els for b in base]
    return els

def residual_cubic_fq(q_el, tv, pctx, ctx):
    # f = q z^5 + z^3 - 3 z - (q-2) tv ; divide by (z - tv)^2
    f = pctx([-(q_el - ctx(2)) * ctx(tv), ctx(-3), ctx(0), ctx(1), ctx(0), q_el])
    lin = pctx([ctx(-tv), ctx(1)])
    g, r = divmod(f, lin * lin)
    assert not r
    return g

def run(q_index):
    """q = generator^q_index in F_25."""
    results = {}
    Ns_D, Ns_B = {}, {}
    for j in (1, 2, 3):
        deg = 2 * j
        ctx = flint.fq_default_ctx(P5, deg)
        pctx = flint.fq_default_poly_ctx(ctx)
        els = enumerate_field(ctx, deg, None)
        # embed q: need a consistent q across j. Use q = w^q_index where w is a
        # fixed root of the F_25 defining poly x^2+4x+2 embedded in F_{5^deg}.
        # Find a root of x^2+4x+2 in ctx:
        defpoly = pctx([ctx(2), ctx(4), ctx(1)])
        rts = sorted([r for r, m in defpoly.roots()], key=str)
        w = rts[0]
        q_el = w ** q_index
        e = (P5**deg - 1) // 2
        one = ctx(1); zero = ctx(0)
        # ---- D_q ----
        gp = residual_cubic_fq(q_el, 1, pctx, ctx)
        gm = residual_cubic_fq(q_el, -1, pctx, ctx)
        G = gp * gm
        u = ctx(3) * q_el * (q_el - ctx(2))**2
        n = 0
        for z in els:
            val = G(z) * u
            if val == zero: n += 1
            elif val ** e == one: n += 2
        lc = u * G[6]
        n += 2 if lc ** e == one else 0
        Ns_D[j] = n
        # ---- B_q ---- roots in z2 of quartic divided difference
        nB = 0
        for z1 in els:
            z2_ = z1 * z1; z3_ = z2_ * z1; z4_ = z2_ * z2_
            f = pctx([q_el * z4_ + z2_ - ctx(3),
                      q_el * z3_ + z1,
                      q_el * z2_ + ctx(1),
                      q_el * z1,
                      q_el])
            nB += len(f.roots())
        Ns_B[j] = nB
    Q0 = 25
    # genus-2 L over F_25 from j=1,2 + functional equation
    s = {j: Q0**j + 1 - Ns_D[j] for j in Ns_D}
    c = [Fraction(1), 0, 0, 0, 0]
    c[1] = -Fraction(s[1])
    c[2] = -(Fraction(s[2]) + c[1] * s[1]) / 2
    c[3] = Fraction(Q0) * c[1]
    c[4] = Fraction(Q0**2)
    s3 = -(3 * c[3] + c[1] * s[2] + c[2] * s[1])
    okD = (s3 == s[3])
    LD = sum(int(c[k]) * T**k for k in range(5))
    # pair curve weight-1 part: N_B = Q^j + c0^j - tr_j hypothesis, c0 = +-1
    sols = []
    for c0 in (1, -1):
        tr1 = Q0 + c0 - Ns_B[1]
        tr2 = Q0**2 + c0**2 - Ns_B[2]
        aa = tr1
        prod = (tr1 * tr1 - tr2) // 2 if (tr1 * tr1 - tr2) % 2 == 0 else None
        if prod is None: continue
        # weight check: prod should be Q0 for a rank-2 weight-1 piece
        if prod != Q0: continue
        tr3 = aa * tr2 - prod * tr1
        if Q0**3 + c0**3 - tr3 == Ns_B[3]:
            sols.append((c0, aa))
    return LD, okD, sols, Ns_D, Ns_B

for qi in [1, 3, 5, 7, 9]:   # w^qi, odd powers not in F_5 (w has order 24)
    LD, okD, sols, NsD, NsB = run(qi)
    print(f"q = w^{qi} (F_25):")
    print(f"   L(D_q)/F_25 = {sp.factor(LD)}   [j=3 check: {okD}]")
    for c0, aa in sols:
        print(f"   B_q weight-1: 1 - ({aa})T + 25T^2, w0 constant {c0:+d}  [j=3 check passed]")
    if not sols:
        print(f"   B_q: no rank-2 weight-1 fit (N_B = {NsB})")
