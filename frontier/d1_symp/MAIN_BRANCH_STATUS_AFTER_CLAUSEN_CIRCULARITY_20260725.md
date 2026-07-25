# Main-branch status after the Laurent--Airy Clausen circularity theorem

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune crown, primes `p congruent 5 mod 6`.  
**Status:** the prescribed local-inertia programme has been completed.  It proves exact local cancellation and an all-power Spin/Clausen factorisation, but it also proves that the Hayes route is algebraically circular.  The crown remains **OPEN**.

## 1. Target

The target is FF-Fortune `(p,1)`:

> for every prime `p`, there is an offset `m` of degree `2` or `3` such that
> \[
> T^p-T+m
> \]
> is irreducible over `F_p`.

For the present half-branch `p congruent 5 mod 6`, the analytic input remains

\[
\boxed{
|T_p|\ll p^{(p-1)/2}
}
\]

with an absolute constant.

## 2. Completed local-inertia calculation

For the rank-four family

\[
\mathscr H_B(u,s)
=H_c^1\!\left(
\mathbf G_m,
\mathcal L_{\chi_2}(x)
\mathcal L_\psi(x^3+ux+s/x)
\right),
\]

the terminal generic class is

\[
\Psi^p(\mathscr H_B)\otimes(\mathcal L_{\chi_2}(s)-1).
\]

The exact local calculation proves:

1. geometrically, `det(H_B)=L_(chi_2)(s)`;
2. at `s=infinity`, the rank-four slope-`3/4` wild induction becomes a tame regular `mu_4` block under `Psi^p`, and the Kummer subtraction cancels it identically;
3. at `s=0`, the residual class is the bounded tame class `2(chi_2-1)`;
4. at generic `u=infinity`, the slope-`3/2` and slope-`1/2` rank-two blocks become tame regular `mu_2` blocks under Adams;
5. the stationary discriminant `u^2+12s=0` is not a singular divisor of the original family.

Thus unbounded wild boundary conductor is not the obstruction.

## 3. Arithmetic orientation no-go

For a fibre polynomial

\[
P_{u,s}(T)=1-e_1T+e_2T^2-e_3T^3+e_4T^4,
\]

the admitted-prime arithmetic identities are

\[
 e_3=-\chi(-1)\chi(s)p\,e_1,
 \qquad
 e_4=-\chi(s)p^2.
\]

The orientation-reversing fibres are the square `s` fibres, and these have `e_2=0`.  But the terminal projector `chi(s)-1` vanishes on squares and retains nonsquares.  Hence the projector retains the arithmetic orientation-preserving rank-four fibres.

The hoped-for pointwise reduction to one rank-two Adams trace is false.

## 4. Geometric Spin factorisation

On the orientation cover

\[
s=r^2,
\]

the geometric determinant is trivial.  Since

\[
H^2_{et}(\mathbf A^1\times\mathbf G_m,\mu_2)=0,
\]

the `SO_4` local system lifts to `Spin_4`.  Using

\[
\operatorname{Spin}_4\cong\operatorname{SL}_2\times\operatorname{SL}_2,
\]

one obtains rank-two local systems `A,C` with

\[
\pi^*\mathscr H_B\cong\mathscr A\otimes\mathscr C.
\]

The deck involution exchanges the two factors.  This lowers the standard actual Adams realization from cubic rank growth to quadratic rank growth, but after the divided Hayes normalization one factor `p` remains.

## 5. Exact Clausen factorisation

Let `alpha^3=4`.  For every finite extension `k/F_p`, put

\[
U=\alpha u,
\qquad
s=-r^2/(3\alpha).
\]

Then

\[
\boxed{
 t_k(u+r)t_k(u-r)
 =-\chi_k(3)G_k h_k(U,s).
}
\]

This is proved by expanding the product, changing variables `x=z+y`, and evaluating one exact quadratic Gauss sum.  The nonsquare `s` fibres are exactly those parametrised by `r!=0`.

Consequently the abstract Spin factors are explicitly

\[
\mathcal A_{u+r},
\qquad
\mathcal A_{u-r},
\]

the two shifted cubic Airy sheaves.

## 6. Exact Hayes circularity

Let

\[
f_p(a)=\operatorname{Tr}(F^p\mid\mathcal A_a),
\qquad
c=-\chi(3)G_p.
\]

The generic Kummer-projected sum is

\[
\mathcal C_{gen}
=
\frac{c^{-p}}p
\left[
\left(\sum_a f_p(a)\right)^2
-
\sum_a f_p(a)^2
\right].
\]

The exact zero-parameter boundary calculation gives

\[
\mathcal A_{0,p}-\mathcal B_{0,p}
=
\frac{c^{-p}}p
\sum_a f_p(a)^2.
\]

Therefore the diagonal second moment cancels exactly and

\[
\boxed{
\mathcal A_p-\mathcal B_p
=
\frac{c^{-p}}p
\left(\sum_a f_p(a)\right)^2.
}
\]

But

\[
\sum_a f_p(a)=-pT_p.
\]

Substitution into the terminal Hayes identity gives `T_p^2=T_p^2` with scalar exactly one.

Hence the Hayes two-plane correlation is not an independent lower-complexity theorem.  It is an exact reconstruction of the original Airy first moment.

## 7. Verification

Remote exact jobs:

- `6a650b39db23d7a7ec1cd027`: stationary expansions and local induced-block Adams characters pass;
- `6a650d0edb23d7a7ec1cd076`: admitted-prime arithmetic orientation identities pass at the complete `p=5` grid and selected `p=11,17` fibres;
- `6a65104ddb23d7a7ec1cd0d0`: exact Clausen identity passes for every nonsquare base-field fibre at `p=5,11,17,23`;
- `6a6511cadb23d7a7ec1cd106`: repository Clausen verifier and complete `F_(5^5)` boundary/off-diagonal cancellation pass.

## 8. Routes now closed

1. unbounded wild boundary conductor as the explanation for the Hayes loss;
2. rank-four Adams plus virtual conductor and termwise Deligne;
3. pointwise rank-two collapse on the Kummer-selected fibres;
4. Spin factorisation plus termwise Deligne;
5. using the Hayes two-plane correlation as an independent route to the Airy estimate;
6. using its diagonal second moment to gain the missing factor.

## 9. Exact remaining analytic wall

The analytic problem returns, without simplification, to

\[
\boxed{
\left|
\sum_{a\in\mathbf F_p}
D_p(t_p(a),p)
\right|
\ll p^{(p+1)/2}.
}
\]

Equivalently,

\[
|T_p|\ll p^{(p-1)/2}.
\]

The branch has already proved that this is an absolute Frobenius correlation between adjacent equal-weight invariant Airy moment motives, after one explicit Picard--Lefschetz Tate correction.  The motives are Hodge-disjoint in characteristic zero, so the required cancellation cannot be supplied by a characteristic-zero motivic correspondence.

## 10. Application wall

Separately, the application-side transport still requires an all-Frobenius identification of the normalized Airy constituent inside the invariant and quadratic q-line projectors of the residual cubic-tail root complex, including every boundary and Tate constituent.

## 11. Scientific position

The requested local programme has reached a theorem-level conclusion, not an unfinished calculation:

- the strongest local/Spin/Hayes mechanism has been completely evaluated;
- it yields a new exact Clausen factorisation;
- it is provably circular for the terminal estimate.

Further progress to `d=1` now requires a genuinely new theorem on the one-dimensional rank-two Airy Adams first moment, or a different application-side certificate that avoids the absolute Airy estimate.