# Programme — FORTUNE_INT_SCME_SELECTED_CENTRE_MEAN_V0_1

## Objective

Resolve issue #58 by proving `INT-SCME`, reducing it to one strictly smaller theorem with a checked implication, matching it to an established theorem with every range verified, or closing the selected-centre mean route at an explicit quantitative obstruction.

The programme works only on the integer Fortune mainline. Higher cumulants, function fields, fixed-order moments, fitted parameters, density-one results and generic moving-centre transfer are excluded.

## Frozen setting

- terminal primes `ell_j in [X,2X)`;
- primorial centres `P_j=ell_j#`;
- `H=X^2/2`;
- parent strata inherited from issue #58;
- common candidate-prime universe `M_b={m:U_b<m<=H, m prime}`;
- weighted selected-centre mean
  \[
  T_b=\frac1{n_b}\sum_{j\in B_b}\sum_{m\in M_b}\log m\,\Lambda(P_j+m).
  \]

The target is `T_b >= kappa X^2 log X` for every sufficiently large parent stratum.

## Gate sequence

### M0 — source freeze
Pin issue #58, PR #57, the inherited `INT-SCME => c_1 >= cX` reduction and all exact primorial-walk collision results.

### M1 — normalization and output prime powers
Reprove the exact weighted normalization, output-prime-power subtraction and implication from a positive weighted mean to the first cumulant.

### M2 — local density and direct sieve audit
Define the output sequence indexed by `n=P_j+m`. Derive its exact divisor sums and test direct Friedlander–Iwaniec eligibility at the actual output scale `n asymp P_j`.

### M3 — deterministic microblocks
Split each parent stratum into consecutive microblocks of `R=X^rho+O(1)` rows without using output primality. Prove that microblock lower bounds aggregate to the parent stratum.

### M4 — selected-residue variance audit
For prime moduli `2X<q<=Q=X^(1+delta)`, derive the selected-residue Cauchy bound using the exact primorial collision energy. Separate:

- the hypothetical variance input `INT-SCVAR: V(H,Q)<<HQ(log H)^C`;
- the unconditional large-sieve variance `V(H,Q)<<(H+Q^2)H(log H)^C`.

Record the exact exponent region under `INT-SCVAR` and the unconditional impossibility inequality.

### M5 — first post-terminal band
Under `INT-SCVAR`, derive the divisor-band asymptotic for `2 delta<rho<1-delta`; optimize at `rho=2/3`, `delta<1/3`. Verify that standard unconditional variance input cannot enter any post-terminal polynomial band.

### M6 — parity-tail anatomy
Use
\[
\Lambda(n)=D_Q(n)+R_Q(n)
\]
to isolate `INT-SCPT`, the signed prime-versus-composite tail. Record the conditional bridge

\[
INT\text{-}SCVAR+INT\text{-}SCPT\Longrightarrow INT\text{-}SCME.
\]

Do not claim a one-theorem unconditional reduction unless M4 is independently proved.

### M7 — source and switching audit
Test Vaughan, Heath–Brown, Möbius-log, asymptotic-sieve and switching formulations against both missing inputs. Record the first factor range where each loses row averaging or parity.

### M8 — exact diagnostics and adversarial controls
Verify collision combinatorics, exponent inequalities, local products, large-sieve obstruction and small factor profiles. Finite panels are diagnostic only.

### M9 — closeout
Run the new sentinel, inherited integer verifiers, full Lean package and formal trust audit. Cancel or complete every programme compute job. Transfer the frontier only if a registered stop condition is met.

## Allowed terminal statuses

- `PROVED_INT_SCME`;
- `REDUCED_TO_ESTABLISHED_THEOREM`;
- `REDUCED_TO_INT_SCVAR_PLUS_INT_SCPT_CONDITIONALLY`;
- `METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE`.

## Non-negotiable exclusions

No claim may treat divisor-band mass as prime mass. No classical BDH estimate may be invoked outside its verified modulus range. No finite factorization panel, average-over-most-strata statement, or unverified asymptotic-sieve localization may be promoted.