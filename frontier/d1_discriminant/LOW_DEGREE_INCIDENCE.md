# Exact low-degree factor incidence in the d=1 cubic slice

**Date:** 2026-07-21  
**Status:** proved.

## 1. Setup

Let `p >= 5` be prime, let `a` be nonzero in `F_p`, and define

`F_(c,d)(X) = X^p + a X^3 + c X + d`.

For a squarefree polynomial `F`, let `nu_k(F)` be the number of monic irreducible degree-k factors of `F`.

## 2. Every irreducible quadratic is compatible

### Theorem LI.1

Let

`h_(s,n)(X) = X^2 - s X + n`

be monic irreducible over `F_p`. There is exactly one pair `(c,d)` for which `h_(s,n)` divides `F_(c,d)`, namely

`c = 1 - a(s^2 - n)`

and

`d = s(an - 1)`.

Consequently

`sum_(c,d in F_p) nu_2(F_(c,d)) = p(p - 1)/2`.

### Proof

In the quotient by `h_(s,n)`,

`X^2 = sX - n`

and

`X^3 = (s^2 - n)X - sn`.

If `theta` is a root, Frobenius exchanges the two conjugates, so

`theta^p = s - theta`.

Therefore, modulo `h_(s,n)`,

`X^p + aX^3 = [-1 + a(s^2 - n)]X + [s - asn]`.

The displayed `c,d` are the unique coefficients cancelling this linear remainder. Uniqueness also follows because a polynomial of degree at least two cannot divide a nonzero linear polynomial.

There are exactly `(p^2 - p)/2` monic irreducible quadratics. Summing one incidence for each gives the result. QED.

## 3. Frobenius-collinearity criterion

Let `h` be monic irreducible of degree `k >= 3`, let `theta` be one of its roots, and put

`y = theta^p + a theta^3`.

### Lemma LI.2

The polynomial `h` divides some `F_(c,d)` if and only if the three points

`(theta, y)`, `(theta^p, y^p)`, and `(theta^(p^2), y^(p^2))`

are collinear. Equivalently, the determinant of the three rows

`[1, theta, y]`, `[1, theta^p, y^p]`, `[1, theta^(p^2), y^(p^2)]`

vanishes. When this holds, `c,d` are unique.

### Proof

If `h` divides `F_(c,d)`, every conjugate point lies on the `F_p`-line

`Y = -cX - d`,

so the determinant vanishes.

Conversely, the first two conjugate points have distinct X-coordinates because `k >= 3`. Let `L` be their affine line. Vanishing of the determinant places the third point on `L`. Frobenius sends `L` to the line through the second and third points, which is again `L`. Thus `L` is Frobenius-stable and has equation `Y = -cX - d` with `c,d` in `F_p`. Hence `F_(c,d)(theta) = 0`, and irreducibility of `h` gives divisibility. QED.

## 4. Exactly one compatible cubic per translation orbit

Let `h` be monic irreducible cubic with Frobenius-ordered roots

`theta_0 = theta`, `theta_1 = theta^p`, `theta_2 = theta^(p^2)`.

Set

`e_1 = theta_0 + theta_1 + theta_2`,

`e_2 = theta_0 theta_1 + theta_0 theta_2 + theta_1 theta_2`,

and

`V = (theta_1 - theta_0)(theta_2 - theta_0)(theta_2 - theta_1)`.

The Frobenius permutation is a 3-cycle, so `V` is a nonzero element of `F_p`.

### Lemma LI.3

The compatibility determinant of Lemma LI.2 equals

`3e_2 - e_1^2 + a e_1 V`.

### Proof

For degree three, the next Frobenius conjugate after `theta_2` is `theta_0`. Expanding the determinant separates it into the determinant with third coordinate `theta_(i+1)` and `a` times the determinant with third coordinate `theta_i^3`.

The first determinant is `3e_2 - e_1^2`. The alternating cubic determinant is `V e_1`. QED.

Translate every root by `t` in `F_p`. Then

`e_1(t) = e_1 + 3t`,

`e_2(t) = e_2 + 2te_1 + 3t^2`,

and `V(t) = V`.

Therefore `3e_2(t) - e_1(t)^2` is invariant, while the compatibility determinant becomes

`C_h(t) = C_h(0) + 3aVt`.

Since `3aV` is nonzero, exactly one `t` makes the determinant vanish.

### Theorem LI.4

Every translation orbit of monic irreducible cubics contains exactly one polynomial dividing a member of the slice `F_(c,d)`. Consequently

`sum_(c,d in F_p) nu_3(F_(c,d)) = (p^2 - 1)/3`.

### Proof

The calculation above gives exactly one compatible translate per orbit. Translation acts freely on monic irreducible cubics for `p >= 5`: a nonzero translation-invariant root set would contain a full additive orbit of size `p`, impossible for a cubic.

The number of monic irreducible cubics is `(p^3 - p)/3`. Every translation orbit has size `p`, so the number of compatible cubics is `(p^2 - 1)/3`. Each contributes one degree-3 factor incidence. QED.

## 5. Sieve interpretation

The first two unconditioned incidence levels are exact:

`sum nu_2(F_(c,d)) = p^2/2 + O(p)`

and

`sum nu_3(F_(c,d)) = p^2/3 + O(1)`.

These are the degree-2 and degree-3 cycle-density main terms expected from random factorization, but here they follow from elementary algebra and Frobenius geometry.

For the parity-breaking sieve, the next quantities are the locally admissible and discriminant-weighted versions

`L_(a,k) = sum_((c,d) in A_a) nu_k(F_(c,d))`

and

`L_(a,k)^chi = sum_((c,d) in A_a) chi(Disc F_(c,d)) nu_k(F_(c,d))`,

for `k = 2,3`.

Theorems LI.1 and LI.4 reduce both to fixed two-variable character sums. Proving

`L_(a,2) = p^2/6 + O(p^(3/2))`

and

`L_(a,3) = p^2/9 + O(p^(3/2))`

with corresponding signed estimates is now a finite Weil-sum problem. Sharpening those errors to `O(p)`, and extending the incidence control multiplicatively, is the next sieve layer.
