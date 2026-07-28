# First-order prime-modulus diagonal theorem

Date: 28 July 2026  
Status: unconditional diagonal estimate proved; cross-modulus covariance remains open.

## 1. Setup

Use the locally centred first-order progression discrepancy

\[
\Delta_{j,r}
=
A_{j,r}-\frac{B_{j,r}^{*}}{r-1},
\qquad
z_j<r\le H,
\]

from `FIRST_ORDER_PRIME_MODULUS_GRAM_20260728.md`, with

\[
A_{j,r}
=
\sum_{m\in\mathcal P_{z_j}(H)\atop r\mid P_j+m}b_{j,m}
\]

and

\[
B_{j,r}^{*}
=
\sum_{m\in\mathcal P_{z_j}(H)\atop m\ne r}b_{j,m}.
\]

Assume the Fortune scaling

\[
H=\eta X^2,
\qquad 0<\eta<1,
\qquad z_j\asymp X,
\]

and the natural Euler--Buchstab weights

\[
|b_{j,m}|\ll\log X.
\tag{1.1}
\]

The diagonal energy is

\[
\mathcal D_X^{(1)}
=
\sum_j\sum_{z_j<r\le H}
\left|\frac{r-1}{r-2}\Delta_{j,r}\right|^2.
\tag{1.2}
\]

## 2. Total source mass

The prime number theorem and (1.1) give

\[
\boxed{
|B_{j,r}^{*}|\ll H
}
\tag{2.1}
\]

uniformly, because the number of candidate primes is `O(H/log H)` and
`log X asymp log H`.

The standard prime reciprocal-square estimate gives

\[
\sum_{r>X\atop r\text{ prime}}\frac1{r^2}
\ll\frac1{X\log X}.
\tag{2.2}
\]

Consequently

\[
\boxed{
\sum_{z_j<r\le H}
\frac{|B_{j,r}^{*}|^2}{(r-1)^2}
\ll
\frac{H^2}{X\log X}
\asymp
\frac{HX}{\log X}.
}
\tag{2.3}
\]

## 3. Brun--Titchmarsh bound for the hit columns

For each prime `r>z_j`, the residue `-P_j mod r` is reduced.  If

\[
z_j<r\le H/2,
\]

Brun--Titchmarsh gives

\[
\#\{m\le H:m\text{ prime},\ m\equiv-P_j\pmod r\}
\ll
\frac{H}{r\log(H/r)}.
\tag{3.1}
\]

Hence, by (1.1),

\[
|A_{j,r}|
\ll
\frac{H\log X}{r\log(H/r)}.
\tag{3.2}
\]

For `H/2<r<=H`, a residue class contains at most two integers in `[1,H]`, so

\[
|A_{j,r}|\ll\log X.
\tag{3.3}
\]

## 4. Dyadic reciprocal estimate

### Lemma 4.1

Uniformly for `z_j asymp X` and `H asymp X^2`,

\[
\boxed{
\sum_{z_j<r\le H/2\atop r\text{ prime}}
\frac1{r^2\log^2(H/r)}
\ll
\frac1{X(\log X)^3}
+
\frac1{H\log H}.
}
\tag{4.1}
\]

### Proof

Split the prime range into dyadic intervals `R<r<=2R`.  The Chebyshev bound

\[
\pi(2R)-\pi(R)\ll\frac R{\log R}
\]

shows that the contribution of one interval is

\[
\ll
\frac1{R\log R\,\log^2(H/(2R))}
\]

away from the final bounded number of intervals near `H/2`; those contribute
`O(1/(H log H))`.  In the remaining intervals the geometric factor `1/R`
makes the sum dominated by the first interval `R asymp X`, where
`log(H/R) asymp log X`.  This gives the first term of (4.1).  \(\square\)

## 5. Hit-column square sum

Combining (3.2) and Lemma 4.1,

\[
\begin{aligned}
\sum_{z_j<r\le H/2}|A_{j,r}|^2
&\ll
H^2(\log X)^2
\left(
\frac1{X(\log X)^3}
+
\frac1{H\log H}
\right)\\
&\ll
\frac{HX}{\log X}+H\log X.
\end{aligned}
\tag{5.1}
\]

The final term is smaller than `HX/log X` for sufficiently large `X`.
For `H/2<r<=H`, (3.3) and the prime number theorem give

\[
\sum_{H/2<r\le H}|A_{j,r}|^2
\ll
\frac{H}{\log H}(\log X)^2
\ll H\log X
=o\left(\frac{HX}{\log X}\right).
\tag{5.2}
\]

Therefore

\[
\boxed{
\sum_{z_j<r\le H}|A_{j,r}|^2
\ll
\frac{HX}{\log X}.
}
\tag{5.3}
\]

## 6. The diagonal theorem

### Theorem 6.1

Under the assumptions above,

\[
\boxed{
\mathcal D_X^{(1)}
\ll
\frac{NHX}{\log X}.
}
\tag{6.1}
\]

### Proof

For `r>z_j`, the factor `(r-1)/(r-2)` is uniformly bounded.  Also

\[
|\Delta_{j,r}|^2
\le
2|A_{j,r}|^2
+
2\frac{|B_{j,r}^{*}|^2}{(r-1)^2}.
\]

Apply (2.3) and (5.3) for each centre and sum over `j`.  \(\square\)

Thus the first-order diagonal is smaller than the Fortune variance threshold by a
factor of `log X`.

## 7. Consequence

The exact first-order Gram identity is

\[
\sum_j|G_j^{(1)}|^2
=
\mathcal D_X^{(1)}+
\mathcal O_X^{(1)}.
\]

Theorem 6.1 removes `mathcal D_X^(1)` from the critical path.  A bound

\[
\boxed{
\mathcal O_X^{(1)}
\ll NHX\,L_1(X),
\qquad L_1(X)=o(\log X),
}
\tag{7.1}
\]

would prove the complete physical first-order estimate.

The unresolved first-order theorem is therefore exclusively a cross-modulus
covariance estimate.

## 8. Numerical calibration

Complete finite panels through `X=101` give

\[
\frac{\mathcal D_{X,j}^{(1)}}{HX}
\approx0.04\text{--}0.10
\]

for the tested centres, with a declining envelope as `X` increases.  This is
consistent with (6.1) and substantially smaller than the theorem's permitted
constant.  The cross term changes sign and can be comparable with or larger than
the diagonal.  These observations are empirical only.

## 9. Boundary

Proved unconditionally:

1. source-mass bound (2.3);
2. hit-column bound (5.3);
3. first-order diagonal theorem (6.1).

Open:

1. cross-modulus covariance (7.1);
2. joint covariance with the sparse Euler chaos;
3. Fortune's conjecture.
