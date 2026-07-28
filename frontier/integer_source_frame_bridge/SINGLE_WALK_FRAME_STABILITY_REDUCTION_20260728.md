# Single-walk frame-stability reduction

Date: 28 July 2026  
Status: exact reduction proved; distinct-modulus reciprocal dispersion open.

## 1. Input

Use the centred reciprocal kernel from
`CENTRED_SOURCE_TO_FRAME_IDENTITY_20260728.md`:

\[
\mathcal K_X(L)
 =2\sum_{\substack{a\ge1\\m_a>0}}
   \frac{|\Theta_{a,X}(L)|^2}{m_a},
\qquad
\mathcal K_X(0)=1,
\qquad
0\le\mathcal K_X(L)\le1.
\]

The centred frame matrix is

\[
\mathbf K_X=
 \bigl(\mathcal K_X(P_j-P_k)\bigr)_{j,k<N},
\]

and for the actual detector residual vector \(c\),

\[
\mathfrak G_X(c)=c^*\mathbf K_Xc.
\]

## 2. Total off-diagonal mass

Define

\[
\boxed{
\mathcal S_X=
 \sum_{\substack{j,k<N\\j\ne k}}
 \mathcal K_X(P_j-P_k).
}
\tag{2.1}
\]

For a positive harmonic \(a\), put

\[
\mathcal E^{(1)}_a
 =
 \sum_{q,r}p_{q,a}p_{r,a}
 \left(
 \left|F_X\!\left(
 a\left(\frac1q-\frac1r\right)
 \right)\right|^2-N
 \right).
\tag{2.2}
\]

### Theorem 2.1 (exact single-walk mass identity)

One has

\[
\boxed{
\mathcal S_X
 =
 2\sum_{\substack{a\ge1\\m_a>0}}
 \frac{\mathcal E^{(1)}_a}{m_a}.
}
\tag{2.3}
\]

### Proof

Expand \(\mathcal K_X(P_j-P_k)\), sum over \(j\ne k\), and use

\[
\sum_{j\ne k}e(\theta(P_j-P_k))
 =|F_X(\theta)|^2-N.
\]

All sums are finite.  \(\square\)

## 3. Same-modulus and distinct-modulus decomposition

Let

\[
\kappa_{2,a}=\sum_qp_{q,a}^2
\]

and

\[
\mathcal R^{(1)}_a
 =
 \sum_{\substack{q,r\\q\ne r}}p_{q,a}p_{r,a}
 \left(
 \left|F_X\!\left(
 a\left(\frac1q-\frac1r\right)
 \right)\right|^2-N
 \right).
\tag{3.1}
\]

### Corollary 3.1 (exact one-walk residual decomposition)

\[
\boxed{
\mathcal S_X
 =
 2N(N-1)\sum_a\frac{\kappa_{2,a}}{m_a}
 +
 2\sum_a\frac{\mathcal R^{(1)}_a}{m_a}.
}
\tag{3.2}
\]

### Proof

When \(q=r\), the phase is zero and the bracket in (2.2) is
\(N^2-N=N(N-1)\).  The remaining terms are exactly (3.1).  \(\square\)

The same estimate used for the diagonal term in corrected Paper II gives

\[
\sum_a\frac{\kappa_{2,a}}{m_a}
 \ll_\rho\frac{\log H}{H}.
\]

Since \(N\asymp X/\log X\) and \(H\asymp X^2\),

\[
\boxed{
2N(N-1)\sum_a\frac{\kappa_{2,a}}{m_a}
 \ll_\rho\frac{N^2\log H}{H}
 \ll\frac1{\log X}=o(1).
}
\tag{3.3}
\]

Thus the forced same-modulus contribution is already below the stability
threshold.

## 4. From scalar mass to an operator lower bound

The matrix \(\mathbf K_X-I\) is real symmetric, has zero diagonal, and has
nonnegative off-diagonal entries.  Therefore

\[
\|\mathbf K_X-I\|_{\mathrm{op}}
 \le
 \max_j\sum_{k\ne j}\mathcal K_X(P_j-P_k)
 \le\mathcal S_X.
\tag{4.1}
\]

### Theorem 4.1 (scalar sufficient condition)

If

\[
\mathcal S_X\le\delta<1,
\tag{4.2}
\]

then for every vector \(c\),

\[
\boxed{
(1-\delta)\|c\|_2^2
 \le c^*\mathbf K_Xc
 \le(1+\delta)\|c\|_2^2.
}
\tag{4.3}
\]

In particular, the reciprocal frame has a uniform lower bound
\(\kappa=1-\delta\).

### Proof

Equation (4.1) and the spectral theorem give

\[
|c^*(\mathbf K_X-I)c|
 \le\delta\|c\|_2^2.
\]

Rearrange.  \(\square\)

## 5. Corrected analytic target

By (3.2)--(3.3), the source-independent lower-frame problem is reduced to

\[
\boxed{
\sum_a\frac{\mathcal R^{(1)}_a}{m_a}=o(1).
}
\tag{5.1}
\]

A stronger convenient sufficient condition is

\[
\sum_a\frac{|\mathcal R^{(1)}_a|}{m_a}=o(1).
\tag{5.2}
\]

This is a distinct-modulus reciprocal dispersion estimate for the
**single primorial-prefix walk**.  It is not the old pair-sum target.

The change of scale is material:

- old unweighted pair-space target: approximately \(M X^{o(1)}\);
- corrected lower-frame target: \(o(1)\) total off-diagonal mass.

The smaller scale is possible because (5.1) controls a normalised frame
operator whose diagonal is exactly one.

## 6. Relation to Fortune

The complete corrected route is now:

1. prove the single-walk stability target (5.1), or a residual-restricted lower
   frame bound;
2. prove the centred source-frame upper bound
   \[
   \mathfrak G_X(c)\ll NHXL(X),
   \qquad L(X)=o(\log X);
   \]
3. infer
   \[
   \sum_j|\Psi_j-\mu_j|^2\ll NHXL(X);
   \]
4. apply the one-sided shifted-detector criterion.

No estimate for the old coefficient-free pair frame is required.

## 7. Boundary

The identities and reduction above are exact.  No estimate of
\(\mathcal R^{(1)}_a\) is proved here.  The next theorem is a genuine
reciprocal-fraction cancellation result for the increasing prime-product walk.
