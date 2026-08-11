# Fable review intake and corrected punctured-centre boundary

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`  
Reviewed mathematical base: `224d670d98cc4bf46c401569758c91537b78b46a`  
Review comment: PR #33, issue comment `5124074182`

## Executive decision

The hostile Fable review is accepted in its central conclusion.

The punctured-centre programme contains a valid new reduction and correct exact algebra, but one collision-support statement was over-scoped. The assertion that the one-variable collision strata reduce to the removed product diagonal is valid only when the relevant source variables are shorter than the physical modulus. It is false on the full unbalanced ranges occurring when `m` extends to `H/d >= p`.

This is a repairable support-ledger flaw, not a failure of the two-level prime-source identity, punctured-centre transport, complete source diagonal, punctured Gram, or weighted multiplicative residue-energy identity. Fortune's conjecture remains **OPEN**.

## 1. Accepted valid claims

The following survive the review.

### 1.1 Exact two-level source identity

With `Y=ceil(sqrt(H))<X`, on `n<=H`:

\[
\Lambda
=
2\mu_{\le Y}*\log
-\mu_{\le Y}*\mu_{\le Y}*1*\log,
\]

and equivalently

\[
\boxed{
\Lambda
=
\mu_{\le Y}*\log
+\mu_{\le Y}*\mu_{>Y}*1*\log.
}
\]

The resummation leaves one explicitly small Möbius variable. The arithmetic contained in the large-variable coefficient remains sign-bearing and must not be replaced by an arbitrary divisor-bounded source.

### 1.2 Punctured-centre transport

For every nonzero squarefree `d<=Y`, one has `d|P_j`; for every first-band prime `p>X`,

\[
p\mid P_j+dm
\iff
p\mid P_j/d+m.
\]

The transport is exact. Its presently proved gain is bookkeeping, injectivity and residue-multiplicity control. No reciprocity or interval localization follows merely from writing `P_j/d`.

### 1.3 Complete source-product diagonal

The exact diagonal formula for the fully recombined source remains valid and lies below the Fortune block allowance. This admissibility belongs to the recombined amplitude. It may not be transferred automatically to a proof that estimates dyadic source cells separately and then sums their positive diagonal costs.

The imported bound on the frozen coefficient `beta_j` remains a dependency to be cited explicitly in any final theorem.

### 1.4 Punctured Gram and multiplicative energy

The punctured-centre Gram and the weighted multiplicative residue-energy identity remain valid, subject to excluding non-unit source terms when a long variable contains multiples of `p`.

## 2. Accepted correction

For fixed `d=d'` with `(d,p)=1`, the collision condition is

\[
p\mid d(m-m')
\iff
m\equiv m'\pmod p.
\]

The earlier inference `m=m'` requires `m,m'` to lie in an interval of length less than `p`. The committed verifier used `m,m'<=Y<p`, so it checked precisely the range where this inference is true.

On the actual unbalanced source range `m,m'<=H/d`, if `H/d>=p+1`, pairs such as

\[
m'=m+p
\]

are distinct one-variable collisions. The review exhibited complete-panel counterexamples, beginning with

- `X=11`, `p=13`, `d=d'=1`, `m=1`, `m'=14`;
- `X=17`, `p=19`, `d=d'=1`, `m=1`, `m'=20`;
- `X=23`, `p=29`, `d=d'=1`, `m=1`, `m'=30`.

Therefore the following unscoped statements are retracted:

- "the one-variable collision strata disappear";
- "only the genuinely two-variable determinant stratum survives".

They are replaced by:

> On cells whose relevant source intervals have length below `p`, the one-variable strata consist only of the removed product diagonal. Long cells require exact completion modulo `p` and a separate dual-kernel ledger.

## 3. Sharpened analytic boundary

The review also correctly sharpens the remaining theorem.

1. A suitable fixed-modulus Möbius-character estimate is a GRH consequence per modulus. The essential open content is unconditional uniformity at `D~p`, coherent averaging across prime moduli, and preservation of physical/high-conductor signs.
2. The punctured centre does not itself create an archimedean interval of inverted numerators; standard Kloosterman-fraction theorems do not become directly applicable from the identity alone.
3. The at-most-one-collision-prime property remains exact for distinct integer products below `H<X^2` and is the most useful surviving global structure.

## 4. Revised programme

### Gate U0 — unbalanced-cell completion

For every dyadic cell with long variable `M>=p`:

1. split the long source into complete residue blocks modulo `p` plus a remainder;
2. complete the `m`-sum exactly on `F_p`;
3. separate non-unit terms `p|m`;
4. derive the dual punctured-centre kernel;
5. recompute the diagonal/off-diagonal ledger without assuming `m<p`;
6. verify the formula on the true ranges `m<=H/d`.

No later determinant theorem is authoritative until this gate passes.

### Gate U1 — exact signed determinant reordering

After combining balanced and completed unbalanced cells, use the fact that a nonzero difference below `H` contains at most one first-band prime divisor. Reorder the band-summed off-diagonal as a signed representation sum over

\[
\Delta=dm-d'm'.
\]

The band-divisibility indicator must be recombined with the complete survivor before any absolute values are taken.

### Gate U2 — signed determinant dispersion

The first genuinely new arithmetic target is a signed determinant-dispersion estimate of the form

\[
\sum_{d,d'\asymp D}\mu(d)\mu(d')
\sum_{m,m'\asymp M\atop dm\ne d'm'}
\gamma(m)\overline{\gamma(m')}
\mathbf 1_{\exists p\in(X,2X]:\ p\mid dm-d'm'}
\ll DM X^{o(1)},
\]

for the actual coefficient families, after the exact main-term and survivor cancellations have been identified.

The suggested progression is:

1. numerical calibration with the actual coefficients;
2. the half-signed case `gamma=1`;
3. the full Möbius-weighted determinant estimate;
4. coherent physical/high-conductor completion;
5. signed source-cell and cross-band recombination.

## 5. Corrected status

### PROVED EXACTLY

- two-level Heath--Brown identity and one-small-variable resummation;
- punctured-centre transport;
- complete recombined source-diagonal formula;
- punctured-centre Gram;
- weighted multiplicative residue-energy identity;
- at-most-one first-band collision prime for a nonzero product difference below `H`;
- one-variable collision collapse on source intervals of length less than `p`.

### COMPUTATIONALLY VERIFIED

- the exact identities on the committed finite panels;
- the balanced-slice collision collapse;
- independent Fable verification of the character identity and the unbalanced counterexamples.

### RETRACTED OR CORRECTED

- unqualified collapse of the one-variable collision strata;
- unqualified statement that only the two-variable determinant stratum survives;
- any implication that the puncture alone supplies Kloosterman reciprocity.

### OPEN

- exact completion and scale ledger for unbalanced cells;
- unconditional Möbius-weighted multiplicative energy at `D~p`;
- signed determinant dispersion;
- coherent physical/high-conductor full-band contraction;
- signed source-cell recombination;
- the first physical-band theorem, `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

## Verdict

The review improves the programme materially. It validates the main algebraic reduction, catches a real support error before it can contaminate the analytic theorem, and supplies a better ordered route. The next work is not to defend the old collision claim; it is to complete the long cells exactly and determine the true signed determinant kernel.