# Programme status after the Kummer-twist compactification audit

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Status:** the proposed paired compactification programme has been completed through its hard kill criterion. It produces a correct Kummer quotient and new exact compactified point-count formula, but no reduction of the function-field `d=1` crown. The crown remains open.

## 1. Correction to the proposed route

The two cubic square classes are not universally quadratic twists.

For

\[
n=p-3,
\]

scalar dilation gives a `mu_n` action. The arithmetic forms are classified by

\[
H^1(\mathbf F_p,\mu_n)
\cong
\mathbf F_p^*/(\mathbf F_p^*)^n,
\]

which has two elements because `gcd(n,p-1)=2`.

The sign element represents the nontrivial class only when

\[
p\equiv1\pmod4.
\]

When

\[
p\equiv3\pmod4,
\]

the sign cocycle is a coboundary and the nonsquare class requires a nonquadratic scalar cocycle.

Thus a universal two-eigenspace quadratic-twist compactification does not exist.

## 2. Correct common quotient

The full Kummer quotient exists. On the irreducibility level,

\[
D_p=C_{1,1}/\mu_{p-3},
\]

and

\[
\boxed{
\#D_p(\mathbf F_p)=\frac{N_++N_-}{2}.
}
\]

On the complete root-cycle quotient open,

\[
\boxed{
\#U_p(\mathbf F_p)=\frac{p-1}{2}(N_++N_-).
}
\]

Therefore the common quotient is a valid positive geometric carrier, but proving that it has a rational point is exactly the original cubic-class positivity statement.

The class difference is a Kummer-local-system trace. The two arithmetic modes are exactly

\[
N_++N_-
\qquad\text{and}\qquad
N_+-N_-,
\]

which are already the invariant and anti-invariant q-line modes `S_0` and `S_chi`.

## 3. Natural projective quotient

Let `mathscr Y_p` be the smooth projective sparse ordered-root surface and put

\[
\mathscr Q_p=\mathscr Y_p/C_p.
\]

The root cycle has one projective fixed point,

\[
[0,1,\ldots,p-1],
\]

and is free elsewhere. Thus `mathscr Q_p` has one isolated wild quotient point.

The source has ample canonical class

\[
K_{\mathscr Y_p}
=
\mathcal O\left(\frac{(p-7)(p-2)}2\right)
\]

for admitted `p>=11`. Automatic transfer of `Q`-Gorenstein, discrepancy, Witt-rational or resolution properties across the wild quotient point is not proved and must not be assumed.

## 4. New exact compactified count

For

\[
W_p=N_2+\frac{N_++N_-}{2},
\]

the proper quotient satisfies

\[
\boxed{
\#\mathscr Q_p(\mathbf F_p)=1+(p-1)W_p.
}
\]

Its boundary and cubic open satisfy

\[
\boxed{
\#(\mathscr Q_p\setminus U_p)(\mathbf F_p)
=1+(p-1)N_2,
}
\]

and

\[
\boxed{
\#U_p(\mathbf F_p)
=\frac{p-1}{2}(N_++N_-).
}
\]

The unique constant term is the projective Artin--Schreier progression point. Every nonlinear affine irreducible orbit contributes one point for each of the `p-1` nonzero Frobenius shifts.

## 5. Why standard compactification theorems cannot finish the proof

A hypothetical standard congruence

\[
\#\mathscr Q_p(\mathbf F_p)\equiv1\pmod p
\]

would imply only

\[
W_p\equiv0\pmod p.
\]

This permits the failure value `W_p=0`. It also occurs with positivity: the exact census has

\[
W_{17}=17,
\qquad
\#\mathscr Q_{17}(\mathbf F_{17})=273\equiv1\pmod{17}.
\]

Boundary subtraction returns exactly

\[
\#U_p(\mathbf F_p)>0
\iff
N_++N_->0,
\]

which is strict invariant q-line nonsaturation.

Thus neither a proper-point congruence nor ordinary boundary bookkeeping reduces the theorem.

## 6. Closed continuations

Without a new ingredient, do not continue with:

1. a universal sign/quadratic twist;
2. an ordinary two-eigenspace compactification;
3. another standard Esnault/Witt point congruence;
4. a Fano/rationally-connected claim that ignores the wild quotient point;
5. another elimination into a bounded-degree coefficient curve;
6. higher cyclotomic moments;
7. larger prime scans;
8. a restatement of `S_0` nonsaturation as quotient positivity.

## 7. Exact remaining theorem

The Kummer compactification route can proceed only if one proves a genuinely new theorem of the form:

> **One-sided Kummer-quotient Frobenius theorem.** For the specific open general sparse quotient `U_p`, prove that its compactly supported Frobenius trace cannot attain the exact zero-point value.

Arithmetically this is

\[
\boxed{N_++N_->0.}
\]

Through the q-line ledger it is exactly exclusion of the invariant saturation value.

No existing theorem in the repository supplies this one-sided statement. The isolated wild quotient singularity is a legitimate independent local problem, but resolving it alone cannot overcome the exact point-count circularity.

## 8. Principal files

- `frontier/strategy/KUMMER_TWIST_AND_PROJECTIVE_QUOTIENT_COMPACTIFICATION_OBSTRUCTION_20260726.md`
- `frontier/strategy/KUMMER_TWIST_COMPACTIFICATION_HOSTILE_AUDIT_20260726.md`
- `frontier/strategy/kummer_twist_compactification_verify.py`
- `frontier/strategy/kummer_twist_compactification_results_20260726.json`

## 9. Final ruling

The paired compactification programme has generated new structural mathematics and corrected a false quadratic-twist premise. It has not proved `d=1`.

The decisive stopping point is again a genuinely new one-sided Frobenius/nonvanishing theorem, now expressed on the exact Kummer quotient. Further reformulation is not progress.
