# Finite-compression / stable-rank assessment

## Terminal classification

`PSD_COMPRESSION_NO_STRICT_ARITHMETIC_GAIN`

The Zeta23 finite-compression idea was tested as a bounded exception to the frozen integer Fortune programme.  The ordinary PSD/stable-rank version does **not** create a new mainline.

## 1. Exact deterministic criterion

For nonnegative row occupancies `Z_1,...,Z_R`, put `D=diag(Z_j)`. Then

`sr(D) = (sum_j Z_j)^2 / sum_j Z_j^2`.

If one row is zero, Cauchy on the remaining at most `R-1` entries gives

`(sum_j Z_j)^2 <= (R-1) sum_j Z_j^2`.

Hence

`(sum Z)^2 > (R-1) sum Z^2`

forces every row to be nonzero.  With empirical mean `mu` and centered sum of squares `V=sum (Z_j-mu)^2`, the criterion is exactly

`V < R mu^2/(R-1)`.

An adversarial vector with one zero and all other entries equal attains equality, so the constant cannot be improved inside this scalar criterion.

## 2. This is the existing one-failure second-moment mechanism

On the Fortune scale `mu ~ X`, the right side is `~X^2`.  This is the same one-failure cost already encoded in `FortuneFormal.Integer.BlockCriterion`: a failed row contributes its full squared baseline gap, so a total centered error below `~X^2` excludes failure.

Moreover `Z_j^2` is already decomposed in the existing programme as `Z_j + 2 C_j`, where `C_j` is the off-diagonal successful-pair count.  Thus the second moment contains the same aggregated four-prime covariance term identified in Paper III.  Calling it a trace or stable rank does not lower the prime-correlation arity.

## 3. Exact panels

The first GitHub Actions execution (`31480948886`, stable-rank job `93745504723`) passed the exact diagnostic and the one-zero adversarial controls.

For the full blocks:

| X | R | zero rows | stable-rank margin above R-1 |
|---:|---:|---:|---:|
| 50 | 10 | 0 | +0.22811491 |
| 75 | 14 | 0 | +0.33232344 |
| 100 | 21 | 0 | -0.67213796 |
| 150 | 27 | 0 | +0.13064888 |
| 200 | 32 | 0 | -0.23534528 |

Thus the full-block sufficient criterion can fail even when every tested row succeeds.  This is expected: deterministic mean heterogeneity consumes the one-row stable-rank margin.

Using the pre-existing terminal-prime stratification with width `X/(log X)^1.25`, every tested stratum passed.  The worst stratum margins were respectively

`0.97943193, 0.90974729, 0.91945866, 0.91327913, 0.93288696`.

These are diagnostics only.

## 4. Stratification trade-off

For a stratum of `n_b` rows with natural variance scale written as

`n_b X L(X)`, one failed row costs `~X^2`, so the deterministic sufficient condition is

`L(X) = o(X/n_b)`.

For the full block `N~X/log X`, this is `L=o(log X)`.

For terminal-prime width `X/log(X)^(1+delta)`, the number of prime-indexed rows is heuristically

`n_b ~ X/log(X)^(2+delta)`,

and the deterministic allowance becomes

`L=o(log(X)^(2+delta))`.

This looks like a gain of `log(X)^(1+delta)`, but the averaging population has been shortened by exactly the same factor `N/n_b ~ log(X)^(1+delta)`.  Therefore the gain is not available from the existing full-block estimate by restriction; it requires a new **uniform localized four-prime covariance theorem** on every deterministic terminal-prime stratum.

This is not demonstrably weaker than the frozen variance frontier.  It trades error allowance for localization.

## 5. PSD Gram obstruction

The more natural prime-offset incidence matrix does not improve the stable-rank route.

Let `B` have one row per selected centre and let `G=B B*`.  Write `a_j=||B_j||^2`. Then

`tr G = sum_j a_j`,

while

`tr(G^2) = sum_j a_j^2 + sum_{j != k} |<B_j,B_k>|^2 >= sum_j a_j^2`.

Consequently

`sr(G) <= (sum a_j)^2 / sum a_j^2 = sr(diag(a_j))`.

So **among ordinary PSD Gram stable-rank certificates using the same row energies, the diagonal compression is optimal**.  Off-diagonal prime coincidences can only worsen the rank lower bound.  They also introduce higher prime-correlation terms.

This rules out the naive hope that a richer PSD incidence matrix will reproduce the Zeta23 gain.

## 6. What would actually be Zeta23-like

Zeta23 does not rely on a bare PSD Gram stable rank.  Its key inequality permits an indefinite Hermitian correction `P+Q`, with independent control of the positive index of `Q`.

A genuine successor for Fortune would therefore need a naturally arising signed Hermitian correction whose inertia can be controlled by already available arithmetic information and whose trace/Frobenius terms avoid the frozen four-prime/logarithmic-order barriers.

No such `Q` emerged from the exact Fortune detector or the existing collision geometry in this run.  Inventing an arbitrary correction merely moves the missing theorem into an inertia hypothesis.

## 7. Gate S5

`S5 = FAIL`.

The ordinary finite-compression route does not produce a strictly weaker available arithmetic target.  The stratified version gives a useful diagnostic reformulation but requires a new localized four-prime covariance theorem.  Non-diagonal PSD Gram constructions are dominated by the diagonal compression.

Therefore the integer Fortune frontier remains `CLOSED`.

A future finite-compression proposal may reopen this ruling only if it supplies a concrete **indefinite signed correction with independently provable inertia control**, not another PSD Gram/stable-rank reformulation.
