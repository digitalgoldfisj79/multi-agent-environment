# d=1 crown push — Phase Z2 big-compute campaign

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Purpose:** use large parallel computation only on proof-relevant gates already reduced to exact finite-dimensional objects.

## Campaign A — Cartier complementary-minor exclusion

Goal: test and structurally classify the dominant corrected support statement

`beta <= gamma+2`

for every nonzero complementary-minor product.

Tasks:

1. enumerate admissible `(E,R)` by torus grading rather than determinant assignments;
2. evaluate the two exact modular minors
   `det(P^-1)_(R,E union {0})` and `det(U)_(R,E union {p-3})`;
3. search specifically for `beta-gamma>=4`;
4. record the first counterexample if one exists;
5. otherwise classify all nonzero cases by interlacing/path data and infer a nonintersecting-forest theorem.

Initial exact range: every prime through 101, extended as runtime permits.

## Campaign B — odd-locus cubic mass

For

`F_(c,0)(X)=X H_c(X^2)`, `H_c(Y)=Y^((p-1)/2)+aY+c`,

compute the projected degree-three factor count `R_3(c)` and its first three factorial moments for both square classes.

Tasks:

1. exact prime sweep through at least 499;
2. separate elementary polynomial terms from Frobenius residuals;
3. search for fixed elliptic/genus-two trace models;
4. compute zeta fingerprints over `F_p` and `F_(p^2)` for candidate curves;
5. produce a theorem-level parametrisation or a precise residual motive.

## Campaign C — cubic mixed-surface fingerprints

For the exact surfaces defining

`M_33=sum binom(Q_3,2)`, `M_13=sum LQ_3`, `M_23=sum Q_2Q_3`,

compute exact data over many primes and both square classes.

Tasks:

1. subtract diagonal, first masses, odd locus, and explicit boundary components;
2. compute residual traces over `F_p` and, where feasible, `F_(p^2)`;
3. test whether residuals factor through fixed elliptic/genus-two traces, quadratic twists, or products already present in the programme;
4. estimate geometric rank from the normalized trace envelope;
5. return exact candidate trace identities or counterevidence.

## Campaign D — all-degree finite sieve stress test

Using exact factorisation of every slice member for moderate primes:

1. construct the full factor-degree cycle index;
2. compare exact irreducible counts against truncations at degrees 1,2,3,...;
3. identify a signed Bonferroni or cycle-index truncation that is uniformly positive in the computed range;
4. isolate the first missing moment needed to make that truncation rigorous.

This is diagnostic: finite positivity is not a proof.

## Evidence and stop rules

- No floating point for identities or counterexamples.
- Every executable, raw output and synthesis note is committed.
- GPU is used only where it accelerates batched finite-field arithmetic; high-core CPU is preferred for branch-heavy exact enumeration.
- Stop immediately on a counterexample to a proposed uniform lemma.
- A compute pattern is not promoted to a theorem without an exact derivation.
- The crown remains open unless a complete positivity/nonvanishing proof is obtained.
