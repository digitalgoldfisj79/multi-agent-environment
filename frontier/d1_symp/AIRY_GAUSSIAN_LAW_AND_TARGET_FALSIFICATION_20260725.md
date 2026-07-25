# The Airy Gaussian law: the terminal analytic target is empirically untenable, and the branch is optimising the wrong boulder

**Date:** 2026-07-25 (revised after independent audit, same day)
**Branch:** `claude/airy-next-after-circularity-8jlrek` (continues `gpt56/d1-main-twisted-descent-20260724` at `c331f740`)
**Scope:** the terminal analytic wall for function-field `d=1`, primes `p = 5 mod 6`.
**Status:** `C = 4` is **rigorously dead**; every absolute constant below `4.8469` is excluded by exhibited primes. Unboundedness is a **strong numerical conjecture, not a theorem**. The specific difference-cancellation mechanism behind the virtual-Adams routes is **measured to be absent**. The pivotal open quantity is relocated to the application side.

### Revision note

An independent audit (`AIRY_GAUSSIAN_INDEPENDENT_AUDIT_20260725.md`, branch
`gpt56/airy-gaussian-independent-audit-20260725`) reproduced every number in this
file and correctly rejected three claims in its first version. All three are
corrected here:

1. the ruling "the target is false" is replaced by the finite, rigorous
   statement that no `C < 4.8469` is admissible (section 3);
2. Lemma 5.1 held for `p > 3`, not for every odd prime; `p = 3` is genuinely
   degenerate and is now recorded as such (section 5);
3. the recommendation to extract `(M_p, S_p)` by scalar fitting was
   **underdetermined and is withdrawn** (section 8).

The audit's narrowing of the section 4 conclusion is also adopted.

This file does not re-prove anything in `MAIN_BRANCH_STATUS_AFTER_CLAUSEN_CIRCULARITY_20260725.md`. It accepts that status as correct and asks the prior question the branch never asked: *is the statement at the end of the funnel true?*

## 1. Summary

Let

\[
\rho_p=\frac{T_p}{p^{(p-1)/2}} .
\]

The named half-theorem is `|rho_p| <= C` with `C` absolute.

1. **`rho_p` is statistically indistinguishable from `N(0,2)`.** Over all `4806` primes `p = 5 mod 6` below `10^5`, a Kolmogorov--Smirnov test against `N(0,2)` **passes** at the 5% level. What follows *rigorously* is only the finite exclusion
   \[
   \boxed{\ \text{no absolute constant } C<4.8468292139\ \text{is admissible,}\ }
   \]
   witnessed at `p = 57653`. Unboundedness, and the limsup law
   `|T_p| = (2+o(1)) sqrt(log p) p^((p-1)/2)`, are **conjectures** supported by
   the distributional fit. A finite sample cannot establish either: a
   distribution bounded by, say, `10` would be indistinguishable from `N(0,2)`
   over this range. The practical consequence is unchanged — the target is
   disfavoured enough that further work aimed at a small absolute constant is
   a poor allocation — but the logical status must not be overstated.
2. **The specific difference-cancellation mechanism is absent.** The two symmetric-power sums whose difference is `Psi^p` have measured correlation `-0.04`, each has root-mean-square exactly `sqrt(p)`, and their difference is `sqrt(2)` times **larger** than either. This refutes the hypothesis that the Adams difference supplies cancellation. It does **not** prove statistical independence, constituent-level non-cancellation, or that no use of the Adams decomposition can work.
3. **The absolute constant is not known to be needed.** `GATE0_PRIME_DEPENDENCY_AUDIT_20260724.md` already ruled that absolute `C` is required by the *named half-theorem* but **not** established as necessary for the crown, and that the only missing quantity is the transport pair `(M_p,S_p)`. The proved unconditional bound is already `C(p) <= 2 sqrt p = o(p)`.

Taken together: the branch has spent its effort improving `2 sqrt p -> O(1)`, a target that the evidence strongly disfavours, while the one unevaluated quantity in the entire dependency graph sits untouched on the application side.

