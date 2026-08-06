import Mathlib

set_option autoImplicit false

namespace FortuneFormal
namespace Quadratic

universe u

variable (F : Type u) [Field F]

/-- Coordinates of the normalized q-free quadratic incidence model:
`P=t²+A`, `S=t²+Bt+C`, and `U=ρ`. -/
structure ModelPoint where
  A : F
  B : F
  C : F
  U : F

variable {F}

/-- First equation of the faithful q-free quadratic model. -/
def f0 (x : ModelPoint F) : F :=
  -4*x.A^2*x.B*x.U + 6*x.A^2*x.B - 2*x.A^2*x.U + 4*x.A^2 +
  4*x.A*x.B^3 + 4*x.A*x.B^2*x.U + 2*x.A*x.B^2 +
  4*x.A*x.B*x.C*x.U - 8*x.A*x.B*x.C - 4*x.A*x.C +
  2*x.B*x.C^2 + 2*x.C^2*x.U

/-- Second equation of the faithful q-free quadratic model. -/
def f1 (x : ModelPoint F) : F :=
  -4*x.A^2*x.U + 4*x.A^2 + 2*x.A*x.B^2 + 6*x.A*x.B*x.U -
  2*x.A*x.B + 8*x.A*x.C*x.U - 8*x.A*x.C - 2*x.B^2*x.C -
  2*x.B*x.C*x.U - 2*x.B*x.C - 4*x.C^2*x.U + 4*x.C^2

/-- Third equation of the faithful q-free quadratic model. -/
def f2 (x : ModelPoint F) : F :=
  -2*x.A^2*x.B - 2*x.A^2*x.U - 2*x.A*x.B^3*x.U - x.A*x.B^3 -
  2*x.A*x.B^2*x.U^2 - 2*x.A*x.B^2*x.U + 4*x.A*x.B*x.C*x.U +
  4*x.A*x.C*x.U^2 - x.B^3*x.C - 2*x.B^2*x.C*x.U -
  4*x.B*x.C^2*x.U + 2*x.B*x.C^2 - 4*x.C^2*x.U^2 + 2*x.C^2*x.U

/-- Fourth equation of the faithful q-free quadratic model. -/
def f3 (x : ModelPoint F) : F :=
  4*x.A^2*x.U - 4*x.A^2 + 2*x.A*x.B^2*x.U - 4*x.A*x.B^2 -
  2*x.A*x.B*x.U^2 - 2*x.A*x.B*x.U - 8*x.A*x.C*x.U +
  8*x.A*x.C - x.B^4 - 2*x.B^3*x.U - 2*x.B^2*x.C*x.U +
  4*x.B^2*x.C - 2*x.B*x.C*x.U^2 + 6*x.B*x.C*x.U +
  4*x.C^2*x.U - 4*x.C^2

/-- The four exact q-free model equations. -/
def Equations (x : ModelPoint F) : Prop :=
  f0 x = 0 ∧ f1 x = 0 ∧ f2 x = 0 ∧ f3 x = 0

/-- A field element is represented as a literal square. -/
def IsLiteralSquare (a : F) : Prop := ∃ r : F, r^2 = a

/-- The arithmetic open conditions inherited from a true incidence.  The
nonsquare clauses are the irreducibility conditions for the two normalized
monic quadratics. -/
def ArithmeticOpen (x : ModelPoint F) : Prop :=
  x.U ≠ 0 ∧ x.A ≠ 0 ∧ x.B^2 - 4*x.C ≠ 0 ∧
  (x.B ≠ 0 ∨ x.A - x.C ≠ 0) ∧
  ¬ IsLiteralSquare (-4*x.A) ∧
  ¬ IsLiteralSquare (x.B^2 - 4*x.C)

/-- The component forced by the two universal localization certificates. -/
def CertifiedComponent (x : ModelPoint F) : Prop :=
  x.U = 1 ∧ x.B = -2 ∧ (x.A - x.C)^2 + 4*x.A = 0

/-- Exact statement supplied by the chart certificates after reduction from a
true incidence. -/
def CertificateStatement : Prop :=
  ∀ x : ModelPoint F, Equations x → ArithmeticOpen x → CertifiedComponent x

end Quadratic
end FortuneFormal
