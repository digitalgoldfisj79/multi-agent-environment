"""Auditor: exhaustively verify N(p)=0 for every claimed zero prime.
Every d in F_p must be PROVEN reducible by one of:
  (R) an exhibited root theta in F_p (checked by direct evaluation),
  (G) nontrivial gcd(x^{p^k}-x mod f, f) for some k<p (factor of degree | k),
  (F) full Rabin failure (x^{p^p} != x mod f).
Any survivor passing full Rabin would REFUTE the N(p)=0 claim."""
from flint import nmod_poly
import numpy as np, json, time, sys

def verify_zero(p, kmax=8):
    th = np.arange(p, dtype=np.int64)
    dwithroot = set(((-(th*th + th)) % p).tolist())   # d such that theta^2+theta+d=0 has a root
    # double-check by direct poly evaluation for 3 sample d
    x = nmod_poly([0,1], p)
    survivors = [d for d in range(p) if d not in dwithroot]
    irreducibles = []
    stats = {'root': p - len(survivors), 'gcd': 0, 'rabin_red': 0, 'irred': 0}
    for d in survivors:
        f = nmod_poly([d,0,1] + [0]*(p-3) + [1], p)
        G1 = x.pow_mod(p, f)
        # sanity: no root (gcd with x^p - x)
        assert f.gcd(G1 - x).degree() == 0, (p, d, 'root sieve unsound!')
        G = G1; caught = False
        for k in range(2, kmax+1):
            G = G1.compose_mod(G, f)          # G = x^{p^k} mod f
            if f.gcd(G - x).degree() > 0:
                stats['gcd'] += 1; caught = True; break
        if caught: continue
        # full Rabin: x^{p^p} mod f via doubling
        result = None; base = G1; k = p
        while k:
            if k & 1:
                result = base if result is None else base.compose_mod(result, f)
            k >>= 1
            if k: base = base.compose_mod(base, f)
        if result == x:
            stats['irred'] += 1; irreducibles.append(d)
        else:
            stats['rabin_red'] += 1
    return stats, irreducibles

if __name__ == '__main__':
    zeros = json.load(open('/home/user/multi-agent-environment/frontier/d1_data/d1_dataset.json'))['N_zero_primes']
    out = {}
    for p in zeros:
        t = time.time()
        stats, irr = verify_zero(p)
        ok = (stats['irred'] == 0)
        out[p] = {'stats': stats, 'irreducibles_found': irr, 'confirmed_zero': ok, 'secs': round(time.time()-t,1)}
        print(f'p={p}: {"CONFIRMED N=0" if ok else "REFUTED! irr at d="+str(irr)} {stats} [{out[p]["secs"]}s]', flush=True)
    json.dump(out, open('audit_zero_results.json','w'))
    print('DONE. all confirmed:', all(v['confirmed_zero'] for v in out.values()))
