# Prime-degree explicit-formula reduction and a new slope signal

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-collapse-integration-20260723`  
**Scope:** function-field `d=1` Fortune sibling only.

## 1. Exact prime-degree identity

Let `A=Ai_{x^3}` be the rank-two cubic Airy sheaf on `A^1/F_p`, and write

\[
M_p:=\sum_{u\in\mathbf F_p}\operatorname{Tr}(\operatorname{Frob}_u^p\mid A_u)=-pT_p.
\]

For every `m>=1`, orthogonality in the Airy parameter gives

\[
\sum_{u\in\mathbf F_{p^m}}\operatorname{Tr}(\operatorname{Frob}_u\mid A_u)=-p^m.
\]

For prime `m=p`, decomposing `A^1(F_{p^p})` into closed points of degrees `1` and `p` gives

\[
-p^p=M_p+pC_p,
\]

where

\[
C_p:=\sum_{\deg(x)=p}\operatorname{Tr}(\operatorname{Frob}_x\mid A_x).
\]

Therefore

\[
\boxed{T_p=p^{p-1}+C_p.}
\]

Thus the desired bound

\[
|T_p|\le C p^{(p-1)/2}
\]

is exactly a square-root error term in the degree-`p` prime-point identity

\[
\boxed{|C_p+p^{p-1}|\le C p^{(p-1)/2}.}
\]

This is **PROVED**. It is an explicit-formula reformulation, not a bound.

## 2. Cyclic-power formulation

For a rank-two vector space `V` and a `p`-cycle `tau` acting on `V^{\otimes p}`,

\[
\operatorname{Tr}(\tau g^{\otimes p})=\operatorname{Tr}(g^p).
\]

Hence `M_p` is the Grothendieck--Lefschetz trace of `Frob_p` composed with the cyclic permutation on the `p`-fold tensor-power sheaf restricted to the diagonal. Equivalently, it is the first global trace of the `p`-th Adams class.

This identifies the remaining theorem as an equivariant fixed-point / Adams--Riemann--Roch problem: compare cyclic tensor power before and after diagonal restriction, with the Tate/main term `p^p` removed.

**OPEN:** prove that the residual equivariant local term has bounded weight-`p+1` multiplicity.

## 3. New exact p-adic valuation signal

For the committed exact values:

| `p` | `T_p` | `v_p(T_p)` | `(p+4)/3` |
|---:|---:|---:|---:|
| 11 | `322102` | 5 | 5 |
| 17 | `11899821517` | 7 | 7 |
| 23 | `-1010446643080743` | 9 | 9 |
| 29 | `-798145148362709627351` | 11 | 11 |

Thus

\[
\boxed{v_p(T_p)=(p+4)/3}
\]

for every nonzero exact value currently available with `p=2 mod 3`, `p>=11`.

Status: **VERIFIED COMPUTATIONALLY**, not proved.

This slope is too small by itself to imply the archimedean target, but it is highly structured and points to a Dwork/Newton-polygon decomposition. Write

\[
T_p=p^{(p+4)/3}U_p.
\]

The desired bound becomes

\[
|U_p|\le C p^{(p-11)/6}.
\]

The next useful theorem is therefore one of:

1. prove the exact valuation formula and identify `U_p` as a bounded-rank Frobenius trace;
2. prove a Dwork chain-level decomposition in which the slope-`(p+4)/3` block is the only block contributing to the rational trace;
3. show that the cyclic Adams residual local term is precisely the unit-root part after removal of the explicit Tate/main contribution.

## 4. What this does and does not achieve

- **PROVED:** the target is a degree-`p` prime-point error term and a cyclic-power diagonal defect.
- **VERIFIED COMPUTATIONALLY:** the exact valuation pattern above.
- **OPEN:** the absolute archimedean bound.
- **NOT CLAIMED:** that p-adic divisibility alone implies square-root cancellation.

The prime-degree and cyclic formulations are stronger guides than further raw prime sweeps because they identify two precise existing toolkits to test: equivariant Lefschetz/Adams operations and Dwork slope decompositions.
