import FortuneFormal.Comparator.P7Challenge
import FortuneFormal.Bilateral.Definitions
import FortuneFormal.Quadratic.ReductionInterface

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Comparator

universe u

variable {F : Type u} [Field F] [Fintype F]

/-- Literal translation from the independent Mathlib-only challenge datum to
FortuneFormal's implementation datum. Every field is copied; no theorem is
inserted during translation. -/
def toBilateral (d : FortuneChallenge.P7.Datum F) : Bilateral.Datum F where
  k := d.k
  L := d.L
  P := d.P
  S := d.S
  Pp := d.Pp
  Sp := d.Sp
  theta := d.theta
  c := d.c
  d := d.d
  mu := d.mu
  mup := d.mup
  nu := d.nu
  nup := d.nup
  k_pos := d.k_pos
  theta_ne_zero := d.theta_ne_zero
  P_monic := d.P_monic
  S_monic := d.S_monic
  Pp_monic := d.Pp_monic
  Sp_monic := d.Sp_monic
  P_irreducible := d.P_irreducible
  S_irreducible := d.S_irreducible
  Pp_irreducible := d.Pp_irreducible
  Sp_irreducible := d.Sp_irreducible
  P_degree := d.P_degree
  S_degree := d.S_degree
  Pp_degree := d.Pp_degree
  Sp_degree := d.Sp_degree
  mu_degree := d.mu_degree
  mup_degree := d.mup_degree
  nu_degree := d.nu_degree
  nup_degree := d.nup_degree
  mu_congruence := d.mu_congruence
  mup_congruence := d.mup_congruence
  nu_congruence := d.nu_congruence
  nup_congruence := d.nup_congruence
  L_coprime_P := d.L_coprime_P
  L_coprime_S := d.L_coprime_S
  L_coprime_Pp := d.L_coprime_Pp
  L_coprime_Sp := d.L_coprime_Sp
  P_coprime_S := d.P_coprime_S
  P_coprime_Pp := d.P_coprime_Pp
  P_coprime_Sp := d.P_coprime_Sp
  S_coprime_Pp := d.S_coprime_Pp
  S_coprime_Sp := d.S_coprime_Sp
  Pp_coprime_Sp := d.Pp_coprime_Sp

lemma crossDistinct_toBilateral (d : FortuneChallenge.P7.Datum F) :
    Bilateral.CrossDistinct (toBilateral d) ↔ FortuneChallenge.P7.CrossDistinct d := by
  rfl

lemma frobeniusBase_toBilateral (d : FortuneChallenge.P7.Datum F) :
    Bilateral.FrobeniusBase (toBilateral d) ↔ FortuneChallenge.P7.FrobeniusBase d := by
  rfl

lemma inverseFree_toBilateral (d : FortuneChallenge.P7.Datum F) :
    Bilateral.InverseFreeIncidence (toBilateral d) ↔
      FortuneChallenge.P7.InverseFreeIncidence d := by
  rfl

/-- Any implementation proof of the literal bilateral K2 theorem solves the
independent Mathlib-only challenge. -/
theorem challenge_of_bilateral
    (h : (Bilateral.specification F).K2EmptyStatement) :
    FortuneChallenge.P7.K2EmptyStatement F := by
  intro d hcross hodd hbase hk hinc
  have hbCross : Bilateral.CrossDistinct (toBilateral d) :=
    (crossDistinct_toBilateral d).2 hcross
  have hbBase : Bilateral.FrobeniusBase (toBilateral d) :=
    (frobeniusBase_toBilateral d).2 hbase
  have hbInc : Bilateral.InverseFreeIncidence (toBilateral d) :=
    (inverseFree_toBilateral d).2 hinc
  exact h (toBilateral d) hbCross hodd hbBase hk hbInc

/-- Zeta23-style conditional solution boundary: normalization is an explicit
hypothesis of this theorem, not a project axiom. -/
theorem challenge_k2_empty_of_normalization
    (hcert : Quadratic.K2CertifiedNormalizationStatement F) :
    FortuneChallenge.P7.K2EmptyStatement F :=
  challenge_of_bilateral (Quadratic.p7_k2_empty_of_certifiedNormalization hcert)

end Comparator
end FortuneFormal
