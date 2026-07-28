#!/usr/bin/env python3
"""Ordering-extremality experiment for the reciprocal pair-sum frame
(mechanism M6 of the review; cf. Paper IV Section 11).

For the block primes L = {primes in [X,2X)} and a permutation sigma, form the
path P^s_j = A * prod_{i<=j} l_{sigma(i)} (j=0..K, with P^s_0 = A), the pair
sums S_u = P_i + P_j (i<=j), and the fixed-harmonic (a=1) reciprocal energy

    E^s = sum_{u != v} |Psi(S_u - S_v)|^2,
    Psi(L) = sum_{q in shell} p_q e(L/q),   p_q ~ rho(H/q), rho(t)=exp(-t^2),

with shell = primes in [H, 2H), H = X^2.  Also the distinct-modulus residual
R^s = E^s - M(M-1)*kappa2 (exact decomposition (2.1) of Paper IV).

Question: is the increasing order sigma = id typical, or extremal, among
orderings?  Full enumeration for small K; random sampling for larger K.

Caveat: at these tiny scales (X = 23..40) asymptotic regimes are far away;
the experiment is indicative only.
"""
import itertools, math, random, sys, time
import numpy as np

def primes_in(a, b):
    return [n for n in range(a, b) if n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))]

def experiment(X, n_sample=None, seed=1):
    L = primes_in(X, 2 * X)
    K = len(L)
    A = 1
    for q in primes_in(2, X):
        A *= q
    H = X * X
    shell = primes_in(H, 2 * H)
    Q = len(shell)
    w = np.array([math.exp(-(H / q) ** 2) for q in shell])
    pq = w / w.sum()
    kappa2 = float((pq ** 2).sum())
    N = K + 1
    pairs = [(i, j) for i in range(N) for j in range(i, N)]
    M = len(pairs)

    Amod = np.array([A % q for q in shell], dtype=np.int64)
    Lmod = np.array([[l % q for q in shell] for l in L], dtype=np.int64)  # K x Q
    qarr = np.array(shell, dtype=np.int64)

    diag = M * (M - 1) * kappa2

    def energy(perm):
        # cumulative products mod each q
        cp = np.zeros((N, Q), dtype=np.int64)
        cp[0] = Amod
        for j in range(K):
            cp[j + 1] = (cp[j] * Lmod[perm[j]]) % qarr
        S = np.array([(cp[i] + cp[j]) % qarr for (i, j) in pairs])  # M x Q
        Z = np.exp(2j * np.pi * S / qarr)                           # M x Q
        T = Z.conj().T @ Z                                          # Q x Q : T[r,q]=sum_u zbar_{u,r} z_{u,q}
        G = (np.abs(T) ** 2 - M)
        E = float(pq @ G @ pq)
        return E

    ids = tuple(range(K))
    rev = tuple(reversed(ids))
    results = {}
    if n_sample is None:
        perms = list(itertools.permutations(range(K)))
    else:
        rng = random.Random(seed)
        perms = [ids, rev] + [tuple(rng.sample(range(K), K)) for _ in range(n_sample)]
    vals = np.array([energy(s) for s in perms])
    Eid = energy(ids)
    Erev = energy(rev)
    rank = float((vals < Eid).mean())
    print(f"X={X}  K={K}  M={M}  |shell|={Q}  M(M-1)k2={diag:.2f}  "
          f"{'full enumeration' if n_sample is None else f'{len(perms)} sampled'}")
    print(f"  E(id)={Eid:.3f}  E(rev)={Erev:.3f}  mean={vals.mean():.3f}  "
          f"std={vals.std():.3f}  min={vals.min():.3f}  max={vals.max():.3f}")
    print(f"  residual R(id)={Eid-diag:.3f}  R mean={vals.mean()-diag:.3f}")
    print(f"  percentile of id among orderings: {100*rank:.1f}%  "
          f"(z-score {(Eid-vals.mean())/vals.std():+.2f})")
    return vals, Eid

if __name__ == "__main__":
    t0 = time.time()
    print("== full enumeration, K=6 ==")
    experiment(23)                    # primes 23..43, K=6, 720 orderings
    print("\n== sampled, K=10 ==")
    experiment(40, n_sample=2000)
    print("\n== sampled, X=53 ==")
    experiment(53, n_sample=500)
    print(f"\n[time {time.time()-t0:.1f}s]")
