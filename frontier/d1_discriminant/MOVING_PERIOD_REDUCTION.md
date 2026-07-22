# Effective moving-period reduction

**Date:** 2026-07-22  
**Status:** theorem derived from Elliott--Schost (2026, Theorem 1.1) and
Kaltofen's effective Noether forms.  The Elliott--Schost input is currently a
March 2026 arXiv preprint submitted to the Journal of Symbolic Computation.

## 1. Result

Let

`F_(a,c,d)(X)=X^p+aX^3+cX+d`, `a!=0`,

and let `N_(a,no[2,K],+)` count locally admissible members with positive
degree-p discriminant and no irreducible factor of any degree from 2 through
K.

### Theorem MPR.1 -- uniform reduction height

There is an effectively computable absolute constant C and, for every
`K>=3`, a nonzero integer `D_K` such that

`log |D_K| <= exp(C K (log K)^2)`

and every prime `p>K` not dividing `D_K` is a good-reduction prime for all
mixed marked-cycle, local-cubic and discriminant-Kummer covers of total
Bonferroni order at most

`L_K=min {odd L:L>=6(H_K-1)}`.

Here good reduction includes geometric irreducibility of every required
finite-field twist, not merely preservation of degree or equidimensionality.

In particular, every prime satisfying

`log log p > C K (log K)^2`

is good for the complete order-`L_K` Bonferroni system.

### Corollary MPR.2 -- explicit all-prime growing cutoff

There is an effectively computable constant `c>0` such that, for every
sufficiently large prime p, the choice

`K(p)=floor(c log log p/(log log log p)^2)`

satisfies, uniformly for every nonzero `a in F_p`,

`boxed(N_(a,no[2,K(p)],+) >= p^2/(24K(p)) > 0.)`

Thus every nonzero cubic slice contains a locally admissible,
positive-discriminant member whose smallest irreducible factor degree tends
to infinity at the explicit all-prime rate

`K(p) >> log log p/(log log log p)^2`.

This does not prove irreducibility: the parity reduction requires roughness
through `floor(p/3)`.

## 2. Integral model for one mixed cover

Fix a Bonferroni tuple

`j=(j_2,...,j_K)`, `sum j_k<=L=L_K`.

Put

`M=sum_(k=2)^K k j_k <= KL`.

It is enough to work at `a=1`.  For any `a!=0`, scaling X over the algebraic
closure gives a geometric isomorphism to the `a=1` model; hence geometric
irreducibility in every nonzero a-slice is equivalent.

For each selected k-cycle introduce coordinates

`x_(k,b,0),...,x_(k,b,k-1)`

and impose

`x_(k,b,i+1)=g(x_(k,b,i))`,

`x_(k,b,0)=g(x_(k,b,k-1))`,

where

`g(X)=-X^3-cX-d`.

These are M equations of total degree three in the M cycle variables and the
base variables c,d.

Let B be the product of the following integral factors.

1. **Exact period.** For every selected cycle, the differences
   `x_(k,b,0)-x_(k,b,r)`, `1<=r<k`.
2. **Distinct selected cycles.** For each pair of selected k-cycles, the k
   differences `x_(k,b,0)-x_(k,b',r)`.
3. **Unramified locus.** The cycle Jacobian factors
   `1-product_i g'(x_(k,b,i))`.
4. **Local cubic.** The fixed discriminant and root-coordinate diagonals of
   `Z^3+(c+1)Z+d`.
5. **Degree-p sign covers.** The fixed raw Kummer branch factors
   `c`, `Fplus`, `Fminus` from the signed-discriminant decomposition.

The number and total degree of these factors are bounded by

`O(M+KL^2)=O(K(log K)^2)`.

Adjoin one variable z and the equation

`zB-1=0`.

The resulting affine algebraic set `V_j` is exactly the required marked open
cover before the finite-field twist.  It is geometrically irreducible in
characteristic zero by the full direct-product monodromy theorem and the
proved independence of the local and Kummer covers.

The model has

`n_j <= C_1 KL`,

`s_j <= C_2 KL`,

`d_j <= C_3 KL^2`,

`h_j <= C_4 KL^2 log(KL)`,

for absolute effective constants.  The coefficient-height estimate follows
by expanding a product of `O(KL^2)` fixed-degree factors with bounded integer
coefficients.

Since `L=O(log K)`, this gives

`n_j=O(Klog K)`,

`log d_j=O(log K)`,

`log(h_j+2)=O(log K)`.

## 3. Preserving the Chow form under reduction

Elliott--Schost consider an arbitrary system

`F_1,...,F_s in Z[X_1,...,X_n]`

of degree at most d and logarithmic height at most h.  Their Theorem 1.1
constructs a nonzero integer `Delta_ES` such that, outside its prime divisors,
the primitive Chow forms of every equidimensional component reduce to the
Chow forms of the reduced system.  Their height estimate is

`log |Delta_ES|`

` <= C_ES n^14 s (h+1) d^(3n+4)`

for an effective absolute constant `C_ES`; writing `h+1` only removes the
irrelevant zero-height degeneracy in asymptotic notation.

Applied to `V_j`,

`log |Delta_ES,j| <= exp(O(K(log K)^2)).`

This prevents dimension jumps and ensures that the reduction of the
primitive Chow form of `V_j` is the Chow form of the unique dimension-two
component of the reduced model.  It does not alone prevent that Chow form
from factoring modulo p.

