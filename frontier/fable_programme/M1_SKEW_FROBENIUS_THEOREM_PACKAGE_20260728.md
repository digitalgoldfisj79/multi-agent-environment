# M1 execution: skew-Frobenius correspondence and integrable exclusions

Date: 28 July 2026

## 1. Skew-Frobenius correspondence

Let `p>3`, let `phi in F_p[X]` have degree less than `p`, and put

`f_phi(X)=X^p-phi(X)`.

Assume `f_phi` is squarefree. Let `R_phi` be its `p` roots in an algebraic closure.

### Theorem 1

On `R_phi`, arithmetic Frobenius is exactly the explicit polynomial map `phi`:

`Frob_p(alpha)=alpha^p=phi(alpha)`.

Consequently:

1. `phi` permutes `R_phi`;
2. the irreducible-factor degrees of `f_phi` are exactly the cycle lengths of `phi` on `R_phi`;
3. `f_phi` is irreducible if and only if this permutation is one `p`-cycle.

### Proof

The defining equation gives `alpha^p=phi(alpha)` at every root. Since `phi` has coefficients in `F_p`, it commutes with Frobenius. Hence Frobenius preserves the root set and agrees there pointwise with `phi`. For a squarefree polynomial over a finite field, irreducible factors are the Frobenius orbits on its roots, and their degrees are the orbit lengths. The three conclusions follow.

## 2. Bounded-period irreducibility criterion

Write `phi^[r]` for the `r`-fold compositional iterate.

### Corollary 2

The squarefree degree-`p` polynomial `f_phi` is irreducible if and only if

`gcd(f_phi, phi^[r](X)-X)=1`

for every `1 <= r <= floor(p/2)`.

### Proof

If `f_phi` is reducible, one irreducible factor has degree at most `p/2`. A root of that factor is fixed by `Frob_p^r`, and therefore by `phi^[r]`, for its factor degree `r`. Conversely, any common root of `f_phi` and `phi^[r]-X` lies in a Frobenius orbit of length dividing `r<p`, so `f_phi` cannot be irreducible.

This gives the fast dynamical irreducibility test used in the new census: iterate the low-degree map modulo `f_phi`, rather than repeatedly exponentiating a general polynomial.

## 3. Affine-conjugacy invariance

Let `L(X)=uX+v` with `u in F_p^*`, `v in F_p`, and define

`psi=L o phi o L^{-1}`.

### Theorem 3

The skew-Frobenius graphs for `phi` and `psi` are isomorphic under `L`. In particular, `X^p-phi(X)` and `X^p-psi(X)` have the same Frobenius cycle partition and are simultaneously irreducible or reducible.

### Proof

For `y=L(x)`, the identity `u^p=u`, `v^p=v` gives

`y^p=L(x)^p=L(x^p)`.

Thus `x^p=phi(x)` if and only if `y^p=L(phi(x))=psi(y)`. The map `L` is defined over `F_p`, so it respects Frobenius and its orbit lengths.

## 4. Rational fixed-point obstruction

### Theorem 4

If `phi(t)=t` for some `t in F_p`, then `X^p-phi(X)` is reducible: it has the rational factor `X-t`.

This elementary obstruction excludes entire integrable conjugacy classes.

### Corollary 5: power maps

For every `k>=1`, the map `phi(X)=X^k` fixes `0`. Hence `X^p-X^k` is reducible. Every `F_p`-affine conjugate of a power map is likewise excluded.

### Corollary 6: Dickson/Chebyshev maps

Let `D_k(X,1)` be the normalised Dickson polynomial satisfying

`D_k(z+z^{-1},1)=z^k+z^{-k}`.

It fixes `2`, because `D_k(2,1)=2`. Hence

`X^p-D_k(X,1)`

is reducible, as is every `F_p`-affine conjugate. In particular, the cubic Chebyshev map `X^3-3X` and the quadratic map `X^2-2` cannot supply crown witnesses.

## 5. Consequence for the crown family

For Paper V's depressed cubic family

`f_{a,c,d}(X)=X^p+aX^3+cX+d`,

the associated map is

`phi_{a,c,d}(X)=-(aX^3+cX+d)`.

Irreducibility is therefore a one-`p`-cycle statement for an explicit cubic map on its skew-Frobenius root set.

The proved exclusions show that standard power and Dickson/Chebyshev conjugacy classes are contained in the reducible locus. The crown must be carried by maps outside these elementary integrable classes.

## 6. Boundary

This package does not classify every dynamically special cubic map. In particular, no universal classification of all Lattes-type or postcritically finite cubic maps over varying `F_p` is asserted. Nor does large generic dynamical monodromy by itself prove that every prime admits a one-cycle parameter.

The next theorem-level target is a family statement on the non-special locus, such as positivity for a density-one set of primes or a monodromy theorem strong enough to count one-cycle specialisations with an effective error uniform in `p`.
