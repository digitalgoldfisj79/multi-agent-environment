import Mathlib
import FortuneFormal.Quadratic.Model

set_option autoImplicit false

namespace FortuneFormal
namespace Quadratic

universe u

variable {F : Type u} [Field F]

/-- On the component forced by the two localization certificates, the
normalized discriminant of `P = t² + A` is the square `(A-C)²`. -/
theorem firstDiscriminant_square_of_certifiedComponent
    (x : ModelPoint F) (h : CertifiedComponent x) :
    IsLiteralSquare (-4 * x.A) := by
  rcases h with ⟨_, _, hrel⟩
  refine ⟨x.A - x.C, ?_⟩
  linear_combination hrel

/-- On the certified component, the normalized discriminant of
`S = t² + Bt + C` is the square `(A-C+2)²`. -/
theorem secondDiscriminant_square_of_certifiedComponent
    (x : ModelPoint F) (h : CertifiedComponent x) :
    IsLiteralSquare (x.B^2 - 4 * x.C) := by
  rcases h with ⟨_, hB, hrel⟩
  refine ⟨x.A - x.C + 2, ?_⟩
  rw [hB]
  linear_combination hrel

/-- The certificate component and the genuine arithmetic open locus are
disjoint: both monic quadratics would have square discriminant. -/
theorem certifiedComponent_not_arithmeticOpen
    (x : ModelPoint F) (hcomp : CertifiedComponent x) :
    ¬ ArithmeticOpen x := by
  intro hopen
  exact hopen.2.2.2.2.1
    (firstDiscriminant_square_of_certifiedComponent x hcomp)

/-- Therefore a proof of the certificate statement immediately makes the
q-free arithmetic model empty. -/
theorem no_arithmeticOpen_model_of_certificate
    (hcert : CertificateStatement (F := F)) :
    ¬ ∃ x : ModelPoint F, Equations x ∧ ArithmeticOpen x := by
  rintro ⟨x, heq, hopen⟩
  exact certifiedComponent_not_arithmeticOpen x (hcert x heq hopen) hopen

end Quadratic
end FortuneFormal
