# Fresh-model cold review packet: punctured-centre full-band Fortune reduction

Date: 29 July 2026  
Repository: `digitalgoldfisj79/multi-agent-environment`  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`  
Mathematical review base head: `224d670d98cc4bf46c401569758c91537b78b46a`  
Pull request: `#33`  

## 0. Review posture

This packet is for a hostile, independent mathematical review. Do not assume that a displayed identity is correct because a verifier passes. Re-derive every load-bearing identity from the definitions, inspect the exact support conditions, and distinguish:

- proved algebra;
- proved estimates from classical input;
- finite exact verification;
- empirical diagnostics;
- open theorems.

The current programme does **not** prove Fortune's conjecture. Its claim is that the first physical-band obstruction has been reduced to one explicit arithmetic theorem after several earlier apparent obstructions were removed exactly.

A useful review should either:

1. validate the reductions and sharpen the remaining theorem;
2. identify a precise false step or missing hypothesis;
3. provide an existing theorem that closes the stated boundary with literal parameter verification; or
4. produce a counterexample showing that the proposed full-band Bessel target is false for the actual coefficients.

## 1. Original integer Fortune target

Let

\[
P_n=p_n\#,
\]

and let `F_n` be the least integer `m>1` such that `P_n+m` is prime. Since every `2\le m<p_{n+1}^2` that is composite has a prime factor at most `p_{n+1}`, the conjectural target is equivalent to proving that for every sufficiently large `n` there is a prime in

\[
(P_n,P_n+p_{n+1}^2).
\]

The current branch works on a dyadic family of consecutive primorial centres with largest prime factors in `[X,2X)` and source length

\[
H=\eta X^2,
\qquad 0<\eta<1.
\]

The intended analytic endpoint is a variance theorem over these centres strong enough to force a prime in each required interval.

## 2. State before the present reduction

Earlier commits on the branch established exact normalized-survivor and frame identities. The immediately preceding boundary was:

- the first physical band could be represented as a complete normalized Euler survivor;
- one Type-II variable and the primorial centre formed a bounded inverse-orbit frame on blocks `K\ll\log X`;
- conductors containing at least two first-band primes had a small complete-model centre collision frame;
- applying generic Cauchy to the remaining Type-II variable lost `X^{1-o(1)}/\log X`;
- physical and high-conductor contributions could not be bounded separately because their covariance is sign-indefinite.

The next programme therefore reinserted the complete Euler band before applying `TT*`, extracted the exact source-product diagonal, and retained only the off-product bilinear survivor tensor.

## 3. Exact prime-source identity

Set

\[
Y=\lceil\sqrt H\rceil.
\]

Because `H<X^2`, one has `Y<X` for the fixed `\eta<1` regime once `X` is large enough.

Define

\[
\mu_{\le Y}(d)=\mu(d)\mathbf 1_{d\le Y},
\qquad
\mu_{>Y}(d)=\mu(d)\mathbf 1_{d>Y}.
\]

### Claim 3.1 — exact two-level identity

For every `n\le H`:

\[
\boxed{
\Lambda(n)
=
2(\mu_{\le Y}*\log)(n)
-
(\mu_{\le Y}*\mu_{\le Y}*1*\log)(n).
}
\tag{3.1}
\]

This is the `k=2` Heath--Brown identity in the range `n\le Y^2`.

### Claim 3.2 — one-small-variable resummation

Using `\mu*1=\varepsilon` and `\mu=\mu_{\le Y}+\mu_{>Y}`, (3.1) resums exactly to

\[
\boxed{
\Lambda
=
\mu_{\le Y}*\log
+
\mu_{\le Y}*\mu_{>Y}*1*\log
\qquad(n\le H).
}
\tag{3.2}
\]

The significance is structural: every term has exactly one explicitly small Möbius variable `d\le Y`. The provisional decomposition with several small Möbius variables and separate overlap classes is unnecessary.

### Review task A

Re-derive (3.1) and (3.2), checking carefully:

- the endpoint convention when `Y=\lceil\sqrt H\rceil`;
- whether the identity is required at `n=1` or only `n\ge2`;
- the convolution convention for `\log`;
- whether any prime-power or endpoint correction was silently moved elsewhere.

## 4. Punctured-centre transport

Every nonzero term from the small variable satisfies `\mu(d)\ne0`, so `d` is squarefree. Since `d\le Y<X`, every prime factor of `d` divides every primorial centre `P_j` in the block. Hence

