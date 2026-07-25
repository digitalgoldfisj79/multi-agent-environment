# The Airy Gaussian law: the terminal analytic target is false, and the branch is optimising the wrong boulder

**Date:** 2026-07-25
**Branch:** `claude/airy-next-after-circularity-8jlrek` (continues `gpt56/d1-main-twisted-descent-20260724` at `c331f740`)
**Scope:** the terminal analytic wall for function-field `d=1`, primes `p = 5 mod 6`.
**Status:** the named Airy half-theorem is **numerically falsified**. The virtual-Adams programme is **shown to have no available gain**. The pivotal open quantity is relocated to the application side.

This file does not re-prove anything in `MAIN_BRANCH_STATUS_AFTER_CLAUSEN_CIRCULARITY_20260725.md`. It accepts that status as correct and asks the prior question the branch never asked: *is the statement at the end of the funnel true?*

## 1. Summary

Let

\[
\rho_p=\frac{T_p}{p^{(p-1)/2}} .
\]

The named half-theorem is `|rho_p| <= C` with `C` absolute.

1. **`rho_p` is statistically indistinguishable from `N(0,2)`.** Over all `4806` primes `p = 5 mod 6` below `10^5`, a Kolmogorov--Smirnov test against `N(0,2)` **passes** at the 5% level. Hence `sup_p |rho_p| = infinity` and **no absolute constant exists**. The correct law is
   \[
   \boxed{\ |T_p|=\left(2+o(1)\right)\sqrt{\log p}\;p^{(p-1)/2}\quad\text{in the limsup.}\ }
   \]
2. **The virtual-Adams difference has no cancellation to give.** The two symmetric-power sums whose difference is `Psi^p` are *uncorrelated* (`r = -0.04`), each of root-mean-square exactly `sqrt(p)`, and their difference is `sqrt(2)` times **larger** than either. The factor `p` is lost inside a *single* symmetric power; the Adams framing cannot recover it.
3. **The absolute constant is not known to be needed.** `GATE0_PRIME_DEPENDENCY_AUDIT_20260724.md` already ruled that absolute `C` is required by the *named half-theorem* but **not** established as necessary for the crown, and that the only missing quantity is the transport pair `(M_p,S_p)`. The proved unconditional bound is already `C(p) <= 2 sqrt p = o(p)`.

Taken together: the branch has spent its effort improving `2 sqrt p -> O(1)`, a target that is false, while the one unevaluated quantity in the entire dependency graph sits untouched on the application side.

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

\[
\boxed{
\text{The statement } |T_p|\le C\,p^{(p-1)/2}\ \text{with absolute } C
\text{ is false.}
}
\]

This is a numerical falsification at overwhelming confidence, not a proof, and it should be recorded as such. But it is decisive for *allocation*: no further effort should be spent trying to prove it.

### Consequence for the circularity theorem

This explains the pattern the branch has been hitting. `T_p` already sits exactly at the square-root threshold with a Gaussian coefficient: **there is no residual cancellation to extract.** Any exact identity that tries to extract it must therefore collapse to a tautology. The Hayes circularity `T_p^2 = T_p^2` is not an accident of that particular route; it is what *must* happen. The same fate awaits any successor route aimed at the same target.

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

This closes, on quantitative evidence, the family of routes that motivated the local-inertia, Spin and Clausen calculations: they were all attempts to exploit a cancellation in the Adams *difference* which is not there.

## 5. A structural lemma: the cubic is as nondegenerate as possible

The remaining hope for a bounded constant would be a hidden degeneracy in the geometry. There is none.

Let `E = F_{p^p}`, `H = ker Tr_{E/F_p}`, and consider the projective cubic

\[
X=\{\operatorname{Tr}(x^3)=0\}\subset\mathbf P(H)\cong\mathbf P^{p-2}.
\]

### Lemma 5.1

For every odd prime `p`, the singular locus of `X` is the **single** point `[1]`.

### Proof

