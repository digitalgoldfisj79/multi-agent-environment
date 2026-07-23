#!/usr/bin/env python3
"""Independent exact depressed-slice irreducible counter using python-flint.

For prime degree p, Rabin's criterion is
  gcd(F,X^p-X)=1 and X^(p^p)=X mod F.
The p-fold Frobenius iterate is computed by binary exponentiation under modular
polynomial composition, requiring O(log p) compositions rather than p dense
matrix applications.  Small factor degrees are screened first but every
accepted polynomial receives the full exact Rabin test.
"""
from __future__ import annotations
import argparse, json, math, multiprocessing as mp, time
from flint import nmod_poly

P=A=0

def legendre(a,p):
    r=pow(a%p,(p-1)//2,p)
    return 0 if not a%p else (1 if r==1 else -1)

def init(p,a):
    global P,A;P=p;A=a

def irreducible(c,d):
    p=P;a=A
    f=nmod_poly([d,c,0,a]+[0]*(p-4)+[1],p)
    x=nmod_poly([0,1],p)
    g1=x.pow_mod(p,f)
    if f.gcd(g1-x).degree()!=0:return False
    # Safe early rejection by factors of degrees 2..6.
    g=g1
    for _ in range(2,7):
        g=g1.compose_mod(g,f)
        if f.gcd(g-x).degree()>0:return False
    # Exact p-fold Frobenius iterate by binary composition.
    result=None;base=g1;k=p
    while k:
        if k&1:result=base if result is None else base.compose_mod(result,f)
        k>>=1
        if k:base=base.compose_mod(base,f)
    return result==x

def work(c):
    n=0
    for d in range(P):
        if irreducible(c,d):n+=1
    return n

def main():
    ap=argparse.ArgumentParser();ap.add_argument('p',type=int);ap.add_argument('--workers',type=int,default=48);a=ap.parse_args();p=a.p
    ns=2
    while legendre(ns,p)!=-1:ns+=1
    rows=[]
    for aa,cl in [(1,'square'),(ns,'nonsquare')]:
        t=time.time()
        with mp.Pool(a.workers,initializer=init,initargs=(p,aa)) as pool:
            n=sum(pool.imap_unordered(work,range(p),chunksize=1))
        rows.append({'prime':p,'a':aa,'square_class':cl,'N':n,'residue_mod_p':n%p,'positive':n>0,'below_3p_over_2':2*n<3*p,'below_2p':n<2*p,'ratio':n/p,'elapsed_seconds':time.time()-t})
        print(json.dumps(rows[-1]),flush=True)
    print(json.dumps({'status':'PASS','method':'exact FLINT Rabin with logarithmic Frobenius composition','rows':rows},indent=2))
if __name__=='__main__':main()
