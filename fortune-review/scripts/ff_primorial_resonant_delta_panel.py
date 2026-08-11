#!/usr/bin/env python3
"""Exact finite Delta_PS audit on the characteristic-three resonant family.

This is a finite-panel Gate 3 diagnostic, not a uniform theorem. It computes
X_a=Ahat_P(mu)Ahat_S(nu), Delta_a, B_a=X_a-Delta_a and the literal cross
terms between a=(P,S) and its resonant partner b=(P',S') for k=3,4,5.
"""
from __future__ import annotations

import json
from collections import Counter
from ff_primorial_resonant_component import (
    generated_points,
    irreducibles_upto,
    local_parameter,
    padd,
    pinv,
    pmod,
    pmul,
    pneg,
    primorial,
)

q = 3
L = primorial()


def zadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def zsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def zmul(a, b):
    out = [0] * q
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i + j) % q] += x * y
    return tuple(out)


def zconj(a):
    return tuple(a[(-i) % q] for i in range(q))


def zscale(a, n):
    return tuple(n * x for x in a)


def zroot(exponent):
    out = [0] * q
    out[exponent % q] = 1
    return tuple(out)


def zcanon(a):
    final = a[-1]
    return tuple(x - final for x in a)


def coeff_top(x, P):
    k = len(P) - 1
    return x[k - 1] if len(x) >= k else 0


def lambda_sources(m):
    irr = irreducibles_upto(m, q)
    out = []
    for d in range(1, m + 1):
        if m % d:
            continue
        for P in irr[d]:
            f = (1,)
            for _ in range(m // d):
                f = pmul(f, P, q)
            out.append((f, d))
    return out


def ahat(P, mu, sources):
    out = (0, 0, 0)
    for f, weight in sources:
        exponent = coeff_top(pmod(pmul(mu, f, q), P, q), P)
        out = zadd(out, zscale(zroot(exponent), weight))
    return out


def pairing(theta, x, W):
    residue = pmod(pmul((theta,), x, q), W, q)
    exponent = residue[len(W) - 2] if len(residue) >= len(W) - 1 else 0
    return zroot(exponent)


def delta(P, S, sources, theta=1):
    W = pmul(P, S, q)
    SinvP = pinv(pmod(S, P, q), P, q)
    PinvS = pinv(pmod(P, S, q), S, q)
    LinvP = pinv(pmod(L, P, q), P, q)
    LinvS = pinv(pmod(L, S, q), S, q)
    eP = pmod(pmul(S, SinvP, q), W, q)
    eS = pmod(pmul(P, PinvS, q), W, q)
    v = pmod(padd(pmul(eP, LinvP, q), pmul(eS, LinvS, q), q), W, q)
    out = (0, 0, 0)
    for f, weight in sources:
        phase = pairing(theta, pneg(pmod(pmul(v, f, q), W, q), q), W)
        out = zadd(out, zscale(phase, weight * weight))
    return out


def pair_value(P, S, sources, theta=1):
    mu = local_parameter(P, S, L, theta)
    nu = local_parameter(S, P, L, theta)
    X = zmul(ahat(P, mu, sources), ahat(S, nu, sources))
    D = delta(P, S, sources, theta)
    return X, D, zsub(X, D)


def panel(k):
    m = 2 * k - 1
    sources = lambda_sources(m)
    _, rows = generated_points(k)
    cache = {}
    sums = {name: (0, 0, 0) for name in ("XX", "XD", "DX", "DD", "BB")}
    patterns = Counter()
    invariant = True
    for P, S, Pp, Sp, Q, epsilon, _ in rows:
        for pair in ((P, S), (Pp, Sp)):
            if pair not in cache:
                cache[pair] = pair_value(*pair, sources)
        X, D, B = cache[(P, S)]
        Xp, Dp, Bp = cache[(Pp, Sp)]
        invariant &= zcanon(X) == zcanon(Xp) and zcanon(D) == zcanon(Dp) and zcanon(B) == zcanon(Bp)
        terms = {
            "XX": zmul(X, zconj(Xp)),
            "XD": zmul(X, zconj(Dp)),
            "DX": zmul(D, zconj(Xp)),
            "DD": zmul(D, zconj(Dp)),
            "BB": zmul(B, zconj(Bp)),
        }
        for name, value in terms.items():
            sums[name] = zadd(sums[name], value)
        patterns[(epsilon, zcanon(X), zcanon(D), zcanon(B), zcanon(terms["BB"]))] += 1
    canonical = {name: list(zcanon(value)) for name, value in sums.items()}
    assert all(all(x == 0 for x in value[1:]) for value in canonical.values())
    target = q ** (2 * m + 3 * k)
    return {
        "q": q,
        "k": k,
        "m": m,
        "resonant_rows": len(rows),
        "source_terms": len(sources),
        "involution_pair_values_equal": invariant,
        "aggregate_terms_canonical": canonical,
        "corrected_BB_over_squared_target": canonical["BB"][0] / target,
        "distinct_pair_value_patterns": len(patterns),
        "max_corrected_pair_square": max(key[-1][0] for key in patterns),
    }


def main():
    result = {
        "status": "EMPIRICAL-EXACT FINITE PANEL",
        "panels": [panel(k) for k in (3, 4, 5)],
        "boundary": {
            "observed": "For every resonant row through k=5, X_a=X_b, Delta_a=Delta_b and B_a=B_b; the corrected cross term is a positive square.",
            "not_proved": "No uniform fixed-q growing-k bound for these corrected pair values is established.",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
