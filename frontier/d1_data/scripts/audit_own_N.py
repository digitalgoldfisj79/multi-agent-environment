"""Auditor's independent N(p) computation. Different code path from both teams:
full Rabin test (no prefilter) for every d, via compose_mod doubling."""
from flint import nmod_poly
import sys, time

def is_irred(p, coeffs):
    f = nmod_poly(coeffs, p)
    x = nmod_poly([0,1], p)
    G1 = x.pow_mod(p, f)
    if f.gcd(G1 - x).degree() != 0:
        return False           # has a root in F_p
    result = None; base = G1; k = p
    while k:
        if k & 1:
            result = base if result is None else base.compose_mod(result, f)
        k >>= 1
        if k: base = base.compose_mod(base, f)
    return result == x

def N_own(p):
    cnt = 0; ds = []
    for d in range(p):
        c = [d,0,1] + [0]*(p-3) + [1]   # x^p + x^2 + d  (needs p>3)
        if is_irred(p, c):
            cnt += 1; ds.append(d)
    return cnt, ds

if __name__ == '__main__':
    for p in [int(a) for a in sys.argv[1:]]:
        t = time.time()
        n, ds = N_own(p)
        print(f'p={p}: N={n} ds={ds}  ({time.time()-t:.1f}s)', flush=True)
