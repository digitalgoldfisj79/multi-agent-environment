# d=1 crown push — Phase Z5 Adams/descent breakthrough status

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** one new exact geometric descent, one new exact one-variable recurrence, and one exact cyclic-Adams count identity have been proved. The previous small-constant `O(p)` middle-trace expectation has been replaced by a weaker sufficient `O(p^(3/2))` theorem. The general function-field d=1 crown remains open.

## 1. Executive assessment

This phase produced a genuine conceptual narrowing rather than another factor-degree lemma.

The exact count `N_a(p)` now has three equivalent descriptions:

1. the original irreducible count in `X^p+aX^3+cX+d`;
2. the square-value irreducible count in the root-negation quotient
   `Y(Y^((p-1)/2)+aY+c)^2-e`;
3. the compactly supported trace of one p-th Adams defect on the étale locus of that quotient cover.

The all-degree irreducibility sieve is therefore not the terminal object. It is an expansion of a single virtual sheaf

`psi^p P-P`.

The unresolved part is now one global primitive trace `E_mid`, after the already completed extremal CM assembly is subtracted.

## 2. Exact theorem: root-negation quadratic descent

Put

`H_c(Y)=Y^((p-1)/2)+aY+c`,

`G_(c,e)(Y)=YH_c(Y)^2-e`.

Then

`G_(c,d^2)(X^2)=F_(c,d)(X)F_(c,-d)(X)`.

For every `d!=0`,

`F_(c,d) irreducible`

iff

`F_(c,-d) irreducible`

iff

`G_(c,d^2) irreducible`.

Consequently

`N_a(p)=2 #{(c,e):e nonzero square, G_(c,e) irreducible}.`

The universal cover has the unusually simple derivative

`G'=(Y^m+aY+c)(3aY+c)`

and complete discriminant

`Disc G=(-1)^m 3a e^m(e-B_a(c))`.

Thus it has only two finite branch divisors, `e=0` and `e=B_a(c)`.

The equivalence was exhaustively audited for both square classes through `p=43`; the discriminant was audited for every `c,e!=0`, both classes, through `p=101`.

## 3. Exact theorem: Moore–Artin–Schreier recurrence

For `u in F_(p^p)^*`, put `v=u^p`, `w=u^(p^2)` and

`Xi_a(u)=[v^2-uw-auv(2u^2+3uv+v^2)]/[3auv(u+v)].`

Then

`pN_a(p)=#{u:Xi_a(u)^p-Xi_a(u)=u}.`

This is an exact one-variable Frobenius-rational formulation. Direct enumeration reproduced the depressed-slice counts for both classes at `p=5,7`.

The induced rational recurrence has rapid degree growth, so no low-degree integrability conclusion is claimed. It is retained as an independent coordinate system for the same global trace.

## 4. Exact theorem: the Adams count bridge

For an unramified degree-`p` fibre with Frobenius permutation `sigma`,

`Tr(sigma|psi^p P-P)=Tr(sigma^p|P)-Tr(sigma|P)`

`                         =p 1_(sigma is a p-cycle).`

On the descended cover, let `P_a` be the root permutation sheaf and `L_chi` the quadratic Kummer sheaf in `e`. Then exactly

`pN_a(p)=Tr(Frob_p | RGamma_c(U_a,`

`  (1 direct_sum L_chi) tensor (psi^p P_a-P_a))).`

This identity is taken on the affine étale complement `U_a`; the discriminant and infinity enter only when compactifying for cohomological analysis.

## 5. Extremal sector already complete

The previously completed extremal assembly gives exact formulas for every known growing-genus term:

- Kummer: elementary;
- pair curve: elementary q-average, bounded in the unweighted sector;
- split D family: one fixed rank-two CM K3 motive of discriminant `-24`;
- nonsplit D family: one fixed rank-two CM K3 motive of discriminant `-40`.

Thus `E_ext(A)=O(p)` with explicit coefficients. No unidentified growing-genus term survives in this sector.

## 6. Enlarged exact middle ledger

The exact middle residual was recomputed for both square classes at every prime `5<=p<=199`, after subtracting the complete extremal ledger.

The former table through `p=31` had

`max |E_mid|/p <11.62`.

The enlarged table has

`max |E_mid|/p=58.059880...`

at `p=167`, while

`max |E_mid|/p^(3/2)=4.492808...`.

The finite computation does not refute an `O(p)` theorem with an unspecified large constant. It does show that the earlier small-linear-constant model was a poor guide. The observed scale is naturally compatible with a weight-three trace.

The complete compact ledger is

`middle_configuration_residual_results_p199.json`.

## 7. Revised terminal lemma

The correct sufficient target is now:

### Cyclic-Adams Weight-Three Lemma

There are explicit absolute constants `C_3,C_2` such that for every prime `p`, and at least one square class `A`,

`|E_mid(A)|<=C_3p^(3/2)+C_2p.`

The exact selected-cell identity is

`pI_A=pM_A-E_ext(A)-E_mid(A)`,

with `M_A>=p-3`. Therefore

`pI_A>=p(p-3)-C_3p^(3/2)-O(p)>0`

for all sufficiently large `p`. Existing exact computation can close the finite remainder once `C_3,C_2` are explicit.

This is a terminal theorem: it is strictly weaker than the previous `O(p)` target but still proves the crown.

## 8. Breakthrough mechanism to prove or kill

The proposed proof must operate on the Adams defect before expanding it into hook or configuration degrees.

1. Compactify the descended finite cover
   `R_a(c,Y)=e`.
2. Use its two explicit finite branch divisors.
3. Apply cyclic-Adams localization or an equivalent equivariant Lefschetz construction to
   `psi^p P_a-P_a`.
4. Remove the exact Kummer/pair/D extremal classes.
5. Prove that the primitive compactly supported complex has weights at most three and uniformly bounded total Betti number.
6. Apply the Weil/Deligne bound to obtain the displayed `p^(3/2)` estimate.

The mechanism has a binary stop rule:

- bounded weight-three primitive cohomology proves the required estimate and closes the crown after finite verification;
- growing Betti number or an unavoidable weight-four component kills the fixed-complexity collapse proposal.

No further unrestricted prime sweeps or degree-by-degree factor moments are justified before this localization question is resolved.

## 9. Exact finite extension-field diagnostic

Exact counts over `F_(p^r)` were obtained at `p=5,7,11,13`.

At `p=5`, the normalized trace sequence is rank-one in the audited range. The sequences at `p=7,11,13` are not rank-one. Therefore the complete count is not governed uniformly by one eigenvalue; the appropriate object is the assembled primitive Adams complex, not a single elliptic curve or rank-one sheaf.

## 10. Epistemic classification

### Exact theorems

- root-negation product and irreducibility descent;
- structural evenness of `N_a`;
- derivative and complete discriminant of the descended cover;
- Moore–Artin–Schreier recurrence identity;
- Adams p-cycle detector and exact compactly supported count identity;
- complete extremal CM assembly from the existing package.

### Exact finite computation

- descent audit through `p=43`;
- discriminant audit through `p=101`;
- middle residual ledger through `p=199`;
- extension-field sequences at `p=5,7,11,13`.

### Open

- cyclic-Adams localization for the descended cover;
- a uniform bounded-Betti weight-three primitive complex;
- the `O(p^(3/2))` middle trace estimate;
- the function-field d=1 crown;
- the integer Fortune conjecture.
