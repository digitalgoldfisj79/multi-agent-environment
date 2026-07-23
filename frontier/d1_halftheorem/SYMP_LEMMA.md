# The cubic-Airy Adams trace lemma after the collapse theorem

**Date:** 2026-07-23.  
**Scope:** function-field `d=1` Fortune sibling only; integer Fortune is untouched.

## 0. Status

- **PROVED:** for `p≡2 (mod 3)`, the original two-parameter WTCK deviation collapses to one cubic hyperplane sum `T_p`, with `D_b=-T_p/p` for `b≠0` and `D_0=(p-1)T_p/p`.
- **PROVED:** the `p`-th Adams virtual representation of the rank-two cubic Airy sheaf has zero Swan conductor at infinity; locally it is represented by an actual tame rank-two inertia representation.
- **VERIFIED COMPUTATIONALLY:** exact quotient reconstruction at `p=5,7,11`; at `p=11`, at least six global Frobenius eigenvalues remain after every possible common-factor cancellation.
- **OPEN:** the absolute-constant first virtual Frobenius trace bound.
- **CONDITIONAL:** the implication from that trace bound to `FF-Fortune(p,1)` until the endpoint/main/Tate/Artin–Schreier and nearby-cycle ledger is written without gaps.

## 1. Exact one-parameter reduction

Let

\[
K=\mathbf F_{p^p},\qquad
H=\{x\in K:\operatorname{Tr}_{K/\mathbf F_p}(x)=0\},
\]

and

\[
T_p=\sum_{x\in H}\psi\bigl(\operatorname{Tr}(x^3)\bigr).
\]

For `p≡2 (mod 3)`, the proved collapse lemma gives

\[
D_b=-\frac{T_p}{p}\quad(b\ne0),
\qquad
D_0=\frac{p-1}{p}T_p=-(p-1)D_b.
\]

Thus the remaining analytic target is exactly

\[
\boxed{|T_p|\le C p^{(p-1)/2}}
\]

for an absolute constant `C`.

The numerical identity for `D_0` removes it as an independent numerical estimate. It does **not** prove that all punctual nearby-cycle constituents vanish categorically.

## 2. Equivalent cubic-Airy Adams trace

Let `A=Ai_{x^3}` be the rank-two cubic Airy sheaf on `A^1/F_p`. At `u∈F_p`, let its local inverse roots be `alpha_u,beta_u`. Orthogonality gives

\[
T_p=-\frac1p\sum_{u\in\mathbf F_p}(\alpha_u^p+\beta_u^p).
\]

For every rank-two representation,

\[
\alpha^p+\beta^p
=\operatorname{Tr}(\operatorname{Sym}^p)
-\alpha\beta\,\operatorname{Tr}(\operatorname{Sym}^{p-2}).
\]

Hence define the virtual Adams sheaf

\[
\Psi^p(A)=\operatorname{Sym}^p A
-\det(A)\otimes\operatorname{Sym}^{p-2}A.
\]

If

\[
V_p=H_c^1(\mathbf A^1_{\overline{\mathbf F}_p},\operatorname{Sym}^p A),
\qquad
W_p=H_c^1(\mathbf A^1_{\overline{\mathbf F}_p},
\det(A)\otimes\operatorname{Sym}^{p-2}A),
\]

then the exact target is

\[
\boxed{
|\operatorname{Tr}(F_p|V_p)-\operatorname{Tr}(F_p|W_p)|
\le C p^{(p+1)/2}.
}
\]

This is equivalent to the displayed bound for `T_p`.

## 3. PROVED: local virtual conductor collapse

