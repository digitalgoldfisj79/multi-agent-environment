import Mathlib
import FortuneFormal.Specification

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

/-- A literal finite-field polynomial datum for the bilateral endpoint system. -/
structure Datum (F : Type u) [Field F] [Fintype F] where
  k : ℕ
  L : Polynomial F
  P : Polynomial F
  S : Polynomial F
  Pp : Polynomial F
  Sp : Polynomial F
  theta : F
  c : F
  d : F
  mu : Polynomial F
  mup : Polynomial F
  nu : Polynomial F
  nup : Polynomial F
  k_pos : 0 < k
  theta_ne_zero : theta ≠ 0
  P_monic : P.Monic
  S_monic : S.Monic
  Pp_monic : Pp.Monic
  Sp_monic : Sp.Monic
  P_irreducible : Irreducible P
  S_irreducible : Irreducible S
  Pp_irreducible : Irreducible Pp
  Sp_irreducible : Irreducible Sp
  P_degree : P.natDegree = k
  S_degree : S.natDegree = k
  Pp_degree : Pp.natDegree = k
  Sp_degree : Sp.natDegree = k
  mu_degree : mu.natDegree < k
  mup_degree : mup.natDegree < k
  nu_degree : nu.natDegree < k
  nup_degree : nup.natDegree < k
  mu_congruence : P ∣ L * S * mu + Polynomial.C theta
  mup_congruence : Pp ∣ L * Sp * mup + Polynomial.C theta
  nu_congruence : S ∣ L * P * nu + Polynomial.C theta
  nup_congruence : Sp ∣ L * Pp * nup + Polynomial.C theta
  L_coprime_P : IsCoprime L P
  L_coprime_S : IsCoprime L S
  L_coprime_Pp : IsCoprime L Pp
  L_coprime_Sp : IsCoprime L Sp
  P_coprime_S : IsCoprime P S
  P_coprime_Pp : IsCoprime P Pp
  P_coprime_Sp : IsCoprime P Sp
  S_coprime_Pp : IsCoprime S Pp
  S_coprime_Sp : IsCoprime S Sp
  Pp_coprime_Sp : IsCoprime Pp Sp

variable {F : Type u} [Field F] [Fintype F]

/-- All four moduli are distinct. -/
def CrossDistinct (x : Datum F) : Prop :=
  x.P ≠ x.S ∧ x.P ≠ x.Pp ∧ x.P ≠ x.Sp ∧
  x.S ≠ x.Pp ∧ x.S ≠ x.Sp ∧ x.Pp ≠ x.Sp

/-- The literal Frobenius base polynomial `t^q - t`, where `q = #F`. -/
def FrobeniusBase (x : Datum F) : Prop :=
  x.L = Polynomial.X ^ Fintype.card F - Polynomial.X

/-- The scalar embedding into the polynomial ring. -/
abbrev scalar (a : F) : Polynomial F := Polynomial.C a

/-- Scalar endpoint contact for the first source pair. -/
def MuEndpointAt (x : Datum F) (c : F) : Prop :=
  x.mu * x.Pp - x.mup * x.P = scalar c

/-- Scalar endpoint contact for the second source pair. -/
def NuEndpointAt (x : Datum F) (d : F) : Prop :=
  x.nu * x.Sp - x.nup * x.S = scalar d

/-- Literal modular-frequency form of simultaneous bilateral endpoint contact. -/
def ScalarFrequencyIncidence (x : Datum F) : Prop :=
  MuEndpointAt x x.c ∧ NuEndpointAt x x.d

/-- The first pair of inverse-free divisibilities at an arbitrary scalar `c`. -/
def MuInverseFreeAt (x : Datum F) (c : F) : Prop :=
  x.P ∣ scalar c * x.L * x.S + scalar x.theta * x.Pp ∧
  x.Pp ∣ scalar c * x.L * x.Sp - scalar x.theta * x.P

/-- The second pair of inverse-free divisibilities at an arbitrary scalar `d`. -/
def NuInverseFreeAt (x : Datum F) (d : F) : Prop :=
  x.S ∣ scalar d * x.L * x.P + scalar x.theta * x.Sp ∧
  x.Sp ∣ scalar d * x.L * x.Pp - scalar x.theta * x.S

/-- The four inverse-free divisibilities of Paper VII, Theorem 3.1. -/
def InverseFreeIncidence (x : Datum F) : Prop :=
  MuInverseFreeAt x x.c ∧ NuInverseFreeAt x x.d

