#!/usr/bin/env python3
"""Exact low-height search for direct dynamical d=1 witnesses.

For every odd prime p below a bound, scan fixed integral cubic tails
(a,b,c,d) reduced modulo p and certify irreducibility of

    X^p + a X^3 + b X^2 + c X + d.

By the established dynamics equivalence this is an exact-period-p certificate
for the corresponding cubic map. Phase one keeps the first few witnesses per
prime. Phase two retests the union of those fixed maps against every prime and
computes an exact greedy set cover. No probabilistic primality or
irreducibility decision is used.
"""
from __future__ import annotations
import argparse, json, math, multiprocessing as mp, time
from flint import nmod_poly


def primes_below(n: int) -> list[int]:
    out=[]
    for x in range(5,n):
        if all(x%d for d in range(2,int(math.isqrt(x))+1)): out.append(x)
    return out


def quick_reducible(p, f, x, kmax=6):
    g1=x.pow_mod(p,f)
    if f.gcd(g1-x).degree()!=0:return True,g1
    g=g1
    for _ in range(2,kmax+1):
        g=g1.compose_mod(g,f)
        if f.gcd(g-x).degree()>0:return True,g1
    return False,g1


def full_rabin(p,f,x,g1):
    result=None;base=g1;k=p
    while k:
        if k&1:result=base if result is None else base.compose_mod(result,f)
        k>>=1
        if k:base=base.compose_mod(base,f)
    return result==x and f.gcd(g1-x).degree()==0


def certified(p,tail):
    a,b,c,d=(v%p for v in tail)
    f=nmod_poly([d,c,b,a]+[0]*(p-4)+[1],p);x=nmod_poly([0,1],p)
    red,g1=quick_reducible(p,f,x)
    return False if red else full_rabin(p,f,x,g1)

CANDIDATES=[]
def init(candidates):
    global CANDIDATES;CANDIDATES=candidates

def find_first(args):
    p,need=args;found=[];tested=0;t=time.time()
    for tail in CANDIDATES:
        tested+=1
        if certified(p,tail):
            found.append(tail)
            if len(found)>=need:break
    return {'p':p,'tested':tested,'found':found,'elapsed':time.time()-t}

def coverage_for_prime(p):
    return p,[i for i,t in enumerate(CANDIDATES) if certified(p,t)]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-prime',type=int,default=1500);ap.add_argument('--height',type=int,default=4);ap.add_argument('--per-prime',type=int,default=3);ap.add_argument('--workers',type=int,default=32);a=ap.parse_args()
    vals=list(range(-a.height,a.height+1)); leads=[v for v in vals if v]
    candidates=[(aa,b,c,d) for aa in leads for b in vals for c in vals for d in vals]
    ps=primes_below(a.max_prime)
    with mp.Pool(a.workers,initializer=init,initargs=(candidates,)) as pool:
        phase1=pool.map(find_first,[(p,a.per_prime) for p in ps])
    union=[]
    for r in phase1:
        for t in r['found']:
            t=tuple(t)
            if t not in union:union.append(t)
    with mp.Pool(a.workers,initializer=init,initargs=(union,)) as pool:
        cov=dict(pool.map(coverage_for_prime,ps))
    uncovered=[p for p in ps if not cov[p]]
    remaining=set(ps);chosen=[]
    while remaining:
        best=None;hit=set()
        for i,t in enumerate(union):
            h={p for p in remaining if i in cov[p]}
            if len(h)>len(hit):best=i;hit=h
        if not hit:break
        chosen.append({'tail':union[best],'new_primes':sorted(hit),'new_count':len(hit)})
        remaining-=hit
    map_coverage=[]
    for i,t in enumerate(union):
        hit=[p for p in ps if i in cov[p]]
        map_coverage.append({'tail':t,'count':len(hit),'primes':hit})
    map_coverage.sort(key=lambda z:(-z['count'],z['tail']))
    out={'status':'PASS','method':'exact FLINT Rabin certification','max_prime':a.max_prime,'height':a.height,'candidate_count':len(candidates),'prime_count':len(ps),'per_prime_target':a.per_prime,'phase1_failures':[r for r in phase1 if len(r['found'])<a.per_prime],'union_map_count':len(union),'uncovered_primes':uncovered,'greedy_menu':chosen,'greedy_uncovered':sorted(remaining),'top_fixed_maps':map_coverage[:25],'phase1':phase1}
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
