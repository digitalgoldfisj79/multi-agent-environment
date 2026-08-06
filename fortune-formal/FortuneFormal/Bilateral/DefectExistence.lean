import Mathlib
import FortuneFormal.Bilateral.DefectCore

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

universe u

variable {F : Type u} [Field F] [Fintype F]

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
    let prod : Polynomial F := x.P * x.Sp * x.S * x.Pp
    have heq : h₁ * prod = h₂ * prod := by
      calc
        h₁ * prod = firstDifference x q * x.S * x.Pp := by
          dsimp [prod]
          rw [hh₁]
          ring
        _ = defectExpression x := firstDifference_transfer x q
        _ = secondDifference x q * x.P * x.Sp :=
          (secondDifference_transfer x q).symm
        _ = h₂ * prod := by
          dsimp [prod]
          rw [hh₂]
          ring
    have hnonzero : prod ≠ 0 := by
      dsimp [prod]
      exact mul_ne_zero (mul_ne_zero (mul_ne_zero x.P_monic.ne_zero x.Sp_monic.ne_zero)
        x.S_monic.ne_zero) x.Pp_monic.ne_zero
    have hzero : (h₁ - h₂) * prod = 0 := by
      rw [sub_mul, heq, sub_self]
    exact sub_eq_zero.mp ((mul_eq_zero.mp hzero).resolve_right hnonzero)
  subst h₂
  let witness : DefectWitness x q h₁ := {
    first := by
      calc
        scalar (rho x) * q.Cq - scalar (lambda x) * q.B =
            x.P * x.Sp * h₁ := hh₁
        _ = h₁ * x.P * x.Sp := by ring
    second := by
      calc
        scalar (rho x) * q.A - scalar (lambda x) * q.Dq =
            x.S * x.Pp * h₁ := hh₂
        _ = h₁ * x.S * x.Pp := by ring
    product := by
      change h₁ * x.P * x.Pp * x.S * x.Sp = defectExpression x
      rw [← firstDifference_transfer x q, hh₁]
      ring
  }
  refine ⟨h₁, witness, ?_⟩
  intro h hh
  let prod : Polynomial F := x.P * x.Pp * x.S * x.Sp
  have heq : h₁ * prod = h * prod := by
    calc
      h₁ * prod = defectExpression x := by
        dsimp [prod]
        rw [← firstDifference_transfer x q, hh₁]
        ring
      _ = h * prod := by
        dsimp [prod]
        calc
          defectExpression x = h * x.P * x.Pp * x.S * x.Sp := hh.product.symm
          _ = h * (x.P * x.Pp * x.S * x.Sp) := by ring
  have hnonzero : prod ≠ 0 := by
    dsimp [prod]
    exact mul_ne_zero (mul_ne_zero (mul_ne_zero x.P_monic.ne_zero x.Pp_monic.ne_zero)
      x.S_monic.ne_zero) x.Sp_monic.ne_zero
  have hzero : (h - h₁) * prod = 0 := by
    rw [sub_mul, ← heq, sub_self]
  exact sub_eq_zero.mp ((mul_eq_zero.mp hzero).resolve_right hnonzero)

end Bilateral
end FortuneFormal
