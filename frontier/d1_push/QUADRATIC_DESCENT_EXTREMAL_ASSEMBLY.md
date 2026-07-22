# Split/nonsplit quadratic descent and the complete extremal trace ledger

**Date:** 2026-07-22  
**Status:** exact for the Kummer, pair-curve and `D`-curve sectors. The ordinary `D` average is evaluated by `D_FAMILY_TOTAL_SPACE_THEOREM.md`; the nonsplit reading is reduced to one fixed elliptic K3 surface with transcendental rank at most three.

## 1. Nonsplit descent operator

Fix a nonsquare `eta in F_p` and `s in F_(p^2)` with `s^2=eta`, so `s^p=-s`. The nonsplit normal-form polynomial is

`G_(q,d)(X)=X^p-(eta q)^(-1)X^3+3q^(-1)X+d`.

After `X=sz`,

`G_(q,d)(sz)=-(s/q)[qz^p+z^3-3z-q d/s]`.

Thus it is the split normal-form cover over `F_(p^2)`, restricted to the anti-invariant parameter line

`t=q d/(s(q-2))`, `t^p=-t`.

Arithmetic Frobenius on this line is therefore the split Frobenius followed by

`iota:(z,t)->(-z,-t)`.

This proves that every nonsplit survivor is the `iota*Frob` reading of the corresponding split geometric object.

## 2. Kummer sector

Put

`delta=chi(-1)`, `epsilon=chi((-1)^((p-1)/2)3)`.

For the split family the weight-zero survivor is

`k_+(q)=epsilon chi(q)`.

The nonsplit discriminant acquires the nonsquare factor `eta`, hence

`k_-(q)=-epsilon chi(q)`.

Over `Q^o=F_p^*\{2}`:

`K_+^0=-epsilon chi(2)`, `K_+^chi=epsilon(p-2)`,

`K_-^0= epsilon chi(2)`, `K_-^chi=-epsilon(p-2)`.

## 3. Pair sector and its descent

On

`B_q: 3s_1^2=12-d^2-4q d^(p-1)`,

the root-negation involution is `(s_1,d)->(-s_1,-d)`. If `sigma` is root swap, `sigma(s_1,d)=(s_1,-d)`, and `alpha` is the hyperelliptic involution, then `iota=alpha sigma`.

On `H^1(B_q)^-`, both `alpha` and `sigma` act by `-1`, so `iota` acts trivially. Therefore the split and nonsplit pair traces are identical.

Let

`B^0=sum_(q in Q^o) b(q)`, `B^chi=sum_(q in Q^o)chi(q)b(q)`.

The unweighted value `B^0` is the bounded formula of BQA. The weighted value is:

### Theorem QDEA.1

For `p=5`, `B^chi=-4`. For `p>5`:

- if `delta=1`,

  `B^chi=-p+(chi(2)chi(3)/2)(chi(5)-3)`;

- if `delta=-1`,

  `B^chi=chi(3)p-chi(3)+(chi(2)chi(3)/2)(chi(5)+1)`.

The proof is the same complete linear/Jacobi-sum evaluation as BQA, with one additional `chi(q)` weight. In particular `|B^chi|<=p+2`.

## 4. Ordinary D reading

Let

`D_+^0=sum_(q in Q^o) Tr(Frob|H^1(D_q))`,

`D_+^chi=sum_(q in Q^o) chi(q)Tr(Frob|H^1(D_q))`.

DTA.1 gives

`D_+^0=epsilon(-chi(-6)p-a_p(24.3.h.a)-delta-2chi(2)+2chi(6)).`

A second exact character-sum evaluation gives

### Theorem QDEA.2

`boxed(D_+^chi=epsilon(-delta p-3).)`

The CM coefficient disappears from the weighted average.

## 5. Nonsplit D reading

The polynomial `g_(q,+)(z)g_(q,-)(z)` is even. Write it as `H_q(r)`, `r=z^2`. The involution `iota_D:(z,w)->(-z,w)` splits

