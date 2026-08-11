#!/usr/bin/env python3
"""Exact audit of the characteristic-three primorial-resonant incidence.

For q=3, L=t^3-t, k>=3, Q of degree k-3 with leading coefficient -1,
define J_Q(T)=LQ-T. For epsilon in F_3^* and S=P+epsilon Q, set
P'=J_Q(P), S'=J_Q(S). Whenever all four degree-k polynomials are
irreducible, the endpoint reciprocal completion numerators are constants
-theta/epsilon and theta/epsilon. Their two Gram phases cancel.

The script verifies the identities on all generated prime points for k=3..7,
checks that the k=4 family is exactly the 12 previously discovered exceptional
incidences, and records the elementary dimension bound for the raw Gram term.
"""
from __future__ import annotations

import itertools
import json
from collections import Counter
from typing import Sequence, Tuple

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


def ppow(a: Poly, exponent: int, modulus: Poly, q: int) -> Poly:
    result, base = (1,), pmod(a, modulus, q)
    while exponent:
        if exponent & 1:
            result = pmod(pmul(result, base, q), modulus, q)
        base = pmod(pmul(base, base, q), modulus, q)
        exponent //= 2
    return result


def pinv(a: Poly, modulus: Poly, q: int) -> Poly:
    assert a
    return ppow(a, q ** (len(modulus) - 1) - 2, modulus, q)


def degree(a: Poly) -> int:
    return len(a) - 1 if a else -1


def monics(d: int, q: int):
    for low in itertools.product(range(q), repeat=d):
        yield trim(list(low) + [1])


