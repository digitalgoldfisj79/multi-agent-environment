import Mathlib

set_option autoImplicit false

noncomputable section

/-!
Mathlib-only trusted statement layer for Paper VII K2 emptiness.

This file deliberately does not import `FortuneFormal`.  It restates the
literal finite-field polynomial datum needed for the published quadratic
claim so that the challenge can be audited independently of the implementation.
-/
namespace FortuneChallenge
namespace P7

open Polynomial

universe u

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

abbrev scalar (a : F) : Polynomial F := Polynomial.C a

def CrossDistinct (x : Datum F) : Prop :=
  x.P ≠ x.S ∧ x.P ≠ x.Pp ∧ x.P ≠ x.Sp ∧
  x.S ≠ x.Pp ∧ x.S ≠ x.Sp ∧ x.Pp ≠ x.Sp

def FrobeniusBase (x : Datum F) : Prop :=
  x.L = Polynomial.X ^ Fintype.card F - Polynomial.X

def MuInverseFreeAt (x : Datum F) (c : F) : Prop :=
  x.P ∣ scalar c * x.L * x.S + scalar x.theta * x.Pp ∧
  x.Pp ∣ scalar c * x.L * x.Sp - scalar x.theta * x.P

def NuInverseFreeAt (x : Datum F) (d : F) : Prop :=
  x.S ∣ scalar d * x.L * x.P + scalar x.theta * x.Sp ∧
  x.Sp ∣ scalar d * x.L * x.Pp - scalar x.theta * x.S

def InverseFreeIncidence (x : Datum F) : Prop :=
  MuInverseFreeAt x x.c ∧ NuInverseFreeAt x x.d

end P7
end FortuneChallenge
