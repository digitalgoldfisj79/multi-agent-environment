#!/usr/bin/env python3
"""Exact independent verifier for the first large-field bilateral counterexample.

No code is imported from the Fable branch or from the existing FF endpoint
verifiers. Coefficients are stored low-to-high over F_11.
"""
from __future__ import annotations

Q = 11
Poly = tuple[int, ...]


def trim(a):
    a = [x % Q for x in a]
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a: Poly, b: Poly) -> Poly:
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def neg(a: Poly) -> Poly:
    return tuple((-x) % Q for x in a)


def sub(a: Poly, b: Poly) -> Poly:
    return add(a, neg(b))


def scale(a: Poly, c: int) -> Poly:
    return trim([c * x for x in a])


def mul(a: Poly, b: Poly) -> Poly:
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % Q
    return trim(out)


def divmod_poly(a: Poly, b: Poly) -> tuple[Poly, Poly]:
    a = list(a)
    out = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], Q - 2, Q)
    while a and len(a) >= len(b):
        c = a[-1] * inv % Q
        shift = len(a) - len(b)
        out[shift] = c
        for i, y in enumerate(b):
            a[shift + i] = (a[shift + i] - c * y) % Q
        while a and a[-1] == 0:
            a.pop()
    return trim(out), tuple(a)


def mod(a: Poly, b: Poly) -> Poly:
    return divmod_poly(a, b)[1]


def powmod(a: Poly, n: int, modulus: Poly) -> Poly:
    result, base = (1,), mod(a, modulus)
    while n:
        if n & 1:
            result = mod(mul(result, base), modulus)
        base = mod(mul(base, base), modulus)
        n >>= 1
    return result


def invmod(a: Poly, modulus: Poly) -> Poly:
    assert a
    return powmod(a, Q ** (len(modulus) - 1) - 2, modulus)


def exact_div(a: Poly, b: Poly) -> Poly:
    quotient, remainder = divmod_poly(a, b)
    assert not remainder, (a, b, remainder)
    return quotient


def irreducible_cubic(f: Poly) -> bool:
    assert len(f) == 4 and f[-1] == 1
    for x in range(Q):
        value = 0
        for coefficient in reversed(f):
            value = (value * x + coefficient) % Q
        if value == 0:
            return False
    return True


def local_frequency(P: Poly, S: Poly, L: Poly) -> Poly:
    return scale(invmod(mod(mul(L, S), P), P), -1)


L = trim([0, -1] + [0] * 9 + [1])  # t^11-t
P = (1, 0, 4, 1)
S = (1, 9, 10, 1)
Pp = (7, 6, 10, 1)
Sp = (10, 3, 4, 1)
c, d, theta = 2, 8, 1
lam = (-theta * pow(c, Q - 2, Q)) % Q
rho = (theta * pow(d, Q - 2, Q)) % Q

assert all(irreducible_cubic(f) for f in (P, S, Pp, Sp))
assert len({P, S, Pp, Sp}) == 4
assert (c + d) % Q == 10
assert lam == 5 and rho == 7 and lam != rho

# Four inverse-free incidence conditions.
assert not mod(sub(mul(L, S), scale(Pp, lam)), P)
assert not mod(add(mul(L, Sp), scale(P, lam)), Pp)
assert not mod(add(mul(L, P), scale(Sp, rho)), S)
assert not mod(sub(mul(L, Pp), scale(S, rho)), Sp)

# Original local-frequency definition, without using the correspondence theorem.
mu_a = local_frequency(P, S, L)
mu_b = local_frequency(Pp, Sp, L)
nu_a = local_frequency(S, P, L)
nu_b = local_frequency(Sp, Pp, L)
E_mu = sub(mul(mu_a, Pp), mul(mu_b, P))
E_nu = sub(mul(nu_a, Sp), mul(nu_b, S))
assert E_mu == (c,)
assert E_nu == (d,)

# Degree-q quotient system and the common nonzero defect.
A = exact_div(sub(mul(L, S), scale(Pp, lam)), P)
B = exact_div(add(mul(L, P), scale(Sp, rho)), S)
C = exact_div(add(mul(L, Sp), scale(P, lam)), Pp)
D = exact_div(sub(mul(L, Pp), scale(S, rho)), Sp)
F = sub(scale(C, rho), scale(B, lam))
G = sub(scale(A, rho), scale(D, lam))
h1 = exact_div(F, mul(P, Sp))
h2 = exact_div(G, mul(S, Pp))
assert h1 == h2
h = h1
assert h == (4, 6, 6, 0, 5, 2)  # 2t^5+5t^4+6t^2+6t+4
assert len(h) - 1 == Q - 2 * 3

lhs = mul(h, mul(mul(P, Pp), mul(S, Sp)))
rhs = add(
    mul(L, sub(scale(mul(S, Sp), rho), scale(mul(P, Pp), lam))),
    scale(sub(mul(P, S), mul(Pp, Sp)), lam * rho),
)
assert lhs == rhs

print("PASS explicit q=11,k=3 cross-distinct incidence")
print(f"c={c} d={d} c_plus_d={(c+d)%Q} lambda={lam} rho={rho}")
print(f"mu_a={mu_a} mu_b={mu_b} nu_a={nu_a} nu_b={nu_b}")
print(f"E_mu={E_mu} E_nu={E_nu}")
print(f"defect_h={h} degree={len(h)-1}")
print("PASS original-frequency, inverse-free, quotient-defect, and product identities")