def irreducibles_upto(dmax: int, q: int):
    irr = {d: [] for d in range(1, dmax + 1)}
    for d in range(1, dmax + 1):
        for f in monics(d, q):
            if not any(not pmod(f, g, q) for e in range(1, d // 2 + 1) for g in irr[e]):
                irr[d].append(f)
    return irr


def primorial() -> Poly:
    return (0, 2, 0, 1)  # t^3-t over F_3


def local_parameter(A: Poly, B: Poly, L: Poly, theta: int, q: int = 3) -> Poly:
    return pmod(
        pmul(
            pmul(((-theta) % q,), pinv(pmod(L, A, q), A, q), q),
            pinv(pmod(B, A, q), A, q),
            q,
        ),
        A,
        q,
    )


def q_polynomials(k: int):
    for low in itertools.product(range(3), repeat=k - 3):
        yield trim(list(low) + [2])  # leading coefficient -1


def generated_points(k: int):
    q = 3
    L = primorial()
    irr = irreducibles_upto(k, q)
    band = irr[k]
    band_set = set(band)
    rows = []
    for P in band:
        for Q in q_polynomials(k):
            Pp = psub(pmul(L, Q, q), P, q)
            for epsilon in (1, 2):
                S = padd(P, pmul((epsilon,), Q, q), q)
                Sp = psub(Pp, pmul((epsilon,), Q, q), q)
                if S not in band_set or Pp not in band_set or Sp not in band_set or P == S or Pp == Sp:
                    continue
                constants = []
                for theta in (1, 2):
                    mu = local_parameter(P, S, L, theta)
                    mup = local_parameter(Pp, Sp, L, theta)
                    nu = local_parameter(S, P, L, theta)
                    nup = local_parameter(Sp, Pp, L, theta)
                    E_mu = psub(pmul(mu, Pp, q), pmul(mup, P, q), q)
                    E_nu = psub(pmul(nu, Sp, q), pmul(nup, S, q), q)
                    assert E_mu == (((-theta * pow(epsilon, -1, 3)) % 3),)
                    assert E_nu == (((theta * pow(epsilon, -1, 3)) % 3),)
                    assert padd(E_mu, E_nu, q) == ()
                    constants.append((theta, E_mu, E_nu))
                assert padd(P, Pp, q) == pmul(L, Q, q)
                assert padd(S, Sp, q) == pmul(L, Q, q)
                assert psub(S, P, q) == pmul((epsilon,), Q, q)
                rows.append((P, S, Pp, Sp, Q, epsilon, constants))
    return irr, rows


def all_exceptions_k4():
    q = 3
    k = 4
    L = primorial()
    band = irreducibles_upto(k, q)[k]
    pairs = []
    for P in band:
        for S in band:
            if P == S:
                continue
            mu = local_parameter(P, S, L, 1)
            nu = local_parameter(S, P, L, 1)
            pairs.append((P, S, mu, nu))
    out = set()
    for P, S, mu, nu in pairs:
        for Pp, Sp, mup, nup in pairs:
            E_mu = psub(pmul(mu, Pp, q), pmul(mup, P, q), q)
            E_nu = psub(pmul(nu, Sp, q), pmul(nup, S, q), q)
            if degree(E_mu) <= 0 and degree(E_nu) <= 0 and (P, S) != (Pp, Sp) and (P, S) != (Sp, Pp):
                out.add((P, S, Pp, Sp))
    return out


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    x = n
    p = 2
    count = 0
    while p * p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def pi_q(d: int, q: int) -> int:
    return sum(mobius(e) * q ** (d // e) for e in divisors(d)) // d


def B_exact(m: int, q: int) -> int:
    return sum(d * d * pi_q(d, q) for d in divisors(m))


def panel(k: int) -> dict:
    q = 3
    m = 2 * k - 1
    irr, rows = generated_points(k)
    B_m = B_exact(m, q)
    raw = len(rows) * B_m * B_m
    target_squared = q ** (2 * m + 3 * k)
    parameter_upper = 2 * q ** k * q ** (k - 3)
    elementary_upper = parameter_upper * (m * q ** m) ** 2
    assert len(rows) <= parameter_upper
    assert raw <= elementary_upper
    epsilon_counts = Counter(row[5] for row in rows)
    return {
        "q": q,
        "k": k,
        "m": m,
        "degree_k_prime_count": len(irr[k]),
        "Q_parameter_count": q ** (k - 3),
        "resonant_ordered_pair_of_pairs": len(rows),
        "epsilon_counts": {str(e): epsilon_counts[e] for e in sorted(epsilon_counts)},
        "completion_constants_verified_for_theta": [1, 2],
        "B_m_sum_Lambda_square": B_m,
        "raw_gram_component": raw,
        "squared_endpoint_target": target_squared,
        "raw_over_squared_target": raw / target_squared,
        "parameter_count_upper_bound": parameter_upper,
        "elementary_raw_upper_bound": elementary_upper,
        "elementary_upper_over_squared_target": elementary_upper / target_squared,
    }


def main() -> None:
    panels = [panel(k) for k in range(3, 8)]
    _, rows4 = generated_points(4)
    generated4 = {(row[0], row[1], row[2], row[3]) for row in rows4}
    complete4 = all_exceptions_k4()
    assert generated4 == complete4 and len(complete4) == 12
    result = {
        "status": {
            "resonance_identity": "MACHINE-VERIFIED IDENTITY supporting an exact algebraic proof",
            "k4_completeness": "EMPIRICAL-EXACT FINITE PANEL",
            "dimension_bound": "PROVED EXACTLY",
        },
        "exact_family": {
            "field": "F_3[t]",
            "puncture": "L=t^3-t",
            "parameters": "deg P=k prime; deg Q=k-3 with leading coefficient -1; epsilon,theta in F_3^*",
            "construction": "S=P+epsilon Q; P'=LQ-P; S'=LQ-S",
            "completion_numerators": "E_mu=-theta/epsilon; E_nu=theta/epsilon",
            "phase_product": "1",
            "classification": "small-characteristic primorial-resonant forced phase; negligible by parameter dimension before Delta interaction",
        },
        "k4_exception_completeness": {
            "all_non_diagonal_non_transpose_incidences": len(complete4),
            "generated_by_resonance": len(generated4),
            "sets_equal": True,
            "epsilon_orbit_sizes": {str(e): sum(1 for row in rows4 if row[5] == e) for e in (1, 2)},
        },
        "panels": panels,
        "uniform_bound": {
            "resonant_point_count": "<=2*3^(2k-3)",
            "B_m": "<=m*3^m",
            "raw_gram_component": "<=2*m^2*3^(2m+2k-3)",
            "squared_endpoint_target": "3^(2m+3k)",
            "saving_ratio": "<=2*m^2*3^(-k-3)",
        },
        "boundary": {
            "proved": "The explicit characteristic-three resonance cannot violate the squared endpoint target through its raw same-source Gram contribution.",
            "open": "Its literal interaction with Delta_PS inside the not-yet-derived centered bilateral identity.",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
