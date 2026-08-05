# O4 — connected-cumulant compression

Let `J` be uniform on the registered rows and define the probability generating function

\[
G_X(s)=\mathbb E[s^{Z_J}]
=\frac1N\sum_{j<N}s^{Z_j}.
\]

Then

\[
\mathrm{INT\!-\!AOD}
\iff
N G_X(e^{-\tau_X})<1.
\]

## Why connected quantities are the correct next object

Raw factorial moments contain large disconnected contributions. For a Poisson variable all factorial cumulants beyond the first vanish, even though every factorial moment is large. A connected expansion can therefore compress the all-orders detector if the arithmetic correlations are close to a locally biased Poisson law.

Write formally

\[
\log G_X(1+t)
=\sum_{k\ge1}\kappa_k\frac{t^k}{k!},
\]

where `kappa_k` are the factorial cumulants of the row distribution. Substituting `t=-q_X` suggests

\[
-\log G_X(1-q_X)
=q_X\kappa_1-
\sum_{k\ge2}\kappa_k\frac{(-q_X)^k}{k!}.
\]

A formal power series is not sufficient. The programme must establish one of:

1. a zero-free disk containing the segment from `1` to `1-q_X`;
2. an absolutely convergent cluster expansion at `q_X`;
3. a direct finite connected identity with a rigorously bounded remainder;
4. a real-variable integral representation yielding the same bound without complex analyticity.

## Candidate successor theorem

> **INT-CCB — connected-cumulant bound.** There exists a justified connected expansion at `q_X` such that
> \[
> q_X\kappa_1-
> \sum_{k\ge2}\frac{q_X^k}{k!}|\kappa_k|
> >(1+\varepsilon)\log N.
> \]

Then

\[
G_X(1-q_X)<N^{-1-\varepsilon}
\]

and hence `INT-AOD`.

A more flexible admissible version may replace the absolute sum by a signed connected remainder, but the sign control must be proved rather than assumed.

## Scale advantage

Conditionally, the first cumulant satisfies

\[
\kappa_1=\mathbb E[Z_J]\asymp X,
\]

whereas the required logarithmic gap is only `Theta(log X)`. Thus the connected remainder may be a large fraction of the first-order mass and still suffice. The programme should exploit this slack explicitly.

## Execution tasks

1. compute exact finite-panel factorial cumulants using integer/rational arithmetic;
2. test the zero set of empirical generating polynomials;
3. compare raw moment growth with connected cumulant growth;
4. derive symbolic partition formulas for the arithmetic coefficients;
5. attempt a Kotecky–Preiss, dependency-graph, or direct connected-majorant criterion;
6. stop immediately if the connected norm is provably at least the first-order mass at all admissible parameters.
