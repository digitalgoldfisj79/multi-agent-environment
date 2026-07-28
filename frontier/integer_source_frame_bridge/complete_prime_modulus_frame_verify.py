#!/usr/bin/env python3
"""Verify the complete prime-modulus centred frame and finite calibration."""
from __future__ import annotations

import cmath
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from sympy import primerange

ETA = 0.8
TARGETS = (11, 23, 53, 131, 257, 503)


def block_data(X: int) -> tuple[list[int], list[int], int, list[int]]:
    ell = [int(p) for p in primerange(X, 2 * X)]
    H = int(ETA * X * X)
    qs = [int(q) for q in primerange(H, 2 * H)]
    prefix = [1]
    for p in ell:
        prefix.append(prefix[-1] * p)
    return ell, qs, H, prefix


def divisor_frame(X: int) -> dict:
    ell, qs, H, prefix = block_data(X)
    N = len(ell)
    Q = len(qs)
    if not N or not Q:
        raise RuntimeError(f"empty block or shell at X={X}")

    A = 1
    for p in primerange(2, X):
        A *= int(p)

    matrix = np.eye(N, dtype=float)
    gap_histogram: Counter[int] = Counter()
    nonzero_pairs = 0
    max_divisor_count = 0
    for j in range(N):
        for k in range(j + 1, N):
            U = prefix[k] // prefix[j]
            count = sum(1 for q in qs if (U - 1) % q == 0)
            max_divisor_count = max(max_divisor_count, count)
            matrix[j, k] = matrix[k, j] = count / Q
            if count:
                nonzero_pairs += 1
                gap_histogram[k - j] += count

            # Check the exact removal of the common primorial factor modulo q.
            Pj = A * prefix[j]
            Pk = A * prefix[k]
            for q in qs[: min(20, Q)]:
                assert ((Pk - Pj) % q == 0) == ((U - 1) % q == 0)

    eigenvalues = np.linalg.eigvalsh(matrix)
    off = matrix - np.eye(N)
    row_sums = off.sum(axis=1)
    theorem_bound = (
        N * (N - 1) * math.log(2 * X) / (2 * Q * math.log(H))
    )
    operator_norm = float(np.max(np.abs(eigenvalues - 1.0)))
    max_row = float(np.max(row_sums))

    assert operator_norm <= max_row + 1e-12
    assert max_row <= theorem_bound + 1e-12
    assert eigenvalues[0] > 0

    return {
        "X": X,
        "N": N,
        "H": H,
        "q_shell_count": Q,
        "minimum_eigenvalue": float(eigenvalues[0]),
        "maximum_eigenvalue": float(eigenvalues[-1]),
        "operator_norm_D_minus_I": operator_norm,
        "maximum_off_diagonal_row_sum": max_row,
        "total_off_diagonal_mass": float(off.sum()),
        "nonzero_off_diagonal_pairs": nonzero_pairs,
        "maximum_shell_divisor_count": max_divisor_count,
        "theorem_row_bound": theorem_bound,
        "gap_divisor_histogram": {
            str(gap): gap_histogram[gap] for gap in sorted(gap_histogram)
        },
    }


def direct_character_check() -> dict:
    X = 5
    ell, qs, H, prefix = block_data(X)
    N = len(ell)
    A = 1
    for p in primerange(2, X):
        A *= int(p)
    centres = [A * prefix[j] for j in range(N)]
    c = [complex(2, -1), complex(-3, 2), complex(1, 4)][:N]

    lhs = 0.0
    for q in qs:
        local = 0.0
        for a in range(q):
            value = sum(
                c[j] * cmath.exp(2j * math.pi * a * (centres[j] % q) / q)
                for j in range(N)
            )
            local += abs(value) ** 2
        lhs += local / q
    lhs /= len(qs)

    rhs = 0j
    for j in range(N):
        for k in range(N):
            kernel = sum(
                1 for q in qs if (centres[j] - centres[k]) % q == 0
            ) / len(qs)
            rhs += c[j] * c[k].conjugate() * kernel

    error = abs(lhs - rhs.real)
    assert error < 1e-10
    return {
        "X": X,
        "N": N,
        "H": H,
        "q_shell_count": len(qs),
        "direct_character_energy": lhs,
        "gram_energy": rhs.real,
        "identity_error": error,
        "imaginary_residue": abs(rhs.imag),
    }


def main() -> None:
    rows = [divisor_frame(X) for X in TARGETS]
    check = direct_character_check()
    payload = {
        "status": "PASS",
        "scope": "exact complete-character identity and finite prime-modulus frame calibration",
        "parameters": {"eta": ETA, "targets": list(TARGETS)},
        "direct_character_check": check,
        "summary": {
            "minimum_eigenvalue": min(r["minimum_eigenvalue"] for r in rows),
            "maximum_eigenvalue": max(r["maximum_eigenvalue"] for r in rows),
            "maximum_operator_norm": max(r["operator_norm_D_minus_I"] for r in rows),
            "maximum_row_sum": max(r["maximum_off_diagonal_row_sum"] for r in rows),
            "largest_X": max(TARGETS),
        },
        "rows": rows,
        "boundary": (
            "Finite calibration is not used to prove the asymptotic theorem; "
            "the uniform frame bound follows from shell-divisor counting and the PNT."
        ),
    }
    path = Path(__file__).with_name("complete_prime_modulus_frame_results.json")
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
