import Mathlib
import FortuneFormal.Bilateral.Definitions

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

/-- The first quotient difference in the common-defect theorem. -/
def firstDifference (x : Datum F) (q : QuotientWitness x) : Polynomial F :=
  scalar (rho x) * q.Cq - scalar (lambda x) * q.B

/-- The second quotient difference in the common-defect theorem. -/
def secondDifference (x : Datum F) (q : QuotientWitness x) : Polynomial F :=
  scalar (rho x) * q.A - scalar (lambda x) * q.Dq

/-- The common transfer expression appearing in both quotient substitutions. -/
def defectExpression (x : Datum F) : Polynomial F :=
  x.L * (scalar (rho x) * x.S * x.Sp - scalar (lambda x) * x.P * x.Pp) +
    scalar (lambda x * rho x) * (x.P * x.S - x.Pp * x.Sp)

/-- First exact transfer identity obtained from the quotient equations. -/
theorem firstDifference_transfer (x : Datum F) (q : QuotientWitness x) :
    firstDifference x q * x.S * x.Pp = defectExpression x := by
  unfold firstDifference defectExpression
  calc
    (scalar (rho x) * q.Cq - scalar (lambda x) * q.B) * x.S * x.Pp =
        scalar (rho x) * x.S * (q.Cq * x.Pp) -
          scalar (lambda x) * x.Pp * (q.B * x.S) := by ring
    _ = scalar (rho x) * x.S *
          (x.L * x.Sp + scalar (lambda x) * x.P) -
        scalar (lambda x) * x.Pp *
          (x.L * x.P + scalar (rho x) * x.Sp) := by rw [q.CPp, q.BS]
    _ = x.L *
          (scalar (rho x) * x.S * x.Sp -
            scalar (lambda x) * x.P * x.Pp) +
        scalar (lambda x * rho x) *
          (x.P * x.S - x.Pp * x.Sp) := by
      simp only [scalar, map_mul]
      ring

/-- Second exact transfer identity obtained from the quotient equations. -/
theorem secondDifference_transfer (x : Datum F) (q : QuotientWitness x) :
    secondDifference x q * x.P * x.Sp = defectExpression x := by
  unfold secondDifference defectExpression
  calc
    (scalar (rho x) * q.A - scalar (lambda x) * q.Dq) * x.P * x.Sp =
        scalar (rho x) * x.Sp * (q.A * x.P) -
          scalar (lambda x) * x.P * (q.Dq * x.Sp) := by ring
    _ = scalar (rho x) * x.Sp *
          (x.L * x.S - scalar (lambda x) * x.Pp) -
        scalar (lambda x) * x.P *
          (x.L * x.Pp - scalar (rho x) * x.S) := by rw [q.AP, q.DSp]
    _ = x.L *
          (scalar (rho x) * x.S * x.Sp -
            scalar (lambda x) * x.P * x.Pp) +
        scalar (lambda x * rho x) *
          (x.P * x.S - x.Pp * x.Sp) := by
      simp only [scalar, map_mul]
      ring

end Bilateral
end FortuneFormal
