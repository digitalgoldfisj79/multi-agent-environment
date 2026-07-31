#!/usr/bin/env python3
"""Exact Gate-0 audit for the nonzero-defect orbit programme.

Checks on the literal q=11,k=3 counterexample:
  * the four bounded-degree Frobenius-root equations in quotient fields;
  * exact AGL(1,q) covariance of incidence parameters lambda,rho;
  * exact covariance law for the common defect polynomial;
  * existence and uniqueness of the canonical gauge lambda=1 and tr(P)=0.

Coefficients are stored low-to-high over F_q. No floating point is used.
"""
from __future__ import annotations
import json
from typing import Iterable

Q = 11
K = 3
Poly = tuple[int, ...]


def trim(a: Iterable[int]) -> Poly:
    out = [x % Q for x in a]
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(a: Poly, b: Poly) -> Poly:
    n = max(len(a), len(b))
    return trim((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n))


def neg(a: Poly) -> Poly:
    return trim(-x for x in a)


def sub(a: Poly, b: Poly) -> Poly:
    return add(a, neg(b))


def scale(a: Poly, c: int) -> Poly:
    return trim(c * x for x in a)


def mul(a: Poly, b: Poly) -> Poly:
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % Q
    return trim(out)


def divmod_poly(a: Poly, b: Poly) -> tuple[Poly, Poly]:
    aa = list(trim(a))
    bb = trim(b)
    if not bb:
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [0] * max(1, len(aa) - len(bb) + 1)
    inv = pow(bb[-1], Q - 2, Q)
    while aa and len(aa) >= len(bb):
        c = aa[-1] * inv % Q
        shift = len(aa) - len(bb)
        quotient[shift] = c
        for i, y in enumerate(bb):
            aa[shift + i] = (aa[shift + i] - c * y) % Q
        while aa and aa[-1] == 0:
            aa.pop()
    return trim(quotient), tuple(aa)


def mod(a: Poly, modulus: Poly) -> Poly:
    return divmod_poly(a, modulus)[1]


def exact_div(a: Poly, b: Poly) -> Poly:
    quotient, remainder = divmod_poly(a, b)
    if remainder:
        raise AssertionError((a, b, remainder))
    return quotient


def powmod(a: Poly, exponent: int, modulus: Poly) -> Poly:
    result, base = (1,), mod(a, modulus)
    while exponent:
        if exponent & 1:
            result = mod(mul(result, base), modulus)
        base = mod(mul(base, base), modulus)
        exponent >>= 1
    return result


def compose_linear(f: Poly, a: int, b: int) -> Poly:
    """Return f(a*t+b)."""
    x = (b % Q, a % Q)
    out: Poly = ()
    for coefficient in reversed(f):
        out = add(mul(out, x), (coefficient,))
    return out


def root_transform(f: Poly, a: int, b: int) -> Poly:
    """Monic polynomial whose roots are a*r+b for roots r of monic f."""
    degree = len(f) - 1
    inva = pow(a, Q - 2, Q)
    transformed = compose_linear(f, inva, (-b * inva) % Q)
    return scale(transformed, pow(a, degree, Q))


def quotient_transform(f: Poly, a: int, b: int) -> Poly:
    """Transformation law for the monic degree-q quotient A,B,C,D."""
    inva = pow(a, Q - 2, Q)
    return scale(compose_linear(f, inva, (-b * inva) % Q), a)


def defect_transform(h: Poly, a: int, b: int) -> Poly:
    inva = pow(a, Q - 2, Q)
    return scale(compose_linear(h, inva, (-b * inva) % Q), pow(a, 2 - 2 * K, Q))


def quotient_system(P: Poly, S: Poly, Pp: Poly, Sp: Poly, lam: int, rho: int, L: Poly):
    A = exact_div(sub(mul(L, S), scale(Pp, lam)), P)
    B = exact_div(add(mul(L, P), scale(Sp, rho)), S)
    C = exact_div(add(mul(L, Sp), scale(P, lam)), Pp)
    D = exact_div(sub(mul(L, Pp), scale(S, rho)), Sp)
    h1 = exact_div(sub(scale(C, rho), scale(B, lam)), mul(P, Sp))
    h2 = exact_div(sub(scale(A, rho), scale(D, lam)), mul(S, Pp))
    assert h1 == h2
    return A, B, C, D, h1


