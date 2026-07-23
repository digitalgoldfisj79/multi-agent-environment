#!/usr/bin/env python3
"""Exact discriminant audit for the root-negation descended family.

For m=(p-1)/2, H(Y)=Y^m+aY+c, G(Y)=Y H(Y)^2-e and
 y0=-c/(3a), B=y0 H(y0)^2, verify

 Disc(G)=(-1)^m 3a e^m (e-B)

for every c and every nonzero e, both square classes of a, and every prime
in the requested range.  All arithmetic is exact modulo p.
"""
from __future__ import annotations
import argparse,json
from math import isqrt
from flint import nmod_poly


def primes_upto(n):
    s=[True]*(n+1);s[:2]=[False,False]
    for i in range(2,isqrt(n)+1):
        if s[i]:s[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]

def chi(x,p):
    x%=p
    return 0 if x==0 else (1 if pow(x,(p-1)//2,p)==1 else -1)

def audit(p,a):
    m=(p-1)//2; mismatches=[]
    inv3a=pow((3*a)%p,p-2,p)
    for c in range(p):
        H=nmod_poly([c,a]+[0]*(m-2)+[1],p)
        y0=(-c*inv3a)%p
        B=(y0*pow(int(H(y0)),2,p))%p
        for e in range(1,p):
            G=nmod_poly([0,1],p)*H*H-e
            got=int(G.discriminant())%p
            pred=(((-1)**m)*3*a*pow(e,m,p)*(e-B))%p
            if got!=pred:
                mismatches.append({'c':c,'e':e,'got':got,'pred':pred,'B':B})
                if len(mismatches)>=5:return {'p':p,'a':a,'pass':False,'mismatches':mismatches}
    return {'p':p,'a':a,'pass':True,'cases':p*(p-1),'mismatches':[]}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-prime',type=int,default=101);args=ap.parse_args()
    rows=[]
    for p in primes_upto(args.max_prime):
        if p<5:continue
        ns=next(x for x in range(2,p) if chi(x,p)==-1)
        for a in (1,ns):
            r=audit(p,a);rows.append(r);print(json.dumps(r),flush=True)
    print(json.dumps({'status':'PASS' if all(r['pass'] for r in rows) else 'FAIL','rows':rows},indent=2))
if __name__=='__main__':main()
