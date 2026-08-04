import Mathlib
import FortuneFormal.Bilateral.Definitions

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

private theorem muError_natDegree_lt (x : Datum F) (c : F) :
    (x.mu * x.Pp - x.mup * x.P - scalar c).natDegree < 2 * x.k := by
  have hmu : (x.mu * x.Pp).natDegree < 2 * x.k := by
    calc
      (x.mu * x.Pp).natDegree ≤ x.mu.natDegree + x.Pp.natDegree :=
        Polynomial.natDegree_mul_le
      _ < x.k + x.k := by rw [x.Pp_degree]; omega
      _ = 2 * x.k := by omega
  have hmup : (x.mup * x.P).natDegree < 2 * x.k := by
    calc
      (x.mup * x.P).natDegree ≤ x.mup.natDegree + x.P.natDegree :=
        Polynomial.natDegree_mul_le
      _ < x.k + x.k := by rw [x.P_degree]; omega
      _ = 2 * x.k := by omega
  have hpair : (x.mu * x.Pp - x.mup * x.P).natDegree < 2 * x.k :=
    lt_of_le_of_lt (Polynomial.natDegree_sub_le _ _) (max_lt hmu hmup)
  have hscalar : (scalar c).natDegree < 2 * x.k := by
    simp only [scalar, Polynomial.natDegree_C]
    omega
  exact lt_of_le_of_lt (Polynomial.natDegree_sub_le _ _) (max_lt hpair hscalar)

private theorem nuError_natDegree_lt (x : Datum F) (d : F) :
    (x.nu * x.Sp - x.nup * x.S - scalar d).natDegree < 2 * x.k := by
  have hnu : (x.nu * x.Sp).natDegree < 2 * x.k := by
    calc
      (x.nu * x.Sp).natDegree ≤ x.nu.natDegree + x.Sp.natDegree :=
        Polynomial.natDegree_mul_le
      _ < x.k + x.k := by rw [x.Sp_degree]; omega
      _ = 2 * x.k := by omega
  have hnup : (x.nup * x.S).natDegree < 2 * x.k := by
    calc
      (x.nup * x.S).natDegree ≤ x.nup.natDegree + x.S.natDegree :=
        Polynomial.natDegree_mul_le
      _ < x.k + x.k := by rw [x.S_degree]; omega
      _ = 2 * x.k := by omega
  have hpair : (x.nu * x.Sp - x.nup * x.S).natDegree < 2 * x.k :=
    lt_of_le_of_lt (Polynomial.natDegree_sub_le _ _) (max_lt hnu hnup)
  have hscalar : (scalar d).natDegree < 2 * x.k := by
    simp only [scalar, Polynomial.natDegree_C]
    omega
  exact lt_of_le_of_lt (Polynomial.natDegree_sub_le _ _) (max_lt hpair hscalar)

/-- The first endpoint identity implies its two inverse-free divisibilities. -/
theorem muEndpoint_implies_inverseFree (x : Datum F) {c : F}
    (h : MuEndpointAt x c) : MuInverseFreeAt x c := by
  constructor
  · rcases x.mu_congruence with ⟨u, hu⟩
    refine ⟨x.Pp * u - x.mup * x.L * x.S, ?_⟩
    calc
      scalar c * x.L * x.S + scalar x.theta * x.Pp =
          x.Pp * (x.L * x.S * x.mu + scalar x.theta) -
            x.P * (x.mup * x.L * x.S) := by rw [← h]; ring
      _ = x.Pp * (x.P * u) - x.P * (x.mup * x.L * x.S) := by rw [hu]
      _ = x.P * (x.Pp * u - x.mup * x.L * x.S) := by ring
  · rcases x.mup_congruence with ⟨u, hu⟩
    refine ⟨x.mu * x.L * x.Sp - x.P * u, ?_⟩
    calc
      scalar c * x.L * x.Sp - scalar x.theta * x.P =
          x.Pp * (x.mu * x.L * x.Sp) -
            x.P * (x.L * x.Sp * x.mup + scalar x.theta) := by rw [← h]; ring
      _ = x.Pp * (x.mu * x.L * x.Sp) - x.P * (x.Pp * u) := by rw [hu]
      _ = x.Pp * (x.mu * x.L * x.Sp - x.P * u) := by ring

