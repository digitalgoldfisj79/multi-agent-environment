import FortuneFormal.Specification

set_option autoImplicit false

namespace FortuneFormal

/-- Temporary assumption for Paper VII claim P7-K2. Remove at F4. -/
axiom p7_k2_empty (S : PaperVIISpecification) :
  S.K2EmptyStatement

end FortuneFormal
