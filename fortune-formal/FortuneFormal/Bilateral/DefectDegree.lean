import Mathlib
import FortuneFormal.Bilateral.Definitions
import FortuneFormal.Bilateral.DefectCore

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

private theorem frobeniusBase_natDegree (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    x.L.natDegree = Fintype.card F := by
  rw [hbase]
  calc
    (Polynomial.X ^ Fintype.card F - Polynomial.X : Polynomial F).natDegree =
        (Polynomial.X ^ Fintype.card F : Polynomial F).natDegree :=
      Polynomial.natDegree_sub_eq_left_of_natDegree_lt (by
        simp only [Polynomial.natDegree_X, Polynomial.natDegree_pow]
        simpa using hp.one_lt)
    _ = Fintype.card F := by simp

private theorem quotient_Cq_natDegree_le (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (q : QuotientWitness x) : q.Cq.natDegree ≤ Fintype.card F := by
  have hL := frobeniusBase_natDegree x hp hbase
  have hright :
      (x.L * x.Sp + scalar (lambda x) * x.P).natDegree ≤
        Fintype.card F + x.k := by
    apply le_trans (Polynomial.natDegree_add_le _ _)
    apply max_le
    · apply le_trans Polynomial.natDegree_mul_le
      rw [hL, x.Sp_degree]
    · apply le_trans Polynomial.natDegree_mul_le
      simp [scalar, x.P_degree]
  have hprod : (q.Cq * x.Pp).natDegree ≤ Fintype.card F + x.k := by
    rw [q.CPp]
    exact hright
  by_cases hC : q.Cq = 0
  · simp [hC]
  · rw [Polynomial.natDegree_mul hC x.Pp_monic.ne_zero, x.Pp_degree] at hprod
    omega

private theorem quotient_B_natDegree_le (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (q : QuotientWitness x) : q.B.natDegree ≤ Fintype.card F := by
  have hL := frobeniusBase_natDegree x hp hbase
  have hright :
      (x.L * x.P + scalar (rho x) * x.Sp).natDegree ≤
        Fintype.card F + x.k := by
    apply le_trans (Polynomial.natDegree_add_le _ _)
    apply max_le
    · apply le_trans Polynomial.natDegree_mul_le
      rw [hL, x.P_degree]
    · apply le_trans Polynomial.natDegree_mul_le
      simp [scalar, x.Sp_degree]
  have hprod : (q.B * x.S).natDegree ≤ Fintype.card F + x.k := by
    rw [q.BS]
    exact hright
  by_cases hB : q.B = 0
  · simp [hB]
  · rw [Polynomial.natDegree_mul hB x.S_monic.ne_zero, x.S_degree] at hprod
    omega

/-- On the prime Frobenius base, the first quotient difference has degree at
most `q`.  This non-truncated estimate is the input needed to force the defect
to vanish when `q < 2k`. -/
theorem firstDifference_natDegree_le (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (q : QuotientWitness x) :
    (firstDifference x q).natDegree ≤ Fintype.card F := by
  unfold firstDifference
  apply le_trans (Polynomial.natDegree_sub_le _ _)
  apply max_le
  · apply le_trans Polynomial.natDegree_mul_le
    simpa [scalar] using quotient_Cq_natDegree_le x hp hbase q
  · apply le_trans Polynomial.natDegree_mul_le
    simpa [scalar] using quotient_B_natDegree_le x hp hbase q

/-- The defect degree is at most `q - 2k` on the prime Frobenius base. -/
theorem defectDegreeBound (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    DefectDegreeBound x := by
  intro h q hh
  by_cases hz : h = 0
  · simp [hz]
  have hdiff := firstDifference_natDegree_le x hp hbase q
  have hprod : (h * x.P * x.Sp).natDegree ≤ Fintype.card F := by
    rw [← hh.first]
    exact hdiff
  have heq : (h * x.P * x.Sp).natDegree = h.natDegree + 2 * x.k := by
    rw [Polynomial.natDegree_mul (mul_ne_zero hz x.P_monic.ne_zero) x.Sp_monic.ne_zero,
      Polynomial.natDegree_mul hz x.P_monic.ne_zero, x.P_degree, x.Sp_degree]
    omega
  rw [heq] at hprod
  exact Nat.le_sub_of_add_le hprod

end Bilateral
end FortuneFormal
