# Vaughan quotient-coefficient collapse

Date: 28 July 2026  
Status: exact convolution identity and uniform coefficient bounds proved.

## 1. Full convolution identity

### Theorem 1.1

For every positive integer `q`,

\[
\boxed{
(\mu*\Lambda)(q)
=-\mu(q)\log q.
}
\tag{1.1}
\]

### Proof

The Dirichlet series of the left side is

\[
\frac1{\zeta(s)}\left(-\frac{\zeta'(s)}{\zeta(s)}\right)
=-\frac{\zeta'(s)}{\zeta(s)^2}.
\]

On the other hand,

\[
\left(\frac1{\zeta(s)}\right)'
=-\sum_{q\ge1}\frac{\mu(q)\log q}{q^s}
=-\frac{\zeta'(s)}{\zeta(s)^2}.
\]

Uniqueness of Dirichlet coefficients gives (1.1).  \(\square\)

Equivalently, the full convolution is supported on squarefree integers and has
only logarithmic size.

## 2. Truncated coefficients

Recall

\[
A_Y(q)
=
\sum_{\substack{dc=q\\d\le Y,\ c\le Y}}
\mu(d)\Lambda(c),
\tag{2.1}
\]

\[
B_Y(q)
=
\sum_{\substack{c\mid q\\c>Y}}
\Lambda(c),
\tag{2.2}
\]

and define the large-large Vaughan coefficient

\[
C_Y(q)
=
\sum_{\substack{ac=q\\a>Y,\ c>Y}}
\mu(a)\Lambda(c).
\tag{2.3}
\]

The supports satisfy

\[
A_Y(q)=0\quad(q>Y^2),
\qquad
C_Y(q)=0\quad(q\le Y^2).
\tag{2.4}
\]

## 3. Pointwise logarithmic bounds

### Proposition 3.1

For every `q>=2`,

\[
\boxed{
|A_Y(q)|\le2\log q,
\qquad
|C_Y(q)|\le2\log q,
\qquad
0\le B_Y(q)\le\log q.
}
\tag{3.1}
\]

### Proof

A nonzero `Lambda(c)` forces `c=p^k` for a prime `p`.  In either (2.1) or
(2.3), a nonzero Möbius factor forces the complementary quotient to be
squarefree.  For a fixed prime `p`, at most the exponents

\[
k=v_p(q),
\qquad
k=v_p(q)-1
\]

can occur.  Each contributes in absolute value `log p`.  Hence

\[
|A_Y(q)|,\ |C_Y(q)|
\le
2\sum_{p\mid q}\log p
\le2\log q.
\]

For `B_Y`, all terms are nonnegative, and the complete prime-power divisor sum is

\[
\sum_{p^k\mid q}\log p
=\log q.
\]

Restricting to `p^k>Y` can only decrease it.  \(\square\)

The factor two is a safe truncation bound.  In the untruncated convolution the two
possible powers cancel whenever `q` is nonsquarefree, leaving (1.1).

## 4. Dyadic norm bounds

### Corollary 4.1

For `Q>=2`,

\[
\boxed{
\sum_{Q<q\le2Q}|A_Y(q)|^2
\ll Q(\log Q)^2,
}
\tag{4.1}
\]

and identically for `C_Y`; while

\[
\sum_{Q<q\le2Q}|B_Y(q)|^2
\ll Q(\log Q)^2.
\tag{4.2}
\]

Also

\[
\boxed{
\sum_{q\le Q}\frac{|A_Y(q)|^2}{q}
+
\sum_{q\le Q}\frac{|B_Y(q)|^2}{q}
+
\sum_{q\le Q}\frac{|C_Y(q)|^2}{q}
\ll(\log Q)^3.
}
\tag{4.3}
\]

These follow immediately from (3.1) and comparison with the corresponding
integrals.

## 5. Consequence for reciprocal-fraction technology

The exact three-column source uses coefficient families

\[
\mu(q)\log D,
\qquad
A_Y(q),
\qquad
\mu(D)B_Y(q),
\]

or, in the original Vaughan modulus variables, `A_Y(q)` and `C_Y(q)`.

The quotient coefficients therefore have fixed logarithmic complexity.  They do
not require divisor functions of order growing like `X/log X`, and their dyadic
`L^2` norms are at the standard square-root scale up to one logarithm.

The remaining issue in applying bilinear or trilinear Kloosterman-fraction bounds
is now parameter placement and preservation of the signed primorial-index sum, not
coefficient growth.

## 6. Boundary

Proved:

1. the exact identity `(mu*Lambda)(q)=-mu(q)log q`;
2. uniform pointwise bounds for all three truncated coefficient families;
3. standard dyadic and harmonic `L^2` norm bounds.

Open:

1. the nonzero-mode dispersion estimate;
2. verification that a completed dyadic block falls in an existing theorem's
   parameter range with the required total saving;
3. Fortune's conjecture.
