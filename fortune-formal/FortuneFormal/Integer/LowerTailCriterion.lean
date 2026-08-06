import FortuneFormal.Integer.BlockCriterion

set_option autoImplicit false

namespace FortuneFormal
namespace Integer

open scoped BigOperators

universe u

variable {ι : Type u} [Fintype ι]

/-- Squared negative deviation. Positive surpluses are discarded. -/
def lowerTailSq (Z base : ℝ) : ℝ :=
  (max 0 (base - Z)) ^ 2

/-- The one-sided lower-tail energy is pointwise bounded by full squared error. -/
theorem lowerTailSq_le_sq (Z base : ℝ) :
    lowerTailSq Z base ≤ (Z - base) ^ 2 := by
  by_cases h : 0 ≤ base - Z
  · rw [lowerTailSq, max_eq_right h]
    nlinarith
  · have h' : base - Z ≤ 0 := le_of_not_ge h
    rw [lowerTailSq, max_eq_left h']
    simpa using sq_nonneg (Z - base)

/-- Summing the pointwise inequality shows that any full variance estimate
controls the lower-tail energy, while the converse need not hold. -/
theorem lowerTail_sum_le_variance (Z base : ι → ℝ) :
    (∑ i, lowerTailSq (Z i) (base i)) ≤
      ∑ i, (Z i - base i) ^ 2 := by
  exact Finset.sum_le_sum fun i _ => lowerTailSq_le_sq (Z i) (base i)

/-- Any failed item whose lower-tail contribution is at least `gap` is excluded
when the total lower-tail energy is strictly below `gap`. -/
theorem no_failure_of_lowerTail_total_gap
    (source base : ι → ℝ) (failure : ι → Prop) (gap : ℝ)
    (htail : (∑ i, lowerTailSq (source i) (base i)) < gap)
    (hfailure : ∀ i, failure i → gap ≤ lowerTailSq (source i) (base i)) :
    ∀ i, ¬ failure i := by
  intro i hi
  have hterm : lowerTailSq (source i) (base i) ≤
      ∑ k, lowerTailSq (source k) (base k) := by
    exact Finset.single_le_sum
      (fun k _ => sq_nonneg (max 0 (base k - source k)))
      (Finset.mem_univ i)
  have hgap := hfailure i hi
  linarith

/-- If every baseline is at least `cX`, then a failed centre contributes at
least `(cX)^2` to the one-sided lower-tail energy. Consequently a total
lower-tail energy below that gap excludes every failure. -/
theorem no_failure_of_lowerTail_below_baseline_gap
    (Z base : ι → ℝ) (cX : ℝ)
    (hcX : 0 ≤ cX)
    (hbase : ∀ i, cX ≤ base i)
    (htail : (∑ i, lowerTailSq (Z i) (base i)) < cX ^ 2) :
    ∀ i, Z i ≠ 0 := by
  intro i hi
  have hterm : lowerTailSq (Z i) (base i) ≤
      ∑ k, lowerTailSq (Z k) (base k) := by
    exact Finset.single_le_sum
      (fun k _ => sq_nonneg (max 0 (base k - Z k)))
      (Finset.mem_univ i)
  have hb0 : 0 ≤ base i := le_trans hcX (hbase i)
  have hprod : 0 ≤ (base i - cX) * (base i + cX) :=
    mul_nonneg (sub_nonneg.mpr (hbase i)) (add_nonneg hb0 hcX)
  have hsq : cX ^ 2 ≤ (base i) ^ 2 := by
    nlinarith [hprod]
  have hfailed : lowerTailSq (Z i) (base i) = (base i) ^ 2 := by
    rw [lowerTailSq, hi, sub_zero, max_eq_right hb0]
  rw [hfailed] at hterm
  linarith

end Integer
end FortuneFormal
