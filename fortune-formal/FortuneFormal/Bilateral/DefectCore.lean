import Mathlib
import FortuneFormal.Bilateral.Definitions

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

/-- The first quotient difference in the common-defect theorem. -/
def firstDifference (x : Datum F) (q : QuotientWitness x) : Polynomial F :=
  scalar (rho x) * q.Cq - scalar (lambda x) * q.B

/-- The second quotient difference in the common-defect theorem. -/
def secondDifference (x : Datum F) (q : QuotientWitness x) : Polynomial F :=
  scalar (rho x) * q.A - scalar (lambda x) * q.Dq

/-- The common transfer expression appearing in both quotient substitutions. -/
def defectExpression (x : Datum F) : Polynomial F :=
  x.L * (scalar (rho x) * x.S * x.Sp - scalar (lambda x) * x.P * x.Pp) +
    scalar (lambda x * rho x) * (x.P * x.S - x.Pp * x.Sp)

/-- First exact transfer identity obtained from the quotient equations. -/
theorem firstDifference_transfer (x : Datum F) (q : QuotientWitness x) :
    firstDifference x q * x.S * x.Pp = defectExpression x := by
  unfold firstDifference defectExpression
  calc
    (scalar (rho x) * q.Cq - scalar (lambda x) * q.B) * x.S * x.Pp =
        scalar (rho x) * x.S * (q.Cq * x.Pp) -
          scalar (lambda x) * x.Pp * (q.B * x.S) := by ring
    _ = scalar (rho x) * x.S *
          (x.L * x.Sp + scalar (lambda x) * x.P) -
        scalar (lambda x) * x.Pp *
          (x.L * x.P + scalar (rho x) * x.Sp) := by rw [q.CPp, q.BS]
    _ = x.L *
          (scalar (rho x) * x.S * x.Sp -
            scalar (lambda x) * x.P * x.Pp) +
        scalar (lambda x * rho x) *
          (x.P * x.S - x.Pp * x.Sp) := by
      simp only [scalar, map_mul]
      ring

/-- Second exact transfer identity obtained from the quotient equations. -/
theorem secondDifference_transfer (x : Datum F) (q : QuotientWitness x) :
    secondDifference x q * x.P * x.Sp = defectExpression x := by
  unfold secondDifference defectExpression
  calc
    (scalar (rho x) * q.A - scalar (lambda x) * q.Dq) * x.P * x.Sp =
        scalar (rho x) * x.Sp * (q.A * x.P) -
          scalar (lambda x) * x.P * (q.Dq * x.Sp) := by ring
    _ = scalar (rho x) * x.Sp *
          (x.L * x.S - scalar (lambda x) * x.Pp) -
        scalar (lambda x) * x.P *
          (x.L * x.Pp - scalar (rho x) * x.S) := by rw [q.AP, q.DSp]
    _ = x.L *
          (scalar (rho x) * x.S * x.Sp -
            scalar (lambda x) * x.P * x.Pp) +
        scalar (lambda x * rho x) *
          (x.P * x.S - x.Pp * x.Sp) := by
      simp only [scalar, map_mul]
      ring

private theorem firstDifference_dvd_P (x : Datum F) (q : QuotientWitness x) :
    x.P ∣ firstDifference x q := by
  have hprod : x.P ∣ firstDifference x q * (x.S * x.Pp) := by
    refine ⟨secondDifference x q * x.Sp, ?_⟩
    calc
      firstDifference x q * (x.S * x.Pp) = defectExpression x := by
        simpa [mul_assoc] using firstDifference_transfer x q
      _ = secondDifference x q * x.P * x.Sp :=
        (secondDifference_transfer x q).symm
      _ = x.P * (secondDifference x q * x.Sp) := by ring
  exact (x.P_coprime_S.mul_right x.P_coprime_Pp).dvd_of_dvd_mul_right hprod

private theorem firstDifference_dvd_Sp (x : Datum F) (q : QuotientWitness x) :
    x.Sp ∣ firstDifference x q := by
  have hprod : x.Sp ∣ firstDifference x q * (x.S * x.Pp) := by
    refine ⟨secondDifference x q * x.P, ?_⟩
    calc
      firstDifference x q * (x.S * x.Pp) = defectExpression x := by
        simpa [mul_assoc] using firstDifference_transfer x q
      _ = secondDifference x q * x.P * x.Sp :=
        (secondDifference_transfer x q).symm
      _ = x.Sp * (secondDifference x q * x.P) := by ring
  exact
    (x.S_coprime_Sp.symm.mul_right x.Pp_coprime_Sp.symm).dvd_of_dvd_mul_right hprod