\[
\boxed{d\mid P_j.}
\tag{4.1}
\]

For every first-band prime `p>X`, `(d,p)=1` and `(P_j/d,p)=1`. Therefore

\[
P_j=d(P_j/d)
\]

and

\[
\boxed{
 p\mid P_j+dm
 \iff
 p\mid P_j/d+m.
}
\tag{4.2}
\]

Equivalently, in inverse-orbit form,

\[
\boxed{
 dP_j^{-1}\equiv(P_j/d)^{-1}\pmod p.
}
\tag{4.3}
\]

The small Möbius variable punctures the primorial centre rather than behaving as an arbitrary bilinear coefficient.

### Review task B

Check that the actual source decomposition never requires a non-squarefree small variable, and that every dyadic cell retains the divisibility information needed for (4.2) rather than absorbing it into a generic coefficient.

## 5. Complete full-band amplitude

For a first physical dyadic band `\mathcal P_R`, define

\[
V_R=\prod_{p\in\mathcal P_R}\frac{p-2}{p-1}
\]

and the centred normalized survivor on the product of unit groups by

\[
g_R(x)
=
V_R^{-1}
\mathbf 1_{x_p\ne1\ \forall p\in\mathcal P_R}
-1.
\tag{5.1}
\]

For one exact source cell, let

\[
b(n)=\sum_{uv=n}\alpha_u\gamma_v.
\]

The complete band amplitude at centre `P_j` is

\[
\mathcal F_{j,R}
=
\sum_n b(n)g_R(-nP_j^{-1}).
\tag{5.2}
\]

This contains all Euler orders in the band. No physical/high-conductor split is made before squaring.

The exact square is

