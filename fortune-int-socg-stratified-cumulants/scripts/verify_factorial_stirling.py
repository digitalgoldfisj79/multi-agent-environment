#!/usr/bin/env python3
"""Exact regression for the correct factorial-to-ordinary cumulant transform.

This does NOT identify factorial cumulants with ordinary joint cumulants over
globally distinct columns. It uses only the scalar generating-function identity
K_ord(t)=K_fac(exp(t)-1).
"""
from __future__ import annotations
from fractions import Fraction
import math
import random

def stirling2(n: int, k: int) -> int:
    table=[[0]*(k+1) for _ in range(n+1)]
    table[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            table[i][j]=table[i-1][j-1]+j*table[i-1][j]
    return table[n][k]

def set_partitions(n: int):
    if n == 0:
        yield []
        return
    blocks=[]
    def rec(i):
        if i==n:
            yield [tuple(b) for b in blocks]
            return
        for b in blocks:
            b.append(i)
            yield from rec(i+1)
            b.pop()
        blocks.append([i])
        yield from rec(i+1)
        blocks.pop()
    yield from rec(0)

def ordinary_cumulant(values,k):
    total=Fraction(0)
    for pi in set_partitions(k):
        coeff=Fraction(((-1)**(len(pi)-1))*math.factorial(len(pi)-1))
        term=Fraction(1)
        for block in pi:
            power=len(block)
            term*=Fraction(sum(v**power for v in values),len(values))
        total+=coeff*term
    return total

def falling(z,r):
    out=1
    for i in range(r):
        out*=z-i
    return out

def factorial_cumulants(values,max_order):
    fm=[Fraction(1)]
    for r in range(1,max_order+1):
        fm.append(Fraction(sum(falling(v,r) for v in values),len(values)))
    out=[Fraction(0)]
    for k in range(1,max_order+1):
        total=Fraction(0)
        for pi in set_partitions(k):
            coeff=Fraction(((-1)**(len(pi)-1))*math.factorial(len(pi)-1))
            term=Fraction(1)
            for block in pi:
                term*=fm[len(block)]
            total+=coeff*term
        out.append(total)
    return out

panels=[[0,1,1,2,3,5,8],[1,1,2,2,4,4,7,9],[0,0,1,3,3,6,10,10,12]]
rng=random.Random(20260805)
for _ in range(4):
    panels.append([rng.randrange(0,12) for _ in range(rng.randrange(7,13))])
for values in panels:
    max_order=min(8,len(values))
    fac=factorial_cumulants(values,max_order)
    for k in range(1,max_order+1):
        transformed=sum(Fraction(stirling2(k,r))*fac[r] for r in range(1,k+1))
        direct=ordinary_cumulant(values,k)
        assert transformed==direct,(values,k,transformed,direct)
    print(f"rows={len(values)} max_order={max_order} transform=exact")

# Coefficientwise ordered-partition bound:
# r! S(k,r) <= k! binom(k-1,r-1), hence
# sum_r S(k,r) r! D^(r-1) <= k! (D+1)^(k-1) for every real D>=0.
for d_num,d_den in [(0,1),(1,10),(1,1),(2,1),(10,1),(100,1)]:
    D=Fraction(d_num,d_den)
    for k in range(1,25):
        lhs=Fraction(0)
        for r in range(1,k+1):
            power=Fraction(1) if r==1 else D**(r-1)
            lhs+=stirling2(k,r)*math.factorial(r)*power
            assert math.factorial(r)*stirling2(k,r)<=math.factorial(k)*math.comb(k-1,r-1)
        rhs=math.factorial(k)*(D+1)**(k-1)
        assert lhs<=rhs,(D,k,lhs,rhs)
    print(f"D={D} radius_shift_bound=passed_through_24")
print("FORTUNE_INT_SOCG_C3_FACTORIAL_STIRLING_PASS")
