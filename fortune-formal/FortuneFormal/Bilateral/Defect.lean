import Mathlib
import FortuneFormal.Bilateral.Definitions
import FortuneFormal.Bilateral.InverseFree

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

private theorem c_ne_zero_of_inverseFree (x : Datum F)
    (h : MuInverseFreeAt x x.c) : x.c ≠ 0 := by
  intro hc
  have htheta : x.P ∣ scalar x.theta := by
    apply x.P_coprime_Pp.dvd_of_dvd_mul_right
    simpa [MuInverseFreeAt, hc] using h.1
  have hscalar : scalar x.theta ≠ 0 := by
    exact Polynomial.C_ne_zero.mpr x.theta_ne_zero
  exact (Polynomial.not_dvd_of_natDegree_lt hscalar <| by
    rw [x.P_degree]
    simpa [scalar] using x.k_pos) htheta

private theorem d_ne_zero_of_inverseFree (x : Datum F)
    (h : NuInverseFreeAt x x.d) : x.d ≠ 0 := by
  intro hd
  have htheta : x.S ∣ scalar x.theta := by
    apply x.S_coprime_Sp.dvd_of_dvd_mul_right
    simpa [NuInverseFreeAt, hd] using h.1
  have hscalar : scalar x.theta ≠ 0 := by
    exact Polynomial.C_ne_zero.mpr x.theta_ne_zero
  exact (Polynomial.not_dvd_of_natDegree_lt hscalar <| by
    rw [x.S_degree]
    simpa [scalar] using x.k_pos) htheta

private theorem normalized_mu_divisibilities (x : Datum F)
    (hc : x.c ≠ 0) (h : MuInverseFreeAt x x.c) :
    x.P ∣ x.L * x.S - scalar (lambda x) * x.Pp ∧
    x.Pp ∣ x.L * x.Sp + scalar (lambda x) * x.P := by
  constructor
  · rcases h.1 with ⟨u, hu⟩
    refine ⟨scalar x.c⁻¹ * u, ?_⟩
    calc
      x.L * x.S - scalar (lambda x) * x.Pp =
          scalar x.c⁻¹ *
            (scalar x.c * x.L * x.S + scalar x.theta * x.Pp) := by
        simp [lambda, scalar, div_eq_mul_inv, hc]
        ring
      _ = scalar x.c⁻¹ * (x.P * u) := by rw [hu]
      _ = x.P * (scalar x.c⁻¹ * u) := by ring
  · rcases h.2 with ⟨u, hu⟩
    refine ⟨scalar x.c⁻¹ * u, ?_⟩
    calc
      x.L * x.Sp + scalar (lambda x) * x.P =
          scalar x.c⁻¹ *
            (scalar x.c * x.L * x.Sp - scalar x.theta * x.P) := by
        simp [lambda, scalar, div_eq_mul_inv, hc]
        ring
      _ = scalar x.c⁻¹ * (x.Pp * u) := by rw [hu]
      _ = x.Pp * (scalar x.c⁻¹ * u) := by ring

private theorem normalized_nu_divisibilities (x : Datum F)
    (hd : x.d ≠ 0) (h : NuInverseFreeAt x x.d) :
    x.S ∣ x.L * x.P + scalar (rho x) * x.Sp ∧
    x.Sp ∣ x.L * x.Pp - scalar (rho x) * x.S := by
  constructor
  · rcases h.1 with ⟨u, hu⟩
    refine ⟨scalar x.d⁻¹ * u, ?_⟩
    calc
      x.L * x.P + scalar (rho x) * x.Sp =
          scalar x.d⁻¹ *
            (scalar x.d * x.L * x.P + scalar x.theta * x.Sp) := by
        simp [rho, scalar, div_eq_mul_inv, hd]
        ring
      _ = scalar x.d⁻¹ * (x.S * u) := by rw [hu]
      _ = x.S * (scalar x.d⁻¹ * u) := by ring
  · rcases h.2 with ⟨u, hu⟩
    refine ⟨scalar x.d⁻¹ * u, ?_⟩
    calc
      x.L * x.Pp - scalar (rho x) * x.S =
          scalar x.d⁻¹ *
            (scalar x.d * x.L * x.Pp - scalar x.theta * x.S) := by
        simp [rho, scalar, div_eq_mul_inv, hd]
        ring
      _ = scalar x.d⁻¹ * (x.Sp * u) := by rw [hu]
      _ = x.Sp * (scalar x.d⁻¹ * u) := by ring

