# Cartier dominant-w=1 coefficients as substitution minors

**Date:** 2026-07-22  
**Status:** exact algebraic reduction. It completes Phase A of the filtered-minor programme. The proposed uniform vanishing theorem is then refuted at `p=29`; see `P29_CARTIER_SUPPORT_COUNTEREXAMPLE.md`.

## 1. Identity-selected dominant block

Let `p>=5` be prime and

`G(X)=d+cX+aX^3`.

Fix an identity selection. In the falling-factorial coordinate put

`N={p-u : u is an active row}`

and

`Q=(N\{p-3}) union {0}`.

The dominant `w=1` identity minor is, up to the already-recorded global row and cofactor signs,

`D_(N,Q)(a,c,d)=det( [X^q]G(X)^n )_(n in N, q in Q).`

Rows and columns may be put in any fixed order; changing an order changes only the corresponding determinant sign.

## 2. Column-choice generating function

For `0<=m<=n`, choose `m` nonconstant factors from `G^n`. Then

`[X^q]G(X)^n`

`=sum_m (n)_m d^(n-m) * (1/m!)[X^q](cX+aX^3)^m.`

Define the substitution matrix

`E_(m,q)(a,c)=(1/m!)[X^q](cX+aX^3)^m.`

If

`q=m+2i`,

put

`j=m-i=(3m-q)/2`.

Then

`E_(m,q)(a,c)=a^i c^j/(i!j!)`

when `i,j` are nonnegative integers, and it is zero otherwise. Thus the required factorial weight, cubic degree, linear degree and falling-factorial degree are encoded in one coefficient of the truncated exponential power.

At `a=c=1`, write

`B_(q,m)=1/m! [X^q](X+X^3)^m`

`=1/(i!j!)`

with the same convention. This is the finite substitution, or exponential-Riordan, matrix for `X -> X+X^3`.

## 3. Exact Cauchy-Binet formula

Let

`F_(n,m)(d)=(n)_m d^(n-m).`

The coefficient matrix factors as

`([X^q]G^n)_(N,Q)=F_(N,{0,...,p-1})(d) E_({0,...,p-1},Q)(a,c).`

Therefore Cauchy-Binet gives

`D_(N,Q)(a,c,d)`

`=sum_(M, |M|=|N|) det((n)_m d^(n-m))_(n in N,m in M)`

`                         * det(E_(m,q)(a,c))_(m in M,q in Q).`

For a fixed cubic-factor total `I`, every contributing degree set satisfies

`sum M=sum Q-2I`.

The coefficient of

`a^I c^(sum Q-3I) d^(sum N-sum Q+2I)`

is consequently

`boxed( sum_M det((n)_m)_(N,M) * Gamma_(Q,M) )`,

where

`Gamma_(Q,M)=det(B_(q,m))_(q in Q,m in M)`

with the determinant orders chosen consistently.

This `Gamma_(Q,M)` is exactly the factorial-weighted signed sum of all compatible column choices producing the degree set `M`. Assignment enumeration is therefore unnecessary: the grouped scalar is a substitution-matrix minor.

## 4. Interpretation of the earlier cancellations

The committed examples become exact minor statements.

- `p=17`, omitted `N`-values `{1,2,4}`: `476` assignments, `2` degree sets, and both relevant substitution minors vanish modulo `17`.
- `p=19`, omitted `N`-values `{1,2,5}`: `7,054` assignments, `5` degree sets, and all five substitution minors vanish modulo `19`.
- `p=23`, omitted `N`-values `{1,2,5,6,7}`: `332,192` assignments, `18` degree sets, and all eighteen substitution minors vanish modulo `23`.

The associated falling-factorial alternants need not vanish. The cancellation in these cases is precisely modular vanishing of the substitution minors `Gamma_(Q,M)`.

## 5. Failure of uniform substitution-minor vanishing

At `p=29`, omit

`T={1,2,4,5,7,8}`

and take `I=43`. There are `2,166,022,375` compatible assignments in `2,177` degree sets. Exactly `15` relevant substitution minors are nonzero modulo `29`.

For example, for

`M={0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,23,24,25,26,27}`

one has

`Gamma_(Q,M)=25 mod 29`

and

`det((n)_m)_(N,M)=15 mod 29`.

Thus neither the grouped scalar nor the associated alternant vanishes.

The proposed theorem

> every above-bound grouped factorial coefficient vanishes modulo `p`

is false. The exact substitution-minor formula remains valid and is the correct algebraic explanation of the finite `p=17,19,23` cancellations.

## 6. Epistemic classification

- Column generating function: exact multinomial identity.
- Matrix factorization and grouped scalar determinant: exact Cauchy-Binet identity.
- `p=17,19,23,29` audit counts and residues: exact finite arithmetic.
- Uniform grouped-coefficient cancellation theorem: refuted at `p=29`.
- Full Cartier support law: refuted at `p=29`; see the counterexample file.
- Function-field crown and integer Fortune conjecture: not decided by this counterexample.
