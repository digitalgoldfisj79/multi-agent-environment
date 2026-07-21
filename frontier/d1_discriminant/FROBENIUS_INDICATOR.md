# Exact Frobenius determinant indicator

**Date:** 2026-07-21  
**Status:** exact theorem proved.

## 1. Setup

Let `p >= 5` be prime, let `a != 0` in `F_p`, and put

`F(X) = X^p + aX^3 + cX + d`.

Let

`A = F_p[X]/(F)`

and let `Phi(z)=z^p`. In the monomial basis

`1,X,...,X^(p-1)`,

let `B` be the matrix of `Phi-I`.

Delete the constant column and the row indexed by `X^(p-3)`. Let the resulting determinant be

`J_a(c,d)`.

## 2. Fixed space for nonreduced algebras

### Lemma FI.1

If

`F = product_i h_i^(e_i)`

is the factorisation into distinct monic irreducibles, then

`dim ker(Phi-I) = number of distinct h_i`.

### Proof

By the Chinese remainder theorem it suffices to treat

`A_i = F_p[X]/(h_i^(e_i))`.

Reduction modulo the nilradical maps a Frobenius-fixed element to an element of

`F_(p^(deg h_i))`

fixed by the p-power Frobenius, hence to `F_p`. Subtract that constant. The remaining element `n` is nilpotent and satisfies `n^p=n`. Iterating gives

`n^(p^k)=n`

for every k. For sufficiently large k the left side is zero, so `n=0`. Thus the fixed subspace of each primary factor is exactly one copy of `F_p`. QED.

### Corollary FI.2

The matrix B has rank `p-1` exactly when F has one distinct irreducible factor.

Because `deg F=p` is prime, this means either

1. F is irreducible of degree p; or
2. `F=(X-r)^p=X^p-r` for some r in `F_p`.

The second case is impossible in the present slice because `a != 0`. Therefore

`rank B = p-1 if and only if F is irreducible`.

This removes the squarefreeness hypothesis from the earlier determinant criterion.

## 3. Exact value on the irreducible locus

### Theorem FI.3

For every `c,d in F_p`,

`J_a(c,d) = 3a` if F is irreducible,

and

`J_a(c,d) = 0` otherwise.

Equivalently,

`J_a(c,d) = 3a * 1_(F irreducible)`

as an exact `F_p`-valued function on the coefficient plane.

### Proof

If F is reducible, Corollary FI.2 gives `rank B <= p-2`, so every `(p-1)`-minor vanishes.

Suppose F is irreducible. Over the algebraic closure, evaluate elements of A at the p roots of F. Let E be the Vandermonde evaluation matrix. In evaluation coordinates Frobenius is a permutation matrix P for one p-cycle, so

`B = E^(-1)(P-I)E`.

For an odd cycle,

`adj(P-I) = 1 1^T`,

where `1` is the all-ones column. One way to see this is that every cofactor of `I-P` is the unique directed spanning-tree count, equal to one; since `p-1` is even, replacing `I-P` by `P-I` does not change the adjugate.

Adjugates commute with conjugation, hence

`adj(B) = E^(-1) 1 1^T E`.

Now

`E^(-1)1 = e_0`,

because the constant polynomial evaluates to the all-ones vector, while

`1^T E = t`

is the algebra-trace row

`t_j = Tr_A/F_p(X^j)`.

Therefore

`adj(B) = e_0 t`.

The entry `adj(B)_(0,p-3)` is the cofactor obtained by deleting row `p-3` and column zero. Newton's identities give

`Tr(X^(p-3)) = 3a`.

Since `p-3` is even, the cofactor sign is positive. Thus the determinant of the selected minor is exactly `3a`. QED.

## 4. Consequences

Let

`N_a(p) = number of (c,d) in F_p^2 for which X^p+aX^3+cX+d is irreducible`.

Then in `F_p`,

`sum_(c,d) J_a(c,d) = 3a N_a(p)`.

Hence any proof that

`sum_(c,d) J_a(c,d) != 0 in F_p`

would immediately prove `N_a(p)>0` and therefore the d=1 function-field Fortune theorem for that cubic slice.

This is potentially much easier than estimating `N_a(p)` as an integer: only a nonvanishing congruence is required.

## 5. Top-coefficient reformulation

Every function on `F_p^2` has a unique canonical polynomial representative

`J_a^can(c,d)`

with degree at most `p-1` in each variable. Finite-field orthogonality gives

`sum_(c,d) J_a(c,d) = coefficient of c^(p-1)d^(p-1) in J_a^can`.

Indeed, the sum of `x^k` over `F_p` is zero for `0 <= k < p-1` and is `-1` for `k=p-1`; the two minus signs cancel.

Therefore the full d=1 theorem would follow from the single coefficient nonvanishing

`[c^(p-1)d^(p-1)] J_a^can != 0`.

This is now the sharpest determinant target. It replaces positivity of an approximately p-sized count by one exact coefficient calculation modulo p.

## 6. Verification

Exhaustive computation for both square classes of a at

`p=5,7,11,13`

shows that the determinant values are exactly

`{0,3a}`

and agree pointwise with an independent Rabin irreducibility test.

The existing small-prime counts are recovered from

`sum J_a/(3a)`.

## 7. Next target

Compute the canonical top coefficient structurally, without constructing the full determinant polynomial.

The relevant mechanisms to test are:

1. multilinearity of the determinant and finite-field orthogonality column by column;
2. Cauchy-Binet after writing the Frobenius columns as reductions of powers of the cubic `-aX^3-cX-d`;
3. a constant-term or resultant representation of the top coefficient;
4. affine invariance and reduction to the two square classes of a;
5. a recurrence for the top coefficient in p.

A nonzero closed formula for this one coefficient proves the function-field crown directly.