/-- Uniqueness of scalar values represented by the two endpoint polynomials. -/
def ScalarWitnessUnique (x : Datum F) : Prop :=
  ∀ c c' d d' : F,
    MuEndpointAt x c → MuEndpointAt x c' →
    NuEndpointAt x d → NuEndpointAt x d' →
      c = c' ∧ d = d'

/-- The normalized scalar parameters used in the quotient equations. -/
def lambda (x : Datum F) : F := -(x.theta / x.c)

def rho (x : Datum F) : F := x.theta / x.d

/-- Quotient-polynomial presentation of the inverse-free coefficient scheme. -/
structure QuotientWitness (x : Datum F) where
  A : Polynomial F
  B : Polynomial F
  Cq : Polynomial F
  Dq : Polynomial F
  AP : A * x.P = x.L * x.S - scalar (lambda x) * x.Pp
  BS : B * x.S = x.L * x.P + scalar (rho x) * x.Sp
  CPp : Cq * x.Pp = x.L * x.Sp + scalar (lambda x) * x.P
  DSp : Dq * x.Sp = x.L * x.Pp - scalar (rho x) * x.S

/-- The common-defect equations from Paper VII, Theorem 4.1. -/
structure DefectWitness (x : Datum F) (q : QuotientWitness x)
    (h : Polynomial F) : Prop where
  first : scalar (rho x) * q.Cq - scalar (lambda x) * q.B = h * x.P * x.Sp
  second : scalar (rho x) * q.A - scalar (lambda x) * q.Dq = h * x.S * x.Pp
  product :
    h * x.P * x.Pp * x.S * x.Sp =
      x.L * (scalar (rho x) * x.S * x.Sp - scalar (lambda x) * x.P * x.Pp) +
      scalar (lambda x * rho x) * (x.P * x.S - x.Pp * x.Sp)

/-- Existence and uniqueness of the common defect, including its quotient data. -/
def CommonDefectExistsUnique (x : Datum F) : Prop :=
  ∃! h : Polynomial F, ∃ q : QuotientWitness x, DefectWitness x q h

/-- The manuscript defect-degree bound `deg h ≤ q - 2k`. -/
def DefectDegreeBound (x : Datum F) : Prop :=
  ∀ h : Polynomial F, ∀ q : QuotientWitness x,
    DefectWitness x q h → h.natDegree ≤ Fintype.card F - 2 * x.k

/-- Zero defect in the quotient presentation. -/
def ZeroDefect (x : Datum F) : Prop :=
  ∃ q : QuotientWitness x, DefectWitness x q 0

/-- Translation component of the zero-defect locus. -/
def TranslationFamily (x : Datum F) : Prop :=
  ∃ R : Polynomial F,
    x.Pp = x.P + x.L * R ∧
    x.S = x.P + scalar (lambda x) * R ∧
    x.Sp = x.S + x.L * R

/-- Reflection component of the zero-defect locus. -/
def ReflectionFamily (x : Datum F) : Prop :=
  ∃ Q : Polynomial F,
    x.Pp = x.L * Q - x.P ∧
    x.S = x.P + scalar (lambda x) * Q ∧
    x.Sp = x.L * Q - x.S

/-- The exact zero-defect classification target. -/
def ReflectionOrTranslation (x : Datum F) : Prop :=
  ReflectionFamily x ∨ TranslationFamily x

/-- Concrete interpretation of the logical Paper VII interface. -/
def specification (F : Type u) [Field F] [Fintype F] : PaperVIISpecification where
  Datum := Datum F
  crossDistinct := CrossDistinct
  inverseFreeIncidence := InverseFreeIncidence
  scalarWitnessIncidence := ScalarFrequencyIncidence
  witnessUnique := ScalarWitnessUnique
  commonDefectExistsUnique := CommonDefectExistsUnique
  defectDegreeBound := DefectDegreeBound
  zeroDefect := ZeroDefect
  reflectionOrTranslation := ReflectionOrTranslation
  frobeniusBase := FrobeniusBase
  fieldSize := fun _ => Fintype.card F
  modulusDegree := fun x => x.k
  primeField := fun _ => Nat.Prime (Fintype.card F)
  oddPrimePowerField := fun _ => Odd (Fintype.card F)

end Bilateral
end FortuneFormal
