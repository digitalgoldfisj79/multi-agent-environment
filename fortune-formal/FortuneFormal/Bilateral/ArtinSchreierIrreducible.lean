import Mathlib
import FortuneFormal.Bilateral.ArtinSchreierTower
import FortuneFormal.Bilateral.FactorOrdering

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

private theorem artinSchreier_monic_degree
    (a : F) (hp : Nat.Prime (Fintype.card F)) :
    (artinSchreierPolynomial F a).Monic ∧
      (artinSchreierPolynomial F a).natDegree = Fintype.card F := by
  let q := Fintype.card F
  let base : Polynomial F := Polynomial.X ^ q - Polynomial.X
  have hbaseMonic : base.Monic := by
    dsimp [base]
    rw [sub_eq_add_neg]
    apply Polynomial.monic_X_pow_add
    simpa using hp.one_lt
  have hbaseDegree : base.natDegree = q := by
    dsimp [base]
    calc
      (Polynomial.X ^ q - Polynomial.X : Polynomial F).natDegree =
          (Polynomial.X ^ q : Polynomial F).natDegree :=
        Polynomial.natDegree_sub_eq_left_of_natDegree_lt (by
          simp only [Polynomial.natDegree_X, Polynomial.natDegree_pow]
          simpa using hp.one_lt)
      _ = q := by simp
  have hconstlt : (Polynomial.C a).natDegree < base.natDegree := by
    rw [hbaseDegree]
    simp only [Polynomial.natDegree_C]
    exact hp.pos
  constructor
  · dsimp [artinSchreierPolynomial]
    change (base - Polynomial.C a).Monic
    rw [sub_eq_add_neg]
    apply hbaseMonic.add_of_left
    rw [Polynomial.degree_neg]
    exact Polynomial.degree_lt_degree hconstlt
  · dsimp [artinSchreierPolynomial]
    change (base - Polynomial.C a).natDegree = q
    exact (Polynomial.natDegree_sub_eq_left_of_natDegree_lt hconstlt).trans hbaseDegree

private theorem artinSchreier_eval
    (a z : F) : Polynomial.eval z (artinSchreierPolynomial F a) = -a := by
  simp [artinSchreierPolynomial, FiniteField.pow_card]

private theorem artinSchreier_no_linear_factor
    (a : F) (ha : a ≠ 0) {f : Polynomial F}
    (hfMonic : f.Monic) (hfIrr : Irreducible f)
    (hfDegree : f.natDegree = 1)
    (hfDiv : f ∣ artinSchreierPolynomial F a) : False := by
  have hsplit : f.Splits :=
    Polynomial.Splits.of_natDegree_le_one_of_monic hfDegree.le hfMonic
  have hdegree : f.degree = (1 : WithBot ℕ) :=
    (Polynomial.degree_eq_iff_natDegree_eq hfIrr.ne_zero).2 hfDegree
  obtain ⟨z, hfz⟩ := hsplit.exists_eval_eq_zero <| by
    rw [hdegree]
    norm_num
  rcases hfDiv with ⟨r, hr⟩
  have hPzero : Polynomial.eval z (artinSchreierPolynomial F a) = 0 := by
    rw [hr, Polynomial.eval_mul, hfz, zero_mul]
  rw [artinSchreier_eval a z] at hPzero
  exact ha (neg_eq_zero.mp hPzero)

/-- For a nonzero parameter over a field of prime cardinality, the
Artin-Schreier polynomial `X^q-X-a` is irreducible. -/
theorem artinSchreier_irreducible
    (a : F) (ha : a ≠ 0) (hp : Nat.Prime (Fintype.card F)) :
    Irreducible (artinSchreierPolynomial F a) := by
  let q := Fintype.card F
  let P := artinSchreierPolynomial F a
  obtain ⟨hPMonic, hPDegree⟩ := artinSchreier_monic_degree a hp
  have hPNonunit : ¬ IsUnit P := by
    intro hunit
    have hzero := Polynomial.natDegree_eq_zero_of_isUnit hunit
    rw [hPDegree] at hzero
    exact hp.ne_zero hzero
  obtain ⟨f, hfMonic, hfIrr, hfDivP⟩ :=
    Polynomial.exists_monic_irreducible_factor P hPNonunit
  have hfDivTower :
      f ∣ Polynomial.X ^ (q ^ q) - Polynomial.X :=
    hfDivP.trans (by
      simpa [P, q] using artinSchreier_dvd_frobeniusTower (F := F) a hp)
  have hfDegreeDiv : f.natDegree ∣ q :=
    hfIrr.natDegree_dvd_of_dvd_X_pow_card_pow_sub_X <| by
      simpa [q] using hfDivTower
  rcases hp.eq_one_or_self_of_dvd f.natDegree hfDegreeDiv with hfOne | hfQ
  · exact (artinSchreier_no_linear_factor a ha hfMonic hfIrr hfOne <| by
      simpa [P] using hfDivP).elim
  · have hfEqP : f = P :=
      monic_eq_of_dvd_of_natDegree_eq hfMonic hPMonic
        (hfQ.trans hPDegree.symm) hfDivP
    simpa [P, hfEqP] using hfIrr

end Bilateral
end FortuneFormal
