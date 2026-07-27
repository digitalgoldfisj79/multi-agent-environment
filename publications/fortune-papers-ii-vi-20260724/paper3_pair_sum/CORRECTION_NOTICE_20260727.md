# Paper III correction notice

Date: 27 July 2026  
Status: **Sections 9--10 and Appendices B--C of the first circulation edition are superseded**.

## Unaffected results

The unconditional kernel theory remains intact:

- bounded-coefficient rigidity;
- exact difference-multiplicity dichotomy;
- exact two-scale energy decomposition;
- high-moment and sub-Weibull Lebesgue bounds;
- exact higher moments;
- the reciprocal exceptional-set transfer gap.

The exact implication that the pair-sum target forces the smaller single-walk energy also remains valid as a theorem inside the reciprocal model.

## Withdrawn arithmetic calibration

The first circulation edition assumed

\[
\sum_{j<N}\Psi_j(H)=NH+O(NH\varepsilon).
\]

Candidate collapse shows that below the square threshold the direct source is instead

\[
Z_j(H)=\sum_{m\le H}{\bf1}_{\mathbb P}(m){\bf1}_{\mathbb P}(P_j+m),
\]

with conjectural mean

\[
\lambda_j(H)=\mathfrak S(P_j)
\int_{\ell_j}^{H}\frac{dt}{\log t\log(P_j+t)}\asymp X.
\]

The old `(H1)` is therefore withdrawn as the conjecturally correct first moment. The old two-output correlation `(H2)` is also insufficient because the corrected second moment has four primality conditions.

## Corrected covariance structure

Exactly,

\[
Z_j(H)^2=Z_j(H)+2\sum_{1\le d<H}C_j(H;d),
\]

where

\[
C_j(H;d)=
\sum_{\substack{m,m+d\le H}}
{f1}_{\mathbb P}(m){\bf1}_{\mathbb P}(m+d)
{f1}_{\mathbb P}(P_j+m){\bf1}_{\mathbb P}(P_j+m+d).
\]

Thus the corrected arithmetic input is an aggregated four-linear-form prime correlation, or an equivalent signed two-prime transference theorem. Uniform asymptotics for each displacement are stronger than necessary; only the weighted aggregate appearing in the variance expansion is load-bearing.

A sufficient corrected pair of conditional estimates is

\[
\sum_{j<N}\lambda_jZ_j
=\sum_{j<N}\lambda_j^2+O(NXL(X)),
\]

and

\[
\sum_{j<N}Z_j^2
=\sum_{j<N}(\lambda_j^2+\lambda_j)+O(NXL(X)).
\]

They imply

\[
\sum_{j<N}|Z_j-\lambda_j|^2\ll NXL(X),
\]

which proves every centre when `L(X)=o(log X)`.

## Programme consequence

The next task is not another pair-sum moment or derandomisation theorem. It is an exact signed decomposition of the corrected two-prime source. The single-walk Fourier kernel arises before the pair-sum kernel. Work on the latter is deferred until a source bridge proves that it is load-bearing.

The original arithmetic sections are retained only for provenance and must not be cited as the corrected Hardy--Littlewood boundary.
