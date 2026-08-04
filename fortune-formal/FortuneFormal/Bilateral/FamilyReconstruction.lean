import Mathlib
import FortuneFormal.Bilateral.ArtinSchreierFactor

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

private theorem scalar_inv_mul_scalar_reconstruct (a : F) (ha : a ≠ 0) :
    scalar a⁻¹ * scalar a = (1 : Polynomial F) := by
  rw [← map_mul]
  simp [ha]

private theorem L_ne_zero (x : Datum F) : x.L ≠ 0 := by
  intro hL
  have hdiv : x.P ∣ x.L := by simp [hL]
  have hunit : IsUnit x.P := x.L_coprime_P.symm.isUnit_of_dvd hdiv
  exact x.P_irreducible.not_isUnit hunit

/-- The ordering `A=L-λ`, `B=L+λ` reconstructs the translation family. -/
theorem translationFamily_of_factorOrdering (x : Datum F) (q : QuotientWitness x)
    (hnormal : ZeroDefectNormalForm x q) (hlambda : lambda x ≠ 0)
    (hA : q.A = x.L - scalar (lambda x))
    (hB : q.B = x.L + scalar (lambda x)) : TranslationFamily x := by
  let R : Polynomial F := scalar (lambda x)⁻¹ * (x.S - x.P)
  have hinv := scalar_inv_mul_scalar_reconstruct (lambda x) hlambda
  have hAP := q.AP
  rw [hA] at hAP
  have htransfer :
      scalar (lambda x) * (x.Pp - x.P) = x.L * (x.S - x.P) := by
    linear_combination hAP
  have hPpSub : x.Pp - x.P = x.L * R := by
    calc
      x.Pp - x.P = (scalar (lambda x)⁻¹ * scalar (lambda x)) *
          (x.Pp - x.P) := by rw [hinv, one_mul]
      _ = scalar (lambda x)⁻¹ *
          (scalar (lambda x) * (x.Pp - x.P)) := by ring
      _ = scalar (lambda x)⁻¹ * (x.L * (x.S - x.P)) := by rw [htransfer]
      _ = x.L * R := by dsimp [R]; ring
  have hPp : x.Pp = x.P + x.L * R := by
    linear_combination hPpSub
  have hSSub : x.S - x.P = scalar (lambda x) * R := by
    calc
      x.S - x.P = (scalar (lambda x)⁻¹ * scalar (lambda x)) *
          (x.S - x.P) := by rw [hinv, one_mul]
      _ = scalar (lambda x) * R := by dsimp [R]; ring
  have hS : x.S = x.P + scalar (lambda x) * R := by
    linear_combination hSSub
  have hcp := q.CPp
  rw [hnormal.C_eq_B, hB, hPp] at hcp
  have hSpEq : x.S + x.L * R = x.Sp := by
    have heq : x.L * (x.S + x.L * R) = x.L * x.Sp := by
      calc
        x.L * (x.S + x.L * R) =
            (x.L + scalar (lambda x)) * (x.P + x.L * R) -
              scalar (lambda x) * x.P := by rw [hS]; ring
        _ = x.L * x.Sp := by rw [hcp]; ring
    have hzero : x.L * ((x.S + x.L * R) - x.Sp) = 0 := by
      rw [mul_sub, heq, sub_self]
    exact sub_eq_zero.mp ((mul_eq_zero.mp hzero).resolve_left (L_ne_zero x))
  exact ⟨R, hPp, hS, hSpEq.symm⟩

/-- The ordering `A=L+λ`, `B=L-λ` reconstructs the reflection family. -/
theorem reflectionFamily_of_factorOrdering (x : Datum F) (q : QuotientWitness x)
    (hnormal : ZeroDefectNormalForm x q) (hlambda : lambda x ≠ 0)
    (hA : q.A = x.L + scalar (lambda x))
    (hB : q.B = x.L - scalar (lambda x)) : ReflectionFamily x := by
  let Q : Polynomial F := scalar (lambda x)⁻¹ * (x.S - x.P)
  have hinv := scalar_inv_mul_scalar_reconstruct (lambda x) hlambda
  have hAP := q.AP
  rw [hA] at hAP
  have htransfer :
      scalar (lambda x) * (x.Pp + x.P) = x.L * (x.S - x.P) := by
    linear_combination hAP
  have hPsum : x.Pp + x.P = x.L * Q := by
    calc
      x.Pp + x.P = (scalar (lambda x)⁻¹ * scalar (lambda x)) *
          (x.Pp + x.P) := by rw [hinv, one_mul]
      _ = scalar (lambda x)⁻¹ *
          (scalar (lambda x) * (x.Pp + x.P)) := by ring
      _ = scalar (lambda x)⁻¹ * (x.L * (x.S - x.P)) := by rw [htransfer]
      _ = x.L * Q := by dsimp [Q]; ring
  have hPp : x.Pp = x.L * Q - x.P := by
    linear_combination hPsum
  have hSSub : x.S - x.P = scalar (lambda x) * Q := by
    calc
      x.S - x.P = (scalar (lambda x)⁻¹ * scalar (lambda x)) *
          (x.S - x.P) := by rw [hinv, one_mul]
      _ = scalar (lambda x) * Q := by dsimp [Q]; ring
  have hS : x.S = x.P + scalar (lambda x) * Q := by
    linear_combination hSSub
  have hcp := q.CPp
  rw [hnormal.C_eq_B, hB, hPp] at hcp
  have hSpEq : x.L * Q - x.S = x.Sp := by
    have heq : x.L * (x.L * Q - x.S) = x.L * x.Sp := by
      calc
        x.L * (x.L * Q - x.S) =
            (x.L - scalar (lambda x)) * (x.L * Q - x.P) -
              scalar (lambda x) * x.P := by rw [hS]; ring
        _ = x.L * x.Sp := by rw [hcp]; ring
    have hzero : x.L * ((x.L * Q - x.S) - x.Sp) = 0 := by
      rw [mul_sub, heq, sub_self]
    exact sub_eq_zero.mp ((mul_eq_zero.mp hzero).resolve_left (L_ne_zero x))
  exact ⟨Q, hPp, hS, hSpEq.symm⟩

/-- Either factor ordering gives precisely one of the two zero-defect families. -/
theorem reflectionOrTranslation_of_factorOrdering (x : Datum F) (q : QuotientWitness x)
    (hnormal : ZeroDefectNormalForm x q) (hlambda : lambda x ≠ 0)
    (horder :
      (q.A = x.L - scalar (lambda x) ∧
          q.B = x.L + scalar (lambda x)) ∨
       (q.A = x.L + scalar (lambda x) ∧
          q.B = x.L - scalar (lambda x))) :
    ReflectionOrTranslation x := by
  rcases horder with htrans | href
  · exact Or.inr <| translationFamily_of_factorOrdering x q hnormal hlambda htrans.1 htrans.2
  · exact Or.inl <| reflectionFamily_of_factorOrdering x q hnormal hlambda href.1 href.2

end Bilateral
end FortuneFormal
