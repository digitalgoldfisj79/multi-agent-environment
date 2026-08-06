#!/usr/bin/env python3
"""Exact rational regression for equality-pattern decomposition of ordinary cumulants."""
from __future__ import annotations
import itertools
import math
import random
from fractions import Fraction

def partitions(items):
    if not items:
        yield ()
        return
    first=items[0]
    for rest in partitions(items[1:]):
        yield ((first,),)+rest
        for i,block in enumerate(rest):
            yield rest[:i]+(tuple(sorted((first,)+block)),)+rest[i+1:]

def canonical_partitions(k):
    seen=set()
    for part in partitions(tuple(range(k))):
        key=tuple(sorted((tuple(sorted(b)) for b in part),key=lambda b:b[0]))
        if key not in seen:
            seen.add(key)
            yield key

def moment(matrix,cols):
    return Fraction(sum(math.prod(row[c] for c in cols) for row in matrix),len(matrix))

def joint_cumulant(matrix,cols):
    total=Fraction(0)
    for part in canonical_partitions(len(cols)):
        coeff=Fraction(((-1)**(len(part)-1))*math.factorial(len(part)-1))
        product=Fraction(1)
        for block in part:
            product*=moment(matrix,tuple(cols[i] for i in block))
        total+=coeff*product
    return total

def scalar_cumulant(values,k):
    total=Fraction(0)
    for part in canonical_partitions(k):
        coeff=Fraction(((-1)**(len(part)-1))*math.factorial(len(part)-1))
        product=Fraction(1)
        for block in part:
            power=len(block)
            product*=Fraction(sum(v**power for v in values),len(values))
        total+=coeff*product
    return total

rng=random.Random(560805)
for rows,cols,max_order in ((7,5,4),(9,6,5),(11,7,5)):
    matrix=[[rng.randrange(2) for _ in range(cols)] for _ in range(rows)]
    occupancies=[sum(row) for row in matrix]
    for k in range(1,max_order+1):
        grouped=Fraction(0)
        pattern_count=0
        for part in canonical_partitions(k):
            block_order=tuple(sorted(part,key=lambda b:b[0]))
            for assigned in itertools.permutations(range(cols),len(block_order)):
                tuple_cols=[0]*k
                for block_index,block in enumerate(block_order):
                    for position in block:
                        tuple_cols[position]=assigned[block_index]
                grouped+=joint_cumulant(matrix,tuple(tuple_cols))
            pattern_count+=1
        direct=scalar_cumulant(occupancies,k)
        assert grouped==direct,(rows,cols,k,grouped,direct)
        print(f"rows={rows} cols={cols} order={k} equality_patterns={pattern_count} cumulant={direct}")
print("FORTUNE_INT_SOCG_C3_EQUALITY_PATTERN_PASS")
