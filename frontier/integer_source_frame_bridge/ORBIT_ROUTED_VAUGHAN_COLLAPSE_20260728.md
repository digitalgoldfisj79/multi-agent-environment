# Orbit-routed Vaughan collapse

Date: 28 July 2026  
Status: exact fixed-complexity decomposition proved; signed trilinear dispersion estimate open.

## 1. Exact identity

For cutoffs `U,V>=1`, write

\[
\mu_{\le U}(n)=\mu(n)\mathbf1_{n\le U},
\qquad
\mu_{>U}=\mu-\mu_{\le U},
\]

and similarly

\[
\Lambda_{\le V}(n)=\Lambda(n)\mathbf1_{n\le V},
\qquad
\Lambda_{>V}=\Lambda-\Lambda_{\le V}.
\]

### Theorem 1.1 (exact Vaughan identity)

For every positive integer `n`,

\[
\boxed{
\Lambda
=
\mu_{\le U}*\log
-\mu_{\le U}*1*\Lambda_{\le V}
+\Lambda_{\le V}
+\mu_{>U}*1*\Lambda_{>V}.
}
\tag{1.1}
\]

### Proof

Start from `Lambda=mu*log` and `log=1*Lambda`.  Then

\[
\begin{aligned}
\Lambda
&=\mu_{\le U}*\log+\mu_{>U}*1*\Lambda\\
&=\mu_{\le U}*\log
 +\mu_{>U}*1*\Lambda_{\le V}
 +\mu_{>U}*1*\Lambda_{>V}.
\end{aligned}
\]

Since

\[
\mu_{>U}*1
=(\mu-\mu_{\le U})*1
=\varepsilon-\mu_{\le U}*1,
\]

one has

\[
\mu_{>U}*1*\Lambda_{\le V}
=
\Lambda_{\le V}
-\mu_{\le U}*1*\Lambda_{\le V}.
\]

Substitution gives (1.1).  \(\square\)

Unlike the bounded-small-variable Heath--Brown identity, (1.1) is exact for every
choice of `U,V`; no condition such as `U^K>=n` occurs.

## 2. Primorial-adapted cutoffs

Let `P_0` be the first primorial centre in the dyadic block and put

\[
Y=\lfloor P_0^{1/3}\rfloor,
\qquad
U=V=Y.
\tag{2.1}
\]

Since

\[
\log P_0\asymp X,
\qquad
H=\eta X^2,
\]

one has, for sufficiently large `X`,

\[
Y>H.
\tag{2.2}
\]

For every shifted output

\[
n=P_j+m,
\qquad 2\le m\le H,
\]

one also has `n>Y`, so the term `Lambda_{<=Y}(n)` vanishes.

Equation (1.1) becomes

\[
\boxed{
\begin{aligned}
\Lambda(n)
={}&
\sum_{\substack{de=n\\d\le Y}}
\mu(d)\log e\\
&-
\sum_{\substack{dbc=n\\d\le Y,\ c\le Y}}
\mu(d)\Lambda(c)\\
&+
\sum_{\substack{abc=n\\a>Y,\ c>Y}}
\mu(a)\Lambda(c).
\end{aligned}
}
\tag{2.3}
\]

All sums are finite and signed.

## 3. Every term has a canonical factor above the physical scale

### Proposition 3.1 (Type I complement)

In the first sum of (2.3),

\[
e=\frac nd
\ge\frac{P_0}{Y}
\ge P_0^{2/3}.
\tag{3.1}
\]

Thus `e>H`, and the pair `(j,e)` selects at most one physical offset.

### Proposition 3.2 (subtraction term)

In the second sum,

\[
b=\frac n{dc}
\ge\frac{P_0}{Y^2}
\ge P_0^{1/3}+O(1).
\tag{3.2}
\]

Thus `b>H`.  Moreover `d,c<=Y`, so `b` is at least the cutoff scale of the other
two variables.  Route the term canonically to `b`, with a fixed tie-breaking rule
at the finite boundary.

### Proposition 3.3 (large-large term)

In the third sum, both

\[
a>Y>H,
\qquad
c>Y>H.
\]

Route the term to

\[
D=\max(a,b,c),
\]

using a fixed lexicographic tie-breaking rule.  Since `abc=n`,

