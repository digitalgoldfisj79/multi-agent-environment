# Cyclic Airy formalism and the pre-cohomology no-go

**Date:** 2026-07-22  
**Status:** exact Grothendieck-group, trace, and representation-theoretic statements proved. This file corrects the single-projector and diagonal-fixed-locus formulations in the provisional Cyclic Airy programme. The function-field crown remains open.

## 1. Conventions

Let `k=F_Q` have characteristic `p>=5`, let `l!=p`, and enlarge the coefficient field so that it contains a primitive p-th root of unity `zeta`.

Use the unnormalised Fourier--Deligne transform

`FT(K)=R p_(s,!)(p_v^*K tensor L_psi(vs))`

on `A^1_v`, and unnormalised additive convolution

`K * L = R a_!(K box L)`

on `A^1_s`, where `a(s_1,s_2)=s_1+s_2`.

With these conventions Fourier inversion gives

`FT(K tensor L) ~= (FT(K)*FT(L))(1)[2]`.

Iterating,

`FT(K^(tensor p)) ~= FT(K)^( *p )(p-1)[2(p-1)].`

At trace-function level the Tate twist contributes the expected factor `Q^(-(p-1))`.

## 2. The correct cyclic projector

Let `tau=(1 2 ... p)` act on `W=K^(tensor p)` by cyclically permuting the tensor factors. Write `e_1` and `e_zeta` for the trivial and one fixed nontrivial eigenspace projectors of `C_p=<tau>`.

### Theorem CAF.1 -- cyclic formula for the Adams operation

In the Grothendieck group,

`boxed(psi^p(K) = [e_1 W]-[e_zeta W].)`

It is not represented by the single summand `e_zeta W`.

Proof. Let `F` be any endomorphism commuting with `tau`. Since `W` and `F` are defined over the rational coefficient field, all nontrivial `C_p` eigenspaces have the same F-trace after scalar extension. Therefore

`Tr(F | e_1W)-Tr(F | e_zeta W)=Tr(F tau | W).`

The cyclic tensor identity gives

`Tr(F tau | K^(tensor p))=Tr(F^p | K)`,

which is the defining trace identity for `psi^p`.

For the p-cycle irreducibility character,

`Lambda_p(K)=psi^p(K)-K`

and hence

`boxed(Lambda_p(K)=[e_1K^(tensor p)]-[e_zeta K^(tensor p)]-[K].)`

This is the cyclic-power form corresponding to `Ind_(C_p)^(S_p)(1-zeta)`.

## 3. Exact Fourier--convolution identity

Let

`R_q=(f_q)_! Q_l`,  `f_q(x)=q x^p+x^3-3x`,

and put `A_q=FT(R_q)`.

The cyclic projectors commute with Fourier transform and additive convolution. Theorem CAF.1 and the product--convolution identity give

### Theorem CAF.2

`boxed(FT(psi^p(R_q))`
` = ([e_1 A_q^( *p)]-[e_zeta A_q^( *p)])(p-1)[2(p-1)].)`

Consequently

`boxed(FT(Lambda_p(R_q))`
` = ([e_1 A_q^( *p)]-[e_zeta A_q^( *p)])(p-1)[2(p-1)]-A_q.)`

Thus the relevant Airy object is the *difference* of the trivial and a nontrivial cyclic eigensummand, followed by subtraction of `A_q`.

## 4. The arithmetic fixed locus is not the diagonal

Let `A` be any Weil complex on `A^1_s`. Let `a_m(y)` denote its trace function over `F_(Q^m)`. Put

`C_p(A)=[e_1 A^( *p)]-[e_zeta A^( *p)].`

For `s in F_Q`, Grothendieck--Lefschetz applied to `Frob_Q composed tau` on the p-fold addition fibre gives:

### Theorem CAF.3 -- trace-fibre formula

`boxed(Tr(Frob_s | C_p(A)_s)`
` = sum_(y in F_(Q^p), Tr_(F_(Q^p)/F_Q)(y)=s) a_p(y).)`

Indeed, a fixed tuple has the form

`(y,Frob(y),...,Frob^(p-1)(y))`

and its sum is the field trace of `y`.

The geometric fixed locus of `tau` alone is the diagonal and maps to `p y=0`. That locus computes `Tr(tau)` without arithmetic Frobenius. It does **not** compute the Frobenius trace of the cyclic eigendifference, which is `Tr(Frob tau)`.

