#!/usr/bin/env python3
"""Terminal bar-homology probe for the full rank-two C_wedge model.

This implements the reduced weight-n bar complex of the quantum shuffle algebra
A((C_wedge^*)_{-conj(zeta)}) at n=p, where zeta is a primitive p-th root.
For C_wedge with basis v0,v1, the untwisted braiding is

    R(vi tensor vj) = (-1)^(i*j) vj tensor vi.

Hence the quantum-shuffle braiding used below has diagonal coefficients

    q_ij = eta * (-1)^(i*j),   eta = -zeta^(-1).

The differential preserves the number k of v1 letters, so every computation is
split into exact Hamming-weight sectors.

Classification:
- Exact algebraic H_1 ranks over Q(zeta_p): p=3,5,7.
- Exact finite-field bar complexes and ranks in three auxiliary
  characteristics: full homology for p=3,5,7; H_1 only for p=11.
- Agreement across auxiliary primes is a strong modular regression, but the
  p=11 result is not promoted to a characteristic-zero theorem here.
"""

from __future__ import annotations

import argparse
from itertools import combinations
from math import comb
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

import numpy as np

try:
    from numba import njit
except ImportError:  # pragma: no cover
    njit = None

Word = Tuple[int, ...]
Composition = Tuple[int, ...]


def compositions(n: int, r: int) -> Iterable[Composition]:
    for cuts in combinations(range(1, n), r - 1):
        pts = (0,) + cuts + (n,)
        yield tuple(pts[i + 1] - pts[i] for i in range(r))


def words_of_weight(n: int, k: int) -> List[Word]:
    out: List[Word] = []
    for ones in combinations(range(n), k):
        ones_set = set(ones)
        out.append(tuple(1 if i in ones_set else 0 for i in range(n)))
    return out


