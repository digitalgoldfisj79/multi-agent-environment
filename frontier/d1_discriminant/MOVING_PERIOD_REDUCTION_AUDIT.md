# Audit of the effective moving-period reduction

**Date:** 2026-07-22  
**Verdict:** the iterated-logarithmic all-prime cutoff follows from the stated
external theorems; three qualifications must remain explicit.

## 1. Logical chain

For each mixed Bonferroni tuple j:

1. characteristic-zero monodromy proves that the marked open cover `V_j` is
   geometrically irreducible and pure of dimension two;
2. the cover has an integral cycle-coordinate model with
   `n=O(Klog K)`, `d=O(K(log K)^2)` and polynomial logarithmic height;
3. Elliott--Schost gives an integer `Delta_ES,j` outside whose prime divisors
   the primitive Chow form of `V_j` reduces to the Chow form of the reduced
   dimension-two component, with no additional-dimensional components;
4. Kaltofen gives a nonzero integer `theta_j` outside whose prime divisors the
   reduced primitive Chow form remains absolutely irreducible;
5. an irreducible Chow form is equivalent to geometric irreducibility of the
   equidimensional algebraic set;
6. finite-field twists are geometrically isomorphic to the reduced cover and
   use integral coordinate-permutation/sign actions;
7. multiplying the finitely many integers over all tuples gives `D_K`.

No step uses a choice of a prime after `D_K` has been constructed.

## 2. Why Elliott--Schost alone is insufficient

Their good-reduction theorem preserves primitive Chow forms as Chow forms of
the reduced equidimensional components.  A primitive Chow form that is
irreducible in characteristic zero can in principle factor after reduction,
and the factored polynomial would then be the Chow form of a reducible
reduced component.

Therefore the claim

`Elliott--Schost good => geometrically irreducible reduction`

is false without an additional irreducibility certificate.

Kaltofen's Noether forms supply exactly that certificate.  If `C_j` is the
primitive Chow form and `Phi(C_j)=theta_j!=0`, then

`p does not divide theta_j`

implies that the reduced Chow form is absolutely irreducible.  Combining the
two integers is necessary and sufficient for the argument used here.

## 3. Height scale re-derived

Write

`m=KL=O(Klog K)`.

The open-locus product has degree

`q=O(KL^2)=O(K(log K)^2)`.

Using one Rabinowitsch variable gives

`n=O(m)`, `d=O(q)`, `h=poly(K)`.

Hence

`n log d=O(K(log K)^2)`.

Elliott--Schost:

`log |Delta_ES,j|`

` <= O(n^14 s(h+1)d^(3n+4))`

` <= exp(O(K(log K)^2)).`

Arithmetic Bezout:

`deg V_j<=d^n`,

`h(V_j)<=d^n poly(n,h)`.

For the dimension-two Chow form:

`D_j<=3d^n`,

`H_j<=d^n poly(n,h)`.

Kaltofen:

`log |theta_j|`

` <= O(D_j^7log D_j+D_j^6q_jlog D_j+D_j^6H_j)`

` <= exp(O(K(log K)^2)).`

The tuple count satisfies

`log binom(K-1+L,L)=O((log K)^2)`,

so multiplication over all tuples leaves the same scale:

`log |D_K|<=exp(O(K(log K)^2)).`

Therefore every bad prime is at most

`exp(exp(O(K(log K)^2)))`,

and

`log log p >> K(log K)^2`

is sufficient for all-prime good reduction.

## 4. Uniformity in the cubic coefficient a

The proof constructs the integral model at `a=1`.  For every nonzero a, the
fixed-a dynatomic, local-cubic and raw Kummer covers are geometrically
isomorphic over the algebraic closure after scaling the dynamical coordinate.
Geometric irreducibility is therefore identical in all nonzero a-slices.

This is a geometric statement only.  It does not assert that the scaling is
defined over `F_p`, nor is that required for geometric connectedness or for
the geometric irreducibility of a finite-field twist.

## 5. Open-locus encoding

The exact-period and distinct-cycle conditions can be encoded with one
Rabinowitsch equation `zB-1`.

- exact period: exclude coordinate repetitions within a cycle;
- distinct selected cycles: exclude equality with every cyclic rotation;
- etale locus: exclude `1-(g^k)'(x_0)=0`;
- local and Kummer branch loci: exclude the fixed discriminant factors.

The number and degree of these factors are `O(KL^2)`.  Expanding their product
may create exponentially many terms, but coefficient size grows only
exponentially in that number; its logarithmic height is polynomial in K.  This
is exactly the height parameter required by the external theorem.

## 6. Scholarly qualification

Elliott--Schost, arXiv:2603.02279, was submitted in March 2026 and is not yet
a final peer-reviewed publication.  The result is explicit and accompanied
by code generating its full inequality, but the present theorem inherits the
ordinary dependency on the correctness of that recent preprint.

Kaltofen's 1995 theorem is published and supplies explicit degree and
coefficient bounds for the Noether forms.

## 7. Mathematical limitation

The achieved cutoff

`K(p) >> log log p/(log log log p)^2`

is far below the required `p/3`.  The result settles moving-period bad
reduction at an explicit order of magnitude; it does not materially reduce
the high-period distribution problem.

The next programme should not spend effort improving the absolute constants
in `D_K`.  Even a dramatic height improvement would remain polylogarithmic or
iterated-logarithmic in p.  The crown requires a different distribution
mechanism for periods comparable with p.