## 2. The exact object being measured

For `t in F_p` let `alpha_t, beta_t` be the Frobenius eigenvalues of the cubic Airy sheaf, so that

\[
\alpha_t+\beta_t=a_t=\sum_{x\in\mathbf F_p}\psi(x^3+tx),
\qquad
\alpha_t\beta_t=p,
\qquad
a_t=2\sqrt p\cos\theta_t .
\]

Additive orthogonality and Hasse--Davenport give the exact identity

\[
T_p=-\frac1p\sum_{t\in\mathbf F_p}\left(\alpha_t^p+\beta_t^p\right),
\]

hence

\[
\boxed{
\rho_p=\frac{T_p}{p^{(p-1)/2}}
=-\frac2{\sqrt p}\sum_{t\in\mathbf F_p}\cos\!\left(p\,\theta_t\right).
}
\]

This is a one-line consequence of facts already committed on the branch. Its value is that it makes `rho_p` computable in `O(p log p)` operations in double precision, for *every* prime, rather than only at the nine primes where an exact integer `T_p` has been committed.

### Calibration

The float model reproduces **all nine** committed exact integers, including the 65-digit `T_71`, to a worst relative error of `2.9e-14` (`airy_gaussian_law_verify.py`, check 1). A pipeline error could not reproduce `T_71` to fourteen significant digits.

## 3. The Gaussian law

Katz's theorem gives the Airy sheaf geometric monodromy `SL_2`, so the angles `theta_t` are Sato--Tate distributed. Under `(2/pi) sin^2`,

\[
\mathbf E[\cos(p\theta)]=0,
\qquad
\operatorname{Var}[\cos(p\theta)]=\tfrac12
\qquad(p\ge3),
\]

so if the `p` angles behave independently at frequency `p`,

\[
\operatorname{Var}(\rho_p)=\frac4p\cdot\frac p2=2 .
\]

### Measurement

All `4806` primes `p = 5 mod 6` below `10^5`:

| statistic | observed | `N(0,2)` |
|---|---:|---:|
| mean | `+0.0033` | `0` |
| variance | `2.0969` | `2` |
| skewness | `-0.0460` | `0` |
| kurtosis | `2.9071` | `3` |
| `P(|rho|>1.0 sd)` | `0.3304` | `0.3173` |
| `P(|rho|>1.5 sd)` | `0.1479` | `0.1336` |
| `P(|rho|>2.0 sd)` | `0.0512` | `0.0455` |
| `P(|rho|>2.5 sd)` | `0.0123` | `0.0124` |
| `P(|rho|>3.0 sd)` | `0.0029` | `0.0027` |

**Kolmogorov--Smirnov:** `D = 0.01362` against a 5% critical value of `0.01959`. The Gaussian hypothesis is *not rejected*.

### No arithmetic sub-structure

Splitting by `p mod 4`, `mod 8`, `mod 9`, `mod 12` gives mean `~0` and variance `~2` in **every** class (worst variance `2.18`, worst mean `+0.06`). There is no congruence sub-family on which `rho_p` is bounded.

### The running maximum does not flatten

| range | `#p` | `max|rho_p|` |
|---|---:|---:|
| `(0,1000]` | `86` | `2.8451` |
| `(1000,3000]` | `135` | `3.7707` |
| `(3000,10000]` | `395` | `4.4798` |
| `(10000,30000]` | `1017` | `4.5563` |
| `(30000,60000]` | `1408` | `4.8468` |

Against the Gaussian prediction `2 sqrt(log n)` the ratio holds at `0.76--0.88` across three orders of magnitude and shows no decay. Already `827` primes below `10^5` have `|rho_p| > 2`, `181` have `|rho_p| > 3`, and `27` have `|rho_p| > 4`. The second moment is `2.04, 2.01, 2.08, 2.22` in successive dyadic ranges: flat, not decaying.

A bounded `rho_p` would produce truncated tails and a flattening maximum. Neither occurs.

### Ruling

**Rigorous:**

