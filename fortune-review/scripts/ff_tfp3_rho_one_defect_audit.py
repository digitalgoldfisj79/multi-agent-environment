#!/usr/bin/env python3
"""Exact audit of the two q=97 normalized TFP3 records with rho=1.

The records satisfy all four inverse-free equations and have nonzero common
defect. This verifies that rho=1 is not a zero-defect criterion; only the
forward implication h=0 => rho=1 is valid.
"""
from __future__ import annotations
import json
import ff_tfp3_orientation_verify as verify

ROWS=[
 {"type":"orbit","q":97,"rho":1,"A":[0,74,40],"B":[57,44,61],"C":[43,76,71],"D":[83,61,67]},
 {"type":"orbit","q":97,"rho":1,"A":[0,28,55],"B":[57,90,77],"C":[71,27,7],"D":[14,10,81]},
]

def divmod_poly(a:list[int],b:list[int],q:int)->tuple[list[int],list[int]]:
    a=verify.trim([x%q for x in a]); b=verify.trim([x%q for x in b])
    out=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b):
        c=a[-1]*pow(b[-1],-1,q)%q; d=len(a)-len(b); out[d]=c
        for i,x in enumerate(b): a[i+d]=(a[i+d]-c*x)%q
        verify.trim(a)
    return verify.trim(out),a

def audit(row:dict)->dict:
    verified=verify.verify_orbit(row)
    q=row["q"]; rho=row["rho"]
    P,S,Pp,Sp=[verify.polynomial(row[n],q) for n in "ABCD"]
    L=[0,q-1]+[0]*(q-2)+[1]
    Aq,r=divmod_poly(verify.sub(verify.mul(L,S,q),Pp,q),P,q); assert not r
    Bq,r=divmod_poly(verify.add(verify.mul(L,P,q),verify.scale(Sp,rho,q),q),S,q); assert not r
    Cq,r=divmod_poly(verify.add(verify.mul(L,Sp,q),P,q),Pp,q); assert not r
    Dq,r=divmod_poly(verify.sub(verify.mul(L,Pp,q),verify.scale(S,rho,q),q),Sp,q); assert not r
    numerator=verify.sub(verify.scale(Cq,rho,q),Bq,q)
    h,r=divmod_poly(numerator,verify.mul(P,Sp,q),q); assert not r and h
    numerator2=verify.sub(verify.scale(Aq,rho,q),Dq,q)
    h2,r=divmod_poly(numerator2,verify.mul(S,Pp,q),q); assert not r and h2==h
    return {**verified,"defect_degree":len(h)-1,"defect_leading_coefficient":h[-1],"defect_nonzero":True}

def main()->None:
    results=[audit(row) for row in ROWS]
    assert all(r["defect_degree"]==89 for r in results)
    print(json.dumps({
      "status":"TFP3_RHO_ONE_NONZERO_DEFECT_EXACT_PASS",
      "implication_correction":"h=0 implies rho=1; rho=1 does not imply h=0",
      "records":results,
    },indent=2,sort_keys=True))
if __name__=="__main__": main()
