# Three-orbit-column source identity

Date: 28 July 2026  
Status: exact signed source identity proved; reciprocal completion estimates open.

## 1. Input

Use the primorial-adapted Vaughan cutoff

\[
Y=\lfloor P_0^{1/3}\rfloor>H
\]

and the exact decomposition

\[
\begin{aligned}
\Lambda(n)
={}&
\sum_{de=n,\ d\le Y}\mu(d)\log e\\
&-
\sum_{dbc=n,\ d,c\le Y}\mu(d)\Lambda(c)\\
&+
\sum_{abc=n,\ a>Y,\ c>Y}\mu(a)\Lambda(c)
\end{aligned}
\tag{1.1}
\]

for shifted outputs `n=P_j+m`.

For every integer `D>H`, define

\[
q_j(D)=\left\lceil\frac{P_j}{D}\right\rceil,
\qquad
m_j(D)=Dq_j(D)-P_j.
\tag{1.2}
\]

Then `D|P_j+m` for an offset `2<=m<=H` if and only if

\[
2\le m_j(D)\le H,
\]

and the quotient is uniquely `q_j(D)`.

Define the fixed cutoff convolutions

\[
A_Y(q)
=
\sum_{\substack{dc=q\\d\le Y,\ c\le Y}}
\mu(d)\Lambda(c),
\tag{1.3}
\]

and

\[
B_Y(q)
=
\sum_{\substack{bc=q\\c>Y}}
\Lambda(c)
=
\sum_{\substack{c\mid q\\c>Y}}\Lambda(c).
\tag{1.4}
\]

## 2. Exact Type I column

### Proposition 2.1

The first term of (1.1), summed over `2<=m<=H`, is

\[
\boxed{
\mathcal I_j
=
\sum_{D>H}
\mathbf1_{\substack{2\le m_j(D)\le H\\q_j(D)\le Y}}
\mu\bigl(q_j(D)\bigr)\log D.
}
\tag{2.1}
\]

### Proof

In the first term write `D=e`.  Since `d<=Y`,

\[
D=e=n/d\ge P_0/Y>H.
\]

For fixed `(j,D)`, the one-point relation (1.2) forces

\[
d=q_j(D),
\qquad
m=m_j(D).
\]

This is a bijection between the original triples `(m,d,e)` and the terms in
(2.1).  \(\square\)

## 3. Exact subtraction column

### Proposition 3.1

The second term of (1.1), summed over the physical interval, is

\[
\boxed{
\mathcal{II}_j
=-
\sum_{D>H}
\mathbf1_{2\le m_j(D)\le H}
A_Y\bigl(q_j(D)\bigr).
}
\tag{3.1}
\]

The summand is automatically zero unless `q_j(D)<=Y^2`.

### Proof

Write `D=b`.  Since `dc<=Y^2`,

\[
D=b=n/(dc)\ge P_0/Y^2>H.
\]

For fixed `(j,D)`, equation (1.2) forces `dc=q_j(D)` and the sum over all such
factorisations is exactly `A_Y(q_j(D))`.  \(\square\)

## 4. Exact large-large column

### Proposition 4.1

The final term of (1.1), summed over offsets, is

\[
\boxed{
\mathcal{III}_j
=
\sum_{D>Y}
\mathbf1_{2\le m_j(D)\le H}
\mu(D)B_Y\bigl(q_j(D)\bigr).
}
\tag{4.1}
\]

### Proof

Write `D=a`.  The condition `a>Y>H` puts the term in the one-point regime.  For
fixed `(j,D)`, equation (1.2) gives `bc=q_j(D)`.  Summing `Lambda(c)` over the
factorisations with `c>Y` produces `B_Y(q_j(D))`.  \(\square\)

No largest-factor tie-breaking is needed: the Möbius-supported variable `a` is
already above the physical scale.

## 5. Exact source identity

### Theorem 5.1 (three-orbit-column identity)

For every sufficiently large `X`,

\[
\boxed{
\Psi_j(H)
=
\mathcal I_j+\mathcal{II}_j+\mathcal{III}_j.
}
\tag{5.1}
\]

For the symmetric source,

\[
\boxed{
T_j(H)
=
\sum_{2\le m\le H}\Lambda(m)\Lambda(P_j+m)
}
\]

is obtained from (2.1), (3.1), and (4.1) by multiplying each column summand by

\[
\Lambda\bigl(m_j(D)igr).
\tag{5.2}
\]

### Proof

Propositions 2.1, 3.1, and 4.1 are bijective rearrangements of the three terms in
(1.1).  Their signed sum is `Lambda(P_j+m)` for every offset before the offset sum
is taken.  \(\square\)

## 6. Column sparsity

The column ranges satisfy

\[
D\ge P_0/Y>P_0^{2/3}
\]

in Type I and

\[
D\ge P_0/Y^2>P_0^{1/3}+O(1)
\]

in Type II, while Type III has `D>Y`.

Consequently the shrinking-target theorem gives uniform bounded support in the
primorial index:

\[
\#\{j:X<m_j(D)\le H\}=O(1)
\]

for every column in all three transforms.  Type I uses the `R=2` bound; Types II
and III use the `R=3` scale bound.

## 7. Why this form is analytically preferable

The unresolved source no longer contains an unspecified high-depth convolution.
It consists of three explicit coefficient families evaluated on the same orbit
coordinates:

\[
q_j(D)=\left\lceil P_j/D\right\rceil,
\qquad
m_j(D)=-P_j\pmod D.
\]

The interval indicator can be completed in additive characters modulo `D`:

\[
\mathbf1_{2\le m_j(D)\le H}
=
\frac1D
\sum_{r\bmod D}
\left(\sum_{2\le m\le H}e(-rm/D)\right)
e(rP_j/D).
\tag{7.1}
\]

Thus every routed column has an exact reciprocal phase

\[
e(rP_j/D),
\]

with fixed-complexity quotient coefficients

\[
\mu(q)\log D,
\qquad
A_Y(q),
\qquad
\mu(D)B_Y(q).
\]

Equation (7.1) is the direct bridge from the primorial-index collapse to bilinear
or trilinear Kloosterman-fraction technology.

## 8. New analytic boundary

The next step is now sharply specified:

1. insert (7.1) into the centred one-sided or symmetric source;
2. subtract the zero-frequency principal term before squaring;
3. retain the signed combination
   `mathcal I + mathcal{II} + mathcal{III}`;
4. use bounded column multiplicity for the primorial-index variable;
5. estimate the nonzero reciprocal modes with fixed-complexity bilinear/trilinear
   bounds.

The package proves the exact reduction.  It does not yet prove that the coefficient
norms and parameter ranges meet an existing Kloosterman-fraction theorem, nor the
required `o(log X)` source-energy bound.
