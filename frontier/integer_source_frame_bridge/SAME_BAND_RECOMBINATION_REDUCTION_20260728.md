# Same-band recombination reduction

Date: 28 July 2026  
Status: exact dyadic recombination theorem proved; uniform same-band Bessel estimate open.

## 1. Mesoscopic frozen source

Let `B` be a consecutive centre block of cardinality at most

\[
K\ll\sqrt X,
\]

and let `\widetilde G_j^{(1)}` be the frozen first-order source from
`MESOSCOPIC_PRIMORIAL_ORBIT_REDUCTION_20260728.md`.  Write

\[
\widetilde G_j^{(1)}=-\sum_{r\in\mathcal R_B}a_{j,r},
\tag{1.1}
\]

where

\[
a_{j,r}=\frac{r-1}{r-2}\widetilde\Delta_{j,r}.
\tag{1.2}
\]

Partition the physical modulus range into disjoint dyadic prime bands

\[
\mathcal R_\ell=\{r\in\mathcal R_B:R_\ell<r\le2R_\ell\},
\qquad
R_\ell=2^\ell R_0,
\tag{1.3}
\]

with empty bands omitted.  Put

\[
G_{j,\ell}=-\sum_{r\in\mathcal R_\ell}a_{j,r}.
\tag{1.4}
\]

Then

\[
\widetilde G_j^{(1)}=\sum_{\ell=1}^{L}G_{j,\ell},
\qquad
L\le1+\log_2(H/X)\ll\log X.
\tag{1.5}
\]

## 2. Outer dyadic recombination

### Theorem 2.1

For every finite centre block,

\[
\boxed{
\sum_{j\in B}|\widetilde G_j^{(1)}|^2
\le
L\sum_{\ell=1}^{L}\sum_{j\in B}|G_{j,\ell}|^2.
}
\tag{2.1}
\]

### Proof

For each fixed `j`, Cauchy--Schwarz in the dyadic index gives

\[
\left|\sum_{\ell=1}^{L}G_{j,\ell}\right|^2
\le L\sum_{\ell=1}^{L}|G_{j,\ell}|^2.
\]

Sum over `j`.  \(\square\)

Thus no estimate of the individual mixed covariance

\[
\sum_jG_{j,\ell}\overline{G_{j,k}},
\qquad \ell\ne k,
\]

is required.

## 3. Same-band conditional reduction

Define the band diagonal

\[
D_{B,\ell}
=
\sum_{j\in B}\sum_{r\in\mathcal R_\ell}|a_{j,r}|^2
\tag{3.1}
\]

and the complete block diagonal

\[
D_B=\sum_{\ell=1}^{L}D_{B,\ell}.
\tag{3.2}
\]

The already-proved first-order diagonal theorem is uniform centre by centre and
therefore gives

\[
\boxed{D_B\ll\frac{KHX}{\log X}.}
\tag{3.3}
\]

### Theorem 3.1 (same-band conditional finish)

Suppose that, uniformly for every mesoscopic block `B` and every dyadic band,

\[
\boxed{
\sum_{j\in B}|G_{j,\ell}|^2
\le C D_{B,\ell}+E_{B,\ell},
}
\tag{3.4}
\]

where `C` is absolute and

\[
\sum_{\ell=1}^{L}E_{B,\ell}
\ll\frac{KHX}{\log X}L_0(X)
\tag{3.5}
\]

for some `L_0(X)=o(log X)`.  Then

\[
\boxed{
\sum_{j\in B}|\widetilde G_j^{(1)}|^2
\ll
KHX\,[1+L_0(X)].
}
\tag{3.6}
\]

In particular this is a valid Fortune-scale first-order bound with a bounded,
hence sublogarithmic, loss when the errors in (3.4) are absorbed by the diagonal.

### Proof

Insert (3.4) into (2.1), sum the diagonals using (3.2)--(3.3), and use
`L\ll log X`:

\[
\begin{aligned}
\sum_{j\in B}|\widetilde G_j^{(1)}|^2
&\le
L\left(CD_B+\sum_\ell E_{B,\ell}\right)\\
&\ll
(\log X)\frac{KHX}{\log X}[1+L_0(X)].
\end{aligned}
\]

This proves (3.6).  \(\square\)

## 4. Global consequence

The mesoscopic freezing theorem gives

\[
\sum_{j<N}|G_j^{(1)}-\widetilde G_j^{(1)}|^2\ll NHX.
\tag{4.1}
\]

Summing (3.6) over the `O(N/K)` blocks and using (4.1) yields

\[
\boxed{
\sum_{j<N}|G_j^{(1)}|^2
\ll NHX[1+L_0(X)].
}
\tag{4.2}
\]

Therefore the physical first-order theorem no longer requires off-diagonal decay
between different dyadic modulus scales.

## 5. Exact same-band target

For one dyadic band `R<r<=2R`, the required estimate is

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{R<r\le2R\atop r\text{ prime}}
\frac{r-1}{r-2}\widetilde\Delta_{j,r}
\right|^2
\ll
\sum_{j\in B}
\sum_{R<r\le2R\atop r\text{ prime}}
\left|
\frac{r-1}{r-2}\widetilde\Delta_{j,r}
\right|^2
}
\tag{5.1}
\]

up to errors whose band sum satisfies (3.5).

This is a same-scale common-source Bessel theorem.  It is weaker than absolute
control of every mixed dyadic covariance and is the correct immediate target.

## 6. Interaction with the rough-quotient collapse

Under the exact rough-quotient representation,

\[
\widetilde\Delta_{j,r}
=
\beta_j
\left(
N_{P_j}(r)-\frac{M_B-1}{r-1}
\right),
\tag{6.1}
\]

where `N_{P_j}(r)` counts primorial-rough quotients in an interval of length
`H/r`.  Hence (5.1) is equivalently a dyadic Bessel theorem for the signed
Möbius--sawtooth family

\[
\sum_{d\mid P_j}\mu(d)
\left[
\psi\!\left(\frac{P_j+z_B}{rd}\right)
-
\psi\!\left(\frac{P_j+H}{rd}\right)
\right].
\tag{6.2}
\]

The source is now rough rather than prime, and all modulus variables lie at one
scale.

## 7. Boundary

Proved exactly:

1. dyadic decomposition (1.5);
2. outer recombination inequality (2.1);
3. same-band conditional finish (3.6);
4. global reduction (4.2).

Already proved:

1. mesoscopic freezing at `O(NHX)` cost;
2. complete first-order diagonal `O(NHX/log X)`;
3. exact rough-quotient representation.

Open:

1. uniform same-band Bessel estimate (5.1);
2. its coupling to the normalized rough coordinate and Buchstab tail;
3. Fortune's conjecture.
