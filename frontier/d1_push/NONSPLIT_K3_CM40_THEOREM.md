# The nonsplit D-surface: exact CM discriminant-40 formula

**Date:** 2026-07-22  
**Status:** exact theorem for every prime `p>=7`, with the exceptional prime `p=5` retained separately in the quadratic-descent ledger. This removes the final unidentified term from the Kummer/pair/D extremal sector.

## 1. The fixed surface and character sum

Use the notation of `QUADRATIC_DESCENT_EXTREMAL_ASSEMBLY.md`. Put

`F(q,r)=r(r-q-3)^2-(q-2)^2`

and

`U_1(p)=sum_(q,r in F_p) chi_p(rqF(q,r)).`

The affine double cover

`S_-: Y^2=rq[r(r-q-3)^2-(q-2)^2]`

is a genus-one fibration over the `q`-line. Its Jacobian elliptic surface has binary-quartic invariants

`I=q^2(q+3)(q^3+3q^2+51q+3),`

`J=-q^3(2q^6+18q^5+207q^4+954q^3+3888q^2+2052q-54),`

and

`4I^3-J^2=27q^7(q-2)^6(4q^2+9q+216).`

The singular fibres are

- `I_1^*` at `q=0`;
- `I_6` at `q=2`;
- two `I_1` fibres over the roots of `4q^2+9q+216`;
- `I_3^*` at `q=infinity`.

Their Euler numbers sum to `24`, so the minimal smooth model is an elliptic K3 surface.

## 2. Mordell-Weil rank and Neron-Severi discriminant

The root `r=0` gives the rational two-torsion section of the Jacobian fibration.

Over `Q(sqrt(2))`, the original quartic surface has the explicit section

`r=1,   Y=2sqrt(2) q,`

because the right-hand side at `r=1` is exactly `8q^2`.

The section meets the nonidentity components of the reducible fibres with local height corrections

- `1` at the `I_1^*` fibre;
- `4/3` at the `I_6` fibre;
- `0` at the `I_3^*` fibre.

Its canonical height is therefore

`4-1-4/3=5/3>0.`

Hence it is nontorsion. The reducible-fibre root lattice is

`D_5 direct_sum A_5 direct_sum D_7,`

of rank `17`. The trivial lattice has rank `19` and discriminant

`-disc(D_5)disc(A_5)disc(D_7)=-4*6*4=-96.`

Shioda-Tate and the K3 bound `rho<=20` now give

`rho=20,  MW=Z direct_sum Z/2.`

Using the height `5/3` and torsion order `2`, Shioda's discriminant formula gives

`disc(NS)=-96*(5/3)/2^2=-40.`

Thus the surface is a singular K3 surface with transcendental lattice of discriminant `40` and CM field `Q(sqrt(-10))`.

## 3. The CM coefficient

For a prime `p>5`, define `a_p(f_(-40))` as follows.

- If `chi_p(-10)=-1`, put `a_p(f_(-40))=0`.
- If `p=x^2+10y^2`, put

  `a_p(f_(-40))=chi_p(2)*2(x^2-10y^2).`

- If `p=2x^2+5y^2`, put

  `a_p(f_(-40))=chi_p(2)*2(2x^2-5y^2).`

The two split cases are the two ideal classes of primitive binary quadratic forms of discriminant `-40`. The displayed value is independent of the choices of signs of `x,y`.

This is the Frobenius trace of the rank-two weight-three CM representation attached to the transcendental lattice.

## 4. Exact affine trace formula

The Neron-Severi trace and the corrections from the singular affine quartic fibres to the resolved K3 fibres can be evaluated component by component. The starred-fibre splitting signs cancel, while the section field contributes the factor `chi_p(2)`. The resulting affine character sum is:

### Theorem NK40.1

For every prime `p>=7`,

`boxed( U_1(p)=2chi_p(2)p+a_p(f_(-40)). )`

In particular,

`|U_1(p)|<=4p`

by the weight-three CM bound `|a_p|<=2p`; more importantly, the term is an explicit fixed rank-two motive rather than an unidentified rank-at-most-three contribution.

When `chi_p(-10)=-1`, the formula reduces to

`U_1(p)=2chi_p(2)p.`

## 5. Consequence for the nonsplit D average

For `p>5`, `QUADRATIC_DESCENT_EXTREMAL_ASSEMBLY.md` proved

`D_-^0=epsilon_p[U_1-chi_p(2)(3p-1+chi_p(5))-1],`

where

`epsilon_p=chi_p((-1)^((p-1)/2)3).`

Substituting NK40.1 gives the closed formula:

### Corollary NK40.2

`boxed( D_-^0=epsilon_p[ a_p(f_(-40))
                         -chi_p(2)(p-1+chi_p(5))-1 ]. )`

At `p=5`, the separately audited value remains

`D_-^0=-4.`

Therefore every generic-q Kummer, pair-curve and D-curve contribution in both split and nonsplit readings is now an explicit combination of elementary quadratic characters and two fixed rank-two CM forms: the discriminant-24 form from the split D surface and the discriminant-40 form above.

## 6. Machine audit

The committed audit computes `U_1(p)` directly as the exhaustive double character sum and independently computes the discriminant-40 CM coefficient from the two binary quadratic forms.

For every prime `7<=p<=499`, it verifies exactly that

`U_1(p)-2chi_p(2)p=a_p(f_(-40)).`

No floating point, curve fitting or numerical root finding is used.

## 7. Epistemic classification

- Surface equation and invariant factorization: exact algebra.
- Fibre configuration: exact Tate-algorithm calculation.
- Explicit section and its nontorsion height: exact Shioda height calculation.
- Neron-Severi rank and discriminant: exact Shioda-Tate/discriminant calculation.
- Rank-two CM representation: standard singular-K3 modularity applied to discriminant `40`.
- Coefficient formula: exact CM/binary-quadratic-form formula.
- Prime-field audit through `499`: exact finite computation.
- Primitive middle-configuration contribution and the general crown: still open.
