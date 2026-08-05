import FortuneFormal.Integer.SoftDefectCriterion
import Mathlib.Analysis.SpecialFunctions.Exp

set_option autoImplicit false

namespace FortuneFormal
namespace Integer

open scoped BigOperators

universe u

variable {ι : Type u} [Fintype ι]

/-- A row-dependent exponential detector remains a valid one-defect detector:
a failed row has source zero and contributes exactly one. -/
theorem no_failure_of_rowDependentExp_sum_lt_one
    (source tau : ι → ℝ) (failure : ι → Prop)
    (hzero : ∀ i, failure i → source i = 0)
    (htotal : (∑ i, Real.exp (-tau i * source i)) < 1) :
    ∀ i, ¬ failure i := by
  intro i hi
  have hnonneg : ∀ k, 0 ≤ Real.exp (-tau k * source k) := by
    intro k
    exact le_of_lt (Real.exp_pos _)
  have hterm : Real.exp (-tau i * source i) ≤
      ∑ k, Real.exp (-tau k * source k) := by
    exact Finset.single_le_sum
      (fun k _ => hnonneg k)
      (Finset.mem_univ i)
  rw [hzero i hi] at hterm
  simp at hterm
  have htotal' : (∑ k, Real.exp (-(tau k * source k))) < 1 := by
    simpa only [neg_mul] using htotal
  exact (not_lt_of_ge hterm) htotal'

/-- If each preregistered row temperature is at most the frozen uniform
temperature, then the uniform detector is termwise no larger. -/
theorem uniformExp_le_rowDependentExp
    (source tau : ℝ) (uniformTau : ℝ)
    (hsource : 0 ≤ source)
    (htau : tau ≤ uniformTau) :
    Real.exp (-uniformTau * source) ≤ Real.exp (-tau * source) := by
  apply Real.exp_le_exp.mpr
  nlinarith

/-- A successful row-dependent detector with temperatures below the frozen
uniform temperature implies the frozen INT-AOD detector bound. -/
theorem uniformExp_sum_lt_one_of_rowDependent
    (source tau : ι → ℝ) (uniformTau : ℝ)
    (hsource : ∀ i, 0 ≤ source i)
    (htau : ∀ i, tau i ≤ uniformTau)
    (hrow : (∑ i, Real.exp (-tau i * source i)) < 1) :
    (∑ i, Real.exp (-uniformTau * source i)) < 1 := by
  have hle : (∑ i, Real.exp (-uniformTau * source i)) ≤
      ∑ i, Real.exp (-tau i * source i) := by
    apply Finset.sum_le_sum
    intro i hi
    exact uniformExp_le_rowDependentExp
      (source i) (tau i) uniformTau (hsource i) (htau i)
  exact lt_of_le_of_lt hle hrow

end Integer
end FortuneFormal
