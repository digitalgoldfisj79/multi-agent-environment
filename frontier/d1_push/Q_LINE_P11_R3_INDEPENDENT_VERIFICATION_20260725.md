# Independent exact verification of the p=11 third q-line trace

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Classification:** **EXACT COMPUTER-ASSISTED RESULT**.  
**Compute job:** Hugging Face job `6a64c6c87ef3c084649685c3`, CPU-XL, 32 processes.

## 1. Quantity tested

Put

\[
Q=11^3=1331.
\]

For every

\[
q\in\mathbf F_Q\setminus\{0,2\},
\qquad
t\in\mathbf F_Q,
\]

the degree-11 polynomial

\[
qz^{11}+z^3-3z-(q-2)t
\]

was factored exactly over `F_Q` using `python-flint`.

Let `I_3(q)` be the number of `t` for which this polynomial is irreducible. The complete generic split q-line trace is

\[
S_3=(Q-2)Q-11\sum_q I_3(q).
\]

## 2. Independent result

The full census returned

\[
\boxed{
\sum_q I_3(q)=161446.
}
\]

Therefore

\[
\begin{aligned}
S_3
&=(1331-2)1331-11(161446)\\
&=-7007.
\end{aligned}
\]

Thus

\[
\boxed{S_3=-7007.}
\]

The calculation covered all

\[
1329\times1331=1,769,899
\]

generic `(q,t)` cells. No sampling or fitted recurrence was used.

## 3. Independence

The verifier was written from the q-line definition and run in a fresh remote container. It did not use the previous q-line output table, Claude's implementation, or a stored factor count. The expected value was asserted only after the independently computed total was assembled.

Committed verifier:

`frontier/d1_push/qline_p11_r3_parallel_verify.py`

## 4. Consequences

### Proved computationally

1. The `p=11` third trace in `Q_LINE_SURFACE_ASSEMBLY_AUDIT_20260725.md` is correct.
2. The low-degree q-line factors at `p=5,7` do not extend to `p=11`.
3. The discrepancy is not caused by an incorrect `q`-domain convention or a stale stored trace.

### Phase-5 implication

If the algebraic part of the q-line surface contributes an integral multiple `c_3 p^3`, the smallest possible cubic-power residual is obtained at `c_3=-5`:

\[
-7007-(-5)11^3=-352.
\]

A pure weight-one contribution of actual rank `R` has cubic trace bounded by

\[
R\,11^{3/2}.
\]

Hence this reading forces

\[
R\ge\frac{352}{11^{3/2}}>9.6,
\]

so

\[
\boxed{R\ge10.}
\]

This is a conditional lower bound because it assumes the algebraic cubic-power contribution is an integer multiple of `p^3`, as it is for a rational Tate/permutation block. It does not by itself prove growth with `p`, refute an `O(1)` bound with a larger constant, or determine the exact algebraic/transcendental split.

## 5. Ruling

The `p=11` trace is now independently secure. Phase 5 cannot be calibrated from `p=5,7` alone: a nontrivial transcendental block is already forced at `p=11` under the standard Tate-integrality model. The exact global split remains open.
