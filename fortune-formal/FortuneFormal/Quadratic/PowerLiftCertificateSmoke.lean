import Mathlib

set_option autoImplicit false
set_option maxHeartbeats 0

noncomputable section

namespace FortuneFormal
namespace Quadratic
namespace PowerLiftSmoke

open MvPolynomial

def q : MvPolynomial (Fin 2) ℤ := X 0 + 2 * X 1 + 3

/-- Smoke test for the proposed exact sparse-polynomial certificate path.
`MvPolynomial` multiplication is noncomputable, so the kernel-certified route
uses the reflective `ring` normalizer rather than `native_decide` directly. -/
theorem q_square :
    q * q = X 0 ^ 2 + 4 * X 0 * X 1 + 6 * X 0 +
      4 * X 1 ^ 2 + 12 * X 1 + 9 := by
  unfold q
  ring

end PowerLiftSmoke
end Quadratic
end FortuneFormal
