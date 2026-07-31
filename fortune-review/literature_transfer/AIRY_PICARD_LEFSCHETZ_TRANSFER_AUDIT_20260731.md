# Airy Picard--Lefschetz transfer audit

**Date:** 31 July 2026  
**Direct d=1 source head:** `c331f740e06a95e5596639800c931e2629ff9178`  
**External source:** Ping-Hsun Chuang, *On the Generalized Arithmetic Picard--Lefschetz Formula*, arXiv:2607.05757.

## 1. Exact object match

The direct Airy target is the rank-two Adams virtual class

\[
\Psi^p(\mathcal A)
=
\operatorname{Sym}^p\mathcal A
-
\det(\mathcal A)\otimes\operatorname{Sym}^{p-2}\mathcal A,
\]

followed by compactly supported cohomology and the `mu_3`-invariant projector.
This is exactly the adjacent pair of symmetric-power Airy motives to which the
repository's Chuang specialization audit applies.

## 2. Chuang specialization at the admitted primes

For `p = 5 mod 6`, hence `p = 2 mod 3`, the exact specialization gives:

- at `k=p`, the arithmetic Picard--Lefschetz correction index set is exactly
  `a={1}`: one Tate line is removed from the special moment;
- that `a=1` correction is not inertia invariant, so the invariant vanishing-
  cycle Frobenius space `E'` is empty;
- at `k=p-2<p`, there is no arithmetic correction at all;
- after the `mu_3` projector, both surviving Airy spaces have the same rank
  `(p-5)/6`.

The committed script `frontier/d1_symp/chuang_specialization_audit.py`
reproduces these index sets, ranks and exact first traces. The modular sequence

\[
0\to E^{(1)}\to\operatorname{Sym}^pE
\to\det(E)\otimes\operatorname{Sym}^{p-2}E\to0
\]

is independently checked by `mod_p_adams_sequence_verify.py`.

## 3. What is now closed

The local bad-reduction ledger for the adjacent Airy moments is complete:

1. the `k=p` moment loses exactly one explicit Tate line;
2. the `k=p-2` moment loses none;
3. no inertia-invariant vanishing-cycle trace remains in the admitted branch;
4. the modular Adams difference contracts to the Frobenius twist of the
   original rank-two Airy object.

Therefore the missing `d=1` cancellation is **not** an unidentified local
Picard--Lefschetz correction.

## 4. What remains open

Chuang's theorem does not control the characteristic-zero virtual trace

\[
\operatorname{Tr}(F\mid U_p)
-p\operatorname{Tr}(F\mid U_{p-2}),
\]

because the modular/Tate contraction forgets the Frobenius spectrum of the
free cyclic part. The natural integral Dwork lift has a linearly growing
comparison cone after the `mu_3` projector.

The direct analytic gate is consequently the already isolated **integral
Tate-diagonal lift theorem**:

- construct a Frobenius-compatible integral comparison whose generic cone is
  uniformly bounded; or
- prove absolute Frobenius cancellation in the existing linearly growing
  cone.

Separately, the application wall still requires an all-Frobenius identification
of the normalized Airy boundary object inside the irreducibility hook/nearby-
cycle ledger at root-direction infinity. Chuang settles the local Airy moment
correction; it does not provide that hook-complex comparison.

## 5. Exact validation

Fresh-checkout job `6a6cf93c6b79c09949c1da73` passed with marker
`CHUANG_ADAMS_TRANSFER_PASS` for `p=11,17,23,29` and verified the modular
Adams exact sequence at `p=5,7,11,13,17,23,29,41`.

## 6. Ruling

- **PROVED / imported and specialized:** local arithmetic
  Picard--Lefschetz correction for the adjacent Airy motives.
- **PROVED in repository:** modular Frobenius contraction of the Adams pair.
- **OPEN:** integral Weil-compatible lift or absolute Airy first-moment
  cancellation.
- **OPEN:** object-level transport from the Airy boundary object into the
  exact irreducibility hook ledger.
- **NOT CLAIMED:** `d=1`, the function-field crown, integer transfer or
  Fortune's conjecture.
