import Mathlib

set_option autoImplicit false

namespace FortuneFormal
namespace Integer

/-- If a proved positive divisor band supplies `bandLower`, the signed tail loses
at most `tailLoss`, and `target` is below their difference, then the full
selected-centre weighted mean reaches `target`. -/
theorem selectedCentreMean_lowerBound_of_band_and_tail
    (band tail bandLower tailLoss target : ℝ)
    (hband : bandLower ≤ band)
    (htail : -tailLoss ≤ tail)
    (htarget : target ≤ bandLower - tailLoss) :
    target ≤ band + tail := by
  linarith

/-- The normalized version used by INT-SCPT: a band of size `delta * scale`
and a tail no smaller than `-(delta-kappa) * scale` leave `kappa * scale`. -/
theorem selectedCentreMean_of_normalized_parityTail
    (band tail scale delta kappa : ℝ)
    (hband : delta * scale ≤ band)
    (htail : -((delta - kappa) * scale) ≤ tail) :
    kappa * scale ≤ band + tail := by
  linarith

end Integer
end FortuneFormal
