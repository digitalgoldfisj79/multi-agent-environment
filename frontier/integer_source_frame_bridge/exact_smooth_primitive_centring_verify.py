#!/usr/bin/env python3
"""Verify exact smooth-primitive centring and new-modulus residual."""
from __future__ import annotations

import json
import math
from pathlib import Path

from sympy import factorint, mobius, primerange, totient


def von_mangoldt(n: int) -> float:
    fs = factorint(n)
    return math.log(int(next(iter(fs)))) if len(fs) == 1 else 0.0


def primorial(z: int) -> int:
    P = 1
    for p in primerange(2, z + 1):
        P *= int(p)
    return P


def ramanujan_sum(q: int, n: int, phi: list[int]) -> int:
    """Exact c_q(n); active q are squarefree because Gamma_Z(q)=0 otherwise."""
    g = math.gcd(q, n)
    return int(mobius(q // g)) * phi[q] // phi[q // g]


def primitive_coefficients(Z: int) -> tuple[list[float], list[int]]:
    """Compute Gamma_Z(q)=-sum_{q|n<=Z} mu(n)log(n)/n by a divisor sieve."""
    mu = [0] * (Z + 1)
    phi = [0] * (Z + 1)
    phi[1] = 1
    for n in range(1, Z + 1):
        mu[n] = int(mobius(n))
        phi[n] = int(totient(n))
    atom = [0.0] * (Z + 1)
    for n in range(2, Z + 1):
        if mu[n]:
            atom[n] = -mu[n] * math.log(n) / n
    gamma = [0.0] * (Z + 1)
    for q in range(2, Z + 1):
        gamma[q] = math.fsum(atom[n] for n in range(q, Z + 1, q))
    return gamma, phi


def one_case(z: int, H: int) -> dict:
    P = primorial(z)
    Z = P + H
    weights = {m: 1.0 + 0.05 * math.cos(m) for m in range(2, H + 1)}
    W = math.fsum(weights.values())
    direct = math.fsum(w * von_mangoldt(P + m) for m, w in weights.items())

    mu_log_atoms = [
        -float(mobius(d)) * math.log(d) / d for d in range(1, Z + 1)
    ]
    zero = W * math.fsum(mu_log_atoms)
    gamma, phi = primitive_coefficients(Z)

    smooth_terms: list[float] = []
    new_terms: list[float] = []
    for q in range(2, Z + 1):
        if abs(gamma[q]) < 1e-18:
            continue
        row = math.fsum(
            w * ramanujan_sum(q, P + m, phi) for m, w in weights.items()
        )
        term = gamma[q] * row
        if P % q == 0:
            smooth_terms.append(term)
        else:
            new_terms.append(term)

    smooth = math.fsum(smooth_terms)
    new = math.fsum(new_terms)
    all_primitive = smooth + new
    exact_centring = zero + smooth
    candidate = P / phi[P] * math.fsum(
        w for m, w in weights.items() if math.gcd(m, P) == 1
    )
    return {
        "z": z,
        "P": P,
        "H": H,
        "Z": Z,
        "direct_source": direct,
        "zero_mode": zero,
        "smooth_primitive": smooth,
        "exact_primitive_centring": exact_centring,
        "candidate_projector_principal": candidate,
        "centring_minus_candidate": exact_centring - candidate,
        "all_primitive_error": abs((direct - zero) - all_primitive),
        "new_residual_error": abs((direct - exact_centring) - new),
        "active_smooth_denominators": len(smooth_terms),
        "active_new_denominators": len(new_terms),
    }


def main() -> None:
    rows = [one_case(7, 20), one_case(11, 30), one_case(13, 36)]
    for row in rows:
        assert row["all_primitive_error"] < 3e-8, row
        assert row["new_residual_error"] < 3e-8, row
    payload = {
        "status": "PASS",
        "scope": "exact smooth-primitive centring and new-modulus residual",
        "rows": rows,
        "boundary": "Finite exact identities only; convergence to the candidate principal is asymptotic.",
    }
    Path(__file__).with_name("exact_smooth_primitive_centring_results.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