`H^1(D_q)=H^1(D_q)^+ direct_sum H^1(D_q)^-`,

and the nonsplit trace is

`d_-(q)=Tr(iota_D Frob|H^1(D_q)).`

For `r!=1`, put `e=chi(r)`. Directly from the two critical residual factors,

`H_q(r)=[r(qe+r-3)^2-(q-2)^2]/(r-1)^2`,

while `H_q(1)=3(q-2)/2`.

Only the nonsquare-r sector survives in the difference of the two quotient traces. Define

`F(q,r)=r(r-q-3)^2-(q-2)^2`.

Then

`d_-(q)/epsilon`

`=chi(q)[(1-delta)-2 sum_(chi(r)=-1) chi(F(q,r))].`

For `p>5`, summing the quadratic polynomial in q gives:

### Theorem QDEA.3

`boxed(D_-^chi=epsilon((p-1)chi(5)-p(1+delta)+2).)`

At `p=5`, `D_-^chi=4`.

For the unweighted total, define fixed surface character sums

`U_0(p)=sum_(q,r) chi(q F(q,r))`,

`U_1(p)=sum_(q,r) chi(rq F(q,r)).`

Then, for `p>5`,

`D_-^0/epsilon=U_1-U_0-chi(2)(p-1+chi(5))`,

and the rational-surface sum is exactly

`U_0=2chi(2)p+1`.

Hence

`boxed(D_-^0=epsilon[U_1-chi(2)(3p-1+chi(5))-1].)`

At `p=5`, `D_-^0=-4`.

## 6. The fixed K3 controlling U_1

The sum `U_1` is the affine character sum of

`Y^2=rq[r(r-q-3)^2-(q-2)^2]`.

Its binary-quartic invariants are

`I=q^2(q+3)(q^3+3q^2+51q+3)`,

`J=-q^3(2q^6+18q^5+207q^4+954q^3+3888q^2+2052q-54)`,

and

`4I^3-J^2=27q^7(q-2)^6(4q^2+9q+216).`

The Jacobian elliptic K3 has fibres

- `I_1^*` at `q=0`;
- `I_6` at `q=2`;
- two `I_1` fibres over the roots of `4q^2+9q+216`;
- `I_3^*` at infinity.

The trivial lattice has root part `D_5+A_5+D_7`, rank 17, so the Neron-Severi rank is at least 19 and the transcendental rank is at most 3. Consequently

`U_1(p)=p A_p+T_p+O(1)`

with `A_p` an explicit finite-character algebraic trace and `|T_p|<=3p`. In particular

`boxed(D_-^0=O(p))`

with an absolute effective constant. An exact modular identification of this rank-at-most-three K3 trace is not needed for asymptotic positivity, but remains available as a refinement target.

## 7. Fixed-a selection operator

For any component with split/nonsplit totals `X_+^0,X_+^chi,X_-^0,X_-^chi`, define

`Sel_A(X)=1/2(X_+^0+A X_+^chi)+1/2(X_-^0-delta A X_-^chi)`,

where `A=chi(a)`.

The completely identified extremal contribution to the virtual irreducibility trace is

`E_ext(A)=Sel_A(K)+Sel_A(B)-Sel_A(D)`.

All four inputs in this expression are now exact fixed-character formulas, except that the unweighted nonsplit D term is represented by the one fixed rank-at-most-three K3 trace above. There is no remaining growing-genus ambiguity in the extremal sector.

## 8. Epistemic classification

- Nonsplit descent operator: exact algebra.
- Kummer sign flip: exact discriminant calculation.
- Pair involution action and both q-averages: exact.
- Ordinary D totals: exact, including the fixed CM K3 coefficient.
- Nonsplit weighted D total and fixed-surface reduction: exact.
- K3 fibre configuration and transcendental-rank bound for U1: exact Tate-algorithm/Shioda-Tate consequence.
- Exact modular decomposition of U1: not claimed.
- Primitive middle-configuration contribution and general crown: open.