Therefore the proposed shortcut

`nonidentity cyclic fixed locus = diagonal supported at zero`

cannot establish the required q-line trace bound.

The relevant arithmetic fixed variety is the Weil-restricted trace fibre, of dimension `p-1` over `F_Q`, not the one-dimensional geometric diagonal.

## 5. Orthogonality recovers the original extension-root count

Apply Theorem CAF.3 to `A_q=FT(R_q)`. Fourier orthogonality on the trace hyperplane gives

`boxed(Tr(Frob_s | C_p(A_q)_s)`
` = Q^(p-1) sum_(v in F_Q) Tr(Frob_v^p | (R_q)_v) psi(sv).)`

After the twist `(p-1)` in Theorem CAF.2, this is exactly the Fourier transform of the function

`v -> # {x in F_(Q^p): f_q(x)=v}`.

Thus cyclic Airy convolution is an exact repackaging of the degree-p extension-root incidence. The trace-fibre formula does not by itself reduce its arithmetic dimension.

## 6. Exact representation-theoretic effectivity barrier

For generic q, the geometric monodromy of the root cover is `S_p`. Let

`Std=Perm_p-1`.

The p-cycle character has the unique irreducible expansion

`Lambda_p=sum_(i=0)^(p-1)(-1)^i exterior^i Std`.

Each hook `exterior^i Std` is irreducible, pairwise nonisomorphic, and has dimension

`binomial(p-1,i)`.

### Theorem CAF.4 -- minimum effective rank before cohomology

Suppose actual semisimple `S_p` representations `E^+` and `E^-` satisfy

`[E^+]-[E^-]=Lambda_p`.

After cancelling common constituents, uniqueness of the irreducible character expansion forces

`E^+ = direct_sum_(i even) exterior^i Std`,

`E^- = direct_sum_(i odd) exterior^i Std`.

Therefore

`boxed(dim E^+=dim E^-=2^(p-2),)`

`boxed(dim E^+ + dim E^-=2^(p-1).)`

No `O(p)` effective local-system model for `Lambda_p` exists before the t/v pushforward. This is an exact obstruction, not a limitation of the hook presentation.

For comparison, if `r=rank R_q=p`, the two cyclic eigenspaces in `R_q^(tensor p)` have dimensions

`dim e_1=(r^p+(p-1)r)/p`,

`dim e_zeta=(r^p-r)/p`,

whose difference is `r`; the virtual cancellation is enormous.

## 7. What is closed and what remains open

The following proposed route is closed:

> Construct the cyclic Airy eigendifference itself, before t/v cohomology, as a two-term effective complex of total rank `O(p)` by localising all nonidentity cyclic elements on the diagonal.

It fails for two independent exact reasons:

1. the required projector is `e_1-e_zeta`, not one `e_zeta` summand;
2. Frobenius traces localise on the degree-p trace fibre, not the geometric diagonal.

The representation-theoretic lower bound additionally proves that no alternative `O(p)` effective replacement exists in the generic root-local-system category.

This does **not** disprove the desired bounded q-line L-function after integrating over the t/v line. Fourier transform changes generic ranks, and derived pushforward can create genuine cancellations between the hook cohomologies. The surviving theorem is therefore strictly an **after-pushforward effectivity theorem**:

### Revised crown obstruction

Let

`K_q=R Gamma_c(A^1_v_bar, Lambda_p(R_q))`

with the appropriate treatment of the two finite singular fibres and infinity. Prove that the semisimplified numerator-plus-denominator degree of the q-line family `K_q`, and of its Kummer twist, is `O(p)` with an absolute constant.

The rank-two Airy transform supplies an alternative presentation of `K_q`, but its generic rank two does not remove the exponential cyclic-power cancellation before cohomology.

## 8. Strategic conclusion

The Cyclic Airy route has reached a sharp no-go boundary. Any successful continuation must introduce a theorem that acts *after* the v/t pushforward -- for example a derived trace formula, a cancellation theorem for paired local Fourier transforms, or an explicit small complex for the already-integrated q-family.

Generic cyclic fixed-locus localisation, ordinary convolution Tannakian arguments, and the rank-two Airy stalk alone cannot prove the crown.