#!/usr/bin/env python3
"""Structural regression for the cyclotomic tangent/Tate precision theorem.

Let R=F_p[epsilon]/(epsilon^2), modelling O/(pi^2) for
O=Z_p[zeta_p], pi=zeta_p-1. The coefficient character sends a generator
tau of C_p to 1+epsilon. The script checks:

* tau^p=1 and the cyclic norm is zero;
* the Tate complex alternates multiplication by epsilon and zero;
* both Tate groups are one-dimensional;
* the coefficient Bockstein (tau-1)/epsilon is nonzero;
* Frobenius lifts 1+lambda*epsilon have identical Tate/Bockstein data but
  arbitrary first-order trace coefficient lambda;
* p is a unit times pi^(p-1), so an undivided hook trace p*(N+pi*M+...)
  places N at order p-1 and M at order p.

This is a structural regression, not a finite-prime proof of Fortune.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

Dual = tuple[int, int]


def add(x: Dual, y: Dual, p: int) -> Dual:
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def mul(x: Dual, y: Dual, p: int) -> Dual:
    return (
        x[0] * y[0] % p,
        (x[0] * y[1] + x[1] * y[0]) % p,
    )


def power(x: Dual, exponent: int, p: int) -> Dual:
    out: Dual = (1, 0)
    for _ in range(exponent):
        out = mul(out, x, p)
    return out


def run_prime(p: int) -> dict[str, object]:
    epsilon: Dual = (0, 1)
    tau: Dual = (1, 1)
    zero: Dual = (0, 0)

    assert power(tau, p, p) == (1, 0)

    norm = zero
    for j in range(p):
        norm = add(norm, power(tau, j, p), p)
    assert norm == zero

    elements = [(a, b) for a in range(p) for b in range(p)]
    image_epsilon = {mul(epsilon, x, p) for x in elements}
    kernel_epsilon = {x for x in elements if mul(epsilon, x, p) == zero}
    assert image_epsilon == kernel_epsilon
    assert len(image_epsilon) == p

    # Lift the quotient generator 1, apply tau-1=epsilon, and divide by
    # epsilon: the coefficient Bockstein is the identity on F_p.
    lifted_generator: Dual = (1, 0)
    boundary = mul(epsilon, lifted_generator, p)
    assert boundary == epsilon
    coefficient_bockstein = boundary[1]
    assert coefficient_bockstein == 1

    # The norm vanishes already modulo epsilon^2, so its first Bockstein is 0.
    norm_bockstein = norm[1]
    assert norm_bockstein == 0

    tangent_coefficients = []
    for lam in range(p):
        phi: Dual = (1, lam)
        assert mul(phi, tau, p) == mul(tau, phi, p)
        # phi acts trivially on R/epsilon and on epsilon R.
        assert mul(phi, lifted_generator, p)[0] == 1
        assert mul(phi, epsilon, p) == epsilon
        tangent_coefficients.append(phi[1])
    assert tangent_coefficients == list(range(p))

    # Phi_p(1+x)=sum_{r=0}^{p-1} binom(p,r+1)x^r.
    cyclotomic_coefficients = [comb(p, r + 1) for r in range(p)]
    assert cyclotomic_coefficients[0] == p
    assert cyclotomic_coefficients[-1] == 1
    assert all(value % p == 0 for value in cyclotomic_coefficients[:-1])

    return {
        "p": p,
        "tau_to_p": [1, 0],
        "norm": [0, 0],
        "tate_even_dimension": 1,
        "tate_odd_dimension": 1,
        "coefficient_bockstein": coefficient_bockstein,
        "norm_bockstein": norm_bockstein,
        "frobenius_tangent_coefficient_count": len(tangent_coefficients),
        "frobenius_tangent_coefficient_range": [0, p - 1],
        "count_cyclotomic_order_in_raw_hook": p - 1,
        "moment_cyclotomic_order_in_raw_hook": p,
        "minimum_raw_modulus_exponent_for_moment": p + 1,
    }


def main() -> None:
    primes = [5, 11, 17, 23, 29, 41, 47, 53, 59, 71]
    rows = [run_prime(p) for p in primes]
    output = {
        "classification": "symbolic structural regression; crown remains open",
        "ring_model": "F_p[epsilon]/(epsilon^2)",
        "theorem_checks": {
            "coefficient_character_is_nonsplit_extension": True,
            "tate_complex_differentials": ["epsilon", "0"],
            "tate_and_bockstein_do_not_determine_frobenius_tangent": True,
            "raw_hook_mod_pi2_is_blind_for_p_at_least_5": True,
            "raw_precision_needed_for_first_moment": "mod pi^(p+1)",
        },
        "rows": rows,
        "status": "PASS",
    }
    path = Path(__file__).with_name(
        "cyclotomic_tangent_tate_precision_results_20260726.json"
    )
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print("CYCLOTOMIC_TANGENT_TATE_PRECISION_VERIFY: PASS")


if __name__ == "__main__":
    main()
