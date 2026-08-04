import Mathlib
import FortuneFormal.Bilateral.Definitions
import FortuneFormal.Bilateral.ZeroDefectReduction

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

private theorem frobeniusBase_monic (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    x.L.Monic := by
  rw [hbase, sub_eq_add_neg]
  apply Polynomial.monic_X_pow_add
  simpa using hp.one_lt

private theorem frobeniusBase_degree (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    x.L.natDegree = Fintype.card F := by
  exact (frobeniusBase_monic x hp hbase).natDegree_eq_iff_degree_eq.mpr <| by
    rw [hbase]
    apply Polynomial.degree_sub_eq_left_of_degree_lt
    simp only [Polynomial.degree_X, Polynomial.degree_X_pow]
    simpa using hp.one_lt

private theorem monic_main_add_lower
    (M N R : Polynomial F) (n : ℕ)
    (hM : M.Monic) (hN : N.Monic)
    (hmain : (M * N).natDegree = n)
    (hlower : R.natDegree < n) : (M * N + R).Monic := by
  apply Polynomial.monic_of_degree_le n
  · apply Polynomial.degree_le_of_natDegree_le
    exact (Polynomial.natDegree_add_le _ _).trans <| max_le hmain.le hlower.le
  · rw [Polynomial.coeff_add]
    have hmainCoeff : (M * N).coeff n = 1 := by
      rw [← hmain, ← Polynomial.leadingCoeff]
      exact hM.mul hN
    have hlowerCoeff : R.coeff n = 0 :=
      Polynomial.coeff_eq_zero_of_natDegree_lt hlower
    rw [hmainCoeff, hlowerCoeff, add_zero]

private theorem B_shape (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (hk : x.k < Fintype.card F) (q : QuotientWitness x) :
    q.B.Monic ∧ q.B.natDegree = Fintype.card F := by
  let Q := Fintype.card F
  have hLmonic := frobeniusBase_monic x hp hbase
  have hLdegree := frobeniusBase_degree x hp hbase
  have hmain : (x.L * x.P).natDegree = Q + x.k := by
    rw [hLmonic.natDegree_mul x.P_monic, hLdegree, x.P_degree]
  have hlower : (scalar (rho x) * x.Sp).natDegree < Q + x.k := by
    apply lt_of_le_of_lt Polynomial.natDegree_mul_le
    simp only [scalar, Polynomial.natDegree_C, x.Sp_degree]
    omega
  have hrhsMonic :
      (x.L * x.P + scalar (rho x) * x.Sp).Monic :=
    monic_main_add_lower x.L x.P (scalar (rho x) * x.Sp) (Q + x.k)
      hLmonic x.P_monic hmain hlower
  have hprodMonic : (q.B * x.S).Monic := by
    rw [q.BS]
    exact hrhsMonic
  have hBmonic : q.B.Monic := x.S_monic.of_mul_monic_right hprodMonic
  have hprodDegree : (q.B * x.S).natDegree = Q + x.k := by
    rw [q.BS]
    exact Polynomial.natDegree_eq_of_le_of_coeff_ne_zero
      (Polynomial.natDegree_le_of_degree_le hrhsMonic.degree_le)
      (by
        rw [← hrhsMonic.leadingCoeff]
        exact one_ne_zero)
  have hBdegree : q.B.natDegree = Q := by
    rw [hBmonic.natDegree_mul x.S_monic, x.S_degree] at hprodDegree
    omega
  exact ⟨hBmonic, hBdegree⟩

private theorem C_shape (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (hk : x.k < Fintype.card F) (q : QuotientWitness x) :
    q.Cq.Monic ∧ q.Cq.natDegree = Fintype.card F := by
  let Q := Fintype.card F
  have hLmonic := frobeniusBase_monic x hp hbase
  have hLdegree := frobeniusBase_degree x hp hbase
  have hmain : (x.L * x.Sp).natDegree = Q + x.k := by
    rw [hLmonic.natDegree_mul x.Sp_monic, hLdegree, x.Sp_degree]
  have hlower : (scalar (lambda x) * x.P).natDegree < Q + x.k := by
    apply lt_of_le_of_lt Polynomial.natDegree_mul_le
    simp only [scalar, Polynomial.natDegree_C, x.P_degree]
    omega
  have hrhsMonic :
      (x.L * x.Sp + scalar (lambda x) * x.P).Monic :=
    monic_main_add_lower x.L x.Sp (scalar (lambda x) * x.P) (Q + x.k)
      hLmonic x.Sp_monic hmain hlower
  have hprodMonic : (q.Cq * x.Pp).Monic := by
    rw [q.CPp]
    exact hrhsMonic
  have hCmonic : q.Cq.Monic := x.Pp_monic.of_mul_monic_right hprodMonic
  have hprodDegree : (q.Cq * x.Pp).natDegree = Q + x.k := by
    rw [q.CPp]
    exact Polynomial.natDegree_eq_of_le_of_coeff_ne_zero
      (Polynomial.natDegree_le_of_degree_le hrhsMonic.degree_le)
      (by
        rw [← hrhsMonic.leadingCoeff]
        exact one_ne_zero)
  have hCdegree : q.Cq.natDegree = Q := by
    rw [hCmonic.natDegree_mul x.Pp_monic, x.Pp_degree] at hprodDegree
    omega
  exact ⟨hCmonic, hCdegree⟩

/-- The two quotient polynomials used by the zero-defect leading-coefficient
argument are monic of degree `q`. -/
theorem quotientLeadingShape (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (hk : x.k < Fintype.card F) (q : QuotientWitness x) :
    QuotientLeadingShape x q := by
  obtain ⟨hBmonic, hBdegree⟩ := B_shape x hp hbase hk q
  obtain ⟨hCmonic, hCdegree⟩ := C_shape x hp hbase hk q
  exact {
    B_monic := hBmonic
    C_monic := hCmonic
    B_degree := hBdegree
    C_degree := hCdegree
  }

end Bilateral
end FortuneFormal
