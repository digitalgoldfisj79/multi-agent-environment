#!/usr/bin/env python3
"""
LOOK THROUGH THE DOOR -- post-pushforward Frobenius spectra for p=5.

For each q in F_5 \ {0,2}, the root cover Y_q : P_{q,t}(z) = q z^5 + z^3 - 3z - (q-2) t = 0
is a degree-5 cover of the t-line, etale over U = P^1 \ {+1,-1,oo}
(critical values of f_q(z) = (q z^5 + z^3 - 3z)/(q-2) are exactly +1,-1).

Hook local systems V_i = Lambda^i Std, ranks (1,4,6,4,1),
h^1_c dims (2,6,8,6,1) from the audited ledger (HCE.3).

We compute, for j = 1..JMAX, the cycle-type census of Frobenius on fibers over
t in U(F_{5^j}) = F_{5^j} \ {1,-1}, giving exact trace sums
    T_j(V_i) = sum_t e_i(Std eigenvalues of Frob_t)
via the per-cycle-type e_i tables. Lefschetz gives
    Tr(F^j | H^1_c(U, V_i)) = [i=0] 5^j - T_j(V_i).

Output: JSON with cycle-type counts per (q, j).
"""
import flint, json, sys, time

P = 5
JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
QLIST = [1, 3, 4]          # F_5 \ {0, 2}

# e_i(Std) per cycle type (partition of 5), from E(t) = prod_j(1-(-t)^{d_j})/(1+t)
ETAB = {
    (1,1,1,1,1): (1, 4, 6, 4, 1),
    (2,1,1,1):   (1, 2, 0,-2,-1),
    (2,2,1):     (1, 0,-2, 0, 1),
    (3,1,1):     (1, 1, 0, 1, 1),
    (3,2):       (1,-1, 0, 1,-1),
    (4,1):       (1, 0, 0, 0,-1),
    (5,):        (1,-1, 1,-1, 1),
}

def enumerate_field(ctx, deg):
    """All elements of GF(p^deg) as list."""
    g = ctx.gen()
    els = [ctx(c) for c in range(P)]
    pw = ctx(1)
    for k in range(1, deg):
        pw = pw * g
        base = [ctx(c) * pw for c in range(P)]
        els = [e + b for e in els for b in base]
    return els

def scan(q, j):
    ctx = flint.fq_default_ctx(P, j)
    pctx = flint.fq_default_poly_ctx(ctx)
    qm2 = ctx(q - 2)
    cq = ctx(q); c3 = ctx(-3); c1 = ctx(1); c0z = ctx(0)
    one = ctx(1); mone = ctx(-1)
    counts = {}
    for t in enumerate_field(ctx, j):
        if t == one or t == mone:
            continue
        f = pctx([-qm2 * t, c3, c0z, c1, c0z, cq])
        _, fac = f.factor()
        degs = []
        for (fi, mult) in fac:
            d = fi.degree()
            if mult != 1:
                raise RuntimeError(f"repeated factor at q={q} j={j} t={t}")
            degs.append(d)
        key = tuple(sorted(degs, reverse=True))
        assert sum(key) == 5, (key, str(t))
        counts[key] = counts.get(key, 0) + 1
    return counts

def main():
    out = {}
    for q in QLIST:
        out[str(q)] = {}
        for j in range(1, JMAX + 1):
            t0 = time.time()
            counts = scan(q, j)
            tot = sum(counts.values())
            assert tot == P**j - 2, (q, j, tot)
            out[str(q)][str(j)] = {",".join(map(str, k)): v for k, v in counts.items()}
            print(f"q={q} j={j}  #t={tot}  irred={counts.get((5,),0)}  "
                  f"({time.time()-t0:.1f}s)", flush=True)
    with open(f"cycle_counts_p5_j{JMAX}.json", "w") as fh:
        json.dump(out, fh, indent=1)

if __name__ == "__main__":
    main()
