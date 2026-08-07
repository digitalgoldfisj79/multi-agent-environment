# Specialist review packet — arithmetic geometry and finite fields

## Scope

Primary manuscripts: Paper V, quotient portions of Paper VI, and Paper VII.

Priority theorem clusters:

- `V-ORBIT-CROWN`, `V-SMOOTH`, `V-SAWIN`, `V-HOOKS`, `V-FIXED`, `V-QLINE`
- `VI-AS-QUOTIENT`, `VI-KUMMER`, `VI-COMPACT`
- `VII-DEFECT`, `VII-ZERO-DEFECT`, `VII-K2`

## Known comparator warning

Grothendieck--Lefschetz factorisation-statistics machinery, Artin--Schreier torsors and Kummer descent are established. Possible novelty lies in the sparse varieties, exact projectors/identities, quotient geometry and endpoint-incidence classification.

## Questions for the reviewer

1. Does the sparse cone/projective surface satisfy the geometric hypotheses used for the cohomological transfer exactly as claimed?
2. Are the crown/q-line projectors and exact fixed-point identities known specializations of existing factorisation-statistics formulae?
3. After the assurance repairs, are the explicit Artin--Schreier quotient, no-split argument, Kummer two-form count and compactified quotient count correct on the stated open loci?
4. Does the compactification introduce any omitted stabiliser, singular boundary or rational component affecting the count?
5. Is Paper VII's common-defect theorem or zero-defect reflection/translation classification known in finite-field Frobenius/incidence language?
6. Independently check the degree-two normalization from genuine polynomial incidence into the q-free model and the two-chart Singular certificate.
7. Is quadratic emptiness over every odd prime power genuinely new, a known special case, or a disguised standard low-degree incidence result?

## Assurance already performed

- Paper V finite orbit/smoothness/projector panels reproduced;
- Paper VI finite quotient/count panels reproduced and three proof-hygiene gaps repaired;
- Paper VII two Singular charts regenerated and independently verified exactly;
- compact power-lift certificate reduces denominator prime support to `{2,3,5}`;
- final Paper VII discriminant contradiction is Lean-kernel checked;
- genuine `Datum` normalization remains the sole formal trust boundary.

## Requested output

For every priority cluster: correctness verdict, closest known result, exact novelty classification, and any required change to the variety/open-locus definitions.
