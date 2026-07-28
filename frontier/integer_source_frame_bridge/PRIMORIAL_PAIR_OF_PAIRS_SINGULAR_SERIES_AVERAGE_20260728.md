# Primorial pair-of-pairs singular-series average

Date: 28 July 2026  
Status: arithmetic principal-series theorem proved; actual four-prime correlation error open.

## 1. Role in the source-energy problem

For the double-von-Mangoldt source

\[
T_j(H)=\sum_{2\le m\le H}\Lambda(m)\Lambda(P_j+m),
\]

the natural first moment is

\[
\nu_j=\mathfrak S_2(P_j)H,
\]

where `mathfrak S_2(P)` is the prime-pair singular series for the shifts
`{0,P}`.  The off-diagonal part of `T_j(H)^2`, after writing `h=n-m`,
involves the four shifts

\[
\{0,P,h,P+h\}.
\]

This note proves that their Hardy--Littlewood singular-series main terms average
to `mathfrak S_2(P)^2` with more than enough uniformity.  It does not prove the
corresponding four-prime asymptotic.

Let `P=y#` be a primorial centre, where

\[
X/2<y<2X,
\]

as occurs uniformly across a dyadic primorial block.  Put `H=eta X^2` and assume
`0<|h|<H<P`.

## 2. Local factors

Let

\[
\mathfrak S_2(P)
 =\prod_p\frac{1-\nu_p(0,P)/p}{(1-1/p)^2}
\tag{2.1}
\]

and, for nonzero `h`,

\[
\mathfrak S_4(P,h)
 =\prod_p\frac{1-\nu_p(0,P,h,P+h)/p}{(1-1/p)^4}.
\tag{2.2}
\]

Define

\[
\mathcal R_P(h)
 =\frac{\mathfrak S_4(P,h)}{\mathfrak S_2(P)^2}.
\tag{2.3}
\]

For `h != 0` this Euler product converges: outside the prime divisors of
`h(P-h)(P+h)` its factors are `1+O(p^{-2})`.

### Lemma 2.1 (primes dividing the primorial)

If `p|P`, then

\[
r_p(h)=
\begin{cases}
\dfrac{p}{p-1},&p\mid h,\\[4pt]
\dfrac{p(p-2)}{(p-1)^2},&p\nmid h.
\end{cases}
\tag{2.4}
\]

For `p=2`, this is `2` for even `h` and `0` for odd `h`.  For every
`p|P`,

\[
\frac1p\sum_{h\bmod p}r_p(h)=1.
\tag{2.5}
\]

For odd `p|P`,

\[
r_p(h)
 =\frac{p(p-2)}{(p-1)^2}
  \left(1+\frac{\mathbf1_{p\mid h}}{p-2}\right).
\tag{2.6}
\]

### Lemma 2.2 (primes beyond the primorial)

If `p\nmid P` and `p>2`, then

\[
r_p(h)=
\begin{cases}
\dfrac{p}{p-2},&h\equiv0\pmod p,\\[5pt]
\dfrac{p(p-3)}{(p-2)^2},&h\equiv P\text{ or }-P\pmod p,\\[5pt]
\dfrac{p(p-4)}{(p-2)^2},&h\not\equiv0,\pm P\pmod p.
\end{cases}
\tag{2.7}
\]

The three exceptional classes are distinct and

\[
\frac1p\sum_{h\bmod p}r_p(h)=1.
\tag{2.8}
\]

Writing

\[
b_p=\frac{p(p-4)}{(p-2)^2},
\]

one has

\[
r_p(h)=b_p\left(
1+\frac{2\mathbf1_{h\equiv0}}{p-4}
 +\frac{\mathbf1_{h\equiv P}+\mathbf1_{h\equiv-P}}{p-4}
\right).
\tag{2.9}
\]

### Proof

If `p|P`, the pair shifts occupy one class; the four shifts occupy one class
when `p|h` and two otherwise.  If `p\nmid P`, the pair shifts occupy two
classes; the four shifts occupy two classes for `h=0`, three for `h=\pm P`, and
four otherwise.  Substitution in (2.1)--(2.3) gives (2.4) and (2.7).

For (2.8), the numerator of the local average is

\[
(1-2/p)+2(1-3/p)+(p-3)(1-4/p)
 =p(1-2/p)^2.
\]

Equations (2.5), (2.6), and (2.9) follow directly.  \(\square\)

## 3. Triangular average

Let

\[
w_H(h)=H-|h|,
\qquad 0<|h|<H.
\]

Uniformly for every modulus `d` and residue `r`,

