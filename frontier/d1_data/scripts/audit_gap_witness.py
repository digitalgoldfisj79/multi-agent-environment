"""Find+certify cubic witnesses for the 8 N(p)=0 primes in (1200,1500]."""
from flint import nmod_poly
import random, time

def quick_reducible(p, f, x, kmax=6):
    G1 = x.pow_mod(p, f)
    if f.gcd(G1 - x).degree() != 0: return True, G1
    G = G1
    for k in range(2, kmax+1):
        G = G1.compose_mod(G, f)
        if f.gcd(G - x).degree() > 0: return True, G1
    return False, G1

def full_rabin(p, f, x, G1):
    result = None; base = G1; k = p
    while k:
        if k & 1:
            result = base if result is None else base.compose_mod(result, f)
        k >>= 1
        if k: base = base.compose_mod(base, f)
    return result == x and f.gcd(G1 - x).degree() == 0

random.seed(4053)
for p in [1423, 1439, 1453, 1481]:
    t = time.time(); tries = 0
    x = nmod_poly([0,1], p)
    while True:
        tries += 1
        a = random.randrange(1, p); b, c, d = [random.randrange(p) for _ in '...']
        f = nmod_poly([d, c, b, a] + [0]*(p-4) + [1], p)
        red, G1 = quick_reducible(p, f, x)
        if red: continue
        if full_rabin(p, f, x, G1):
            print(f'p={p}: witness (a,b,c,d)=({a},{b},{c},{d}) certified irreducible after {tries} tries [{time.time()-t:.0f}s]', flush=True)
            break
