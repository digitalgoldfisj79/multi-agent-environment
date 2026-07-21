#!/usr/bin/env python3
"""
Order-ensemble numerics for the Fortune programme (Paper II setting).

Question: is the TRUE increasing order of the block primes generic among
orderings for the walk exponential sums at the real problem scale?  This
probes the derandomization gap (RESEARCH_VECTORS.md, B2 gap (ii)): a
random-order model theorem would be vacuous for the real problem if the
increasing order were an outlier of the order ensemble.

For X in {300, 1000, 3000, 10000}:
  L = primes in [X, 2X)  (K of them, the block primes ell_1 < ... < ell_K)
  40 random prime moduli q in [X^2, 2 X^2]   (shell scale H = eta X^2)
  A = (prod of primes < X) mod q             (A_X mod q)
  For an ordering sigma of L, Q_j = prefix product of the first j primes
  in the order sigma (mod q), and the walk statistic is
      V(sigma, q, a) = | sum_{j=1}^{K} e_q(a * A * Q_j) |^2 / K,
  for harmonics a in {1, 2, 3}, where e_q(x) = exp(2 pi i x / q).

Orderings tested per (X, q):
  inc          increasing order (the TRUE order of the programme)
  dec          decreasing order
  rand (x200)  uniformly random orders (fresh per q, fixed global seed)
  adv_spec     "sort primes by ell mod q ascending" -- NOTE: since
               q >= X^2 > 2X > ell, ell mod q = ell, so this coincides
               with inc identically.  Kept and flagged.
  adv_mult     sort primes by (A * ell) mod q ascending -- a genuinely
               q-dependent adversarial order (aligns the first step's
               phase-relevant residues).

Null model: for random phases, V ~ Exp(1) approximately (mean 1, sd 1).

Percentile of a distinguished order within the 200 random orders is
p = (#{V_rand < V} + 0.5 #{V_rand = V}) / 200, computed per (q, a);
over the 40 q values this should be ~ Uniform(0,1) if the order is
exchangeable with random orders.  We report a KS-type max deviation of
the percentile ECDF from uniform (n = 40; 5% critical value ~ 0.215).

Single-walk energy analogue G(sigma,q,a) = (1/K) sum_{i != k}
e_q(aA(Q_i - Q_k)) is NOT computed separately: for a single modulus q it
is an exact linear function of V, since
   sum_{i != k} e_q(aA Q_i) conj(e_q(aA Q_k)) = |sum_j e_q(aAQ_j)|^2 - K
   => G = V - 1  (after the 1/K normalization).
So V carries all the information at fixed q; noted in the writeup.

Diagnostics only, not proofs.  No external dependencies.
"""

import json
import math
import random
import time
import sys
import os

SEED = 20260721
OUTDIR = os.path.dirname(os.path.abspath(__file__))
JSON_OUT = os.path.join(OUTDIR, "order_ensemble_results.json")

N_MODULI = 40
N_RANDOM_ORDERS = 200
HARMONICS = (1, 2, 3)
X_VALUES = (300, 1000, 3000, 10000)
TIME_BUDGET_SECONDS = 480  # skip X=10000 if the smaller X's already ate this

TWO_PI = 2.0 * math.pi


# ----------------------------------------------------------------------
# primality / prime generation
# ----------------------------------------------------------------------
def sieve(limit):
    """Primes < limit."""
    bs = bytearray([1]) * limit
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(limit ** 0.5) + 1):
        if bs[i]:
            bs[i * i:limit:i] = bytearray(len(range(i * i, limit, i)))
    return [i for i in range(limit) if bs[i]]


