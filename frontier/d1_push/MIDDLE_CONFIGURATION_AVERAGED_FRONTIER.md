# The final averaged middle-configuration frontier

**Date:** 2026-07-22  
**Status:** exact reduction. All weight-zero and extremal weight-one contributions have been evaluated or reduced to fixed-rank K3 motives. The only remaining generic-q obstruction is the primitive middle-configuration average.

## 1. Exact decomposition

For `A=chi(a)` and `delta=chi(-1)`, let

`Sel_A(X)=1/2(X_+^0+A X_+^chi)+1/2(X_-^0-delta A X_-^chi)`.

For the generic normal-form cells `q!=0,2`, write the selected virtual p-cycle trace as

`E_total(A)=E_ext(A)+E_mid(A)`,

where

`E_ext(A)=Sel_A(K)+Sel_A(B)-Sel_A(D)`

is the completely identified Kummer/pair/D ledger of `QUADRATIC_DESCENT_EXTREMAL_ASSEMBLY.md`, and `E_mid(A)` is the residual contribution of the primitive configuration hooks.

If `M_A` is the number of selected generic cells and `I_A` their total irreducible-fibre count, then

`p I_A = p M_A-E_total(A)`.

The omitted q=2 and c=0 boundary counts are nonnegative. Therefore `I_A>0` for either class proves the crown.

## 2. Sufficient averaged lemma

### Middle Averaged Trace Lemma (MATL)

There is an explicit absolute constant `C_mid` such that, for every prime p and at least one `A in {+1,-1}`,

`|E_mid(A)| <= C_mid p`.

The exact extremal ledger already has a fixed effective linear bound

`|E_ext(A)| <= C_ext p+C_0`

because:

- Kummer and weighted pair terms are elementary linear character sums;
- the ordinary D term is one rank-two CM K3 trace;
- the nonsplit D term is one K3 trace of transcendental rank at most three.

Since `M_A>=p-3`, MATL with `C_mid+C_ext<1197` proves `I_A>0` for every `p>=1200`; the existing machine crown handles `p<1200`. More generally, any explicit absolute constant completes the proof after extending the finite certificate to the corresponding threshold.

This is strictly weaker than proving semisimple rank/conductor O(p) before the q-average. Only one scalar Frobenius trace is required.

## 3. Exact configuration-space form

Let `C_k(q)` be the sign-isotypic H^1 of the ordered distinct k-root configuration curve. From `CONFIGURATION_CURVE_RECURSION.md`,

`sum_i (-1)^i H_i(q)=sum_(k=2)^(p-1)(p-k)(-1)^k C_k(q)`.

The k=2 term is the proved pair curve. The extremal sign-twist term containing `D_q` is also removed in `E_ext`. Thus `E_mid` is the selected q-average of the remaining primitive part of

`sum_(k=3)^(p-2)(p-k)(-1)^k C_k(q)`.

A proof of MATL should operate after this alternating sum and after the q-average. Estimating individual C_k is both unnecessary and exponentially wasteful.

## 4. Two-class projection

Adding the two square classes eliminates every chi(q)-weighted term:

`E_total(+)+E_total(-)=E_+^0+E_-^0`.

Under the exact nonsplit descent, this is the `(1+iota)` Frobenius projection for root negation. It is geometrically the involution-quotient sector of

`G_(a,c,e)(Y)=Y(Y^((p-1)/2)+aY+c)^2-e`.

This projection is a legitimate reduced target because the crown needs only one class. However, the exact residual probe shows that the middle quotient trace is not identically zero. A proof must bound or evaluate it; parity alone does not finish.

## 5. Exact finite residual diagnostic

After subtracting K, B and D, exact factorisation gives the following middle traces:

| p | E_mid(+) | E_mid(-) |
|---:|---:|---:|
| 5 | 0 | 0 |
| 7 | 0 | -26 |
| 11 | -80 | 24 |
| 13 | 49 | 77 |
| 17 | -51 | 151 |
| 19 | 22 | -10 |
| 23 | 148 | 54 |
| 29 | -210 | 22 |
| 31 | 196 | -360 |

The largest observed ratio is `|E_mid|/p=360/31<11.62`. This is strong evidence for MATL with a small constant, but it is not a proof.

## 6. Cartier face of the same cancellation

The Cartier cofactor identity gives

`S_a=sum_(c,d) C_3(F_(a,c,d))=3a N_a mod p`.

After coefficient orthogonality, only monomials

`c^(alpha(p-1)) d^(beta(p-1))`

survive. The exact computations suggest

`alpha+2beta <= (p+1)/2`.

A structural audit of the determinant support finds:

- the tropical assignment bound is strictly larger because its leading coefficient matrices are rank-deficient;
- for p=11,13 the only combinatorially possible support point above the claimed boundary is

  `(alpha,beta)=((p-9)/2,3)`;

- its coefficient vanishes separately in each of the three possible structural strata;
- the relevant entries are coefficient matrices of powers of the depressed cubic `aX^3+cX+d`, and satisfy the derivative recurrence

  `m[X^m]G^n=n(c[X^(m-1)]G^(n-1)+3a[X^(m-3)]G^(n-1))`.

This identifies a precise rank/Lindstrom-Gessel-Viennot cancellation mechanism caused by the missing X^2 term. A uniform proof of that boundary cancellation would prove the Cartier support law, but the support law alone does not yet evaluate `S_a`. It is therefore a parallel structural target, not a substitute for MATL.

## 7. External prescribed-coefficient bypass

General theorems on irreducible polynomials with prescribed coefficients do not apply directly. They allow a small number of coefficients to be fixed, whereas the present family fixes all coefficients from X^(p-1) through X^4 to zero. The degree and characteristic also coincide. The sparse constraint is the exceptional feature, not covered by the standard few-prescribed-coefficients asymptotics.

## 8. Precise next theorem

The highest-value statement is now:

`boxed( |E_mid(A)| <= C p for at least one square class A, with explicit absolute C. )`

The preferred proof architecture is:

1. take the alternating primitive configuration combination before cohomology;
2. apply the `(1+iota)` projection when summing the two classes;
3. compactify the total `(q, configuration)` space;
4. use deletion-contraction or an equivariant configuration generating function at `u=-1`;
5. show that all growing-dimensional boundary strata cancel, leaving a fixed list of surface motives.

The empirical D and B calculations show exactly what success should look like: large pointwise genera collapse after q-averaging to fixed K3/rational motives.

## 9. Stop rule reached in this run

The programme has removed every previously named obstruction except MATL. No remaining unidentified contribution comes from:

- weight zero;
- pair curves;
- the ordinary D family;
- nonsplit quadratic descent;
- q-Kummer signs;
- or the generic extremal curve list.

Continuing by fitting more fixed-q L-polynomials would not address MATL. A further advance requires a new global cancellation argument for the primitive total configuration space, or an equivalent uniform Cartier determinant identity.
