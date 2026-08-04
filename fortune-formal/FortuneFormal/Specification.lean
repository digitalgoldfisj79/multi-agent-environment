import Mathlib

set_option autoImplicit false

namespace FortuneFormal

universe u

/--
Stage-F0 logical interface for the stable Paper VII theorem package.

The predicates are deliberately abstract at this gate. F1 must replace them by
literal finite-field polynomial definitions before any manuscript theorem is
counted as formally reconstructed.
-/
structure PaperVIISpecification where
  Datum : Type u
  crossDistinct : Datum → Prop
  inverseFreeIncidence : Datum → Prop
  scalarWitnessIncidence : Datum → Prop
  witnessUnique : Datum → Prop
  commonDefectExistsUnique : Datum → Prop
  defectDegreeBound : Datum → Prop
  zeroDefect : Datum → Prop
  reflectionOrTranslation : Datum → Prop
  fieldSize : Datum → ℕ
  modulusDegree : Datum → ℕ
  primeField : Datum → Prop
  oddPrimePowerField : Datum → Prop

namespace PaperVIISpecification

variable (S : PaperVIISpecification)

/-- P7-IFA1: inverse-free incidence is equivalent to scalar-witness incidence,
with unique witnesses, on the cross-distinct locus. -/
def IFA1Statement : Prop :=
  ∀ d : S.Datum,
    S.crossDistinct d →
      (S.inverseFreeIncidence d ↔ S.scalarWitnessIncidence d) ∧
      S.witnessUnique d

/-- P7-BDD1: every cross-distinct incidence has a unique common defect obeying
the manuscript degree bound. -/
def BDD1Statement : Prop :=
  ∀ d : S.Datum,
    S.crossDistinct d →
    S.inverseFreeIncidence d →
      S.commonDefectExistsUnique d ∧ S.defectDegreeBound d

/-- P7-BDD2: zero defect forces the reflection/translation classification. -/
def BDD2Statement : Prop :=
  ∀ d : S.Datum,
    S.crossDistinct d →
    S.inverseFreeIncidence d →
    S.zeroDefect d →
      S.reflectionOrTranslation d

/-- P7-STRIP: over prime fields, the cross-distinct incidence is empty in the
intermediate strip `k < q < 2k`. -/
def StripStatement : Prop :=
  ∀ d : S.Datum,
    S.crossDistinct d →
    S.primeField d →
    S.modulusDegree d < S.fieldSize d →
    S.fieldSize d < 2 * S.modulusDegree d →
      ¬ S.inverseFreeIncidence d

/-- P7-K2: over every odd prime-power field, the cross-distinct incidence is
empty in modulus degree two. -/
def K2EmptyStatement : Prop :=
  ∀ d : S.Datum,
    S.crossDistinct d →
    S.oddPrimePowerField d →
    S.modulusDegree d = 2 →
      ¬ S.inverseFreeIncidence d

end PaperVIISpecification

end FortuneFormal
