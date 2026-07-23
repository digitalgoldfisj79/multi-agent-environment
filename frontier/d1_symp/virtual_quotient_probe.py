#!/usr/bin/env python3
"""
Focused exact probe for the virtual cubic-Airy Adams quotient.

For p in {5,7,11}, compute modulo split coefficient primes ell == 1 (mod p)

    L_p(T) = L(A^1, Sym^p(Ai_{x^3}), T),
    L_{p-2}^det(T) = L(A^1, det(Ai_{x^3}) tensor Sym^{p-2}(Ai_{x^3}), T),

using exact finite-field arithmetic and an exact p-ary DFT over F_ell.

This is not a raw T_p prime sweep. It tests whether the two linearly growing
cohomology spaces have enough common Frobenius factors to leave a very small
residual quotient.

The DFT computes the multiset
    S_m(u) = sum_{x in F_{p^m}} zeta_p^{Tr(x^3 + u x)}
for all u. The trace pairing differs from the coordinate dot product by an
invertible linear change of frequency, so the multiset is unchanged. From
t_u = -S_m(u) and det(Frob_u)=p^m, the symmetric-power trace is obtained by
h_0=1, h_1=t, h_n=t h_{n-1}-q h_{n-2}. Newton identities reconstruct the
global L-polynomials.

Dependencies: Python 3, numpy, sympy.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np
import sympy as sp

T = sp.symbols("T")


@dataclass(frozen=True)
class ProbeResult:
    p: int
    ell: int
    degree_p: int
    degree_pm2: int
    gcd_degree: int
    residual_total_degree: int
    first_virtual_trace: int


def airy_degree(p: int, k: int) -> int:
    """Haessig--Rojas-Leon degree formula for f=x^3."""
    floor = k // p
    delta = 1 if (k - floor) % 2 == 0 else 0
    numerator = k + 1 - 3 * (floor + delta)
    assert numerator >= 0 and numerator % 2 == 0
    return numerator // 2


def find_irreducible_polynomial(p: int, m: int) -> list[int]:
    """Return low-to-high coefficients of a monic irreducible degree-m polynomial."""
    x = sp.symbols("x")
    if m == 1:
        return [0, 1]
    for c0 in range(1, p):
        for j in range(1, m):
            for cj in range(1, p):
                poly = sp.Poly(x**m + cj * x**j + c0, x, modulus=p)
                if poly.is_irreducible:
                    return [int(poly.nth(i)) % p for i in range(m + 1)]
    rng = np.random.default_rng(1000003 * p + m)
    for _ in range(20000):
        low = [int(v) for v in rng.integers(0, p, size=m)]
        low[0] = low[0] or 1
        poly = sp.Poly(
            x**m + sum(low[i] * x**i for i in range(m)), x, modulus=p
        )
        if poly.is_irreducible:
            return low + [1]
    raise RuntimeError(f"failed to find irreducible polynomial for p={p}, m={m}")


def all_elements(p: int, m: int) -> np.ndarray:
    q = p**m
    idx = np.arange(q, dtype=np.int64)
    out = np.empty((q, m), dtype=np.int64)
    for i in range(m):
        out[:, i] = idx % p
        idx //= p
    return out


def multiply_batch(
    a: np.ndarray, b: np.ndarray, p: int, modulus: list[int]
) -> np.ndarray:
    """Multiply equally shaped batches in F_p[x]/(modulus)."""
    n, m = a.shape
    conv = [np.zeros(n, dtype=np.int64) for _ in range(2 * m - 1)]
    for i in range(m):
        for j in range(m):
            conv[i + j] = (conv[i + j] + a[:, i] * b[:, j]) % p
    for degree in range(2 * m - 2, m - 1, -1):
        coefficient = conv[degree] % p
        for i in range(m):
            conv[degree - m + i] = (
                conv[degree - m + i] - coefficient * modulus[i]
            ) % p
    return np.stack([conv[i] % p for i in range(m)], axis=1)


def multiply_scalar(
    a: list[int], b: list[int], p: int, modulus: list[int]
) -> list[int]:
    aa = np.asarray(a, dtype=np.int64).reshape(1, -1)
    bb = np.asarray(b, dtype=np.int64).reshape(1, -1)
    return multiply_batch(aa, bb, p, modulus)[0].tolist()


def power_scalar(a: list[int], exponent: int, p: int, modulus: list[int]) -> list[int]:
    m = len(a)
    result = [1] + [0] * (m - 1)
    base = list(a)
    while exponent:
        if exponent & 1:
            result = multiply_scalar(result, base, p, modulus)
        base = multiply_scalar(base, base, p, modulus)
        exponent //= 2
    return result


def trace_basis(p: int, m: int, modulus: list[int]) -> np.ndarray:
    """Return Tr(1), Tr(theta), ..., Tr(theta^(m-1))."""
    traces: list[int] = []
    for i in range(m):
        value = [0] * m
        value[i] = 1
        total = [0] * m
        conjugate = value
        for _ in range(m):
            total = [(total[j] + conjugate[j]) % p for j in range(m)]
            conjugate = power_scalar(conjugate, p, p, modulus)
        assert all(total[j] == 0 for j in range(1, m))
        traces.append(total[0] % p)
    return np.asarray(traces, dtype=np.int64)


def split_prime(p: int, start: int) -> int:
    candidate = start + ((1 - start) % p)
    while not sp.isprime(candidate):
        candidate += p
    return int(candidate)


def dft_all_axes(array: np.ndarray, p: int, ell: int, root: int) -> np.ndarray:
    matrix = np.asarray(
        [
            [pow(root, (frequency * x) % p, ell) for x in range(p)]
            for frequency in range(p)
        ],
        dtype=np.int64,
    )
    result = array.astype(np.int64, copy=True)
    for axis in range(result.ndim):
        result = np.moveaxis(result, axis, 0)
        shape = result.shape
        result = ((matrix @ result.reshape(p, -1)) % ell).reshape(shape)
        result = np.moveaxis(result, 0, axis)
    return result


def airy_s_values_mod(p: int, m: int, ell: int) -> np.ndarray:
    modulus = find_irreducible_polynomial(p, m)
    elements = all_elements(p, m)
    squares = multiply_batch(elements, elements, p, modulus)
    cubes = multiply_batch(squares, elements, p, modulus)
    traces = (cubes @ trace_basis(p, m, modulus)) % p

    primitive = int(sp.primitive_root(ell))
    root = pow(primitive, (ell - 1) // p, ell)
    assert root != 1 and pow(root, p, ell) == 1

    phase = np.asarray([pow(root, int(e), ell) for e in traces], dtype=np.int64)
    # Coefficient a_0 is the fastest-varying base-p digit.
    phase_tensor = phase.reshape((p,) * m, order="F")
    return dft_all_axes(phase_tensor, p, ell, root).reshape(-1, order="F")


def symmetric_trace(t: np.ndarray, q: int, k: int, ell: int) -> np.ndarray:
    if k == 0:
        return np.ones_like(t) % ell
    if k == 1:
        return t % ell
    previous_previous = np.ones_like(t) % ell
    previous = t % ell
    for _ in range(2, k + 1):
        current = (t * previous - q * previous_previous) % ell
        previous_previous, previous = previous, current
    return previous


def polynomial_from_log_traces(traces: list[int], ell: int) -> list[int]:
    """If log L = sum_m A_m T^m/m, return coefficients of L."""
    coefficients = [1]
    for n in range(1, len(traces) + 1):
        total = 0
        for i in range(1, n + 1):
            total = (total + traces[i - 1] * coefficients[n - i]) % ell
        coefficients.append((total * pow(n, -1, ell)) % ell)
    return coefficients


def as_poly(coefficients: list[int], ell: int) -> sp.Poly:
    return sp.Poly(
        sum(
            int(coefficient) * T**i
            for i, coefficient in enumerate(coefficients)
        ),
        T,
        modulus=ell,
    )


def probe_one(p: int, ell: int) -> ProbeResult:
    assert p >= 5 and sp.isprime(p)
    assert sp.isprime(ell) and ell % p == 1

    degree_p = airy_degree(p, p)
    degree_pm2 = airy_degree(p, p - 2)
    max_degree = max(degree_p, degree_pm2)
    traces_p: list[int] = []
    traces_pm2_det: list[int] = []

    for m in range(1, max_degree + 1):
        s_values = airy_s_values_mod(p, m, ell)
        local_trace = (-s_values) % ell
        q = pow(p, m, ell)
        if m <= degree_p:
            traces_p.append(
                int(symmetric_trace(local_trace, q, p, ell).sum() % ell)
            )
        if m <= degree_pm2:
            trace_pm2 = symmetric_trace(local_trace, q, p - 2, ell)
            traces_pm2_det.append(int((q * trace_pm2).sum() % ell))

    poly_p = as_poly(polynomial_from_log_traces(traces_p, ell), ell)
    poly_pm2 = as_poly(polynomial_from_log_traces(traces_pm2_det, ell), ell)

    assert poly_p.degree() == degree_p
    assert poly_pm2.degree() == degree_pm2
    assert int(poly_p.LC()) % ell != 0
    assert int(poly_pm2.LC()) % ell != 0

    gcd_degree = sp.gcd(poly_p, poly_pm2).degree()
    first_virtual_trace = (
        (traces_p[0] if traces_p else 0)
        - (traces_pm2_det[0] if traces_pm2_det else 0)
    ) % ell

    # Independent committed checks for the p == 2 mod 3 collapse sector.
    committed_t = {5: 0, 11: 322102}
    if p in committed_t:
        expected = (-p * committed_t[p]) % ell
        assert first_virtual_trace == expected, (
            p,
            ell,
            first_virtual_trace,
            expected,
        )

    return ProbeResult(
        p=p,
        ell=ell,
        degree_p=degree_p,
        degree_pm2=degree_pm2,
        gcd_degree=gcd_degree,
        residual_total_degree=degree_p + degree_pm2 - 2 * gcd_degree,
        first_virtual_trace=first_virtual_trace,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--primes",
        nargs="*",
        type=int,
        default=[5, 7, 11],
        help="base characteristics; defaults are focused mechanism tests",
    )
    parser.add_argument(
        "--ell-starts",
        nargs="*",
        type=int,
        default=[10000, 20000, 50000, 100000, 200000],
        help="starting points for split primes ell == 1 mod p",
    )
    args = parser.parse_args()

    for p in args.primes:
        print(f"p={p}: degrees ({airy_degree(p, p)}, {airy_degree(p, p - 2)})")
        for start in args.ell_starts:
            ell = split_prime(p, start)
            result = probe_one(p, ell)
            print(
                f"  ell={ell}: gcd degree={result.gcd_degree}, "
                f"residual total degree={result.residual_total_degree}, "
                f"first virtual trace mod ell={result.first_virtual_trace}"
            )


if __name__ == "__main__":
    main()
