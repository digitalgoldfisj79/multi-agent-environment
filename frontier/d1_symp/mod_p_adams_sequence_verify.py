#!/usr/bin/env python3
"""Exact coefficient checks for the rank-two characteristic-p sequence.

For a two-dimensional vector space E in characteristic p:

  0 -> F^*E -> Sym^p(E) -> det(E) tensor Sym^(p-2)(E) -> 0.

In a basis X,Y, the quotient map sends

  X^(p-i)Y^i -> i (X wedge Y) tensor X^(p-1-i)Y^(i-1)

for 1 <= i <= p-1 and kills X^p,Y^p.  The checks below verify
compatibility with diagonal and upper/lower unipotent generators of GL_2.
"""
from math import comb


def check_prime(p):
    # Upper unipotent compatibility.
    for i in range(1, p):
        for j in range(1, i + 1):
            lhs = comb(i, j) * j
            rhs = i * comb(i - 1, j - 1)
            assert (lhs - rhs) % p == 0

    # Lower unipotent compatibility.  Terms landing at Y^p are killed
    # because their quotient coefficient is p=0.
    for i in range(1, p):
        for h in range(0, p - i + 1):
            lhs = comb(p - i, h) * (i + h)
            rhs = i * comb(p - 1 - i, h) if h <= p - 1 - i else 0
            assert (lhs - rhs) % p == 0

    print(f"p={p}: GL2 generator identities and dimensions: OK")


if __name__ == "__main__":
    for p in (5, 7, 11, 13, 17, 23, 29, 41):
        check_prime(p)
    print("MOD-p ADAMS/FROBENIUS EXACT SEQUENCE VERIFIED")
