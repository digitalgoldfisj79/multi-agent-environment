# Cyclic Tate diagonal and the exact Airy lift obstruction

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic main branch for primes `p=5 mod 6`.  
**Status:** the modular Tate-diagonal statements are **PROVED**. Their application identifies a precise integral-lift theorem; the absolute Airy correlation remains **OPEN**.

## 1. Tate cohomology of a cyclic tensor power

Let `k` be a perfect field of characteristic `p`, let `V` be a finite-dimensional `k`-vector space, and let `C_p` act on `V^(tensor p)` by cyclic permutation of the factors.

### Theorem 1

For every Tate degree `n`, there is a natural Frobenius-semilinear isomorphism

\[
\boxed{
\widehat H^n(C_p,V^{\otimes p})\cong V^{(1)},
}
\]

where `V^(1)` is the Frobenius twist. It is induced by the diagonal polynomial law

\[
v\longmapsto v^{\otimes p}.
\]

### Proof

Choose a basis of `V`. The tensor-word basis of `V^(tensor p)` splits into:

1. constant words `e_i^(tensor p)`, each fixed by `C_p`;
2. nonconstant words, whose orbits have size exactly `p` because `p` is prime.

Every nonconstant orbit spans a free regular `k[C_p]`-module and therefore has zero Tate cohomology. Each constant word spans a trivial module. In characteristic `p`, both maps in the periodic Tate complex, `1-sigma` and the norm `1+sigma+...+sigma^(p-1)`, vanish on a trivial line, so that line contributes one copy of `k` in every Tate degree.

The resulting basis identification is natural. Indeed,

\[
(v+w)^{\otimes p}-v^{\otimes p}-w^{\otimes p}
\]

is a sum of complete nonconstant cyclic orbits, hence is zero in Tate cohomology, and

\[
(av)^{\otimes p}=a^p v^{\otimes p}.
\]

Thus the diagonal is additive after passage to Tate cohomology and is Frobenius-semilinear, which is exactly a linear map from `V^(1)`. The basis calculation proves that it is an isomorphism. \(\square\)

If an endomorphism `F` of `V` is present, the isomorphism is compatible with the induced endomorphism because

\[
F^{\otimes p}(v^{\otimes p})=(Fv)^{\otimes p}.
\]

## 2. Rank-two Adams collapse in characteristic `p`

For a rank-two bundle or representation `E` in characteristic `p`, the standard modular exact sequence is

\[
0\longrightarrow E^{(1)}
\longrightarrow\operatorname{Sym}^pE
\longrightarrow\det(E)\otimes\operatorname{Sym}^{p-2}E
\longrightarrow0.
\]

Therefore, in the modular Grothendieck group,

\[
\boxed{
[\operatorname{Sym}^pE]
-[\det(E)\otimes\operatorname{Sym}^{p-2}E]
=[E^{(1)}].
}
\]

This is the local explanation for the exceptional Airy pair

\[
R_p=U_p-U_{p-2}(-1).
\]

It is also the algebraic shadow of Theorem 1: the `p`-th cyclic Adams character of `E` contracts, after modular Tate localization, to the Frobenius twist of the original rank-two object.

Pointwise, if `A` has eigenvalues `alpha,beta`, then

\[
\operatorname{Tr}(\sigma A^{\otimes p}|E^{\otimes p})
=\operatorname{Tr}(A^p|E)
=\alpha^p+\beta^p.
\]

Thus the cubic Airy Adams trace is naturally a cyclic tensor trace before taking compact support.

## 3. What the modular theorem does prove

The local characteristic-`p` class is genuinely rank two. This is not heuristic and not a statement about generic monodromy. It proves that the coincidence `k=p=char` has a canonical Frobenius-contraction mechanism at the modular fibre.

Together with Chuang's arithmetic Picard--Lefschetz theorem, the local specialisation data are complete:

- the invariant `k=p` moment loses exactly one Tate line;
- the `k=p-2` moment loses none;
- the remaining modular Adams class is the Frobenius contraction of the original Airy object.

The missing cancellation is therefore not another local vanishing cycle.

## 4. Why this does not yet bound the characteristic-zero trace

