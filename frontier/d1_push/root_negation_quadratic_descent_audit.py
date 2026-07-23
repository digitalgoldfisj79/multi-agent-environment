#!/usr/bin/env python3
"""Audit the exact root-negation quadratic descent.

For m=(p-1)/2,
 F_d(X)=X^p+aX^3+cX+d,
 G_e(Y)=Y(Y^m+aY+c)^2-e.

The theorem predicts, for every d!=0,
 F_d irreducible <=> F_-d irreducible <=> G_(d^2) irreducible,
and N_a=2*#{(c,e square nonzero):G_e irreducible}.
All tests are exact finite-field polynomial factorizations.
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

def irreducible(f):
    _,fac=f.factor()
    return len(fac)==1 and fac[0][1]==1 and fac[0][0].degree()==f.degree()

def audit_case(p,a):
    m=(p-1)//2; mismatches=[]; nf=0;ng=0
    squares=sorted({d*d%p for d in range(1,p)})
    for c in range(p):
        H=nmod_poly([c,a]+[0]*(m-2)+[1],p) if m>=2 else nmod_poly([c,a+1],p)
        for e in squares:
            G=nmod_poly([0,1],p)*H*H-e
            if irreducible(G):ng+=1
        for d in range(1,p):
            F=nmod_poly([d,c,0,a]+[0]*(p-4)+[1],p)
            Fm=nmod_poly([-d,c,0,a]+[0]*(p-4)+[1],p)
            G=nmod_poly([0,1],p)*H*H-(d*d%p)
            vals=(irreducible(F),irreducible(Fm),irreducible(G))
            nf+=vals[0]
            if not(vals[0]==vals[1]==vals[2]):
                mismatches.append({'c':c,'d':d,'values':vals})
                if len(mismatches)>=5:return {'p':p,'a':a,'pass':False,'mismatches':mismatches}
    return {'p':p,'a':a,'N_F':nf,'N_G_square':ng,'pass':not mismatches and nf==2*ng,'mismatches':mismatches}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-prime',type=int,default=43);args=ap.parse_args()
    rows=[]
    for p in primes_upto(args.max_prime):
        if p<5:continue
        ns=next(a for a in range(2,p) if chi(a,p)==-1)
        for a in (1,ns):
            r=audit_case(p,a);rows.append(r);print(json.dumps(r),flush=True)
    print(json.dumps({'status':'PASS' if all(r['pass'] for r in rows) else 'FAIL','rows':rows},indent=2))
if __name__=='__main__':main()
