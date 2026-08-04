import Mathlib
import FortuneFormal.Quadratic.Model

set_option autoImplicit false
set_option maxHeartbeats 800000

namespace FortuneFormal
namespace Quadratic

universe u

variable {F : Type u} [Field F]

private theorem four_ne_zero (h2 : (2 : F) ≠ 0) : (4 : F) ≠ 0 := by
  norm_num [show (2 : F) ≠ 0 from h2]

private theorem B_ne_zero_of_open_equations
    (h2 : (2 : F) ≠ 0) (x : ModelPoint F)
    (heq : Equations x) (hopen : ArithmeticOpen x) : x.B ≠ 0 := by
  rcases heq with ⟨h0, h1, h2eq, h3eq⟩
  rcases hopen with ⟨hU, hA, hdisc, hchart, hnsqP, hnsqS⟩
  intro hB
  have hAC : x.A - x.C ≠ 0 := hchart.resolve_left hB
  have hprod : -4 * (x.A - x.C)^2 * (x.U - 1) = 0 := by
    dsimp [f1] at h1
    rw [hB] at h1
    polyrith
  have hU1 : x.U = 1 := by
    rcases mul_eq_zero.mp hprod with hfourprod | hUm
    · rcases mul_eq_zero.mp hfourprod with hfour | hsq
      · exact False.elim ((four_ne_zero h2) (by simpa using hfour))
      · exact False.elim ((pow_ne_zero 2 hAC) hsq)
    · exact sub_eq_zero.mp hUm
  have hsq : (x.A - x.C)^2 = 0 := by
    dsimp [f0] at h0
    rw [hB, hU1] at h0
    polyrith
  exact (pow_ne_zero 2 hAC) hsq

/-- Away from characteristic three, the four q-free equations force the
small branch factor used in the hand reconstruction of the universal
localization certificate. -/
private theorem branch_factor_of_equations
    (h3 : (3 : F) ≠ 0) (x : ModelPoint F) (heq : Equations x) :
    (x.B^5 * x.U^3) * ((x.B + 2) * (x.B + 2*x.U)) = 0 := by
  rcases heq with ⟨h0, h1, h2, h3eq⟩
  dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
  polyrith

private theorem component_of_first_branch
    (x : ModelPoint F) (heq : Equations x) (hopen : ArithmeticOpen x)
    (hBval : x.B + 2 = 0) : CertifiedComponent x := by
  rcases heq with ⟨h0, h1, h2, h3eq⟩
  rcases hopen with ⟨hU, hA, hdisc, hchart, hnsqP, hnsqS⟩
  have hB : x.B = -2 := by polyrith
  have hAU : (x.A + 1) * (x.U - 1) = 0 := by
    dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
    polyrith
  have hCU : (x.C - 1) * (x.U - 1) = 0 := by
    dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
    polyrith
  have hU1 : x.U = 1 := by
    by_contra hUne
    have hUm : x.U - 1 ≠ 0 := sub_ne_zero.mpr hUne
    have hA1 : x.A = -1 := by
      have := (mul_eq_zero.mp hAU).resolve_right hUm
      exact add_eq_zero.mp this
    have hC1 : x.C = 1 := by
      have := (mul_eq_zero.mp hCU).resolve_right hUm
      exact sub_eq_zero.mp this
    apply hdisc
    rw [hB, hC1]
    ring
  have hrel : (x.A - x.C)^2 + 4*x.A = 0 := by
    dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
    polyrith
  exact ⟨hU1, hB, hrel⟩

