# d=1 discriminant/dynamics branch handover

**Branch:** `gpt56/d1-discriminant-dynamics-20260721`  
**Base:** `claude/experimental-branch-review-am0zpg`  
**Date:** 2026-07-21

## What is proved

1. **Exact degree-p discriminant formula.** For
   \(F_{a,c,d}=X^p+aX^3+cX+d\), the derivative is quadratic and the
   discriminant collapses to the explicit formula in
   `DISCRIMINANT_MASS.md`.

2. **Exact complete-slice Möbius mass.** The full \((c,d)\)-sum is
   \(0\), \(\pm p\), or \(\pm2p\), according to elementary quadratic
   characters. The zero-discriminant count is also exact.

3. **Canonical local convention corrected.** On \(\mathbf F_p\),
   \(F(x)=a x^3+(c+1)x+d\). The earlier unshifted diagnostic restriction
   was misindexed. All current local results use the `+1` convention.

4. **Local admissibility implies squarefreeness.** If
   \(aX^3+(c+1)X+d\) is rootless, then
   \(\operatorname{Disc}(F_{a,c,d})\ne0\). Thus the discriminant character
   on the admissible set is always \(\pm1\) and exactly records factor
   parity through Pellet's formula.

5. **Exact fixed-linear-coefficient cubic count.** With
   \(\rho=\chi(-3)\), for every \(u\ne0\), exactly
   \((p-\rho)/3\) values of \(v\) make \(X^3+uX+v\) irreducible. The
   \(u=0\) count is \((1+\rho)(p-1)/3\). Total admissible count is
   \((p^2-1)/3\).

6. **Exact restricted-mass decomposition.** The admissible Möbius mass is
   \((2S_a+C_a-R_a-\tau_a)/3\), where \(S_a\) is already known exactly
   and \(C_a,R_a\) are two explicit complete character sums.

7. **Uniform one-variable Weil theorem.** At most three fibres are
   exceptional in each sum. Hence
   \[
   |M_a^{\mathrm{loc}}(p)|
   \le (8p^{3/2}+10p+1)/3,
   \]
   and the admissible family is asymptotically split equally between odd
   and even factor parity:
   \[
   N_{a,\pm}=p^2/6+O(p^{3/2}).
   \]

8. **Constructive-dynamics pruning.** The exact period-p equivalence is
   proved. Affine dynamics gives only excluded Artin--Schreier constant
   offsets, and a global rational semiconjugacy from translation cannot
   produce a nonlinear map.

## Verification

`discriminant_mass_check.py` is standard-library only. It checks:

- the pointwise discriminant formula against Sylvester determinants;
- complete-slice masses and zero counts;
- the fixed-\(u\) admissible counts;
- local squarefreeness;
- the exact restricted-mass identity.

Equivalent independent notebook checks passed for all primes through 199
for the fixed-\(u\) theorem and through 79 for the full restricted identity.
No GitHub Actions workflow has yet been added.

## What this does not prove

Positive discriminant character means an odd number of irreducible factors,
not necessarily one. A reducible product of three or more factors remains
in the positive class. Therefore these results do not by themselves prove
FF-Fortune\((p,1)\).

## Exact interface with RQM

The discriminant theorem reduces the remaining positive-parity obstruction
to locally admissible members with at least three irreducible factors. An
RQM or reducible-count theorem proving that this odd reducible sector is
strictly smaller than \(N_{a,+}\) forces an irreducible member.

## Next non-overlapping target

The empirical masses are \(O(p)\), not merely \(O(p^{3/2})\). After
splitting the nested quadratic character, \(C_a\) and \(R_a\) become finite
linear combinations of point-count traces on explicit double covers of
\(\mathbf P^1\times\mathbf P^1\):

- cross-term branch bidegrees `(6,4)` and `(8,4)`;
- root-incidence branch bidegrees `(4,6)`.

The expected sharpening is

\[
C_a,R_a=O(p),
\qquad
M_a^{\mathrm{loc}}(p)=O(p).
\]

The remaining work is a singularity/irregularity audit of those fixed
double-plane surfaces. This is a finite algebraic-geometry problem, not a
growing-dimension character-sum problem. It is the recommended next action
on this branch.