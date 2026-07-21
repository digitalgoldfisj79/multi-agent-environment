# The O(p) target for signed quadratic incidence

**Date:** 2026-07-21  
**Status:** finite geometric audit specified; no O(p) theorem claimed here.

## 1. What the O(p^(3/2)) proof leaves

`SIGNED_QUADRATIC_INCIDENCE.md` expresses the signed incidence as a fixed linear combination of ordinary two-variable quadratic-character sums. The slicing proof loses a factor `sqrt(p)` because it bounds each one-variable fibre separately.

The observed signed incidences are much smaller. For both square classes of `a` and every prime through 293, the transformed exact formulas give

`max |L_(a,2)^chi|/p = 480/239 < 2.01`.

This is diagnostic only. It suggests that the weight-three cohomology cancels or vanishes.

## 2. Complete-sum surfaces

Every raw complete term has the form

`sum_(D,S) chi(Ue(D,S) D^d S^s L(D,S)^l Q(D,S)^q)`,

where

- `e` is plus or minus;
- `d,s,l,q` belong to `{0,1}`;
- `Ue` and `Q` have bidegree `(3,2)`;
- `L` has bidegree `(1,1)`;
- `D=0` and `S=0` are ruling lines.

After adding the required infinity rulings to make the branch class even, every surface is a double cover of `P^1 x P^1`. The maximal branch class is `(8,6)`.

The three nonlinear branch curves have one affine cusp each:

- `Uplus=0` at `(-1/2,7/2)`;
- `Uminus=0` at `(-7/2,1/2)`;
- `Q=0` at `(-1,3)`.

Their quadratic discriminants in `S` are

`Disc_S(Uplus) = 1296(2D+1)^2(4D+9)`,

`Disc_S(Uminus) = 432(2D+7)^2(4D+11)`,

`Disc_S(Q) = 20736(D+1)^3`.

All pairwise intersections with `S=0`, `L=0`, and each other are already encoded by the resultant ledger in `signed_quadratic_symbolic_audit.py`. The maximal complete arrangements to resolve are therefore only

`D S L Q Uplus = 0`

and

`D S L Q Uminus = 0`.

Every other complete surface is obtained by deleting components.

## 3. Root-incidence surfaces

Every raw root term is one of

`sum_(w,t) chi(A1(w,t) A2(w,t) t^r E(w,t)^e [w(w-4)]^v)`

or

`sum_(w,t) chi(B(w,t) t^r E(w,t)^e [w(w-4)]^v)`,

with `r,e,v` in `{0,1}`.

The maximal A-arrangement has branch components

`t`, `w`, `w-4`, `E`, `A1`, `A2`.

Its even completion has branch class `(8,8)`.

The maximal B-arrangement has components

`t`, `w`, `w-4`, `E`, `B`,

and already has branch class `(8,8)`.

The symbolic audit gives all discriminant and resultant factors. In particular:

`Disc_t(E) = -3(w-3)(w+1)`,

`Disc_t(A2) = -w^3(w-4)(2w-7)^2(4w^3-37w^2+122w-125)`,

and `Disc_t(B)` is the explicit factorization recorded in the audit script. Thus only these two maximal root arrangements require resolution.

## 4. Why irregularity is the exact issue

For a smooth double cover `pi:X->P^1 x P^1` with branch class `(2m,2n)`,

`pi_* O_X = O + O(-m,-n)`.

When `m,n > 0`, Kunneth gives `H^1(O_X)=0`; by duality the third l-adic cohomology also vanishes. The point-count trace is then `O(p)`.

Our covers are singular. If every singularity in the four maximal arrangements is rational, resolution preserves irregularity zero and all 48 raw sums are `O(p)`. Conversely, any possible `p^(3/2)` contribution must come from a non-rational branch singularity in one of those four arrangements.

Therefore no further global character manipulation is needed. The exact remaining task is a canonical-resolution ledger for four fixed branch divisors.

## 5. Required resolution ledger

For each maximal arrangement:

1. bihomogenise on `P^1 x P^1`;
2. list affine and infinity singular points;
3. record branch multiplicity and tangent cone at each point;
4. blow up every point of multiplicity at least two, updating the parity of the exceptional divisor;
5. continue until the branch divisor is normal crossing;
6. compute the correction to the double-cover line bundle;
7. verify `H^1(O(-L_final))=0`, equivalently that the resolved cover has irregularity zero.

If this ledger closes, then

`L_(a,2)^chi = O(p)`

with an absolute effective constant. If it fails, the ledger will identify the precise singularity carrying weight-three cohomology, and the required cancellation must then be sought between its character eigenspaces rather than term by term.