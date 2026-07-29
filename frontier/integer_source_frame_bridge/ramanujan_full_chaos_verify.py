#!/usr/bin/env python3
"""Exact/finite audit for the next two Fortune levels.

Checks:
1. Ramanujan roughness projector and its coefficient/energy identities.
2. Exact rough-quotient interval representation through incomplete Ramanujan sums.
3. Exact CRT band-martingale telescoping and orthogonality.
4. Empirical reinsertion covariance on small complete Fortune panels.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import factorint, isprime, primerange, totient


def primorial(z: int) -> int:
    out = 1
    for p in primerange(2, z + 1):
        out *= int(p)
    return out


def divisors_squarefree(P: int) -> list[int]:
    divs = [1]
    for p in factorint(P):
        divs += [d * int(p) for d in list(divs)]
    return sorted(divs)


def mobius_squarefree_divisor(d: int) -> int:
    return -1 if len(factorint(d)) % 2 else 1


def ramanujan_sum(d: int, k: int) -> int:
    # c_d(k) = mu(d/g) phi(d) / phi(d/g), g=(d,k), valid generally.
    g = math.gcd(d, k)
    q = d // g
    fac = factorint(q)
    if any(e > 1 for e in fac.values()):
        return 0
    mu = -1 if len(fac) % 2 else 1
    return mu * int(totient(d)) // int(totient(q))


def projector_value(P: int, k: int) -> Fraction:
    phiP = int(totient(P))
    total = Fraction(0)
    for d in divisors_squarefree(P):
        total += Fraction(mobius_squarefree_divisor(d) * ramanujan_sum(d, k), int(totient(d)))
    return Fraction(phiP, P) * total


def interval_projector_count(P: int, Z: int, H: int, q: int) -> tuple[int, Fraction]:
    lo = (P + Z) // q + 1
    hi = (P + H) // q
    direct = sum(1 for k in range(lo, hi + 1) if math.gcd(k, P) == 1)
    phiP = int(totient(P))
    expanded = Fraction(0)
    for d in divisors_squarefree(P):
        C = sum(ramanujan_sum(d, k) for k in range(lo, hi + 1))
        expanded += Fraction(mobius_squarefree_divisor(d) * C, int(totient(d)))
    expanded *= Fraction(phiP, P)
    return direct, expanded


def ramanujan_projector_panel(z: int, Z: int, H: int) -> dict:
    P = primorial(z)
    divs = divisors_squarefree(P)
    phiP = int(totient(P))
    density = Fraction(phiP, P)

    for k in range(1, P + 1):
        assert projector_value(P, k) == (1 if math.gcd(k, P) == 1 else 0)

    l1 = sum((abs(Fraction(phiP * mobius_squarefree_divisor(d), P * int(totient(d)))) for d in divs), Fraction(0))
    qmass = sum((Fraction(phiP * phiP, P * P * int(totient(d))) for d in divs), Fraction(0))
    assert l1 == 1
    assert qmass == density

    # Complete-period Ramanujan orthogonality.
    for d in divs:
        for e in divs:
            avg = Fraction(sum(ramanujan_sum(d, k) * ramanujan_sum(e, k) for k in range(1, P + 1)), P)
            assert avg == (int(totient(d)) if d == e else 0)

    nontrivial_mass = qmass - density * density
    indicator_variance = Fraction(sum((Fraction(1 if math.gcd(k, P) == 1 else 0) - density) ** 2 for k in range(1, P + 1)), P)
    assert nontrivial_mass == indicator_variance == density * (1 - density)

    checked_moduli = 0
    interval_count_checksum = 0
    for q in primerange(Z + 1, H + 1):
        direct, expanded = interval_projector_count(P, Z, H, int(q))
        assert expanded.denominator == 1 and int(expanded) == direct
        checked_moduli += 1
        interval_count_checksum += direct

    return {
        "z": z,
        "Z": Z,
        "H": H,
        "P": P,
        "divisor_count": len(divs),
        "coefficient_l1": str(l1),
        "weighted_quadratic_mass": str(qmass),
        "rough_density": str(density),
        "nontrivial_complete_period_energy": str(nontrivial_mass),
        "checked_physical_moduli": checked_moduli,
        "interval_count_checksum": interval_count_checksum,
    }


def xi(r: int, hit: bool) -> Fraction:
    return Fraction(1, r - 2) - (Fraction(r - 1, r - 2) if hit else 0)


def band_martingale_panel() -> dict:
    P = 30
    local_primes = [7, 11, 13]
    bands = [[7, 11], [13]]
    W = math.prod(local_primes)
    units = [m for m in range(1, W + 1) if math.gcd(m, W) == 1]

    increments: list[list[Fraction]] = [[], []]
    finals: list[Fraction] = []
    for m in units:
        current = Fraction(1)
        band_values = []
        for band in bands:
            before = current
            for r in band:
                current *= 1 + xi(r, (P + m) % r == 0)
            band_values.append(current - before)
        direct = Fraction(1)
        for r in local_primes:
            direct *= 1 + xi(r, (P + m) % r == 0)
        assert current == direct
        assert sum(band_values, Fraction(0)) == direct - 1
        for idx, value in enumerate(band_values):
            increments[idx].append(value)
        finals.append(direct - 1)

    means = [sum(values, Fraction(0)) / len(units) for values in increments]
    assert means == [0, 0]
    cross = sum(a * b for a, b in zip(increments[0], increments[1])) / len(units)
    assert cross == 0
    qv = sum(sum(value * value for value in values) / len(units) for values in increments)
    final_energy = sum(value * value for value in finals) / len(units)
    assert qv == final_energy

    return {
        "P": P,
        "local_primes": local_primes,
        "bands": bands,
        "sample_size": len(units),
        "increment_means": [str(x) for x in means],
        "cross_band_covariance": str(cross),
        "quadratic_variation": str(qv),
        "final_energy": str(final_energy),
    }


def full_chaos_center(z: int, H: int) -> dict:
    P = primorial(z)
    Y = math.isqrt(P + H)
    local_primes = [int(r) for r in primerange(z + 1, Y + 1)]
    physical = [r for r in local_primes if r <= H]
    tail = [r for r in local_primes if r > H]
    logV = sum(math.log((r - 2) / (r - 1)) for r in local_primes)
    V = math.exp(logV)
    Aphys = sum(1 / (r - 2) for r in physical)
    Atail = sum(1 / (r - 2) for r in tail)
    candidates = [int(m) for m in primerange(z + 1, H + 1)]

    physical_first = 0.0
    tail_first = 0.0
    prime_pairs = 0
    max_cluster = 0
    for m in candidates:
        n = P + m
        prime_output = bool(isprime(n))
        if prime_output:
            prime_pairs += 1
            hits: list[int] = []
        else:
            hits = [int(r) for r in factorint(n) if z < r <= Y]
        max_cluster = max(max_cluster, len(hits))
        physical_hits = [r for r in hits if r <= H]
        tail_hits = [r for r in hits if r > H]
        physical_first += Aphys - sum((r - 1) / (r - 2) for r in physical_hits)
        tail_first += Atail - sum((r - 1) / (r - 2) for r in tail_hits)

    M = len(candidates)
    complete_residual = prime_pairs / V - M
    higher = complete_residual - physical_first - tail_first
    return {
        "z": z,
        "P": P,
        "Y": Y,
        "candidate_count": M,
        "V": V,
        "prime_pair_count": prime_pairs,
        "physical_first": physical_first,
        "tail_first": tail_first,
        "higher": higher,
        "complete_residual": complete_residual,
        "max_factor_cluster": max_cluster,
    }


def full_chaos_panel(X: int) -> dict:
    H = 4 * X * X // 5
    K = max(1, math.isqrt(X))
    centres = [full_chaos_center(int(z), H) for z in primerange(X, 2 * X)]
    blocks = []
    for start in range(0, len(centres), K):
        block = centres[start : start + K]
        p = [row["physical_first"] for row in block]
        t = [row["tail_first"] for row in block]
        h = [row["higher"] for row in block]
        full = [a + b + c for a, b, c in zip(p, t, h)]
        energy = lambda xs: sum(x * x for x in xs)
        dot2 = lambda xs, ys: 2 * sum(x * y for x, y in zip(xs, ys))
        ep = energy(p)
        ef = energy(full)
        blocks.append(
            {
                "start_index": start,
                "block_size": len(block),
                "physical_energy": ep,
                "tail_energy": energy(t),
                "higher_energy": energy(h),
                "complete_energy": ef,
                "twice_cov_physical_tail": dot2(p, t),
                "twice_cov_physical_higher": dot2(p, h),
                "twice_cov_tail_higher": dot2(t, h),
                "complete_to_physical_ratio": ef / ep if ep else None,
            }
        )
    return {
        "X": X,
        "H": H,
        "K": K,
        "centre_count": len(centres),
        "maximum_factor_cluster": max((row["max_factor_cluster"] for row in centres), default=0),
        "blocks": blocks,
    }


def main() -> None:
    payload = {
        "status": "PASS",
        "exact": {
            "ramanujan_projector_panels": [
                ramanujan_projector_panel(5, 7, 39),
                ramanujan_projector_panel(7, 11, 96),
            ],
            "band_martingale_panel": band_martingale_panel(),
        },
        "empirical": {
            "full_chaos_reinsertion_panels": [full_chaos_panel(X) for X in (7, 11, 13, 17)],
            "qualification": (
                "Finite full-chaos energies and covariance signs are diagnostics only. "
                "They show that reinsertion is not a monotone contraction; no asymptotic estimate is inferred."
            ),
        },
        "boundary": (
            "The exact Ramanujan projector removes the exponential coefficient-count loss, but a joint incomplete "
            "Ramanujan interval theorem is still open. Exact band-martingale reinsertion preserves Euler-cluster "
            "cancellation, but deterministic sampling of its increments is still open. Fortune remains open."
        ),
    }
    output = Path(__file__).with_name("ramanujan_full_chaos_results.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