def trace_coefficient(P: Poly) -> int:
    return P[-2] if len(P) >= 2 else 0


L = trim([0, -1] + [0] * 9 + [1])
P = (1, 0, 4, 1)
S = (1, 9, 10, 1)
Pp = (7, 6, 10, 1)
Sp = (10, 3, 4, 1)
lam, rho = 5, 7
A, B, C, D, h = quotient_system(P, S, Pp, Sp, lam, rho, L)

# Bounded-degree Frobenius-root equations. In F_q[t]/P, t^q-t is the
# difference between a root and its Frobenius successor; all polynomial
# products below have degree bounded in k after this substitution.
x = (0, 1)
root_equations = []
for modulus, lhs_factors, scalar, rhs_poly, sign in [
    (P, (S,), lam, Pp, 1),
    (Pp, (Sp,), lam, P, -1),
    (S, (P,), rho, Sp, -1),
    (Sp, (Pp,), rho, S, 1),
]:
    frob_difference = sub(powmod(x, Q, modulus), x)
    left = frob_difference
    for factor in lhs_factors:
        left = mod(mul(left, factor), modulus)
    right = mod(scale(rhs_poly, sign * scalar), modulus)
    assert left == right
    assert powmod(x, Q ** K, modulus) == x
    assert powmod(x, Q, modulus) != x
    root_equations.append({"modulus": list(modulus), "left": list(left), "right": list(right)})

# AGL covariance and defect law on every affine transformation.
checks = 0
for a in range(1, Q):
    for b in range(Q):
        Pt = root_transform(P, a, b)
        St = root_transform(S, a, b)
        Ppt = root_transform(Pp, a, b)
        Spt = root_transform(Sp, a, b)
        lamt, rhot = a * lam % Q, a * rho % Q
        At, Bt, Ct, Dt, ht = quotient_system(Pt, St, Ppt, Spt, lamt, rhot, L)
        assert At == quotient_transform(A, a, b)
        assert Bt == quotient_transform(B, a, b)
        assert Ct == quotient_transform(C, a, b)
        assert Dt == quotient_transform(D, a, b)
        assert ht == defect_transform(h, a, b)
        checks += 1

# Canonical gauge: lambda'=1 and t^(k-1) coefficient of P' equals zero.
# Under roots r -> a*r+b, p_(k-1) transforms as a*p_(k-1)-k*b.
a0 = pow(lam, Q - 2, Q)
b0 = a0 * trace_coefficient(P) * pow(K, Q - 2, Q) % Q
Pg = root_transform(P, a0, b0)
Sg = root_transform(S, a0, b0)
Ppg = root_transform(Pp, a0, b0)
Spg = root_transform(Sp, a0, b0)
lamg, rhog = a0 * lam % Q, a0 * rho % Q
Ag, Bg, Cg, Dg, hg = quotient_system(Pg, Sg, Ppg, Spg, lamg, rhog, L)
assert lamg == 1
assert trace_coefficient(Pg) == 0

unique = []
for a in range(1, Q):
    for b in range(Q):
        if a * lam % Q == 1 and trace_coefficient(root_transform(P, a, b)) == 0:
            unique.append((a, b))
assert unique == [(a0, b0)]

result = {
    "status": "MACHINE-VERIFIED IDENTITY",
    "q": Q,
    "k": K,
    "root_equations_checked": len(root_equations),
    "agl_transformations_checked": checks,
    "original": {
        "lambda": lam,
        "rho": rho,
        "defect": list(h),
        "defect_degree": len(h) - 1,
    },
    "canonical_gauge": {
        "a": a0,
        "b": b0,
        "lambda": lamg,
        "rho": rhog,
        "P": list(Pg),
        "S": list(Sg),
        "P_prime": list(Ppg),
        "S_prime": list(Spg),
        "defect": list(hg),
        "unique": True,
    },
    "proved_target_not_claimed": "The audit verifies exact identities on the explicit orbit; it does not prove zero-dimensionality or a uniform orbit bound.",
}
print(json.dumps(result, indent=2, sort_keys=True))
