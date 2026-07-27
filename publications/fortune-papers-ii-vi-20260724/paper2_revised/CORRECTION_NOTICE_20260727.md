# Paper II correction notice

Date: 27 July 2026  
Status: **prior exact-hash review and compiled release superseded for the arithmetic interface**.

## Critical correction

Below `H<ell_{j+1}^2`, a prime output `P_j+m` forces `m` itself to be prime. Hence

\[
\Psi_j(H)=\sum_{\substack{m\le H\\m\ {m prime}}}\Lambda(P_j+m)+R_j(H),
\qquad R_j(H)=O(X\log X),
\]

and the ordinary short-interval centring `Psi_j-H` is not the standard conjectural fluctuation variable.

The valid implication in the circulation manuscript remains valid as an implication, but its hypothesis is withdrawn as the conjecturally natural target.

## Corrected detectors

Define

\[
Z_j(H)=\sum_{m\le H}{\bf1}_{\mathbb P}(m){\bf1}_{\mathbb P}(P_j+m),
\]

\[
Y_j(H)=\sum_{m\le H}{\bf1}_{\mathbb P}(m)\Lambda(P_j+m),
\]

and

\[
T_j(H)=\sum_{m\le H}\Lambda(m)\Lambda(P_j+m).
\]

The Hardy--Littlewood calibrations are

\[
\lambda_j(H)=\mathfrak S(P_j)\int_{\ell_j}^{H}\frac{dt}{\log t\log(P_j+t)},
\]

\[
\mu_j(H)=\mathfrak S(P_j)\int_{\ell_j}^{H}\frac{dt}{\log t},
\qquad
\nu_j(H)=\mathfrak S(P_j)H.
\]

These are conjectural baselines; the following implications are unconditional once baselines of the corresponding sizes are supplied.

## Corrected all-centres criteria

If `lambda_j asymp X` and

\[
\sum_{j<N}|Z_j-\lambda_j|^2\ll NXL(X),
\qquad L(X)=o(\log X),
\]

then every centre succeeds.

If `mu_j asymp H` and

\[
\sum_{j<N}|Y_j-\mu_j|^2\ll NHXL(X),
\]

the same conclusion holds.

At a failed centre,

\[
T_j(H)=O(X(\log X)^2),
\]

so if `nu_j asymp H log X` and

\[
\sum_{j<N}|T_j-\nu_j|^2
\ll NHX(\log X)^2L(X),
\]

then every centre again succeeds.

## Corrected source identity

With

\[
A_H(\theta)=\sum_{m\le H}\Lambda(m)e(-m\theta),
\quad
B_X(\theta)=\sum_n\Lambda(n)e(n\theta),
\]

on the finite source intervals,

\[
T_j(H)=\int_0^1A_H(\theta)B_X(\theta)e(-P_j\theta)\,d\theta.
\]

The first exact path kernel in the block second moment is therefore

\[
F_X(\beta-\alpha)=\sum_{j<N}e((\beta-\alpha)P_j),
\]

the single-walk polynomial. The old pair-sum frame does not contain the offset-prime source factor and is no longer claimed to be the principal Fortune boundary.

## Review and release consequence

The existing Paper II PDF/DOCX remain provenance copies of the first circulation edition. The exact reciprocal-frame identities and obstruction theorems remain valid internally. Sections 1--2, the source-to-frame status, the theorem boundary, abstract and conclusion require a corrected edition and fresh hostile review before further release or Zenodo publication.

Authoritative programme record:

`frontier/integer_mainterm_correction/MAINTERM_CORRECTION_AND_PROGRAMME_STATUS_20260727.md`
