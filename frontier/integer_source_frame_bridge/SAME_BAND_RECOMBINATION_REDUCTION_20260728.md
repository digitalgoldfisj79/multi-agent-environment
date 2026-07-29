# Same-band recombination reduction

Date: 29 July 2026  
Status: **PROVED EXACTLY** as a dyadic reduction; the uniform same-band Bessel estimate is **OPEN**.

## 1. Frozen source and exact dyadic partition

Let `B` be a consecutive centre block of size at most

\[
K\ll\sqrt X.
\]

Let `Z=z_B` be its common frozen cutoff and

\[
\mathcal R_B=\{q:Z<q\le H,\ q\text{ prime}\}.
\]

Write

\[
\widetilde G_j^{(1)}=-\sum_{q\in\mathcal R_B}a_{j,q},
\qquad
a_{j,q}=\frac{q-1}{q-2}\widetilde\Delta_{j,q}.
\tag{1.1}
\]

Define

\[
R_\ell=2^\ell Z,
\qquad
\mathcal R_\ell=\{q\in\mathcal R_B:R_\ell<q\le\min(2R_\ell,H)\},
\tag{1.2}
\]

for `0\le\ell<L_*`, where

\[
L_*=\left\lceil\log_2(H/Z)\right\rceil.
\]

Discard empty bands, denote the remaining index set by `\mathscr L`, and put `L=|\mathscr L|`. Then

\[
L\le L_*\le1+\log_2(H/X)\ll\log X,
\tag{1.3}
\]

and the half-open bands form an exact disjoint partition of `\mathcal R_B`. For `\ell\in\mathscr L`, put

\[
G_{j,\ell}=-\sum_{q\in\mathcal R_\ell}a_{j,q}.
\tag{1.4}
\]

Hence

\[
\boxed{\widetilde G_j^{(1)}=\sum_{\ell\in\mathscr L}G_{j,\ell}.}
\tag{1.5}
\]

This replaces the earlier ambiguous choice of `R_0`; no endpoint or first-band gap remains.

## 2. Outer recombination

### Theorem 2.1

For every finite block,

\[
\boxed{
\sum_{j\in B}|\widetilde G_j^{(1)}|^2
\le L\sum_{\ell\in\mathscr L}\sum_{j\in B}|G_{j,\ell}|^2.
}
\tag{2.1}
\]

Apply Cauchy--Schwarz to (1.5) for each fixed `j` and sum over `j`. \(\square\)

No individual mixed-`(R,S)` Cotlar estimate is required for this sufficient route. The price is the single outer factor `L\ll\log X`.

## 3. Conditional same-band finish

Define

\[
D_{B,\ell}=\sum_{j\in B}\sum_{q\in\mathcal R_\ell}|a_{j,q}|^2,
\qquad
D_B=\sum_{\ell\in\mathscr L}D_{B,\ell}.
\tag{3.1}
\]

The established first-order diagonal theorem gives

\[
\boxed{D_B\ll\frac{KHX}{\log X}.}
\tag{3.2}
\]

### Theorem 3.1 — **CONDITIONAL** same-band finish

Assume uniformly for every block and nonempty band that

\[
\boxed{
\sum_{j\in B}|G_{j,\ell}|^2
\le C D_{B,\ell}+E_{B,\ell},
}
\tag{3.3}
\]

where `C` is absolute and

\[
\sum_{\ell\in\mathscr L}E_{B,\ell}
\ll\frac{KHX}{\log X}L_0(X),
\qquad L_0(X)=o(\log X).
\tag{3.4}
\]

Then

\[
\boxed{
\sum_{j\in B}|\widetilde G_j^{(1)}|^2
\ll KHX[1+L_0(X)].
}
\tag{3.5}
\]

Insert (3.3) into (2.1), use (3.2), and use `L\ll\log X`. \(\square\)

## 4. Global consequence

The mesoscopic freezing theorem gives

\[
\sum_{j<N}|G_j^{(1)}-\widetilde G_j^{(1)}|^2\ll NHX.
\tag{4.1}
\]

Summing (3.5) over the disjoint centre blocks and applying `|u+v|^2\le2|u|^2+2|v|^2` yields

\[
\boxed{
\sum_{j<N}|G_j^{(1)}|^2
\ll NHX[1+L_0(X)].
}
\tag{4.2}
\]

This is a sufficient first-order estimate; it is not the complete Fortune variance theorem.

## 5. Exact same-band target

For one band `R<q\le\min(2R,H)`, define

\[
T_{B,R}(j)=
\sum_{q\in\mathcal R_B\atop R<q\le\min(2R,H)}
\frac{q-1}{q-2}\widetilde\Delta_{j,q}.
\tag{5.1}
\]

The open estimate is

\[
\boxed{
\sum_{j\in B}|T_{B,R}(j)|^2
\ll
\sum_{j\in B}\sum_{q\in\mathcal R_B\atop R<q\le\min(2R,H)}
\left|\frac{q-1}{q-2}\widetilde\Delta_{j,q}\right|^2
+E_{B,R}.
}
\tag{5.2}
\]

The dyadic errors must satisfy (3.4).

## 6. Rough-quotient form

For centre `P_j`, common cutoff `Z`, and

\[
M_Z=|\{m:Z<m\le H,\ m\text{ prime}\}|,
\]

the corrected general-cutoff identity gives

\[
\boxed{
\widetilde\Delta_{j,q}
=\beta_j\left(N_{P_j,Z}(q)-\frac{M_Z-1}{q-1}\right),
}
\tag{6.1}
\]

where

\[
N_{P_j,Z}(q)=\#\{k:P_j+Z<qk\le P_j+H,\ (k,P_j)=1\}.
\]

Equivalently,

\[
\begin{aligned}
N_{P_j,Z}(q)
={}&\frac{H-Z}{q}\frac{\varphi(P_j)}{P_j}\\
&+\sum_{d\mid P_j}\mu(d)
\left[\psi\!\left(\frac{P_j+Z}{qd}\right)-
\psi\!\left(\frac{P_j+H}{qd}\right)\right].
\end{aligned}
\tag{6.2}
\]

Thus (5.2) is a signed common-source dispersion theorem for microscopic rough intervals of length `H/q\le X`.

## 7. Exact covariance formulation

Put

\[
C_B(q,s)=\sum_{j\in B}a_{j,q}\overline{a_{j,s}}.
\tag{7.1}
\]

Then

\[
\boxed{
\sum_{j\in B}|T_{B,R}(j)|^2
=D_{B,R}+2\Re\sum_{R<q<s\le\min(2R,H)}C_B(q,s).
}
\tag{7.2}
\]

Consequently the same-band theorem is precisely a signed bound for the aggregate cross-modulus covariance in (7.2). The established diagonal theorem controls only the first term.

## 8. Boundary

**PROVED EXACTLY**

1. exact half-open dyadic partition (1.2)--(1.5);
2. outer recombination (2.1);
3. conditional implication (3.3)--(3.5);
4. global implication (4.2);
5. covariance identity (7.2).

**COMPUTATIONALLY VERIFIED**

The finite verifier checks the generalized quotient identity, exact dyadic coverage, exact recombination and outer Cauchy inequality. Reported same-band ratios are diagnostics only.

**CONDITIONAL**

The physical first-order theorem (4.2) is conditional on (5.2) and (3.4).

**OPEN**

1. the uniform same-band estimate (5.2);
2. covariance with the normalized rough coordinate and ordered Buchstab tail;
3. the complete centred Fortune variance theorem;
4. Fortune's conjecture.
