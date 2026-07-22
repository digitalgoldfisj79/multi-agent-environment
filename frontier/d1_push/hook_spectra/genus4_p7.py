#!/usr/bin/env python3
"""
p=7 sgn-twist curves D_q : w^2 = u_q * g_+(z) g_-(z)  (deg 10, genus 4),
where q z^7 + z^3 - 3z -+ (q-2) = q (z -+ 1)^2 g_{+-}(z), u_q = disc unit.
Weight-1 part of L_5 = L(H^1_c(U, Std (x) sgn)) should be L(D_q) (dim 8).

Genus-4 L-poly from j=1..4 counts + functional equation; j=5 validates.
"""
import flint
from fractions import Fraction
import sympy as sp

P = 7
U = {1: 4, 3: 3, 4: 2, 5: 6, 6: 6}   # disc_z = u (t^2-1) mod 7  (computed earlier)

def residual_quintic(q, tv):
    f = flint.nmod_poly([(-(q - 2) * tv) % P, -3 % P, 0, 1, 0, 0, 0, q % P], P)
    lin = flint.nmod_poly([(-tv) % P, 1], P)
    g, r = divmod(f, lin * lin)
    assert not r
    return g

def enumerate_field(ctx, deg):
    g = ctx.gen()
    els = [ctx(c) for c in range(P)]
    pw = ctx(1)
    for k in range(1, deg):
        pw = pw * g
        base = [ctx(c) * pw for c in range(P)]
        els = [e + b for e in els for b in base]
    return els

T = sp.symbols('T')
for q in [1, 3, 4, 5, 6]:
    gp = residual_quintic(q, 1)
    gm = residual_quintic(q, -1)
    G = gp * gm
    Gc = [int(G[k]) for k in range(11)]
    u = U[q]
    Ns = {}
    for j in range(1, 6):
        ctx = flint.fq_default_ctx(P, j)
        els = enumerate_field(ctx, j)
        uG = [ctx(u * c % P) for c in Gc]
        e = (P**j - 1) // 2
        one = ctx(1); zero = ctx(0)
        n = 0
        for z in els:
            val = uG[10]
            for k in range(9, -1, -1):
                val = val * z + uG[k]
            if val == zero:
                n += 1
            elif val ** e == one:
                n += 2
        n += 2 if uG[10] ** e == one else 0   # deg 10 even: 2 pts at infinity iff lc square
        Ns[j] = n
    s = {j: P**j + 1 - Ns[j] for j in Ns}
    # Newton for c1..c4, then functional equation c_{8-k} = 7^{4-k} c_k
    c = [Fraction(1)] + [Fraction(0)] * 8
    for j in range(1, 5):
        acc = Fraction(s[j])
        for m in range(1, j):
            acc += c[m] * s[j - m]
        c[j] = -acc / j
    for k in range(0, 4):
        c[8 - k] = Fraction(P**(4 - k)) * c[k]
    assert all(x.denominator == 1 for x in c)
    # validate with j=5: s5 = -(5 c5 + sum_{m=1}^{4} c_m s_{5-m})
    s5 = -(5 * c[5] + sum(c[m] * s[5 - m] for m in range(1, 5)))
    ok = (s5 == s[5])
    L = sum(int(c[k]) * T**k for k in range(9))
    print(f"q={q}: N_j={ [Ns[j] for j in sorted(Ns)] }")
    print(f"   L(D_{q}) = {sp.factor(L)}   [j=5 validation: {ok}]")