Haessig–Rojas-León's local Fourier description gives, on the quadratic inertia cover `I'⊂I_∞`,

\[
A|_{I'}=(\chi\kappa)\oplus(\chi^{-1}\kappa),
\]

where `chi` is an order-`p` wild Artin–Schreier character and `kappa` is a tame quadratic character. Since the character of the `p`-th Adams operation is `g↦Tr(A(g^p))`, raising to the `p`-th power kills `chi` exactly. One obtains

\[
\boxed{\Psi^p(A)|_{I_\infty}^{ss}\cong
\operatorname{Ind}_{I'}^{I_\infty}(\kappa).}
\]

Therefore

\[
\boxed{\operatorname{Swan}_\infty(\Psi^p(A))=0.}
\]

The two separate Swan conductors are equal:

\[
\operatorname{Swan}_\infty(\operatorname{Sym}^p A)
=\operatorname{Swan}_\infty(\det A\otimes\operatorname{Sym}^{p-2}A)
=\frac{3p-3}{2}.
\]

This follows independently from the exact Haessig–Rojas-León degree formulas

\[
\dim V_p=\frac{p-5}{2},
\qquad
\dim W_p=\frac{p-1}{2}.
\]

Thus the quotient

\[
R_p(T)=
\frac{L(\mathbf A^1,\operatorname{Sym}^p A,T)}
{L(\mathbf A^1,\det A\otimes\operatorname{Sym}^{p-2}A,T)}
\]

has virtual degree `-2`.

## 4. Why local rank two is not a global rank-two theorem

For `p>5`, the geometric monodromy is `SL_2`. In its characteristic-zero representation ring,

\[
[\Psi^p(\mathrm{Std})]
=[\operatorname{Sym}^p(\mathrm{Std})]
-[\operatorname{Sym}^{p-2}(\mathrm{Std})].
\]

The irreducible `Sym^{p-2}` occurs with coefficient `-1`. Therefore the Adams class is not the class of an actual global semisimple rank-two representation.

The tame rank-two object at infinity is consequently only a local representative. Complete cancellation of wild inertia does not imply cancellation of the two global Frobenius modules.

This is the exact obstruction to the inference

> virtual rank two plus Swan zero implies a bounded number of global eigenvalues.

It implies only bounded virtual Euler characteristic.

## 5. Rigorous fallback

For odd `p` and `p-2`, the local invariant factor at infinity is trivial, and both global cohomology spaces are pure of weight `p+1` after the determinant twist. Therefore

\[
|\operatorname{Tr}(F_p|V_p)-\operatorname{Tr}(F_p|W_p)|
\le(\dim V_p+\dim W_p)p^{(p+1)/2}
=(p-3)p^{(p+1)/2}.
\]

Equivalently,

\[
\boxed{|T_p|\le(p-3)p^{(p-1)/2}},
\qquad
\boxed{|D_b|\le(p-3)p^{(p-3)/2}}.
\]

This is **PROVED** but loses a factor of order `p` and does not prove the half-theorem.

## 6. Focused quotient test

The reproducible exact probe

`frontier/d1_symp/virtual_quotient_probe.py`

reconstructs the two global `L`-polynomials modulo split coefficient primes. It tests common Frobenius factors rather than extending the raw `T_p` table.

| `p` | degrees `(V_p,W_p)` | common-factor degree | residual total degree |
|---:|---:|---:|---:|
| 5 | `(0,2)` | `0` | `2` |
| 7 | `(1,3)` | `0` | `4` |
| 11 | `(3,5)` | at most `1` | at least `6` |

At `p=11`, five independent split coefficient primes give modular gcd degree one with nonzero leading coefficients. Any characteristic-zero common factor must reduce to a common modular factor, so the characteristic-zero common-factor degree is at most one. Hence the residual total degree is at least six.

Therefore the proposed interpretation of the observed `C≈4` profile as the trace of at most four residual eigenvalues is **DISPROVED** already at `p=11`.

This does not disprove the absolute trace bound or the working numerical conjecture `C=4`; six or more eigenvalues may obey structured phase cancellation.

## 7. Exact calibration

The normalized values `T_p/p^{(p-1)/2}` for
`p=5,11,17,23,29,41,47,53` are approximately

\[
0,\ 2.0000,\ 1.7059,\ -1.0605,\ -2.6823,\ 1.5852,\ -0.1260,\ 0.9223.
\]

The observed supremum is `2.6823`. The statement `C=4` remains a **HEURISTIC working conjecture**, not a rank consequence.

## 8. Smallest remaining theorem

The remaining theorem is a genuinely global cross-symmetric-power Frobenius-correlation estimate:

\[
|\operatorname{Tr}(F_p|V_p)-\operatorname{Tr}(F_p|W_p)|
\le C p^{(p+1)/2}.
\]

A valid proof must provide one of:

1. a Frobenius-equivariant Dwork/cohomological chain map pairing `V_p` and `W_p` up to a bounded trace defect;
2. an exact cross-`k` identity between the two Airy `L`-functions, stronger than their separate functional equations;
3. a Jacobi-sum decomposition for the cyclic cubic **linear section**, not the ambient diagonal Fermat tensor product.

Separate GOS degrees, purity, local monodromy, and virtual Euler characteristic are insufficient.

## 9. Application boundary

Even after proving the trace bound, the following must be checked explicitly:

1. `T_p→D_b` normalization;
2. transport into the Cyclic-Adams weight-three estimate;
3. endpoint/main/Tate/Artin–Schreier subtraction;
4. sufficiency of `D_0=-(p-1)D_b` for the nearby-fibre ledger;
5. final implication to `FF-Fortune(p,1)` for `p≡2 (mod 3)`.

Until that chain is complete, the half-theorem is **CONDITIONAL**.
