# Replacement Paper V: independent reconstruction record

**Date:** 2026-07-27  
**Scope:** the load-bearing arithmetic and geometric identities proposed for replacement Paper V.  
**Method:** clean reconstruction without importing the repository verification modules.

## 1. Degree barrier

Let
\[
P_d=\prod_{\deg \pi\le d}\pi
\]
be the polynomial primorial over a finite field. If a reducible offset `m` is coprime to `P_d`, every irreducible factor of `m` has degree at least `d+1`. A reducible polynomial has at least two irreducible factors counted with multiplicity, hence
\[
\deg m\ge 2d+2.
\]
Thus an irreducible value `P_d+m` with `deg m<=2d+1` forces the least admissible offset to be irreducible.

## 2. Affine orbit decomposition

For `d=1` over `F_p`, the full degree-at-most-three interval is
\[
f_{a,b,c,d}(T)=T^p-T+aT^3+bT^2+cT+d.
\]
Let `I_4` denote its irreducible count.

### Quadratic sector

When `a=0` and `b\ne0`, translation removes the linear interaction and scaling reduces the non-Artin--Schreier orbits to the normal form
\[
T^p+T^2+d.
\]
Each normal-form irreducible has an affine orbit of size `p(p-1)`. The exceptional linear Artin--Schreier orbit contributes `p-1`. If `N_2` is the normal-form count, the sector contributes
\[
(p-1)+p(p-1)N_2.
\]

### Cubic sector

For `a\ne0`, the translation
\[
T\mapsto T-\frac{b}{3a}
\]
uniquely removes the quadratic coefficient. Therefore every irreducible in a fixed depressed slice has exactly `p` translates in the full interval. Scaling changes the depressed cubic coefficient by a square because
\[
a\mapsto a\lambda^{p-3}=a\lambda^{-2}.
\]
Hence there are two scaling classes, represented by a square and a nonsquare, each containing `(p-1)/2` values. If their depressed counts are `N_+` and `N_-`, the cubic sector contributes
\[
\frac{p(p-1)}2(N_++N_-).
\]

Combining sectors gives
\[
\boxed{I_4=(p-1)+p(p-1)N_2+\frac{p(p-1)}2(N_++N_-).}
\]
Set
\[
W_p=N_2+\frac{N_++N_-}{2}.
\]
Then
\[
I_4=(p-1)+p(p-1)W_p.
\]
Since all three counts are nonnegative and `N_+`, `N_-` are even under `d\mapsto-d`, the crown condition `I_4>p-1` is equivalent to `W_p>0`, and failure is exactly
\[
N_2=N_+=N_-=0.
\]

The clean-room script exhaustively verifies the formula at `p=5,7,11`, reproducing

| p | I4 | N2 | N+ | N- |
|---:|---:|---:|---:|---:|
| 5 | 124 | 1 | 4 | 6 |
| 7 | 426 | 1 | 10 | 8 |
| 11 | 1660 | 1 | 14 | 14 |

## 3. Alternating-hook projector

For an `S_p`-representation `V` with commuting Frobenius `F`, the alternating hook multiplicity trace is
\[
\frac1{p!}\sum_{g\in S_p}\det(1-g\mid\operatorname{Std})\operatorname{Tr}(Fg\mid V).
\]
If the cycle lengths of `g` are `\lambda_1,\ldots,\lambda_r`, then
\[
\det(1-tg\mid\operatorname{Std})=
\frac{\prod_j(1-t^{\lambda_j})}{1-t}.
\]
At `t=1` this vanishes when `r>1`; for one `p`-cycle it equals `p`. The class contains `(p-1)!` elements, so
\[
\frac{p(p-1)!}{p!}=1.
\]
Thus the alternating hook projector is exactly one `p`-cycle trace, with no missing scalar.

The clean-room script checks the character on every partition of every prime `p<=11`.

## 4. Fixed-point count and circularity

Work on the affine ordered-root variety
\[
X_p=\{e_1=\cdots=e_{p-4}=0\}\subset\mathbf A^p.
\]
An `F\sigma`-fixed tuple is an ordered Frobenius orbit of some `\alpha\in F_{p^p}`. Since `p` is prime, its degree is one or `p`.

- Degree `p` gives an irreducible polynomial in the interval and `p` choices of initial root.
- Degree one gives the diagonal tuples and the polynomials `(T-a)^p`, one for each `a\in F_p`.

Therefore
\[
\boxed{\#\operatorname{Fix}(F\sigma\mid X_p)=pI_4+p.}
\]
Substituting the orbit decomposition shows that any one-sided trace inequality obtained solely by rewriting this fixed locus is equivalent to `W_p>0`; it is not an independent reduction.

## 5. Sparse-surface smoothness

Let
\[
\widetilde Y_p=\{s_1=s_2=\cdots=s_{p-4}=0\}\subset\mathbf A^p.
\]
At a point whose coordinates take distinct values `\alpha_1,\ldots,\alpha_r` with multiplicities `n_1,\ldots,n_r`, the Jacobian rank is `min(r,p-4)` by the truncated Vandermonde matrix. A rank failure requires `r<=p-5`.

The moment equations include
\[
\sum_j n_j\alpha_j^m=0\qquad(0\le m\le r-1),
\]
where the `m=0` equation is `\sum n_j=p=0` in characteristic `p`. The Vandermonde matrix is invertible, so every `n_j=0` in `F_p`. If `r>=2`, each multiplicity lies strictly between zero and `p`, contradiction. Thus `r=1`; the point is diagonal. Conversely every diagonal point is singular.

Hence
\[
\operatorname{Sing}(\widetilde Y_p)=\mathbf A^1(1,\ldots,1).
\]
After quotienting by diagonal translation and projectivising, the sparse surface
\[
Y_p=\{s_2=\cdots=s_{p-4}=0\}\subset\mathbf P^{p-3}
\]
is a smooth complete-intersection surface of multidegree `(2,3,...,p-4)`.

A fresh C++ enumeration checks all `7^7=823543` vectors at `p=7`: there are `5047` cone points, exactly `7` singular points, exactly the `7` diagonal points, and no mismatch.

## 6. q-line saturation

For the two depressed cubic classes, the exact ledger has the form
\[
N_A=(p-2)+B_A-\frac{S_0+A S_\chi}{2p}.
\]
Adding the two classes gives
\[
N_++N_-=2(p-2)+B_++B_- -\frac{S_0}{p}.
\]
Define
\[
S_0^{\mathrm{sat}}=p\bigl(2(p-2)+B_++B_-\bigr).
\]
Then algebraically
\[
\boxed{S_0^{\mathrm{sat}}-S_0=p(N_++N_-).}
\]
Because each depressed count is even,
\[
S_0^{\mathrm{sat}}-S_0\in2p\mathbf Z_{\ge0}.
\]
Consequently strict nonsaturation is exactly cubic positivity, not a weaker estimate. When `N_2=0`, it is exactly the full crown.

## 7. Scientific boundary

The reconstruction confirms the replacement Paper V endpoint:

1. the crown has an exact nonnegative normal-form coordinate `W_p`;
2. the sparse surface is smooth and its nontrivial representation sectors concentrate in primitive middle cohomology;
3. the alternating-hook projector and fixed-point formula recover the unknown count exactly;
4. the invariant q-line saturation defect is exactly the cubic count.

The remaining result is a genuinely new one-sided nonvanishing/nonsaturation theorem. No theorem reconstructed here proves it.
