import Mathlib

set_option autoImplicit false

namespace FortuneChallenge
namespace IntegerBlock

open scoped BigOperators

universe u
variable {ι : Type u} [Fintype ι]

/-- Independent Mathlib-only formulation of the one-failure block criterion. -/
def NoFailureFromVariance : Prop :=
  ∀ (Z base : ι → ℝ) (cX : ℝ),
    0 ≤ cX →
    (∀ i, cX ≤ base i) →
    (∑ i, (Z i - base i)^2) < cX^2 →
    ∀ i, Z i ≠ 0

/-- Independent exact centred second-moment identity. -/
def CenteredSecondMomentIdentity : Prop :=
  ∀ (Z base : ι → ℝ),
    (∑ i, (Z i - base i)^2) =
      (∑ i, base i) +
      ∑ i, (Z i^2 - 2 * base i * Z i + base i^2 - base i)

/-- Independent exact four-prime covariance substitution identity. -/
def FourPrimeCovarianceIdentity : Prop :=
  ∀ (Z base C : ι → ℝ),
    (∀ i, Z i^2 = Z i + 2 * C i) →
    (∑ i, (Z i - base i)^2) =
      (∑ i, base i) +
      ∑ i, (Z i + 2 * C i - 2 * base i * Z i + base i^2 - base i)

end IntegerBlock
end FortuneChallenge
