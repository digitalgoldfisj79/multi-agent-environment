# Exact critical factorization of the weighted descended cover

**Date:** 2026-07-23  
**Status:** exact algebra for every prime `p>=5`. The weighted root-negation cover has only two critical components, and their intersections reproduce the complete triple/quadruple collision inventory. This removes any unidentified finite critical component from the cyclic Thom–Sebastiani bridge.

## 1. Full weighted descended family

Put

`m=(p-1)/2`,

`H(Z)=Z^m+C+a v Z`,

where `v=r^(p-3)` is the tame normal parameter of the weighted corner. The descended cover is

`G_(a,v,C)(Z)=Z H(Z)^2=E.`

The central exceptional family is obtained at `v=0`.

## 2. Characteristic-p derivative identity

Differentiate:

`dG/dZ=H^2+2ZH(m Z^(m-1)+a v)`

`       =H[H+2m Z^m+2a v Z].`

Because

`1+2m=p=0`

in characteristic `p`, the bracket collapses:

`H+2m Z^m+2a vZ`

`=C+(1+2m)Z^m+3a vZ`

`=C+3a vZ.`

### Theorem DCF.1 — complete critical factorization

`boxed(dG/dZ=(Z^m+C+a vZ)(C+3a vZ).)`

Hence the critical scheme has exactly two components:

1. `H=0`;
2. `L:=C+3a vZ=0`.

No additional critical divisor exists, regardless of `p`.

## 3. The H component

On `H=0`,

`E=ZH^2=0.`

This is the familiar double-root branch. At a generic point its local inertia is a transposition, so the p-cycle Adams defect is zero. Its degenerations are included in the exact finite-collision theorem.

Thus `H=0` belongs entirely to the already removed finite branch/boundary ledger.

## 4. The linear component

On `L=0`,

`C=-3a vZ`

and

`H=Z^m-2a vZ=Z(Z^(m-1)-2a v).`

The critical value is therefore

`boxed(E=Z^3(Z^(m-1)-2a v)^2.)`

This gives an explicit two-variable parametrization of the only potentially primitive critical component.

## 5. Intersections of the two components

The intersection `H=L=0` is

`Z(Z^(m-1)-2a v)=0`,

so it consists of:

1. the persistent point `Z=0,C=0,E=0`;
2. for `v!=0`, the nonzero solutions

   `Z^(m-1)=2a v`,  `C=-3a vZ`,  `E=0`.

### 5.1 The persistent point

For `v!=0`, at `Z=0` one has

`H'(0)=a v`,

`L'(0)=3a v`.

Both critical factors vanish simply. Therefore `dG/dZ` has order two and `G-E` has order three: this is the triple-root/A2 collision corresponding to multiplicity partition

`3,2^((p-3)/2)`.

### 5.2 The nonzero intersections

At a nonzero solution of `Z^(m-1)=2a v`,

`H'=mZ^(m-1)+a v=(2m+1)a v=p a v=0`,

while

`L'=3a v!=0`.

For `p>5`,

`H''=m(m-1)Z^(m-2)!=0`,

so `H` has order two and `L` order one. Hence `dG/dZ` has order three and `G-E` order four. These are exactly the quadruple-root/A3 collisions with partition

`1,4,2^((p-5)/2)`.

The small prime `p=5` follows by direct substitution and is covered by the exact audit range.

## 6. Adams consequence

Neither a transposition, a triple collision, nor a quadruple collision contains a p-cycle in its local inertia. Therefore the Adams defect vanishes on:

- the generic `H=0` component;
- the persistent triple collision for finite `v!=0`;
- every nonzero quadruple collision.

This recovers the complete finite Adams-annihilation theorem directly inside the weighted corner model.

The only possible residual contribution is therefore created when the entire collision configuration specializes to `v=0`, where the central cover becomes linearized Artin–Schreier. That specialization is exactly the wild cyclic excess isolated in `LOCAL_FOURIER_RANK_FOUR_BRIDGE.md`.

## 7. Structural interpretation

The apparent degree-growing collision scheme is a tame Kummer family

`Z^(m-1)=2a v`

plus one persistent point. Every member is individually Adams-annihilated. Consequently a growing primitive Fourier rank cannot come from independent finite collision vanishing cycles. It could only arise from a genuinely wild failure of specialization at `v=0`.

The weighted Artin–Schreier theorem and endpoint classification show that the limiting wild representation is already explicit. The remaining bridge must compare the specialization map, not discover another critical family.

## 8. Epistemic classification

### Exact

- derivative factorization;
- two-component critical scheme;
- critical-value parametrization on `L=0`;
- complete intersection scheme;
- A2/triple type at `Z=0` for finite `v`;
- A3/quadruple type at nonzero intersections;
- agreement with the previously proved multiplicity partitions;
- Adams annihilation of every finite critical stratum.

### Open

- derived specialization from finite `v` to the Artin–Schreier fibre `v=0`;
- effective rank of the wild specialization cone;
- rank-four local Fourier theorem and conductor bound.
