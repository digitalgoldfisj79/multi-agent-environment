#!/usr/bin/env python3
"""Exact F^3 traces on the mu_3-invariant cubic-Airy moment spaces.

For p == 5 (mod 6), odd Frobenius powers exchange the two nontrivial
mu_3 eigenspaces, so their traces vanish.  The full H_c^1 trace therefore
equals the invariant trace.  This script computes the m=3 traces by an
exact p-ary DFT over coefficient primes ell == 1 (mod p), then reconstructs
the signed integer by CRT.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from sympy import isprime, primitive_root
from sympy.ntheory.modular import crt

PRIMES = (11, 17, 23, 29)


def find_irreducible_cubic(p: int) -> list[int]:
    """Low-to-high coefficients of a monic irreducible cubic over F_p."""
    # A cubic is irreducible iff it has no F_p root.
    for a0 in range(1, p):
        for a1 in range(p):
            for a2 in range(p):
                if all((x**3 + a2*x*x + a1*x + a0) % p for x in range(p)):
                    return [a0, a1, a2, 1]
    raise RuntimeError(f"no irreducible cubic found for p={p}")


def multiply(a: np.ndarray, b: np.ndarray, modulus: list[int], p: int) -> np.ndarray:
    out = [0] * 5
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[i+j] = (out[i+j] + int(ai)*int(bj)) % p
    for degree in (4, 3):
        coefficient = out[degree] % p
        if coefficient:
            for j in range(3):
                out[degree-3+j] = (out[degree-3+j] - coefficient*modulus[j]) % p
    return np.asarray(out[:3], dtype=np.int64)


def cube_trace_tensor(p: int) -> tuple[list[int], list[int], np.ndarray]:
    modulus = find_irreducible_cubic(p)
    # Newton sums for 1, theta, theta^2 in F_{p^3}.
    trace_theta = (-modulus[2]) % p
    trace_theta2 = (-(modulus[2]*trace_theta + 2*modulus[1])) % p
    trace_basis = np.asarray([3 % p, trace_theta, trace_theta2], dtype=np.int64)
    tensor = np.empty((p, p, p), dtype=np.int64)
    for a in range(p):
        for b in range(p):
            for c in range(p):
                x = np.asarray([a, b, c], dtype=np.int64)
                x3 = multiply(multiply(x, x, modulus, p), x, modulus, p)
                tensor[a, b, c] = int(np.dot(x3, trace_basis) % p)
    return modulus, trace_basis.tolist(), tensor


def split_primes(p: int, count: int, start: int = 30_000_000) -> list[int]:
    result: list[int] = []
    k = (start - 1 + p - 1) // p
    while len(result) < count:
        ell = k*p + 1
        if isprime(ell):
            result.append(int(ell))
        k += 1
    return result


def dft3_mod(cube_traces: np.ndarray, p: int, ell: int) -> np.ndarray:
    root = pow(int(primitive_root(ell)), (ell-1)//p, ell)
    assert root != 1 and pow(root, p, ell) == 1
    powers = np.asarray([pow(root, j, ell) for j in range(p)], dtype=np.int64)
    matrix = np.empty((p, p), dtype=np.int64)
    indices = np.arange(p)
    for frequency in range(p):
        matrix[frequency] = powers[(frequency*indices) % p]
    values = powers[cube_traces]
    # Every matrix product is reduced modulo ell before the next one; int64 is safe.
    values = np.tensordot(matrix, values, axes=(1, 0)) % ell
    values = np.tensordot(matrix, values, axes=(1, 1)) % ell
    values = np.transpose(values, (1, 0, 2))
    values = np.tensordot(matrix, values, axes=(1, 2)) % ell
    values = np.transpose(values, (1, 2, 0))
    return values.reshape(-1)


def signed_crt(moduli: list[int], residues: list[int]) -> tuple[int, int]:
    value, modulus = crt(moduli, residues)
    value, modulus = int(value), int(modulus)
    if value > modulus // 2:
        value -= modulus
    return value, modulus


def compute(primes: tuple[int, ...] = PRIMES) -> dict[str, object]:
    output: dict[str, object] = {}
    for p in primes:
        q = p**3
        field_poly, trace_basis, cube_traces = cube_trace_tensor(p)
        rank = (p-5)//6
        # Deligne bound for Tr(F^3|U_p); it dominates the adjacent bound.
        bound = max(1, rank) * p**(3*(p+1)//2)
        count = math.ceil((math.log2(2*bound)+10)/math.log2(30_000_000)) + 1
        moduli = split_primes(p, count)
        residues = {p-2: [], p: []}
        for ell in moduli:
            local_sum = dft3_mod(cube_traces, p, ell)
            h_previous_previous = np.ones(q, dtype=np.int64)
            h_previous = (-local_sum) % ell
            selected: dict[int, int] = {}
            for k in range(2, p+1):
                current = (-(local_sum*h_previous) - (q % ell)*h_previous_previous) % ell
                if k in (p-2, p):
                    selected[k] = int(current.sum(dtype=np.int64) % ell)
                h_previous_previous, h_previous = h_previous, current
            for k, residue in selected.items():
                residues[k].append(residue)
        record: dict[str, object] = {
            "field_polynomial": field_poly,
            "trace_basis": trace_basis,
            "coefficient_primes": moduli,
        }
        for k in (p-2, p):
            sigma, modulus = signed_crt(moduli, residues[k])
            assert modulus > 2*bound
            record[f"Sigma_h3_{k}"] = sigma
            record[f"TrU3_{k}"] = -sigma
            record[f"crt_modulus_bits_{k}"] = modulus.bit_length()
        output[str(p)] = record
    return output


def main() -> None:
    result = compute()
    path = Path("frontier/d1_symp/airy_odd_power_spectra_results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
