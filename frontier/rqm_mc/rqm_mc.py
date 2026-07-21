#!/usr/bin/env python3
"""
G2 Monte Carlo diagnostic for the RQM assembly target (Theorem RQM, provable-sketch).

Estimates E_sigma[E_1] empirically at small scales X in {40,60,80,120} and compares
with the claimed C * M * (log X)^{C0} law.  DIAGNOSTIC ONLY, NOT A PROOF.

Conventions (stated explicitly, following Paper II Sec. 3 and the task spec):
  - Block primes: ell in [X, 2X), K of them; centres P_j = A_X * prod_{i<=j} ell_{sigma(i)},
    j = 0..K, with A_X = prod_{p<X} p (exact Python big ints; reduced mod q per shell prime).
    N = K+1 centres; pair sums S_u = P_j + P_k over multisets u = {j,k}, j<=k; M = N(N+1)/2.
  - Shell: primes q in [H, 2H), H = 0.5 * X^2  (eta = 0.5).
  - Weights: rho(x) = exp(-x^2) (smooth even bump, our fixed simple choice), harmonics
    restricted to 1 <= |a| <= 8; w_{q,a} = rho(H a / q); p_{q,a} = w_{q,a}/D_X with
    D_X = sum_{q in shell} sum_{0<|a|<=8} w_{q,a}, so that sum_{q,a!=0} p_{q,a} = 1
    (Paper II (3.3) restricted to |a|<=8; the tail |a|>8 of exp(-x^2) with H/q in (1/2,1]
    is < 1e-27 relative, so the truncation is numerically irrelevant).
  - E_1 = sum_{u != v} |Psi_1(S_u - S_v)|^2 with Psi_1(L) = sum_q p_{q,1} e(L/q),
    computed exactly (residues S_u mod q via exact integer arithmetic, then complex
    phases in double precision; vectorized over shell primes with numpy).
  - Exact diagonal (q = r sector): M(M-1) * kappa_2, kappa_2 = sum_q p_{q,1}^2.
    Residual R_1 = E_1 - M(M-1)*kappa_2 (the q != r sector, the quantity the
    character machinery actually bounds).
  - Dichotomy split: for ordered pairs (u,v), u != v, multiset overlap |u cap v| is
    0 (Sidon part, 4 distinct rank slots up to coincidences) or 1 (sliding family:
    D_uv = P_k - P_{k'}, multiplicity ~ N over the shared index).  We report
    E_slide, E_sidon (E_1 = E_slide + E_sidon exactly) and N*G_1 with
    G_1 = sum_{k != k'} |Psi_1(P_k - P_{k'})|^2, to check E_slide ~ N*G_1.

Also: independent re-verification of the exact partition identity (Lemma 3.1 of
v1.rigor.json) at K = 7 against the true permutation law, with fresh code.
"""

import json, math, time, itertools
from fractions import Fraction
import numpy as np

RNG = np.random.default_rng(20260721)
OUT = {}

def primes_in(lo, hi):
    sieve = np.ones(hi, dtype=bool); sieve[:2] = False
    for i in range(2, int(hi**0.5) + 1):
        if sieve[i]: sieve[i*i::i] = False
    return [int(p) for p in np.nonzero(sieve)[0] if p >= lo]

# ----------------------------------------------------------------------------
# Part 1: exact partition identity re-verification at K = 7 (own code)
# ----------------------------------------------------------------------------
def dlog_table(q, g):
    t, x = {}, 1
    for e in range(q - 1):
        t[x] = e; x = (x * g) % q
    return t

def char_val(q, dl, order_exp, n):
    """chi(n) = e(order_exp * dlog(n) / (q-1)) as exact Fraction exponent."""
    return Fraction(order_exp * dl[n % q], q - 1)

