# First-order prime-modulus Gram identity

Date: 28 July 2026  
Status: exact locally centred progression, character and Gram identities proved; Fortune-scale estimate open.

## 1. Physical first-order term

Use the Euler--Buchstab detector with

\[
b_{j,m}=u_{j,m}V(z_j,Y_j),
\qquad
Y_j=\sqrt{P_j+H}.
\]

For a prime `r` in the physical new-prime range

\[
z_j<r\le H,
\]

define

\[
X_{j,r}
=
\sum_{m\in\mathcal P_{z_j}(H)}
 b_{j,m}\xi_r(P_j+m),
\tag{1.1}
\]

where

\[
\xi_r(n)
=
\frac1{r-2}-
\frac{r-1}{r-2}\mathbf1_{r\mid n}.
\]

Then

\[
\mathcal F_{j,\le H}^{(1)}
=
\sum_{z_j<r\le H}X_{j,r}.
\tag{1.2}
\]

## 2. Exact prime-progression discrepancy

The candidate offset `m=r` is the unique candidate prime lying in the zero
residue modulo `r`.  Since `r` does not divide `P_j`, it is never a divisor hit.
Define

\[
B_{j,r}^{*}
=
\sum_{m\in\mathcal P_{z_j}(H)\atop m\ne r}b_{j,m}
\tag{2.1}
\]

and

\[
A_{j,r}
=
\sum_{m\in\mathcal P_{z_j}(H)\atop r\mid P_j+m}b_{j,m}.
\tag{2.2}
\]

### Theorem 2.1 (exact local centring)

One has

\[
\boxed{
X_{j,r}
=
\frac{b_{j,r}}{r-2}
-
\frac{r-1}{r-2}
\left(
A_{j,r}-\frac{B_{j,r}^{*}}{r-1}
\right).
}
\tag{2.3}
\]

### Proof

Separate `m=r` in (1.1).  Its contribution is `b_{j,r}/(r-2)`.  For every
remaining candidate prime `m`, the residue is nonzero.  Summing the constant part
of `xi_r` gives `B_{j,r}^*/(r-2)`, and the divisor hits contribute
`-(r-1)A_{j,r}/(r-2)`.  Rearrangement gives (2.3).  \(\square\)

Define the progression discrepancy

\[
\boxed{
\Delta_{j,r}
=
A_{j,r}-\frac{B_{j,r}^{*}}{r-1}.
}
\tag{2.4}
\]

and the locally centred first-order term

\[
\boxed{
G_j^{(1)}
=-
\sum_{z_j<r\le H}
\frac{r-1}{r-2}\Delta_{j,r}.
}
\tag{2.5}
\]

Then

\[
\mathcal F_{j,\le H}^{(1)}
=
G_j^{(1)}+E_j^{\mathrm{exc}},
\qquad
E_j^{\mathrm{exc}}
=
\sum_{z_j<r\le H}
\frac{b_{j,r}}{r-2}.
\tag{2.6}
\]

For the natural Euler weight `b_{j,r} ll log X`,

\[
E_j^{\mathrm{exc}}\ll\log X
\tag{2.7}
\]

because the reciprocal prime sum over `(z_j,H]` is bounded.  Therefore

\[
\sum_j|E_j^{\mathrm{exc}}|^2
\ll N(\log X)^2
=o(NHX).
\tag{2.8}
\]

The exceptional zero-residue column is harmless.

## 3. Exact character frame

For a nonprincipal Dirichlet character `chi mod r`, put

\[
S_{j,r}(\chi)
=
\sum_{m\in\mathcal P_{z_j}(H)\atop m\ne r}
 b_{j,m}\chi(m).
\tag{3.1}
\]

Since every summation residue in (3.1) is nonzero, multiplicative character
orthogonality gives

\[
\boxed{
\Delta_{j,r}
=
\frac1{r-1}
\sum_{\chi\bmod r\atop\chi\ne\chi_0}
\overline{\chi(-P_j)}S_{j,r}(\chi).
}
\tag{3.2}
\]

Consequently

\[
\boxed{
G_j^{(1)}
=-
\sum_{z_j<r\le H}
\frac1{r-2}
\sum_{\chi\bmod r\atop\chi\ne\chi_0}
\overline{\chi(-P_j)}S_{j,r}(\chi).
}
\tag{3.3}
\]

