import FortuneFormal.Comparator.P7ChallengeDeps

set_option autoImplicit false

namespace FortuneChallenge
namespace P7

universe u

/-- Independent trusted statement of Paper VII quadratic emptiness.

No proof is supplied here.  In particular this file does not convert the
project's normalization axiom into an unconditional challenge theorem.
-/
def K2EmptyStatement (F : Type u) [Field F] [Fintype F] : Prop :=
  ∀ d : Datum F,
    CrossDistinct d →
    Odd (Fintype.card F) →
    FrobeniusBase d →
    d.k = 2 →
      ¬ InverseFreeIncidence d

end P7
end FortuneChallenge
