import FortuneFormal.Comparator.IntegerBlockChallenge
import FortuneFormal.Integer.BlockCriterion

set_option autoImplicit false

namespace FortuneFormal
namespace Comparator

open scoped BigOperators

universe u
variable {ι : Type u} [Fintype ι]

/-- The implementation solves the independent one-failure challenge. -/
theorem integer_no_failure_challenge :
    FortuneChallenge.IntegerBlock.NoFailureFromVariance (ι := ι) := by
  intro Z base cX hcX hbase hvar
  exact FortuneFormal.Integer.no_failure_of_variance_below_baseline_gap
    Z base cX hcX hbase hvar

/-- The implementation solves the independent centred-moment challenge. -/
theorem integer_centered_moment_challenge :
    FortuneChallenge.IntegerBlock.CenteredSecondMomentIdentity (ι := ι) := by
  intro Z base
  exact FortuneFormal.Integer.centered_second_moment_identity Z base

/-- The implementation solves the independent four-prime covariance challenge. -/
theorem integer_four_prime_challenge :
    FortuneChallenge.IntegerBlock.FourPrimeCovarianceIdentity (ι := ι) := by
  intro Z base C hC
  exact FortuneFormal.Integer.four_prime_covariance_identity Z base C hC

end Comparator
end FortuneFormal