/-- The second endpoint identity implies its two inverse-free divisibilities. -/
theorem nuEndpoint_implies_inverseFree (x : Datum F) {d : F}
    (h : NuEndpointAt x d) : NuInverseFreeAt x d := by
  constructor
  · rcases x.nu_congruence with ⟨u, hu⟩
    refine ⟨x.Sp * u - x.nup * x.L * x.P, ?_⟩
    calc
      scalar d * x.L * x.P + scalar x.theta * x.Sp =
          x.Sp * (x.L * x.P * x.nu + scalar x.theta) -
            x.S * (x.nup * x.L * x.P) := by rw [← h]; ring
      _ = x.Sp * (x.S * u) - x.S * (x.nup * x.L * x.P) := by rw [hu]
      _ = x.S * (x.Sp * u - x.nup * x.L * x.P) := by ring
  · rcases x.nup_congruence with ⟨u, hu⟩
    refine ⟨x.nu * x.L * x.Pp - x.S * u, ?_⟩
    calc
      scalar d * x.L * x.Pp - scalar x.theta * x.S =
          x.Sp * (x.nu * x.L * x.Pp) -
            x.S * (x.L * x.Pp * x.nup + scalar x.theta) := by rw [← h]; ring
      _ = x.Sp * (x.nu * x.L * x.Pp) - x.S * (x.Sp * u) := by rw [hu]
      _ = x.Sp * (x.nu * x.L * x.Pp - x.S * u) := by ring

/-- The first two inverse-free divisibilities recover the scalar endpoint identity. -/
theorem muInverseFree_implies_endpoint (x : Datum F) {c : F}
    (h : MuInverseFreeAt x c) : MuEndpointAt x c := by
  have hscaledP : x.P ∣ (x.L * x.S) * (x.mu * x.Pp - scalar c) := by
    have h₁ := x.mu_congruence.mul_right x.Pp
    have h₂ := h.1
    have hsub := dvd_sub h₁ h₂
    convert hsub using 1 <;> ring
  have hbaseP : x.P ∣ x.mu * x.Pp - scalar c :=
    (x.L_coprime_P.symm.mul_right x.P_coprime_S).dvd_of_dvd_mul_left hscaledP
  have herrorP : x.P ∣ x.mu * x.Pp - x.mup * x.P - scalar c := by
    have hmup : x.P ∣ x.mup * x.P := ⟨x.mup, by ring⟩
    have := dvd_sub hbaseP hmup
    convert this using 1 <;> ring
  have hscaledPp : x.Pp ∣ (x.L * x.Sp) * (scalar c + x.mup * x.P) := by
    have h₁ := h.2
    have h₂ := x.mup_congruence.mul_right x.P
    have hadd := dvd_add h₁ h₂
    convert hadd using 1 <;> ring
  have hbasePp : x.Pp ∣ scalar c + x.mup * x.P :=
    (x.L_coprime_Pp.symm.mul_right x.Pp_coprime_Sp).dvd_of_dvd_mul_left hscaledPp
  have herrorPp : x.Pp ∣ x.mu * x.Pp - x.mup * x.P - scalar c := by
    have hmu : x.Pp ∣ x.mu * x.Pp := ⟨x.mu, by ring⟩
    have := dvd_sub hmu hbasePp
    convert this using 1 <;> ring
  have hproduct : x.P * x.Pp ∣ x.mu * x.Pp - x.mup * x.P - scalar c :=
    x.P_coprime_Pp.mul_dvd herrorP herrorPp
  have hprodDegree : (x.P * x.Pp).natDegree = 2 * x.k := by
    rw [Polynomial.natDegree_mul x.P_monic.ne_zero x.Pp_monic.ne_zero,
      x.P_degree, x.Pp_degree]
    omega
  have hzero : x.mu * x.Pp - x.mup * x.P - scalar c = 0 :=
    Polynomial.eq_zero_of_dvd_of_natDegree_lt hproduct <| by
      rw [hprodDegree]
      exact muError_natDegree_lt x c
  exact sub_eq_zero.mp hzero

