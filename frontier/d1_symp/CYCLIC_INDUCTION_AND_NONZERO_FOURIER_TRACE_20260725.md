# Cyclic induction and the nonzero-frequency hook trace

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Status:** the representation identity, affine trace formula, and finite-critical-locus theorem are **PROVED**. The wild-infinity comparison is **OPEN**.

## 1. One cyclic difference replaces all hooks

Let `G=S_p`, let `C=<sigma>` for a `p`-cycle, and let `xi` be any nontrivial character of `C` over a characteristic-zero coefficient field containing the `p`-th roots of unity. Define

\[
\Lambda_p=\sum_{i=0}^{p-1}(-1)^i\bigwedge^i\mathrm{Std}.
\]

### Theorem 1

\[
\boxed{\Lambda_p=\operatorname{Ind}_C^{S_p}{\bf1}-\operatorname{Ind}_C^{S_p}\xi.}
\]

For `g in S_p`, the left character is `det(1-g|Std)`: it is `p` on a `p`-cycle and zero otherwise. The two induced characters have equal value `(p-1)!` at the identity, vanish off the identity and `p`-cycle classes, and have values `p-1` and `-1` on a `p`-cycle. Their difference has the same character.

Hence, for every `S_p`-equivariant Weil complex `K`,

\[
\boxed{\operatorname{HookAlt}(K)=K^C-K_\xi}
\]

in the Grothendieck group. This identity commutes with compact support, Fourier transform, restriction, and localization triangles. For ambient primitive cohomology it recovers `K_ambient=D_p`. On the open Fourier sector it removes the need for a separate theorem for every hook.

## 2. Exact affine Fourier trace

Put `q=p^r`, `L=F_{q^p}`, and write `Tr=Tr_{L/F_q}`. For

\[
\lambda=(\lambda_4,\ldots,\lambda_{p-4}),\qquad
P_\lambda(T)=\sum_{m=4}^{p-4}\lambda_mT^m,
\]

let `h_q(lambda)` be the affine monic separable degree-`p` point sum with `Tr(alpha)=Tr(alpha^2)=Tr(alpha^3)=0`, weighted by the alternating-hook trace and by the additive Fourier phase.

### Theorem 2

\[
\boxed{
h_q(\lambda)=
\sum_{\substack{\alpha\in L\\Tr(\alpha)=Tr(\alpha^2)=Tr(\alpha^3)=0}}
\psi_q(Tr(P_\lambda(\alpha)))-q.
}
\]

Only irreducible degree-`p` polynomials contribute to the hook trace, with value `p`. Replacing that factor by the sum over their `p` roots gives the degree-`p` elements of `L`. Since `p` is prime, the only elements of smaller degree are those in `F_q`. Every such element satisfies all trace equations and has phase one because extension trace multiplies by `p=0`; subtracting them gives the final `-q`.

Additive orthogonality gives the equivalent generalized-Airy form

\[
\boxed{
h_q(\lambda)=q^{-3}\sum_{u_1,u_2,u_3\in F_q}
\sum_{\alpha\in L}\psi_q\!\left(Tr(F_{\lambda,u}(\alpha))\right)-q,
}
\]

where

\[
F_{\lambda,u}(T)=P_\lambda(T)+u_1T+u_2T^2+u_3T^3.
\]

At `lambda=0` the degree drops to at most three and recovers the cubic Airy boundary. Away from the origin this is a family of generalized Airy sums of degrees at most `p-4`.

This formula is for the affine monic chart. Passing to the projective translation/scaling quotient requires the already separated Artin--Schreier, stabilizer, Tate, and boundary terms; no such term is silently discarded here.

## 3. No finite stationary point on the irreducible locus

### Theorem 3

If `(lambda,u_1,u_2,u_3)` is nonzero, then `F_{lambda,u}` has no critical point in `L\F_q`.

Indeed, `F'_{lambda,u}` is a nonzero polynomial of degree at most `p-5`, because all exponents lie strictly between zero and `p`. A root in `L` has degree over `F_q` dividing `p`. If it were not in `F_q`, its degree would be `p`, impossible for a root of a polynomial of degree at most `p-5`.

Therefore the nonzero-frequency alternating-hook transform has no interior finite stationary-phase contribution on the degree-`p` root locus. Every nontrivial contribution comes from:

1. vanishing cycles at infinity in a compactification of `F_{lambda,u}`;
2. the discriminant/nonseparable boundary;
3. the explicit affine quotient and exceptional-cell corrections.

The first item is the sole positive-dimensional generic source left.

## 4. Correct location of the Airy constituent

The earlier localization theorem proves that the half-twisted Airy object is absent from the canonical zero-frequency summand. The result above also closes finite stationary phase at nonzero frequency. Thus any transported copy of

\[
R_p((p-1)/2)
\]

must arise as a nearby-cycle object **at infinity in the root direction**, where the generalized Airy degree drops as `lambda` approaches zero. This does not reopen local vanishing cycles of the sparse section; that section is transverse on the separable locus.

Dobrovolska's characteristic-zero Fourier theorem for symmetric-group local systems is the relevant tame model: long-first-row hooks transform to IC sheaves on secant varieties of the rational normal curve. It does not directly settle the present case because the degree equals the base characteristic, the frequencies form a weighted sparse subspace, and the required contribution lies at a wild degree-drop boundary. The cyclic-induction theorem above does remove the need to handle high and low hooks separately.

## 5. Exact remaining application theorem

Construct a weighted projective compactification of `F_{lambda,u}` and compute the `C`-trivial minus `C`-nontrivial nearby-cycle complex at infinity over the frequency origin. Prove that its weight-two part is `R_p((p-1)/2)` and identify every complementary piece with the proved `S_0`, `S_chi`, `q=2`, `q=infinity`, discriminant, punctual, Tate, and Artin--Schreier ledger.

Equivalently, one needs a characteristic-`p` divided-power/wild-infinity analogue of the tame secant-support theorem restricted to the sparse frequency bundle.

## 6. Ruling

### PROVED

- the complete alternating hook is one cyclic induction difference;
- hook extraction is functorially `C`-invariants minus one nontrivial eigenspace;
- the affine nonzero-frequency trace is the displayed generalized Airy sum;
- every nonzero phase has no finite critical point of degree `p`.

### OPEN

- the wild-infinity nearby-cycle calculation;
- occurrence or absence of `R_p((p-1)/2)` there;
- the crown.

The generic interior stationary-phase route is closed. The application wall is now a specific wild-infinity Fourier theorem.

## Reference

G. Dobrovolska, *Fourier-Deligne transform and representations of the symmetric group*, arXiv:1301.2157.
