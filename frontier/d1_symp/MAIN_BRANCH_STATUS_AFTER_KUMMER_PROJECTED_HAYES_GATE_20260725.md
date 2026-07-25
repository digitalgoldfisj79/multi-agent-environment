# Main-branch status after the Kummer-projected Hayes gate

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Target:** FF-Fortune `(p,1)` for every prime `p`.

## 1. New proved reductions

### Universal Hayes sheaf

The degree-at-most-four Hayes `L`-polynomials are the fibre `L`-functions of

\[
\mathcal L_{\chi_2}(x)
\otimes
\mathcal L_\psi(wx^3+ux+v/x)
\]

on `G_m`. Its compactly supported `H^1` has rank four when `wv!=0`.

The two terminal parameter planes are

\[
\mathscr H_A(u,t)=H_c^1(\mathcal L_{\chi_2}(x)\mathcal L_\psi(tx^3+ux+x^{-1})),
\]

and

\[
\mathscr H_B(u,t)=H_c^1(\mathcal L_{\chi_2}(x)\mathcal L_\psi(x^3+ux+t/x)).
\]

Their affine rank drops are `4->2->1` for A and `4->3` for B.

### Two-plane collapse

For `t=s^3!=0`, root scaling gives

\[
I_A(u,s^3)=\chi(s)I_B(u/s,s).
\]

Since `chi(3)=-chi(-1)` for `p=5 mod 6`, the terminal signed combination reduces exactly to

\[
\chi(-1)\left(
\mathcal A_{0,p}-\mathcal B_{0,p}
+
\sum_{u,s\ne0}(\chi(s)-1)I_B(u,s)
\right).
\]

The two one-dimensional boundary sums already satisfy the required `p^(p/2)` scale by the pointwise rank-at-most-three Hayes bound.

Thus the analytic boulder is now one theorem:

\[
\boxed{
\left|
\sum_{u\in F_p}\sum_{s\in F_p^*}
(\chi(s)-1)I_B(u,s)
\right|
\ll p^{p/2}.
}
\]

Equivalently, it is the compactly supported trace of

\[
\Psi^p(\mathscr H_B)\otimes(\mathcal L_\chi-1)
\]

on `A^1 x G_m`.

## 2. Proved no-go for the naive conductor route

For a rank-four object,

\[
\Psi^p(V)=\sum_{j=0}^3(-1)^jS_{(p-j,1^j)}(V).
\]

The total actual rank of the standard Schur realization is

\[
\frac{4p(p^2+2)}3,
\]

and after the Kummer difference it is twice this. Hence termwise Deligne plus triangle inequality necessarily has a growing polynomial constant. Virtual rank zero is not a bounded-Betti theorem.

## 3. Published literature boundary

The family is exactly Katz--Tiep's two-parameter `t=1` Laurent--Airy family

\[
G(1/x,x,3,\chi_2).
\]

Published results prove rank four, geometric irreducibility, self-duality and fourth moment

\[
M_{2,2}=3.
\]

However, their general rank-four tensor-indecomposability theorem explicitly excludes

\[
(A,B,a)=(1,1,3),
\]

which is exactly this family. No published theorem located in the audit supplies the varying `p`-th Adams correlation or a bounded-complexity realization.

## 4. Current theorem-level wall

> **Kummer-projected exceptional Laurent--Airy Adams theorem.** Prove an absolute `p^(p/2)` bound for the parameter-plane trace of
> \[
> \Psi^p(\mathscr H_B)\otimes(\mathcal L_\chi-1).
> \]

A proof must use object-level cancellation among the four hook-Schur terms, a nonstandard characteristic-`p` realization, or direct parameter-plane orthogonality. The standard Adams realization and existing fixed-moment monodromy theory do not suffice.

## 5. Application boulder

The application-side target remains the object-level extraction of the normalized Airy constituent from the already reduced cubic-tail root complex, with every `q=2`, `q=infinity`, discriminant, affine, Tate, invariant and quadratic-projector term identified for all Frobenius powers.

The full Fourier elimination through the first `p-4` coefficient directions is already proved and is not part of the remaining wall.

## 6. Scientific ruling

### New proved progress

- exact universal rank-four Laurent-sheaf realization;
- exact two-plane-to-one-plane Kummer-projector collapse;
- harmless separation of affine boundary sums;
- exact cubic growth of the standard Adams realization;
- precise applicability and exceptional-case boundary of the Katz--Tiep literature.

### Closed

- the original two-independent-plane formulation;
- deriving the estimate from fibre rank four alone;
- termwise Deligne on the standard Schur realization;
- claiming full monodromy or bounded Adams complexity from the available literature.

### Open

- the Kummer-projected exceptional Laurent--Airy Adams theorem;
- the cubic-tail Airy-to-hook application comparison;
- FF-Fortune `(p,1)`.