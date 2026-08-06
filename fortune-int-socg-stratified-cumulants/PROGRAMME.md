# Programme — FORTUNE_INT_SOCG_STRATIFIED_CUMULANTS_V0_1

## Objective

Resolve issue #56 by proving `INT-SOCG`, reducing it to one strictly smaller theorem with a verified implication, matching it to an established theorem with every range checked, or closing the signed-cumulant route at an explicit quantitative obstruction.

The programme may not retreat to density-one, relative-error, fixed-order, fitted-parameter, or ordinary-moving-centre statements.

## Frozen setting

- terminal primes `ell_j in [X,2X)`;
- primorial centres `P_j=ell_j#`;
- `H=eta X^2` with frozen `eta>0`;
- candidate offsets `ell_j<m<=H`, with `m` prime;
- deterministic contiguous terminal-prime strata of width
  \[
  W_X=X/(\log X)^{1+\sigma}
  \]
  for one preregistered `sigma>0`;
- `B=polylog(X)` strata and `n_b` rows per stratum;
- ordinary, not factorial, cumulants.

## Gate sequence

### C0 — source freeze and inherited implication

Pin issue #56, PR #55, the corrected ordinary-cumulant identity, and the kernel-checked row-dependent detector. Re-run the parent static sentinel before opening analytic work.

**Pass:** every inherited hash and theorem statement is recorded.  
**Kill:** any attempt to reuse the rejected factorial-cumulant/distinct-column identity.

### C1 — deterministic stratum geometry

Fix `sigma`, endpoint conventions, common candidate-offset universe, minimum admissible `n_b`, and deterministic lower scales `L_b`. Prove the exact comparison from stratum detectors to the frozen uniform detector.

**Pass:** no parameter depends on observed prime outputs or occupancies.  
**Output:** `INT-SOCG-GEOM`.

### C2 — first-cumulant lower bound

Isolate

\[
c_{1,b}=\frac1{n_b}\sum_{j\in B_b}Z_j.
\]

Separate actual primes, von Mangoldt weights, and proper prime powers. Derive the smallest row-uniform selected-centre mean theorem sufficient for `c_{1,b}\ge cX`.

**Pass:** an unconditional lower bound, an exact reduction to one named selected-centre mean theorem, or a proof that the mean is itself the primary obstruction.  
**Kill:** substituting the Hardy--Littlewood main term without an error below the stratum budget.

### C3 — equality-pattern and diagonal elimination

Group the full ordered column sum

\[
c_{k,b}=\sum_{m_1,\ldots,m_k}\operatorname{Cum}_b(I_{m_1},\ldots,I_{m_k})
\]

by equality partitions of `[k]`. Use indicator idempotence to derive exact coefficients for `r` distinct offsets and isolate all repeated-column diagonals.

**Pass:** exact partition-lattice identity, rational regression, and a diagonal contribution compatible with a dependence scale `D_b=o(X/log X)`.  
**Kill:** any diagonal term already forcing `D_b\gg X/log X`.

### C4 — connected local-factor renormalization

For each distinct-offset connected kernel, remove the universal primorial small-prime enhancement once, not once per block of a partition. Separate collision primes dividing offset differences from the Euler-product tail.

Define a renormalized connected singular-series kernel and test whether it admits a tree or spanning-forest majorant before selected-centre errors are inserted.

**Pass:** `INT-LCSK`, a local connected-kernel bound with explicit dependence radius.  
**Kill:** absolute local interaction alone exceeds the registered `D_b` scale.

### C5 — primorial-walk orbit identity

For moduli composed of primes above the current terminal prime, use

\[
P_{j+1}=\ell_{j+1}P_j
\]

to derive the exact residue-orbit recurrence. Fourier-expand the selected-centre incidence errors and identify the required cancellation along the multiplicative primorial walk.

**Pass:** reduction to `INT-PWOC`, one explicit primorial-walk orthogonality theorem with conductor, length, frequency and error ranges stated.  
**Kill:** the trivial or large-sieve norm cannot reach the absolute one-stratum budget.

### C6 — signed ordinary-cumulant assembly

Combine C3--C5 only after disconnected main terms cancel. Test signed tree-graph, partition-Möbius, and cumulant-recursion assemblies. No absolute value may be taken before the registered recombination point.

**Pass:** prove `INT-SOCG` or reduce it to one explicit signed connected-correlation estimate.  
**Kill:** the assembled dependence radius is `\gg X/log X`.

### C7 — arithmetic source decomposition

Test Heath--Brown/Vaughan/divisor decompositions only against the C6 target. Every source identity must retain the common row variable and actual-prime conclusion after recombination.

**Pass:** a source-to-connected-frame identity plus a Type I/II or zero-source estimate that reaches `D_b`.  
**Kill:** parity loss, post-level sparse-hyperbola loss, or an error that only controls almost primes or almost all rows.

### C8 — conditional bridge and falsification

State the exact row-uniform Hardy--Littlewood moment hypothesis through logarithmic order that implies C6. Run low-order exact panels, equality-pattern regressions, residue-orbit diagnostics and adversarial incidence models only to select or falsify methods.

**Pass:** diagnostics agree with all exact identities and no finite result is promoted.  
**Kill:** any proposed statistic is matched by a registered adversarial zero-row model.

### C9 — closeout

Run the programme sentinel, all exact regressions, inherited integer verifiers, targeted Lean if a new formal module exists, and a full clean-room package build. Cancel or complete every programme compute job.

## Allowed terminal statuses

- `PROVED_INT_SOCG`;
- `REDUCED_TO_SELECTED_PRIMORIAL_WALK_CORRELATION`;
- `REDUCED_TO_LOCAL_CONNECTED_SINGULAR_SERIES`;
- `MEAN_LOWER_BOUND_IS_PRIMARY_OBSTRUCTION`;
- `REDUCED_TO_ESTABLISHED_THEOREM`;
- `METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE`.

## Non-negotiable exclusions

No function-field tangent, fixed-order moment campaign, whole-block cumulant expansion, post-hoc temperature, generic dependency-graph invocation, dense-centre transfer, or finite-panel asymptotic claim is admissible.