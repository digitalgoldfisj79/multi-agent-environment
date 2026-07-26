# Hostile audit: p-cycle fixed-point circularity and q-line bridge

**Date:** 2026-07-26  
**Audited claim:** the alternating-hook p-cycle route is exact but circular, and its primitive trace is the invariant q-line wall in another normalization.  
**Verdict:** **PASS**, subject to the scope restrictions stated below.

## 1. Projector normalization

The critical normalization is correct. For a permutation with cycle lengths `lambda_j`,

\[
\det(1-tg\mid\operatorname{Std})
=\frac{\prod_j(1-t^{\lambda_j})}{1-t}.
\]

At `t=1` it is zero unless `g` is a single `p`-cycle, in which case it is `p`. The `p`-cycle class has `(p-1)!` elements, so the class average has coefficient

\[
\frac{p(p-1)!}{p!}=1.
\]

No factor is missing.

## 2. Correct fixed locus

The safe fixed-point calculation is on the affine Sawin variety `X_p`, not directly on the projective quotient `Y_p`. On `Y_p`, fixed points are semilinear up to projective scaling and diagonal translation. Ignoring those parameters would be a gap.

On `X_p`, an `F sigma`-fixed tuple is an ordered Frobenius orbit of one element of `F_(p^p)`. Since `p` is prime, the orbit has length `1` or `p`. Length `p` gives an irreducible polynomial and `p` choices of initial root. Length `1` gives `(T-a)^p`, one for each `a`. Hence `pI4+p` is exact.

## 3. Prime-power correction

The extra `p` is load-bearing. Omitting it changes the circularity formula by `1/(p-1)` and breaks integrality. It is exactly the contribution of the `p` polynomials `(T-a)^p`, each carrying von Mangoldt weight `1`.

## 4. Endpoint subtraction

The mid-hook trace does not equal the complete alternating-hook trace. The trivial term supplies the main term `p^4`; the sign term is the separately proved

\[
s_pp^2(p-1).
\]

After those endpoints are removed, the cone transfer supplies `p(p-1)T_mid`. The derived formula

\[
T_{mid}=\frac{I4+1-p^3}{p-1}-s_pp
\]

passes exact regression at every listed prime.

## 5. Orbit-count factors

For `a=0`, the established affine-orbit theorem gives

\[
(p-1)+p(p-1)N_2.
\]

For fixed `a nonzero`, translation depresses the quadratic coefficient and gives `p N_A`, not merely `N_A`. Multiplication by `(p-1)/2` square and nonsquare values gives

\[
\frac{p(p-1)}2(N_++N_-).
\]

The factors of `p`, `(p-1)`, and `1/2` all agree with the exhaustive census.

## 6. q-line factor of two

The q-line formula is

\[
N_A=(p-2)+B_A-\frac{S_0+A S_\chi}{2p}.
\]

Adding the two signs gives `-S0/p`, not `-2S0/p`. Substitution produces

\[
T_{mid}=p(N_2-3-s_p+(B_++B_-)/2)-S_0/2.
\]

The committed ledgers at `p=11,17,23` independently reproduce the aggregate trace.

## 7. Airy coincidence

The equality at `p=11`, `T_mid=p rho_p=22`, is real but accidental as a proposed uniform identity. Exact values at `p=17` and `p=23` disagree, and the `p=23` Airy normalization has denominator `23`. The audit therefore permits only the narrow conclusion that direct equality is false. It does not prove that no more complicated Fourier--Cayley relation exists.

## 8. What the theorem does not prove

It does not prove:

1. the crown;
2. a uniform bound on `S0`;
3. a parity correspondence on the primitive cohomology;
4. that a characteristic-`p` Smith-defect theorem cannot exist;
5. that all constructive or mass-formula approaches are impossible.

It proves that the particular sequence

\[
\text{hooks}\to p\text{-cycle trace}\to F\sigma\text{-fixed points}
\]

returns exactly to the unknown irreducible count and therefore supplies no independent saving.

## 9. Reproducibility ruling

The Python verifier checks the conjugacy-class projector, every algebraic bridge, exact sign coefficients, q-line regression, and the Airy mismatch. The C++ verifier exhaustively counts all `p^4` polynomials at `p=5,7,11,13,17,23` using a prime-degree Frobenius criterion. Its sector totals independently reconstruct `N2`, `N+`, and `N-`.

**Final hostile verdict:** the new theorem is a valid decisive stopping point. Further progress requires a genuinely new positivity, nonsaturation, Frobenius-correlation, Smith-defect, constructive, or mass-formula theorem; another projector or fixed-point rewrite is not progress.
