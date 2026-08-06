#!/usr/bin/env python3
"""Exact finite regression for the prime-modulus primorial-walk large-sieve lemma."""
from __future__ import annotations
import cmath
import math

def primes_upto(limit):
    sieve=bytearray(b"\x01")*(limit+1)
    if limit>=0: sieve[0]=0
    if limit>=1: sieve[1]=0
    for p in range(2,int(limit**0.5)+1):
        if sieve[p]:
            sieve[p*p:limit+1:p]=b"\x00"*(((limit-p*p)//p)+1)
    return [i for i,v in enumerate(sieve) if v]

def test_panel(X,Q):
    ps=primes_upto(Q)
    rows=[p for p in ps if X<=p<2*X]
    probes=[q for q in ps if 2*X<q<=Q]
    residues={}
    for q in probes:
        acc=1
        vals=[]
        rowset=set(rows)
        for p in ps:
            if p>rows[-1]: break
            acc=(acc*p)%q
            if p in rowset:
                vals.append(acc)
        residues[q]=vals
    lhs=0
    collision_weight=0
    for q,vals in residues.items():
        energy=0.0
        for a in range(q):
            s=sum(cmath.exp(2j*math.pi*a*v/q) for v in vals)
            energy+=abs(s)**2
        collisions=sum(1 for x in vals for y in vals if x==y)
        exact=q*collisions
        assert abs(energy-exact)<=1e-6*max(1,exact),(X,Q,q,energy,exact)
        lhs+=exact
        collision_weight+=q*(collisions-len(vals))
    n=len(rows)
    diagonal=n*sum(probes)
    pair_budget=2*Q*sum((n-d)*d for d in range(1,n))
    assert collision_weight<=pair_budget,(X,Q,collision_weight,pair_budget)
    assert lhs<=diagonal+pair_budget
    print(f"X={X} Q={Q} rows={n} prime_moduli={len(probes)} collision_weight={collision_weight} pair_budget={pair_budget}")
for X,Q in [(20,97),(30,149),(50,251),(80,401)]:
    test_panel(X,Q)
print("FORTUNE_INT_SOCG_C5_PRIME_MODULUS_WALK_LARGE_SIEVE_PASS")
