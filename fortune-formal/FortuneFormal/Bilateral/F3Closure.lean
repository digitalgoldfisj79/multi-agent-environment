import Mathlib
import FortuneFormal.Bilateral.ArtinSchreierIrreducible
import FortuneFormal.Bilateral.BDD2Conditional
import FortuneFormal.Bilateral.StripReduction

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

universe u

/-- The concrete prime-field Artin-Schreier support theorem required by BDD2
and strip emptiness. -/
theorem artinSchreierSupport_concrete
    (F : Type u) [Field F] [Fintype F] : ArtinSchreierSupport F := by
  intro x hp hbase hinc
  have hlam := lambda_ne_zero_of_inverseFree x hinc.1
  rw [hbase]
  simpa [artinSchreierPolynomial] using
    artinSchreier_irreducible (F := F) (lambda x) hlam hp

/-- Kernel-level reconstruction of the zero-defect reflection/translation
classification. -/
theorem p7_bdd2_concrete
    (F : Type u) [Field F] [Fintype F] :
    (specification F).BDD2Statement :=
  p7_bdd2_of_artinSchreier F (artinSchreierSupport_concrete F)

/-- Kernel-level reconstruction of intermediate-strip emptiness. -/
theorem p7_strip_concrete
    (F : Type u) [Field F] [Fintype F] :
    (specification F).StripStatement :=
  p7_strip_of_artinSchreier F (artinSchreierSupport_concrete F)

end Bilateral
end FortuneFormal
