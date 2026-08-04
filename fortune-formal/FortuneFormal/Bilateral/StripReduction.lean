import Mathlib
import FortuneFormal.Bilateral.BDD2Conditional
import FortuneFormal.Bilateral.DefectDegree
import FortuneFormal.Bilateral.DefectExistence
import FortuneFormal.Bilateral.Quotient

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

private theorem frobeniusBase_monic_strip (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    x.L.Monic := by
  rw [hbase, sub_eq_add_neg]
  apply Polynomial.monic_X_pow_add
  simpa using hp.one_lt

private theorem frobeniusBase_degree_strip (x : Datum F)
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

/-- If `q < 2k`, the common defect is zero.  This is a direct degree
contradiction and therefore does not rely on truncated natural subtraction. -/
theorem defect_eq_zero_of_card_lt_two_mul (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (hstrip : Fintype.card F < 2 * x.k)
    (q : QuotientWitness x) (h : Polynomial F)
    (hh : DefectWitness x q h) : h = 0 := by
  by_contra hz
  have hdiff := firstDifference_natDegree_le x hp hbase q
  have hprod : (h * x.P * x.Sp).natDegree ≤ Fintype.card F := by
    rw [← hh.first]
    exact hdiff
  have heq : (h * x.P * x.Sp).natDegree = h.natDegree + 2 * x.k := by
    rw [Polynomial.natDegree_mul (mul_ne_zero hz x.P_monic.ne_zero) x.Sp_monic.ne_zero,
      Polynomial.natDegree_mul hz x.P_monic.ne_zero, x.P_degree, x.Sp_degree]
    omega
  rw [heq] at hprod
  omega

private theorem sub_natDegree_le_k
    (x : Datum F) : (x.Pp - x.P).natDegree ≤ x.k := by
  exact (Polynomial.natDegree_sub_le _ _).trans <| by
    rw [x.Pp_degree, x.P_degree, max_self]

private theorem add_natDegree_le_k
    (x : Datum F) : (x.Pp + x.P).natDegree ≤ x.k := by
  exact (Polynomial.natDegree_add_le _ _).trans <| by
    rw [x.Pp_degree, x.P_degree, max_self]

/-- Neither zero-defect family can occur when the Frobenius-base degree exceeds
the modulus degree. -/
theorem no_reflectionOrTranslation_above_modulus (x : Datum F)
    (hcross : CrossDistinct x)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (hk : x.k < Fintype.card F) :
    ¬ ReflectionOrTranslation x := by
  have hLmonic := frobeniusBase_monic_strip x hp hbase
  have hLdegree := frobeniusBase_degree_strip x hp hbase
  intro hfamily
  rcases hfamily with href | htrans
  · rcases href with ⟨Q, hPp, hS, _⟩
    have hQ : Q ≠ 0 := by
      intro hQ
      have hSP : x.S = x.P := by simpa [hQ] using hS
      exact hcross.1 hSP.symm
    have hsum : x.Pp + x.P = x.L * Q := by
      linear_combination hPp
    have hdegLeft : (x.Pp + x.P).natDegree ≤ x.k := add_natDegree_le_k x
    have hdegRight : (x.L * Q).natDegree = Fintype.card F + Q.natDegree := by
      rw [hLmonic.natDegree_mul (Polynomial.monic_of_leadingCoeff_eq_one <| by
        have hlead : Q.leadingCoeff ≠ 0 := Polynomial.leadingCoeff_ne_zero.mpr hQ
        exact one_ne_zero) ]
    have hQmonicFree : (x.L * Q).natDegree = x.L.natDegree + Q.natDegree :=
      Polynomial.natDegree_mul x.L_monic_or hQ
    rw [hsum] at hdegLeft
    rw [Polynomial.natDegree_mul hLmonic.ne_zero hQ, hLdegree] at hdegLeft
    omega
  · rcases htrans with ⟨R, hPp, hS, _⟩
    have hR : R ≠ 0 := by
      intro hR
      have hSP : x.S = x.P := by simpa [hR] using hS
      exact hcross.1 hSP.symm
    have hsub : x.Pp - x.P = x.L * R := by
      linear_combination hPp
    have hdegLeft : (x.Pp - x.P).natDegree ≤ x.k := sub_natDegree_le_k x
    rw [hsub, Polynomial.natDegree_mul hLmonic.ne_zero hR, hLdegree] at hdegLeft
    omega

/-- Conditional strip theorem: every step except the same isolated
Artin-Schreier support theorem is kernel checked. -/
theorem p7_strip_of_artinSchreier
    (F : Type u) [Field F] [Fintype F]
    (hartin : ArtinSchreierSupport F) :
    (specification F).StripStatement := by
  change ∀ x : Datum F,
    CrossDistinct x →
    Nat.Prime (Fintype.card F) →
    Odd (Fintype.card F) →
    FrobeniusBase x →
    x.k < Fintype.card F →
    Fintype.card F < 2 * x.k →
      ¬ InverseFreeIncidence x
  intro x hcross hp hodd hbase hk hstrip hinc
  obtain ⟨q⟩ := quotientWitness_of_inverseFree x hinc
  obtain ⟨h, hh, _⟩ := commonDefect_of_quotient x q
  have hz : h = 0 :=
    defect_eq_zero_of_card_lt_two_mul x hp hbase hstrip q h hh
  have hzero : ZeroDefect x := by
    refine ⟨q, ?_⟩
    simpa [hz] using hh
  have hclass : ReflectionOrTranslation x :=
    p7_bdd2_of_artinSchreier F hartin x hcross hp hodd hbase hk hinc hzero
  exact no_reflectionOrTranslation_above_modulus x hcross hp hbase hk hclass

end Bilateral
end FortuneFormal
