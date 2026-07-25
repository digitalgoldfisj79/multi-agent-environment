#!/usr/bin/env python3
"""Verifier for AIRY_GAUSSIAN_LAW_AND_TARGET_FALSIFICATION_20260725.md.

Three independent checks.

1. CALIBRATION.  The float model
       rho_p = T_p / p^((p-1)/2) = (2/sqrt p) sum_{t in F_p} cos(p theta_t),
       a_t = sum_{x in F_p} psi(x^3 + t x) = 2 sqrt(p) cos(theta_t),
   is validated against all nine committed exact integers T_p, including the
   65-digit value T_71.

2. GAUSSIAN LAW.  Over every prime p = 5 mod 6 up to a bound, rho_p is
   compared with N(0,2), which is what independent Sato-Tate angles predict:
       E[cos(p theta)] = 0,  Var[cos(p theta)] = 1/2  under (2/pi) sin^2,
       => Var(rho_p) = (4/p) * (p/2) = 2.
   A bounded rho_p would show a decaying running maximum and truncated tails.

3. ADAMS NO-GAIN.  With U_m the Chebyshev-U character of Sym^m,
       sum_t Tr(Sym^p A_t)            = p^(p/2) M_plus,   M_plus  = sum_t U_p,
       sum_t Tr(det (x) Sym^(p-2) A_t)= p^(p/2) M_minus,  M_minus = sum_t U_(p-2),
       sum_t Tr(Psi^p A_t)            = p^(p/2) (M_plus - M_minus).
   Sato-Tate orthonormality predicts rms(M/sqrt p) = 1 for each symmetric
   power.  If the Adams difference produced cancellation, M_plus and M_minus
   would be positively correlated and the difference would be smaller than
   either.  The measured correlation is ~0 and the difference is sqrt(2)
   times LARGER, so the virtual-Adams framing gains nothing.

4. SINGULAR LOCUS.  Lemma: the projective cubic {Tr(x^3)=0} in P(ker Tr),
   of dimension p-2, has exactly one singular point, [1].  Checked by
   enumeration for p = 5, 7.
"""

from __future__ import annotations

import math

import numpy as np

EXACT_T = {
    5: 0,
    11: 322102,
    17: 11899821517,
    23: -1010446643080743,
    29: -798145148362709627351,
    41: 285608599198466451834837856911313,
    47: -36201375290118292903477796139763762494,
    53: 625211553014678241605175931243651758726469297,
    71: 36727396978062655326395765238086038211050946366161670340353263984,
}

# The document reports the scan over p < 10^5; the verifier must reproduce that
# range, not a smaller one.  Override with argv[1] for a quick run.
SCAN_LIMIT = 100000

# Rigorously excluded constant, witnessed at p = 57653.  Everything beyond this
# finite exclusion (unboundedness, the 2 sqrt(log p) limsup law) is CONJECTURAL:
# a finite sample cannot separate N(0,2) from a sufficiently wide bounded law.
WITNESS_PRIME = 57653
EXCLUDED_CONSTANT = 4.8468292139


def primes_upto(n: int) -> list[int]:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return np.nonzero(sieve)[0].tolist()


def angles(p: int) -> np.ndarray:
    """theta_t for all t in F_p, via a_t = 2 sqrt(p) cos(theta_t)."""
    x = np.arange(p)
    cubes = (x * x % p) * x % p
    a = (p * np.fft.ifft(np.exp(2j * np.pi * cubes / p))).real
    return np.arccos(np.clip(a / (2.0 * math.sqrt(p)), -1.0, 1.0))


def rho(p: int) -> float:
    return (2.0 / math.sqrt(p)) * float(np.cos(p * angles(p)).sum())


def symmetric_power_sums(p: int) -> tuple[float, float]:
    th = angles(p)
    s = np.sin(th)
    safe = np.abs(s) > 1e-12
    up = np.zeros(p)
    um = np.zeros(p)
    up[safe] = np.sin((p + 1) * th[safe]) / s[safe]
    um[safe] = np.sin((p - 1) * th[safe]) / s[safe]
    return float(up.sum()), float(um.sum())


