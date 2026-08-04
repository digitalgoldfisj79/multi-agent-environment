import FortuneFormal.Specification

set_option autoImplicit false

namespace FortuneFormal

/-- Temporary F0 assumption for Paper VII claim P7-IFA1. Remove at F2. -/
axiom p7_ifa1 (S : PaperVIISpecification) :
  S.IFA1Statement

/-- Temporary F0 assumption for Paper VII claim P7-BDD1. Remove at F3. -/
axiom p7_bdd1 (S : PaperVIISpecification) :
  S.BDD1Statement

/-- Temporary F0 assumption for Paper VII claim P7-BDD2. Remove at F3. -/
axiom p7_bdd2 (S : PaperVIISpecification) :
  S.BDD2Statement

/-- Temporary F0 assumption for Paper VII claim P7-STRIP. Remove at F3. -/
axiom p7_strip (S : PaperVIISpecification) :
  S.StripStatement

/-- Temporary F0 assumption for Paper VII claim P7-K2. Remove at F4. -/
axiom p7_k2_empty (S : PaperVIISpecification) :
  S.K2EmptyStatement

end FortuneFormal
