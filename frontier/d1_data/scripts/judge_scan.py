"""JUDGE: extended scan of cubic slices I_+, I_- and quadratic N(p) for p up to ~PMAX.

Uses proved reductions (independently re-verified at p=5 in judge_p5_full.py):
  - #irred_a = p * #{(c,d): T^p + aT^3 + cT + d irreducible}   (b=0 via translation, a!=0, p>=5)
  - #irred_a depends only on chi(a): compute a=1 (I_+) and a=n (I_-), n smallest nonresidue
  - N(p) = #{d: T^p + T^2 + d irreducible} (quadratic normal form)
Prime-degree irreducibility test: f (monic, deg p) irreducible over F_p iff
  gcd(x^p - x mod f, f) = 1  and  x^{p^p} = x mod f.
Statistic: z_a = (#_{b=0,a} - p)/sqrt(p)   [Poisson model: z ~ N(0,1) indep of p]
           r_a = I_a/p^2 - 1 = z_a / sqrt(p) [critical model: r ~ O(1) indep of p]
"""
import sys, json, time
from flint import nmod_poly
from sympy import primerange, isprime

def is_irred_degp(coeffs, p):
    f = nmod_poly(coeffs, p)
    x = nmod_poly([0, 1], p)
    h = pow(x, p, f)
    if f.gcd(h - x).degree() > 0:
        return False
    g = h
    for _ in range(p - 1):
        g = pow(g, p, f)
    return g == x

def smallest_nonresidue(p):
    for n in range(2, p):
        if pow(n, (p-1)//2, p) == p-1:
            return n

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 61
results = {}
for p in primerange(5, PMAX+1):
    t0 = time.time()
    n = smallest_nonresidue(p)
    counts = {}
    for a in (1, n):
        cnt = 0
        base = [0]*(p+1); base[p] = 1; base[3] = a
        for c in range(p):
            for d in range(p):
                co = list(base); co[1] = c; co[0] = d
                if is_irred_degp(co, p):
                    cnt += 1
        counts[a] = cnt
    Np = 0
    for d in range(p):
        co = [d, 0, 1] + [0]*(p-3) + [1]
        if is_irred_degp(co, p): Np += 1
    cp, cm = counts[1], counts[n]
    Ip, Im = p*cp, p*cm
    zp = (cp - p)/p**0.5; zm = (cm - p)/p**0.5
    rp = Ip/p**2 - 1; rm = Im/p**2 - 1
    results[p] = dict(cnt_plus=cp, cnt_minus=cm, N=Np, z_plus=zp, z_minus=zm,
                      r_plus=rp, r_minus=rm, secs=round(time.time()-t0, 1))
    print(f"p={p:3d}  #b0(+)={cp:4d} #b0(-)={cm:4d}  N={Np}  "
          f"z=({zp:+.2f},{zm:+.2f})  r=({rp:+.3f},{rm:+.3f})  [{results[p]['secs']}s]",
          flush=True)
    json.dump(results, open('judge_scan_results.json', 'w'))
print("done")