\[
\boxed{
\text{No absolute constant } C<4.8468292139 \text{ satisfies } |T_p|\le C\,p^{(p-1)/2},
}
\]

witnessed at `p = 57653`. In particular the working conjecture `C = 4` is dead,
by exhibited counterexample at 27 primes below `10^5`.

**Conjectural:** `sup_p|rho_p| = infinity`, with limsup law
`2 sqrt(log p)`. The distributional evidence is strong but a finite sample
cannot separate `N(0,2)` from any sufficiently wide bounded law. This must be
recorded as a conjecture.

The distinction matters for how the result is used. It does **not** license the
statement "the half-theorem is false"; it *does* license the judgement that
further analytic effort aimed at a small absolute constant is a poor
allocation.

### Consequence for the circularity theorem

This offers a *heuristic* explanation of the pattern the branch has been
hitting. If `T_p` already sits at the square-root threshold with a Gaussian
coefficient, there is no residual cancellation for an exact identity to
extract, so such an identity would be expected to collapse to a tautology. The
Hayes circularity `T_p^2 = T_p^2` is rigorously established on its own terms;
the broader claim that *any* exact identity must be tautological is heuristic
and is not proved here.

## 4. The virtual-Adams programme has no available gain

Write `U_m` for the Chebyshev-`U` character of `Sym^m`, and

\[
\sum_t\operatorname{Tr}(\operatorname{Sym}^pA_t)=p^{p/2}M_+,
\qquad
\sum_t\operatorname{Tr}(\det\otimes\operatorname{Sym}^{p-2}A_t)=p^{p/2}M_-,
\]

so that `Psi^p` corresponds to `M_+ - M_- = 2 sum_t cos(p theta_t)`.

Measured over `1136` primes below `2 x 10^4`:

\[
\operatorname{rms}\!\left(\frac{M_+}{\sqrt p}\right)=0.969,
\qquad
\operatorname{rms}\!\left(\frac{M_-}{\sqrt p}\right)=0.983,
\qquad
\operatorname{rms}\!\left(\frac{M_+-M_-}{\sqrt p}\right)=1.410,
\]
\[
\boxed{\operatorname{corr}(M_+,M_-)=-0.043 .}
\]

Three conclusions.

1. **Each symmetric power already exhibits full square-root cancellation.** Sato--Tate orthonormality predicts `rms = 1`; the observed values are `0.97` and `0.98`. Deligne's bound for `sum_t Tr(Sym^p)` is `dim H^1_c * p^{(p+1)/2} ~ (3/4)p^2 * p^{(p+1)/2}`. The truth is `sqrt p * p^{p/2}`. **The entire loss of order `p` (indeed `p^2`) is already present inside one symmetric power.**
2. **The Adams difference is anti-helpful.** `M_+` and `M_-` are uncorrelated, so their difference has variance `1+1=2` and is `sqrt 2` times *larger* than either term. Subtracting `det (x) Sym^{p-2}` from `Sym^p` adds noise; it removes none.
3. Therefore the virtual conductor identity `Swan_infinity(Psi^p A)=0` — correct as stated in `SYMP_LEMMA.md` — is **not** a route to the estimate. A vanishing virtual Swan conductor bounds an Euler characteristic; it does not induce an eigenvalue matching between `H^1_c(Sym^p A)` and `H^1_c(det (x) Sym^{p-2} A)`, and the measurement above shows no such matching exists.

**Scope of this conclusion.** What is measured is the covariance of the two
*total scalar traces*. That refutes the hypothesis of persistent positive
covariance, which is the mechanism the local-inertia, Spin and Clausen
calculations were built to exploit. It does **not** establish statistical
independence, rule out cancellation at the level of individual constituents,
or prove that no use of the Adams decomposition can succeed. The correct
reading is: this specific difference-cancellation mechanism is empirically
absent, so routes resting on it are disfavoured — not that the Adams
programme is closed as a matter of logic.

## 5. A structural lemma: the cubic is as nondegenerate as possible

The remaining hope for a bounded constant would be a hidden degeneracy in the geometry. There is none.

