import FortuneFormal.Quadratic.Model

set_option autoImplicit false

namespace FortuneFormal
namespace Quadratic

universe u

variable {F : Type u} [Field F]

/-- B-chart localization factor used by the exact q-free certificates. -/
def gB (x : ModelPoint F) : F :=
  x.U * x.A * (x.B^2 - 4*x.C) * x.B

/-- X-chart localization factor used by the exact q-free certificates. -/
def gX (x : ModelPoint F) : F :=
  x.U * x.A * (x.B^2 - 4*x.C) * (x.A - x.C)

/-- The six pointwise consequences supplied by the two exact power-lift charts.
This proposition is deliberately separate from how those polynomial identities
are certified. -/
def ChartIdentities (x : ModelPoint F) : Prop :=
  gB x ^ 3 * (x.U - 1) = 0 ∧
  gB x ^ 3 * (x.B + 2) = 0 ∧
  gB x ^ 3 * ((x.A - x.C)^2 + 4*x.A) = 0 ∧
  gX x ^ 2 * (x.U - 1) = 0 ∧
  gX x ^ 4 * (x.B + 2) = 0 ∧
  gX x ^ 4 * ((x.A - x.C)^2 + 4*x.A) = 0

lemma gB_ne_zero_of_open {x : ModelPoint F} (h : ArithmeticOpen x)
    (hB : x.B ≠ 0) : gB x ≠ 0 := by
  rcases h with ⟨hU, hA, hdisc, _, _, _⟩
  simp only [gB]
  exact mul_ne_zero (mul_ne_zero (mul_ne_zero hU hA) hdisc) hB

lemma gX_ne_zero_of_open {x : ModelPoint F} (h : ArithmeticOpen x)
    (hX : x.A - x.C ≠ 0) : gX x ≠ 0 := by
  rcases h with ⟨hU, hA, hdisc, _, _, _⟩
  simp only [gX]
  exact mul_ne_zero (mul_ne_zero (mul_ne_zero hU hA) hdisc) hX

private lemma target_eq_zero_of_pow_mul_eq_zero {g t : F} {n : ℕ}
    (hg : g ≠ 0) (h : g ^ n * t = 0) : t = 0 := by
  exact (mul_eq_zero.mp h).resolve_left (pow_ne_zero n hg)

/-- Pure logical chart-selection bridge: once the six exact chart identities
hold at an arithmetic-open q-free point, that point lies on the certified
component. No characteristic assumption is needed here. -/
theorem certifiedComponent_of_chartIdentities {x : ModelPoint F}
    (hopen : ArithmeticOpen x) (hids : ChartIdentities x) :
    CertifiedComponent x := by
  rcases hopen with ⟨hU, hA, hdisc, hchart, hirrA, hirrS⟩
  have hopen' : ArithmeticOpen x :=
    ⟨hU, hA, hdisc, hchart, hirrA, hirrS⟩
  rcases hids with ⟨hBU, hBB, hBD, hXU, hXB, hXD⟩
  rcases hchart with hB | hX
  · have hg : gB x ≠ 0 := gB_ne_zero_of_open hopen' hB
    have hU0 : x.U - 1 = 0 := target_eq_zero_of_pow_mul_eq_zero hg hBU
    have hB0 : x.B + 2 = 0 := target_eq_zero_of_pow_mul_eq_zero hg hBB
    have hD0 : (x.A - x.C)^2 + 4*x.A = 0 :=
      target_eq_zero_of_pow_mul_eq_zero hg hBD
    constructor
    · exact sub_eq_zero.mp hU0
    constructor
    · exact eq_neg_of_add_eq_zero_left hB0
    · exact hD0
  · have hg : gX x ≠ 0 := gX_ne_zero_of_open hopen' hX
    have hU0 : x.U - 1 = 0 := target_eq_zero_of_pow_mul_eq_zero hg hXU
    have hB0 : x.B + 2 = 0 := target_eq_zero_of_pow_mul_eq_zero hg hXB
    have hD0 : (x.A - x.C)^2 + 4*x.A = 0 :=
      target_eq_zero_of_pow_mul_eq_zero hg hXD
    constructor
    · exact sub_eq_zero.mp hU0
    constructor
    · exact eq_neg_of_add_eq_zero_left hB0
    · exact hD0

/-- If the six chart identities are known for every q-free solution, the
published certificate statement follows kernel-theoretically. -/
theorem certificateStatement_of_chartIdentities
    (h : ∀ x : ModelPoint F, Equations x → ArithmeticOpen x → ChartIdentities x) :
    CertificateStatement (F := F) := by
  intro x heq hopen
  exact certifiedComponent_of_chartIdentities hopen (h x heq hopen)

end Quadratic
end FortuneFormal
