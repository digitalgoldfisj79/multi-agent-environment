# Exact q-average of the pair-curve weight-one trace

**Date:** 2026-07-22  
**Status:** exact theorem. The pair-curve contribution to the q-line assembly is uniformly bounded by `3`.

## 1. Setup

For prime `p>=5` and `q in F_p^* \ {2}`, let `B_q` be the pair curve from `EXTREMAL_WEIGHT1_CURVES_THEOREM.md`:

`3s^2=12-d^2-4q d^(p-1)`.

Let `sigma(d,s)=(-d,s)` and let `Q_q=B_q/<sigma>`:

`3s^2=12-r-4q r^m`, `m=(p-1)/2`.

The weight-one trace of the second hook is

`b_p(q)=Tr(Frob_p | H^1(B_q)^-)`.

Since `H^1(B_q)^+=H^1(Q_q)`,

`b_p(q)=#Q_q(F_p)-#B_q(F_p)`.

Define

`B_p=sum_(q in F_p^* \ {2}) b_p(q)`.

## 2. Point count for `B_q`

Write `chi` for the quadratic character of `F_p`, extended by `chi(0)=0`.

The affine point count is

`#B_q^aff(F_p)=p+sum_d chi((12-d^2-4q d^(p-1))/3)`.

For `d!=0`, `d^(p-1)=1`. Summing over `q!=0,2` and using the complete linear-character sum gives

`sum_q sum_d chi((12-d^2-4q d^(p-1))/3)`

`=p-1+chi(3)+2chi(-3)`.

Because the defining polynomial has even degree and leading coefficient `-4q/3`, the total number of points at infinity, summed over `q!=0,2`, is

`p-2-chi(-2/3)`.

Therefore

`sum_q #B_q(F_p)`

`=p^2-3+chi(3)+2chi(-3)-chi(-2/3)`.

## 3. Point count for the quotient

The affine quotient count is

`#Q_q^aff(F_p)=p+sum_r chi((12-r-4q r^m)/3)`.

For `r!=0`, `r^m=chi(r)`. For `p>5`, split the sum into squares and nonsquares. The two required Jacobi sums are

`sum_(r!=0) chi(r)chi(a-r)=-1` for `a!=0`.

The result is

`sum_q sum_r chi((12-r-4q r^m)/3)`

`=p-1 + (chi(3)/2)(1+chi(5))`.

If `p=1 mod 4`, the quotient polynomial has even degree and its summed infinity contribution is again

`p-2-chi(-2/3)`.

If `p=3 mod 4`, it has odd degree and contributes one point at infinity for each q, hence `p-2` in total.

Thus, for `p>5`,

`sum_q #Q_q(F_p)=`

- `p^2-3 + (chi(3)/2)(1+chi(5)) - chi(-2/3)` if `p=1 mod 4`;
- `p^2-3 + (chi(3)/2)(1+chi(5))` if `p=3 mod 4`.

The prime `p=5` is exceptional only because `20=0`; it is checked directly.

## 4. Closed formula

Subtracting the two point-count formulas gives:

### Theorem BQA

For `p=5`,

`boxed(B_5=0.)`

For every prime `p>5`,

`boxed(
B_p =
  chi(3)(chi(5)-5)/2,                         p=1 mod 4,
  chi(3)((3+chi(5))/2-chi(2)),                p=3 mod 4.
)`

In particular,

`boxed(|B_p|<=3.)`

## 5. Consequence for the crown programme

The uniform pair-curve survivor has rank `2 floor((p-1)/4)`, but its complete generic-q Frobenius trace has absolute size at most `3`. Its apparent `O(p)` pointwise Weil cost cancels exactly in the q-average.

Therefore the pair curve is harmless in the final constant battle. Any potentially fatal linear constant must come from:

- the genus-`p-3` twist curves `D_q`;
- primitive middle configuration factors;
- the boundary fibres `q=2,infinity`;
- or their split/nonsplit twist assembly.

This is the first exact general-p q-line trace calculation for a nontrivial weight-one survivor family.

## 6. Epistemic classification

- Curve identification and trace interpretation: exact theorem from `EXTREMAL_WEIGHT1_CURVES_THEOREM.md`.
- Character-sum evaluation: exact elementary finite-field calculation.
- Uniform bound `|B_p|<=3`: exact theorem.
- Analogous closed formula for `D_q` or all middle factors: open.