Let `E = F_{p^p}`, `H = ker Tr_{E/F_p}`, and consider the projective cubic

\[
X=\{\operatorname{Tr}(x^3)=0\}\subset\mathbf P(H)\cong\mathbf P^{p-2}.
\]

### Lemma 5.1

For every prime `p > 3`, the singular locus of `X` is the **single** point `[1]`.

### Proof

`d(\operatorname{Tr}x^3)_x(y)=3\operatorname{Tr}(x^2y)`, and `3` is invertible
because `p > 3`. This vanishes on `H = ker Tr` iff `Tr(x^2 y) = lambda Tr(y)` for all `y in E` and some `lambda`, iff `x^2 = lambda in F_p`, because the trace form is nondegenerate. Then `F_p(x) supseteq F_p(x^2) = F_p` with `[F_p(x):F_p] <= 2`; but `F_p(x) subseteq E` and `[E:F_p] = p` is an odd prime, so `[F_p(x):F_p] in {1,p}`, forcing `x in F_p`. Conversely every `x in F_p` lies in `H` (since `Tr(x)=px=0`) and satisfies `Tr(x^3)=px^3=0`. Hence the affine singular locus is `F_p^*`, a single projective point. `QED`

### The excluded case `p = 3` is genuinely degenerate

The hypothesis `p > 3` is not cosmetic. In characteristic `3` cubing *is* the
Frobenius, so by additivity of Frobenius

\[
\operatorname{Tr}(x^3)=\left(\operatorname{Tr}x\right)^3=\operatorname{Tr}(x),
\]

the last step by Fermat since `Tr(x) in F_3`. Hence `Tr(x^3)` vanishes
**identically** on `H = ker Tr`: there is no hypersurface at all, and the
conclusion of Lemma 5.1 fails completely. Equivalently, the differential
`3 Tr(x^2 y)` is identically zero. This is confirmed by enumeration in
`F_27`, where `|ker Tr| = 9` and the cubic vanishes at all nine points.

The exclusion costs nothing for the programme, whose admitted primes are
`p = 5 mod 6`, but the lemma must not be stated for "every odd prime".

Verified by enumeration at `p = 5, 7`, together with the `p = 3` degeneracy
(`airy_gaussian_law_verify.py`, check 4).

So the cubic form is smooth away from one point — maximally nondegenerate. This is *consistent* with, and explains, the Gaussian law: a nondegenerate cubic form's exponential sum is generic, hence square-root-sized with a random-sign coefficient. It also removes the last structural reason to expect a bounded constant.

## 6. Where the pivotal unknown actually is

`GATE0_PRIME_DEPENDENCY_AUDIT_20260724.md` states the dependency interface exactly:

\[
\mathcal R_p=S_p+M_pT_p,
\qquad
C(p)<B_p:=\frac{L_p-|S_p|}{|M_p|\,p^{(p-1)/2}} .
\]

and rules (lines 74--86):

> They do **not** provide `M_p`, `S_p`, or an equivalent exact formula. Consequently `B_p` cannot be evaluated. [...] Do not claim that absolute `C` is necessary for the Fortune crown. [...] Once that formula exists, the slack question becomes elementary.

Three further facts, all already committed, now become load-bearing.

1. **The proved unconditional bound is already `o(p)`.** From `CHARACTER_ORBIT_AND_EXTENSION_BOUND.md`, elementary Weil applied termwise to `T_p = (1/p) sum_b sum_{x in K} psi_K(x^3+bx)` gives
   \[
   |T_p|\le\frac{2(p-1)}{\sqrt p}p^{(p-1)/2},
   \]
   i.e. `C(p) <= 2 sqrt p`, combined with the Chuang `mu_3` bound `(p-5)/3`.
