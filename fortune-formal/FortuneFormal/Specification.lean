import Mathlib

set_option autoImplicit false

namespace FortuneFormal

universe u

/--
Logical interface for the stable Paper VII theorem package.

F1 supplies a literal finite-field polynomial interpretation.  The scope
predicates are explicit because the defect, strip, and quadratic theorems are
statements about the Frobenius base polynomial `t^q - t`, not arbitrary data.
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
  frobeniusBase : Datum → Prop
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

/-- P7-BDD1 in its manuscript scope: over the prime Frobenius base and for
`k < q`, every cross-distinct incidence has a unique common defect obeying the
degree bound. -/
def BDD1Statement : Prop :=
  ∀ d : S.Datum,
    S.crossDistinct d →
    S.primeField d →
    S.frobeniusBase d →
    S.modulusDegree d < S.fieldSize d →
    S.inverseFreeIncidence d →
      S.commonDefectExistsUnique d ∧ S.defectDegreeBound d

/-- P7-BDD2 in the same prime-field Frobenius scope: zero defect forces the
reflection/translation classification. -/
def BDD2Statement : Prop :=
  ∀ d : S.Datum,
    S.crossDistinct d →
    S.primeField d →
    S.frobeniusBase d →
    S.modulusDegree d < S.fieldSize d →
    S.inverseFreeIncidence d →
    S.zeroDefect d →
      S.reflectionOrTranslation d

/-- P7-STRIP: over the prime Frobenius base, the cross-distinct incidence is
empty in the intermediate strip `k < q < 2k`. -/
def StripStatement : Prop :=
  ∀ d : S.Datum,
    S.crossDistinct d →
    S.primeField d →
    S.frobeniusBase d →
    S.modulusDegree d < S.fieldSize d →
    S.fieldSize d < 2 * S.modulusDegree d →
      ¬ S.inverseFreeIncidence d

/-- P7-K2: over every odd prime-power Frobenius base, the cross-distinct
incidence is empty in modulus degree two. -/
def K2EmptyStatement : Prop :=
  ∀ d : S.Datum,
    S.crossDistinct d →
    S.oddPrimePowerField d →
    S.frobeniusBase d →
    S.modulusDegree d = 2 →
      ¬ S.inverseFreeIncidence d

end PaperVIISpecification

end FortuneFormal
