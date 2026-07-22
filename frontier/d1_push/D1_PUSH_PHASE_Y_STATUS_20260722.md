# d=1 crown push — Phase Y status: Cartier support counterexample

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Starting head:** `88ee34d3cd001c39565d06cbf85d8ed43f6ccf83`

## 1. Executive result

The filtered-minor programme reached stop condition 3.

The factorial-weighted grouped coefficient has an exact compact formula as a minor of the substitution matrix for

`X -> X+X^3`.

This explains the committed `p=17,19,23` cancellations. It also permits an exact search without assignment enumeration.

The proposed cancellation and support laws are false at `p=29`.

For the complete Cartier determinant,

`[c^224 d^112] det(I-H)=22 a chi_29(a)`,

with filtration weight

`448>420=(29^2-1)/2`.

The same coefficient is already present in the dominant `w=1` block. The `w=2,3,4` terms do not repair it.

## 2. Phase A — completed

For active row-degree set `N` and column-deficit set

`Q=(N\{p-3}) union {0}`,

the dominant coefficient matrix factors through

`E_(m,q)(a,c)=1/m! [X^q](cX+aX^3)^m.`

For a fixed degree set `M`, the factorial-weighted signed column-choice sum is exactly

`Gamma_(Q,M)=det(E_(m,q))_(m in M,q in Q).`

At `a=c=1`, this is a minor of the finite substitution/exponential-Riordan matrix

`B_(q,m)=1/m! [X^q](X+X^3)^m.`

Cauchy-Binet gives the full fixed-`I` identity-minor coefficient as a sum of `Gamma_(Q,M)` times falling-factorial alternants.

## 3. Phase B — completed and delimited

The selected excess witnesses have the following exact ledger.

| p | omitted n-values | assignments | degree sets | nonzero substitution minors | identity-minor coefficient |
|---|---|---:|---:|---:|---:|
| 17 | `{1,2,4}` | 476 | 2 | 0 | 0 mod 17 |
| 19 | `{1,2,5}` | 7,054 | 5 | 0 | 0 mod 19 |
| 23 | `{1,2,5,6,7}` | 332,192 | 18 | 0 | 0 mod 23 |
| 29 | `{1,2,4,5,7,8}` | 2,166,022,375 | 2,177 | 15 | 7 mod 29 |

Thus the common identity at `p=17,19,23` is modular vanishing of the appropriate substitution minors. It is not a uniform identity in `p`.

## 4. Phase C — target refuted

At `p=29`, the identity selection corresponding to omitted `n`-values

`{1,2,4,5,7,8}`

and cubic total `I=43` yields

`c^224 d^112`,

weight `448`, and identity-minor coefficient `7 mod 29`. After the exact cofactor and row signs, its Cartier contribution is `22 mod 29`.

Therefore no general dominant-`w=1` theorem can assert grouped coefficient cancellation above the proposed boundary.

## 5. Phase D — independent audit completed

Two exact implementations agree.

1. A standard-library Python dynamic programme plus Cauchy-Binet computation obtains the assignment ledger, all substitution minors, the coefficient `7`, and the signed contribution `22`.
2. A C++ two-stage multiplicative-Fourier extraction evaluates the complete Cartier determinant over both `F_29[s]/(s^2-2)` and `F_29[s]/(s^2-3)`.

The complete determinant gives `22` for square representative `a=1` and `14` for nonsquare representative `a=2`, in both field models.

## 6. Phase E — answered negatively

The same full-determinant extraction restricted to `w=1` gives exactly the same coefficients `22,14`.

Hence:

- the counterexample is genuinely dominant-`w=1`;
- lower blocks do not cancel it;
- the proposed full support law fails, not merely the per-degree-set strengthening.

## 7. What remains exact from earlier phases

Unaffected:

- weight-zero collapse;
- uniform pair and discriminant-curve identifications;
- split discriminant-24 and nonsplit discriminant-40 K3 formulas;
- complete extremal assembly;
- configuration trace cancellation and its circularity;
- dominant no-identity determinant formula;
- complete finite `p=23` support audit.

The `p=23` support statement remains true as a finite theorem. It is not the instance of a uniform support cutoff extending through `p=29`.

## 8. Strategic consequence

The present Cartier route cannot prove the crown by deleting every orthogonality survivor above `(p^2-1)/2`.

Any replacement must retain the above-bound tail and prove one of the following:

1. exact cancellation only after a broader assembly than the Cartier cofactor coefficient itself;
2. a controlled trace formula for the tail;
3. direct nonvanishing or positivity of the complete survivor sum without a hard support cutoff;
4. a different certificate for irreducibility.

No claim is made here that the crown is false. The counterexample applies to the proposed sufficient support theorem.

## 9. Epistemic classification

- Substitution-minor reduction: exact theorem.
- `p=17,19,23,29` grouped audits: exact.
- `p=29` full support counterexample: exact.
- Dominant-`w=1` uniform cancellation: refuted.
- Full Cartier support law: refuted.
- Boundary survivor-sum nonvanishing: open.
- General-prime function-field crown: open.
- Integer Fortune conjecture: open.
