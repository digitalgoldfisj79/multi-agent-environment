import Mathlib
import FortuneFormal.Bilateral.FactorOrdering
import FortuneFormal.Bilateral.QuotientShape
import FortuneFormal.Bilateral.ZeroDefectScoped

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

private theorem frobenius_monic_for_factor (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    x.L.Monic := by
  rw [hbase, sub_eq_add_neg]
  apply Polynomial.monic_X_pow_add
  simpa using hp.one_lt

private theorem frobenius_degree_for_factor (x : Datum F)
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

private theorem artin_minus_monic_degree (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    (x.L - scalar (lambda x)).Monic ∧
      (x.L - scalar (lambda x)).natDegree = Fintype.card F := by
  have hLmonic := frobenius_monic_for_factor x hp hbase
  have hLdegree := frobenius_degree_for_factor x hp hbase
  have hlt : (scalar (lambda x)).natDegree < x.L.natDegree := by
    rw [hLdegree]
    simp only [scalar, Polynomial.natDegree_C]
    exact hp.pos
  constructor
  · rw [sub_eq_add_neg]
    apply hLmonic.add_of_left
    rw [Polynomial.degree_neg]
    exact Polynomial.degree_lt_degree hlt
  · exact (Polynomial.natDegree_sub_eq_left_of_natDegree_lt hlt).trans hLdegree

private theorem artin_plus_monic_degree (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x) :
    (x.L + scalar (lambda x)).Monic ∧
      (x.L + scalar (lambda x)).natDegree = Fintype.card F := by
  have hLmonic := frobenius_monic_for_factor x hp hbase
  have hLdegree := frobenius_degree_for_factor x hp hbase
  have hlt : (scalar (lambda x)).natDegree < x.L.natDegree := by
    rw [hLdegree]
    simp only [scalar, Polynomial.natDegree_C]
    exact hp.pos
  constructor
  · apply hLmonic.add_of_left
    exact Polynomial.degree_lt_degree hlt
  · exact (Polynomial.natDegree_add_eq_left_of_natDegree_lt hlt).trans hLdegree

/-- Conditional factor ordering for an actual zero-defect incidence.  Every
step except the single displayed Artin-Schreier irreducibility hypothesis is
kernel checked. -/
theorem zeroDefect_factorOrdering_of_artinIrreducible (x : Datum F)
    (hp : Nat.Prime (Fintype.card F)) (hbase : FrobeniusBase x)
    (hk : x.k < Fintype.card F) (hinc : InverseFreeIncidence x)
    (hz : ZeroDefect x)
    (hirr : Irreducible (x.L - scalar (lambda x))) :
    ∃ q : QuotientWitness x,
      ZeroDefectNormalForm x q ∧
      ((q.A = x.L - scalar (lambda x) ∧
          q.B = x.L + scalar (lambda x)) ∨
       (q.A = x.L + scalar (lambda x) ∧
          q.B = x.L - scalar (lambda x))) := by
  obtain ⟨q, hnormal⟩ :=
    zeroDefect_normalForm_of_incidence x hp hbase hk hinc hz
  obtain ⟨hAmonic, hBmonic, hAdegree, hBdegree⟩ :=
    quotientABShape x hp hbase hk q
  obtain ⟨hfmonic, hfdegree⟩ := artin_minus_monic_degree x hp hbase
  obtain ⟨hgmonic, hgdegree⟩ := artin_plus_monic_degree x hp hbase
  have horder := twoFactor_ordering
    hirr hfmonic hgmonic hAmonic hBmonic
    (hfdegree.trans hAdegree.symm)
    (hAdegree.trans hBdegree.symm)
    (hgdegree.trans hAdegree.symm)
    hnormal.AB_factorization
  exact ⟨q, hnormal, horder⟩

end Bilateral
end FortuneFormal
