# Fourier–Airy compression and the exact cyclic-convolution obstruction

**Date:** 2026-07-22  
**Status:** exact Fourier calculation proved; crown remains open. The remaining effectivity theorem is sharpened from a general toric direct-image problem to a characteristic-p cyclic-convolution problem for a rank-two cubic Airy sheaf.

## 1. Root sheaf and Fourier transform

For fixed `q != 0`, put

`f_q(x)=q x^p+x^3-3x`

and let

`R_q=(f_q)_! Q_l[1]`

on the affine `v`-line (up to the harmless sign convention `v=-f_q(x)`). Its Frobenius trace at `v` is the number of roots of `f_q(x)+v=0`.

Let `FT_v` denote the Fourier--Deligne transform in `v`. For nonzero dual coordinate `s`, the transformed trace is represented by

`sum_x psi(s(qx^p+x^3-3x)).`

Over a perfect characteristic-p base, the Artin--Schreier sheaf satisfies

`L_psi(s q x^p) ~= L_psi((s q)^(1/p) x)`

geometrically (equivalently after inverse-Frobenius pullback in the parameter). Thus the phase is geometrically equivalent to

`s x^3 + ((s q)^(1/p)-3s)x.`

This is a cubic Airy phase. Its compactly supported cohomology in `x` has generic dimension two. Therefore:

### Theorem FAC.1

Away from the standard exceptional loci, `FT_v(R_q)` is a cubic Airy perverse sheaf of generic rank `2`.

This is an exact cancellation-before-cohomology compression of the original degree-p root cover.

## 2. Why rank two does not immediately prove the crown

The irreducibility indicator is

`Lambda_p = psi^p(R_q)-R_q`

at the level of fibrewise Frobenius traces, where `psi^p` is the p-th Adams operation:

`Tr(Frob_v | psi^p R_q)=Tr(Frob_v^p | R_q).`

Fourier transform does not commute with tensor products or Adams operations. It exchanges tensor product on the `v`-line with additive convolution on the dual line. Consequently

`FT_v(psi^p R_q)`

is not `psi^p(FT_v R_q)` in the ordinary tensor category. It is a cyclic-isotypic summand of the p-fold additive convolution power of the rank-two Airy object.

The tempting substitution

`psi^p(R_q) -> psi^p(A_q)`, `A_q=FT_v(R_q)`,

would give an immediate `O(p)` rank bound because for rank two

`psi^p(V)=Sym^p(V)-det(V) Sym^(p-2)(V)`

has total effective rank `2p`. But this substitution is unjustified: it uses the tensor Adams operation after a transform that changes tensor into convolution.

## 3. Exact sharpened target

Let `A_q=FT_v(R_q)`, a rank-two cubic Airy perverse sheaf. Let `Cyc_p^*(A_q)` denote the virtual cyclic-isotypic object obtained from the p-fold additive convolution under the action of the cyclic permutation group `C_p`, with character `1-psi` matching

`Ind_(C_p)^(S_p)(1-psi)=Lambda_p`.

The missing theorem can be stated as follows.

### Cyclic Airy Effectivity Lemma (CAEL)

For the family `A_q`, the semisimplified numerator-plus-denominator rank and total q-line conductor of

`Cyc_p^*(A_q)`

and its quadratic Kummer twist are `O(p)` with an absolute implied constant.

CAEL implies the required `O(sqrt(p))` bounds after division by the normalizing factor `p`, hence the function-field crown after finite certification.

## 4. Characteristic-p opportunity and obstruction

The exponent of the cyclic power equals the characteristic. This is not a generic p-fold convolution problem. The diagonal and Frobenius graph in the p-fold addition map can coalesce inseparably, so a characteristic-p cyclic-power or Adams--Riemann--Roch formula might reduce `Cyc_p^*(A_q)` to a bounded number of Frobenius pullbacks and vanishing-cycle corrections.

No theorem located in the checked Fourier--Deligne and convolution literature directly supplies that identity with quantitative effective ranks. Standard Fourier--Deligne theory controls the transform, and convolution categories make convolution into a tensor operation, but neither statement by itself bounds the effective size of the characteristic-p cyclic isotypic summand.

## 5. Relation to the toric five-term equation

The Laurent equation

`q(u^(2p)+1)+u^(p+3)+u^(p-3)+v u^p=0`

encodes the same transformed object after Kummer descent `x=u+u^(-1)`. The Fourier calculation shows that the central `p`-dependence is already absorbed by inverse Frobenius in the linear coefficient of a cubic phase. Therefore the five-term toric support should not be attacked by a generic Newton-polytope bound. The correct object is the characteristic-p cyclic convolution of a rank-two Airy sheaf.

## 6. Strategic conclusion

This route is not closed. It has produced a material new reduction:

- before: prove effectivity for a rank-zero two-dimensional toric direct image with apparent degree p;
- now: prove effectivity for one explicitly defined cyclic-isotypic p-fold convolution of a rank-two cubic Airy family.

The theorem-level obstruction is CAEL, specifically the absence of a characteristic-p formula that converts the cyclic convolution summand into an effective complex of total rank `O(p)` before taking q-line cohomology.

Any future continuation should begin with cyclic power operations in the convolution Tannakian category, not with generic toric bounds or hook-by-hook cohomology.