def is_prime(n):
    """Deterministic Miller-Rabin for n < 3.3e24 (bases cover our range)."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def random_prime_in(lo, hi, rng):
    while True:
        c = rng.randrange(lo, hi + 1) | 1
        if c <= hi and is_prime(c):
            return c


# ----------------------------------------------------------------------
# walk statistic
# ----------------------------------------------------------------------
def walk_V(order, q, A, harmonics):
    """V(sigma,q,a) for each harmonic a: |sum_j e_q(a*A*Q_j)|^2 / K."""
    K = len(order)
    # prefix products t_j = A * Q_j mod q
    ts = []
    cur = A
    for ell in order:
        cur = cur * ell % q
        ts.append(cur)
    w = TWO_PI / q
    out = {}
    for a in harmonics:
        sr = 0.0
        si = 0.0
        for t in ts:
            ph = w * ((a * t) % q)
            sr += math.cos(ph)
            si += math.sin(ph)
        out[a] = (sr * sr + si * si) / K
    return out


def percentile_within(value, ensemble_sorted):
    """(#below + 0.5*#equal)/n via binary search on a sorted list."""
    import bisect
    lo = bisect.bisect_left(ensemble_sorted, value)
    hi = bisect.bisect_right(ensemble_sorted, value)
    n = len(ensemble_sorted)
    return (lo + 0.5 * (hi - lo)) / n


def ks_uniform(ps):
    """Max deviation of the ECDF of ps from Uniform(0,1)."""
    ps = sorted(ps)
    n = len(ps)
    d = 0.0
    for i, p in enumerate(ps):
        d = max(d, abs((i + 1) / n - p), abs(p - i / n))
    return d


def mean_sd(xs):
    n = len(xs)
    m = sum(xs) / n
    v = sum((x - m) ** 2 for x in xs) / (n - 1) if n > 1 else 0.0
    return m, math.sqrt(v)


# ----------------------------------------------------------------------
# main experiment
# ----------------------------------------------------------------------
def run_X(X, rng):
    t0 = time.time()
    primes_2X = sieve(2 * X)
    small = [p for p in primes_2X if p < X]          # primes < X (for A_X)
    block = [p for p in primes_2X if X <= p < 2 * X]  # block primes
    K = len(block)

    moduli = []
    seen = set()
    while len(moduli) < N_MODULI:
        q = random_prime_in(X * X, 2 * X * X, rng)
        if q not in seen:
            seen.add(q)
            moduli.append(q)

    # Distinguished orders independent of q
    inc = list(block)
    dec = list(reversed(block))

    # per-q results
    per_q = []
    # accumulators across q, keyed by harmonic
    acc = {a: {"rand_means": [], "rand_sds": [],
               "V_inc": [], "V_dec": [], "V_adv_spec": [], "V_adv_mult": [],
               "pct_inc": [], "pct_dec": [], "pct_adv_spec": [],
               "pct_adv_mult": []} for a in HARMONICS}

    for qi, q in enumerate(moduli):
        A = 1
        for p in small:
            A = A * p % q

        adv_spec = sorted(block, key=lambda ell: ell % q)   # == inc, flagged
        adv_mult = sorted(block, key=lambda ell: (A * ell) % q)

        V_inc = walk_V(inc, q, A, HARMONICS)
        V_dec = walk_V(dec, q, A, HARMONICS)
        V_as = walk_V(adv_spec, q, A, HARMONICS)
        V_am = walk_V(adv_mult, q, A, HARMONICS)

        rand_vals = {a: [] for a in HARMONICS}
        order = list(block)
        for _ in range(N_RANDOM_ORDERS):
            rng.shuffle(order)
            V = walk_V(order, q, A, HARMONICS)
            for a in HARMONICS:
                rand_vals[a].append(V[a])

        row = {"q": q, "adv_spec_equals_inc": adv_spec == inc}
        for a in HARMONICS:
            ens = sorted(rand_vals[a])
            m, s = mean_sd(ens)
            acc[a]["rand_means"].append(m)
            acc[a]["rand_sds"].append(s)
            for tag, V in (("inc", V_inc), ("dec", V_dec),
                           ("adv_spec", V_as), ("adv_mult", V_am)):
                acc[a]["V_" + tag].append(V[a])
                acc[a]["pct_" + tag].append(percentile_within(V[a], ens))
            row[f"a{a}"] = {
                "rand_mean": m, "rand_sd": s,
                "V_inc": V_inc[a], "V_dec": V_dec[a],
                "V_adv_spec": V_as[a], "V_adv_mult": V_am[a],
                "pct_inc": acc[a]["pct_inc"][-1],
                "pct_dec": acc[a]["pct_dec"][-1],
                "pct_adv_spec": acc[a]["pct_adv_spec"][-1],
                "pct_adv_mult": acc[a]["pct_adv_mult"][-1],
            }
        per_q.append(row)
        if (qi + 1) % 10 == 0:
            print(f"  X={X}: modulus {qi+1}/{N_MODULI} "
                  f"({time.time()-t0:.1f}s)", flush=True)

    summary = {}
    for a in HARMONICS:
        s = acc[a]
        rm, _ = mean_sd(s["rand_means"])
        rs, _ = mean_sd(s["rand_sds"])
        entry = {"rand_mean_over_q": rm, "rand_sd_over_q": rs}
        for tag in ("inc", "dec", "adv_spec", "adv_mult"):
            vm, vs = mean_sd(s["V_" + tag])
            ps = s["pct_" + tag]
            pm, psd = mean_sd(ps)
            entry[tag] = {
                "V_mean": vm, "V_sd": vs,
                "pct_mean": pm, "pct_sd": psd,
                "pct_min": min(ps), "pct_max": max(ps),
                "ks_D": ks_uniform(ps),
                "n_below_05": sum(1 for p in ps if p < 0.05),
                "n_above_95": sum(1 for p in ps if p > 0.95),
                # effect size: (mean V of the order - rand mean)/(rand sd/sqrt(n_q))
                "z_of_meanV": ((vm - rm) / (rs / math.sqrt(len(ps))))
                if rs > 0 else 0.0,
            }
        summary[f"a={a}"] = entry

    return {
        "X": X, "K": K, "n_moduli": N_MODULI,
        "n_random_orders": N_RANDOM_ORDERS,
        "adv_spec_note": "sort by ell mod q == increasing order for all q "
                         "(q >= X^2 > 2X > ell); kept as a consistency check",
        "runtime_seconds": round(time.time() - t0, 1),
        "summary": summary,
        "per_q": per_q,
    }


def main():
    rng = random.Random(SEED)
    t_start = time.time()
    results = {"seed": SEED, "harmonics": list(HARMONICS),
               "ks_critical_5pct_n40": 1.358 / math.sqrt(N_MODULI),
               "runs": []}
    for X in X_VALUES:
        elapsed = time.time() - t_start
        if X == 10000 and elapsed > TIME_BUDGET_SECONDS:
            print(f"Skipping X={X}: elapsed {elapsed:.0f}s over budget",
                  flush=True)
            results["skipped"] = [X]
            break
        print(f"Running X={X} (elapsed {elapsed:.0f}s)", flush=True)
        results["runs"].append(run_X(X, rng))
    with open(JSON_OUT, "w") as f:
        json.dump(results, f, indent=1)
    print(f"Wrote {JSON_OUT} (total {time.time()-t_start:.0f}s)")


if __name__ == "__main__":
    main()
