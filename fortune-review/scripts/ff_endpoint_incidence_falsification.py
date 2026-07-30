#!/usr/bin/env python3
"""Expanded exact falsification panel for bilateral endpoint incidence.

Imports only the independent arithmetic engine committed alongside this file.
It tests whether simultaneous completion in both source variables collapses to
only diagonal/transpose incidences. The q=3,k=4 panel falsifies that naive
universal conjecture and classifies its 12 non-diagonal exceptions into affine
orbits.
"""
from __future__ import annotations
import json
from ff_endpoint_centered_dispersion_audit import (
    degree, irreducibles_upto, padd, pinv, pmod, pmul, pneg, primorial, psub,
)


def affine(T, lam, a, q):
    x = (a, lam)
    out = ()
    for c in reversed(T):
        out = padd(pmul(out, x, q), (c,), q)
    inv = pow(pow(lam, len(T) - 1, q), q - 2, q)
    return tuple((z * inv) % q for z in out)


def pair_geometry(q, k, theta=(1,)):
    band = irreducibles_upto(k, q)[k]
    L = primorial(q)
    pairs = []
    for P in band:
        LinvP = pinv(pmod(L, P, q), P, q)
        for S in band:
            if S == P:
                continue
            SinvP = pinv(pmod(S, P, q), P, q)
            PinvS = pinv(pmod(P, S, q), S, q)
            LinvS = pinv(pmod(L, S, q), S, q)
            mu = pmod(pmul(pmul(pneg(theta, q), LinvP, q), SinvP, q), P, q)
            nu = pmod(pmul(pmul(pneg(theta, q), LinvS, q), PinvS, q), S, q)
            pairs.append((P, S, mu, nu))
    return pairs


def panel(q, k):
    m = 2 * k - 1
    pairs = pair_geometry(q, k)
    source_1 = source_2 = simultaneous = diagonal = transpose = other = 0
    exceptions = []
    for P, S, mu, nu in pairs:
        for Pp, Sp, mup, nup in pairs:
            c2 = degree(psub(pmul(nu, Sp, q), pmul(nup, S, q), q)) <= 0
            c1 = degree(psub(pmul(mu, Pp, q), pmul(mup, P, q), q)) <= 0
            source_1 += int(c1)
            source_2 += int(c2)
            if not (c1 and c2):
                continue
            simultaneous += 1
            if (P, S) == (Pp, Sp):
                diagonal += 1
            elif (P, S) == (Sp, Pp):
                transpose += 1
            else:
                other += 1
                exceptions.append((P, S, Pp, Sp))

    group = [(lam, a) for lam in range(1, q) for a in range(q)]
    exception_set = set(exceptions)
    seen = set()
    orbit_sizes = []
    orbit_representatives = []
    for exc in sorted(exception_set):
        if exc in seen:
            continue
        orbit = {
            tuple(affine(T, lam, a, q) for T in exc)
            for lam, a in group
        } & exception_set
        seen |= orbit
        orbit_sizes.append(len(orbit))
        orbit_representatives.append([list(T) for T in min(orbit)])
    assert len(seen) == len(exception_set)

    return {
        "q": q,
        "k": k,
        "m": m,
        "ordered_prime_pairs": len(pairs),
        "source_1_incidences": source_1,
        "source_2_incidences": source_2,
        "simultaneous_incidences": simultaneous,
        "diagonal": diagonal,
        "transpose": transpose,
        "other": other,
        "exception_affine_orbit_sizes": sorted(orbit_sizes),
        "exception_affine_orbit_representatives": orbit_representatives,
    }


def main():
    result = {
        "status": "EMPIRICAL-EXACT FINITE PANEL",
        "falsified_claim": "simultaneous endpoint incidence is universally diagonal or diagonal-plus-transpose",
        "panels": [panel(5, 3), panel(3, 4)],
        "conclusion": "The q=3,k=4 panel has 12 genuine non-diagonal, non-transpose incidences in two AGL(1,3)-orbits of size 6. General CBEA_FF must classify and bound exceptional components rather than assume diagonal rigidity.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
