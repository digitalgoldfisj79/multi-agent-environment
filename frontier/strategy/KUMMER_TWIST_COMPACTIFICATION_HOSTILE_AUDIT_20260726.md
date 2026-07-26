# Hostile audit: Kummer twist and projective quotient compactification

**Date:** 2026-07-26  
**Audited file:** `KUMMER_TWIST_AND_PROJECTIVE_QUOTIENT_COMPACTIFICATION_OBSTRUCTION_20260726.md`  
**Verdict:** **PASS WITH ONE CORRECTED OVERCLAIM**. The Kummer and point-count theorems pass. Automatic transfer of general type through the isolated wild quotient point was removed and remains open.

## 1. Scalar-weight normalization

For scalar dilation `x -> lambda x`, the elementary coefficient `e_k` has weight `k`. On the fixed cubic slice, with `n=p-3`, the stabilizer `mu_n` therefore acts with weights

\[
a:0,
\qquad b:1,
\qquad c:2,
\qquad d:3
\pmod n.
\]

The transfer defining `y` has degree `n`, so `y` and `g=y^p-y` are invariant. This normalization is correct.

## 2. Kummer classification

Kummer theory gives

\[
H^1(\mathbf F_p,\mu_n)
=\mathbf F_p^*/(\mathbf F_p^*)^n.
\]

Because `gcd(n,p-1)=2`, the two classes are exactly square and nonsquare cubic coefficients.

In exponent notation, Frobenius coboundaries are even exponents because

\[
p-1\equiv2\pmod n.
\]

The sign element has exponent `n/2`. It is nontrivial exactly when `n/2` is odd, i.e. `p=1 mod 4`. Thus:

- for `p=1 mod 4`, the nonsquare class may be represented by the sign twist;
- for `p=3 mod 4`, the sign twist is cohomologically trivial and cannot exchange the two classes.

This is a load-bearing correction to the proposed programme and passes.

## 3. Common-quotient count

On the irreducibility level, `d != 0`. Since admitted primes have `gcd(3,p-3)=1`, no nontrivial scalar in `mu_(p-3)` fixes a point. The quotient is therefore a genuine torsor on the target level.

For each rational point of the common quotient, the fibre has one of the two classes in `H^1(F_p,mu_n)`. Exactly one arithmetic form trivializes that class. A trivialized fibre has

\[
\#\mu_n(\mathbf F_p)=2
\]

rational points. Hence

\[
\#D_p(\mathbf F_p)=\frac{N_++N_-}{2}
\]

and

\[
\#U_p(\mathbf F_p)=\frac{p-1}{2}(N_++N_-).
\]

No hidden factor of `p-3` is present: only the `F_p`-rational scalar stabilizer contributes, and it has order two.

## 4. Projective fixed locus

The permutation module in characteristic `p` is one Jordan block. On

\[
W=\ker(\text{augmentation})/\text{constants},
\]

the root cycle has one fixed line. A representative satisfies

\[
x_{i+1}-x_i=t,
\]

so the unique projective fixed point is the arithmetic progression

\[
[0,1,\ldots,p-1].
\]

The power-sum identities place this point on the sparse surface. There are no other fixed points for any nonidentity element because every such element generates `C_p`.

## 5. Split-locus audit

For a full cubic-tail polynomial, evaluation on `F_p` reduces to

\[
h(X)=aX^3+bX^2+(c+1)X+d.
\]

If `h` is nonzero, all distinct roots lie among at most three roots. When the derivative is nonzero, the reduced logarithmic derivative gives

\[
f'R=Pf
\]

with left degree at most five and right degree at least `p`. This excludes `p>5`.

If `h=0`, the sole projective configuration is `X^p-X`, the arithmetic-progression fixed point. If the derivative vanishes for another member, the roots are all equal and the diagonal class disappears in the translation quotient.

Thus there is no omitted free Frobenius-shift-zero orbit.

## 6. Compactified count

The proved affine-orbit theorem gives:

- `N_2` nonlinear quadratic affine orbits;
- `(N_++N_-)/2` nonlinear cubic affine orbits;
- one linear Artin--Schreier orbit, compactifying to the fixed point.

Each nonlinear orbit gives one rational quotient point for each nonzero Frobenius shift, hence `p-1` points. The linear orbit has full root-cycle stabilizer and contributes one coarse point, not `p-1` points.

Therefore

\[
\#\mathscr Q_p(\mathbf F_p)
=1+(p-1)\left(N_2+\frac{N_++N_-}{2}\right).
\]

The boundary and open formulas follow. The exact census at `p=7,11,13,17,23` passes all arithmetic regressions.

## 7. Corrected wild-canonical claim

The source `mathscr Y_p` is a smooth general-type complete intersection for admitted `p>=11`, and the quotient is free in codimension one with one isolated wild point.

It is **not** automatic in a modular constant-`C_p` quotient that:

1. the quotient is `Q`-Gorenstein;
2. canonical positivity descends across the isolated point;
3. a resolution has the same Kodaira dimension;
4. the singularity is Witt-rational or canonical.

Those assertions require a local invariant-ring/discrepancy calculation. The first draft overstated this and was corrected.

The source does have nonzero canonical sections, and every nonzero `C_p`-module in characteristic `p` has a nonzero invariant. This supplies a reflexive canonical form on the quotient smooth locus, but extension across a resolution remains part of the wild-local problem.

## 8. Literature applicability

The standard finite-field point congruence theorems require hypotheses not established here:

- regular proper models with positive-degree Hodge type at least one;
- or Witt-rational singularities plus the required zero-cycle condition.

More decisively, even if such a theorem supplied

\[
\#\mathscr Q_p(\mathbf F_p)\equiv1\pmod p,
\]

the exact ledger would give only

\[
W_p\equiv0\pmod p.
\]

This allows the failure value `W_p=0`. It also occurs at a positive exact example: `W_17=17`.

Thus the standard point-congruence route is arithmetically insufficient independently of the unresolved singularity hypotheses.

## 9. Relation to the q-line wall

The common quotient point count is exactly the class sum. The twisted Kummer local-system trace is the class difference. By the proved q-line ledger these are precisely the existing `S_0` and `S_chi` modes.

The compactification therefore supplies a correct geometric realization, but no smaller Frobenius space or weaker nonvanishing theorem.

## 10. Final ruling

### Passed

- Kummer rather than universal quadratic twisting;
- the exact sign-twist criterion;
- the common quotient and its factor of two;
- the unique projective fixed point;
- the no-free-split theorem;
- the compactified point-count formula;
- equivalence with the existing q-line sum/difference modes.

### Corrected

- automatic descent of general type through the isolated wild quotient point.

### Decisive stopping point

The proposed paired compactification programme does not reduce the crown. It returns to

\[
\#U_p(\mathbf F_p)>0
\iff
N_++N_->0,
\]

which is exactly invariant q-line nonsaturation. Further progress requires a genuinely new one-sided compactly-supported Frobenius theorem; another twist, compactification or standard point congruence is not progress.
