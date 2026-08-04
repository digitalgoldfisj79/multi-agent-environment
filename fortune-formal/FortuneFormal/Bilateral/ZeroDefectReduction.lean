import Mathlib
import FortuneFormal.Bilateral.Definitions
import FortuneFormal.Bilateral.DefectCore

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F] [Fintype F]

/-- The quotient information needed to read the leading coefficient of the
first zero-defect identity.  A later theorem derives this shape from the
Frobenius-base quotient equations. -/
structure QuotientLeadingShape (x : Datum F) (q : QuotientWitness x) : Prop where
  B_monic : q.B.Monic
  C_monic : q.Cq.Monic
  B_degree : q.B.natDegree = Fintype.card F
  C_degree : q.Cq.natDegree = Fintype.card F

/-- Algebraic normal form forced by zero defect, before using irreducibility of
`L ± λ`. -/
structure ZeroDefectNormalForm (x : Datum F) (q : QuotientWitness x) : Prop where
  rho_eq_lambda : rho x = lambda x
  C_eq_B : q.Cq = q.B
  A_eq_D : q.A = q.Dq
  AB_factorization :
    q.A * q.B =
      (x.L - scalar (lambda x)) * (x.L + scalar (lambda x))

/-- Zero defect forces equality of the normalized scalars, equality of the
paired quotient polynomials, and the two-factor Artin-Schreier product. -/
theorem zeroDefect_normalForm (x : Datum F) (q : QuotientWitness x)
    (shape : QuotientLeadingShape x q) (hlambda : lambda x ≠ 0)
    (hh : DefectWitness x q 0) : ZeroDefectNormalForm x q := by
  have hCcoeff : q.Cq.coeff (Fintype.card F) = 1 := by
    rw [← shape.C_degree]
    exact shape.C_monic
  have hBcoeff : q.B.coeff (Fintype.card F) = 1 := by
    rw [← shape.B_degree]
    exact shape.B_monic
  have hrho : rho x = lambda x := by
    have hcoeff := congrArg
      (fun f : Polynomial F => f.coeff (Fintype.card F)) hh.first
    simp only [zero_mul, zero_eq_mul, Polynomial.coeff_zero] at hcoeff
    simpa [scalar, hCcoeff, hBcoeff] using sub_eq_zero.mp hcoeff
  have hscalar : scalar (lambda x) ≠ 0 :=
    Polynomial.C_ne_zero.mpr hlambda
  have hCB : q.Cq = q.B := by
    have hzero : scalar (lambda x) * (q.Cq - q.B) = 0 := by
      calc
        scalar (lambda x) * (q.Cq - q.B) =
            scalar (rho x) * q.Cq - scalar (lambda x) * q.B := by
          rw [hrho]
          ring
        _ = 0 := by simpa using hh.first
    exact sub_eq_zero.mp ((mul_eq_zero.mp hzero).resolve_left hscalar)
  have hAD : q.A = q.Dq := by
    have hzero : scalar (lambda x) * (q.A - q.Dq) = 0 := by
      calc
        scalar (lambda x) * (q.A - q.Dq) =
            scalar (rho x) * q.A - scalar (lambda x) * q.Dq := by
          rw [hrho]
          ring
        _ = 0 := by simpa using hh.second
    exact sub_eq_zero.mp ((mul_eq_zero.mp hzero).resolve_left hscalar)
  have hAB_on_S :
      q.A * q.B * x.S =
        (x.L * x.L - scalar (lambda x * lambda x)) * x.S := by
    calc
      q.A * q.B * x.S = q.A * (q.B * x.S) := by ring
      _ = q.A * (x.L * x.P + scalar (lambda x) * x.Sp) := by
        rw [q.BS, hrho]
      _ = x.L * (q.A * x.P) + scalar (lambda x) * (q.A * x.Sp) := by ring
      _ = x.L *
            (x.L * x.S - scalar (lambda x) * x.Pp) +
          scalar (lambda x) *
            (x.L * x.Pp - scalar (lambda x) * x.S) := by
        rw [q.AP, hAD, q.DSp, hrho]
      _ = (x.L * x.L - scalar (lambda x * lambda x)) * x.S := by
        simp only [scalar, map_mul]
        ring
  have hAB :
      q.A * q.B = x.L * x.L - scalar (lambda x * lambda x) := by
    have hzero :
        (q.A * q.B -
          (x.L * x.L - scalar (lambda x * lambda x))) * x.S = 0 := by
      rw [sub_mul, hAB_on_S, sub_self]
    exact sub_eq_zero.mp
      ((mul_eq_zero.mp hzero).resolve_right x.S_monic.ne_zero)
  refine {
    rho_eq_lambda := hrho
    C_eq_B := hCB
    A_eq_D := hAD
    AB_factorization := ?_
  }
  calc
    q.A * q.B = x.L * x.L - scalar (lambda x * lambda x) := hAB
    _ = (x.L - scalar (lambda x)) * (x.L + scalar (lambda x)) := by
      simp only [scalar, map_mul]
      ring

end Bilateral
end FortuneFormal