\[
\sum_{0<|h|<H\atop h\equiv r\pmod d}w_H(h)
 =\frac{H^2}{d}+O(H).
\tag{3.1}
\]

The exclusion of `h=0` changes the sum by at most `H`.

### Theorem 3.1 (primorial pair-of-pairs average)

Uniformly for `P=y#` with `X/2<y<2X`,

\[
\boxed{
\sum_{0<|h|<H}w_H(h)\,\mathfrak S_4(P,h)
 =H^2\mathfrak S_2(P)^2
  \left(1+O\!\left(\frac{\log X}{H}\right)\right).
}
\tag{3.2}
\]

The implied constant depends only on `eta`.

### Proof

Split (2.3) into three prime ranges.

#### (i) `p<=y`

Every such prime divides `P`.  By (2.6), apart from the bounded parity factor,
the product is a constant times

\[
\prod_{3\le p\le y\atop p\mid h}
 \left(1+\frac1{p-2}\right).
\]

Expand over squarefree divisors of the odd primorial.  The absolute coefficient
sum is

\[
\prod_{3\le p\le y}\left(1+\frac1{p-2}\right)
 \ll\log y\ll\log X
\tag{3.3}
\]

by Mertens' theorem.  Apply (3.1) to each divisibility class.  The exact local
means give main term `H^2`; the total boundary error is `O(H log X)`.

#### (ii) `y<p<=H`

All these primes are coprime to `P`, so (2.9) applies.  Expanding the three
possible residue indicators at each selected prime gives absolute coefficient
sum

\[
\prod_{y<p\le H}\left(1+\frac4{p-4}\right)=O(1),
\tag{3.4}
\]

because `y asymp X`, `H asymp X^2`, and

\[
\sum_{y<p\le H}\frac1p=O(1).
\]

Equation (3.1) and the local mean-one identities give main term `H^2` and error
`O(H)`.

#### (iii) `p>H`

Since `0<|h|<H`, the class `h\equiv0 (mod p)` is impossible.  The generic
factors contribute

\[
1+O\!\left(\sum_{p>H}p^{-2}\right)
 =1+O((H\log H)^{-1}).
\]

An exceptional factor can occur only if `p|P-h` or `p|P+h`, and changes the
product by `1+O(1/p)`.  Pointwise,

\[
\sum_{p>H\atop p\mid(P-h)(P+h)}\frac1p
 \ll\frac{\log(P+H)}{H\log H}
 \ll\frac1{X\log X},
\]

so the product may be linearised.  For the weighted average, each `p>H`
selects at most two values of `h` for each sign.  Hence

\[
\frac1{H^2}\sum_{0<|h|<H}w_H(h)
 \sum_{p>H\atop p\mid(P-h)(P+h)}\frac1p
 \ll\frac1H\sum_{H<p\le P+H}\frac1p
 \ll\frac{\log X}{H}.
\tag{3.5}
\]

Combining the three ranges proves (3.2).  \(\square\)

## 4. Consequence for the double-source principal term

Uniformly across the block,

\[
\mathfrak S_2(P)\asymp\log X.
\]

Therefore Theorem 3.1 gives

\[
\sum_{0<|h|<H}w_H(h)\mathfrak S_4(P,h)
 =H^2\mathfrak S_2(P)^2
 +O(H(\log X)^3).
\tag{4.1}
\]

Thus the off-diagonal Hardy--Littlewood principal term cancels

\[
\nu_j^2=H^2\mathfrak S_2(P_j)^2
\]

with error `O(H (log X)^3)` per centre.  Across the block this contributes

\[
NH(\log X)^3,
\]

which is negligible relative to the double-source variance allowance

\[
NHX(\log X)^2L(X)
\]

for any bounded positive `L(X)`, and therefore certainly for the intended
sublogarithmic loss.

The singular-series principal covariance is not the remaining wall.

## 5. Remaining theorem

The unresolved term is the actual averaged four-prime correlation error

\[
\Lambda(m)\Lambda(P_j+m)\Lambda(m+h)\Lambda(P_j+m+h)
 -\mathfrak S_4(P_j,h),
\]

summed over `j`, `h`, and `m` at total scale

\[
NHX(\log X)^2o(\log X).
\]

The theorem above removes the deterministic singular-series covariance before
that error is attacked.

## 6. Boundary

Proved:

1. exact local mean-one identities at every prime;
2. a uniform triangular average with relative error `O(log X/H)`;
3. negligible principal-series error at the Fortune variance scale.

Not proved:

1. the Hardy--Littlewood four-prime asymptotic;
2. the required aggregate correlation-error bound;
3. Fortune's conjecture.