def primitive_root_mod(prime: int) -> int:
    n = prime - 1
    factors: List[int] = []
    x = n
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        factors.append(x)
    for g in range(2, prime):
        if all(pow(g, n // q, prime) != 1 for q in factors):
            return g
    raise RuntimeError(f"no primitive root found modulo {prime}")


def cwedge_qmatrix(p: int, auxiliary_prime: int) -> Tuple[List[List[int]], int, int]:
    if (auxiliary_prime - 1) % (2 * p) != 0:
        raise ValueError("auxiliary prime must be 1 modulo 2p")
    g = primitive_root_mod(auxiliary_prime)
    zeta = pow(g, (auxiliary_prime - 1) // p, auxiliary_prime)
    eta = (-pow(zeta, -1, auxiliary_prime)) % auxiliary_prime
    q = [[eta, eta], [eta, (-eta) % auxiliary_prime]]
    return q, zeta, eta


def scalar_qmatrix(p: int, auxiliary_prime: int) -> List[List[int]]:
    g = primitive_root_mod(auxiliary_prime)
    zeta = pow(g, (auxiliary_prime - 1) // p, auxiliary_prime)
    return [[zeta]]


def shuffle_product_terms_mod(
    u: Word, v: Word, q: Sequence[Sequence[int]], modulus: int
) -> Dict[Word, int]:
    """Quantum-shuffle product of two words for diagonal braiding."""
    a, b = len(u), len(v)
    n = a + b
    out: Dict[Word, int] = {}
    for positions_u_tuple in combinations(range(n), a):
        positions_u = set(positions_u_tuple)
        iu = iv = 0
        coeff = 1
        word: List[int] = []
        for pos in range(n):
            if pos in positions_u:
                word.append(u[iu])
                iu += 1
            else:
                vv = v[iv]
                for remaining_u in u[iu:]:
                    coeff = (coeff * q[remaining_u][vv]) % modulus
                word.append(vv)
                iv += 1
        output = tuple(word)
        out[output] = (out.get(output, 0) + coeff) % modulus
    return {word: coeff for word, coeff in out.items() if coeff}


def chain_basis(
    n: int, r: int, k: int
) -> Tuple[List[Tuple[Composition, Word]], Mapping[Tuple[Composition, Word], int]]:
    words = words_of_weight(n, k)
    basis = [(composition, word) for composition in compositions(n, r) for word in words]
    return basis, {item: i for i, item in enumerate(basis)}


def differential_matrix_mod(
    n: int, r: int, k: int, q: Sequence[Sequence[int]], modulus: int
) -> np.ndarray:
    """Matrix C_r -> C_(r-1), target rows by source columns."""
    if r < 2:
        raise ValueError("bar differential starts at r=2")
    source, _ = chain_basis(n, r, k)
    target, target_index = chain_basis(n, r - 1, k)
    matrix = np.zeros((len(target), len(source)), dtype=np.int64)
    cache: Dict[Tuple[Word, Word], Dict[Word, int]] = {}

    for column, (composition, word) in enumerate(source):
        offsets = [0]
        for part in composition:
            offsets.append(offsets[-1] + part)
        for i in range(r - 1):
            a, b = composition[i], composition[i + 1]
            u = word[offsets[i] : offsets[i + 1]]
            v = word[offsets[i + 1] : offsets[i + 2]]
            key = (u, v)
            terms = cache.get(key)
            if terms is None:
                terms = shuffle_product_terms_mod(u, v, q, modulus)
                cache[key] = terms
            merged_composition = composition[:i] + (a + b,) + composition[i + 2 :]
            prefix = word[: offsets[i]]
            suffix = word[offsets[i + 2] :]
            sign = 1 if i % 2 == 0 else -1
            for merged_word, coeff in terms.items():
                output_word = prefix + merged_word + suffix
                row = target_index[(merged_composition, output_word)]
                matrix[row, column] = (matrix[row, column] + sign * coeff) % modulus
    return matrix


def _rank_mod_python(matrix: np.ndarray, modulus: int) -> int:
    a = matrix.copy() % modulus
    rows, columns = a.shape
    rank = 0
    for column in range(columns):
        pivots = np.flatnonzero(a[rank:, column])
        if pivots.size == 0:
            continue
        pivot = rank + int(pivots[0])
        if pivot != rank:
            a[[rank, pivot]] = a[[pivot, rank]]
        inverse = pow(int(a[rank, column]), -1, modulus)
        a[rank, :] = (a[rank, :] * inverse) % modulus
        nonzero_rows = np.flatnonzero(a[:, column])
        for row in nonzero_rows:
            if row == rank:
                continue
            factor = int(a[row, column])
            a[row, :] = (a[row, :] - factor * a[rank, :]) % modulus
        rank += 1
        if rank == rows:
            break
    return rank


if njit is not None:
    @njit(cache=True)
    def _inverse_mod_numba(value: int, modulus: int) -> int:
        t, new_t = 0, 1
        r, new_r = modulus, value
        while new_r:
            quotient = r // new_r
            t, new_t = new_t, t - quotient * new_t
            r, new_r = new_r, r - quotient * new_r
        return t + modulus if t < 0 else t

    @njit(cache=True)
    def _rank_mod_numba(matrix: np.ndarray, modulus: int) -> int:
        a = matrix.copy() % modulus
        rows, columns = a.shape
        rank = 0
        for column in range(columns):
            pivot = -1
            for row in range(rank, rows):
                if a[row, column] % modulus != 0:
                    pivot = row
                    break
            if pivot < 0:
                continue
            if pivot != rank:
                temporary = a[rank].copy()
                a[rank] = a[pivot]
                a[pivot] = temporary
            inverse = _inverse_mod_numba(int(a[rank, column]), modulus)
            for j in range(column, columns):
                a[rank, j] = (a[rank, j] * inverse) % modulus
            for row in range(rows):
                if row == rank:
                    continue
                factor = a[row, column] % modulus
                if factor:
                    for j in range(column, columns):
                        a[row, j] = (a[row, j] - factor * a[rank, j]) % modulus
            rank += 1
            if rank == rows:
                break
        return rank


def rank_mod(matrix: np.ndarray, modulus: int) -> int:
    """Exact Gauss-Jordan rank over the prime field F_modulus."""
    if njit is not None:
        return int(_rank_mod_numba(matrix, modulus))
    return _rank_mod_python(matrix, modulus)


def sector_homology_mod(
    n: int, k: int, q: Sequence[Sequence[int]], modulus: int, full: bool
) -> Dict[int, int]:
    max_r = n if full else 2
    ranks = {1: 0}
    matrices: Dict[int, np.ndarray] = {}
    for r in range(2, max_r + 1):
        matrix = differential_matrix_mod(n, r, k, q, modulus)
        matrices[r] = matrix
        ranks[r] = rank_mod(matrix, modulus)
    if full:
        if n <= 5:
            for r in range(3, n + 1):
                if np.any((matrices[r - 1] @ matrices[r]) % modulus):
                    raise AssertionError(f"d^2 != 0 at n={n}, k={k}, r={r}")
        homology: Dict[int, int] = {}
        word_dimension = comb(n, k)
        for r in range(1, n + 1):
            chain_dimension = comb(n - 1, r - 1) * word_dimension
            homology[r] = chain_dimension - ranks.get(r, 0) - ranks.get(r + 1, 0)
        return homology
    return {1: comb(n, k) - ranks[2]}


def shuffle_terms_cyclotomic(u: Word, v: Word, p: int) -> Dict[Word, Tuple[int, ...]]:
    """Coefficients in the basis 1,zeta,...,zeta^(p-2), returned descending."""
    a, b = len(u), len(v)
    n = a + b
    raw: Dict[Word, List[int]] = {}
    for positions_u_tuple in combinations(range(n), a):
        positions_u = set(positions_u_tuple)
        iu = iv = 0
        crossings = odd_crossings = 0
        word: List[int] = []
        for pos in range(n):
            if pos in positions_u:
                word.append(u[iu])
                iu += 1
            else:
                vv = v[iv]
                remaining = u[iu:]
                crossings += len(remaining)
                if vv == 1:
                    odd_crossings += sum(remaining)
                word.append(vv)
                iv += 1
        output = tuple(word)
        coefficients = raw.setdefault(output, [0] * p)
        exponent = (-crossings) % p
        coefficients[exponent] += -1 if (crossings + odd_crossings) % 2 else 1

    reduced: Dict[Word, Tuple[int, ...]] = {}
    for word, coefficients in raw.items():
        last = coefficients[p - 1]
        ascending = [coefficients[j] - last for j in range(p - 1)]
        if any(ascending):
            reduced[word] = tuple(reversed(ascending))
    return reduced


def exact_h1_cyclotomic(p: int, k: int) -> int:
    try:
        import sympy as sp
        from sympy.polys.matrices import DomainMatrix
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("sympy is required for exact cyclotomic ranks") from exc

    x = sp.symbols("x")
    polynomial = sp.Poly(sp.cyclotomic_poly(p, x), x, domain=sp.QQ)
    field = sp.QQ.alg_field_from_poly(polynomial, alias=f"z{p}")
    source, _ = chain_basis(p, 2, k)
    target, target_index = chain_basis(p, 1, k)
    entries: Dict[int, Dict[int, object]] = {}
    cache: Dict[Tuple[Word, Word], Dict[Word, Tuple[int, ...]]] = {}

    for column, (composition, word) in enumerate(source):
        a, _ = composition
        u, v = word[:a], word[a:]
        terms = cache.get((u, v))
        if terms is None:
            terms = shuffle_terms_cyclotomic(u, v, p)
            cache[(u, v)] = terms
        for output_word, coefficients in terms.items():
            element = field.new([sp.QQ(int(value)) for value in coefficients])
            if element != field.zero:
                row = target_index[((p,), output_word)]
                entries.setdefault(row, {})[column] = element

    matrix = DomainMatrix.from_dod(entries, (len(target), len(source)), field)
    return comb(p, k) - matrix.rank()


AUXILIARY_PRIMES = {
    3: (1009, 2017, 3001),
    5: (1021, 1031, 1051),
    7: (1009, 2003, 3011),
    11: (1013, 2003, 3037),
}

EXPECTED_FULL = {
    3: {2: (1, 1), 3: (1, 1)},
    5: {4: (1, 1), 5: (1, 1)},
    7: {2: (1, 1), 3: (2, 2), 4: (1, 1), 6: (1, 1), 7: (1, 1)},
}

EXPECTED_H1_P11 = {2: 1, 3: 2, 4: 2, 5: 4, 6: 6, 7: 4, 8: 1, 10: 1, 11: 1}


def nonzero_profile(
    homology_by_weight: Mapping[int, Mapping[int, int]]
) -> Dict[int, Tuple[int, ...]]:
    profile: Dict[int, Tuple[int, ...]] = {}
    for k, homology in homology_by_weight.items():
        values = tuple(value for _, value in sorted(homology.items()))
        if any(values):
            while values and values[-1] == 0:
                values = values[:-1]
            profile[k] = values
    return profile


def run_scalar_calibration() -> None:
    for p in (3, 5, 7):
        auxiliary_prime = AUXILIARY_PRIMES[p][0]
        q = scalar_qmatrix(p, auxiliary_prime)
        dimensions = [comb(p - 1, r - 1) for r in range(1, p + 1)]
        ranks = {1: 0}
        for r in range(2, p + 1):
            source = list(compositions(p, r))
            target = list(compositions(p, r - 1))
            target_index = {c: i for i, c in enumerate(target)}
            matrix = np.zeros((len(target), len(source)), dtype=np.int64)
            for column, composition in enumerate(source):
                for i in range(r - 1):
                    a, b = composition[i], composition[i + 1]
                    terms = shuffle_product_terms_mod(
                        (0,) * a, (0,) * b, q, auxiliary_prime
                    )
                    coefficient = terms.get((0,) * (a + b), 0)
                    merged = composition[:i] + (a + b,) + composition[i + 2 :]
                    matrix[target_index[merged], column] = (
                        (1 if i % 2 == 0 else -1) * coefficient
                    ) % auxiliary_prime
            ranks[r] = rank_mod(matrix, auxiliary_prime)
        homology = {
            r: dimensions[r - 1] - ranks.get(r, 0) - ranks.get(r + 1, 0)
            for r in range(1, p + 1)
        }
        assert homology[1] == homology[2] == 1
        assert all(homology[r] == 0 for r in range(3, p + 1))
    print("scalar terminal two-line calibration: PASS")


def run_full_small_primes() -> None:
    for p in (3, 5, 7):
        profiles = []
        for auxiliary_prime in AUXILIARY_PRIMES[p]:
            q, _, _ = cwedge_qmatrix(p, auxiliary_prime)
            by_weight = {
                k: sector_homology_mod(p, k, q, auxiliary_prime, full=True)
                for k in range(p + 1)
            }
            profiles.append(nonzero_profile(by_weight))
        assert all(profile == profiles[0] for profile in profiles[1:])
        assert profiles[0] == EXPECTED_FULL[p]
        total = sum(sum(values) for values in profiles[0].values())
        print(f"p={p}: full modular profile {profiles[0]}, total={total}: PASS")


def run_exact_small_primes() -> None:
    for p in (3, 5, 7):
        exact = {k: exact_h1_cyclotomic(p, k) for k in range(p + 1)}
        exact = {k: value for k, value in exact.items() if value}
        expected = {k: values[0] for k, values in EXPECTED_FULL[p].items()}
        assert exact == expected
        print(f"p={p}: exact H_1 over Q(zeta_{p}) {exact}: PASS")


def run_p11_h1(thorough: bool = False) -> None:
    profiles = []
    primes = AUXILIARY_PRIMES[11] if thorough else AUXILIARY_PRIMES[11][:1]
    for auxiliary_prime in primes:
        q, _, _ = cwedge_qmatrix(11, auxiliary_prime)
        profile = {}
        for k in range(12):
            h1 = sector_homology_mod(11, k, q, auxiliary_prime, full=False)[1]
            if h1:
                profile[k] = h1
        profiles.append(profile)
    assert all(profile == profiles[0] for profile in profiles[1:])
    assert profiles[0] == EXPECTED_H1_P11
    total_h1 = sum(profiles[0].values())
    assert total_h1 == 22
    assert total_h1 > 2 * (11 - 1)
    print(
        f"p=11: stable modular H_1 profile {profiles[0]}, "
        "total=22 > 2(p-1)=20: PASS"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-p11", action="store_true")
    parser.add_argument("--skip-exact", action="store_true")
    parser.add_argument(
        "--thorough", action="store_true", help="use all three auxiliary fields at p=11"
    )
    args = parser.parse_args()

    run_scalar_calibration()
    run_full_small_primes()
    if not args.skip_exact:
        run_exact_small_primes()
    if not args.skip_p11:
        run_p11_h1(thorough=args.thorough)
    print("CWEDGE_TERMINAL_BAR_PROBE: PASS")


if __name__ == "__main__":
    main()
