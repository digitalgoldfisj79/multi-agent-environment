#!/usr/bin/env python3
"""
p=7 ordered pair curve B_q: {(z1,z2): D(z1,z2) := (P_q(z1)-P_q(z2))/(z1-z2) = 0},
P_q(z) = q z^7 + z^3 - 3z.  Plane sextic  q*h6(z1,z2) + h2(z1,z2) - 3 = 0.
Affine point counts over F_{7^j}, j <= JMAX (roots of the sextic in z2 per z1).
"""
import flint, sys, json

P = 7
JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
QS = [int(x) for x in sys.argv[2:]] or [1, 3, 4, 5, 6]

def enumerate_field(ctx, deg):
    g = ctx.gen()
    els = [ctx(c) for c in range(P)]
    pw = ctx(1)
    for k in range(1, deg):
        pw = pw * g
        base = [ctx(c) * pw for c in range(P)]
        els = [e + b for e in els for b in base]
    return els

out = {}
for q in QS:
    out[q] = {}
    for j in range(1, JMAX + 1):
        ctx = flint.fq_default_ctx(P, j)
        pctx = flint.fq_default_poly_ctx(ctx)
        els = enumerate_field(ctx, j)
        cq = ctx(q); c3 = ctx(3); c1 = ctx(1)
        n = 0
        for z1 in els:
            zp = [c1]
            for _ in range(6):
                zp.append(zp[-1] * z1)
            # sextic in z2: q*(z2^6 + z1 z2^5 + ... + z1^6) + z2^2 + z1 z2 + z1^2 - 3
            f = pctx([cq * zp[6] + zp[2] - c3,
                      cq * zp[5] + zp[1],
                      cq * zp[4] + c1,
                      cq * zp[3],
                      cq * zp[2],
                      cq * zp[1],
                      cq])
            n += len(f.roots())
        out[q][j] = n
        print(f"q={q} j={j}: N_B = {n}  (N-7^j = {n - P**j})", flush=True)
json.dump(out, open("pair_curve_p7.json", "w"), indent=1)
