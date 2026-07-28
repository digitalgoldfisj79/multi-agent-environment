# Normalized tail-chaos energy identity

Date: 28 July 2026  
Status: exact orthogonal normalization and Fortune-scale coefficient budget proved; centred sampling/Bessel theorem open.

## 1. Absorb the physical sieve exactly

Let

\[
P=\prod_{r\le z}r,
\qquad
z<H<(z^+)^2,
\qquad
Y=\sqrt{P+H}.
\]

For a candidate prime offset `m`, put `n=P+m`.  Define the exact physical
roughness indicator

\[
\boxed{
R_H(n)
=
\prod_{z<r\le H\atop r\text{ prime}}
\mathbf1_{r\nmid n}.
}
\tag{1.1}
\]

and the tail normalizing product

\[
\boxed{
V_H(Y)
=
\prod_{H<r\le Y\atop r\text{ prime}}
\frac{r-2}{r-1}.
}
\tag{1.2}
\]

The exact Euler detector factors at the physical threshold:

### Theorem 1.1

\[
\boxed{
\mathbf1_{n\text{ prime}}
=
R_H(n)V_H(Y)
\prod_{H<r\le Y\atop r\text{ prime}}
(1+\xi_r(n)),
}
\tag{1.3}
\]

where

\[
\xi_r(n)
=
\frac1{r-2}-
\frac{r-1}{r-2}\mathbf1_{r\mid n}.
\]

### Proof

The factors with `z<r<=H` in the full Euler detector multiply with their
normalizing constants to give exactly `R_H(n)`.  The remaining factors give
(1.3).  \(\square\)

All nontrivial tail primes now exceed the physical interval length.  Hence a fixed
pair `(P,r)` selects at most one offset.

## 2. Local orthonormal coordinate

For `r>H`, define

\[
\boxed{
\eta_r(n)=\sqrt{r-2}\,\xi_r(n).
}
\tag{2.1}
\]

On the probability space of nonzero offset residues modulo `r`, with `P` fixed
and nonzero, one has

\[
\mathbb E\eta_r(P+m)=0
\tag{2.2}
\]

and

\[
\boxed{
\mathbb E|\eta_r(P+m)|^2=1.
}
\tag{2.3}
\]

Indeed, `xi_r=-1` at the unique divisor residue and `xi_r=1/(r-2)` at the other
`r-2` nonzero offset residues, so

\[
\mathbb E|\xi_r|^2
=
\frac1{r-1}
+
\frac{r-2}{r-1}\frac1{(r-2)^2}
=
\frac1{r-2}.
\]

For a squarefree product `q` of primes in `(H,Y]`, define

\[
\eta_q(n)=\prod_{r\mid q}\eta_r(n),
\qquad
\rho(q)=\prod_{r\mid q}(r-2),
\tag{2.4}
\]

with `eta_1=1` and `rho(1)=1`.  Under the complete product measure on nonzero
residues, the functions `eta_q` form an orthonormal product basis.

## 3. Exact normalized chaos expansion

Since

\[
\xi_r=\frac{\eta_r}{\sqrt{r-2}},
\]

one has exactly

\[
\boxed{
\prod_{H<r\le Y}(1+\xi_r(n))
=
\sum_{q\in\mathcal Q(H,Y)}
\frac{\eta_q(n)}{\sqrt{\rho(q)}},
}
\tag{3.1}
\]

where `mathcal Q(H,Y)` is the set of squarefree integers whose prime factors all
lie in `(H,Y]`, including `q=1`.

Thus the shifted prime-output detector is

\[
\boxed{
\begin{aligned}
\mathcal D_P
={}&
\sum_{z<m\le H\atop m\text{ prime}}
\log(P+m)R_H(P+m)V_H(Y)\\
&\times
\sum_{q\in\mathcal Q(H,Y)}
\frac{\eta_q(P+m)}{\sqrt{\rho(q)}}.
\end{aligned}
}
\tag{3.2}
\]

## 4. Exact coefficient mass

The squared chaos coefficients satisfy

