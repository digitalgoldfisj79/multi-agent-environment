import FortuneFormal.Bilateral.Definitions
import FortuneFormal.Quadratic.Model
import FortuneFormal.Quadratic.CertificateReduction
import FortuneFormal.Quadratic.DiscriminantContradiction

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Quadratic

open Bilateral

universe u

variable (F : Type u) [Field F]

/-- Exact remaining normalization obligation for the `k=2` theorem.

It contains no emptiness or Gröbner conclusion: it only says that a genuine
cross-distinct inverse-free quadratic incidence in the abstract Paper VII
specification supplies odd characteristic and a faithful point of the
literal q-free arithmetic model. -/
def K2NormalizationStatement : Prop :=
  ∀ d : Datum F,
    CrossDistinct d →
    d.k = 2 →
    OddPrimePower d.q →
    InverseFreeIncident d →
    (2 : F) ≠ 0 ∧ ∃ x : ModelPoint F, Equations x ∧ ArithmeticOpen x

variable {F}

/-- Once faithful quadratic normalization is available, the kernel-checked
q-free certificate and discriminant contradiction prove Paper VII's
quadratic emptiness statement. -/
theorem p7_k2_empty_of_normalization
    (hnorm : K2NormalizationStatement F) :
    (specification F).K2EmptyStatement := by
  intro d hcross hk hodd
  intro hinc
  obtain ⟨hchar, x, heq, hopen⟩ := hnorm d hcross hk hodd hinc
  have hcert : CertificateStatement (F := F) :=
    certificateStatement_of_char_ne_two hchar
  exact no_arithmeticOpen_model_of_certificate hcert ⟨x, heq, hopen⟩

end Quadratic
end FortuneFormal
