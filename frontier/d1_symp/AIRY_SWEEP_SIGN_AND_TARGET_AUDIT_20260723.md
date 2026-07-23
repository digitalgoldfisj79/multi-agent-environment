# Sign, sweep, and target audit for the Airy edge programme

**Date:** 2026-07-23  
**Status:** corrections and statistical recomputation complete.

## 1. Sign correction

The separate-trace computation correctly retracted the claim that two earlier displays contradicted each other. The stronger repository-level ruling is:

- the two displays are mutually consistent;
- both are sign-reversed relative to the explicit positive hyperplane definition of `T_p` in `COLLAPSE_LEMMA.md`.

The correct identity is

\[
pT_p=\sum_uD_p(t_u,p)=\operatorname{Tr}(F|U_p)-p\operatorname{Tr}(F|U_{p-2}).
\]

The `p=5` calculation fixes only the additive-sum/Dickson orientation. Since `T_5=0`, it contains no information about the `T`-to-cohomology sign. The later separated traces fix that missing side.

## 2. What the trace inequalities prove

At `p=11`, rank one plus exact saturation determines the individual eigenvalues and verifies the predicted modulus.

At ranks `2,3,4`, passing

\[
|\operatorname{Tr}(F|U_k)|\le\dim(U_k)p^{(k+1)/2}
\]

shows compatibility with purity, not purity itself. The third-power computation in `AIRY_ODD_POWER_SPECTRA_AUDIT_20260723.md` is what upgrades several low-rank cases to complete individual spectra.

## 3. Exact audit of the sweep through `10^5`

The uploaded CSV contains `4806` primes `p ≡ 5 (mod 6)` up to `100000`. Independent recomputation gives

- `RMS(z)=1.0239444050`;
- maximum `|z|=3.4272555277` at `p=57653`;
- fourteen-bin growth slope `0.5220202 ± 0.0285417` using the supplied OLS formula;
- Spearman `rho(|z|,p)=0.01903`, `p=0.1871`.

These reproduce the continuation's descriptive statistics.

The extreme-value calibration in that continuation was incorrect. For `n` independent standard normal variables,

\[
\Pr\left(\max_{i\le n}|Z_i|\le x\right)=(2\Phi(x)-1)^n.
\]

At `n=4806`, numerical integration gives

\[
\mathbf E\max|Z_i|=3.8418853,
\]

not approximately `3.55`. The observed maximum `3.4273` is at approximately the `5.33` percentile of the iid-normal maximum distribution. It is statistically compatible with that null, but low rather than typical.

The ratio to `sqrt(2 log n)` is not an independent growth test. A running maximum is piecewise constant while the denominator changes slowly; three ratios cannot establish a Gumbel rate.

## 4. Correct empirical conclusion

The sweep supports typical square-root scale and a nearly Gaussian one-prime marginal distribution over the tested range. It does **not** distinguish:

1. a uniformly bounded normalized arithmetic sequence;
2. a sequence with very slow unbounded extremes;
3. an iid-like Gaussian extreme law emerging only later.

It supplies no positive evidence that the absolute-constant target is false. Extending the same sweep to `10^6` would add calibration but cannot decide boundedness.

## 5. Gate 0

The documented Airy half-theorem requires

\[
|T_p|\le C p^{(p-1)/2}
\]

with absolute `C`. Neither a `sqrt(log p)` loss nor a `p^epsilon` loss closes that intermediate statement.

However, the repository does not contain the final categorical application ledger from this Airy estimate to `FF-Fortune(p,1)`. Therefore:

- absolute `C` is required for the currently stated Airy half-theorem;
- its necessity and sufficiency for the full function-field Fortune crown have not been proved.

The target cannot responsibly be weakened, but the analytic estimate also cannot yet be advertised as a completed implication to the crown.