\[
D\ge n^{1/3}\ge P_0^{1/3}>H.
\tag{3.3}
\]

Hence every component of the exact Vaughan decomposition has a canonical routed
factor `D>H`.

## 4. One-point orbit form

For a routed factor `D>H`, define

\[
E_j(D)=\left\lceil\frac{P_j}{D}\right\rceil,
\qquad
m_j(D)=DE_j(D)-P_j.
\]

The divisibility condition `D|P_j+m` with `2<=m<=H` is exactly

\[
2\le m_j(D)\le H,
\]

and then the offset is unique.

Accordingly, every Type I, subtraction, and large-large term in (2.3) can be
written as a finite sum over routed columns `D`, each evaluated at the unique orbit
point `m_j(D)` and carrying only one or two quotient-factor sums.

No term contains a growing number of convolution variables.

## 5. Uniform centre multiplicity

The routed factors satisfy:

- Type I: `D=e>=P_0^{2/3}` and the product has two factors;
- subtraction term: `D=b>=P_0^{1/3}` and the product has three factors;
- large-large term: `D>=P_0^{1/3}` and the product has three factors.

The shrinking-target theorem therefore gives:

### Theorem 5.1 (fixed-complexity column sparsity)

For every routed numerical factor `D`, the prime-candidate support

\[
\{j:X<m_j(D)\le H\}
\]

has cardinality `O(1)`, uniformly in `D` and `X`.

More precisely:

1. Type I columns have the `R=2` multiplicity bound;
2. subtraction and large-large columns have the `R=3` multiplicity bound.

The asymptotic bounds are eventually at most three and four, respectively; the
exact finite bound is the shrinking-target formula with the actual value of `D`.

## 6. Consequence for the former depth obstruction

The previous fixed-depth objection combined two statements:

1. a bounded-small-variable Heath--Brown identity requires depth
   `K asymp X/log X`;
2. fixed depth leaves exponentially large factors with no useful physical
   progression.

The first statement remains true for that particular identity.  The second is now
replaced by a positive theorem:

> exponentially large factors are one-point in the physical variable but
> bounded-multiplicity in the primorial index.

Vaughan's exact identity (1.1) requires at most three factors.  Thus neither growing
depth nor growing divisor-function complexity is intrinsic to the shifted source.

## 7. New fixed-complexity analytic object

After multiplying (2.3) by the offset weight `Lambda(m)` for the symmetric source,
summing over `m`, and routing each term to `D`, the unresolved covariance is a
finite linear combination of forms with variables of the schematic types

\[
(j,D,d),
\qquad
(j,D,d,c),
\qquad
(j,D,a,c),
\]

subject to the exact one-point relation

\[
P_j+m_j(D)=D E_j(D).
\]

At fixed `D`, only `O(1)` primorial indices occur.  The quotient variables remain
fixed-complexity and retain their Möbius and von Mangoldt signs.

This is the correct input for a dispersion/completion step.  A successful reduction
should transform the quotient correlations into bilinear or trilinear reciprocal
phases while keeping the primorial-index sum inside the signed form.

## 8. Relation to current Kloosterman-fraction technology

The earlier applicability audit rejected direct substitution because a growing-
depth Heath--Brown expansion produced

\[
(j,h,m,d_1,\ldots,d_K),
\qquad K\asymp X/\log X.
\]

That parameter obstruction is removed.  The remaining mismatch is narrower:

1. derive the signed dispersion/completion from (2.3);
2. verify the coefficient norms after largest-factor routing;
3. place the resulting fixed two- or three-variable reciprocal form inside an
   existing bilinear or trilinear theorem;
4. retain enough saving to reach `o(log X)` in the Fortune variance bound.

No claim is made here that an existing theorem automatically supplies those four
steps.

## 9. Boundary

Proved:

1. exact Vaughan identity at arbitrary cutoffs;
2. exact primorial-adapted decomposition (2.3);
3. every term has a canonical factor `D>H`;
4. every routed column has uniformly bounded centre multiplicity;
5. convolution complexity is fixed at at most three factors;
6. the growing-depth obstruction is representation-dependent and does not apply
   to (2.3).

Open:

1. the signed dispersion/completion of the routed forms;
2. the coefficient norm estimates required by current reciprocal-fraction
   theorems;
3. the centred source-energy bound;
4. Fortune's conjecture.
