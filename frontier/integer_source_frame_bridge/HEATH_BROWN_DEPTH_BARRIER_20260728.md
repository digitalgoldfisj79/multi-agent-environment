# Heath--Brown depth barrier at the primorial short-window scale

Date: 28 July 2026  
Status: exact parameter obstruction for standard bounded-depth decompositions.

## 1. Scale

Across the dyadic primorial block,

\[
\log P_j\asymp X,
\qquad
H=\eta X^2,
\qquad
\log H=2\log X+O(1),
\qquad
N\asymp\frac{X}{\log X}.
\]

The output variable `n=P_j+m` has size `P_j`, while the physical offset window
has length only `H`.

## 2. Standard Heath--Brown identity

For an integer `K>=1`, the standard identity on `n<=Z` has the form

\[
\Lambda(n)=
\sum_{r=1}^{K}(-1)^{r-1}\binom Kr
\left(\mu_{\le Z^{1/K}}^{*r}*1^{*(r-1)}*\log\right)(n).
\tag{2.1}
\]

More generally, if one prescribes a Möbius cutoff `U`, the same combinatorial
identity is exact on the range `n<=U^K`.  Thus an exact use at `n=P_j+m`
requires

\[
U^K\ge P_j+H.
\tag{2.2}
\]

## 3. Polynomial-cutoff depth

To keep every Möbius-supported variable within the physical/sieve scale, take
`U<=H^A` for a fixed `A>0`.  Then (2.2) forces

\[
K\ge\frac{\log(P_j+H)}{A\log H}.
\tag{3.1}
\]

Since `log P_j asymp X`,

\[
\boxed{
K\gg_A\frac{X}{\log X}.
}
\tag{3.2}
\]

For the natural cutoff `U=H`,

\[
\boxed{
K\ge
\left\lceil\frac{\log(P_j+H)}{\log H}\right\rceil
 =\left(\frac12+o(1)\right)\frac{X}{\log X}.
}
\tag{3.3}
\]

This is of the same order as the number `N` of primorial-prefix centres.

### Theorem 3.1 (bounded-depth exclusion)

No fixed-depth Heath--Brown identity can simultaneously be exact at the output
scale `P_j` and keep all Möbius-supported variables below any fixed polynomial
power of `H`.

### Proof

For fixed `K` and `A`, the right side of (2.2) with `U=H^A` has logarithm

\[
AK\log H=O_{A,K}(\log X),
\]

whereas `log(P_j+H) asymp X`.  The inequality fails for large `X`.  Equivalently,
(3.1) diverges.  \(\square\)

## 4. Fixed-depth cutoff size

Conversely, for fixed `K`, exactness requires

\[
U\ge(P_j+H)^{1/K}
 =\exp(\!\left((1+o(1))X/K\right)).
\tag{4.1}
\]

Hence

\[
\frac{U}{H}\to\infty
\]

faster than every power of `X`.  Divisor variables at this scale exceed the
short offset interval.  Congruence classes in `m` then contain at most one point
rather than a long progression, so the usual Type I averaging over the physical
variable is unavailable.

## 5. Why current bilinear/trilinear estimates do not plug in

The 2026 Kloosterman-fraction theorems apply to a bounded number of convolution
variables with fixed divisor-function complexity.  Taking

\[
K\asymp X/\log X
\]

in (2.1) produces:

1. up to `2K` convolution variables;
2. binomial coefficients of size `2^{K+o(K)}`;
3. coefficient sequences controlled by divisor functions of growing order;
4. no uniform fixed-order Siegel--Walfisz input;
5. a combinatorial loss vastly exceeding the required logarithmic saving.

Thus the standard all-small-variable Heath--Brown route reaches a theorem-level
method obstruction before any Kloosterman estimate is applied.

## 6. Vaughan/divisor-switching alternative

Vaughan's identity does not require all variables to be below `H`.  It leaves
Type II pieces in which two or more factors may be much larger than `H`.  For
`n=P_j+m`, a divisor `d>H` selects at most one `m` in the interval.  This permits
exact divisor switching, but removes the long variable over which classical
bilinear cancellation is normally obtained.

A viable alternative must prove a new lemma of the following kind:

> Average the one-point large-divisor contributions over the primorial index
> before absolute values, and convert the multiplicative walk `P_j mod d` into
> enough cancellation to recover the factor `X/log X`.

No such lemma follows from the standard Vaughan identity alone.

## 7. Boundary

Proved:

1. polynomial divisor cutoffs force depth `K asymp X/log X`;
2. fixed depth forces exponentially large divisor variables;
3. standard fixed-complexity bilinear/trilinear theorems cannot be applied by a
   direct Heath--Brown substitution.

Not proved:

1. impossibility of every signed decomposition;
2. failure of a primorial-index divisor-switching theorem;
3. the required four-prime covariance estimate.

The next genuinely new mathematical target is the primorial-index
large-divisor switching lemma, not a routine increase in Heath--Brown depth.