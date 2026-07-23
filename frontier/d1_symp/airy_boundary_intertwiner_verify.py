#!/usr/bin/env python3
"""Symbolic verification of the Airy k=p near-intertwiner defect.

Let G_k act on q_i=X^(k-i)Y^i by

    G_k q_i = A (k-i) q_(i+1) + B i q_(i-1).

Let P: Sym^p -> det tensor Sym^(p-2) be the integral lift of the
characteristic-p quotient map, P(q_i)=i r_(i-1) for 1<=i<=p-1 and
P(q_0)=P(q_p)=0.  Then

    P G_p - G_(p-2) P = p A J + p(p-1) B E,

where J(q_i)=r_i for 0<=i<=p-2 and E(q_p)=r_(p-2).
"""
import sympy as sp

A, B = sp.symbols("A B")


def action_matrix(k):
    G = sp.zeros(k + 1, k + 1)
    for i in range(k + 1):
        if i + 1 <= k:
            G[i + 1, i] = A * (k - i)
        if i - 1 >= 0:
            G[i - 1, i] = B * i
    return G


def check(p):
    Gp = action_matrix(p)
    Gm = action_matrix(p - 2)

    P = sp.zeros(p - 1, p + 1)
    for i in range(1, p):
        P[i - 1, i] = i

    J = sp.zeros(p - 1, p + 1)
    for i in range(p - 1):
        J[i, i] = 1

    E = sp.zeros(p - 1, p + 1)
    E[p - 2, p] = 1

    defect = P * Gp - Gm * P
    expected = p * A * J + p * (p - 1) * B * E
    assert sp.simplify(defect - expected) == sp.zeros(p - 1, p + 1)
    assert J.rank() == p - 1
    print(f"p={p}: defect identity and full target rank: OK")


if __name__ == "__main__":
    for prime in (5, 7, 11, 13, 17, 23):
        check(prime)
    print("AIRY BOUNDARY NEAR-INTERTWINER VERIFIED")
