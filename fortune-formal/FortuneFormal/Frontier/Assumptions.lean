import FortuneFormal.Quadratic.ReductionInterface

set_option autoImplicit false

namespace FortuneFormal

universe u

/-- The sole remaining Paper VII trust boundary after F3.

It is narrower than P7-K2 itself: the external Singular/normalization package
must produce the certified q-free component from each genuine quadratic
incidence. Lean then derives the contradiction and P7-K2. -/
axiom p7_k2_certified_normalization
    (F : Type u) [Field F] [Fintype F] :
    Quadratic.K2CertifiedNormalizationStatement F

/-- P7-K2 derived from the one ledgered external boundary and the
kernel-checked discriminant contradiction. This theorem is not axiom-free. -/
theorem p7_k2_empty_from_external_certificate
    (F : Type u) [Field F] [Fintype F] :
    (Bilateral.specification F).K2EmptyStatement :=
  Quadratic.p7_k2_empty_of_certifiedNormalization
    (p7_k2_certified_normalization F)

end FortuneFormal
