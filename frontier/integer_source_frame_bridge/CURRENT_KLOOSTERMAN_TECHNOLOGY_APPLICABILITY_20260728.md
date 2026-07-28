# Applicability of current Kloosterman-fraction technology

Date: 28 July 2026  
Status: parameter and structural audit; no new external theorem claimed.

## 1. Remaining arithmetic object

After the complete-modulus lower frame and the pair-of-pairs singular-series
average, the unresolved object is the signed aggregate correlation error

\[
\sum_{j<N}\sum_{0<|h|<H}\sum_m
\left[
\prod_{t\in\{0,P_j,h,P_j+h\}}\Lambda(m+t)
 -\mathfrak S_4(P_j,h)
\right],
\]

with the obvious interpretation of the four factors, `H asymp X^2`, and
`log P_j asymp X`.

Equivalently, a Heath--Brown decomposition of `Lambda(P_j+m)` produces divisor
variables whose product is of size `P_j`, but they are coupled to the short
offset by the affine equation

\[
uv\cdots-m=P_j.
\]

## 2. Wright's partially fixed-modulus theorem

Thomas Wright, arXiv:2604.25177, proves distribution estimates for convolutions

\[
\sum_{mn\equiv a\pmod q}\alpha_m\beta_n
\]

with fixed residue `a`, one coefficient sequence satisfying a Siegel--Walfisz
condition, and moduli in specified ranges around the square-root barrier of the
convolution length.  The work is driven by improved trilinear Kloosterman
fraction estimates with a partially fixed denominator.

This does not directly match the Fortune source:

1. after decomposing `Lambda(P_j+m)`, the residue is `P_j+m`, not fixed while
   `m` is summed;
2. the short offset itself carries a prime or von Mangoldt weight in the
   symmetric source;
3. the required result is a signed four-factor covariance, not a first-order
   distribution estimate for one convolution;
4. no available input supplies Siegel--Walfisz control for the already centred
   prime-pair residual at length `H=(log P_j)^2`.

Wright's theorem may become relevant after an additional dispersion and
Cauchy--Schwarz step creates a genuine fixed-residue trilinear form.  Such a
reduction has not been proved.

## 3. Dong--Robles--Zeindler bilinear fractions

Anji Dong, Nicolas Robles, and Dirk Zeindler, arXiv:2601.00292, prove improved
bounds for bilinear forms of the shape

\[
\sum_{m,n}\alpha_m\beta_n
 e\!\left(\frac{a\overline m}{bn}\right)
\]

with arbitrary divisor-bounded coefficient sequences.  The power saving over
the trivial bound is useful once a completed dispersion calculation has already
produced this phase.

The current Fortune error has not yet been reduced to that bilinear form.  A
Heath--Brown expansion initially has at least the variables

\[
(j,h,m,d_1,\ldots,d_k),
\]

with the primorial centre entering as an affine difference.  Applying absolute
values early recreates the positive-diagonal loss `X/log X`.  Therefore the
bilinear theorem cannot be inserted before a signed variable-elimination
lemma.

## 4. Precise missing reduction

A viable use of current Kloosterman technology would require a theorem of the
following form.

After subtracting the four-form singular series and applying a bounded-depth
Heath--Brown identity, decompose the complete aggregate error into finitely many
forms

\[
\mathcal B_\sigma
 =\sum_{r,s}\alpha_r\beta_s
  e\!\left(\frac{A_\sigma\overline r}{B_\sigma s}\right)
\]

plus acceptable errors, such that:

1. the coefficient norms remain at the random covariance scale;
2. one sequence satisfies the required small-modulus equidistribution;
3. the parameter ranges meet an existing bilinear or trilinear theorem;
4. the sum over primorial indices is retained before absolute values;
5. the total saving is at least `X/log X` over the positive sieve bound.

No such signed reduction is currently known in the programme.

## 5. Ruling

The 2026 Kloosterman-fraction improvements are potentially relevant technology,
but they do not close the source theorem by direct substitution.  The next
load-bearing lemma is not a stronger black-box exponential-sum estimate.  It is
a signed Heath--Brown/dispersion reduction that places the primorial four-prime
covariance inside the hypotheses of one of those estimates without paying the
positive-diagonal loss.

The programme should therefore attack the reduction first.  If that reduction
necessarily loses `X/log X`, Route B reaches a theorem-level obstruction under
current methods.