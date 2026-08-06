import Mathlib
import FortuneFormal.Bilateral.Definitions

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

private theorem scalar_inv_mul_scalar (a : F) (ha : a ≠ 0) :
    scalar a⁻¹ * scalar a = (1 : Polynomial F) := by
  rw [← map_mul]
  simp [ha]

private theorem scalar_lambda_eq (x : Datum F) :
    scalar (lambda x) = -(scalar x.theta * scalar x.c⁻¹) := by
  simp [lambda, scalar, div_eq_mul_inv]

private theorem scalar_rho_eq (x : Datum F) :
    scalar (rho x) = scalar x.theta * scalar x.d⁻¹ := by
  simp [rho, scalar, div_eq_mul_inv]

private theorem c_ne_zero_of_inverseFree (x : Datum F)
    (h : MuInverseFreeAt x x.c) : x.c ≠ 0 := by
  intro hc
  have htheta : x.P ∣ scalar x.theta := by
    apply x.P_coprime_Pp.dvd_of_dvd_mul_right
    simpa [MuInverseFreeAt, hc] using h.1
  have hscalar : scalar x.theta ≠ 0 :=
    Polynomial.C_ne_zero.mpr x.theta_ne_zero
  exact (Polynomial.not_dvd_of_natDegree_lt hscalar <| by
    rw [x.P_degree]
    simpa [scalar] using x.k_pos) htheta

private theorem d_ne_zero_of_inverseFree (x : Datum F)
    (h : NuInverseFreeAt x x.d) : x.d ≠ 0 := by
  intro hd
  have htheta : x.S ∣ scalar x.theta := by
    apply x.S_coprime_Sp.dvd_of_dvd_mul_right
    simpa [NuInverseFreeAt, hd] using h.1
  have hscalar : scalar x.theta ≠ 0 :=
    Polynomial.C_ne_zero.mpr x.theta_ne_zero
  exact (Polynomial.not_dvd_of_natDegree_lt hscalar <| by
    rw [x.S_degree]
    simpa [scalar] using x.k_pos) htheta

private theorem normalized_mu_divisibilities (x : Datum F)
    (hc : x.c ≠ 0) (h : MuInverseFreeAt x x.c) :
    x.P ∣ x.L * x.S - scalar (lambda x) * x.Pp ∧
    x.Pp ∣ x.L * x.Sp + scalar (lambda x) * x.P := by
  have hcinv := scalar_inv_mul_scalar x.c hc
  have hlam := scalar_lambda_eq x
  constructor
  · rcases h.1 with ⟨u, hu⟩
    refine ⟨scalar x.c⁻¹ * u, ?_⟩
    calc
      x.L * x.S - scalar (lambda x) * x.Pp =
          (scalar x.c⁻¹ * scalar x.c) * (x.L * x.S) +
            (scalar x.c⁻¹ * scalar x.theta) * x.Pp := by
        rw [hlam, hcinv]
        ring
      _ = scalar x.c⁻¹ *
            (scalar x.c * x.L * x.S + scalar x.theta * x.Pp) := by ring
      _ = scalar x.c⁻¹ * (x.P * u) := by rw [hu]
      _ = x.P * (scalar x.c⁻¹ * u) := by ring
  · rcases h.2 with ⟨u, hu⟩
    refine ⟨scalar x.c⁻¹ * u, ?_⟩
    calc
      x.L * x.Sp + scalar (lambda x) * x.P =
          (scalar x.c⁻¹ * scalar x.c) * (x.L * x.Sp) -
            (scalar x.c⁻¹ * scalar x.theta) * x.P := by
        rw [hlam, hcinv]
        ring
      _ = scalar x.c⁻¹ *
            (scalar x.c * x.L * x.Sp - scalar x.theta * x.P) := by ring
      _ = scalar x.c⁻¹ * (x.Pp * u) := by rw [hu]
      _ = x.Pp * (scalar x.c⁻¹ * u) := by ring

private theorem normalized_nu_divisibilities (x : Datum F)
    (hd : x.d ≠ 0) (h : NuInverseFreeAt x x.d) :
    x.S ∣ x.L * x.P + scalar (rho x) * x.Sp ∧
    x.Sp ∣ x.L * x.Pp - scalar (rho x) * x.S := by
  have hdinv := scalar_inv_mul_scalar x.d hd
  have hrho := scalar_rho_eq x
  constructor
  · rcases h.1 with ⟨u, hu⟩
    refine ⟨scalar x.d⁻¹ * u, ?_⟩
    calc
      x.L * x.P + scalar (rho x) * x.Sp =
          (scalar x.d⁻¹ * scalar x.d) * (x.L * x.P) +
            (scalar x.d⁻¹ * scalar x.theta) * x.Sp := by
        rw [hrho, hdinv]
        ring
      _ = scalar x.d⁻¹ *
            (scalar x.d * x.L * x.P + scalar x.theta * x.Sp) := by ring
      _ = scalar x.d⁻¹ * (x.S * u) := by rw [hu]
      _ = x.S * (scalar x.d⁻¹ * u) := by ring
  · rcases h.2 with ⟨u, hu⟩
    refine ⟨scalar x.d⁻¹ * u, ?_⟩
    calc
      x.L * x.Pp - scalar (rho x) * x.S =
          (scalar x.d⁻¹ * scalar x.d) * (x.L * x.Pp) -
            (scalar x.d⁻¹ * scalar x.theta) * x.S := by
        rw [hrho, hdinv]
        ring
      _ = scalar x.d⁻¹ *
            (scalar x.d * x.L * x.Pp - scalar x.theta * x.S) := by ring
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

end Bilateral
end FortuneFormal
