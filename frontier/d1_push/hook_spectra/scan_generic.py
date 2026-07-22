#!/usr/bin/env python3
"""
Generic cycle-type census for the normal-form family
    P_{q,t}(z) = q z^p + z^3 - 3 z - (q-2) t   over F_{p^j},
for all t in F_{p^j} \ {1,-1}, j = 1..JMAX, q in F_p \ {0,2}.

Parallel over chunks of the top base-p digit of t.

Usage: scan_generic.py p jmin jmax nworkers [q1 q2 ...]
Writes cycle_counts_p{p}_j{j}_q{q}.json incrementally.
"""
import flint, json, sys, time, os
from multiprocessing import Pool

P = int(sys.argv[1])
JMIN = int(sys.argv[2])
JMAX = int(sys.argv[3])
NW = int(sys.argv[4])
QLIST = [int(x) for x in sys.argv[5:]] or [q for q in range(1, P) if q != 2]


def low_elements(ctx, deg):
    """All elements with top digit 0 (i.e. of the F_p-span of 1..g^{deg-2})."""
    g = ctx.gen()
    els = [ctx(c) for c in range(P)]
    pw = ctx(1)
    for k in range(1, deg - 1):
        pw = pw * g
        base = [ctx(c) * pw for c in range(P)]
        els = [e + b for e in els for b in base]
    return els


def work(args):
    q, j, wid, nw = args
    ctx = flint.fq_default_ctx(P, j)
    pctx = flint.fq_default_poly_ctx(ctx)
    qm2 = ctx(q - 2)
    coeffs_tail = [ctx(-3), ctx(0), ctx(1)] + [ctx(0)] * (P - 4) + [ctx(q)]
    one = ctx(1); mone = ctx(-1)
    if j == 1:
        tops = [ctx(0)] if wid == 0 else []
        lows = [ctx(c) for c in range(P)]
    else:
        g = ctx.gen()
        gp = g ** (j - 1)
        tops = [ctx(d) * gp for d in range(P) if d % nw == wid]
        lows = low_elements(ctx, j)
    counts = {}
    for top in tops:
        for lo in lows:
            t = top + lo
            if t == one or t == mone:
                continue
            f = pctx([-qm2 * t] + coeffs_tail)
            _, fac = f.factor()
            key = []
            for (fi, mult) in fac:
                if mult != 1:
                    raise RuntimeError(f"repeated factor q={q} j={j} t={t}")
                key.append(fi.degree())
            key = tuple(sorted(key, reverse=True))
            counts[key] = counts.get(key, 0) + 1
    return counts


def main():
    for q in QLIST:
        for j in range(JMIN, JMAX + 1):
            fn = f"cycle_counts_p{P}_j{j}_q{q}.json"
            if os.path.exists(fn):
                print(f"skip existing {fn}", flush=True)
                continue
            t0 = time.time()
            nw = min(NW, P) if j > 1 else 1
            tasks = [(q, j, w, nw) for w in range(nw)]
            if nw == 1:
                results = [work(tasks[0])]
            else:
                with Pool(nw) as pool:
                    results = pool.map(work, tasks)
            counts = {}
            for c in results:
                for k, v in c.items():
                    counts[k] = counts.get(k, 0) + v
            tot = sum(counts.values())
            assert tot == P ** j - 2, (q, j, tot)
            with open(fn, "w") as fh:
                json.dump({",".join(map(str, k)): v for k, v in counts.items()}, fh)
            print(f"p={P} q={q} j={j}  #t={tot}  irred={counts.get((P,), 0)}  "
                  f"({time.time()-t0:.1f}s)", flush=True)


if __name__ == "__main__":
    main()
