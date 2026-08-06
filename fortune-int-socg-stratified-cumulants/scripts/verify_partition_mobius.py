#!/usr/bin/env python3
"""Verify partition-lattice Möbius cancellation used by connected cumulants."""
import math

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

for k in range(1,10):
    coefficient_sum=sum(((-1)**(len(part)-1))*math.factorial(len(part)-1) for part in canonical_partitions(k))
    expected=1 if k==1 else 0
    assert coefficient_sum==expected,(k,coefficient_sum)
    print(f"order={k} partition_mobius_sum={coefficient_sum}")
print("FORTUNE_INT_SOCG_C3_PARTITION_MOBIUS_PASS")
