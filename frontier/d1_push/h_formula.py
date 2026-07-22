#!/usr/bin/env python3
"""Explicit trinomial-coefficient formula for the Cartier matrix entries.

F = X^p + aX^3 + cX + d.  F^{p-1} = sum over m+i+j+k=p-1 of
multinom(p-1;m,i,j,k) a^i c^j d^k X^{pm+3i+j}.

Mod p: multinom(p-1;m,i,j,k) = (-1)^{i+j+k} (i+j+k)!/(i!j!k!).

H_{u,v} = [X^{pu-v}] F^{p-1}:  need pm+3i+j = pu-v.  Put w=u-m (1<=w<=min(4,u)),
then 3i+j = pw-v and n := i+j+k = p-1-u+w is DETERMINED by (u,w).

H_{u,v} = sum_{w=1}^{min(4,u)} sum_{i} (-1)^n n!/(i! j! k!) a^i c^j d^k
   with n = p-1-u+w, j = pw-v-3i >= 0, k = n-i-j >= 0.

This script verifies the formula against flint coefficients of F^{p-1}
for p = 5,7,11,13 and all (a,c,d) in a random sample + all for p=5,7.
"""
from flint import nmod_poly
from math import factorial
import random

def entry_formula(p, u, v, a, c, d):
    """H_{u,v} mod p via the trinomial-coefficient formula."""
    total = 0
    for w in range(1, min(4, u) + 1):
        n = p - 1 - u + w
        if n < 0 or n > p - 1:
            continue
        sgn = (-1) ** n
        target = p * w - v          # 3i + j = target
        for i in range(0, min(n, target // 3) + 1):
            j = target - 3 * i
            if j < 0:
                break
            k = n - i - j
            if k < 0:
                continue
            coef = factorial(n) // (factorial(i) * factorial(j) * factorial(k))
            total += sgn * coef * pow(a, i, p) * pow(c, j, p) * pow(d, k, p)
    return total % p

def entry_flint(p, u, v, a, c, d, Gcache):
    G = Gcache
    e = p * u - v
    return int(G[e]) if 0 <= e <= G.degree() else 0

def check(p, samples=None):
    trip = []
    if samples is None:
        trip = [(a, c, d) for a in range(1, p) for c in range(p) for d in range(p)]
    else:
        rng = random.Random(42)
        trip = [(rng.randrange(1, p), rng.randrange(p), rng.randrange(p))
                for _ in range(samples)]
    bad = 0
    for (a, c, d) in trip:
        F = nmod_poly([d, c, 0, a] + [0]*(p-4) + [1], p)
        G = F ** (p - 1)
        for u in range(1, p + 1):
            for v in range(1, p + 1):
                x = entry_formula(p, u, v, a, c, d)
                y = entry_flint(p, u, v, a, c, d, G)
                if x != y:
                    bad += 1
                    if bad < 5:
                        print("BAD", p, u, v, a, c, d, x, y)
    print(f"p={p}: {len(trip)} triples x {p*p} entries checked, bad={bad}")
    return bad

tot = 0
tot += check(5)
tot += check(7)
tot += check(11, samples=30)
tot += check(13, samples=30)
print("FORMULA VERIFIED" if tot == 0 else "FORMULA FAILED")
