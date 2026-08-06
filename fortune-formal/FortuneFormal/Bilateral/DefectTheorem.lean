import Mathlib
import FortuneFormal.Bilateral.DefectCore
import FortuneFormal.Bilateral.DefectExistence
import FortuneFormal.Bilateral.Quotient
import FortuneFormal.Bilateral.DefectDegree

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

universe u

/-- Kernel-level reconstruction of Paper VII BDD1 in its corrected manuscript scope. -/
theorem p7_bdd1_concrete (F : Type u) [Field F] [Fintype F] :
    (specification F).BDD1Statement := by
  change ∀ x : Datum F,
    CrossDistinct x →
    Nat.Prime (Fintype.card F) →
    FrobeniusBase x →
    x.k < Fintype.card F →
    InverseFreeIncidence x →
      CommonDefectExistsUnique x ∧ DefectDegreeBound x
  intro x _ hp hbase _ hinc
  obtain ⟨q⟩ := quotientWitness_of_inverseFree x hinc
  obtain ⟨h, hh, _⟩ := commonDefect_of_quotient x q
  constructor
  · refine ⟨h, ⟨q, hh⟩, ?_⟩
    intro h' hex
    rcases hex with ⟨q', hh'⟩
    let prod : Polynomial F := x.P * x.Pp * x.S * x.Sp
    have heq : h * prod = h' * prod := by
      calc
        h * prod = h * x.P * x.Pp * x.S * x.Sp := by
          dsimp [prod]
          ring
        _ = defectExpression x := hh.product
        _ = h' * x.P * x.Pp * x.S * x.Sp := hh'.product.symm
        _ = h' * prod := by
          dsimp [prod]
          ring
    have hnonzero : prod ≠ 0 := by
      dsimp [prod]
      exact mul_ne_zero (mul_ne_zero (mul_ne_zero x.P_monic.ne_zero x.Pp_monic.ne_zero)
        x.S_monic.ne_zero) x.Sp_monic.ne_zero
    have hzero : (h' - h) * prod = 0 := by
      rw [sub_mul, ← heq, sub_self]
    have hsub : h' - h = 0 :=
      (mul_eq_zero.mp hzero).resolve_right hnonzero
    exact sub_eq_zero.mp hsub
  · exact defectDegreeBound x hp hbase

end Bilateral
end FortuneFormal
