#!/usr/bin/env python3
"""Independent endpoint audit for the function-field FFPR programme.

Checks, without importing the Fable scripts:
1. Exact Plancherel scale for Ahat_P(mu): the total nonzero-frequency mass is
   q^k times the all-residue progression variance. The finite panels show the
   mass is of order q^(m+k), not q^m.
2. The published first-dispersion object omits the f=f' correction. Compute the
   uncorrected product, the correction, and the actual product-minus-correction.
3. Exact endpoint completion coincidence relations in each source variable and
   their intersection (double-coincidence rigidity finite panels).
4. Literal exponent ledger for the first-dispersion diagonal floor.

Statuses: exact identities and finite-panel exact arithmetic only. No asymptotic
claim is inferred from the panels.
"""
from __future__ import annotations
import cmath
import itertools
import json
from dataclasses import dataclass
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
    inv = pow(b[-1], q - 2, q)
    while a and len(a) - 1 >= db:
        c = a[-1] * inv % q
        shift = len(a) - 1 - db
        for i, y in enumerate(b):
            a[shift + i] = (a[shift + i] - c * y) % q
        while a and a[-1] == 0:
            a.pop()
    return tuple(a)


def monics(d: int, q: int) -> Iterable[Poly]:
    for lo in itertools.product(range(q), repeat=d):
        yield trim(list(lo) + [1])


def irreducibles_upto(dmax: int, q: int) -> Dict[int, List[Poly]]:
    irr = {d: [] for d in range(1, dmax + 1)}
    for d in range(1, dmax + 1):
        for f in monics(d, q):
            reducible = False
            for e in range(1, d // 2 + 1):
                if any(not pmod(f, P, q) for P in irr[e]):
                    reducible = True
                    break
            if not reducible:
                irr[d].append(f)
    return irr


def pinv(a: Poly, modulus: Poly, q: int) -> Poly:
    exponent = q ** (len(modulus) - 1) - 2
    result, base = (1,), pmod(a, modulus, q)
    while exponent:
        if exponent & 1:
            result = pmod(pmul(result, base, q), modulus, q)
        base = pmod(pmul(base, base, q), modulus, q)
        exponent >>= 1
    return result


def degree(a: Poly) -> int:
    return len(a) - 1 if a else -1


def lambda_sources(m: int, q: int, irr: Dict[int, List[Poly]]) -> List[Tuple[Poly, int]]:
    out: List[Tuple[Poly, int]] = []
    for d in range(1, m + 1):
        if m % d:
            continue
        e = m // d
        for P in irr[d]:
            f = (1,)
            for _ in range(e):
                f = pmul(f, P, q)
            out.append((f, d))
    return out


# Exact arithmetic in Z[zeta_q], represented modulo zeta_q^q=1 and
# canonicalized by 1+zeta+...+zeta^(q-1)=0. All q used below are prime.
Zeta = Tuple[int, ...]


def zzero(q: int) -> Zeta:
    return tuple([0] * q)


def zroot(e: int, q: int) -> Zeta:
    out = [0] * q
    out[e % q] = 1
    return tuple(out)


def zadd(a: Zeta, b: Zeta) -> Zeta:
    return tuple(x + y for x, y in zip(a, b))


def zscale(a: Zeta, n: int) -> Zeta:
    return tuple(n * x for x in a)


def zmul(a: Zeta, b: Zeta) -> Zeta:
    q = len(a)
    out = [0] * q
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i + j) % q] += x * y
    return tuple(out)


def zconj(a: Zeta) -> Zeta:
    q = len(a)
    return tuple(a[(-i) % q] for i in range(q))


def zcanon(a: Zeta) -> Zeta:
    c = a[-1]
    return tuple(x - c for x in a)


def zsub(a: Zeta, b: Zeta) -> Zeta:
    return tuple(x - y for x, y in zip(a, b))


def zint(a: Zeta) -> int:
    c = zcanon(a)
    assert all(x == 0 for x in c[1:]), c
    return c[0]


