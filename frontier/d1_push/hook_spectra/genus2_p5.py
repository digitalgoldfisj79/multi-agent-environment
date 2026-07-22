#!/usr/bin/env python3
"""
The sgn-twist curve of the p=5 family:
  D_q : w^2 = u_q * G_q(z),  G_q = g_+ g_-  (sextic),
where f_q(z) -+ 1 = const*(z -+ 1)^2 g_{+-}(z) and disc_z P_{q,t} = u_q (t^2-1).
H^1 of D_q should contain the weight-1 part of L_3 = L(H^1_c(U, Std (x) sgn)).

Counts points over F_{5^j}, j=1..4, and produces the genus-2 L-polynomial.
"""
import flint
from fractions import Fraction
import sympy as sp

P = 5
U = {1: -2, 3: -1, 4: -2}   # disc unit mod 5 per q

def residual_cubic(q, tv):
    """g s.t. q z^5+z^3-3z-(q-2)tv = q*(z-tv)^2*g(z) [tv=+-1 critical]."""
    f = flint.nmod_poly([(-(q - 2) * tv) % P, -3 % P, 0, 1, 0, q % P], P)
    lin = flint.nmod_poly([(-tv) % P, 1], P)
    g, r = divmod(f, lin * lin)
    assert not r, (q, tv)
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

def lpoly(q):
    gp = residual_cubic(q, 1)
    gm = residual_cubic(q, -1)
    Gcoeffs = [int((gp * gm)[k]) for k in range(7)]
    u = U[q] % P
    print(f"q={q}: u={u}, g+ = {gp}, g- = {gm}")
    Ns = {}
    for j in range(1, 5):
        ctx = flint.fq_default_ctx(P, j)
        els = enumerate_field(ctx, j)
        uG = [ctx(u * c % P) for c in Gcoeffs]
        # chi_Q(x) = x^((Q-1)/2); test squareness via exponentiation
        e = (P**j - 1) // 2
        one = ctx(1); zero = ctx(0)
        n = 0
        for z in els:
            val = uG[6]
            for k in range(5, -1, -1):
                val = val * z + uG[k]
            if val == zero:
                n += 1
            elif val ** e == one:
                n += 2
        # two points at infinity iff lc = u*q^2... leading coeff of uG:
        lc = uG[6]
        n += 2 if lc ** e == one else 0
        Ns[j] = n
        print(f"  j={j}: N={n}, N-(5^j+1)={n-P**j-1}")
    # Newton: sum lambda^j = 5^j + 1 - N_j; L(T)=prod(1-lambda T), deg 4
    s = {j: P**j + 1 - Ns[j] for j in Ns}
    c = [Fraction(1)] + [Fraction(0)] * 4
    for j in range(1, 5):
        acc = Fraction(s[j])
        for m in range(1, j):
            acc += c[m] * s[j - m]
        c[j] = -acc / j
    T = sp.symbols('T')
    L = sum(int(c[k]) * T**k for k in range(5))
    print(f"  L(D_{q}) = {sp.factor(L)}\n")
    return L

for q in [1, 3, 4]:
    lpoly(q)
