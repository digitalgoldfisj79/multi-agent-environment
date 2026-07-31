#!/usr/bin/env python3
# Independent exact verifier for canonical TFP3 orbit JSONL records.
from __future__ import annotations
import argparse, json
from collections import Counter, defaultdict
from pathlib import Path

def trim(p: list[int]) -> list[int]:
    while p and p[-1] == 0:
        p.pop()
    return p

def add(a: list[int], b: list[int], q: int) -> list[int]:
    n=max(len(a),len(b))
    return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%q for i in range(n)])

def scale(a: list[int], c: int, q: int) -> list[int]:
    return trim([(c*x)%q for x in a])

def sub(a: list[int], b: list[int], q: int) -> list[int]:
    return add(a,scale(b,-1,q),q)

def mul(a: list[int], b: list[int], q: int) -> list[int]:
    if not a or not b: return []
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]=(out[i+j]+x*y)%q
    return trim(out)

def rem(a: list[int], f: list[int], q: int) -> list[int]:
    a=trim(a[:]); f=trim(f[:])
    while len(a)>=len(f):
        c=a[-1]*pow(f[-1],-1,q)%q
        d=len(a)-len(f)
        for i,x in enumerate(f): a[i+d]=(a[i+d]-c*x)%q
        trim(a)
    return a

def mulmod(a: list[int], b: list[int], f: list[int], q: int) -> list[int]:
    return rem(mul(a,b,q),f,q)

def powmod(a: list[int], n: int, f: list[int], q: int) -> list[int]:
    out=[1]
    while n:
        if n&1: out=mulmod(out,a,f,q)
        a=mulmod(a,a,f,q); n//=2
    return out

def polynomial(record: list[int], q: int) -> list[int]:
    a2,a1,a0=record
    return [a0%q,a1%q,a2%q,1]

def evaluate(f: list[int], x: int, q: int) -> int:
    out=0
    for c in reversed(f): out=(out*x+c)%q
    return out

def irreducible_cubic(f: list[int], q: int) -> bool:
    return len(f)==4 and f[-1]==1 and all(evaluate(f,x,q) for x in range(q))

def eta_frobenius(f: list[int], q: int) -> int:
    x=[0,1]
    xq=powmod(x,q,f,q)
    xq2=powmod(xq,q,f,q)
    eta=mulmod(mulmod(sub(x,xq,q),sub(x,xq2,q),f,q),sub(xq,xq2,q),f,q)
    if any(eta[i] for i in range(1,len(eta))):
        raise AssertionError(f"Frobenius Vandermonde is not scalar: {eta}")
    value=eta[0] if eta else 0
    if not value: raise AssertionError("zero Frobenius Vandermonde")
    return value

def cycle_numerator(f: list[int], eta: int, q: int) -> list[int]:
    a0,a1,a2,_=f
    i2=pow(2,-1,q)
    return [
        (i2*a2*a2*a1+3*i2*a2*a0-2*a1*a1-i2*a2*eta)%q,
        (a2**3-7*i2*a2*a1+9*i2*a0-3*i2*eta)%q,
        (a2*a2-3*a1)%q,
    ]

def is_prime(q: int) -> bool:
    return q>=2 and all(q%d for d in range(2,int(q**0.5)+1))

def verify_orbit(row: dict) -> dict:
    q=int(row["q"]); rho=int(row["rho"])%q
    if not is_prime(q) or q in (2,3): raise AssertionError(f"unsupported q={q}")
    blocks=[polynomial(row[name],q) for name in "ABCD"]
    if len({tuple(f) for f in blocks}) != 4: raise AssertionError("not cross-distinct")
    if blocks[0][2] != 0: raise AssertionError("A2 gauge failed")
    if rho in (0,1): raise AssertionError("nonzero-defect rho gate failed")
    if not all(irreducible_cubic(f,q) for f in blocks):
        raise AssertionError("reducible cubic in true orbit")
    A,B,C,D=blocks
    L=lambda f: sub(powmod([0,1],q,f,q),[0,1],q)
    direct=[
        rem(sub(mul(L(A),B,q),C,q),A,q),
        rem(add(mul(L(C),D,q),A,q),C,q),
        rem(add(mul(L(B),A,q),scale(D,rho,q),q),B,q),
        rem(sub(mul(L(D),C,q),scale(B,rho,q),q),D,q),
    ]
    if any(direct): raise AssertionError(f"inverse-free equation failed: {direct}")
    eta=[eta_frobenius(f,q) for f in blocks]
    N=[cycle_numerator(f,e,q) for f,e in zip(blocks,eta)]
    oriented=[
        rem(sub(mul(N[0],B,q),scale(C,eta[0],q),q),A,q),
        rem(add(mul(N[2],D,q),scale(A,eta[2],q),q),C,q),
        rem(add(mul(N[1],A,q),scale(D,rho*eta[1],q),q),B,q),
        rem(sub(mul(N[3],C,q),scale(B,rho*eta[3],q),q),D,q),
    ]
    if any(oriented): raise AssertionError(f"Frobenius orientation equation failed: {oriented}")
    return {"q":q,"rho":rho,"eta":eta}

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("panel",type=Path)
    args=parser.parse_args()
    orbit_rows=[]; summaries={}
    for line in args.panel.read_text().splitlines():
        if not line.strip(): continue
        row=json.loads(line)
        if row["type"]=="orbit": orbit_rows.append(row)
        elif row["type"]=="summary": summaries[int(row["q"])]=row
    verified=defaultdict(list)
    for row in orbit_rows:
        result=verify_orbit(row); verified[result["q"]].append(result)
    for q,summary in summaries.items():
        rows=verified[q]
        if len(rows)!=int(summary["true_orbits"]): raise AssertionError(f"orbit count mismatch q={q}")
        if int(summary["incidences"]) != len(rows)*q*(q-1):
            raise AssertionError(f"AGL orbit count mismatch q={q}")
        rhos=Counter(r["rho"] for r in rows)
        inverses=Counter(pow(r["rho"],-1,q) for r in rows)
        if rhos != inverses: raise AssertionError(f"rho inversion symmetry failed q={q}")
    output={
        "status":"TFP3_TRUE_ORIENTATION_EXACT_PASS",
        "fields":sorted(summaries),
        "verified_orbits":sum(len(v) for v in verified.values()),
        "checks":[
            "prime-field and canonical affine gauge",
            "pairwise-distinct irreducible cubics",
            "four original inverse-free divisibilities",
            "Frobenius-Vandermonde cycle orientation",
            "q(q-1) affine orbit restoration",
            "rho -> rho^-1 transpose symmetry",
        ],
    }
    print(json.dumps(output,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
