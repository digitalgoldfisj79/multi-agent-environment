#!/usr/bin/env python3
"""
p=7: pair-curve traces, untwisted and sgn-twisted:
  anti_j     = X2_j  - Q_j    -> Lambda^2-isotypic trace  (compare P_j(2))
  antichi_j  = X2c_j - Qc_j   -> Lambda^2 (x) sgn trace   (compare P_j(4))
where
  X2_j  = sum_{z1} #{z2 != z1 : f(z2)=f(z1)}          (ordered pairs)
  X2c_j = same but weighted chi(u (t^2-1)), t = f(z1)
  Q_j   = # rational points of the (s,m) quotient curve (distinct-pair part)
  Qc_j  = same weighted chi(u (t^2-1)), t = (q p7(s,m) + p3(s,m) - 3s)/(2(q-2))
Diagonal / critical points carry chi-weight 0 automatically in twisted sums;
untwisted sums exclude z1=z2 explicitly and the (s,m) count includes only
s^2 != 4m points (diagonal points are (+-1,+-1) with t=+-1; we drop them).
"""
import flint, sys, json

P = 7
JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
UQ = {1: 4, 3: 3, 4: 2, 5: 6, 6: 6}

def enumerate_field(ctx, deg):
    g = ctx.gen()
    els = [ctx(c) for c in range(P)]
    pw = ctx(1)
    for k in range(1, deg):
        pw = pw * g
        base = [ctx(c) * pw for c in range(P)]
        els = [e + b for e in els for b in base]
    return els

def chi(ctx, x, e):
    if x == ctx(0): return 0
    return 1 if x ** e == ctx(1) else -1

out = {}
for q in [int(x) for x in sys.argv[2:]] or [1, 3, 4, 5, 6]:
    out[q] = {}
    for j in range(1, JMAX + 1):
        ctx = flint.fq_default_ctx(P, j)
        pctx = flint.fq_default_poly_ctx(ctx)
        els = enumerate_field(ctx, j)
        e = (P**j - 1) // 2
        cq = ctx(q); c3 = ctx(3); c1 = ctx(1); u = ctx(UQ[q])
        qm2inv = ctx(1) / ctx(q - 2); half = ctx(1) / ctx(2)
        one = ctx(1)
        X2 = Q = X2c = Qc = 0
        for z1 in els:
            zp = [c1]
            for _ in range(7):
                zp.append(zp[-1] * z1)
            t = (cq * zp[7] + zp[3] - c3 * z1) * qm2inv
            f = pctx([cq * zp[6] + zp[2] - c3,
                      cq * zp[5] + zp[1],
                      cq * zp[4] + c1,
                      cq * zp[3], cq * zp[2], cq * zp[1], cq])
            rts = f.roots()
            k = sum(1 for (r, m) in rts if r != z1)
            X2 += k
            w = chi(ctx, u * (t * t - one), e)
            X2c += w * k
        for s in els:
            s2 = s * s; s4 = s2 * s2; s6 = s4 * s2
            g = pctx([cq * s6 + s2 - c3,
                      -ctx(5) * cq * s4 - c1,
                      ctx(6) * cq * s2, -cq])
            for (m, mult) in g.roots():
                if s2 == ctx(4) * m:
                    continue          # diagonal (ramification) points
                # p1=s, p2=s^2-2m, p3=s^3-3sm, ... p7 via Newton
                pk = [ctx(2), s]
                for kk in range(2, 8):
                    pk.append(s * pk[-1] - m * pk[-2])
                t = (cq * pk[7] + pk[3] - c3 * s) * qm2inv * half
                Q += 1
                Qc += chi(ctx, u * (t * t - one), e)
        anti, antic = X2 - Q, X2c - Qc
        out[q][j] = (X2, Q, X2c, Qc, anti, antic)
        print(f"q={q} j={j}: X2={X2} Q={Q} anti={anti} | X2c={X2c} Qc={Qc} antichi={antic}",
              flush=True)
json.dump(out, open("pair_twist_p7.json", "w"), indent=1)
