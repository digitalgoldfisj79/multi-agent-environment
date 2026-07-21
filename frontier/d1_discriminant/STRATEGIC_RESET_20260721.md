# Strategic reset after external review

**Date:** 2026-07-21  
**Status:** active programme directive.

## 1. Correct diagnosis

The fixed-period programme has succeeded through periods 2,3,4,5. It has established a repeatable mechanism:

1. full wreath-product dynatomic monodromy;
2. direct-product monodromy across a fixed finite period set;
3. independence from local admissibility;
4. signed Kummer independence;
5. fixed-degree Lang--Weil factorial moments;
6. exact finite inclusion--exclusion.

This does not solve the crown.

The crown cutoff is

`K=floor(p/3)`.

When K grows with p, the issue is not merely replacing an `O(p^(3/2))` error by `o(p)`. The independence and complexity statements themselves must be uniform in a family of periods whose size and dynatomic degrees grow with p. Those correlations are the main substance of the remaining theorem.

## 2. What not to do

Do not make degree 6,7,8 the main programme.

Further fixed degrees may be useful as validation examples, but each one only proves another fixed-complexity theorem. They do not approach a linearly growing cutoff.

An arbitrary fixed-set theorem is worthwhile consolidation and publishable mathematics, but it is not crown progress. It should be written as a byproduct, not consume the principal research effort.

## 3. Fixed-period package status

The cold audit in `DYNATOMIC_COLD_AUDIT.md` found:

- Morton's unicritical wreath-product and cross-period disjointness inputs are supported by the published literature;
- the specialization sandwich to the centered family is logically sound;
- the committed period-2,3,4,5 ramification certificates reproduce in a clean Sage environment;
- no fatal defect was found in the fixed-period foundation;
- the signed Kummer and finite-field twist ledger still needs fuller publication-level exposition.

The fixed package is frozen pending that written audit. No crown claim may treat fixed-period Lang--Weil constants as uniform in the period.

## 4. First active crown front: determinant congruence

The exact cofactor gives

`T_p(a)=sum_(c,d)J_a(c,d)=3aN_a(p)`.

The initial exhaustive scan through p=199 found no zero residue in either square class. The determinant shortcut therefore survives its first direct falsification test.

The precise failure criterion is:

- one zero square class does not kill the route;
- both square classes zero at the same prime kill the immediate two-class nonvanishing architecture.

`DETERMINANT_TWO_CLASS_REDUCTION.md` proves the exact two-mode form

`T_p(a)=alpha_p a+beta_p a^((p+1)/2)`.

Thus the determinant crown target is

`(alpha_p,beta_p)!=(0,0)`.

The immediate algebraic work is to compute or constrain the two orthogonality aggregates extracting alpha_p and beta_p.

## 5. Second active crown front: Frobenius-aligned compression

The ordinary Artin--Mazur zeta function of the cubic map is not the exact object, because it counts every dynamical cycle rather than cycles satisfying Frobenius alignment.

The correct cycle polynomial is

`Z_F(T)=det(1-T Phi | F_p[X]/(F))`

and exactly

`Z_F(T)=product_k (1-T^k)^(nu_k(F))`.

This unifies the dynatomic factorial sieve and the Berlekamp determinant.

The crown-level objective is a family trace, transfer-operator, resultant, or p-adic cohomological formula for this Frobenius-aligned determinant that avoids expansion over all mixed factorial moments.

## 6. P-adic incidence reformulation

Let C_a count triples `(theta,c,d)` with theta in `F_(p^p)` satisfying

`theta^p+a theta^3+c theta+d=0`.

Then

`C_a=pN_a+p^2`.

Consequently

`N_a mod p !=0`

if and only if

`v_p(C_a)=1`.

The determinant residue can therefore be attacked as a Hasse-type first p-adic point-count coefficient. This points toward Stickelberger, Gross--Koblitz, Dwork trace, or Hasse--Witt calculations rather than further fixed-period sieving.

## 7. Ordered execution

1. Complete a broad determinant congruence scan and test both class residues, their sum, difference, and character-weighted aggregates.
2. Finish the cold written audit of the fixed 2--5 package; do not extend the period range except for targeted validation.
3. Attack the two determinant modes by multilinearity and three-variable finite-field orthogonality.
4. In parallel derive the p-adic leading term of the incidence count C_a.
5. Use the Frobenius-aligned cycle polynomial as the only accepted growing-period compression target.
6. Return to fixed-period geometry only if it supplies a lemma needed by one of the two crown fronts.

## 8. Scope warning

Success here would prove the d=1 function-field Fortune crown. It would not prove the original integer Fortune conjecture. The increasing-order integer transfer remains a separate major obstruction.