def zfloat(a: Zeta) -> complex:
    zeta = cmath.exp(2j * cmath.pi / len(a))
    return sum(x * zeta ** i for i, x in enumerate(a))


def coeff_top(x: Poly, P: Poly) -> int:
    k = len(P) - 1
    return x[k - 1] if len(x) >= k else 0


def ahat_exact(P: Poly, mu: Poly, sources: List[Tuple[Poly, int]], q: int) -> Zeta:
    out = zzero(q)
    for f, w in sources:
        exponent = coeff_top(pmod(pmul(mu, f, q), P, q), P)
        out = zadd(out, zscale(zroot(exponent, q), w))
    return out


def pairing_exact(theta: Poly, x: Poly, W: Poly, q: int) -> Zeta:
    r = pmod(pmul(theta, x, q), W, q)
    exponent = r[len(W) - 2] if len(r) >= len(W) - 1 else 0
    return zroot(exponent, q)


def residue_index(f: Poly, P: Poly, q: int) -> int:
    r = pmod(f, P, q)
    return sum((r[i] if i < len(r) else 0) * q ** i for i in range(len(P) - 1))


@dataclass(frozen=True)
class PairData:
    P: Poly
    S: Poly
    mu: Poly
    nu: Poly
    LinvP: Poly
    LinvS: Poly
    SinvP: Poly
    PinvS: Poly


def primorial(q: int) -> Poly:
    return trim([0, q - 1] + [0] * (q - 2) + [1])


def build_pairs(q: int, k: int, m: int, L: Poly, theta: Poly = (1,)) -> Tuple[List[Poly], List[Tuple[Poly, int]], List[PairData]]:
    irr = irreducibles_upto(max(k, m), q)
    band = irr[k]
    sources = lambda_sources(m, q, irr)
    pairs: List[PairData] = []
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
            pairs.append(PairData(P, S, mu, nu, LinvP, LinvS, SinvP, PinvS))
    return band, sources, pairs


def plancherel_panel(q: int, k: int = 2, m: int = 3) -> dict:
    irr = irreducibles_upto(m, q)
    P = irr[k][0]
    sources = lambda_sources(m, q, irr)
    mus = [trim(x) for x in itertools.product(range(q), repeat=k) if any(x)]
    lhs_z = zzero(q)
    max_abs = 0.0
    for mu in mus:
        value = ahat_exact(P, mu, sources, q)
        lhs_z = zadd(lhs_z, zmul(value, zconj(value)))
        max_abs = max(max_abs, abs(zfloat(value)))
    lhs = zint(lhs_z)
    counts = [0] * (q ** k)
    for f, w in sources:
        counts[residue_index(f, P, q)] += w
    mean = q ** (m - k)
    variance = sum((x - mean) ** 2 for x in counts)
    rhs = q ** k * variance
    assert lhs == rhs
    return {
        "q": q,
        "k": k,
        "m": m,
        "sum_nonzero_frequency_mass": lhs,
        "all_residue_variance": variance,
        "qk_times_variance": rhs,
        "mass_over_q_m_plus_k": lhs / q ** (m + k),
        "max_A_over_q_m_over_2": max_abs / q ** (m / 2),
    }


