# Hodge obstruction to a characteristic-zero `k=p` versus `k=p-2` correspondence

**Date:** 2026-07-23  
**Scope:** cubic Airy moments underlying the function-field `d=1` programme.  
**Status:** the Hodge-disjointness statement is **PROVED**.

## 1. Sabbah--Yu's odd-moment Hodge spectrum

For odd `k`, Sabbah--Yu compute the finite-monodromic pure Hodge structure on

\[
H^1_{\mathrm{dR}}(\mathbb A^1,\operatorname{Sym}^k\mathrm{Ai}).
\]

It has weight `k+1`, every nonzero Hodge number equals one, and the first Hodge coordinates are

\[
\boxed{
\frac{k+2i}{3},
\qquad
1\le i\le\frac{k+1}{2}.
}
\]

The second coordinate is `k+1` minus the first.

Reference: Sabbah--Yu, *Hodge properties of Airy moments*, Theorem 1.1, arXiv:2112.13405.

## 2. Compare the adjacent moments at common weight

Take an odd prime `p`. The `k=p` moment has weight `p+1` and first coordinates

\[
A_p=
\left\{
\frac{p+2i}{3}:
1\le i\le\frac{p+1}{2}
\right\}.
\]

The `k=p-2` moment has weight `p-1`. After the Tate twist `(-1)` required by the determinant factor, it has weight `p+1` and first coordinates

\[
B_p=
\left\{
\frac{p-2+2j}{3}+1:
1\le j\le\frac{p-1}{2}
\right\}
=
\left\{
\frac{p+1+2j}{3}:
1\le j\le\frac{p-1}{2}
\right\}.
\]

If a Hodge type occurred in both spaces, its first coordinates would satisfy

\[
\frac{p+2i}{3}=
\frac{p+1+2j}{3},
\]

hence

\[
2(i-j)=1,
\]

which is impossible.

Therefore

\[
\boxed{A_p\cap B_p=\varnothing.}
\]

Since both structures are pure of the same weight, a morphism of Hodge structures must preserve each `(a,b)` summand. Thus

\[
\boxed{
\operatorname{Hom}_{\mathrm{HS}}
\left(
H^1_{\mathrm{dR}}(\operatorname{Sym}^{p}\mathrm{Ai}),
H^1_{\mathrm{dR}}(\operatorname{Sym}^{p-2}\mathrm{Ai})(-1)
\right)=0.
}
\]

## 3. Consequence for the geometric programme

Any algebraic correspondence over characteristic zero between the two global Airy-moment motives induces a morphism of their Hodge realizations. The displayed Hom group is zero, so such a correspondence acts trivially.

This rules out the proposed explanation

> the equal-rank special-fibre trace spaces are reductions of two globally paired characteristic-zero motives.

They are not. Their characteristic-zero Hodge spectra do not overlap.

## 4. Exact boundary of the result

This does **not** rule out:

- a correspondence existing only in characteristic `p`;
- a wild nearby-cycle identity at the exceptional boundary `k=p`;
- or a numerical Frobenius-trace cancellation without a motivic map.

It proves that any successful relation must be special to the coincidence

\[
k=\operatorname{char}(\mathbb F_p)=p.
\]

Such a relation cannot be obtained by spreading out a characteristic-zero geometric correspondence. It is genuinely new wild arithmetic.