private theorem component_of_second_branch
    (x : ModelPoint F) (heq : Equations x) (hopen : ArithmeticOpen x)
    (hBval : x.B + 2*x.U = 0) : CertifiedComponent x := by
  rcases heq with ⟨h0, h1, h2, h3eq⟩
  rcases hopen with ⟨hU, hA, hdisc, hchart, hnsqP, hnsqS⟩
  have hCU : x.C * x.U^4 * (x.U - 1) = 0 := by
    dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
    polyrith
  have hAU : x.U * (x.U - 1) *
      (x.A + 12*x.C*x.U^2 + 4*x.C*x.U + x.C) = 0 := by
    dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
    polyrith
  have hU1 : x.U = 1 := by
    by_contra hUne
    have hUm : x.U - 1 ≠ 0 := sub_ne_zero.mpr hUne
    have hC0 : x.C = 0 := by
      rcases mul_eq_zero.mp hCU with hCU0 | hUm0
      · rcases mul_eq_zero.mp hCU0 with hC | hUpow
        · exact hC
        · exact False.elim ((pow_ne_zero 4 hU) hUpow)
      · exact False.elim (hUm hUm0)
    have hA0 : x.A = 0 := by
      rcases mul_eq_zero.mp hAU with hUU | hlast
      · rcases mul_eq_zero.mp hUU with hU0 | hUm0
        · exact False.elim (hU hU0)
        · exact False.elim (hUm hUm0)
      · rw [hC0] at hlast
        simpa using hlast
    exact hA hA0
  have hB : x.B = -2 := by
    rw [hU1] at hBval
    polyrith
  have hrel : (x.A - x.C)^2 + 4*x.A = 0 := by
    dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
    polyrith
  exact ⟨hU1, hB, hrel⟩

/-- The universal q-free certificate in odd characteristic other than three,
reconstructed directly in Lean from the four equations. -/
theorem certificateStatement_of_char_ne_two_three
    (h2 : (2 : F) ≠ 0) (h3 : (3 : F) ≠ 0) :
    CertificateStatement (F := F) := by
  intro x heq hopen
  have hB := B_ne_zero_of_open_equations h2 x heq hopen
  have hU := hopen.1
  have hfactor := branch_factor_of_equations h3 x heq
  have hprefix : x.B^5 * x.U^3 ≠ 0 :=
    mul_ne_zero (pow_ne_zero 5 hB) (pow_ne_zero 3 hU)
  have hbranches : (x.B + 2) * (x.B + 2*x.U) = 0 :=
    (mul_eq_zero.mp hfactor).resolve_left hprefix
  rcases mul_eq_zero.mp hbranches with hfirst | hsecond
  · exact component_of_first_branch x heq hopen hfirst
  · exact component_of_second_branch x heq hopen hsecond

/-- Characteristic-three saturation is kept as an explicit, separately
checkable polynomial certificate rather than being inferred from the
characteristic-zero denominator calculation. -/
theorem certificateStatement_of_char_three
    (hchar : (3 : F) = 0) : CertificateStatement (F := F) := by
  intro x heq hopen
  rcases heq with ⟨h0, h1, h2, h3eq⟩
  rcases hopen with ⟨hU, hA, hdisc, hchart, hnsqP, hnsqS⟩
  have htwo : (2 : F) ≠ 0 := by
    intro htwo0
    have hone : (1 : F) = 0 := by polyrith
    exact one_ne_zero hone
  have hB := B_ne_zero_of_open_equations htwo x ⟨h0, h1, h2, h3eq⟩
    ⟨hU, hA, hdisc, hchart, hnsqP, hnsqS⟩
  have hinv :
      (x.U * x.A * (x.B^2 - 4*x.C) * x.B) *
        (x.U * x.A * (x.B^2 - 4*x.C) * x.B)⁻¹ = 1 := by
    field_simp [hU, hA, hdisc, hB]
  have hU1 : x.U = 1 := by
    dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
    polyrith
  have hBval : x.B = -2 := by
    dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
    polyrith
  have hrel : (x.A - x.C)^2 + 4*x.A = 0 := by
    dsimp [f0, f1, f2, f3] at h0 h1 h2 h3eq
    polyrith
  exact ⟨hU1, hBval, hrel⟩

/-- Complete odd-characteristic certificate statement. -/
theorem certificateStatement_of_char_ne_two
    (h2 : (2 : F) ≠ 0) : CertificateStatement (F := F) := by
  by_cases h3 : (3 : F) = 0
  · exact certificateStatement_of_char_three h3
  · exact certificateStatement_of_char_ne_two_three h2 h3

end Quadratic
end FortuneFormal
