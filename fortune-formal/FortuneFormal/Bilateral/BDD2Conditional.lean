import Mathlib
import FortuneFormal.Bilateral.ArtinSchreierFactor
import FortuneFormal.Bilateral.FamilyReconstruction
import FortuneFormal.Bilateral.ZeroDefectScoped

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

universe u

/-- The exact supporting statement still required to close BDD2. -/
def ArtinSchreierSupport (F : Type u) [Field F] [Fintype F] : Prop :=
  ∀ x : Datum F,
    Nat.Prime (Fintype.card F) →
    FrobeniusBase x →
    InverseFreeIncidence x →
      Irreducible (x.L - scalar (lambda x))

/-- Once the prime-field Artin-Schreier support theorem is supplied, every
remaining step of the zero-defect classification is kernel checked. -/
theorem p7_bdd2_of_artinSchreier
    (F : Type u) [Field F] [Fintype F]
    (hartin : ArtinSchreierSupport F) :
    (specification F).BDD2Statement := by
  change ∀ x : Datum F,
    CrossDistinct x →
    Nat.Prime (Fintype.card F) →
    FrobeniusBase x →
    x.k < Fintype.card F →
    InverseFreeIncidence x →
    ZeroDefect x →
      ReflectionOrTranslation x
  intro x _ hp hbase hk hinc hz
  have hirr := hartin x hp hbase hinc
  obtain ⟨q, hnormal, horder⟩ :=
    zeroDefect_factorOrdering_of_artinIrreducible x hp hbase hk hinc hz hirr
  have hlam := lambda_ne_zero_of_inverseFree x hinc.1
  exact reflectionOrTranslation_of_factorOrdering x q hnormal hlam horder

end Bilateral
end FortuneFormal
