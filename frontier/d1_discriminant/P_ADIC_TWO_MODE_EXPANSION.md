# P-adic character expansion for the two determinant modes

**Date:** 2026-07-21  
**Status:** exact orthogonality reduction proved; p-adic nonvanishing open.

## 1. Root-incidence count

Let `Q=p^p` and let `Tr` denote the trace from `F_Q` to `F_p`. For fixed nonzero a, define

`C_a=# {(theta,c,d) in F_Q x F_p^2 : theta^p+a theta^3+c theta+d=0}`.

Every theta in F_p contributes one solution d for each c, giving p^2 incidences. Every theta outside F_p has degree p; if it is a root of a family member, that member is irreducible and contributes all p conjugate roots. Hence

`C_a=p^2+p N_a(p)`.

Thus `N_a mod p` is the first p-adic coefficient of C_a beyond the trivial p^2 incidence.

## 2. Additive-character expansion

Fix the standard additive character

`psi(z)=e_p(Tr(z))`

of F_Q. Orthogonality gives

`C_a=(p^2/Q) sum_(Tr(t)=0) sum_(Tr(t theta)=0)`
`      psi(t theta^p+a t theta^3)`.

The t=0 term is p^2. Therefore

`N_a=(p/Q) sum_(t !=0, Tr(t)=0) S_a(t)`,

where

`S_a(t)=sum_(Tr(t theta)=0)`
`       e_p(Tr(t^(1/p) theta)+a Tr(t theta^3))`.

The identity

`Tr(t theta^p)=Tr(t^(1/p) theta)`

was used to linearize the wild term.

For fixed t and theta put

`u=Tr(t theta^3)`,

`v=Tr(t^(1/p) theta)`.

## 3. Unweighted a-mode

For u in F_p,

`sum_(a !=0) e_p(a u)=p 1_(u=0)-1`.

Hence

`sum_(a !=0) S_a(t)`
` =p sum_(Tr(t theta)=0, Tr(t theta^3)=0) e_p(v)`
`  -sum_(Tr(t theta)=0)e_p(v)`.

The annihilator of the hyperplane `Tr(t theta)=0` is the line `F_p t`. Therefore the last linear sum is nonzero exactly when

`t^(1/p) in F_p t`.

If `t^(1/p)=lambda t`, applying Frobenius and then its pth iterate forces `lambda=1`; hence t is in F_p. Conversely every nonzero t in F_p lies in `ker Tr` because the extension degree is p.

Thus

`sum_(Tr(t theta)=0)e_p(v)`

is `p^(p-1)` for `t in F_p^*` and zero otherwise.

Define

`U_p=sum_(t !=0, Tr(t)=0)`
`    sum_(Tr(t theta)=0, Tr(t theta^3)=0)`
`    e_p(Tr(t^(1/p)theta))`.

Then the exact aggregate is

### Theorem PA.1

`sum_(a !=0) N_a=p^(2-p) U_p-(p-1)`.

Since

`sum_(a !=0)N_a=((p-1)/2)(N_++N_-)`,

this is the unweighted square-class mode alpha_p.

## 4. Quadratic-character a-mode

Let chi be the quadratic character of F_p and

`G_p=sum_(a !=0) chi(a)e_p(a)`.

For every u in F_p,

`sum_(a !=0)chi(a)e_p(a u)=G_p chi(u)`,

with `chi(0)=0`.

Define

`V_p=sum_(t !=0, Tr(t)=0)`
`    sum_(Tr(t theta)=0)`
`    chi(Tr(t theta^3))`
`    e_p(Tr(t^(1/p)theta))`.

Then:

### Theorem PA.2

`sum_(a !=0)chi(a)N_a=(p/Q)G_p V_p`.

Since

`sum_(a !=0)chi(a)N_a=((p-1)/2)(N_+-N_-)`,

this is the character square-class mode beta_p.

## 5. Crown criterion

The determinant route succeeds if the two class counts are not both zero modulo p. Equivalently, the two normalized quantities in Theorems PA.1 and PA.2 are not simultaneously zero modulo p.

This replaces p-1 separate a-slices by two explicit sums:

1. a cubic trace-zero incidence sum U_p;
2. a hybrid quadratic-character cubic sum V_p with one Gauss factor.

## 6. Next p-adic tasks

1. Embed the additive characters into the p-adic cyclotomic field.
2. Apply Stickelberger or Gross--Koblitz to determine the minimal valuation strata of U_p and `G_p V_p`.
3. Identify the reductions of the leading strata modulo p.
4. Test whether the two leading reductions can vanish simultaneously.
5. Compare the resulting Hasse-type invariants with alpha_p and beta_p from the determinant scan.

A proof that either leading reduction is nonzero for every p proves the d=1 cubic-slice crown.
