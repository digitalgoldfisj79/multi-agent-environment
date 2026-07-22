# Critical-value normal form and the two universal q-families

**Date:** 2026-07-22  
**Status:** exact algebraic reduction proved; exhaustive invariance checks passed through all completed primes of the all-a scan.

## 1. Fixed-c cubic cover

Fix `a,c in F_p` with `a c !=0`, and put

`phi_(a,c)(x)=x^p+a x^3+c x`.

Choose r in the quadratic closure such that

`r^2=-c/(3a)`.

Set

`epsilon=r^(p-1)=chi(-c/(3a)) in {+1,-1}`

and

`q=r^(p-3)/a`.

Since `r^p=epsilon r`,

`q=epsilon/(a r^2)=-3 epsilon/c`,

so `q in F_p^*` and is independent of the choice of sign of r.

Substitution `x=r z` gives

`phi_(a,c)(r z)=a r^3(q z^p+z^3-3z)`.

The critical points are `z=+1,-1`. If `q!=2`, division by the positive critical value `a r^3(q-2)` gives the normalized map

`boxed(f_q(z)=(q z^p+z^3-3z)/(q-2).)`

Its finite critical values are exactly

`f_q(1)=1`, `f_q(-1)=-1`.

The formula without the denominator remains valid at q=2, where the two critical values collide.

## 2. Parameter singularities

The normalized family has only the three parameter degenerations

- `q=0`, where the degree-p term disappears;
- `q=2`, where the two finite critical values collide;
- `q=infinity`, corresponding to `c=0`.

Thus the many collision points seen in the original c-coordinate are pullbacks of the single point `q=2` under the high-degree critical-root parameterization.

## 3. Universal square-root types

Fix once and for all a nonsquare `eta in F_p^*`.

### Split critical roots

If `epsilon=+1`, then `r^2` is a square. Scaling x by an element of `F_p^*` reduces the pair `(a,c)` to

`a=1/q`, `c=-3/q`.

Define

`n_+(q)=# {d in F_p :`
` X^p+q^(-1)X^3-3q^(-1)X+d is irreducible}.`

Every original fixed-c slice with epsilon=+1 has exactly `n_+(q)` irreducible constants.

### Nonsplit critical roots

If `epsilon=-1`, write `r^2=eta lambda^2` with `lambda in F_p^*`. Scaling by lambda reduces `(a,c)` to

`a=-1/(eta q)`, `c=3/q`.

Define

`n_-(q)=# {d in F_p :`
` X^p-(eta q)^(-1)X^3+3q^(-1)X+d is irreducible}.`

Every original fixed-c slice with epsilon=-1 has exactly `n_-(q)` irreducible constants.

Changing eta to another nonsquare only rescales X over `F_p`, so `n_-(q)` is independent of that choice.

### Theorem CVN.1

For every `a,c!=0`, the number of irreducible constants d depends only on

`(epsilon,q)=(chi(-c/(3a)),-3epsilon/c)`,

and is respectively `n_+(q)` or `n_-(q)`.

## 4. Exact reconstruction of a fixed-a slice

Put

`A=chi(a)`, `delta=chi(-1)`.

For epsilon=+1, substitution `c=-3/q` into the consistency condition

`chi(-c/(3a))=+1`

gives

`chi(q)=A`.

For epsilon=-1, substitution `c=3/q` gives

`chi(q)=-delta A`.

Let `N_(a,0)` be the number of irreducible constants on the exceptional line c=0. Then:

### Theorem CVN.2

`boxed(N_a(p)=N_(a,0)`
` + sum_(q!=0, chi(q)=A) n_+(q)`
` + sum_(q!=0, chi(q)=-delta A) n_-(q).)`

Equivalently, the crown is a linear combination of four q-sums:

`S_+^0=sum_(q!=0)n_+(q)`,

`S_+^chi=sum_(q!=0)chi(q)n_+(q)`,

`S_-^0=sum_(q!=0)n_-(q)`,

`S_-^chi=sum_(q!=0)chi(q)n_-(q)`,

plus the single c=0 fibre.

Explicitly,

`N_a=N_(a,0)`
` +(1/2)(S_+^0+A S_+^chi)`
` +(1/2)(S_-^0-delta A S_-^chi).`

## 5. Computational audit

An all-a, all-c, all-d `python-flint` scan grouped every fixed-c count by `(epsilon,q)`.

For every completed prime from 5 through 37:

- every group was a singleton;
- no dependence on a remained after fixing `(epsilon,q)`;
- the c=0 count depended only on the square class of a.

The run was stopped after the exact scaling proof made further all-a factorization redundant.

Hugging Face job: `6a605835d09dc1f57c6c148d`.

## 6. Sheaf-theoretic consequence

The two-dimensional coefficient-plane problem has been reorganized into two universal trace functions on the q-line. After normalization, each has finite singular set contained in

`{0,2,infinity}`.

The ordinary and quadratic-character sums in Theorem CVN.2 correspond to the untwisted and Kummer-twisted compactly supported cohomology of these two q-line objects.

A proof of bounds

`S_+^0=p+O(sqrt(p))`, `S_-^0=p+O(sqrt(p))`,

`S_+^chi=O(sqrt(p))`, `S_-^chi=O(sqrt(p))`

with absolute constants would give

`N_a(p)=p+O(sqrt(p))`

and prove the d=1 cubic crown after finite verification.

The remaining task is to construct the p-cycle virtual sheaf on these normalized families in a form whose total q-line conductor is O(p), not exponential in p.
