import Mathlib

set_option autoImplicit false

namespace FortuneFormal
namespace Integer

open scoped BigOperators

universe u v

variable {ι : Type u} [Fintype ι]
variable {κ : Type v} [Fintype κ]

/-- A rowwise collision budget aggregates without any hidden positivity,
character-sum or arithmetic assumption. All analytic content remains in `hrow`. -/
theorem totalCollision_le_of_rowBudget
    (collision : ι → κ → ℝ) (mass : ι → ℝ) (radius : ℝ)
    (hrow : ∀ i, (∑ k, collision i k) ≤ radius * mass i) :
    (∑ i, ∑ k, collision i k) ≤ radius * ∑ i, mass i := by
  calc
    (∑ i, ∑ k, collision i k) ≤ ∑ i, radius * mass i := by
      apply Finset.sum_le_sum
      intro i hi
      exact hrow i
    _ = radius * ∑ i, mass i := by
      rw [Finset.mul_sum]

/-- Pointwise diagonal-plus-collision estimates and one aggregate collision
budget imply the global weighted energy estimate. The pointwise decomposition
and collision bound are explicit assumptions rather than analytic axioms. -/
theorem weightedEnergy_le_of_collisionBudget
    (energy diagonal collision : κ → ℝ) (mass radius : ℝ)
    (hpoint : ∀ q, energy q ≤ diagonal q * mass + collision q)
    (hcollision : (∑ q, collision q) ≤ radius * mass) :
    (∑ q, energy q) ≤ ((∑ q, diagonal q) + radius) * mass := by
  calc
    (∑ q, energy q) ≤ ∑ q, (diagonal q * mass + collision q) := by
      apply Finset.sum_le_sum
      intro q hq
      exact hpoint q
    _ = (∑ q, diagonal q) * mass + ∑ q, collision q := by
      rw [Finset.sum_add_distrib, Finset.sum_mul]
    _ ≤ (∑ q, diagonal q) * mass + radius * mass := by
      linarith
    _ = ((∑ q, diagonal q) + radius) * mass := by
      ring

/-- Combined deterministic bridge: a row-indexed collision decomposition and
rowwise budgets imply the global weighted energy estimate. -/
theorem weightedEnergy_le_of_rowCollisionBudget
    (energy diagonal : κ → ℝ)
    (rowCollision : ι → κ → ℝ)
    (rowMass : ι → ℝ)
    (mass radius : ℝ)
    (hmass : mass = ∑ i, rowMass i)
    (hpoint : ∀ q, energy q ≤ diagonal q * mass + ∑ i, rowCollision i q)
    (hrow : ∀ i, (∑ q, rowCollision i q) ≤ radius * rowMass i) :
    (∑ q, energy q) ≤ ((∑ q, diagonal q) + radius) * mass := by
  have hcollisionRows :
      (∑ i, ∑ q, rowCollision i q) ≤ radius * ∑ i, rowMass i :=
    totalCollision_le_of_rowBudget rowCollision rowMass radius hrow
  have hcollision :
      (∑ q, ∑ i, rowCollision i q) ≤ radius * mass := by
    calc
      (∑ q, ∑ i, rowCollision i q) = ∑ i, ∑ q, rowCollision i q := by
        rw [Finset.sum_comm]
      _ ≤ radius * ∑ i, rowMass i := hcollisionRows
      _ = radius * mass := by
        rw [← hmass]
  exact weightedEnergy_le_of_collisionBudget
    energy diagonal (fun q => ∑ i, rowCollision i q)
    mass radius hpoint hcollision

/-- The fixed-order collision counts sum by the exact hockey-stick identity.
This is the combinatorial summation used after the pairwise support bound. -/
theorem fixedOrderChooseSum (n r : ℕ) :
    (∑ m ∈ Finset.Icc r n, m.choose r) = (n + 1).choose (r + 1) := by
  exact Nat.sum_Icc_choose n r

end Integer
end FortuneFormal
