# Hostile-review disposition: Euler--Buchstab package

Date: 28 July 2026  
Review jobs: `6a68c0b115e81eca66a8d2cf`, `6a68c341a9f4e0ab00b2b7d0`  
Disposition: exact-identity and diagonal-theorem package passes; reviewer boundary statement corrected; deterministic transference remains open.

## 1. Review scope

The external review was asked to audit:

1. the exact Euler detector;
2. local centring and character conjugations;
3. the Brun--Titchmarsh diagonal theorem;
4. normalized coefficient mass;
5. the ordered Buchstab identity;
6. the one-hit structure and quadratic variation;
7. any illicit transfer from the complete product model to the deterministic source.

## 2. Substantive findings

The long review accepted the displayed exact identities and retained the deterministic
sampling theorem as the unresolved step.  It did not supply a concrete counterexample,
sign error, failed finite hypothesis, or invalid line in the diagonal proof.

Its final summary nevertheless displayed

\[
\sum_j|\mathcal T_j^\circ|^2\ll NHX\log X
\]

under an assumed missing transference hypothesis and called this the “strongest
corrected boundary.”  That wording is rejected.  An inequality obtained by assuming
the missing theorem is not a proved boundary.  The repository consistently labels the
sampling estimate as open.

A second compact review followed the requested labels but omitted all mathematical
reasons.  It is non-evidentiary and is not used to validate or reject any claim.

## 3. Independent disposition by claim

### Euler detector

Pass.  The identity follows locally from

\[
\frac{r-2}{r-1}(1+\xi_r(n))=\mathbf1_{r\nmid n}
\]

and globally from the least-prime-factor criterion below `sqrt(P+H)`.

### Local centring

Pass.  On nonzero offset residues modulo `r`, one divisor residue has value `-1`
and the other `r-2` residues have value `1/(r-2)`, giving mean zero.

### Character reconstruction

Pass.  Multiplicative-character orthogonality on `F_r^*` gives the displayed
conjugation `overline{chi(-P_j)}`.  The independent exact verifier reconstructs every
finite discrepancy within the committed tolerance.

### First-order diagonal theorem

Pass, with the stated hypotheses `H asymp X^2`, `z_j asymp X`, and
`|b_{j,m}| ll log X`.  Brun--Titchmarsh is used only for `r<=H/2`; the final range is
handled by the at-most-two-integers bound.  The dyadic reciprocal sum gives

\[
\mathcal D_X^{(1)}\ll NHX/\log X.
\]

### Normalized tail coefficient mass

Pass.  The exact Euler product

\[
\sum_q1/\rho(q)=1/V_H(Y)
\]

leaves per-source squared coefficient mass
`log^2(P+m) R_H(P+m)V_H(Y)`, whose total is `O(NHX)` by Mertens and the PNT.

### Ordered Buchstab identity

Pass.  It is the finite telescoping formula

\[
\prod_i(1+x_i)=1+\sum_ix_i\prod_{h<i}(1+x_h)
\]

with the normalizing products absorbed exactly.

### One-hit structure

Pass.  For an `H`-rough composite, the first tail divisor is the unique active
negative hit; the pre-hit increments are baselines and the survival factor kills every
post-hit increment.

### Quadratic variation

Pass in the complete independent residue model.  The increments are martingale
differences, and their exact squared sum is the variance of the tail-survival
indicator:

\[
V(H,Y)(1-V(H,Y)).
\]

### Deterministic transference

Open.  No file claims that complete-product orthogonality automatically holds on the
primorial source grid.  The support-only no-go and tail-diagonal obstruction explain
why this step requires a new signed arithmetic theorem.

## 4. Machine validation

The critical workflow passes from a fresh checkout and independently verifies:

1. primitive frequency grouping;
2. candidate projection and exact centring;
3. the Euler detector;
4. local progression and character identities;
5. first-order Gram algebra;
6. ordered Buchstab telescoping;
7. one-hit structure;
8. exact complete-model quadratic variation.

Machine validation supports finite identities only; asymptotic estimates remain tied to
their written proofs and cited classical inputs.

## 5. Final classification

Proved exact/unconditional:

1. Euler--Buchstab detector;
2. physical first-order discrepancy and character frame;
3. first-order diagonal theorem;
4. normalized coefficient budget;
5. ordered Buchstab martingale and complete-model quadratic variation;
6. support-only and positive-tail-diagonal obstructions.

Empirical:

1. complete first-order block calibration through `X=211`.

Open:

1. bilinear source--orbit cross-modulus dispersion;
2. deterministic martingale sampling and rough-coordinate covariance;
3. the full centred variance theorem;
4. Fortune's conjecture.

No merge-time claim should elevate any item in the open list.
