# Programme protocol

## Frozen notation

For the registered increasing primorial centres,

\[
Z_j=\#\{m:\ell_j<m\le H,\ m\in\mathbb P,\ P_j+m\in\mathbb P\},
\qquad N\asymp X/\log X,
\]

and

\[
\gamma_{\min}=\min_{j<N}\gamma_j,
\qquad
\tau_X=2\log N/\gamma_{\min},
\qquad
q_X=1-e^{-\tau_X}.
\]

The target is

\[
\mathrm{INT\!-\!AOD}:\qquad
\sum_{j<N}(1-q_X)^{Z_j}<1.
\]

## Gate O0 — source freeze

Verify the exact parent head, issue #54, the registered centre block, the definition of `Z_j`, the compressed margin, and the implication `INT-AOD => eventual Fortune`. No alternative Fortune branch may enter without a proved implication to this target.

## Gate O1 — detector admissibility and no-tautology rule

Introduce the weighted detector

\[
\mathcal O_X(a)=
\sum_{j<N}
\exp\!\left(-\sum_m a_m I_{jm}\right),
\qquad
I_{jm}=1_{\mathbb P}(m)1_{\mathbb P}(P_j+m),
\]

with `a_m>=0`. A zero row contributes one for every choice of weights.

Weights are admissible only when they are frozen before the output-prime incidences are inspected. They may depend on `X`, `H`, the candidate offset `m`, and explicitly registered residue or singular-series features, but not on whether `P_j+m` is prime. A budget such as

\[
\sum_m a_m\le \tau_X M_X
\]

must be enforced, where `M_X` is the candidate-offset count. This prevents the circular choice of placing all weight on already-known successful columns.

**Pass condition:** a formal generic weighted-detector implication and a machine-checkable admissibility contract.

## Gate O2 — exact random-cover dual

Give two exact interpretations:

1. Bernoulli cover: select each candidate offset independently with probability `q_X`; the expected number of uncovered rows is `INT-AOD`.
2. Hypergeometric cover: select exactly `K` offsets from a candidate universe of size `M`; a row with `Z` successes is missed with probability

\[
\frac{\binom{M-Z}{K}}{\binom{M}{K}}.
\]

Derive the exact comparison with `(1-q)^Z` when `K/M` is fixed.

**Kill condition:** no argument may call the existence of a hitting set a proof of Fortune unless the expected uncovered-row bound is established independently.

## Gate O3 — degree and coefficient-cost audit

Quantify the cost of replacing the exponential detector by a finite polynomial or Bonferroni truncation.

The uniform Bernoulli detector has `q_X=Theta(1)`. Its exact without-replacement analogue therefore has

\[
K=\Theta(M_X)=\Theta(X^2/\log X),
\]

far above the information-theoretic lower bound `Omega(log N)` from the previous programme.

For every proposed polynomial majorant `P_R(z)` of the zero indicator, ledger:

- degree `R`;
- coefficient `l1` norm in the factorial basis;
- range of `z` on which positivity is guaranteed;
- tail growth for `z>R`;
- corresponding prime-correlation arity.

**Stop condition:** close any truncation whose coefficient norm or uncontrolled tail exceeds the complete one-row margin before arithmetic estimates are inserted.

## Gate O4 — connected-cumulant compression

Let `J` be uniform over rows and

\[
G_X(s)=\mathbb E[s^{Z_J}].
\]

The target is `N G_X(e^{-tau_X})<1`.

Attempt to replace raw factorial moments by connected factorial cumulants. A sufficient target is a directly justified identity or inequality of the form

\[
-\log G_X(1-q_X)
\ge q_X\kappa_1-
\sum_{k\ge2}\frac{q_X^k}{k!}|\kappa_k|
>(1+\varepsilon)\log N,
\]

where `kappa_1=E[Z_J]` and the higher `kappa_k` are connected cumulants.

The programme must verify convergence or a zero-free/cluster criterion at `s=1-q_X`; a merely formal Taylor series is not admissible.

Define the candidate smaller theorem:

> **INT-CCB — connected-cumulant bound.** A convergent connected expansion exists at `q_X`, and the first cumulant minus the absolute connected remainder exceeds `(1+epsilon) log N`.

**Pass condition:** prove `INT-CCB => INT-AOD` and identify each arithmetic connected coefficient exactly.

## Gate O5 — arithmetic connected-correlation expansion

Expand the connected coefficients into prime-offset configurations at a common primorial centre. Disconnected singular-series contributions must cancel algebraically before any absolute values are taken.

Audit:

- local factors from primes dividing `P_j`;
- collision graphs among offsets;
- connected versus disconnected set partitions;
- uniformity in `j` and in cluster size;
- coefficient growth as cluster size increases.

The desired bound is not a list of Hardy–Littlewood asymptotics for every tuple. It is a summable bound on the aggregate connected remainder.

**Kill condition:** if the dependency/cluster norm is at least the first-order mass at every admissible truncation, close this lane at the explicit scale.

## Gate O6 — conditional Poisson and singular-series benchmark

Construct a fully conditional benchmark under a stated row-uniform Hardy–Littlewood hypothesis for growing tuples. Determine the weakest uniformity in tuple size, shift range, and error term that would imply `INT-AOD` or `INT-CCB`.

Use modern growing-set singular-series results only for the part they actually supply: averages of local constants. They do not supply prime-tuple counts at the selected primorial centres.

**Output:** a theorem of the form `RUHL(parameters) => INT-AOD`, with every parameter and error budget explicit. It remains conditional unless `RUHL` is independently proved.

## Gate O7 — rowwise parity-breaking dual

Independently derive a parity-breaking asymptotic-sieve or Type I/II formulation for

\[
S_j=\sum_{m\le H}\Lambda(m)\Lambda(P_j+m).
\]

The decomposition must preserve one-row resolution. Record the exact divisor ranges, large-divisor switching, coefficient norms, and the point where the post-level factor range `r>sqrt(H)` enters.

Define the smallest sufficient bilinear theorem rather than citing an asymptotic sieve abstractly.

**Permitted outcome:** `REDUCED_TO_ROWWISE_PARITY_BREAKING_BILINEAR` only if the implication to `INT-AOD` is complete and no hidden distribution assumption remains.

## Gate O8 — falsification and finite-panel diagnostics

Build adversarial incidence matrices that match all statistics used by a proposed proof while retaining one zero row. Reject any inequality that also holds for these surrogates.

On exact small primorial panels, record only diagnostics:

- occupancy histogram;
- column degrees and overlaps;
- uniform and admissible weighted detector values;
- factorial cumulants and connected-cluster norms;
- parity-breaking bilinear surrogates.

Finite panels may select methods but cannot establish asymptotics.

## Gate O9 — closeout

Run static, exact-regression, formal, and inherited clean-room validation. Inspect all provider jobs before cancellation and leave unrelated jobs untouched.

Allowed terminal outcomes are exactly those in `PREREGISTERED_GATES.json`. If no theorem is proved, freeze one successor theorem and close every tested method at an explicit reason or scale.