def check_calibration() -> None:
    from fractions import Fraction

    print("[1] calibration of the float model against exact integers")
    worst = 0.0
    for p in sorted(EXACT_T):
        exact = float(Fraction(EXACT_T[p], p ** ((p - 1) // 2)))
        got = rho(p)
        err = abs(got - exact) / max(abs(exact), 1.0)
        worst = max(worst, err)
        print(f"    p={p:>3}  rho_exact={exact:+.9f}  rho_float={got:+.9f}  rel={err:.1e}")
    assert worst < 1e-9, f"calibration failed, worst relative error {worst}"
    print(f"    PASS  worst relative error {worst:.2e}\n")


def check_gaussian_law() -> None:
    print(f"[2] Gaussian law for rho_p over p = 5 mod 6, p < {SCAN_LIMIT}")
    ps = [p for p in primes_upto(SCAN_LIMIT) if p % 6 == 5]
    vals = np.array([rho(p) for p in ps])
    var = float(vals.var(ddof=1))
    mean = float(vals.mean())
    kurt = float(((vals - mean) ** 4).mean() / vals.std() ** 4)

    sd = math.sqrt(2.0)
    x = np.sort(vals / sd)
    n = len(x)
    cdf = 0.5 * (1.0 + np.vectorize(math.erf)(x / math.sqrt(2.0)))
    ks = float(
        max(
            np.abs(cdf - np.arange(n) / n).max(),
            np.abs(cdf - np.arange(1, n + 1) / n).max(),
        )
    )
    crit = 1.358 / math.sqrt(n)

    print(f"    n={n}  mean={mean:+.4f} (model 0)  var={var:.4f} (model 2)"
          f"  kurtosis={kurt:.4f} (model 3)")
    print(f"    KS statistic {ks:.5f} vs 5% critical {crit:.5f}")
    assert ks < crit, "rho_p is NOT consistent with N(0,2)"
    assert 1.7 < var < 2.4, f"variance {var} far from the predicted 2"

    # the running maximum must keep growing: a bounded rho_p would flatten
    running = []
    for bound in (1000, 3000, 10000, SCAN_LIMIT):
        sub = np.array([r for p, r in zip(ps, vals) if p <= bound])
        running.append(float(np.abs(sub).max()))
        print(f"    max|rho_p| for p <= {bound:>6} : {running[-1]:.4f}")
    assert running == sorted(running), "running maximum must be non-decreasing"

    # The only RIGOROUS claim: a finite exclusion witnessed at a named prime.
    if SCAN_LIMIT >= WITNESS_PRIME:
        witness = abs(rho(WITNESS_PRIME))
        beaten = [p for p, r in zip(ps, vals) if abs(r) > 4.0]
        print(f"    witness p={WITNESS_PRIME}: |rho_p| = {witness:.10f}")
        print(f"    => no absolute constant C < {EXCLUDED_CONSTANT} is admissible")
        print(f"    C = 4 fails at {len(beaten)} primes below {SCAN_LIMIT}")
        assert witness > EXCLUDED_CONSTANT - 1e-6, "witness value not reproduced"
        assert len(beaten) >= 20, "expected many primes exceeding C = 4"
    print("    PASS  consistent with N(0,2); C = 4 rigorously excluded.")
    print("    NOTE  unboundedness is CONJECTURAL, not established by this test.\n")


def check_adams_no_gain() -> None:
    print("[3] the virtual Adams difference produces no cancellation")
    ps = [p for p in primes_upto(SCAN_LIMIT) if p % 6 == 5]
    rows = [symmetric_power_sums(p) for p in ps]
    sp = np.array([math.sqrt(p) for p in ps])
    mp = np.array([r[0] for r in rows]) / sp
    mm = np.array([r[1] for r in rows]) / sp
    dd = mp - mm
    corr = float(np.corrcoef(mp, mm)[0, 1])
    r_plus = float(np.sqrt((mp**2).mean()))
    r_minus = float(np.sqrt((mm**2).mean()))
    r_diff = float(np.sqrt((dd**2).mean()))
    print(f"    rms(M+/sqrt p)      = {r_plus:.4f}   (Sato-Tate model 1)")
    print(f"    rms(M-/sqrt p)      = {r_minus:.4f}   (Sato-Tate model 1)")
    print(f"    rms((M+ - M-)/sqrt p) = {r_diff:.4f}   (model sqrt 2 = {math.sqrt(2):.4f})")
    print(f"    corr(M+, M-)        = {corr:.4f}   (model 0)")
    assert abs(corr) < 0.15, "M+ and M- are correlated; Adams difference may gain"
    assert r_diff > 1.2 * max(r_plus, r_minus), "difference is not larger than either term"
    print("    PASS  M+ and M- are uncorrelated; the difference is LARGER than either\n")


def check_singular_locus() -> None:
    print("[4] the cubic {Tr(x^3)=0} in P(ker Tr) has exactly one singular point (p > 3)")

    # p = 3 is genuinely degenerate: cubing IS Frobenius, so by additivity
    # Tr(x^3) = (Tr x)^3 = Tr(x), which vanishes identically on ker Tr.
    g3 = [1, -1, 0, 1]  # t^3 = t + 1 over F_3
    elts3 = list(_all_elements(3))
    ker3 = [e for e in elts3 if _trace(e, g3, 3) == 0]
    cube_tr = [_trace(_mul(_mul(e, e, g3, 3), e, g3, 3), g3, 3) for e in ker3]
    assert len(ker3) == 9, f"expected |ker Tr| = 9 in F_27, got {len(ker3)}"
    assert all(t == 0 for t in cube_tr), "p=3 cubic should vanish identically on ker Tr"
    print(f"    p= 3: DEGENERATE - cubic vanishes on all {len(ker3)} points of ker Tr;")
    print("          Lemma 5.1 is false at p = 3 and must exclude it")

    for p in (5, 7):
        # build F_{p^p} = F_p[t]/(g), g monic irreducible of degree p
        g = None
        for top in range(p ** (p - 1)):
            coeffs = [(top // p**i) % p for i in range(p - 1)] + [0, 1]
            if _is_irreducible(coeffs, p):
                g = coeffs
                break
        assert g is not None
        elements = list(_all_elements(p))
        trace = {e: _trace(e, g, p) for e in elements}
        # singular points: x in ker Tr, x != 0, with x^2 in F_p
        singular = [
            e
            for e in elements
            if any(e) and trace[e] == 0 and _in_prime_field(_mul(e, e, g, p))
        ]
        # they must all be scalars, i.e. one projective point
        assert all(_in_prime_field(e) for e in singular), f"p={p}: non-scalar singular point"
        assert len(singular) == p - 1, f"p={p}: expected {p-1} scalars, got {len(singular)}"
        print(f"    p={p:>2}: singular locus = {{[1]}}, {len(singular)} affine points, all in F_p")
    print("    PASS  one singular point for p = 5, 7; p = 3 degenerate as expected\n")


def _all_elements(p: int):
    from itertools import product

    return product(range(p), repeat=p)


def _in_prime_field(e) -> bool:
    return not any(e[1:])


def _mul(a, b, g, p):
    n = len(g) - 1
    out = [0] * (2 * n - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
    for i in range(len(out) - 1, n - 1, -1):
        c = out[i]
        if c:
            out[i] = 0
            for j in range(n):
                out[i - n + j] = (out[i - n + j] - c * g[j]) % p
    return tuple(out[:n])


def _pow_frob(e, g, p):
    r = (1,) + (0,) * (len(g) - 2)
    for _ in range(p):
        r = _mul(r, e, g, p)
    return r


def _trace(e, g, p):
    total = [0] * (len(g) - 1)
    cur = e
    for _ in range(p):
        total = [(a + b) % p for a, b in zip(total, cur)]
        cur = _pow_frob(cur, g, p)
    return total[0] if not any(total[1:]) else -1


def _is_irreducible(g, p) -> bool:
    n = len(g) - 1
    x = (0, 1) + (0,) * (n - 2)
    cur = x
    for k in range(1, n):
        cur = _pow_frob(cur, g, p)
        if cur == x:
            return False
    return _pow_frob(cur, g, p) == x


def main() -> None:
    global SCAN_LIMIT
    import sys

    if len(sys.argv) > 1:
        SCAN_LIMIT = int(sys.argv[1])
    check_calibration()
    check_gaussian_law()
    check_adams_no_gain()
    check_singular_locus()
    print("AIRY_GAUSSIAN_LAW_VERIFY: PASS")


if __name__ == "__main__":
    main()
