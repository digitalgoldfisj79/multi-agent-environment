import Mathlib

set_option autoImplicit false

noncomputable section

namespace FortuneFormal
namespace Bilateral

open Polynomial

universe u

variable {F : Type u} [Field F]

/-- Two monic polynomials of the same degree are equal when one divides the
other. -/
theorem monic_eq_of_dvd_of_natDegree_eq
    {f g : Polynomial F} (hf : f.Monic) (hg : g.Monic)
    (hdeg : f.natDegree = g.natDegree) (hdiv : f ∣ g) : f = g := by
  rcases hdiv with ⟨r, hr⟩
  subst g
  have hrmonic : r.Monic := hf.of_mul_monic_left hg
  have hrdeg : r.natDegree = 0 := by
    rw [hf.natDegree_mul hrmonic] at hdeg
    omega
  have hrone : r = 1 := hrmonic.natDegree_eq_zero.mp hrdeg
  rw [hrone, mul_one]

/-- If an irreducible monic degree-`n` factor divides a product of two monic
polynomials of degree `n`, the product ordering has only the two expected
possibilities. -/
theorem twoFactor_ordering
    {f g A B : Polynomial F}
    (hfIrr : Irreducible f)
    (hfMonic : f.Monic) (hgMonic : g.Monic)
    (hAMonic : A.Monic) (hBMonic : B.Monic)
    (hfDeg : f.natDegree = A.natDegree)
    (hABDeg : A.natDegree = B.natDegree)
    (hgDeg : g.natDegree = A.natDegree)
    (hprod : A * B = f * g) :
    (A = f ∧ B = g) ∨ (A = g ∧ B = f) := by
  have hfdiv : f ∣ A * B := by
    rw [hprod]
    exact dvd_mul_right f g
  rcases hfIrr.prime.dvd_mul.mp hfdiv with hfA | hfB
  · have hAf : A = f :=
      (monic_eq_of_dvd_of_natDegree_eq hfMonic hAMonic hfDeg hfA).symm
    left
    refine ⟨hAf, ?_⟩
    subst A
    have heq : f * B = f * g := hprod
    have hzero : f * (B - g) = 0 := by
      rw [mul_sub, heq, sub_self]
    exact sub_eq_zero.mp
      ((mul_eq_zero.mp hzero).resolve_left hfIrr.ne_zero)
  · have hBf : B = f := by
      have hdeg : f.natDegree = B.natDegree := hfDeg.trans hABDeg
      exact (monic_eq_of_dvd_of_natDegree_eq hfMonic hBMonic hdeg hfB).symm
    right
    refine ⟨?_, hBf⟩
    subst B
    have heq : A * f = f * g := hprod
    have heq' : f * A = f * g := by
      calc
        f * A = A * f := by ring
        _ = f * g := heq
    have hzero : f * (A - g) = 0 := by
      rw [mul_sub, heq', sub_self]
    exact sub_eq_zero.mp
      ((mul_eq_zero.mp hzero).resolve_left hfIrr.ne_zero)

end Bilateral
end FortuneFormal
