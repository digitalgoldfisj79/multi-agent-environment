import Mathlib

set_option autoImplicit false

namespace FortuneFormal
namespace Integer

open scoped BigOperators

universe u

variable {ι : Type u} [Fintype ι]

/-- A single failed centre already contributes its full squared gap to the
nonnegative block variance. -/
theorem no_failure_of_total_error_lt_gap
    (Z base : ι → ℝ) (gap : ℝ)
    (hvar : (∑ i, (Z i - base i)^2) < gap)
    (hfailure : ∀ i, Z i = 0 → gap ≤ (Z i - base i)^2) :
    ∀ i, Z i ≠ 0 := by
  intro i hi
  have hterm : (Z i - base i)^2 ≤ ∑ k, (Z k - base k)^2 := by
    exact Finset.single_le_sum
      (fun k _ => sq_nonneg (Z k - base k))
      (Finset.mem_univ i)
  have hgap := hfailure i hi
  linarith

/-- Baselines bounded below by `cX` give a squared failure gap `(cX)^2`. -/
theorem no_failure_of_variance_below_baseline_gap
    (Z base : ι → ℝ) (cX : ℝ)
    (hcX : 0 ≤ cX)
    (hbase : ∀ i, cX ≤ base i)
    (hvar : (∑ i, (Z i - base i)^2) < cX^2) :
    ∀ i, Z i ≠ 0 := by
  apply no_failure_of_total_error_lt_gap Z base (cX^2) hvar
  intro i hi
  have hb0 : 0 ≤ base i := le_trans hcX (hbase i)
  have hprod : 0 ≤ (base i - cX) * (base i + cX) :=
    mul_nonneg (sub_nonneg.mpr (hbase i)) (add_nonneg hb0 hcX)
  have hsquare : cX^2 ≤ (base i)^2 := by
    nlinarith
  simpa [hi] using hsquare

/-- Exact centred second-moment identity. The final summand is the unique
signed covariance residual that must be bounded after centring. -/
theorem centered_second_moment_identity
    (Z base : ι → ℝ) :
    (∑ i, (Z i - base i)^2) =
      (∑ i, base i) +
      ∑ i, (Z i^2 - 2 * base i * Z i + base i^2 - base i) := by
  calc
    (∑ i, (Z i - base i)^2) =
        ∑ i, (base i + (Z i^2 - 2 * base i * Z i + base i^2 - base i)) := by
      apply Finset.sum_congr rfl
      intro i _
      ring
    _ = (∑ i, base i) +
        ∑ i, (Z i^2 - 2 * base i * Z i + base i^2 - base i) := by
      rw [Finset.sum_add_distrib]

/-- If `C i` is the off-diagonal successful-pair count satisfying
`Z i ^ 2 = Z i + 2 C i`, the variance is exactly the baseline sum plus the
four-prime covariance residual. -/
theorem four_prime_covariance_identity
    (Z base C : ι → ℝ)
    (hC : ∀ i, Z i^2 = Z i + 2 * C i) :
    (∑ i, (Z i - base i)^2) =
      (∑ i, base i) +
      ∑ i, (Z i + 2 * C i - 2 * base i * Z i + base i^2 - base i) := by
  rw [centered_second_moment_identity Z base]
  congr 1
  apply Finset.sum_congr rfl
  intro i _
  rw [hC i]

end Integer
end FortuneFormal