def verify_partition_identity():
    """E_sigma[prod_s psi_s(prod W_s)] over ALL K! permutations of a 7-prime block,
    cells = consecutive sigma-positions of sizes n = (n_0..n_m), vs the multinomial
    coefficient extraction of prod_ell (sum_s x_s psi_s(ell)). Exact up to float eps."""
    q = 11; g = 2; dl = dlog_table(q, g)
    L = [41, 43, 47, 53, 59, 61, 67]  # 7 block primes, all units mod 11
    K = len(L)
    results = []
    configs = [
        ((3, 2, 2), (1, 3, 7)),     # three cells, distinct nonprincipal characters
        ((2, 2, 2, 1), (2, 5, 1, 8)),
        ((3, 2, 2), (0, 3, 3)),     # principal + repeated characters
        ((4, 3), (4, 9)),
        ((1, 5, 1), (7, 2, 6)),     # micro cells
    ]
    for sizes, exps in configs:
        m = len(sizes)
        # character value tables psi_s(ell) as complex
        psi = [[complex(np.exp(2j * np.pi * float(char_val(q, dl, e, ell)))) for ell in L]
               for e in exps]
        # (a) true permutation law, all K! = 5040 orderings
        tot = 0.0 + 0.0j
        bounds = np.cumsum((0,) + sizes)
        for perm in itertools.permutations(range(K)):
            v = 1.0 + 0.0j
            for s in range(m):
                for pos in range(bounds[s], bounds[s + 1]):
                    v *= psi[s][perm[pos]]
            tot += v
        lhs = tot / math.factorial(K)
        # (b) coefficient extraction: prod_ell (sum_s x_s psi_s(ell)), coefficient of
        # x^sizes, divided by multinomial(K; sizes)
        poly = {(0,) * m: 1.0 + 0.0j}
        for i in range(K):
            new = {}
            for mono, c in poly.items():
                for s in range(m):
                    if mono[s] < sizes[s]:
                        mo = list(mono); mo[s] += 1; mo = tuple(mo)
                        new[mo] = new.get(mo, 0.0 + 0.0j) + c * psi[s][i]
            poly = new
        multinom = math.factorial(K)
        for n in sizes: multinom //= math.factorial(n)
        rhs = poly.get(tuple(sizes), 0.0 + 0.0j) / multinom
        results.append({
            "sizes": list(sizes), "char_exps": list(exps),
            "E_permutation_law": [lhs.real, lhs.imag],
            "E_coeff_extraction": [rhs.real, rhs.imag],
            "abs_diff": abs(lhs - rhs)})
    return results

# ----------------------------------------------------------------------------
# Part 2: Monte Carlo E_1 over random orderings
# ----------------------------------------------------------------------------
AMAX = 8  # harmonic truncation for the normalization D_X

def setup_scale(X):
    ell = primes_in(X, 2 * X)
    K = len(ell); N = K + 1
    A_X = 1
    for p in primes_in(2, X): A_X *= p
    H = 0.5 * X * X
    shell = primes_in(int(math.ceil(H)), int(2 * H))
    qarr = np.array(shell, dtype=np.int64)
    # weights
    W = np.zeros(len(shell))
    D = 0.0
    for a in range(1, AMAX + 1):
        wa = np.exp(-(H * a / qarr.astype(float)) ** 2)
        D += 2.0 * wa.sum()
        if a == 1: W = wa.copy()
    p1 = W / D                      # p_{q,1}
    m1 = p1.sum()
    kappa2 = (p1 ** 2).sum()
    Ares = np.array([A_X % int(q) for q in shell], dtype=np.int64)
    # multiset pair index arrays
    ju, ku = [], []
    for j in range(N):
        for k in range(j, N):
            ju.append(j); ku.append(k)
    ju = np.array(ju); ku = np.array(ku)
    M = len(ju)
    # overlap classification for ordered pairs (u,v), u != v
    us = np.stack([ju, ku], axis=1)
    ov = np.zeros((M, M), dtype=np.int8)
    for i in range(M):
        a1, b1 = us[i]
        for j2 in range(M):
            if i == j2: continue
            a2, b2 = us[j2]
            # multiset intersection size of {a1,b1} and {a2,b2}
            c = 0; pool = [a2, b2]
            for x in (a1, b1):
                if x in pool: pool.remove(x); c += 1
            ov[i, j2] = c
    return dict(X=X, ell=ell, K=K, N=N, M=M, H=H, shell=qarr, p1=p1, m1=m1,
                kappa2=kappa2, Ares=Ares, ju=ju, ku=ku, ov=ov)

def energies_for_order(sc, order):
    """E_1, R_1, E_slide, E_sidon, N*G_1 for a given ordering (list of block primes)."""
    qarr = sc["shell"]; p1 = sc["p1"]; N = sc["N"]
    # prefix-product residues P_j mod q, j = 0..K  (P_0 = A_X)
    Pres = np.empty((N, len(qarr)), dtype=np.int64)
    Pres[0] = sc["Ares"]
    for j, l in enumerate(order):
        Pres[j + 1] = (Pres[j] * l) % qarr
    Sres = (Pres[sc["ju"]] + Pres[sc["ku"]]) % qarr        # (M, Q)
    V = np.exp(2j * np.pi * Sres / qarr)                    # (M, Q)
    Psi = (V * p1) @ V.conj().T                             # (M, M): Psi_1(S_u - S_v)
    A2 = np.abs(Psi) ** 2
    np.fill_diagonal(A2, 0.0)
    E1 = A2.sum()
    E_slide = A2[sc["ov"] == 1].sum()
    E_sidon = A2[sc["ov"] == 0].sum()
    M = sc["M"]
    R1 = E1 - M * (M - 1) * sc["kappa2"]
    # G_1 over centre differences
    WV = np.exp(2j * np.pi * Pres / qarr)
    Phi = (WV * p1) @ WV.conj().T
    B2 = np.abs(Phi) ** 2
    np.fill_diagonal(B2, 0.0)
    G1 = B2.sum()
    return E1, R1, E_slide, E_sidon, N * G1

