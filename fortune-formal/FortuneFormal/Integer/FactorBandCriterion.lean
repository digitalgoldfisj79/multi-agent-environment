import FortuneFormal.Integer.LowerTailCriterion

set_option autoImplicit false

namespace FortuneFormal
namespace Integer

open scoped BigOperators

universe u

variable {ι : Type u} [Fintype ι]

/-- If a failed source is at most half its nonnegative threshold, then its
one-sided lower-tail contribution is at least one quarter of the squared
threshold. -/
theorem lowerTail_quarter_gap_of_source_le_half
    (source base : ℝ)
    (hbase : 0 ≤ base)
    (hsource : source ≤ base / 2) :
    (base / 2) ^ 2 ≤ lowerTailSq source base := by
  have hdiff : 0 ≤ base - source := by
    linarith
  rw [lowerTailSq, max_eq_right hdiff]
  nlinarith

/-- A uniform lower bound on the quarter-gap at every failed row converts a
variable-threshold lower-tail estimate into exclusion of all failures. -/
theorem no_failure_of_variable_source_cap
    (source base : ι → ℝ) (failure : ι → Prop) (gap : ℝ)
    (hbase : ∀ i, 0 ≤ base i)
    (hcap : ∀ i, failure i → source i ≤ base i / 2)
    (hgap : ∀ i, failure i → gap ≤ (base i / 2) ^ 2)
    (htail : (∑ i, lowerTailSq (source i) (base i)) < gap) :
    ∀ i, ¬ failure i := by
  apply no_failure_of_lowerTail_total_gap source base failure gap htail
  intro i hi
  exact le_trans (hgap i hi)
    (lowerTail_quarter_gap_of_source_le_half
      (source i) (base i) (hbase i) (hcap i hi))

/-- Squared excess of factor coverage above the allowed coverage ceiling. -/
def coverageExcessSq (candidate covered margin : ℝ) : ℝ :=
  (max 0 (covered - candidate + margin)) ^ 2

/-- Complete coverage at a failed row creates a full squared margin. -/
theorem coverageExcessSq_of_complete
    (candidate covered margin : ℝ)
    (hmargin : 0 ≤ margin)
    (hcomplete : covered = candidate) :
    coverageExcessSq candidate covered margin = margin ^ 2 := by
  rw [coverageExcessSq, hcomplete]
  simp [max_eq_right hmargin]

/-- If every failure is complete factor coverage and the total coverage excess
is below the smallest squared margin, no failure exists. -/
theorem no_failure_of_coverage_excess
    (candidate covered margin : ι → ℝ) (failure : ι → Prop) (gap : ℝ)
    (hmargin : ∀ i, 0 ≤ margin i)
    (hcomplete : ∀ i, failure i → covered i = candidate i)
    (hgap : ∀ i, failure i → gap ≤ (margin i) ^ 2)
    (htotal : (∑ i, coverageExcessSq (candidate i) (covered i) (margin i)) < gap) :
    ∀ i, ¬ failure i := by
  intro i hi
  have hterm : coverageExcessSq (candidate i) (covered i) (margin i) ≤
      ∑ k, coverageExcessSq (candidate k) (covered k) (margin k) := by
    exact Finset.single_le_sum
      (fun k _ => sq_nonneg (max 0 (covered k - candidate k + margin k)))
      (Finset.mem_univ i)
  have hfull := coverageExcessSq_of_complete
    (candidate i) (covered i) (margin i) (hmargin i) (hcomplete i hi)
  rw [hfull] at hterm
  have hg := hgap i hi
  linarith

end Integer
end FortuneFormal