\[
\begin{aligned}
\sum_{q\in\mathcal Q(H,Y)}\frac1{\rho(q)}
&=
\prod_{H<r\le Y}
\left(1+\frac1{r-2}\right)\\
&=
\prod_{H<r\le Y}\frac{r-1}{r-2}\\
&=
\boxed{\frac1{V_H(Y)}}.
\end{aligned}
\tag{4.1}

This is exact.

For one candidate offset `m`, the complete squared coefficient mass in (3.2) is
therefore

\[
\boxed{
\log^2(P+m)R_H(P+m)V_H(Y).
}
\tag{4.2}

The same formula with the `q=1` term omitted is bounded by (4.2).

## 5. Fortune-scale coefficient budget

Mertens' theorem gives

\[
V_H(Y)
\asymp
\frac{\log H}{\log Y}
\asymp
\frac{\log X}{X}.
\tag{5.1}
\]

Also

\[
\log(P+m)\asymp X
\]

and the number of candidate prime offsets is `O(H/log H)`.  Summing (4.2) over
the physical source gives

\[
\begin{aligned}
&\sum_{z<m\le H\atop m\text{ prime}}
\log^2(P+m)R_H(P+m)V_H(Y)\\
&\qquad\ll
\frac{H}{\log H}
X^2
\frac{\log X}{X}.
\end{aligned}
\]

Since `log H asymp log X`,

\[
\boxed{
\sum_m\sum_q
|c_{P,m,q}|^2
\ll HX,
}
\tag{5.2}

where

\[
c_{P,m,q}
=
\log(P+m)R_H(P+m)V_H(Y)\rho(q)^{-1/2}.
\]

Across `N` primorial centres,

\[
\boxed{
\sum_{j,m,q}|c_{P_j,m,q}|^2
\ll NHX.
}
\tag{5.3}

This is exactly the Fortune variance scale.  There is no remaining coefficient-
size, convolution-depth or divisor-order loss.

## 6. The principal coordinate

The `q=1` coordinate in (3.2) is

\[
\boxed{
\mathcal Z_{P,H}^{\mathrm{rough}}
=
V_H(Y)
\sum_{z<m\le H\atop m\text{ prime}}
\log(P+m)R_H(P+m).
}
\tag{6.1}

It has main-term size `H`.  Therefore a raw Bessel inequality for the complete
chaos cannot prove the centred Fortune variance: the principal coordinate must be
subtracted first.

The exact smooth-primitive centring and the explicit candidate principal identify
the required deterministic main component.  The remaining obligation is to show
that the centred version of (6.1), together with the nonempty tail chaos, obeys a
sampling inequality at the coefficient scale (5.3).

## 7. Exact conditional finish

Let

\[
\mathcal T_j^{\circ}
=
\mathcal D_{P_j}-\mu_{P_j}^{\mathrm{prim}}.
\]

A centred tail-chaos Bessel theorem of the form

\[
\boxed{
\sum_j|\mathcal T_j^{\circ}|^2
\ll
L(X)
\sum_{j,m,q}|c_{P_j,m,q}|^2,
\qquad
L(X)=o(\log X),
}
\tag{7.1}

would, by (5.3), give

\[
\sum_j|\mathcal T_j^{\circ}|^2
\ll NHX L(X)
\]

and hence complete the Fortune implication.

The theorem must preserve the covariance between the centred rough coordinate and
the nonempty tail chaos.  Bounding them independently by positive majorants would
recreate the sieve parity loss.

## 8. Consequence for method selection

The exact remaining problem is now a sampling theorem, not a source-size theorem:

1. the source is exact;
2. the principal term is explicit;
3. the local coordinates are orthonormal under the complete residue model;
4. the total coefficient mass is already at Fortune scale;
5. every nontrivial tail modulus exceeds `H` and is one-point in the physical
   offset.

The role of the primorial shrinking-target theorem is to replace complete-residue
orthogonality by deterministic sparse sampling across the actual centre orbit.

## 9. Boundary

Proved exactly:

1. physical-sieve absorption (1.3);
2. local normalization (2.1)--(2.3);
3. orthogonal product expansion (3.1)--(3.2);
4. coefficient identity (4.1)--(4.2).

Proved from classical input:

1. Fortune-scale coefficient budget (5.2)--(5.3).

Open:

1. centred sampling/Bessel theorem (7.1);
2. covariance of the rough principal coordinate with the sparse tail;
3. Fortune's conjecture.
