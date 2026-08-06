import FortuneFormal.Integer.FactorBandCriterion
import Mathlib.Analysis.SpecialFunctions.Exp

set_option autoImplicit false

namespace FortuneFormal
namespace Integer

open scoped BigOperators

universe u v

variable {ι : Type u} [Fintype ι]

/-- Complete factor coverage is algebraically the complement of the successful
prime-pair count. Hence the PFLI factor excess is exactly the count lower tail. -/
theorem coverageExcessSq_eq_lowerTailSq
    (candidate covered count margin : ℝ)
    (hpartition : candidate = count + covered) :
    coverageExcessSq candidate covered margin = lowerTailSq count margin := by
  rw [coverageExcessSq, lowerTailSq, hpartition]
  congr 1
  ring_nf

/-- Any nonnegative soft detector which equals one at every failed row excludes
all failures once its total mass is strictly below one. -/
theorem no_failure_of_soft_detector_sum_lt_one
    {α : Type v}
    (source : ι → α) (failure : ι → Prop) (detector : α → ℝ)
    (hnonneg : ∀ x, 0 ≤ detector x)
    (hfailure : ∀ i, failure i → detector (source i) = 1)
    (htotal : (∑ i, detector (source i)) < 1) :
    ∀ i, ¬ failure i := by
  intro i hi
  have hterm : detector (source i) ≤ ∑ k, detector (source k) := by
    exact Finset.single_le_sum
      (fun k _ => hnonneg (source k))
      (Finset.mem_univ i)
  rw [hfailure i hi] at hterm
  linarith

/-- Exponential occupancy detector. -/
noncomputable def expDefect (tau source : ℝ) : ℝ :=
  Real.exp (-tau * source)

@[simp] theorem expDefect_zero (tau : ℝ) : expDefect tau 0 = 1 := by
  simp [expDefect]

theorem expDefect_nonneg (tau source : ℝ) : 0 ≤ expDefect tau source := by
  exact le_of_lt (Real.exp_pos _)

/-- A failed row has source zero and therefore contributes one to the
exponential occupancy mass. Total mass below one excludes every failed row. -/
theorem no_failure_of_expDefect_sum_lt_one
    (source : ι → ℝ) (failure : ι → Prop) (tau : ℝ)
    (hzero : ∀ i, failure i → source i = 0)
    (htotal : (∑ i, expDefect tau (source i)) < 1) :
    ∀ i, ¬ failure i := by
  apply no_failure_of_soft_detector_sum_lt_one
    source failure (expDefect tau)
  · intro x
    exact expDefect_nonneg tau x
  · intro i hi
    rw [hzero i hi]
    exact expDefect_zero tau
  · exact htotal

end Integer
end FortuneFormal
