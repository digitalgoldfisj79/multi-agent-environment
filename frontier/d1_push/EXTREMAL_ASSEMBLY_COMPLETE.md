# Complete split/nonsplit extremal trace assembly

**Date:** 2026-07-22  
**Status:** exact. This supersedes the rank-at-most-three placeholder in `QUADRATIC_DESCENT_EXTREMAL_ASSEMBLY.md`. Every Kummer, pair-curve and D-curve average in both quadratic readings is now an explicit finite-character expression plus one of two fixed rank-two CM coefficients.

## 1. Notation

For a prime `p>=5`, put

`delta=chi_p(-1),`

`epsilon=chi_p((-1)^((p-1)/2)3),`

and write `a_p(f_(-24))` for the weight-three CM coefficient attached to the split D K3 of Neron-Severi discriminant `-24`, as in `D_FAMILY_TOTAL_SPACE_THEOREM.md`.

Write `a_p(f_(-40))` for the discriminant-40 coefficient defined in `NONSPLIT_K3_CM40_THEOREM.md`.

For a sector `X`, use

`X_+^0=sum_q x_+(q),`

`X_+^chi=sum_q chi(q)x_+(q),`

and similarly for the nonsplit reading `-`, with `q in F_p^*\{2}`.

## 2. Kummer sector

`K_+^0=-epsilon chi(2),`

`K_+^chi=epsilon(p-2),`

`K_-^0=epsilon chi(2),`

`K_-^chi=-epsilon(p-2).`

## 3. Pair sector

The root-negation descent involution acts trivially on `H^1(B_q)^-`, so split and nonsplit pair traces coincide.

The unweighted average is bounded absolutely:

- `B^0=0` at `p=5`;
- if `p>5` and `delta=1`,

  `B^0=chi(3)(chi(5)-5)/2`;

- if `p>5` and `delta=-1`,

  `B^0=chi(3)((3+chi(5))/2-chi(2)).`

The weighted average is

- `B^chi=-4` at `p=5`;
- if `p>5` and `delta=1`,

  `B^chi=-p+(chi(2)chi(3)/2)(chi(5)-3);`

- if `p>5` and `delta=-1`,

  `B^chi=chi(3)p-chi(3)+(chi(2)chi(3)/2)(chi(5)+1).`

## 4. Split D sector

The unweighted split average is

`D_+^0=epsilon[-chi(-6)p-a_p(f_(-24))
                 -delta-2chi(2)+2chi(6)].`

The weighted split average is elementary:

`D_+^chi=epsilon[-delta p-3].`

## 5. Nonsplit D sector

The weighted nonsplit average is

`D_-^chi=epsilon[(p-1)chi(5)-p(1+delta)+2]`

for `p>5`, with the separately audited value `D_-^chi=4` at `p=5`.

The former fixed rank-at-most-three term is now completely identified. For `p>5`,

`boxed( D_-^0=epsilon[a_p(f_(-40))
                       -chi(2)(p-1+chi(5))-1]. )`

At `p=5`, `D_-^0=-4`.

## 6. Fixed square-class selector

For `A=chi(a)` define

`Sel_A(X)=1/2(X_+^0+A X_+^chi)
          +1/2(X_-^0-delta A X_-^chi).`

The complete extremal contribution to the selected virtual irreducibility trace is

`boxed( E_ext(A)=Sel_A(K)+Sel_A(B)-Sel_A(D). )`

Every term on the right is now explicit.

For reference,

`Sel_A(K)=A epsilon(p-2)(1+delta)/2,`

`Sel_A(B)=B^0+A(1-delta)B^chi/2,`

and

`Sel_A(D)=1/2(D_+^0+A D_+^chi)
          +1/2(D_-^0-delta A D_-^chi).`

Thus the complete extremal sector consists only of:

- elementary multiples of `p` and quadratic characters;
- the fixed rank-two CM coefficient `a_p(f_(-24))`;
- the fixed rank-two CM coefficient `a_p(f_(-40))`.

There is no remaining growing-genus, growing-conductor or unidentified K3 term in the extremal sector.

## 7. What remains

The unresolved contribution is the primitive middle-configuration sector. `CONFIGURATION_TRACE_CANCELLATION.md` proves that its large degree-by-degree Tate terms cancel in the full alternating generating function, but also proves that the resulting trace identity is exactly the original irreducibility detector. Consequently no positivity estimate follows from configuration recursion alone.

The next genuinely independent target is therefore the Cartier determinant support/cancellation law and, beyond that, evaluation or nonvanishing of its survivor sum.

## 8. Epistemic classification

- All displayed extremal formulas: exact theorems from the cited files.
- CM coefficients: fixed rank-two singular-K3 motives with explicit binary-quadratic-form formulas.
- Selector algebra: exact.
- Middle primitive contribution: open.
- General function-field crown: open.
