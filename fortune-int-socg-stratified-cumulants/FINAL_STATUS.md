# INT-SOCG stratified-cumulant closeout

**Programme:** `FORTUNE_INT_SOCG_STRATIFIED_CUMULANTS_V0_1`  
**Date:** 5 August 2026  
**Branch:** `gpt56/fortune-int-socg-stratified-cumulants-v01-20260805`  
**Outcome:** `MEAN_LOWER_BOUND_IS_PRIMARY_OBSTRUCTION`  
**Terminal target:** `INT-SCME`

## Final ruling

The programme does not establish `INT-SOCG`, `INT-AOD`, or Fortune's conjecture. It isolates the first-cumulant lower bound as the logically prior obstruction and reduces it to one exact selected-centre weighted mean theorem.

## Primary successor

For every deterministic stratum, prove

\[
T_b=
\frac1{n_b}
\sum_{j\in B_b}
\sum_{m\in\mathcal M_b}
\log m\,\Lambda(P_j+m)
\ge\kappa X^2\log X.
\]

Proper output prime powers contribute only

\[
O(X(\log X)^2)
\]

per row. Therefore `INT-SCME` implies

\[
c_{1,b}\ge c_0X.
\]

No selected-primorial-centre theorem found in the literature audit supplies this lower bound. Generic short-interval, dense-shift and singular-series-average results do not transfer to the registered sparse multiplicative path.

## Exact results obtained

### Deterministic stratification

The programme fixes `sigma=1/2`, terminal-prime width

\[
W_X=X/(\log X)^{3/2},
\]

common restricted offset universes and output-independent temperatures. Transition-prime reciprocal mass is subcritical.

### Correct factorial-cumulant reduction

If `f_{r,b}` are the correctly defined scalar factorial cumulants, then

\[
c_{k,b}=\sum_{r=1}^kS(k,r)f_{r,b}.
\]

The coefficientwise ordered-partition bound

\[
r!S(k,r)\le k!\binom{k-1}{r-1}
\]

gives

\[
|f_{r,b}|\le c_{1,b}r!D^{r-1}
\Longrightarrow
|c_{k,b}|\le c_{1,b}k!(D+1)^{k-1}.
\]

Thus repeated-column ordinary-cumulant patterns add only one to the dependence radius. This does not identify factorial cumulants with ordinary distinct-column joint cumulants.

### Local pair scale

The post-terminal collision-plus-tail edge majorant has candidate-column row sum

\[
O(X/(\log X)^2).
\]

Pairwise local interaction is therefore subcritical. The all-orders local connected tree or hypergraph theorem `INT-LCSK` remains open.

### Prime-modulus primorial-walk theorem

For prime `q>2X`, collision of two primorial rows at distance `d` can occur for fewer than `d` such prime moduli. Consequently

\[
\sum_{\substack{2X<q\le Q\\q\text{ prime}}}
\sum_{c\bmod q}
\left|\sum_ja_je(cP_j/q)\right|^2
\le
\left(
\sum_{\substack{2X<q\le Q\\q\text{ prime}}}q+Qn_b^2
\right)
\sum_j|a_j|^2.
\]

The weighted squarefree-composite extension required by source decompositions remains open.

## Closed direct methods

Exact Vaughan, Heath--Brown and divisor decompositions of the output von Mangoldt factor require scales far beyond `H`. For moduli above `H`, each row supplies at most one offset per residue class, leaving only `n_b` selected centres. The prime-modulus energy already has a diagonal floor too large at exponential conductor ranges. Classical lower sieve and switching routes retain the parity or sparse-hyperbola obstruction.

These are method closures, not universal impossibility theorems.

## Diagnostics

The corrected exact panel and orbit job reruns:

- factorial-to-ordinary transforms;
- the weighted-mean prime-power scale;
- prime-modulus Parseval and collision bounds;
- local edge rows;
- selected-centre panels through `X=300`;
- primorial-walk traces through `X=800`.

Finite panels are diagnostic only and are not promoted.

## Explicitly not claimed

- `INT-SCME`;
- `INT-LCSK`;
- the composite-modulus `INT-PWOC` extension;
- `INT-SOCG` or `INT-AOD`;
- Fortune's conjecture;
- any function-field-to-integer transfer.
