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
`{0,P}`.

The off-diagonal part of `T_j(H)^2` is organised by `h=n-m` and involves the
four shifts

\[
\{0,P,h,P+h\}.
\]

This note proves that their Hardy--Littlewood singular-series main terms average
to `mathfrak S_2(P)^2` with more than enough uniformity.  It does not prove the
corresponding four-prime asymptotic.

Throughout, `P` is a primorial centre containing every prime at most `X`,
`H=eta X^2`, and `0<|h|<H<P`.

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

Define the normalised ratio

\[
\mathcal R_P(h)
 =\frac{\mathfrak S_4(P,h)}{\mathfrak S_2(P)^2}.
\tag{2.3}
\]

The Euler product converges for `h != 0`: away from the prime divisors of
`h(P-h)(P+h)` its local factors are `1+O(p^{-2})`, and the exceptional set is
finite.

### Lemma 2.1 (local factors at primorial primes)

If `p|P`, then

\[
r_p(h)=
\begin{cases}
\dfrac{p}{p-1},&p\mid h,\\[4pt]
\dfrac{p(p-2)}{(p-1)^2},&p\nmid h.
\end{cases}
\tag{2.4}
\]

For `p=2`, this says `r_2(h)=2` for even `h` and `r_2(h)=0` for odd `h`.
For every prime `p|P`,

\[
\frac1p\sum_{h\bmod p}r_p(h)=1.
\tag{2.5}
\]

For odd `p|P`, one may write

\[
r_p(h)
 =\frac{p(p-2)}{(p-1)^2}
  \left(1+\frac{\mathbf1_{p\mid h}}{p-2}\right).
\tag{2.6}
\]

### Lemma 2.2 (local factors beyond the primorial)

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

The three exceptional residue classes are distinct.  Moreover,

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

### Proof of the local lemmas

For `p|P`, the two pair shifts occupy one residue class.  The four shifts occupy
one class when `p|h` and two otherwise.  Substitution in (2.1)--(2.3) gives
(2.4).  Equation (2.5) is immediate.

For `p\nmid P`, the pair shifts occupy two classes.  The four shifts occupy two
classes when `h=0`, three when `h=\pm P`, and four otherwise.  Substitution gives
(2.7).  The numerator of the average in (2.8) is

\[
(1-2/p)+2(1-3/p)+(p-3)(1-4/p)
 =p(1-2/p)^2,
\]

which proves (2.8).  Equations (2.6) and (2.9) are algebraic rearrangements.
\(\square\)

## 3. Triangular singular-series average

Let

\[
w_H(h)=H-|h|,
\qquad 0<|h|<H.
\]

The elementary residue-class estimate

\[
\sum_{0<|h|<H\atop h\equiv r\pmod d}w_H(h)
 =\frac{H^2}{d}+O(H)
\tag{3.1}
\]

holds uniformly for every modulus `d` and residue `r`; excluding `h=0` changes
the left side by at most `H`.

### Theorem 3.1 (primorial pair-of-pairs average)

Uniformly for primorial centres `P` containing every prime at most `X`,

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

Split the ratio product (2.3) into three ranges.

#### (i) Primes `p<=X`

All such primes divide `P`.  By (2.6), apart from the bounded parity factor, the
product is a constant times

\[
\prod_{3\le p\le X\atop p\mid h}
 \left(1+\frac1{p-2}\right).
\]

Expand over squarefree divisors of the odd primorial.  The sum of the absolute
coefficients is

\[
\prod_{3\le p\le X}\left(1+\frac1{p-2}\right)
 \ll\log X
\tag{3.3}
\]

by Mertens' theorem.  Apply (3.1) to every divisibility class.  Since each local
mean is one, the main term is `H^2`; the total boundary error is
`O(H log X)`.

#### (ii) Primes `X<p<=H`

Use (2.9).  On expanding the three possible residue indicators at each selected
prime, the sum of absolute coefficients is bounded by

\[
\prod_{X<p\le H}\left(1+\frac4{p-4}\right)=O(1),
\tag{3.4}
\]

because `H asymp X^2` and

\[
\sum_{X<p\le X^2}\frac1p=\log2+o(1).
\]

Equation (3.1) and the exact local means again give main term `H^2` and boundary
error `O(H)`.

#### (iii) Primes `p>H`

For nonzero `|h|<H`, the congruence `p|h` is impossible.  The generic factors
contribute

\[
1+O\!\left(\sum_{p>H}p^{-2}\right)
 =1+O((H\log H)^{-1}).
\]

An exceptional factor can occur only when `p|P-h` or `p|P+h`, and its relative
change is `1+O(1/p)`.  Pointwise,

\[
\sum_{p>H\atop p\mid(P-h)(P+h)}\frac1p
 \ll\frac{\log(P+H)}{H\log H}
 \ll\frac1{X\log X},
\]

so products may be linearised.  Averaging more sharply, each prime `p>H`
selects at most two admissible values of `h` for each sign, and therefore

\[
\frac1{H^2}\sum_{0<|h|<H}w_H(h)
 \sum_{p>H\atop p\mid(P-h)(P+h)}\frac1p
 \ll\frac1H\sum_{H<p\le P+H}\frac1p
 \ll\frac{\log X}{H}.
\tag{3.5}
\]

This is the tail error.

Combining the three ranges proves

\[
\frac1{H^2}\sum_{0<|h|<H}w_H(h)\mathcal R_P(h)
 =1+O(\log X/H),
\]

which is (3.2).  \(\square\)

## 4. Consequence for the double-source principal term

Since

\[
\mathfrak S_2(P)\asymp\log X,
\]

Theorem 3.1 gives

\[
\sum_{0<|h|<H}w_H(h)\mathfrak S_4(P,h)
 =H^2\mathfrak S_2(P)^2
 +O(H(\log X)^3).
\tag{4.1}
\]

Thus the off-diagonal Hardy--Littlewood principal term cancels the baseline
square

\[
\nu_j^2=H^2\mathfrak S_2(P_j)^2
\]

with an error `O(H (log X)^3)` per centre.

The all-centres variance allowance for the double source is

\[
NHX(\log X)^2L(X).
\]

The aggregate principal-series error

\[
NH(\log X)^3
\]

is smaller by the factor `log X/(X L(X))`; in particular it is negligible even
for bounded positive `L(X)`.

Therefore the singular-series main term is not the remaining wall.

## 5. Remaining theorem

What remains is a genuine averaged four-prime correlation error estimate for

\[
\Lambda(m)\Lambda(P_j+m)\Lambda(m+h)\Lambda(P_j+m+h)
 -\mathfrak S_4(P_j,h),
\]

summed over `j`, `h`, and `m` at the total scale

\[
NHX(\log X)^2o(\log X).
\]

The theorem above removes the deterministic singular-series covariance before
that error is attacked.

## 6. Boundary

Proved:

1. exact local mean-one identities at every prime;
2. a uniform triangular average with relative error `O(log X/H)`;
3. negligible aggregate principal-series error at the Fortune variance scale.

Not proved:

1. the Hardy--Littlewood four-prime asymptotic;
2. the required aggregate correlation-error bound;
3. Fortune's conjecture.