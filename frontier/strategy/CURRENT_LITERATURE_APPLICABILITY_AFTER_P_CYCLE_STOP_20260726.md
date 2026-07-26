# Current literature applicability after the p-cycle stopping theorem

**Date:** 2026-07-26  
**Scope:** current prescribed-coefficient results that might conceivably imply the function-field `d=1` positivity statement.  
**Ruling:** no located theorem applies to the diagonal regime `q=n=p` with `p-4` prescribed leading coefficients.

## 1. Kolekar 2025/2026 affine-set preprint

Neil Kolekar, *Irreducible Polynomials with Coefficients in an Affine Algebraic Set*, arXiv:2512.08994, revised 22 March 2026, is the closest current result located.

Its main theorem assumes

\[
n<p,
\]

where `p` is the characteristic. The Fortune problem has

\[
q=n=p.
\]

It is therefore outside the theorem's hypotheses at the exact equality boundary.

This is not a cosmetic restriction. The proof's polarization-rank lemma recovers a degree-`n` homogeneous polynomial from its polarization using the factor `1/n!`; this fails when `n=p` in characteristic `p`. The paper's Question 5.1 explicitly asks whether the argument can be extended beyond this restriction, including by a p-adic method.

Hence the newest affine-algebraic-set bound does not supply the missing q-line nonsaturation theorem. Its stated future direction is essentially the same characteristic-`p` obstruction isolated in this repository.

## 2. Granger prescribed-leading-coefficient method

Robert Granger, *On the Enumeration of Irreducible Polynomials over GF(q) with Prescribed Coefficients*, Finite Fields and Their Applications 57 (2019), requires the polynomial degree `n` to be coprime to the characteristic for its general `l<p` algorithm and asymptotic formula.

Here `n=p`, so the method does not apply. The failure of the ordinary Newton/polarization machinery at degree divisible by the characteristic is precisely why the current programme uses modular Jordan, divided-power, Fourier--Cayley, and q-line constructions.

## 3. Other recent restricted-coefficient results

The 2025 papers on restricted coefficient sets and square coefficient distributions work in large-field or positive-density coefficient regimes. They do not cover a four-dimensional sparse family inside the `p`-dimensional coefficient space with `n=q=p`.

The general several-prescribed-coefficient theorems prescribe only a fixed positive fraction strictly below the number required here. Fortune prescribes `p-4` leading coefficients and leaves only four free coefficients, which is the opposite density regime.

## 4. Final literature ruling

The latest apparently relevant preprint reaches exactly to, but not across, the equality boundary `n=p`. No current result located proves existence in the Fortune sparse family or yields the required one-sided invariant q-line estimate.

The remaining theorem is therefore not hidden in the current prescribed-coefficient literature. It requires a new argument that survives the characteristic-divides-degree boundary: characteristic-`p` Frobenius correlation, integral/divided-power Smith control, an exact mass invariant, or a constructive orbit theorem.