## 4. Preserving absolute irreducibility of the Chow form

Let `C_j` be the primitive Chow form of `V_j`.  Since `V_j` is geometrically
irreducible, `C_j` is absolutely irreducible.

The standard arithmetic Bezout bounds quoted and used by Elliott--Schost give

`deg(V_j)<=d_j^(n_j)`,

`h(V_j)<=d_j^(n_j)[n_j h_j+2n_j log(n_j+1)].`

For a dimension-two variety, `C_j` has

`q_j=3(n_j+1)` variables,

`D_j=3deg(V_j)` total degree,

and primitive coefficient height

`H_j<=h(V_j)+3log(n_j+2)deg(V_j).`

Consequently

`log D_j=O(n_j log d_j)=O(K(log K)^2)`,

`log(H_j+2)=O(K(log K)^2).`

Kaltofen's Theorem 7 supplies integral Noether forms for a degree-`D_j`
polynomial in `q_j` variables, of degree at most

`12D_j^6`

and coefficient 1-norm at most

`(2D_j)^[12D_j^7+12D_j^6 q_j+32D_j^6].`

Since `C_j` is absolutely irreducible, at least one such form has a nonzero
integer value `theta_j` on its coefficients.  Direct evaluation gives

`log |theta_j|`

` <= [12D_j^7+12D_j^6q_j+32D_j^6]log(2D_j)`

`    +12D_j^6 H_j`

` <= exp(O(K(log K)^2)).`

For every prime not dividing `theta_j`, the reduced primitive Chow form
remains absolutely irreducible.

Combining this with the Elliott--Schost integer shows that, outside the prime
divisors of

`Delta_j=Delta_ES,j theta_j`,

the reduced cover is pure of dimension two and geometrically irreducible.
Every finite-field twist is geometrically isomorphic to this cover after
base extension.  The cycle-coordinate actions are integral coordinate
permutations, and the local and Kummer actions are the standard integral
permutation and sign actions.  Therefore all twists needed by Chebotarev are
geometrically irreducible at the same primes.

## 5. Combining all Bonferroni covers

The number of tuples of total order at most L is

`N_(K,L)=binom(K-1+L,L).`

With `L=O(log K)`,

`log N_(K,L)=O((log K)^2).`

There are only a fixed number of local/sign twists per tuple.  Define `D_K`
as the product of all corresponding integers `Delta_j`, together with the
finitely many small denominators and leading coefficients used in the
integral models.

Then

`log |D_K|`

` <= N_(K,L) exp(O(K(log K)^2))`

` <= exp(O(K(log K)^2)).`

This proves Theorem MPR.1.

## 6. Combining reduction and point counting

`GROWING_CUTOFF_BONFERRONI.md` proves that a good prime p satisfies

`N_(a,no[2,K],+)>=p^2/(24K)`

once

`log p>=100Klog K`.

The new all-prime reduction condition

`log log p>C K(log K)^2`

is much stronger for large K, and therefore automatically implies the
point-count condition after enlarging C.

Put

`T=log log p`

and choose

`K=floor(cT/(log T)^2)`.

For sufficiently small effective c,

`K(log K)^2 <= T/C`.

Theorem MPR.1 and the Bonferroni point-count theorem then give Corollary
MPR.2.

## 7. What has and has not been made effective

The theorem removes the earlier moving-good-prime qualification.  It gives a
uniform all-prime order of magnitude for the roughness cutoff.

The absolute numerical constant is, in principle, computable by combining:

1. the explicit Maple inequality supplied with Elliott--Schost;
2. the displayed Kaltofen coefficient bounds;
3. the explicit model counts above;
4. the existing Cafure--Matera point-count threshold.

It has not been numerically expanded here.  The resulting threshold would be
far beyond practical computation and would not improve the scientific
content of the asymptotic rate.

The use of Elliott--Schost should be labelled accurately: as of this date it
is a recent preprint, not yet a peer-reviewed theorem in final journal form.
The derivation is unconditional conditional only in the ordinary scholarly
sense that it relies on the correctness of that cited theorem.

## 8. Remaining wall

The exact crown needs factor exclusion through `p/3`.  The achieved cutoff is

`K(p) >> log log p/(log log log p)^2`.

The ratio to the target still tends to zero extremely rapidly.  The next
obstruction is no longer bad reduction at fixed or slowly moving period.  It
is distribution at high periods.

No refinement of the present height bounds can bridge an iterated-logarithmic
cutoff to a linear cutoff.  The remaining viable multiplicative routes need
one of:

1. a lower-bound Frobenius sieve whose level is a positive power of p;
2. a direct estimate for the high-period tail `(K,p/3]`;
3. a structural argument showing that positive-discriminant reducible members
   cannot concentrate in that tail.

## 9. Primary inputs

- J. Elliott and E. Schost, *Primes of bad reduction for systems of
  polynomial equations*, arXiv:2603.02279, Theorem 1.1 and the Chow-form
  height bounds in Sections 3 and 5.
- E. Kaltofen, *Effective Noether Irreducibility Forms and Applications*, J.
  Comput. System Sci. 50 (1995), Theorem 7.
- `GROWING_CUTOFF_BONFERRONI.md` and
  `GROWING_CUTOFF_GEOMETRIC_AUDIT.md` for the marked-cycle models and the
  point-count lower bound.
