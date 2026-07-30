#!/usr/bin/env python3
"""Exact finite-panel discriminator for the FFPR sampled diagonal.

The script verifies:
  * fixed-P sampled-frequency injectivity through direct construction;
  * the projective-line occupancy lemma for k=2;
  * exact sampled mass, full Plancherel mass, source diagonal,
    distinct-source residue coincidences and signed residual;
  * the exact lower inequality obtained by summing over theta.

All polynomial and cyclotomic accumulations are exact over odd prime fields.
Floating-point evaluation is presentation-only for non-rational cyclotomic totals.
"""
from __future__ import annotations

import argparse
import cmath
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
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] = (out[i + j] + x * y) % q
    return trim(out)


def pmod(a: Poly, b: Poly, q: int) -> Poly:
    a = list(a)
    db = len(b) - 1
    inv = pow(b[-1], q - 2, q)
    while a and len(a) - 1 >= db:
        c = a[-1] * inv % q
        shift = len(a) - 1 - db
        if c:
            for i, y in enumerate(b):
                a[shift + i] = (a[shift + i] - c * y) % q
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
    assert a
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


def lambda_sources(m: int, q: int, irr: Dict[int, List[Poly]]) -> List[Tuple[Poly, int]]:
    out: List[Tuple[Poly, int]] = []
    for d in range(1, m + 1):
        if m % d:
            continue
        exponent = m // d
        for prime in irr[d]:
            f = (1,)
            for _ in range(exponent):
                f = pmul(f, prime, q)
            out.append((f, d))
    return out


def primorial(q: int) -> Poly:
    return trim([0, q - 1] + [0] * (q - 2) + [1])


def control_puncture(q: int) -> Poly:
    return pmul((0, 1), (1, 1), q)


def residue_coefficients(k: int, q: int) -> List[Tuple[int, ...]]:
    rows: List[Tuple[int, ...]] = []
    for index in range(q ** k):
        value = index
        coefficients = []
        for _ in range(k):
            coefficients.append(value % q)
            value //= q
        rows.append(tuple(coefficients))
    return rows


def poly_to_index(a: Poly, k: int, q: int) -> int:
    return sum((a[i] if i < len(a) else 0) * q ** i for i in range(k))


def bilinear_matrix(P: Poly, q: int) -> List[List[int]]:
    k = len(P) - 1
    basis = [tuple([0] * i + [1]) for i in range(k)]
    matrix = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            product = pmod(pmul(basis[i], basis[j], q), P, q)
            matrix[i][j] = product[k - 1] if len(product) >= k else 0
    return matrix


def phase_bins(mu: Poly, counts: List[int], residues: List[Tuple[int, ...]], B: List[List[int]], q: int) -> List[int]:
    k = len(B)
    mu_coeff = [(mu[i] if i < len(mu) else 0) for i in range(k)]
    functional = [sum(mu_coeff[i] * B[i][j] for i in range(k)) % q for j in range(k)]
    bins = [0] * q
    for count, residue in zip(counts, residues):
        if count:
            exponent = sum(functional[j] * residue[j] for j in range(k)) % q
            bins[exponent] += count
    return bins


def abs_square_vector(bins: List[int]) -> List[int]:
    q = len(bins)
    out = [0] * q
    for e, a in enumerate(bins):
        if not a:
            continue
        for f, b in enumerate(bins):
            if b:
                out[(e - f) % q] += a * b
    return out


def vector_add(a: List[int], b: List[int]) -> List[int]:
    return [x + y for x, y in zip(a, b)]


def vector_sub(a: List[int], b: List[int]) -> List[int]:
    return [x - y for x, y in zip(a, b)]


def canonical(vector: List[int]) -> List[int]:
    last = vector[-1]
    return [x - last for x in vector]


def evaluate(vector: List[int]) -> complex:
    q = len(vector)
    root = cmath.exp(2j * cmath.pi / q)
    return sum(value * root ** exponent for exponent, value in enumerate(vector))


def mu_value(P: Poly, S: Poly, L: Poly, theta: int, q: int) -> Poly:
    Linv = pinv(pmod(L, P, q), P, q)
    Sinv = pinv(pmod(S, P, q), P, q)
    return pmod(pmul(pmul(((-theta) % q,), Linv, q), Sinv, q), P, q)


def projective_key(a: Poly, k: int, q: int) -> Tuple[int, ...]:
    coefficients = [(a[i] if i < len(a) else 0) for i in range(k)]
    for coefficient in coefficients:
        if coefficient:
            inv = pow(coefficient, q - 2, q)
            return tuple(value * inv % q for value in coefficients)
    raise AssertionError("zero has no projective class")


def projective_occupancy_panel(q: int) -> dict:
    assert q % 2 == 1
    band = irreducibles_upto(2, q)[2]
    all_lines = {
        projective_key(trim(residue), 2, q)
        for residue in residue_coefficients(2, q)
        if any(residue)
    }
    expected_low = (q - 3) // 2
    expected_high = (q - 1) // 2
    histograms = set()
    for P in band:
        counts = {line: 0 for line in all_lines}
        for S in band:
            if S != P:
                counts[projective_key(psub(S, P, q), 2, q)] += 1
        histogram = tuple(sorted((value, list(counts.values()).count(value)) for value in set(counts.values())))
        assert min(counts.values()) == expected_low
        assert max(counts.values()) == expected_high
        assert list(counts.values()).count(expected_low) == (q + 1) // 2
        assert list(counts.values()).count(expected_high) == (q + 1) // 2
        histograms.add(histogram)
    assert len(histograms) == 1
    representative = {str(value): count for value, count in next(iter(histograms))}
    return {
        "q": q,
        "degree": 2,
        "degree_two_prime_count": len(band),
        "projective_line_count": q + 1,
        "minimum_occupancy": expected_low,
        "maximum_occupancy": expected_high,
        "lines_at_each_occupancy": (q + 1) // 2,
        "common_occupancy_histogram": representative,
        "verified_for_every_P": True,
    }


