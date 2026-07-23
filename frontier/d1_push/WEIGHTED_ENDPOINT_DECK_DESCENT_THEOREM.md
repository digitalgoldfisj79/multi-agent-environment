# Weighted endpoint deck descent: only the quadratic quotient acts on the escaping pair

**Date:** 2026-07-23  
**Status:** exact algebraic theorem for every prime `p>=5`. On the degree-`p-1` Kummer cover of the `c`-line, the two escaping critical sections are permuted by the deck group only through its quadratic character. This proves that the geometric critical support at the weighted endpoint has fixed degree two. It does not by itself identify the Fourier–Adams specialization multiplicity carried by those sections.

## 1. Normalized endpoint family

Put

`e=(p-3)/2`

and consider

`F_tau(w)=w^p-w+a tau^(p-3)w^3=B`,

with

`tau^(p-1)=-1/c`.

The Kummer deck group is `mu_(p-1)`. For `zeta in mu_(p-1)`, define

`g_zeta:(tau,w,B) -> (zeta tau, zeta w, zeta B)`.

Since `zeta^p=zeta` and `zeta^(p-1)=1`,

`F_(zeta tau)(zeta w)=zeta F_tau(w)`.

Thus `g_zeta` is an exact automorphism of the normalized family over the original `c`-coordinate.

## 2. Critical sections

Choose `xi` with

`xi^2=(3a)^(-1)`.

For `tau!=0`, the two and only two critical sections are

`w_s(tau)=s xi tau^(-e)`,  `s in {+1,-1}`.

At the transformed parameter,

`w_(s')(zeta tau)=s' xi zeta^(-e)tau^(-e)`.

On the other hand,

`g_zeta(w_s(tau))=zeta s xi tau^(-e)`.

These are equal exactly when

`s'=s zeta^(e+1)`.

But

`e+1=(p-1)/2=:m`,

so `zeta^m` is the quadratic character of `zeta`. Therefore:

### Theorem WEDD.1 — quadratic branch action

`boxed(g_zeta sends branch s to branch s*chi(zeta).)`

Squares preserve each section and nonsquares interchange the two sections.

Equivalently, the permutation representation on the escaping critical pair is

`boxed(1 direct_sum chi_quad.)`

No character of order greater than two occurs in the geometric branch support.

## 3. Critical values

The critical values satisfy

`B_s(tau)=w_s(tau)^p-(2/3)w_s(tau)`.

The family automorphism gives

`B_(s chi(zeta))(zeta tau)=zeta B_s(tau)`.

After the weighted rescaling used in `WEIGHTED_ENDPOINT_ESCAPING_A1_THEOREM.md`, the two limiting critical values are `+xi^p` and `-xi^p`, hence remain separated. The deck action above is therefore the complete action on the stationary sections; no hidden collision orbit appears at the weighted limit.

## 4. Descent consequence

The critical support over the Kummer cover is the disjoint union of two sections. Its descent to the original `c`-line is the rank-two permutation object

`Q_l direct_sum L_chi`,

where `L_chi` is the quadratic Kummer line. This is the same trivial/quadratic decomposition obtained from the finite critical parabola

`c=-3a x^2`.

Consequently the growing tame quotient `C_m` cannot survive at the corner as a growing set of distinct geometric stationary sections. Any remaining `O(p)` tame augmentation must cancel or specialize through multiplicities on these two sections or through a punctual specialization defect.

## 5. Important limitation

For the geometric rank-one `A1` sign line `V`, oddness of `p` gives

`Psi^p(V)=V`

as a geometric finite-monodromy representation. Hence this theorem must **not** be read as saying that each section carries a nonzero ordinary class `Psi^p(V)-V`.

The nonzero endpoint term sought in the Fortune programme is a Fourier–specialization defect: Fourier transform, cyclic convolution and wild specialization do not reduce to applying the geometric Adams operation to an isolated sign line. Its multiplicity and Frobenius structure remain to be identified by the endpoint localization theorem.

## 6. Audit

`weighted_endpoint_deck_descent_audit.py` verifies exactly for every audited prime:

- `F_(zeta tau)(zeta w)=zeta F_tau(w)`;
- `e+1=(p-1)/2`;
- the branch-sign action `s -> s zeta^m`;
- preservation by squares and interchange by nonsquares;
- compatibility of the critical values.

## 7. Epistemic classification

### Exact

- Kummer deck automorphism of the normalized endpoint family;
- complete two-section critical locus;
- factorization of the deck action through the quadratic quotient;
- trivial-plus-quadratic descended critical support;
- absence of higher-order characters in the geometric stationary-section permutation.

### Open

- Fourier–Adams multiplicity carried by each section;
- Frobenius-equivariant wild specialization defect;
- zero-frequency punctual contribution;
- conductor-defect lemma and crown.
