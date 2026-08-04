# INT-ISC focused research programme v0.1

## Governing rule

Every round must either improve the exact exponent/dependency ledger, prove a frozen implication, or close a method by a reproducible obstruction. New notation, equivalent quotients, extra moments and finite panels are not progress by themselves.

## Gate I0 — source and target freeze

Deliverables:

- pin the corrected Papers II–III and integrated closeout sources;
- reproduce the exact centred identity in Lean;
- verify all scales in `EXPONENT_LEDGER.json`;
- state the target with every quantifier, smoothing convention, endpoint and uniformity condition.

Pass condition: no ambiguity remains in `Z_j`, `C_j`, the baseline, the residual or the required loss.

## Gate I1 — weakest-sufficient-target audit

The current `INT-ISC` statement may be stronger than Fortune. Before analytic proof search:

1. derive every necessary consequence of the variance target, including the sparse first-moment consequence
   \[
   \left|\sum_{j<N}(Z_j-\lambda_j)\right|
   \le \sqrt{N}\left(\sum_{j<N}|Z_j-\lambda_j|^2\right)^{1/2}
   \ll N\sqrt{XL(X)};
   \]
2. compare the Hardy–Littlewood baseline `lambda_j^*` with all admissible deterministic baselines satisfying `cX <= lambda_j <= CX`;
3. test whether a one-sided, truncated, smoothed, averaged-in-H or positive-semidefinite statement is strictly weaker while still excluding every failure;
4. formalize any replacement implication before changing the primary target.

Pass condition: either `INT-ISC` remains the weakest visible sufficient theorem, or a strictly smaller theorem is frozen and substituted with an exact proof of sufficiency.

Kill condition: a proposed replacement is rejected if it only renames the same covariance, loses the actual increasing centres, assumes a conjectural mean as a theorem, or proves only density-one success.

## Gate I2 — necessary sparse first moment

This is the first analytic boulder. Determine whether current methods can prove the necessary selected-centre asymptotic at the scale forced by I1.

Required work:

- expand the sum over `j,m` and expose all local congruence restrictions;
- derive the exact singular-series average over increasing primorial centres;
- compare direct sieve, dispersion, circle-method and transference formulations;
- audit whether any cited theorem is uniform in the centre size, interval length, sparse centre set and growing local modulus;
- record the best unconditional error in the exponent ledger.

Pass condition: a proved sparse first-moment theorem at the required or stronger scale.

Stop condition: if no method reaches the scale, isolate the smallest missing theorem and prove why dense-centre results cannot supply it.

No four-prime compute campaign begins before this gate has a decisive result, unless a direct signed method rigorously bypasses a separate first-moment estimate.

## Gate I3 — direct four-prime covariance lane

Starting from

\[
Z_j^2=Z_j+2\sum_{1\le d<H}C_j(H;d),
\]

construct an aggregate, fully centred four-linear-form expansion.

Required work:

- classify diagonal, near-diagonal and genuinely four-distinct configurations;
- compute the local singular series without decoupling the four primality conditions;
- identify which displacement ranges are automatically negligible;
- retain the signed baseline subtraction until the final estimate;
- measure every use of Cauchy–Schwarz against the `o(log X)` loss budget.

Promotion condition: an explicit theorem whose proof reduces `INT-ISC` to named bilinear, trilinear or dispersion estimates with verified ranges.

Kill condition: raw absolute-value bounds, termwise Hardy–Littlewood conjectures, or uniform estimates in every `d` that are stronger than the aggregate target without a credible route.

## Gate I4 — double-von-Mangoldt dispersion lane

Use the exact source

\[
T_j(H)=\sum_{m\le H}\Lambda(m)\Lambda(P_j+m)
\]

and its Fourier representation while preserving both von Mangoldt factors and the centring.

Required work:

- perform a Heath–Brown/Vaughan-type decomposition with a complete type ledger;
- identify the principal term before any norm inequality;
- derive the sparse-centre kernel exactly;
- test large-sieve, dispersion, Kloosterman-fraction and bilinear technology at the actual moduli and lengths;
- account for prime powers and conversion back to the existence detector.

Promotion condition: a source-to-variance theorem with total loss `o(log X)`.

Kill condition: any decomposition whose best possible norm bound already exceeds the loss budget, or which reconstructs the old unweighted reciprocal frame without a proved bridge.

## Gate I5 — deterministic source/orbit and PSD lane

Search for an exact identity or dual formulation that makes the centred residual positive-semidefinite or isolates a signed operator norm.

Required work:

- derive the Gram/operator associated with the increasing primorial path;
- separate forced diagonal eigenmodes from the genuinely arithmetic residual;
- test whether source averaging supplies orthogonality or merely reparametrizes the same kernel;
- prove lower bounds showing when a frame/operator route cannot reach the target.

Pass condition: a strictly smaller operator theorem implying `INT-ISC` with a verified exponent ledger.

Kill condition: a frame with norm lower bound at or above the forbidden scale, or a representation that loses baseline centring.

## Gate I6 — falsification and adversarial models

Construct finite and asymptotic surrogate models preserving progressively more of:

- local prime densities;
- primorial divisibility;
- superincreasing centre geometry;
- one- and two-point singular series;
- the exact baseline and failure gap.

The purpose is to determine which structural inputs are insufficient. Countermodels must be explicit, reproducible and must not be mistaken for counterexamples to the prime theorem itself.

Pass condition: either the surviving method distinguishes the genuine primes from every registered surrogate, or a no-go theorem identifies the missing arithmetic input.

## Gate I7 — theorem or obstruction closeout

A closeout requires:

- a theorem statement and complete dependency graph;
- an exponent table showing the final loss;
- independent reconstruction of all computational certificates;
- a clean formal/static build;
- a provider sweep with no active programme jobs;
- an exact statement of consequences for Fortune.

Allowed final statuses:

- `PROVED_INT_ISC`;
- `REDUCED_TO_ESTABLISHED_THEOREM`;
- `REDUCED_TO_SMALLER_NEW_THEOREM`;
- `METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE`.

No “one lemma remains” or probability-of-success language is permitted without a frozen theorem and dependency graph.

## Compute discipline

- Every remote job must include programme ID, gate and lane in its command or metadata.
- Run a sentinel before a full job.
- Initial sentinels are capped at 10 minutes; ordinary proof/verification jobs at 45 minutes; no job may exceed two hours without a committed justification.
- Invalidated, superseded or stalled jobs are cancelled immediately.
- Every round ends with a provider sweep. Unrelated jobs are inspected and left untouched.
- Finite experiments may calibrate identities or falsify methods; they may not promote asymptotic claims.