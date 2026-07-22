#!/usr/bin/env python3
"""
Pair curve of the p=5 family: B_q = {(z1,z2) : (P_q(z1)-P_q(z2))/(z1-z2) = 0}
with P_q(z) = q z^5 + z^3 - 3z  (the t-independent part; equal t-values).

Affine equation: q*h4(z1,z2) + h2(z1,z2) - 3 = 0,
  h4 = z1^4+z1^3 z2+z1^2 z2^2+z1 z2^3+z2^4,  h2 = z1^2+z1 z2+z2^2.

Counts points over F_{5^j}, j=1..JMAX, both on B_q (ordered pairs incl. z1=z2
solutions of the divided difference) and on the S_2-quotient in coordinates
s=z1+z2, m=z1*z2:  q*(s^4-3s^2 m+m^2) + (s^2-m) - 3 = 0
  [since h4 = s^4-3s^2 m + m^2, h2 = s^2 - m].
Quotient count via solving quadratic in m (degree 2 in m).
"""
import flint, sys, time, json

P = 5
JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8

def enumerate_field(ctx, deg):
    g = ctx.gen()
    els = [ctx(c) for c in range(P)]
    pw = ctx(1)
    for k in range(1, deg):
        pw = pw * g
        base = [ctx(c) * pw for c in range(P)]
        els = [e + b for e in els for b in base]
    return els

def counts_for(q):
    out = {}
    for j in range(1, JMAX + 1):
        ctx = flint.fq_default_ctx(P, j)
        pctx = flint.fq_default_poly_ctx(ctx)
        els = enumerate_field(ctx, j)
        cq = ctx(q); c3 = ctx(3); c1 = ctx(1)
        # ordered-pair affine curve: for each z1, roots in z2 of
        # q(z2^4 + z1 z2^3 + z1^2 z2^2 + z1^3 z2 + z1^4) + z2^2 + z1 z2 + z1^2 - 3
        n_ord = 0
        for z1 in els:
            z1_2 = z1*z1; z1_3 = z1_2*z1; z1_4 = z1_2*z1_2
            f = pctx([cq*z1_4 + z1_2 - c3, cq*z1_3 + z1, cq*z1_2 + c1, cq*z1, cq])
            n_ord += len(f.roots())
        # quotient curve in (s,m): q*(s^4-3 s^2 m+m^2) + s^2 - m - 3 = 0
        n_sym = 0
        for s in els:
            s2 = s*s; s4 = s2*s2
            g = pctx([cq*s4 + s2 - c3, -c3*cq*s2 - c1, cq])
            n_sym += len(g.roots())
        out[j] = (n_ord, n_sym)
        print(f"q={q} j={j}: ordered {n_ord}, sym(s,m) {n_sym}", flush=True)
    return out

res = {}
for q in [1, 3, 4]:
    res[q] = counts_for(q)
json.dump({str(k): v for k, v in res.items()}, open("pair_curve_p5.json", "w"), indent=1)
