import FortuneFormal.Bilateral.Definitions
import FortuneFormal.Quadratic.Model
import FortuneFormal.Quadratic.DiscriminantContradiction

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Quadratic

open Bilateral

universe u

variable (F : Type u) [Field F] [Fintype F]

/-- Exact remaining F4 boundary.

For every genuine cross-distinct inverse-free incidence of modulus degree two
over an odd finite field with the literal Frobenius base, the external
normalization-and-certificate package must produce a point of the q-free model
which lies simultaneously in the genuine arithmetic open locus and in the
certified component.  The contradiction after this production step is checked
by Lean in `DiscriminantContradiction.lean`.

This statement deliberately contains the only external trust boundary still
needed for P7-K2.  It does not assert emptiness directly. -/
def K2CertifiedNormalizationStatement : Prop :=
  ∀ d : Datum F,
    CrossDistinct d →
    Odd (Fintype.card F) →
    FrobeniusBase d →
    d.k = 2 →
    InverseFreeIncidence d →
    ∃ x : ModelPoint F,
      Equations x ∧ ArithmeticOpen x ∧ CertifiedComponent x

variable {F}

/-- The external certified-normalization boundary plus the kernel-checked
discriminant contradiction proves the concrete Paper VII quadratic theorem. -/
theorem p7_k2_empty_of_certifiedNormalization
    (hcert : K2CertifiedNormalizationStatement F) :
    (specification F).K2EmptyStatement := by
  intro d hcross hodd hbase hk hinc
  obtain ⟨x, _heq, hopen, hcomp⟩ :=
    hcert d hcross hodd hbase hk hinc
  exact certifiedComponent_not_arithmeticOpen x hcomp hopen

end Quadratic
end FortuneFormal
