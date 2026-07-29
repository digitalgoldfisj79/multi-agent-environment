# Normalized survivor martingale and sparse-tail audit

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the normalized-survivor identities and complete-CRT martingale statements below are **PROVED EXACTLY**. A support-only sparse-tail Carleson argument is **REJECTED AS A SEPARATE POSITIVE ROUTE**. Deterministic sampling transfer remains **OPEN**.

## 1. Normalized survivor form

For `z<R\le Y`, put

\[
V(z,R)=\prod_{z<r\le R\atop r\ {m prime}}\frac{r-2}{r-1}
\]

and

\[
\Pi(z,R)=\prod_{z<r\le R\atop r\ {m prime}}r.
\]

The local Euler coordinate satisfies

\[
1+\xi_r(n)=\frac{r-1}{r-2}\mathbf1_{r\nmid n}.
\]

Therefore the partial Euler product has the exact form

\[
\boxed{
M_R(n)
:=
\prod_{z<r\le R}(1+\xi_r(n))
=
V(z,R)^{-1}\mathbf1_{(n,\Pi(z,R))=1}.
}
\]

Thus the Euler martingale is precisely the normalized survivor process of the sieve.

## 2. Exact band increments

Let

\[
z=R_0<R_1<\cdots<R_L=Y
\]

be ordered band endpoints. Define

\[
B_\ell(n)=M_{R_\ell}(n)-M_{R_{\ell-1}}(n).
\]

Then

\[
\boxed{M_Y(n)-1=\sum_{\ell=1}^{L}B_\ell(n).}
\]

Equivalently,

\[
B_\ell(n)
=
M_{R_{\ell-1}}(n)
\left[
V(R_{\ell-1},R_\ell)^{-1}
\mathbf1_{(n,\Pi(R_{\ell-1},R_\ell))=1}
-1
\right].
\]

This is the exact martingale increment including every Euler order in the band.

## 3. Complete-CRT orthogonality

Under the product measure in which the candidate offset is uniform over the nonzero residue classes at each new prime, one has

\[
\mathbb E M_R=1.
\]

The process `(M_{R_\ell})` is a martingale, hence

\[
\mathbb E B_\ell=0,
\qquad
\mathbb E(B_\ell B_m)=0
\quad(\ell\ne m).
\]

Moreover, conditionally on the previous bands,

\[
\boxed{
\mathbb E(B_\ell^2\mid\mathcal F_{\ell-1})
=
M_{R_{\ell-1}}^2
\left(V(R_{\ell-1},R_\ell)^{-1}-1\right).
}
\]

Consequently,

\[
\boxed{
\mathbb E|M_Y-1|^2
=
\sum_{\ell=1}^{L}\mathbb E|B_\ell|^2.
}
\]

This is the exact quadratic variation that the deterministic Fortune sample must imitate.

## 4. Weighted survivor counts

For one centre `P_j`, define the weighted survivor count

\[
S_j(R)
=
\sum_{z_j<m\le H\atop m\ {m prime}}
 u_{j,m}
 \mathbf1_{(P_j+m,\Pi(z_j,R))=1}.
\]

Since

\[
M_R(P_j+m)
=
V(z_j,R)^{-1}
\mathbf1_{(P_j+m,\Pi(z_j,R))=1},
\]

the weighted band increment is exactly

\[
\boxed{
\mathcal B_{j,\ell}
=
V(z_j,Y)
\left[
V(z_j,R_\ell)^{-1}S_j(R_\ell)
-
V(z_j,R_{\ell-1})^{-1}S_j(R_{\ell-1})
\right].
}
\]

The complete detector residual is the zeroth coordinate plus the sum of these normalized survivor increments.

Thus `BMST(X)` can be read as a deterministic square-function theorem for normalized sifted counts.

## 5. Top-tail drift/hit decomposition

Consider one band `(R_0,R_1]` with `R_0\ge H`. Put

\[
A=V(R_0,R_1)^{-1}.
\]

Every prime in the band can hit at most one physical offset for a fixed centre, but the martingale increment is not only the sparse hit term. It decomposes exactly as

\[
\boxed{
B(n)
=
M_{R_0}(n)(A-1)
-
M_{R_0}(n)A\,
\mathbf1_{\exists r\in(R_0,R_1]:r\mid n}.
}
\]

The first term is a dense deterministic normalization drift. The second is the sparse kill term. Their expectations cancel in the CRT model.

Both pieces are of main size. Therefore the one-point support of the hit term does not permit it to be bounded independently.

## 6. Rejection of the separate sparse Carleson route

A support-only Carleson estimate would bound

\[
M_{R_0}(n)A
\mathbf1_{\exists r\in(R_0,R_1]:r\mid n}
\]

positively by the multiplicity of one-point hits. This discards the drift

\[
M_{R_0}(n)(A-1),
\]

which is the conditional mean required to centre the band.

The finite exact decomposition shows that the drift and hit block energies can each be tens of times larger than their combined energy, with a large negative cross term. Hence sparse support is useful only inside the centred band increment.

The route

> control dense physical bands analytically, then bound the top tail by a separate positive one-point Carleson estimate

is therefore rejected. The interface covariance is load-bearing.

## 7. The deterministic transfer theorem

### Open theorem `NSMT(X)` — normalized survivor martingale transfer

For every mesoscopic block `B`, prove

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{\ell}\mathcal B_{j,\ell}
+
\text{zeroth-centred coordinate}
\right|^2
\ll
KHX\,L(X),
\qquad L(X)=o(\log X),
}
\]

while preserving the band conditional means.

Equivalently, prove an approximate deterministic square-function inequality

\[
\sum_{j\in B}\left|\sum_\ell\mathcal B_{j,\ell}\right|^2
\ll
\sum_\ell\sum_{j\in B}|\mathcal B_{j,\ell}|^2
+
E_B
\]

with Fortune-scale error, together with the correct control of each centred band.

`NSMT(X)` is an explicit normalized-sieve form of `BMST(X)`.

## 8. Range disposition

### Dense physical bands

These require the common-base joint hybrid Gram theorem `JHGF(X)` or an equivalent actual-source same-band theorem. Fixed-conductor orbit control alone is insufficient because density/spectrum cancellation is cross-conductor.

### Transition bands

Neither complete-period Ramanujan orthogonality nor a positive sieve estimate matches the moving interval length. The normalized survivor increment must remain centred.

### One-point tail

Hit support is sparse, but its normalization drift is dense. The pair must be estimated jointly. Same-offset repeated hits retain the existing primorial-prefix rigidity; different offsets do not force a common divisor of centre differences.

## 9. Boundary

**PROVED EXACTLY**

1. normalized survivor representation of every partial Euler product;
2. exact survivor-band telescope;
3. exact conditional quadratic variation under complete CRT sampling;
4. exact weighted survivor-count representation;
5. exact drift/hit decomposition in the one-point tail.

**REJECTED AS A SEPARATE POSITIVE ROUTE**

1. support-only sparse-tail Carleson control;
2. treating tail hits independently of normalization drift;
3. gluing a physical estimate to an independently bounded tail by triangle inequality.

**COMPUTATIONALLY VERIFIED**

1. complete-CRT martingale means, orthogonality and quadratic variation;
2. exact finite tail drift/hit decomposition.

**EMPIRICAL ONLY**

Finite block energies show large cancellation between tail drift and sparse hits; no asymptotic estimate is inferred.

**OPEN**

1. `NSMT(X)` / `BMST(X)`;
2. joint common-base physical theorem `JHGF(X)`;
3. the Fortune variance theorem and Fortune's conjecture.