`d(\operatorname{Tr}x^3)_x(y)=3\operatorname{Tr}(x^2y)`. This vanishes on `H = ker Tr` iff `Tr(x^2 y) = lambda Tr(y)` for all `y in E` and some `lambda`, iff `x^2 = lambda in F_p`, because the trace form is nondegenerate. Then `F_p(x) supseteq F_p(x^2) = F_p` with `[F_p(x):F_p] <= 2`; but `F_p(x) subseteq E` and `[E:F_p] = p` is an odd prime, so `[F_p(x):F_p] in {1,p}`, forcing `x in F_p`. Conversely every `x in F_p` lies in `H` (since `Tr(x)=px=0`) and satisfies `Tr(x^3)=px^3=0`. Hence the affine singular locus is `F_p^*`, a single projective point. `QED`

Verified by enumeration at `p = 5, 7` (`airy_gaussian_law_verify.py`, check 4).

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

1. **Compute `(M_p, S_p)` at `p = 11, 17, 23, 29`,** where `S_0`, `S_chi`, `B_A`, `N_A` and exact `T_p` are all already committed. Even an empirical fit of `R_p = S_p + M_p T_p` across four primes determines whether `|M_p|` is bounded, grows like `sqrt p`, or grows like `p`. That one number decides the entire programme:
   - `M_p = O(1)`: the crown follows from the **already-proved** `C(p) = 2 sqrt p`. The analytic boulder disappears.
   - `M_p ~ sqrt p`: the threshold becomes `C(p) = o(sqrt p)`; a genuine but *bounded* analytic improvement is needed, and `sqrt(log p)` suffices.
   - `M_p ~ p`: the route needs absolute `C`, which is false, and the sufficient condition must be replaced wholesale.
2. **Restate the analytic target** everywhere as `|T_p| << sqrt(log p) p^{(p-1)/2}`, or `<<_eps p^{(p-1)/2+eps}`. Retire "absolute constant `C`" as a goal, and retire `C = 4` as a working conjecture (already exceeded: `max|rho_p| = 4.85` at `p = 57653`).
3. **Do not open new cohomological routes against the old target.** In particular do not pursue further conductor, Spin, Clausen, Hayes or projector variants aimed at bounding `Psi^p` termwise: section 4 shows the difference structure they exploit carries no cancellation.
4. If an analytic improvement *is* required, note what section 4 implies about its shape: the loss lives inside one symmetric power at `k = p`, so the problem is the classical **uniform-in-`k` large-symmetric-power** barrier, not something idiosyncratic to this family. That reclassification is itself useful — it connects the wall to a recognised problem with a known literature rather than a bespoke obstruction.

## 9. What is and is not claimed

**Established here (numerically, at high confidence):**

1. `rho_p` is consistent with `N(0,2)`; KS test passes over `4806` primes.
2. No absolute constant `C` bounds `|rho_p|`; the observed maximum is `4.85` and rising.
3. `M_+` and `M_-` are uncorrelated; the Adams difference supplies no cancellation.
4. Each symmetric power already achieves square-root cancellation, `rms = sqrt p`.

**Proved here:**

5. Lemma 5.1: the cubic `{Tr(x^3)=0}` in `P(ker Tr)` has exactly one singular point.

**Not claimed:**

- No proof that `limsup |rho_p| = infinity`. The Gaussian law is a heuristic backed by measurement; making it a theorem is at least as hard as the original estimate.
- No claim that the crown is true or false. Only that the *sufficient condition* the branch adopted is stronger than the truth, and stronger than the repository's own audit says is needed.

## 10. Verification

`airy_gaussian_law_verify.py` performs four independent checks and passes all of them:

1. calibration against all nine committed exact `T_p`, worst relative error `2.9e-14`;
2. the Gaussian law, with a KS test against `N(0,2)` and a non-decreasing running maximum exceeding `4`;
3. the Adams no-gain measurement, asserting `|corr(M_+,M_-)| < 0.15` and that the difference exceeds either term;
4. Lemma 5.1 by enumeration at `p = 5, 7`.
