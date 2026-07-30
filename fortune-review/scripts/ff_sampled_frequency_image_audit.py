#!/usr/bin/env python3
"""Exact finite-field audit for the sampled-frequency image used by FFPR.

This verifier is independent of the Fable scripts.  It checks the exact map

    S -> mu_{P,S} = -theta * L^{-1} * S^{-1} (mod P)

for ordered distinct monic irreducibles P,S of the same degree k.  For fixed P
this map is injective; its inverse on the image is

    S (mod P) = -theta * L^{-1} * mu^{-1} (mod P).

Because P and S are both monic of degree k, S mod P = S-P.  Thus the sampled
frequencies are precisely an inverse image of the irreducible-translate set
{S-P}.  The script also verifies puncture covariance by unit dilation.

All assertions are exact over prime fields.  The output is a deterministic JSON
panel and makes no asymptotic claim.
"""
from __future__ import annotations

import itertools
import json
from typing import Dict, Iterable, List, Sequence, Tuple

Poly = Tuple[int, ...]


def trim(a: Sequence[int]) -> Poly:
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def padd(a: Poly, b: Poly, q: int) -> Poly:
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % q for i in range(n)])


def pneg(a: Poly, q: int) -> Poly:
    return tuple((-x) % q for x in a)


def psub(a: Poly, b: Poly, q: int) -> Poly:
    return padd(a, pneg(b, q), q)


def pmul(a: Poly, b: Poly, q: int) -> Poly:
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % q
    return trim(out)


def pmod(a: Poly, b: Poly, q: int) -> Poly:
    a = list(a)
    db = len(b) - 1
    inv_lead = pow(b[-1], q - 2, q)
    while a and len(a) - 1 >= db:
        coeff = a[-1] * inv_lead % q
        shift = len(a) - 1 - db
        for i, y in enumerate(b):
            a[shift + i] = (a[shift + i] - coeff * y) % q
        while a and a[-1] == 0:
            a.pop()
    return tuple(a)


def ppow(a: Poly, exponent: int, modulus: Poly, q: int) -> Poly:
    result, base = (1,), pmod(a, modulus, q)
    while exponent:
        if exponent & 1:
            result = pmod(pmul(result, base, q), modulus, q)
        base = pmod(pmul(base, base, q), modulus, q)
        exponent >>= 1
    return result


def pinv(a: Poly, modulus: Poly, q: int) -> Poly:
    assert a, "attempted to invert zero"
    return ppow(a, q ** (len(modulus) - 1) - 2, modulus, q)


def monics(degree: int, q: int) -> Iterable[Poly]:
    for low in itertools.product(range(q), repeat=degree):
        yield trim(list(low) + [1])


def irreducibles_upto(dmax: int, q: int) -> Dict[int, List[Poly]]:
    irreducibles: Dict[int, List[Poly]] = {d: [] for d in range(1, dmax + 1)}
    for degree in range(1, dmax + 1):
        for f in monics(degree, q):
            reducible = False
            for d in range(1, degree // 2 + 1):
                if any(not pmod(f, g, q) for g in irreducibles[d]):
                    reducible = True
                    break
            if not reducible:
                irreducibles[degree].append(f)
    return irreducibles


def primorial(q: int) -> Poly:
    # t^q - t
    return trim([0, q - 1] + [0] * (q - 2) + [1])


def control_puncture(q: int) -> Poly:
    # t(t+1)
    return pmul((0, 1), (1, 1), q)


def mu_value(P: Poly, S: Poly, L: Poly, theta: int, q: int) -> Poly:
    linv = pinv(pmod(L, P, q), P, q)
    sinv = pinv(pmod(S, P, q), P, q)
    return pmod(pmul(pmul(((-theta) % q,), linv, q), sinv, q), P, q)


def panel(q: int, k: int, theta: int = 1) -> dict:
    assert q > 2 and pow(theta, q - 1, q) == 1
    band = irreducibles_upto(k, q)[k]
    L1, L2 = primorial(q), control_puncture(q)
    qk = q ** k
    fixed_p_rows = []
    total_pairs = 0

    for P in band:
        linv1 = pinv(pmod(L1, P, q), P, q)
        dilation = pmod(pmul(pmod(L1, P, q), pinv(pmod(L2, P, q), P, q), q), P, q)
        seen: Dict[Poly, Poly] = {}
        for S in band:
            if S == P:
                continue
            total_pairs += 1
            mu1 = mu_value(P, S, L1, theta, q)
            mu2 = mu_value(P, S, L2, theta, q)
            assert mu1 and mu2
            assert mu1 not in seen, (q, k, P, S, seen[mu1])
            seen[mu1] = S

            # Exact inverse formula on the image.
            recovered = pmod(
                pmul(pmul(((-theta) % q,), linv1, q), pinv(mu1, P, q), q),
                P,
                q,
            )
            assert recovered == pmod(S, P, q)

            # Equal-degree monic translate identity: S mod P = S-P.
            assert pmod(S, P, q) == psub(S, P, q)

            # Changing the puncture dilates the sampled image by a unit.
            assert mu2 == pmod(pmul(mu1, dilation, q), P, q)

        fixed_p_rows.append({
            "P": list(P),
            "sample_size": len(seen),
            "unit_frequency_space_size": qk - 1,
            "density": len(seen) / (qk - 1),
        })

    expected_pairs = len(band) * (len(band) - 1)
    assert total_pairs == expected_pairs
    sample_sizes = {row["sample_size"] for row in fixed_p_rows}
    assert sample_sizes == {len(band) - 1}
    densities = [row["density"] for row in fixed_p_rows]
    return {
        "q": q,
        "k": k,
        "band_size": len(band),
        "ordered_pair_count": total_pairs,
        "sample_size_per_fixed_P": len(band) - 1,
        "unit_frequency_space_size": qk - 1,
        "sample_density": densities[0] if densities else 0.0,
        "injective_for_every_P": True,
        "inverse_formula_verified": True,
        "equal_degree_translate_verified": True,
        "puncture_unit_dilation_verified": True,
    }


def main() -> None:
    panels = [
        panel(3, 2),
        panel(5, 2),
        panel(7, 2),
        panel(3, 3),
        panel(5, 3),
        panel(3, 4),
    ]
    result = {
        "status": "MACHINE-VERIFIED IDENTITY / EMPIRICAL-EXACT FINITE PANEL",
        "theorem_checked": "fixed-P sampled-frequency injectivity, inverse translate formula, and puncture dilation",
        "asymptotic_claim": False,
        "panels": panels,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
