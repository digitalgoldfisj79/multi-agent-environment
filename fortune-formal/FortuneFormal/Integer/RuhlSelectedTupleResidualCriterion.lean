import Mathlib

namespace FortuneFormal.Integer

/-- An absolute factorial-moment envelope that contains a non-negative remainder
forces the first-order error below the detector margin divided by its weight. -/
theorem firstOrderError_lt_allowance
    (q e₁ rest margin : ℝ)
    (hq : 0 < q)
    (hrest : 0 ≤ rest)
    (hbudget : q * |e₁| + rest < margin) :
    |e₁| < margin / q := by
  have hmul : |e₁| * q < margin := by
    nlinarith [abs_nonneg e₁]
  exact (lt_div_iff₀ hq).2 hmul

/-- If the detector margin is at most a fixed multiple of the first-order
weight, the same envelope forces a fixed absolute first-moment error bound. -/
theorem firstOrderError_lt_constant
    (q e₁ rest margin C : ℝ)
    (hq : 0 < q)
    (hrest : 0 ≤ rest)
    (hbudget : q * |e₁| + rest < margin)
    (hmargin : margin ≤ C * q) :
    |e₁| < C := by
  have hweighted : |e₁| * q < C * q := by
    nlinarith [abs_nonneg e₁]
  have hdiv : |e₁| < (C * q) / q := (lt_div_iff₀ hq).2 hweighted
  simpa [hq.ne'] using hdiv

/-- The signed residual is algebraically the difference of the weighted actual
and model moment polynomials. -/
theorem weightedResidual_eq_difference
    (S : Finset ℕ) (w actual model : ℕ → ℝ) :
    (∑ k ∈ S, w k * (actual k - model k)) =
      (∑ k ∈ S, w k * actual k) - (∑ k ∈ S, w k * model k) := by
  simp only [mul_sub, Finset.sum_sub_distrib]

end FortuneFormal.Integer