/-- The second pair of inverse-free divisibilities recovers the scalar endpoint identity. -/
theorem nuInverseFree_implies_endpoint (x : Datum F) {d : F}
    (h : NuInverseFreeAt x d) : NuEndpointAt x d := by
  have hscaledS : x.S ∣ (x.L * x.P) * (x.nu * x.Sp - scalar d) := by
    have h₁ := x.nu_congruence.mul_right x.Sp
    have h₂ := h.1
    have hsub := dvd_sub h₁ h₂
    convert hsub using 1 <;> ring
  have hbaseS : x.S ∣ x.nu * x.Sp - scalar d :=
    (x.L_coprime_S.symm.mul_right x.P_coprime_S.symm).dvd_of_dvd_mul_left hscaledS
  have herrorS : x.S ∣ x.nu * x.Sp - x.nup * x.S - scalar d := by
    have hnup : x.S ∣ x.nup * x.S := ⟨x.nup, by ring⟩
    have := dvd_sub hbaseS hnup
    convert this using 1 <;> ring
  have hscaledSp : x.Sp ∣ (x.L * x.Pp) * (scalar d + x.nup * x.S) := by
    have h₁ := h.2
    have h₂ := x.nup_congruence.mul_right x.S
    have hadd := dvd_add h₁ h₂
    convert hadd using 1 <;> ring
  have hbaseSp : x.Sp ∣ scalar d + x.nup * x.S :=
    (x.L_coprime_Sp.symm.mul_right x.Pp_coprime_Sp.symm).dvd_of_dvd_mul_left hscaledSp
  have herrorSp : x.Sp ∣ x.nu * x.Sp - x.nup * x.S - scalar d := by
    have hnu : x.Sp ∣ x.nu * x.Sp := ⟨x.nu, by ring⟩
    have := dvd_sub hnu hbaseSp
    convert this using 1 <;> ring
  have hproduct : x.S * x.Sp ∣ x.nu * x.Sp - x.nup * x.S - scalar d :=
    x.S_coprime_Sp.mul_dvd herrorS herrorSp
  have hprodDegree : (x.S * x.Sp).natDegree = 2 * x.k := by
    rw [Polynomial.natDegree_mul x.S_monic.ne_zero x.Sp_monic.ne_zero,
      x.S_degree, x.Sp_degree]
    omega
  have hzero : x.nu * x.Sp - x.nup * x.S - scalar d = 0 :=
    Polynomial.eq_zero_of_dvd_of_natDegree_lt hproduct <| by
      rw [hprodDegree]
      exact nuError_natDegree_lt x d
  exact sub_eq_zero.mp hzero

/-- Scalar endpoint values are unique. -/
theorem scalarWitnessUnique (x : Datum F) : ScalarWitnessUnique x := by
  intro c c' d d' hc hc' hd hd'
  constructor
  · apply Polynomial.C_injective
    calc
      scalar c = x.mu * x.Pp - x.mup * x.P := hc.symm
      _ = scalar c' := hc'
  · apply Polynomial.C_injective
    calc
      scalar d = x.nu * x.Sp - x.nup * x.S := hd.symm
      _ = scalar d' := hd'

/-- Kernel-level reconstruction of Paper VII Theorem 3.1 for a literal datum. -/
theorem inverseFreeAlgebraization (x : Datum F) :
    (InverseFreeIncidence x ↔ ScalarFrequencyIncidence x) ∧ ScalarWitnessUnique x := by
  constructor
  · constructor
    · intro h
      exact ⟨muInverseFree_implies_endpoint x h.1, nuInverseFree_implies_endpoint x h.2⟩
    · intro h
      exact ⟨muEndpoint_implies_inverseFree x h.1, nuEndpoint_implies_inverseFree x h.2⟩
  · exact scalarWitnessUnique x

/-- Concrete F2 theorem replacing the abstract P7-IFA1 assumption. -/
theorem p7_ifa1_concrete (F : Type u) [Field F] [Fintype F] :
    (specification F).IFA1Statement := by
  intro x _
  exact inverseFreeAlgebraization x

end Bilateral
end FortuneFormal