def sampled_mass_panel(q: int, k: int, puncture_name: str = "primorial", all_theta: bool = True) -> dict:
    m = 2 * k - 1
    irr = irreducibles_upto(m, q)
    band = irr[k]
    sources = lambda_sources(m, q, irr)
    L = primorial(q) if puncture_name == "primorial" else control_puncture(q)
    residues = residue_coefficients(k, q)
    thetas = list(range(1, q)) if all_theta else [1]
    totals = {theta: [0] * q for theta in thetas}
    full_mass = 0
    distinct_residue_collision = 0
    sum_lambda_square = sum(weight * weight for _, weight in sources)

    for P in band:
        counts = [0] * (q ** k)
        for f, weight in sources:
            counts[poly_to_index(pmod(f, P, q), k, q)] += weight
        count_square_sum = sum(value * value for value in counts)
        full_mass += q ** k * count_square_sum - q ** (2 * m)
        distinct_residue_collision += (len(band) - 1) * (count_square_sum - sum_lambda_square)
        B = bilinear_matrix(P, q)
        needed: Dict[int, Poly] = {}
        pair_indices: Dict[Tuple[Poly, int], int] = {}
        for S in band:
            if S == P:
                continue
            for theta in thetas:
                mu = mu_value(P, S, L, theta, q)
                index = poly_to_index(mu, k, q)
                needed[index] = mu
                pair_indices[(S, theta)] = index
        squares = {
            index: abs_square_vector(phase_bins(mu, counts, residues, B, q))
            for index, mu in needed.items()
        }
        for (S, theta), index in pair_indices.items():
            totals[theta] = vector_add(totals[theta], squares[index])

    ordered_pairs = len(band) * (len(band) - 1)
    source_diagonal = ordered_pairs * sum_lambda_square
    density = (len(band) - 1) / (q ** k - 1)
    theta_rows = []
    for theta in thetas:
        raw = totals[theta]
        value = evaluate(raw)
        diagonal_vector = [source_diagonal] + [0] * (q - 1)
        collision_vector = [distinct_residue_collision] + [0] * (q - 1)
        residual = vector_sub(vector_sub(raw, diagonal_vector), collision_vector)
        theta_rows.append({
            "theta": theta,
            "M_samp_cyclotomic_canonical": canonical(raw),
            "M_samp_real": value.real,
            "M_samp_imaginary_abs": abs(value.imag),
            "M_samp_over_q_3k": value.real / q ** (3 * k),
            "M_samp_over_q_m_plus_2k": value.real / q ** (m + 2 * k),
            "M_samp_over_M_full": value.real / full_mass,
            "energy_enrichment_over_density": (value.real / full_mass) / density,
            "signed_residual_cyclotomic_canonical": canonical(residual),
            "signed_residual_real": evaluate(residual).real,
        })
    sum_theta = sum(row["M_samp_real"] for row in theta_rows)
    result = {
        "q": q,
        "k": k,
        "m": m,
        "puncture": puncture_name,
        "band_size": len(band),
        "ordered_prime_pairs": ordered_pairs,
        "source_terms": len(sources),
        "M_full": full_mass,
        "sample_density": density,
        "source_diagonal": source_diagonal,
        "distinct_source_residue_coincidence": distinct_residue_collision,
        "theta_rows": theta_rows,
    }
    if k == 2 and all_theta:
        lower = (q - 3) / 2 * full_mass
        assert sum_theta + 1e-6 >= lower
        result["projective_occupancy_lower_bound"] = lower
        result["sum_theta_M_samp"] = sum_theta
        result["lower_bound_verified"] = True
        result["max_theta_over_q_6"] = max(row["M_samp_real"] for row in theta_rows) / q ** 6
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()

    ci_parameters = [(3, 2), (5, 2), (7, 2), (11, 2), (3, 3), (5, 3), (3, 4)]
    true_panels = [sampled_mass_panel(q, k) for q, k in ci_parameters]
    control_panels = [sampled_mass_panel(q, k, "control") for q, k in [(3, 2), (5, 2), (7, 2)]]
    extended = []
    if args.extended:
        for q, k in [(13, 2), (17, 2), (19, 2), (23, 2), (3, 5), (5, 4)]:
            extended.append(sampled_mass_panel(q, k, all_theta=False))

    result = {
        "status": {
            "projective_occupancy": "MACHINE-VERIFIED IDENTITY",
            "sampled_mass_panels": "EMPIRICAL-EXACT FINITE PANEL",
            "asymptotic_route_A_closure": "PROVED FROM PUBLISHED INPUT plus exact occupancy lemma",
        },
        "theorem_boundary": {
            "proved": "For k=2,m=3, averaging over nonzero theta samples every local projective line with multiplicity at least (q-3)/2. Combined with Keating-Rudnick Theorem 2.2(ii), max_theta M_samp(theta) >= (1/4+o(1))q^7 as q tends to infinity.",
            "consequence": "The uniform Route A target M_samp(theta) << q^(3k) poly(k,m) is false.",
            "not_proved": "The endpoint FFPR target is not falsified; Route B remains open.",
        },
        "projective_occupancy": [projective_occupancy_panel(q) for q in (3, 5, 7, 11)],
        "true_primorial_panels": true_panels,
        "control_puncture_panels": control_panels,
        "extended_theta_1_panels": extended,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
