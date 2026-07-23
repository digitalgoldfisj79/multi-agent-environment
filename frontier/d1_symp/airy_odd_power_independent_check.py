#!/usr/bin/env python3
"""Independent residue validation for airy_odd_power_spectra.py.

Uses a different irreducible cubic and fresh coefficient primes.  It checks
p=23,29, the two largest computations, without reusing the CRT primes.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from sympy import isprime, primitive_root


def irreducible_cubics(p: int):
    for a0 in range(1, p):
        for a1 in range(p):
            for a2 in range(p):
                if all((x**3+a2*x*x+a1*x+a0) % p for x in range(p)):
                    yield [a0, a1, a2, 1]


def multiply(a, b, modulus, p):
    out = [0]*5
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] = (out[i+j] + int(ai)*int(bj)) % p
    for degree in (4, 3):
        coefficient = out[degree]
        if coefficient:
            for j in range(3):
                out[degree-3+j] = (out[degree-3+j] - coefficient*modulus[j]) % p
    return np.asarray(out[:3], dtype=np.int64)


def trace_cube_tensor(p, modulus):
    s1 = (-modulus[2]) % p
    s2 = (-(modulus[2]*s1 + 2*modulus[1])) % p
    traces = np.asarray([3 % p, s1, s2], dtype=np.int64)
    tensor = np.empty((p, p, p), dtype=np.int64)
    for a in range(p):
        for b in range(p):
            for c in range(p):
                x = np.asarray([a, b, c], dtype=np.int64)
                x3 = multiply(multiply(x, x, modulus, p), x, modulus, p)
                tensor[a, b, c] = int(np.dot(x3, traces) % p)
    return tensor


def dft3(tensor, p, ell):
    root = pow(int(primitive_root(ell)), (ell-1)//p, ell)
    powers = np.asarray([pow(root, j, ell) for j in range(p)], dtype=np.int64)
    matrix = np.empty((p, p), dtype=np.int64)
    indices = np.arange(p)
    for frequency in range(p):
        matrix[frequency] = powers[(frequency*indices) % p]
    values = powers[tensor]
    values = np.tensordot(matrix, values, axes=(1, 0)) % ell
    values = np.tensordot(matrix, values, axes=(1, 1)) % ell
    values = np.transpose(values, (1, 0, 2))
    values = np.tensordot(matrix, values, axes=(1, 2)) % ell
    return np.transpose(values, (1, 2, 0)).reshape(-1)


def fresh_primes(p, count=2, start=40_000_000):
    result=[]
    k=start//p
    while len(result)<count:
        ell=k*p+1
        k+=1
        if isprime(ell):
            result.append(int(ell))
    return result


def main():
    known=json.loads(Path("frontier/d1_symp/airy_odd_power_spectra_results.json").read_text())
    for p in (23, 29):
        modulus=list(irreducible_cubics(p))[1]
        tensor=trace_cube_tensor(p, modulus)
        q=p**3
        for ell in fresh_primes(p):
            local=dft3(tensor, p, ell)
            h0=np.ones(q, dtype=np.int64)
            h1=(-local) % ell
            hm2, hm1=h0, h1
            selected={}
            for k in range(2, p+1):
                h=(-(local*hm1) - (q % ell)*hm2) % ell
                if k in (p-2, p):
                    selected[k]=int(h.sum(dtype=np.int64) % ell)
                hm2, hm1=hm1, h
            for k, value in selected.items():
                expected=int(known[str(p)][f"Sigma_h3_{k}"]) % ell
                assert value == expected, (p, ell, k, value, expected)
    print("INDEPENDENT RESIDUE CHECKS PASS")


if __name__ == "__main__":
    main()