2. **The other two independent thresholds in the repository both read `o(p)`, not `O(1)`.** The Lemma L route needs "*any* `o(p^p)` bound on the fluctuating part of `R_a`" (`D1_ATTACK.md`), and the Sawin interval-variety route needs a Betti bound `B(pi) = o(p)` (`FRONTIER.md`).
3. **The ledger margin is large and growing.** With `B_+ = 0` proved uniformly for `p = 5 mod 6`, the certificate `0 < N_+ < 2p` reads `|S_0+S_chi| < 2p(p-2)`. Against the committed exact values the observed usage is a *shrinking* fraction of the tolerance:

   | `p` | `S_0+S_chi` | `2p(p-2)` | usage |
   |---:|---:|---:|---:|
   | 11 | `-110` | `198` | `0.56` |
   | 17 | `-102` | `510` | `0.20` |
   | 23 | `+414` | `966` | `0.43` |
   | 29 | `-522` | `1566` | `0.33` |
   | 53 | `-530` | `5406` | `0.098` |
   | 71 | `-426` | `9798` | `0.043` |

   The numerator grows roughly like `p`; the tolerance grows like `p^2`.

If `M_p = O(1)` and `|S_p| = O(p)`, the threshold is `C(p) < 2p/M_p` — and the **already-proved** `C(p) = 2 sqrt p` closes the crown for all large `p`. Whether that hypothesis holds is unknown *because nobody has computed `M_p`*, not because it was computed and failed. The proved half-twist mismatch in `FOURIER_CAYLEY_ZERO_FREQUENCY_OBSTRUCTION_20260725.md` (canonical zero-frequency term carries twist `p-7`, Airy term `(p-7)/2`) is a genuine warning that `M_p` may carry a `p^{1/2}`; that too is a computation, not a theorem.

## 7. The programme priority is inverted

`D1_FINAL_BOULDER_PROGRAMME_20260725.md` step 5 directs:

> In parallel, construct the cubic-tail localization/projector diagram, but do not invest in final assembly until the analytic gate passes.

This ordering is now untenable, for two independent reasons:

- the analytic gate *as stated* can never pass, because the statement is false;
- the analytic gate is not known to be *needed*, and the proved bound may already suffice.

**The gate should be deleted and the order reversed.** The single highest-value next action is to compute the transport pair `(M_p, S_p)` — which is a finite calculation on objects the branch has already constructed, not a new theorem in analytic number theory.

## 8. Recommended sequence

1. **Prove the object-level nonzero-frequency Fourier--Cayley theorem** —
   construct a canonical Airy summand or subquotient of the residual
   cubic-tail complex together with its canonical residual. This, and only
   this, *defines* `M_p` and `S_p`, fixes their Tate powers and cell
   multiplicities, and makes the threshold calculation meaningful. The
   repository already isolates this positive-dimensional nonzero-frequency
   sector as the theorem-level obstruction
   (`FOURIER_CAYLEY_ZERO_FREQUENCY_OBSTRUCTION_20260725.md`).

   **Withdrawn.** The first version of this file recommended extracting
   `(M_p, S_p)` by fitting `R_p = S_p + M_p T_p` at `p = 11, 17, 23, 29`. That
   is **underdetermined and invalid**: for any chosen `m_p` the assignment
   `M_p = m_p`, `S_p = R_p - m_p T_p` satisfies the equation identically, so
   four primes give four equations in eight prime-dependent unknowns. No
   growth rate for `M_p` can be inferred from scalar data before the pair is
   defined object-theoretically. This restates, rather than resolves, the
   Gate `0'` finding.

2. **Once the symbolic bridge exists, evaluate it at `p = 11, 17, 23, 29` as
   validation**, not as a means of discovering the decomposition, and compare
   its exact growth against the proved `C(p) = 2 sqrt p`. The decision rule is
   then elementary, as Gate `0'` says:
   - `M_p = O(1)`: the crown follows from the **already-proved** bound; the analytic boulder disappears.
   - `M_p ~ sqrt p`: the threshold becomes `C(p) = o(sqrt p)`, which the conjectured `sqrt(log p)` law would satisfy.
   - `M_p ~ p`: the route needs an absolute constant, which the evidence disfavours, and the sufficient condition must be replaced wholesale.
