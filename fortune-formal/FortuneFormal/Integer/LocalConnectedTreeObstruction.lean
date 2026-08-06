import Mathlib

set_option autoImplicit false

namespace FortuneFormal
namespace Integer

/-- Exact equal-residue pair coefficient for the normalized local factor. -/
theorem normalizedPairCollision (p : ℝ) (hp : p ≠ 1) :
    p / (p - 1) - 1 = 1 / (p - 1) := by
  have hden : p - 1 ≠ 0 := sub_ne_zero.mpr hp
  field_simp [hden]
  ring

/-- Exact third connected coefficient when all three offsets occupy one residue
class modulo the local prime. -/
theorem normalizedTripleCollisionCumulant (p : ℝ) (hp : p ≠ 1) :
    p ^ 2 / (p - 1) ^ 2 - 3 * (p / (p - 1)) + 2 =
      -(p - 2) / (p - 1) ^ 2 := by
  have hden : p - 1 ≠ 0 := sub_ne_zero.mpr hp
  field_simp [hden]
  ring

/-- No fixed pair-edge constant controls the equal-residue triple once the
local prime is larger than the displayed threshold. -/
theorem tripleCollisionExceedsPairTree
    (p C : ℝ) (hp : 1 < p) (hgap : 3 * C ^ 2 < p - 2) :
    3 * (C / (p - 1)) ^ 2 < (p - 2) / (p - 1) ^ 2 := by
  have hpos : 0 < p - 1 := by
    linarith
  have hden : 0 < (p - 1) ^ 2 := pow_pos hpos 2
  have hscaled :
      (3 * C ^ 2) / (p - 1) ^ 2 < (p - 2) / (p - 1) ^ 2 :=
    (div_lt_div_iff_of_pos_right hden).2 hgap
  calc
    3 * (C / (p - 1)) ^ 2 = (3 * C ^ 2) / (p - 1) ^ 2 := by
      rw [div_pow]
      ring
    _ < (p - 2) / (p - 1) ^ 2 := hscaled

/-- The absolute r-body logarithmic exponent `r` cannot meet a fixed-delta
radius once `delta * (r - 1) > 1`. -/
theorem absoluteHyperedgeExponentGap
    (r δ : ℝ) (hgap : 1 < δ * (r - 1)) :
    r < (1 + δ) * (r - 1) := by
  nlinarith

end Integer
end FortuneFormal