def run_scale(X, nsigma=120):
    t0 = time.time()
    sc = setup_scale(X)
    K = sc["K"]
    ell_sorted = list(sc["ell"])
    rows = []
    for s in range(nsigma):
        perm = RNG.permutation(K)
        order = [ell_sorted[i] for i in perm]
        rows.append(energies_for_order(sc, order))
    rows = np.array(rows)
    inc = np.array(energies_for_order(sc, ell_sorted))
    M = sc["M"]
    res = dict(
        X=X, K=K, N=sc["N"], M=M, Q=len(sc["shell"]), H=sc["H"],
        m1=float(sc["m1"]), kappa2=float(sc["kappa2"]),
        diag_term=float(M * (M - 1) * sc["kappa2"]),
        nsigma=nsigma,
        mean=dict(zip(["E1", "R1", "E_slide", "E_sidon", "NG1"], rows.mean(0).tolist())),
        sd=dict(zip(["E1", "R1", "E_slide", "E_sidon", "NG1"], rows.std(0, ddof=1).tolist())),
        increasing=dict(zip(["E1", "R1", "E_slide", "E_sidon", "NG1"], inc.tolist())),
        mean_over_M=dict(zip(["E1", "R1", "E_slide", "E_sidon", "NG1"],
                             (rows.mean(0) / M).tolist())),
        sd_over_M=dict(zip(["E1", "R1", "E_slide", "E_sidon", "NG1"],
                           (rows.std(0, ddof=1) / M).tolist())),
        increasing_over_M=dict(zip(["E1", "R1", "E_slide", "E_sidon", "NG1"],
                                   (inc / M).tolist())),
        runtime_s=time.time() - t0)
    return res

def main():
    OUT["convention"] = {
        "eta": 0.5, "H": "0.5*X^2", "rho": "exp(-x^2)", "harmonic_truncation_for_DX": AMAX,
        "normalization": "sum_{q in shell,[1<=|a|<=8]} p_{q,a} = 1",
        "a_reported": 1, "seed": 20260721,
        "note": "E_1 exact residue arithmetic; phases in double precision"}
    print("Part 1: partition identity at K=7 ...")
    OUT["partition_identity_K7"] = verify_partition_identity()
    for r in OUT["partition_identity_K7"]:
        print("  sizes", r["sizes"], "chars", r["char_exps"], "absdiff %.3e" % r["abs_diff"])
    OUT["scales"] = []
    for X in (40, 60, 80, 120):
        print(f"Part 2: X = {X} ...")
        res = run_scale(X, nsigma=120)
        OUT["scales"].append(res)
        print(f"  K={res['K']} M={res['M']} Q={res['Q']} "
              f"mean E1/M={res['mean_over_M']['E1']:.4f} sd={res['sd_over_M']['E1']:.4f} "
              f"R1/M={res['mean_over_M']['R1']:.4f} diag/M={res['diag_term']/res['M']:.4f} "
              f"inc E1/M={res['increasing_over_M']['E1']:.4f}  ({res['runtime_s']:.1f}s)")
    # polylog fit: mean(E1/M) and mean(R1/M) vs (log X)^c  -> slope in loglog(logX)
    xs = np.array([r["X"] for r in OUT["scales"]], dtype=float)
    fits = {}
    for key in ("E1", "R1", "E_slide", "E_sidon", "NG1"):
        ys = np.array([r["mean_over_M"][key] for r in OUT["scales"]])
        mask = ys > 0
        if mask.sum() >= 2:
            c, lc = np.polyfit(np.log(np.log(xs[mask])), np.log(ys[mask]), 1)
            fits[key] = {"polylog_exponent_c": float(c), "prefactor": float(np.exp(lc)),
                         "values_over_M": ys.tolist()}
        else:
            fits[key] = {"polylog_exponent_c": None, "values_over_M": ys.tolist()}
        # also power-law fit in X for contrast
        if mask.sum() >= 2:
            a, la = np.polyfit(np.log(xs[mask]), np.log(ys[mask]), 1)
            fits[key]["power_law_exponent_in_X"] = float(a)
    OUT["fits_mean_over_M"] = fits
    with open("/home/user/multi-agent-environment/frontier/rqm_mc/results.json", "w") as f:
        json.dump(OUT, f, indent=1)
    print("fits:", json.dumps(fits, indent=1))

if __name__ == "__main__":
    main()