3. **Retire `C = 4` permanently**, and restate the analytic target everywhere as the conjectural `|T_p| << sqrt(log p) p^{(p-1)/2)}`, or `<<_eps p^{(p-1)/2+eps}`. Record absolute unboundedness and the `2 sqrt(log p)` law as strong numerical conjectures, not established facts.
4. **Suspend analytic work aimed specifically at a small absolute constant.** In particular do not pursue further conductor, Spin, Clausen, Hayes or projector variants that rely on cancellation in the Adams *difference*: section 4 measures that mechanism to be absent. This is a judgement about allocation — no absolute constant has been mathematically disproved.
5. If an analytic improvement *is* required, note what section 4 implies about its shape: the loss lives inside one symmetric power at `k = p`, so the problem is the classical **uniform-in-`k` large-symmetric-power** barrier, not something idiosyncratic to this family. That reclassification is itself useful — it connects the wall to a recognised problem with a known literature rather than a bespoke obstruction.

## 9. What is and is not claimed

**Rigorous (finite exclusions from exhibited primes):**

1. No absolute constant `C < 4.8468292139` bounds `|rho_p|`, witnessed at `p = 57653`. `C = 4` fails at 27 primes below `10^5`.

**Proved here:**

2. Lemma 5.1, for `p > 3`: the cubic `{Tr(x^3)=0}` in `P(ker Tr)` has exactly one singular point. At `p = 3` the form vanishes identically on `ker Tr` and the lemma fails.

**Measured (high confidence, not theorems):**

3. `rho_p` is consistent with `N(0,2)`; KS test passes over `4806` primes.
4. `corr(M_+, M_-) = -0.04`, and the Adams difference has rms `sqrt 2` times either term.
5. Each symmetric power already achieves square-root cancellation, `rms = sqrt p`.

**Explicitly not claimed:**

- **Not** that `limsup |rho_p| = infinity`, nor the `2 sqrt(log p)` limsup law. Both are conjectures; a finite sample cannot distinguish `N(0,2)` from a sufficiently wide bounded law. Proving unboundedness is plausibly as hard as the original estimate.
- **Not** that the named half-theorem is false. Only that every constant below `4.8469` is excluded and the remainder is disfavoured.
- **Not** that item 4 proves independence, constituent-level non-cancellation, or that no use of the Adams decomposition can succeed. It refutes one specific mechanism.
- **Not** that the broader claim "any exact identity aimed at this target must be tautological" is proved. The Hayes circularity is rigorous on its own terms; the generalisation is heuristic.
- **Not** any claim that the crown is true or false. Only that the *sufficient condition* the branch adopted is stronger than the evidence suggests is true, and stronger than the repository's own Gate `0'` says is needed.
- **Not** that `(M_p, S_p)` can be obtained from scalar data. See section 8.

## 10. Verification

`airy_gaussian_law_verify.py` runs the **full `p < 10^5` range** reported above
(the first version scanned only `p < 2 x 10^4`, so it did not reproduce the
advertised figures; pass a smaller limit as `argv[1]` for a quick run). Four
independent checks, all passing:

1. calibration against all nine committed exact `T_p`, worst relative error `2.9e-14`;
2. the Gaussian law: KS statistic `0.01362` against a 5% critical value `0.01959`, a non-decreasing running maximum, and the **rigorous finite exclusion** — witness `p = 57653` with `|rho_p| = 4.8468292139`, and `C = 4` failing at 27 primes. The verifier prints an explicit note that unboundedness is *not* established by the test;
3. the Adams measurement, asserting `|corr(M_+,M_-)| < 0.15` and that the difference exceeds either term;
4. Lemma 5.1 by enumeration at `p = 5, 7`, **together with the `p = 3` degeneracy** — asserting that the cubic vanishes at all nine points of `ker Tr` in `F_27`, so that the excluded case is tested rather than merely excluded.

Independently reproduced in `AIRY_GAUSSIAN_INDEPENDENT_AUDIT_20260725.md`
(branch `gpt56/airy-gaussian-independent-audit-20260725`), including the
witness value to ten decimal places.