/-- The inverse-free incidence supplies the four quotient polynomials. -/
theorem quotientWitness_of_inverseFree (x : Datum F)
    (h : InverseFreeIncidence x) : Nonempty (QuotientWitness x) := by
  have hc := c_ne_zero_of_inverseFree x h.1
  have hd := d_ne_zero_of_inverseFree x h.2
  obtain ⟨hAP, hCPp⟩ := normalized_mu_divisibilities x hc h.1
  obtain ⟨hBS, hDSp⟩ := normalized_nu_divisibilities x hd h.2
  rcases hAP with ⟨A, hA⟩
  rcases hBS with ⟨B, hB⟩
  rcases hCPp with ⟨Cq, hC⟩
  rcases hDSp with ⟨Dq, hD⟩
  refine ⟨{
    A := A
    B := B
    Cq := Cq
    Dq := Dq
    AP := ?_
    BS := ?_
    CPp := ?_
    DSp := ?_
  }⟩
  · rw [mul_comm]
    exact hA.symm
  · rw [mul_comm]
    exact hB.symm
  · rw [mul_comm]
    exact hC.symm
  · rw [mul_comm]
    exact hD.symm

private theorem frobeniusBase_natDegree (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    x.L.natDegree = Fintype.card F := by
  rw [hbase]
  apply Polynomial.natDegree_sub_eq_left_of_natDegree_lt
  simp only [Polynomial.natDegree_X, Polynomial.natDegree_pow]
  simpa using hp.one_lt

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

/-- The defect degree is at most `q - 2k` on the prime Frobenius base. -/
theorem defectDegreeBound (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    DefectDegreeBound x := by
  intro h q hh
  by_cases hz : h = 0
  · simp [hz]
  have hdiff : (firstDifference x q).natDegree ≤ Fintype.card F := by
    unfold firstDifference
    apply le_trans (Polynomial.natDegree_sub_le _ _)
    apply max_le
    · apply le_trans Polynomial.natDegree_mul_le
      simpa [scalar] using quotient_Cq_natDegree_le x hp hbase q
    · apply le_trans Polynomial.natDegree_mul_le
      simpa [scalar] using quotient_B_natDegree_le x hp hbase q
  have hprod : (h * x.P * x.Sp).natDegree ≤ Fintype.card F := by
    rw [← hh.first]
    exact hdiff
  have heq : (h * x.P * x.Sp).natDegree = h.natDegree + 2 * x.k := by
    rw [Polynomial.natDegree_mul (mul_ne_zero hz x.P_monic.ne_zero) x.Sp_monic.ne_zero,
      Polynomial.natDegree_mul hz x.P_monic.ne_zero, x.P_degree, x.Sp_degree]
    omega
  rw [heq] at hprod
  exact Nat.le_sub_of_add_le hprod

/-- Kernel-level reconstruction of Paper VII BDD1 in its corrected manuscript scope. -/
theorem p7_bdd1_concrete (F : Type u) [Field F] [Fintype F] :
    (specification F).BDD1Statement := by
  intro x _ hp hbase _ hinc
  obtain ⟨q⟩ := quotientWitness_of_inverseFree x hinc
  obtain ⟨h, hh, huniq⟩ := commonDefect_of_quotient x q
  constructor
  · refine ⟨h, ⟨q, hh⟩, ?_⟩
    intro h' hex
    rcases hex with ⟨q', hh'⟩
    have heq : h * (x.P * x.Pp * x.S * x.Sp) =
        h' * (x.P * x.Pp * x.S * x.Sp) := by
      calc
        h * (x.P * x.Pp * x.S * x.Sp) = defectExpression x := by
          rw [← hh.product]
          ring
        _ = h' * (x.P * x.Pp * x.S * x.Sp) := by
          rw [← hh'.product]
          ring
    have hnonzero : x.P * x.Pp * x.S * x.Sp ≠ 0 := by
      exact mul_ne_zero (mul_ne_zero (mul_ne_zero x.P_monic.ne_zero x.Pp_monic.ne_zero)
        x.S_monic.ne_zero) x.Sp_monic.ne_zero
    exact mul_right_cancel₀ hnonzero heq
  · exact defectDegreeBound x hp hbase

end Bilateral
end FortuneFormal