\[
|\mathcal F_{j,R}|^2
=
\sum_n|b(n)|^2|g_R(-nP_j^{-1})|^2
+
\sum_{n\ne n'}b(n)\overline{b(n')}
 g_R(-nP_j^{-1})\overline{g_R(-n'P_j^{-1})}.
\tag{5.3}
\]

## 6. Exact source-product diagonal

For the fully recombined prime source, let `M_Z` be the number of source primes under consideration and let `H_{j,R}` be the number hit by at least one first-band prime. Put

\[
\delta_R=V_R^{-1}-1.
\]

On an unhit source, `g_R=\delta_R`; on a hit source, `g_R=-1`. Hence the exact source-product diagonal is

\[
\boxed{
\mathcal D_{j,R}
=(M_Z-H_{j,R})\delta_R^2+H_{j,R}.
}
\tag{6.1}
\]

Using the frozen source weight `\beta_j` from the branch, the claimed bound is

\[
\boxed{
\sum_{j\in B}\beta_j^2\mathcal D_{j,R}
\ll KH\log X.
}
\tag{6.2}
\]

The first-band Fortune block allowance is

\[
\asymp \frac{KHX}{\log X}.
\tag{6.3}
\]

Thus the diagonal is below the allowance by a factor of order `X/\log^2X`.

### Review task C

Verify (6.2) from the exact definitions of `\beta_j`, `M_Z`, `H_{j,R}` and `V_R`. In particular, check:

- all logarithmic factors;
- uniformity across first-band dyadic ranges;
- the sparse prime-power correction;
- whether recombination of the source cells changes the diagonal coefficient or introduces cross-cell diagonal terms.

## 7. Punctured-centre Gram

For first-band prime `p`, logarithmic centre block `B`, and small squarefree variables `d,d'\le Y`, the claimed fixed-modulus Gram is

\[
\boxed{
G_p((j,d),(k,d'))
=
\frac1p\mathbf 1_{p\mid P_jd'-P_kd}
-
\frac1{p^2}.
}
\tag{7.1}
\]

This is the additive-frequency Gram for the punctured orbit

\[
(j,d)\longmapsto (P_j/d)\pmod p
\]

or equivalently its inverse phase.

### Review task D

Re-derive (7.1), including the exact normalization and whether the zero additive frequency has been removed consistently with the unit-residue centring.

## 8. Off-product collision collapse

Consider balanced source products

\[
n=dm,
\qquad
n'=d'm',
\qquad
n,n'<p^2.
\]

After the integer product diagonal `n=n'` is removed, a low-mode collision at prime `p` is exactly

\[
\boxed{p\mid dm-d'm'.}
\tag{8.1}
\]

Because `d,d',m,m'<p` in the balanced cells under review:

- if `d=d'`, then (8.1) implies `m=m'`;
- if `m=m'`, then (8.1) implies `d=d'`.

Therefore both one-variable collision strata consist entirely of the removed product diagonal. The only surviving collision stratum is

\[
\boxed{
 d\ne d',
 \qquad
 m\ne m',
 \qquad
 p\mid dm-d'm'.
}
\tag{8.2}
\]

Furthermore, because `|dm-d'm'|<H<X^2`, at most one first-band prime can divide this nonzero determinant.

### Review task E

This is a particularly important support-sensitive claim. Check:

- that every critical balanced cell really has all four variables below the first-band primes;
- whether cells with one variable reaching or exceeding `p` were excluded, reclassified or overlooked;
- whether `n,n'<p^2` is strict enough at all dyadic endpoints;
- whether product equality can occur with `d\ne d'` and `m\ne m'`, and whether it has been removed before the argument.

## 9. Exact multiplicative residue energy

For fixed `p`, define

\[
r_p(a)
=
\sum_{dm\equiv a\pmod p}\alpha_d\gamma_m,
\]

with

\[
A=\sum_d\alpha_d,
\qquad
C=\sum_m\gamma_m.
\]

The claimed exact identity is

\[
\boxed{
\sum_{a\in\mathbb F_p^\times}
\left|r_p(a)-\frac{AC}{p-1}\right|^2
=
\frac1{p-1}
\sum_{\chi\ne\chi_0}
\left|\sum_d\alpha_d\chi(d)\right|^2
\left|\sum_m\gamma_m\chi(m)\right|^2.
}
\tag{9.1}
\]

For the actual source,

\[
\alpha_d=\mu(d)
\]

on the small range, while `\gamma_m` is the exact signed coefficient produced by (3.2), including the large-Möbius and logarithmic convolutions.

### Review task F

Re-derive (9.1) and identify the strongest known theorem that applies to the literal coefficient pair. A citation is useful only if all of the following are checked explicitly:

- modulus range `p\asymp X`;
- source-product length `H\asymp X^2`;
- small variable length `Y\asymp X` but strictly below `p`;
- exact Möbius and Heath--Brown weights;
- averaging over consecutive primorial centres;
- coherent summation across distinct physical moduli;
- preservation of the complete Euler-band signs.

## 10. Remaining full-band theorem

The branch currently isolates the following first-band target. For the exact source coefficients `c_d(m)` produced by (3.2), prove

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{d\le Y}\mu(d)
\sum_m c_d(m)
 g_R\!\left(-m(P_j/d)^{-1}\right)
\right|^2
\ll
\sum_{j,n}|b(n)|^2|g_R(-nP_j^{-1})|^2
+E_{B,R},
}
\tag{10.1}
\]

where:

- the source-product diagonal is already isolated;
- every physical and higher conductor in the band remains present;
- the signs between physical and one-point conductors are preserved;
- `E_{B,R}` must be summable over source cells, dyadic bands and logarithmic centre blocks at the Fortune scale.

The irreducible arithmetic content is described as:

\[
\boxed{
\text{Möbius-weighted multiplicative energy plus coherent cross-conductor survivor cancellation.}
}
\tag{10.2}
\]

This is not yet a theorem.

## 11. What has been closed as a direct route

Subject to validation of the preceding algebra, the branch treats the following as closed without a new ingredient:

1. a three-small-variable Heath--Brown decomposition;
2. separate overlap estimates among small variables;
3. another arbitrary-coefficient frame followed by Cauchy;
4. unweighted multiplicative energy as a substitute for the actual source coefficients;
5. direct insertion of currently available square-root Kloosterman bounds before full survivor recombination;
6. separate positive estimates of physical and high-conductor terms.

A reviewer should reopen one of these only by giving a concrete estimate that reaches the literal Fortune block scale and preserves the required signs.

## 12. Exact and computational evidence

### Proved algebraically in the notes

- two-level identity (3.1);
- one-small-variable resummation (3.2);
- punctured-centre transport (4.2)--(4.3);
- source diagonal formula (6.1);
- punctured-centre Gram (7.1);
- determinant collision kernel (8.1);
- multiplicative residue-energy identity (9.1).

### Finite exact verification

The committed verifiers check:

- source identities on complete panels `X=11,17,23,29,37`;
- punctured-centre transport and Gram identities;
- exact full-band diagonal/off-diagonal square decomposition;
- one-variable collision collapse;
- more than two million finite determinant/collision instances on panels `X=11,17,23`.

Finite verification does not establish any asymptotic estimate.

## 13. Files to inspect first

Authoritative notes:

1. `frontier/integer_source_frame_bridge/PROGRAMME_STATUS_AFTER_PUNCTURED_CENTRE_GATE_20260729.md`
2. `frontier/integer_source_frame_bridge/PRIME_SOURCE_TWO_LEVEL_IDENTITY_AND_PUNCTURED_CENTRE_20260729.md`
3. `frontier/integer_source_frame_bridge/PUNCTURED_CENTRE_FULL_BAND_GATE_20260729.md`
4. `frontier/integer_source_frame_bridge/NEXT_PROGRAMME_FULL_BAND_TYPEII_DISPERSION_20260729.md`
5. `frontier/integer_source_frame_bridge/PRIMORIAL_ORBIT_TYPEII_AND_HIGH_CONDUCTOR_FRAME_20260729.md`
6. `frontier/integer_source_frame_bridge/COMPLETE_CRT_SURVIVOR_GRAM_AND_SAMPLING_BOUNDARY_20260729.md`

Verifiers and frozen results:

1. `frontier/integer_source_frame_bridge/prime_source_heath_brown_verify.py`
2. `frontier/integer_source_frame_bridge/prime_source_heath_brown_results.json`
3. `frontier/integer_source_frame_bridge/punctured_centre_offdiagonal_verify.py`
4. `frontier/integer_source_frame_bridge/punctured_centre_offdiagonal_results.json`
5. `frontier/integer_source_frame_bridge/full_band_typeii_programme_verify.py`
6. `frontier/integer_source_frame_bridge/full_band_typeii_programme_results.json`

Relevant workflows:

- `.github/workflows/validate-prime-source-heath-brown.yml`
- `.github/workflows/validate-punctured-centre-offdiagonal.yml`
- `.github/workflows/validate-full-band-typeii-programme.yml`

## 14. Requested reviewer output

Please return a report with the following structure.

### A. Verdict table

For each of Claims 3.1, 3.2, 4.2, 6.1, 6.2, 7.1, 8.1--8.2 and 9.1, mark:

- correct as stated;
- correct with missing hypotheses;
- incorrect;
- unclear from the committed material.

Give a derivation or counterexample for every nontrivial verdict.

### B. Scale audit

Recompute the dimensions and logarithmic factors in:

- the source diagonal;
- the off-product determinant energy;
- the centre block summation;
- the required Fortune allowance.

State the exact missing factor after the best classical estimate you can justify.

### C. Literature match

Identify the closest applicable theorem for (9.1) or (10.1). Do not cite by analogy: map every parameter and hypothesis explicitly. State whether it:

- closes the theorem;
- gives a partial power/logarithmic saving;
- is inapplicable.

### D. Best next move

Choose exactly one:

1. prove a Möbius-weighted multiplicative fourth-moment theorem;
2. derive a stronger all-order cancellation identity before estimating (9.1);
3. refute the proposed full-band Bessel theorem by an actual-coefficient counterexample;
4. identify a different exact decomposition that bypasses the determinant kernel.

Provide a concrete mathematical programme, not a list of generic techniques.

## 15. Current boundary

**PROVED EXACTLY, subject to cold review**

- exact two-level prime-source identity;
- one-small-variable resummation;
- punctured-centre transport;
- exact full-band source-product diagonal;
- punctured-centre Gram;
- collapse of one-variable collision strata;
- determinant kernel `p\mid dm-d'm'`;
- multiplicative residue-energy identity.

**PROVED FROM ELEMENTARY/CLASSICAL INPUT, subject to scale audit**

- source-product diagonal is Fortune-admissible;
- at most one first-band prime divides a nonzero source determinant.

**COMPUTATIONALLY VERIFIED**

- the listed finite exact identities and collision checks.

**OPEN**

- actual-coefficient Möbius-weighted fourth moment;
- coherent physical/high-conductor full-band contraction;
- signed source-cell recombination at theorem scale;
- first physical-band theorem;
- `NSMT(X)`;
- Fortune variance theorem;
- Fortune's conjecture.