private theorem secondDifference_dvd_S (x : Datum F) (q : QuotientWitness x) :
    x.S ∣ secondDifference x q := by
  have hprod : x.S ∣ secondDifference x q * (x.P * x.Sp) := by
    refine ⟨firstDifference x q * x.Pp, ?_⟩
    calc
      secondDifference x q * (x.P * x.Sp) = defectExpression x := by
        simpa [mul_assoc] using secondDifference_transfer x q
      _ = firstDifference x q * x.S * x.Pp :=
        (firstDifference_transfer x q).symm
      _ = x.S * (firstDifference x q * x.Pp) := by ring
  exact
    (x.P_coprime_S.symm.mul_right x.S_coprime_Sp).dvd_of_dvd_mul_right hprod

private theorem secondDifference_dvd_Pp (x : Datum F) (q : QuotientWitness x) :
    x.Pp ∣ secondDifference x q := by
  have hprod : x.Pp ∣ secondDifference x q * (x.P * x.Sp) := by
    refine ⟨firstDifference x q * x.S, ?_⟩
    calc
      secondDifference x q * (x.P * x.Sp) = defectExpression x := by
        simpa [mul_assoc] using secondDifference_transfer x q
      _ = firstDifference x q * x.S * x.Pp :=
        (firstDifference_transfer x q).symm
      _ = x.Pp * (firstDifference x q * x.S) := by ring
  exact
    (x.P_coprime_Pp.symm.mul_right x.Pp_coprime_Sp).dvd_of_dvd_mul_right hprod

/-- Every quotient witness determines a unique common defect satisfying all
three manuscript identities. -/
theorem commonDefect_of_quotient (x : Datum F) (q : QuotientWitness x) :
    ∃! h : Polynomial F, DefectWitness x q h := by
  have hfirst : x.P * x.Sp ∣ firstDifference x q :=
    x.P_coprime_Sp.mul_dvd (firstDifference_dvd_P x q) (firstDifference_dvd_Sp x q)
  have hsecond : x.S * x.Pp ∣ secondDifference x q :=
    x.S_coprime_Pp.mul_dvd (secondDifference_dvd_S x q) (secondDifference_dvd_Pp x q)
  rcases hfirst with ⟨h₁, hh₁⟩
  rcases hsecond with ⟨h₂, hh₂⟩
  have hcommon : h₁ = h₂ := by
    have heq : h₁ * (x.P * x.Sp * x.S * x.Pp) =
        h₂ * (x.P * x.Sp * x.S * x.Pp) := by
      calc
        h₁ * (x.P * x.Sp * x.S * x.Pp) =
            firstDifference x q * x.S * x.Pp := by rw [hh₁]; ring
        _ = defectExpression x := firstDifference_transfer x q
        _ = secondDifference x q * x.P * x.Sp :=
          (secondDifference_transfer x q).symm
        _ = h₂ * (x.P * x.Sp * x.S * x.Pp) := by rw [hh₂]; ring
    have hnonzero : x.P * x.Sp * x.S * x.Pp ≠ 0 := by
      exact mul_ne_zero (mul_ne_zero (mul_ne_zero x.P_monic.ne_zero x.Sp_monic.ne_zero)
        x.S_monic.ne_zero) x.Pp_monic.ne_zero
    exact mul_right_cancel₀ hnonzero heq
  subst h₂
  refine ⟨h₁, ?_, ?_⟩
  · constructor
    · simpa [firstDifference] using hh₁
    · constructor
      · simpa [secondDifference] using hh₂
      · calc
          h₁ * x.P * x.Pp * x.S * x.Sp =
              firstDifference x q * x.S * x.Pp := by rw [hh₁]; ring
          _ = defectExpression x := firstDifference_transfer x q
          _ = x.L *
                (scalar (rho x) * x.S * x.Sp -
                  scalar (lambda x) * x.P * x.Pp) +
              scalar (lambda x * rho x) *
                (x.P * x.S - x.Pp * x.Sp) := rfl
  · intro h hh
    have heq : h₁ * (x.P * x.Pp * x.S * x.Sp) =
        h * (x.P * x.Pp * x.S * x.Sp) := by
      calc
        h₁ * (x.P * x.Pp * x.S * x.Sp) = defectExpression x := by
          rw [← firstDifference_transfer x q, hh₁]
          ring
        _ = h * (x.P * x.Pp * x.S * x.Sp) := by
          rw [← hh.product]
          ring
    have hnonzero : x.P * x.Pp * x.S * x.Sp ≠ 0 := by
      exact mul_ne_zero (mul_ne_zero (mul_ne_zero x.P_monic.ne_zero x.Pp_monic.ne_zero)
        x.S_monic.ne_zero) x.Sp_monic.ne_zero
    exact mul_right_cancel₀ hnonzero heq

end Bilateral
end FortuneFormal