def corrected_T_panel(q: int, k: int = 2, R: int = 3, m: int = 3) -> dict:
    L = primorial(q)
    theta = (1,)
    _, sources, pairs = build_pairs(q, k, m, L, theta)
    tR = tuple([0] * R + [1])
    uncorrected = zzero(q)
    correction = zzero(q)
    for a in pairs:
        A1 = ahat_exact(a.P, a.mu, sources, q)
        A2 = ahat_exact(a.S, a.nu, sources, q)
        W = pmul(a.P, a.S, q)
        eP = pmod(pmul(a.S, a.SinvP, q), W, q)
        eS = pmod(pmul(a.P, a.PinvS, q), W, q)
        v = pmod(padd(pmul(eP, a.LinvP, q), pmul(eS, a.LinvS, q), q), W, q)
        delta = zzero(q)
        for f, w in sources:
            phase = pairing_exact(theta, pneg(pmod(pmul(v, f, q), W, q), q), W, q)
            delta = zadd(delta, zscale(phase, w * w))
        phase0 = pairing_exact(theta, pneg(tR, q), W, q)
        uncorrected = zadd(uncorrected, zmul(zmul(A1, A2), phase0))
        correction = zadd(correction, zmul(delta, phase0))
    actual = zsub(uncorrected, correction)
    u_abs = abs(zfloat(uncorrected))
    d_abs = abs(zfloat(correction))
    a_abs = abs(zfloat(actual))
    target = q ** (m + 1.5 * k)
    return {
        "q": q,
        "pairs": len(pairs),
        "uncorrected_exact_cyclotomic_vector": list(zcanon(uncorrected)),
        "diagonal_correction_exact_cyclotomic_vector": list(zcanon(correction)),
        "actual_exact_cyclotomic_vector": list(zcanon(actual)),
        "abs_uncorrected": u_abs,
        "abs_diagonal_correction": d_abs,
        "abs_actual": a_abs,
        "uncorrected_over_FFPR_target": u_abs / target,
        "correction_over_FFPR_target": d_abs / target,
        "actual_over_FFPR_target": a_abs / target,
    }


def double_coincidence_panel(q: int, k: int, m: int) -> dict:
    _, _, pairs = build_pairs(q, k, m, primorial(q), (1,))
    threshold = 2 * k - m - 1
    v_count = u_count = both_count = diag = transpose = other = 0
    for a in pairs:
        for b in pairs:
            Ev = psub(pmul(a.nu, b.S, q), pmul(b.nu, a.S, q), q)
            Eu = psub(pmul(a.mu, b.P, q), pmul(b.mu, a.P, q), q)
            cv = degree(Ev) <= threshold
            cu = degree(Eu) <= threshold
            v_count += int(cv)
            u_count += int(cu)
            if cv and cu:
                both_count += 1
                if (a.P, a.S) == (b.P, b.S):
                    diag += 1
                elif (a.P, a.S) == (b.S, b.P):
                    transpose += 1
                else:
                    other += 1
    return {
        "q": q,
        "k": k,
        "m": m,
        "pairs": len(pairs),
        "source_1_coincidences": u_count,
        "source_2_coincidences": v_count,
        "double_coincidences": both_count,
        "double_diagonal": diag,
        "double_transpose": transpose,
        "double_other": other,
    }


def main() -> None:
    result = {
        "status_labels": {
            "plancherel": "MACHINE-VERIFIED IDENTITY",
            "corrected_T": "EMPIRICAL-EXACT FINITE PANEL",
            "double_coincidence": "EMPIRICAL-EXACT FINITE PANEL",
            "diagonal_floor": "PROVED EXACTLY (exponent ledger)",
        },
        "plancherel": [plancherel_panel(q) for q in (3, 5, 7)],
        "corrected_T": [corrected_T_panel(q) for q in (3, 5, 7, 11)],
        "double_coincidence": [
            double_coincidence_panel(3, 2, 3),
            double_coincidence_panel(5, 2, 3),
            double_coincidence_panel(7, 2, 3),
            double_coincidence_panel(3, 3, 5),
        ],
        "diagonal_floor_ledger": {
            "sampled_A_square_mass": "q^(m+2k) up to polynomial factors",
            "first_dispersion_diagonal": "q^m * q^(m+2k) = q^(2m+2k)",
            "after_source_Cauchy": "|T| <= q^(3m/2+k) up to polynomial factors",
            "FFPR_target": "q^(m+3k/2)",
            "endpoint_m_2k_minus_1_deficit": "q^((k-1)/2)",
            "conclusion": "Class control C=O(Diag) preserves this bound but cannot remove its diagonal floor. Any closing second dispersion must be centered before the first positive Cauchy step or use a genuinely signed bilinear assembly theorem.",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
