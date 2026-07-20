#!/usr/bin/env python3
"""Validate the cumulative Mobius-degree detector identity."""
from math import comb

def lhs(s: int, k: int) -> int:
    return sum((-1)**j * comb(s,j) for j in range(min(k,s)+1))

def rhs(s: int, k: int) -> int:
    if s == 0: return 1
    if 1 <= s <= k: return 0
    return (-1)**k * comb(s-1,k)

def main() -> None:
    for s in range(0,80):
        for k in range(0,30):
            assert lhs(s,k)==rhs(s,k),(s,k,lhs(s,k),rhs(s,k))
    print("MOBIUS_DEGREE_IDENTITY_PASS cases=2400")

if __name__ == "__main__":
    main()
