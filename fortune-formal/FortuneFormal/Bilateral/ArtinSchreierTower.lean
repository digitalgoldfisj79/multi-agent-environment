import Mathlib

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

/-- The prime-field Artin-Schreier polynomial with parameter `a`. -/
def artinSchreierPolynomial (F : Type u) [Field F] [Fintype F]
    (a : F) : Polynomial F :=
  Polynomial.X ^ Fintype.card F - Polynomial.X - Polynomial.C a

/-- In the adjoined-root ring, the defining root satisfies `α^q = α + a`. -/
theorem artinSchreier_root_relation
    (a : F) (hp : Nat.Prime (Fintype.card F)) :
    let P := artinSchreierPolynomial F a
    let α := AdjoinRoot.root P
    α ^ Fintype.card F = α + algebraMap F (AdjoinRoot P) a := by
  let q := Fintype.card F
  let P := artinSchreierPolynomial F a
  let R := AdjoinRoot P
  letI : Fact q.Prime := ⟨hp⟩
  letI : CharP F q :=
    (CharP.charP_iff_prime_eq_zero hp).2 (FiniteField.cast_card_eq_zero F)
  have hroot := AdjoinRoot.eval₂_root P
  change (AdjoinRoot.root P) ^ q - AdjoinRoot.root P -
      algebraMap F R a = 0 at hroot
  · linear_combination hroot
  · simp [P, R, artinSchreierPolynomial, q, AdjoinRoot.algebraMap_eq]

/-- Iterating the Artin-Schreier relation gives
`α^(q^n) = α + algebraMap ((n : F) * a)`. -/
theorem artinSchreier_root_iterate
    (a : F) (hp : Nat.Prime (Fintype.card F)) (n : ℕ) :
    let P := artinSchreierPolynomial F a
    let α := AdjoinRoot.root P
    α ^ (Fintype.card F ^ n) =
      α + algebraMap F (AdjoinRoot P) ((n : F) * a) := by
  let q := Fintype.card F
  let P := artinSchreierPolynomial F a
  let R := AdjoinRoot P
  letI : Fact q.Prime := ⟨hp⟩
  letI : CharP F q :=
    (CharP.charP_iff_prime_eq_zero hp).2 (FiniteField.cast_card_eq_zero F)
  have hrel : (AdjoinRoot.root P) ^ q =
      AdjoinRoot.root P + algebraMap F R a := by
    simpa [q, P, R] using artinSchreier_root_relation (F := F) a hp
  induction n with
  | zero =>
      simp [P, R]
  | succ n ih =>
      have hpowBase (b : F) : (algebraMap F R b) ^ q = algebraMap F R b := by
        rw [← map_pow, FiniteField.pow_card]
      calc
        (AdjoinRoot.root P) ^ (q ^ (n + 1)) =
            ((AdjoinRoot.root P) ^ (q ^ n)) ^ q := by
          rw [pow_succ, pow_mul]
        _ = (AdjoinRoot.root P +
              algebraMap F R ((n : F) * a)) ^ q := by rw [ih]
        _ = (AdjoinRoot.root P) ^ q +
              (algebraMap F R ((n : F) * a)) ^ q := by
          rw [add_pow_char (AdjoinRoot.root P)
            (algebraMap F R ((n : F) * a)) q]
        _ = AdjoinRoot.root P + algebraMap F R a +
              algebraMap F R ((n : F) * a) := by rw [hrel, hpowBase]
        _ = AdjoinRoot.root P +
              algebraMap F R (((n + 1 : ℕ) : F) * a) := by
          simp only [map_add, map_mul]
          push_cast
          ring

/-- The Artin-Schreier polynomial divides the `q`th Frobenius tower
`X^(q^q)-X`. -/
theorem artinSchreier_dvd_frobeniusTower
    (a : F) (hp : Nat.Prime (Fintype.card F)) :
    artinSchreierPolynomial F a ∣
      Polynomial.X ^ (Fintype.card F ^ Fintype.card F) - Polynomial.X := by
  let q := Fintype.card F
  let P := artinSchreierPolynomial F a
  let R := AdjoinRoot P
  letI : Fact q.Prime := ⟨hp⟩
  letI : CharP F q :=
    (CharP.charP_iff_prime_eq_zero hp).2 (FiniteField.cast_card_eq_zero F)
  rw [← AdjoinRoot.mk_eq_zero]
  have hiter := artinSchreier_root_iterate (F := F) a hp q
  dsimp [P, R] at hiter
  have hqa : ((q : F) * a) = 0 := by
    rw [show (q : F) = 0 from FiniteField.cast_card_eq_zero F, zero_mul]
  simp only [map_sub, map_pow, AdjoinRoot.mk_X]
  rw [hiter, hqa, map_zero, add_zero, sub_self]

end Bilateral
end FortuneFormal
