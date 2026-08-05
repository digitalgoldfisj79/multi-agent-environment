# Programme — FORTUNE_INT_SCME_SELECTED_CENTRE_MEAN_V0_1

## Objective

Resolve issue #58 by proving `INT-SCME`, reducing it to one strictly smaller parity-breaking theorem with a checked implication, matching it to an established theorem with every range verified, or closing the selected-centre mean route at an explicit quantitative obstruction.

The programme works only on the integer Fortune mainline. Higher cumulants, function fields, fixed-order moments, fitted parameters, density-one results and generic moving-centre transfer are excluded.

## Frozen setting

- terminal primes `ell_j in [X,2X)`;
- primorial centres `P_j=ell_j#`;
- `H=eta X^2` with `eta=1/2`;
- parent strata inherited from issue #58;
- common candidate-prime universe `M_b={m: U_b<m<=H, m prime}`;
- weighted selected-centre mean
  \[
  T_b=\frac1{n_b}\sum_{j\in B_b}\sum_{m\in M_b}\log m\,\Lambda(P_j+m).
  \]

The target is `T_b >= kappa X^2 log X` for every sufficiently large parent stratum.

## Gate sequence

### M0 — source freeze
Pin issue #58, PR #57, the inherited `INT-SCME => c_1 >= cX` reduction and all exact primorial-walk collision results.

### M1 — normalization and output prime powers
Reprove the exact weighted normalization, the output-prime-power subtraction and the implication from a positive weighted mean to the first cumulant.

### M2 — local density and direct sieve audit
Define the output sequence indexed by `n=P_j+m`. Derive its exact divisor sums, local density and predicted Euler factor. Test direct Friedlander–Iwaniec eligibility at the actual output scale `n asymp P_j`.

### M3 — deterministic microblocks
Split each parent stratum into consecutive microblocks of `R=X^rho+O(1)` rows without using output primality. Prove that a uniform lower bound on every microblock implies the parent-stratum lower bound.

### M4 — selected-residue Barban–Davenport–Halberstam band
For prime moduli `2X<q<=Q=X^(1+delta)`, evaluate
\[
D_C(Q)=\frac1R\sum_{j\in C}\sum_{m\in M_b}\log m
\sum_{\substack{2X<q<=Q\\q\mid P_j+m}}\log q.
\]
Combine the classical BDH mean square with the exact primorial collision count. Optimize `rho,delta` and record the precise exponent frontier.

### M5 — first post-terminal band theorem
Prove the unconditional asymptotic for every deterministic microblock when
\[
2\delta<\rho<1-\delta.
\]
The optimized choice is `rho=2/3`, any fixed `delta<1/3`, giving access to `Q<X^(4/3)` and a positive divisor-band mass of order `delta H log X`.

### M6 — parity-tail reduction
Use the exact identity
\[
\Lambda(n)=D_Q(n)+R_Q(n),\qquad
D_Q(n)=\sum_{\substack{2X<q<=Q\\q\mid n}}\log q,
\]
to reduce `INT-SCME` to one signed remainder theorem after the proved divisor-band main term. Define the successor `INT-SCPT` (selected-centre parity tail).

### M7 — source and switching audit
Test Vaughan, Heath–Brown, Möbius-log, asymptotic-sieve and switching formulations against `INT-SCPT`. Record the first factor range where each loses row averaging or parity.

### M8 — exact diagnostics and adversarial controls
Verify collision combinatorics, exponent inequalities, local products and small factor profiles. Finite panels are diagnostic only.

### M9 — closeout
Run the new sentinel, inherited integer verifiers, full Lean package and formal trust audit. Cancel or complete every programme compute job. Transfer the sole frontier only after the final frozen re-clone passes.

## Allowed terminal statuses

- `PROVED_INT_SCME`;
- `REDUCED_TO_SELECTED_CENTRE_PARITY_TAIL`;
- `REDUCED_TO_ESTABLISHED_THEOREM`;
- `METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE`.

## Non-negotiable exclusions

No claim may treat the BDH divisor-band mass as prime mass. The signed tail contains both the positive prime contribution and the cancelling composite contribution. No finite factorization panel, average-over-most-strata statement, or unverified asymptotic-sieve localization may be promoted.