Equation (3.3) is the exact first-order character frame.  The centre appears only
through the multiplicative prime-prefix phase `chi(P_j)`; the source appears only
through prime character sums in the physical interval.

## 4. Exact Gram decomposition

Let

\[
a_{j,r}=\frac{r-1}{r-2}\Delta_{j,r}.
\tag{4.1}
\]

### Theorem 4.1

For every finite primorial block,

\[
\boxed{
\sum_j|G_j^{(1)}|^2
=
\mathcal D_X^{(1)}+
\mathcal O_X^{(1)},
}
\tag{4.2}
\]

where

\[
\mathcal D_X^{(1)}
=
\sum_j\sum_{z_j<r\le H}|a_{j,r}|^2
\tag{4.3}
\]

and

\[
\mathcal O_X^{(1)}
=
\sum_j
\sum_{\substack{z_j<r,s\le H\\r\ne s}}
 a_{j,r}\overline{a_{j,s}}.
\tag{4.4}
\]

This is the literal diagonal/off-diagonal expansion of (2.5).

Equivalently, inserting (3.2) gives the exact character Gram

\[
\boxed{
\begin{aligned}
\sum_j|G_j^{(1)}|^2
={}&
\sum_j
\sum_{r,s}
\frac1{(r-2)(s-2)}\\
&\times
\sum_{\chi\ne\chi_0\ (r)}
\sum_{\psi\ne\psi_0\ (s)}
\overline{\chi(-P_j)}\psi(-P_j)
S_{j,r}(\chi)\overline{S_{j,s}(\psi)}.
\end{aligned}
}
\tag{4.5}
\]

All prime ranges are `z_j<r,s<=H`.

## 5. Collision structure of the centre phases

For `j<k`, write

\[
P_k=P_jQ_{j,k},
\qquad
Q_{j,k}=\prod_{j<u\le k}p_u.
\]

For a new prime `r>z_k`,

\[
P_j\equiv P_k\pmod r
\Longleftrightarrow
r\mid Q_{j,k}-1.
\tag{5.1}
\]

Thus collisions of the sampled residue classes are controlled by prime divisors
of consecutive-prime products minus one.  For fixed `(j,k)`, the number of
colliding primes `r>X` is bounded by

\[
\frac{\log(Q_{j,k}-1)}{\log X}
\ll k-j.
\tag{5.2}
\]

Summing (5.2) over index pairs gives useful average collision sparsity, but does
not by itself control the cross-modulus term (4.4).

## 6. Relation to classical distribution theorems

The local discrepancy (2.4) samples prime offsets in the single reduced residue
class

\[
m\equiv-P_j\pmod r
\]

for moduli

\[
X<r\le H\asymp X^2.
\]

Classical Bombieri--Vinogradov reaches only approximately `r<=H^{1/2}=X`, the
lower endpoint of this range.  Therefore a direct invocation of standard level
of distribution does not prove (4.2) at the required scale.

The primorial block supplies an additional average over the moving classes
`-P_j mod r`.  The new theorem required is an averaged level-of-distribution or
large-sieve result for this multiplicative prefix orbit.

## 7. Load-bearing first-order target

A sufficient first-order estimate is

\[
\boxed{
\sum_j|G_j^{(1)}|^2
\ll NHX\,L_1(X),
\qquad
L_1(X)=o(\log X).
}
\tag{7.1}
\]

However, (7.1) is not sufficient for Fortune by itself.  The exact detector also
contains the sparse first-order tail, higher-order Euler chaos and all cross
covariances.  The purpose of (7.1) is to determine whether the physical
prime-modulus frame is controlled at the correct scale before those terms are
reinserted.

The decisive diagnostics are:

1. whether `mathcal D_X^(1)` already has Fortune scale;
2. whether `mathcal O_X^(1)` is lower order, cancelling, or dominant;
3. whether the centre collision structure (5.1) yields the missing level beyond
   Bombieri--Vinogradov.

## 8. Boundary

Proved exactly:

1. progression discrepancy identity (2.3);
2. harmless exceptional column (2.6)--(2.8);
3. character frame (3.2)--(3.3);
4. Gram decomposition (4.2)--(4.5);
5. centre collision criterion (5.1).

Open:

1. the Fortune-scale Gram estimate (7.1);
2. control of the cross-modulus covariance (4.4);
3. the joint Euler-chaos variance theorem;
4. Fortune's conjecture.
