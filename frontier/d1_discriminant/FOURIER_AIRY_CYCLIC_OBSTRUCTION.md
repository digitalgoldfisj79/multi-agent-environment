# Fourier–Airy compression and the exact cyclic-convolution obstruction

**Date:** 2026-07-22  
**Status:** **partly superseded.** The Fourier calculation and rank-two cubic Airy transform remain exact. The pre-cohomology Cyclic Airy Effectivity Lemma and diagonal-fixed-locus strategy in this note are superseded by:

- `CYCLIC_AIRY_FORMALISM_AND_NO_GO.md`;
- `HOOK_COHOMOLOGY_EFFECTIVITY_LEDGER.md`;
- `ADAMS_PUSHFORWARD_NO_GO.md`.

The correct cyclic class is the virtual difference `e_1-e_zeta`, not a single nontrivial eigensummand. Frobenius traces localise on a degree-p field-trace fibre rather than the geometric diagonal. No `O(p)` effective local-system model exists before t/v cohomology. The crown remains open at the after-pushforward effectivity theorem.

The remainder of this file is retained as the historical derivation of the Airy transform and the provisional target that it motivated.

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

This is an exact Fourier compression of the original degree-p root cover. It does not, by itself, provide effective cyclic-power cancellation.

## 2. Why rank two does not immediately prove the crown

The irreducibility indicator is

`Lambda_p = psi^p(R_q)-R_q`

at the level of fibrewise Frobenius traces, where `psi^p` is the p-th Adams operation:

`Tr(Frob_v | psi^p R_q)=Tr(Frob_v^p | R_q).`

Fourier transform does not commute with tensor products or Adams operations. It exchanges tensor product on the `v`-line with additive convolution on the dual line. Consequently

`FT_v(psi^p R_q)`

is not `psi^p(FT_v R_q)` in the ordinary tensor category. It is represented by the difference of the trivial and a nontrivial cyclic eigensummand of the p-fold additive convolution power, with the exact Tate twist and shift recorded in `CYCLIC_AIRY_FORMALISM_AND_NO_GO.md`.

The tempting substitution

`psi^p(R_q) -> psi^p(A_q)`, `A_q=FT_v(R_q)`,

would give an immediate `O(p)` rank bound because for rank two

`psi^p(V)=Sym^p(V)-det(V) Sym^(p-2)(V)`

has total effective rank `2p`. This substitution is unjustified: it uses the tensor Adams operation after a transform that changes tensor into convolution.

## 3. Historical provisional target

The provisional Cyclic Airy Effectivity Lemma sought an `O(p)` effective model for the cyclic convolution before q-line cohomology. The later audit proved that formulation too strong:

- the generic p-cycle local-system class has minimum positive-plus-negative effective rank `2^(p-1)`;
- its canonical fixed-q hook cohomology has total actual middle dimension
  `((2p-3)2^(p-1)+3)/p`;
- the geometric cyclic diagonal computes the wrong fixed-point problem for arithmetic Frobenius traces.

The surviving target is after-pushforward cancellation between the even and odd hook cohomologies, leaving only `O(p)` uncancelled q-line Frobenius constituents.

## 4. Characteristic-p opportunity and obstruction

The exponent of the cyclic power equals the characteristic, but standard cyclic localisation does not collapse the arithmetic trace. Fixed points of `Frob composed tau` are parameterised by the degree-p field-trace fibre, whereas fixed points of `tau` alone form the diagonal supported over zero.

Likewise, moving Adams through compact support changes the point set from `U(F_Q)` to `U(F_(Q^p))`. The discrepancy is global and cannot be absorbed into a finite boundary or tangent correction.

## 5. Relation to the toric five-term equation

The Laurent equation

`q(u^(2p)+1)+u^(p+3)+u^(p-3)+v u^p=0`

encodes the same transformed object after Kummer descent `x=u+u^(-1)`. The Fourier calculation shows that the degree-p term is absorbed geometrically into an inverse-Frobenius linear coefficient of a cubic phase. Generic Newton-polytope estimates therefore remain inappropriate.

However, the exact audits show that the Airy transform is an alternative presentation of the same exponential virtual cancellation, not an automatic effective reduction.

## 6. Revised strategic conclusion

The Airy calculation remains useful, but the pre-cohomology Cyclic Airy route is closed. A future continuation must act on the already-integrated q-family and prove an explicit parity-reversing pairing between hook cohomologies, or an equivalent cancellation of all but `O(p)` semisimple Frobenius factors.

Do not resume the single-projector, geometric-diagonal, or coherent Adams--Riemann--Roch variants without a materially new theorem that overcomes the exact no-go results cited above.