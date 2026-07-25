# Rank-four Adams standard-realization no-go

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** conductor gate for the Kummer-projected Hayes Adams object.  
**Status:** **PROVED**.

## 1. Adams operation in the representation ring

Let `V` have rank four. The `p`-th Adams operation has the hook-Schur expansion

\[
\boxed{
\Psi^p(V)
=
\sum_{j=0}^{3}(-1)^j
S_{(p-j,1^j)}(V).
}
\]

This is the standard Newton/Schur realization of the power-sum character

\[
g\longmapsto\operatorname{Tr}(g^p|V).
\]

Its virtual rank is four, because Adams operations preserve rank.

## 2. Exact actual ranks

The Weyl dimension formula for `GL_4` gives

\[
\dim S_{(p)}(V)
=
\frac{(p+1)(p+2)(p+3)}6,
\]

\[
\dim S_{(p-1,1)}(V)
=
\frac{(p-1)(p+1)(p+2)}2,
\]

\[
\dim S_{(p-2,1,1)}(V)
=
\frac{(p-2)(p-1)(p+1)}2,
\]

and

\[
\dim S_{(p-3,1,1,1)}(V)
=
\frac{(p-3)(p-2)(p-1)}6.
\]

Therefore the sum of the ranks of the positive and negative terms is

\[
\boxed{
\sum_{j=0}^{3}
\dim S_{(p-j,1^j)}(V)
=
\frac{4p(p^2+2)}3.
}
\]

This grows cubically with `p`.

## 3. Consequence for the Hayes programme

For the rank-four universal Hayes sheaf `H_B`, the canonical realization of

\[
\Psi^p(\mathscr H_B)
\otimes
(\mathcal L_\chi-1)
\]

has total termwise generic rank

\[
\frac{8p(p^2+2)}3.
\]

Applying Deligne separately to these actual Schur-functor terms and then using the triangle inequality necessarily introduces a polynomially growing constant. It cannot prove the required absolute-constant estimate.

Thus the following inference is invalid:

> `H_B` has rank four, Adams preserves virtual rank, therefore the Adams parameter-plane complex has bounded Betti numbers.

Virtual rank cancellation does not control actual cohomological complexity.

## 4. Exact surviving gate

A successful Hayes proof must establish one of:

1. an actual bounded-complexity geometric realization of the **signed Kummer-projected combination** that is not the standard Schur realization;
2. an object-level cancellation between the four hook-Schur terms before applying Deligne;
3. a direct trace estimate exploiting orthogonality across the parameter plane without bounding the Schur terms separately.

Without one of these, the simple bounded-rank sheaf route is closed.

## 5. Ruling

### Closed

- deriving the terminal estimate from the rank-four fibre bound alone;
- applying Deligne termwise to the standard Adams/Schur expansion with an absolute constant;
- identifying virtual rank zero with bounded actual Betti complexity.

### Open

- nonstandard characteristic-`p` cancellation in the Kummer-projected Adams complex;
- direct parameter-plane orthogonality;
- the equivalent projective character theorem.