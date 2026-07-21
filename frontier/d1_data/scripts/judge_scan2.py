"""Fast extended scan (judge): same counts as judge_scan.py but using a Frobenius
composition ladder: h_n(x) := x^{p^n} mod f satisfies h_{m+n} = h_n(h_m) mod f
(exact congruence over F_p; Frobenius endomorphism of F_p[x]/(f)).
Irreducible (deg p prime) iff gcd(h_1 - x, f) = 1 and h_p = x.
"""
import sys, json, time
from flint import nmod_poly
from sympy import primerange

def frob_ladder(h1, f, n):
    """x^{p^n} mod f given h1 = x^p mod f, via binary ladder on composition."""
    # binary: maintain (result, base) as exponents in composition monoid
    res = None  # identity (x)
    base = h1
    e = n
    while e:
        if e & 1:
            res = base if res is None else res.compose_mod(base, f)
        e >>= 1
        if e:
            base = base.compose_mod(base, f)
    return res

def is_irred_degp(coeffs, p, x=None):
    f = nmod_poly(coeffs, p)
    x = nmod_poly([0, 1], p)
    h1 = x.pow_mod(p, f)
    if f.gcd(h1 - x).degree() > 0:
        return False
    return frob_ladder(h1, f, p) == x

def smallest_nonresidue(p):
    for n in range(2, p):
        if pow(n, (p-1)//2, p) == p-1:
            return n

if __name__ == '__main__':
    P0 = int(sys.argv[1]); P1 = int(sys.argv[2])
    OUT = sys.argv[3] if len(sys.argv) > 3 else 'judge_scan2_results.json'
    results = {}
    try:
        results = json.load(open(OUT))
    except Exception:
        pass
    for p in primerange(P0, P1+1):
        if str(p) in results: continue
        t0 = time.time()
        n = smallest_nonresidue(p)
        counts = {}
        for a in (1, n):
            cnt = 0
            for c in range(p):
                for d in range(p):
                    co = [d, c, 0, a] + [0]*(p-4) + [1]
                    if is_irred_degp(co, p):
                        cnt += 1
            counts[a] = cnt
        Np = 0
        for d in range(p):
            co = [d, 0, 1] + [0]*(p-3) + [1]
            if is_irred_degp(co, p): Np += 1
        cp, cm = counts[1], counts[n]
        zp = (cp - p)/p**0.5; zm = (cm - p)/p**0.5
        results[str(p)] = dict(cnt_plus=cp, cnt_minus=cm, N=Np, z_plus=zp, z_minus=zm,
                               r_plus=cp/p - 1, r_minus=cm/p - 1,
                               secs=round(time.time()-t0, 1))
        print(f"p={p:3d}  #b0(+)={cp:4d} #b0(-)={cm:4d}  N={Np}  z=({zp:+.2f},{zm:+.2f})  [{results[str(p)]['secs']}s]", flush=True)
        json.dump(results, open(OUT, 'w'))
    print("done")
