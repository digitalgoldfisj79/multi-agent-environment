import Mathlib

set_option autoImplicit false

namespace FortuneFormal
namespace Quadratic
namespace PowerLiftSmoke

open MvPolynomial

def q : MvPolynomial (Fin 2) ℤ := X 0 + 2 * X 1 + 3

/-- Smoke test for the proposed exact sparse-polynomial certificate path. -/
theorem q_square :
    q * q = X 0 ^ 2 + 4 * X 0 * X 1 + 6 * X 0 +
      4 * X 1 ^ 2 + 12 * X 1 + 9 := by
  native_decide

end PowerLiftSmoke
end Quadratic
end FortuneFormal
