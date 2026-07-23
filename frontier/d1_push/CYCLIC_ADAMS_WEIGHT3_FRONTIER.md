# Cyclic-Adams bridge and the revised weight-three frontier

**Date:** 2026-07-23  
**Status:** exact trace reduction plus a sharply formulated sufficient theorem. The reduction replaces the all-degree irreducibility sieve by one p-th Adams defect on the root-negation descended cover. The required global weight-three bound remains open.

## 1. The descended universal cover

Fix `a in F_p^*`, put `m=(p-1)/2`, and define

`R_a(c,Y)=Y(Y^m+aY+c)^2`.

Over the base

`B=A^2_(c,e)`,

the equation

`R_a(c,Y)=e`

defines a finite degree-`p` cover. On the complement `U_a` of its discriminant, let `P_a` be the rank-`p` permutation sheaf on the roots.

By `ROOT_NEGATION_QUADRATIC_DESCENT_THEOREM.md`, its square-value fibres encode the original depressed slice exactly:

`N_a(p)=2 #{(c,e): e nonzero square, R_a(c,Y)-e irreducible}.`

The derivative and discriminant are

`dR_a/dY=(Y^m+aY+c)(3aY+c)`,

`Disc_Y(R_a-e)=(-1)^m 3a e^m(e-B_a(c))`,

with `B_a(c)=y_0(y_0^m+ay_0+c)^2`, `y_0=-c/(3a)`.

Thus the only finite branch divisors are `e=0` and `e=B_a(c)`.

## 2. The p-cycle detector as an Adams defect

Let `sigma in S_p` be the Frobenius permutation of one unramified fibre. The trace of the p-th Adams operation on a permutation representation is

`Tr(sigma | psi^p P)=Tr(sigma^p | P)`.

Because `p` is prime, a cycle of `sigma` contributes new fixed points to `sigma^p` only when it has length `p`. Therefore

### Theorem CAW.1 — exact fibre detector

`boxed( Tr(sigma | psi^p P-P)=p 1_(sigma is a p-cycle). )`

For a degree-`p` étale fibre, `sigma` is a p-cycle exactly when its defining polynomial is irreducible.

This is equivalent to, but more economical than, the complete alternating hook/configuration identity: the entire all-degree cycle sieve is one Adams defect.

## 3. Exact global count formula

Let `L_chi` denote the quadratic Kummer sheaf in the `e` coordinate. For `e!=0`,

`1+chi(e)`

is twice the indicator that `e` is a square. An irreducible finite-field polynomial is separable, so every irreducible fibre lies in the étale complement `U_a`. Combining RNQD.3 with CAW.1 gives:

### Theorem CAW.2 — exact Adams expression for the depressed count

`boxed( pN_a(p)`

` =sum_((c,e) in U_a(F_p))`

`   (1+chi(e)) Tr(Frob_(c,e) | psi^p P_a-P_a). )`

Equivalently, put

`A_a=(1 direct_sum L_chi) tensor (psi^p P_a-P_a)`

on `U_a`. Grothendieck-Lefschetz gives the exact identity

`boxed( pN_a(p)=Tr(Frob_p | RGamma_c(U_a,A_a)). )`

There is no correction term in this affine compactly supported formula. The two finite discriminant components and the divisor at infinity enter only when `U_a` is compactified in order to analyse and bound its cohomology.

## 4. Known extremal collapse

The pre-existing q-line decomposition has already evaluated every weight-zero and extremal weight-one term:

- the Kummer sector is elementary;
- the pair sector has an exact bounded q-average;
- the split D sector is one fixed rank-two CM K3 motive of discriminant `-24`;
- the nonsplit D sector is one fixed rank-two CM K3 motive of discriminant `-40`.

Thus the complete extremal contribution `E_ext(A)` is an explicit combination of elementary linear terms and two fixed weight-three CM coefficients. No growing-genus term remains there.

The only unknown is the primitive middle Adams defect `E_mid(A)`.

## 5. Correction of the expected scale

The earlier Middle Averaged Trace Lemma proposed

`|E_mid(A)|<=C p`.

That statement is still logically possible with a large constant, but the enlarged exact ledger through `p=199` no longer supports a small linear constant. The observed maximum is

`max |E_mid|/p =58.059880...` at `p=167`,

whereas

`max |E_mid|/p^(3/2)=4.492808...`.

The natural target is therefore weight three rather than weight two.

## 6. Revised sufficient theorem

### Cyclic-Adams Weight-Three Lemma (CAW3)

There are explicit absolute constants `C_3,C_2` such that, for every prime `p` and at least one square class `A in {+1,-1}`,

`boxed( |E_mid(A)| <= C_3 p^(3/2)+C_2 p. )`

This is enough for the crown. Indeed the exact selected-cell identity is

`p I_A=p M_A-E_ext(A)-E_mid(A)`,

with `M_A>=p-3` and `E_ext(A)=O(p)` explicitly. Hence

`p I_A >= p(p-3)-C_3p^(3/2)-O(p)>0`

for every sufficiently large `p`. The remaining finite range is decidable by the existing exact irreducibility counter.

CAW3 is strictly weaker than the obsolete fixed-rank `O(p)` aspiration and exactly matches the square-root fluctuation `N_a-p=O(sqrt p)`.

## 7. Proposed proof architecture

The terminal proof task is now:

1. use CAW.2 before expanding into hooks or factor degrees;
2. compactify the finite cover `R_a(c,Y)=e` together with the two explicit branch divisors;
3. apply cyclic-Adams/localization or an equivalent equivariant Lefschetz construction to the virtual sheaf `psi^p P_a-P_a`;
4. subtract the already identified extremal Kummer/pair/D classes;
5. show that the remaining compactly supported complex has weights at most three and uniformly bounded total Betti number;
6. apply Deligne's eigenvalue bound to obtain CAW3 with an explicit constant.

The crucial point is that the Adams defect must be localized before resolving the individual configuration degrees. Expanding first recreates the circular configuration identity and loses the cancellation.

## 8. Binary stop rule

This proposal has a terminal outcome.

- **Success:** the primitive Adams defect has uniformly bounded weight-three cohomology. CAW3 follows, and finite verification closes the function-field d=1 crown.
- **Failure:** the localized primitive Betti number grows with `p`, or an unavoidable weight-four component remains. Then the fixed-complexity geometric-collapse proposal is false and should be abandoned rather than refined indefinitely.

## 9. Epistemic classification

- Root-negation descended cover: exact theorem.
- Adams p-cycle detector: exact representation-theoretic identity.
- Exact global count formula: exact Grothendieck-Lefschetz identity on the étale complement.
- Complete extremal CM assembly: previously proved exact.
- Middle ledger through `p=199`: exact finite computation.
- Weight-three scaling: finite-data interpretation, not a theorem.
- CAW3 and uniform Betti bound: open.
- Function-field d=1 crown: open.
