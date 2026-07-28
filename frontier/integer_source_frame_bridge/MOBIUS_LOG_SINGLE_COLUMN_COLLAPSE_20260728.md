# Möbius--log single-column collapse

Date: 28 July 2026  
Status: exact source, principal-term and nonzero-mode identities proved; signed variance estimate open.

## 1. The minimal divisor identity

### Theorem 1.1

For every integer `n>1`,

\[
\boxed{
\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d.
}
\tag{1.1}
\]

### Proof

Starting from `Lambda=mu*log`,

\[
\Lambda(n)=\sum_{d\mid n}\mu(d)\log(n/d).
\]

Since `n>1`,

\[
\sum_{d\mid n}\mu(d)=0.
\]

Expanding `log(n/d)=log n-log d` gives (1.1).  \(\square\)

This identity is exact, signed and supported only on squarefree divisors through
`mu(d)`.  It eliminates every complementary quotient coefficient from the source.

## 2. Exact weighted shifted source

Let `w_m` be deterministic weights supported on `2<=m<=H`, and put

\[
W_H=\sum_{m=2}^{H}w_m,
\qquad
Z_j=P_j+H.
\]

Define the divisor-incidence column

\[
A_{j,d}(w)=
\sum_{m=2}^{H}w_m\mathbf1_{d\mid P_j+m}.
\tag{2.1}
\]

### Theorem 2.1 (single-column source identity)

One has exactly

\[
\boxed{
\sum_{m=2}^{H}w_m\Lambda(P_j+m)
=-\sum_{d\le Z_j}\mu(d)\log d\,A_{j,d}(w).
}
\tag{2.2}
\]

### Proof

Apply (1.1) to every shifted output and interchange the finite sums.  A divisor of
`P_j+m` is at most `Z_j`.  \(\square\)

For the sharp one-sided detector take `w_m=1`.  For the symmetric detector take
`w_m=Lambda(m)`.

## 3. Exact additive completion

For every modulus `d`, define

\[
\widehat w_d(r)=\sum_{m=2}^{H}w_m e(rm/d),
\qquad r\bmod d.
\tag{3.1}
\]

Additive orthogonality gives

\[
A_{j,d}(w)
=
\frac1d\sum_{r\bmod d}
\widehat w_d(r)e(rP_j/d).
\tag{3.2}
\]

Separating `r=0` yields

\[
A_{j,d}(w)
=
\frac{W_H}{d}
+
\frac1d\sum_{r=1}^{d-1}
\widehat w_d(r)e(rP_j/d).
\tag{3.3}
\]

## 4. Exact principal term

Insert (3.3) into (2.2).  The zero-frequency contribution is

\[
\boxed{
\mu_j^{\mathrm{mob}}
=-W_H\sum_{d\le Z_j}\frac{\mu(d)\log d}{d}.
}
\tag{4.1}
\]

The classical prime number theorem zero-free-region estimate gives

\[
\sum_{d\le Z}\frac{\mu(d)\log d}{d}
=-1+O\!\left(
\exp[-c(\log Z)^{3/5}(\log\log Z)^{-1/5}]
\right).
\tag{4.2}
\]

Therefore, uniformly over the primorial block,

\[
\boxed{
\mu_j^{\mathrm{mob}}=W_H+o(W_H).
}
\tag{4.3}
\]

For nonnegative weights with `W_H>0`, this gives

\[
\frac12W_H\le\mu_j^{\mathrm{mob}}\le\frac32W_H
\]

for all sufficiently large `X`.

Thus the explicit positive baseline follows from the single divisor identity; the
three Vaughan zero modes recombine to (4.1).

## 5. Exact nonzero-mode source

Define

\[
\mathcal E_j^{\mathrm{mob}}
=
\sum_{m=2}^{H}w_m\Lambda(P_j+m)-\mu_j^{\mathrm{mob}}.
\]

### Theorem 5.1 (single-column nonzero identity)

One has exactly

\[
\boxed{
\mathcal E_j^{\mathrm{mob}}
=-
\sum_{d\le Z_j}
\frac{\mu(d)\log d}{d}
\sum_{r=1}^{d-1}
\widehat w_d(r)e(rP_j/d).
}
\tag{5.1}
\]

Every coefficient is explicit and bounded by `log d`.  No growing-depth
convolution, truncated quotient coefficient, or heuristic principal subtraction
remains.

## 6. Physical-scale split

Equation (5.1) has a natural exact decomposition at `d=H`.

### Small moduli

For `d<=H`, the incidence column contains a physical progression of length about
`H/d`.  This is the range for classical completion, Type I averaging and
small-modulus cancellation.

### Large moduli

For `d>H`, a fixed pair `(j,d)` selects at most one offset.  Put

\[
m_j(d)=d\left\lceil\frac{P_j}{d}\right\rceil-P_j.
\]

Then

\[
A_{j,d}(w)
=
\mathbf1_{2\le m_j(d)\le H}w_{m_j(d)}.
\tag{6.1}
\]

On the prime-candidate range `X<m<=H`, the primorial shrinking-target theorem
shows that a fixed exponential-scale divisor column touches only boundedly many
centres.

Thus the source has exactly two analytic regimes:

1. polynomial small moduli with long physical progressions;
2. exponential large moduli with sparse primorial-index columns.

## 7. Revised Fortune target

For the sharp detector, it is sufficient to prove

\[
\boxed{
\sum_{j<N}|\mathcal E_j^{\mathrm{mob}}|^2
\ll NHX L(X),
\qquad L(X)=o(\log X).
}
\tag{7.1}
\]

Together with the positive baseline (4.3), the corrected one-sided detector
criterion then excludes every failed centre.

The remaining theorem is a signed Möbius--log divisor-dispersion estimate.  The
Möbius signs must remain inside the square; replacing them by absolute values
recreates the known positive-sieve loss.

## 8. Strategic consequence

The following issues are now removed from the critical path:

1. growing Heath--Brown depth;
2. fixed-depth coefficient proliferation;
3. Type I/II/III quotient-coefficient bookkeeping;
4. construction of the principal term;
5. source-to-frame coefficient preservation.

The exact remaining object is the one-modulus expression (5.1), with a
small-modulus progression range and a large-modulus shrinking-target range.

## 9. Boundary

Proved:

1. the exact Möbius--log identity (1.1);
2. the exact shifted source (2.2);
3. the exact positive principal term (4.1)--(4.3);
4. the exact nonzero source (5.1);
5. the physical-scale split and one-point large-modulus form.

Open:

1. the signed variance estimate (7.1);
2. the joint treatment of small and large moduli without absolute-value loss;
3. Fortune's conjecture.
