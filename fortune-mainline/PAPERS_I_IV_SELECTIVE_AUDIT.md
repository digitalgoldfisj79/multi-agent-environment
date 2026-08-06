# Papers I and IV: selective mainline audit

**Date:** 4 August 2026  
**Purpose:** determine whether either paper remains load-bearing after the corrected prime-pair detector

## Executive result

Paper I contains substantial exact collision geometry, but its unresolved energy estimates still require a separate signed prime-detection bridge. Paper IV proves a random-order reciprocal-frame theorem whose cancellation comes from permutation averaging; it gives no control of the unique increasing primorial order.

Neither paper supplies or materially shortens `INT-ISC`. Both should be preserved as independent structural papers, not expanded on the Fortune mainline at present.

## Paper I

### Source

`paper1_collision_geometry/manuscript.md`, publication blob `1734d956dc10ce2c48ddd7c11b1df625ebdba0be`.

The independently recovered source has 1,910 lines, 6,487 words and SHA-256

`0e0f8a0d89209b8f4dd8c589526a89d57bd536f4889fdcd9c902a09b1a62f157`.

### Retained exact core

The following results remain mathematically useful and internally independent of the detector correction:

- Proposition 2.1: exact fourth-moment/collision identity;
- Lemma 3.1 and Theorems 3.2–3.3: transport and offset-slice incidence identities/bounds;
- Theorem 3.4 and Corollary 3.5: average almost-injectivity;
- Proposition 3.6 and Corollary 3.7: nearby collision-interval geometry;
- Theorem 4.1: endpoint-graph affine rank and Smith form;
- Proposition 5.1: exact pair-overlap decomposition;
- Theorem 5.2 and Corollary 5.3: overlap transport bounds and three-shared-endpoint closure;
- Proposition 5.4 and Theorem 5.5: median bilinear decomposition and exact independent-prefix covariance;
- Proposition 5.6: non-Gaussian fourth-moment law;
- Theorem 6.1 and Theorem 7.1: support-family and sparse-composition closures;
- Proposition 8.1 and Lemma 8.2: square-function comparison and local correction;
- Theorem 9.1: additive-frequency fourth moment;
- Propositions 10.1–10.3: common-translation shortening and exact multiplier obstruction.

### Open or conditional content

- HTE4 centred rank-two dispersion;
- HWF4 hereditary weighted moment;
- FBHE4 four-distinct-block energy;
- RQHE4 root-quartet estimate;
- conditional edge closure dependent on HWF4;
- any signed sieve/von-Mangoldt bridge to prime detection.

### Mainline relevance ruling

Even proving all four internal energy conjectures would not prove `INT-ISC`, because their variables and centring arise from the old collision architecture. A new theorem would still be required to map the corrected prime-pair covariance to those energies while preserving signs and baselines.

The exact graph/Smith and collision identities may be reused if a future derivation naturally produces them. Formalizing the entire paper before such a bridge exists would not reduce the active arithmetic frontier.

**Decision:** freeze Paper I. Selective reuse only.

## Paper IV

### Source

`paper4_random_order/manuscript.md` at commit `af9350f06e41e94d79f583b2e8fca45b55b92852`, blob `1a3d39d974bfa37d31c100f536dcaa1b74f6d688`, SHA-256

`548460849cc9c6125fbe59d0a4f2f37ec680761174c25556b5e781a8ae9372f1`.

### Retained exact/proved core

- Theorem 2.1: random-order reciprocal-frame theorem;
- Proposition 2.2: per-modulus-pair bias sum;
- Lemmas 3.1–3.4: path rigidity, unit multipliers, complete coefficient patterns and multiplicities;
- Lemmas 4.1–4.2: ordered-partition identity and contour decay;
- Lemmas 5.1–5.2: Gauss coefficients and exceptional-character sixth moment;
- Lemmas 6.1–6.3 and Proposition 6.4: ratio coordinates, matching and all-bad domination;
- complete configuration and exponent ledgers.

### Exact scope limitation

The expectation over permutations is the source of the cancellation. The identity ordering has no order entropy. The proof does not show that the increasing prime order is typical, nonexceptional or controlled by the random-order second moment.

The paper itself states that it proves neither Fortune nor the reciprocal-frame target for increasing primorials.

### Mainline relevance ruling

A second moment over orderings would still not identify the increasing order without a deterministic arithmetic theorem. More importantly, after the detector correction, even a derandomised reciprocal-frame theorem would still need a source-to-frame bridge to `INT-ISC`.

Thus Paper IV is separated from the mainline by two missing arrows:

\[
\text{random order}
\not\Rightarrow
\text{increasing order}
\not\Rightarrow
\text{corrected detector covariance}.
\]

**Decision:** freeze Paper IV. Do not pursue random-order moments or derandomisation until a corrected source bridge makes the frame load-bearing.

## Combined final ruling

Papers I and IV are not retracted. Their exact theorems remain valid within their declared models. They are, however, secondary to the present mainline.

No further theorem-discovery work on HTE4, HWF4, random-order concentration or reciprocal derandomisation is justified until it is preceded by a proved map from the corrected prime-pair source.