The required trace lives on an `ell`-adic or `p`-adic characteristic-zero Weil object. The Tate-diagonal theorem lives after reduction to characteristic `p` and in a two-periodic Tate/Smith category. That localization kills free cyclic orbits and records the Frobenius-twisted fixed part, but it forgets the characteristic-zero eigenvalue distribution of the killed part.

Consequently, the implication

\[
\text{modular Tate object has rank two}
\quad\Longrightarrow\quad
|\operatorname{Tr}(F|R_p)|=O(p^{(p+1)/2})
\]

is invalid without an integral lift theorem.

This is visible in the repository's exact Dwork audit. The natural integral connection lift has full surviving defect rank `(p-5)/6` after the `mu_3` projector, and its two residue covectors expand into `(p+1)/3` invariant Laurent endpoint classes before cohomological reduction. Thus the most direct integral lift does not have a bounded-rank cone. The modular rank-two collapse and the characteristic-zero global correlation are different assertions.

## 5. Exact sufficient lift theorem

Let `O` be a complete discrete valuation ring of residue characteristic `p`, large enough for the cyclic action, and let

\[
\mathscr M_p
=R\Gamma_c
\left(\mathbf A^1,
\mathscr A_O^{\otimes p}
\right)^{\mu_3}
\]

be a perfect `C_p`-equivariant integral Airy complex with Frobenius. Its generic cyclic trace realises the already proved Airy virtual trace, while its modular Smith/Tate localisation is governed by Theorem 1.

A sufficient theorem for the analytic crown is:

> **Integral Tate-diagonal lift theorem.** Construct a Frobenius-compatible comparison from the generic cyclic Adams trace of `M_p` to a lift of its Smith/Tate fixed-locus object such that, after removing Chuang's single Tate line, the comparison cone has uniformly bounded total generic rank, or more generally has Frobenius trace bounded by `C p^((p+1)/2)` with absolute `C`.

A bounded generic rank would suffice by purity: every remaining eigenvalue has absolute value `p^((p+1)/2)` after the common normalization.

The theorem must be integral. A comparison only after reduction modulo the maximal ideal, or only inside the Tate quotient, supplies congruences but no archimedean trace bound.

## 6. Precise obstruction

Existing cyclic Adams and Smith/Tate formalisms provide the modular Frobenius contraction but not a Weil-compatible bounded lift. Existing arithmetic Picard--Lefschetz theory provides the one local Tate correction but not the trace of the global comparison cone. The natural Dwork lift has linearly growing defect, so a bounded-cone theorem is false for that unmodified lift.

Therefore any successful analytic proof must do one of two genuinely new things:

1. construct a different integral Smith/Tate lift whose generic cone is bounded; or
2. prove absolute Frobenius cancellation inside the linearly growing cone left by the natural lift.

The second alternative is exactly the characteristic-`p` correlation theorem already isolated between `U_p^gen` and `U_{p-2}^gen(-1)`.

## 7. Ruling

### PROVED

- cyclic Tate cohomology of `V^(tensor p)` is the Frobenius twist of `V`;
- the rank-two modular Adams difference is the Frobenius contraction;
- the exceptional Airy correlation has a canonical modular mechanism;
- a modular or two-periodic Smith statement alone cannot control the characteristic-zero Frobenius trace;
- the natural integral Dwork lift has a linearly growing, not bounded, surviving defect.

### OPEN

- an integral Weil-compatible Tate-diagonal lift with bounded generic cone;
- absolute cancellation in the existing linear-rank cone;
- the bound
  \[
  |\operatorname{Tr}(F|R_p)|\le C p^{(p+1)/2};
  \]
- the crown.

The analytic wall is no longer merely “Katz uniformity at degree `p`”. It is an exact integral lifting problem from modular Frobenius contraction to characteristic-zero Weil trace.

## References

- M. K. Brown, C. Miller, P. Thompson and M. E. Walker, *Cyclic Adams Operations*, arXiv:1601.05072.
- S. Leslie and G. Lonergan, *Parity Sheaves and Smith Theory*, arXiv:1708.08174.
- T. Feng, *Smith Theory and Cyclic Base Change Functoriality*, arXiv:2009.14236.
- P.-H. Chuang, *On the Generalized Arithmetic Picard--Lefschetz Formula*, arXiv:2607.05757.
