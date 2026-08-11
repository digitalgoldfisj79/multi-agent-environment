# Fortune Zeta23 transfer programme v0.1

Date: 2026-08-11

## Scope

This is a bounded exception to the frozen integer Fortune programme, motivated by the finite-compression/rank-trace methodology and trusted/untrusted formal-verification architecture of `anthropics/zeta-23-lean`.

Two lanes only are authorised.

### Lane F — formal trust architecture

Goal: replace the current Paper VII presentation in which the unconditional theorem is obtained from the project axiom `p7_k2_certified_normalization` by an independently stated Mathlib-only challenge and an explicit conditional bridge.

Gates:

1. `F0`: define the degree-two bilateral challenge from Mathlib primitives only; it must not import `FortuneFormal`.
2. `F1`: build an explicit datum translation into `FortuneFormal.Bilateral.Datum` and prove that an assumed `K2CertifiedNormalizationStatement` solves the independent challenge.
3. `F2`: run `#print axioms` on the conditional bridge. No project axiom may appear because the normalization statement is a theorem parameter, not a global axiom.
4. `F3`: scan the challenge/comparator layer for `axiom`, `sorry`, `admit`, and `unsafe`.
5. `F4`: attempt to shrink the remaining unconditional gap. Deleting or renaming the existing axiom without proving the datum-normalization theorem is forbidden.

Success levels:

- `COMPARATOR_ARCHITECTURE_PASS`: F0–F3 pass.
- `AXIOM_REDUCED`: a strictly smaller explicit normalization subtheorem remains.
- `AXIOM_CLOSED`: `p7_k2_certified_normalization` is deleted and the unconditional independent challenge is kernel proved.

### Lane S — finite compression / stable-rank transfer

For each selected-centre block or deterministic terminal-prime stratum, let `Z_j >= 0` be the exact prime-pair occupancy count.

The diagonal compression `D = diag(Z_j)` has

- `rank D = # {j : Z_j != 0}`;
- `tr D = sum_j Z_j`;
- `||D||_F^2 = sum_j Z_j^2`.

Cauchy/stable rank gives the exact sufficient criterion

`(sum Z_j)^2 > (R-1) * sum Z_j^2  =>  every row succeeds`.

Equivalently, with empirical mean `mu` and centered sum of squares `V`,

`V < R * mu^2 / (R-1)`.

The programme must determine whether this changes the arithmetic frontier rather than merely renaming the existing Paper II/III variance criterion.

Gates:

1. `S0`: verify the exact finite implication, including adversarial one-zero equality controls.
2. `S1`: compare the whole-block criterion symbolically with Paper II Theorem 2.4 / Paper III Theorem 9.1.
3. `S2`: evaluate exact primorial panels globally and under the already-preregistered terminal-prime stratification of width `X/(log X)^1.25`.
4. `S3`: derive the asymptotic error allowance for a stratum of size `n_b`. If a variance theorem has scale `n_b X L(X)` and means are `~ X`, one failure is excluded when `L(X)=o(X/n_b)`.
5. `S4`: map the second moment exactly. If it requires the same aggregated four-prime correlation as Paper III, record that; do not advertise it as a lower-order miracle.
6. `S5`: only reopen an analytic Fortune lane if the stratified target is demonstrably weaker than the frozen signed logarithmic-order tuple target and not already ruled out by an existing programme.

Kill rules:

- If finite compression is exactly the old all-centres variance criterion with no quantitative gain, close it.
- If stratification improves the deterministic loss budget but the available arithmetic estimate worsens by at least the same factor, close it.
- If `tr(D^2)` or a non-diagonal Gram variant simply recreates an unavailable four-prime/Hardy–Littlewood input at no lower strength, close it.
- No result from this lane may be called progress toward Fortune unless it proves a strictly weaker sufficient arithmetic theorem than the frozen frontier.

## Governance

The existing integer Fortune frontier remains closed unless Gate S5 passes. The novelty/assurance programme remains authoritative for publication claims. This programme may add a new candidate theorem or a new obstruction; it may not silently rewrite prior ledgers.