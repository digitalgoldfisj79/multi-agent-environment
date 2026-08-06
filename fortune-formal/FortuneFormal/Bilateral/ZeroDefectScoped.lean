import Mathlib
import FortuneFormal.Bilateral.Definitions
import FortuneFormal.Bilateral.QuotientShape
import FortuneFormal.Bilateral.ZeroDefectReduction

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

/-- The first scalar endpoint witness is nonzero on an inverse-free incidence. -/
theorem c_ne_zero_of_inverseFree (x : Datum F)
    (h : MuInverseFreeAt x x.c) : x.c ≠ 0 := by
  intro hc
  have htheta : x.P ∣ scalar x.theta := by
    apply x.P_coprime_Pp.dvd_of_dvd_mul_right
    simpa [MuInverseFreeAt, hc] using h.1
  have hscalar : scalar x.theta ≠ 0 :=
    Polynomial.C_ne_zero.mpr x.theta_ne_zero
  exact (Polynomial.not_dvd_of_natDegree_lt hscalar <| by
    rw [x.P_degree]
    simpa [scalar] using x.k_pos) htheta

/-- The normalized scalar `λ=-θ/c` is nonzero on an inverse-free incidence. -/
theorem lambda_ne_zero_of_inverseFree (x : Datum F)
    (h : MuInverseFreeAt x x.c) : lambda x ≠ 0 := by
  have hc := c_ne_zero_of_inverseFree x h
  simp [lambda, div_eq_mul_inv, x.theta_ne_zero, hc]

/-- In the corrected prime-Frobenius scope, an actual zero-defect incidence
supplies a quotient witness in the Artin-Schreier normal form. -/
theorem zeroDefect_normalForm_of_incidence (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (hk : x.k < Fintype.card F) (hinc : InverseFreeIncidence x)
    (hz : ZeroDefect x) :
    ∃ q : QuotientWitness x, ZeroDefectNormalForm x q := by
  rcases hz with ⟨q, hh⟩
  have shape := quotientLeadingShape x hp hbase hk q
  have hlam := lambda_ne_zero_of_inverseFree x hinc.1
  exact ⟨q, zeroDefect_normalForm x q shape hlam hh⟩

end Bilateral
end FortuneFormal
