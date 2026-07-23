# Virtual Adams local collapse and the remaining global theorem

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling only; integer Fortune is untouched.  
**Primary reference:** C. Douglas Haessig and Antonio Rojas-León, *L-functions of symmetric powers of the generalized Airy family of exponential sums*, arXiv:1008.0408, especially the local Fourier description in §3, the invariant-factor calculation in §4, and the `f=x^3` formulas in §5.

## 0. Status ledger

- **PROVED:** the `p`-th Adams virtual representation of the rank-two cubic Airy sheaf has zero Swan conductor at infinity. More precisely, on the quadratic cover of inertia it kills the order-`p` wild characters exactly and becomes an actual tame rank-two inertia representation.
- **PROVED:** the two separate Swan conductors are equal to `(3p-3)/2`; the quotient of the two global symmetric-power `L`-functions has virtual degree `-2`.
- **PROVED:** this local tame representation cannot be promoted naively to an actual global rank-two sheaf: in the geometric `SL_2` representation ring the Adams class contains `-Sym^{p-2}`.
- **VERIFIED COMPUTATIONALLY:** exact modular reconstruction at `p=5,7,11` gives residual total degrees `2,4,6`; at `p=11` the common-factor degree is at most one, so a residual of total degree at most four is impossible.
- **OPEN:** an absolute bound for the first *virtual* Frobenius trace. Local conductor cancellation and bounded virtual Euler characteristic do not imply it.

## 1. Setup

Let `p>=7` be prime and let `A=Ai_{x^3}` be the rank-two cubic Airy sheaf on `A^1/F_p`. For every rank-two representation `V`,

\[
\Psi^p(V)=\operatorname{Sym}^p V-\det(V)\otimes\operatorname{Sym}^{p-2}V
\]

in the characteristic-zero representation ring, and its character is

\[
\chi_{\Psi^p(V)}(g)=\operatorname{Tr}(V(g^p)).
\]

At a rational point `u`, if the local inverse roots are `alpha_u,beta_u`, then this character is `alpha_u^p+beta_u^p`.

## 2. PROVED: exact local tame collapse at infinity

### Theorem 2.1

Let `I=I_infinity` be geometric inertia and let `I'` be the index-two subgroup obtained from the quadratic cover used in the local Fourier description of the cubic Airy sheaf. After a harmless finite extension of the constant field, the semisimplified restriction has the form

\[
A|_{I'}=(\chi\kappa)\oplus(\chi^{-1}\kappa),
\]

where:

- `chi` is the nontrivial Artin–Schreier character supplied by `L_psi(c t^3)` and has exact order `p`;
- `kappa` is the tame quadratic character supplied by the Kummer factor `L_rho(t)`;
- the nontrivial element of `I/I'` interchanges the two summands.

Then, as a semisimple virtual representation of `I`,

\[
\boxed{\Psi^p(A)|_I\cong\operatorname{Ind}_{I'}^I(\kappa).}
\]

In particular,

\[
\boxed{\operatorname{Swan}_\infty(\Psi^p(A))=0.}
\]

The resulting tame rank-two inertia representation has no invariant vector.

### Proof

For `g in I'`, the two eigencharacters of `A(g)` are `chi(g)kappa(g)` and `chi(g)^{-1}kappa(g)`. Since `chi^p=1` and `p` is odd,

\[
\chi_{\Psi^p(A)}(g)
=(\chi\kappa)^p(g)+(\chi^{-1}\kappa)^p(g)
=2\kappa(g).
\]

For `g notin I'`, its image in `I/I'` is nontrivial. Because `p` is odd, `g^p` is still outside `I'`. The induced rank-two Airy representation has trace zero on this coset, so

\[
\chi_{\Psi^p(A)}(g)=\operatorname{Tr}(A(g^p))=0.
\]

The character that is `2kappa` on `I'` and zero on the other coset is exactly the character of `Ind_{I'}^I(kappa)`. Character equality determines semisimplification because the relevant inertia image is finite. This induced representation is tame because `kappa` is tame. It has no invariants because `kappa` is nontrivial on `I'`. ∎

### Corollary 2.2: exact Swan equality

Haessig–Rojas-León give, for `f=x^3`,

\[
\deg L(A^1,\operatorname{Sym}^p A,T)=\frac{p-5}{2},
\qquad
\deg L(A^1,\det A\otimes\operatorname{Sym}^{p-2}A,T)=\frac{p-1}{2}.
\]

The ranks are `p+1` and `p-1`. Their GOS formula `deg L=Swan-rank` therefore gives

\[
\operatorname{Swan}_\infty(\operatorname{Sym}^p A)
=\frac{p-5}{2}+p+1
=\frac{3p-3}{2},
\]

and

\[
\operatorname{Swan}_\infty(\det A\otimes\operatorname{Sym}^{p-2}A)
=\frac{p-1}{2}+p-1
=\frac{3p-3}{2}.
\]

Thus the local character proof and the independent global degree formula agree exactly. The virtual rank is two, the virtual Swan conductor is zero, and

\[
\deg R_p(T)=\frac{p-5}{2}-\frac{p-1}{2}=-2.
\]

This is genuine cancellation, not a dimension heuristic.

## 3. Why this does not yet prove bounded global cohomology

For `p>5`, the geometric monodromy of the cubic Airy sheaf is `SL_2`. In its characteristic-zero representation ring,

\[
[\Psi^p(\mathrm{Std})]=[\operatorname{Sym}^p(\mathrm{Std})]
-[\operatorname{Sym}^{p-2}(\mathrm{Std})].
\]

The coefficient of the irreducible `Sym^{p-2}` is `-1`. Hence this class is not the class of an actual semisimple `SL_2` representation: actual representations have nonnegative irreducible multiplicities.

Therefore the actual tame rank-two representation found at infinity is only a **local** representative of the Adams class. It cannot be substituted for the global Adams virtual sheaf. The positive and negative high-rank constituents can cancel completely on inertia while remaining unrelated under global arithmetic Frobenius.

This identifies the exact logical failure in the tempting argument:

> `virtual rank 2 + Swan 0` implies only bounded virtual Euler characteristic. It does not imply a bounded total number of global Frobenius eigenvalues, nor a bounded first virtual trace.

## 4. Purity and the rigorous fallback

For odd `p` and `p-2`, the local invariant factor at infinity in Haessig–Rojas-León is `1`. The two global cohomology spaces are therefore pure of the same weight `p+1` after the determinant twist. Put

\[
V_p=H_c^1(A^1_{\overline{F}_p},\operatorname{Sym}^p A),
\qquad
W_p=H_c^1(A^1_{\overline{F}_p},\det A\otimes\operatorname{Sym}^{p-2}A).
\]

Then

\[
\dim V_p=\frac{p-5}{2},
\qquad
\dim W_p=\frac{p-1}{2},
\]

and every Frobenius eigenvalue on both spaces has absolute value `p^((p+1)/2)`. Consequently

\[
|\operatorname{Tr}(F_p|V_p)-\operatorname{Tr}(F_p|W_p)|
\le (p-3)p^{(p+1)/2}.
\]

This recovers the rigorous linear-loss estimate and shows exactly where the factor `p` enters: it is the sum of the two global dimensions, not the local conductor.

## 5. Focused exact quotient computation

Script: `frontier/d1_symp/virtual_quotient_probe.py`  
Committed output: `frontier/d1_symp/virtual_quotient_probe_results.txt`

The script reconstructs the two global `L`-polynomials exactly modulo split coefficient primes `ell=1 mod p`. It uses:

1. exact arithmetic in `F_{p^m}`;
2. an exact `p`-ary DFT over `F_ell` to obtain the complete multiset of cubic Airy sums over `F_{p^m}`;
3. the rank-two recurrence with determinant `p^m`;
4. Newton identities to reconstruct the global polynomials through their exact known degrees.

It is a mechanism test, not a broad prime sweep.

| `p` | degrees `(Sym^p, det Sym^{p-2})` | modular gcd degree | residual total degree |
|---:|---:|---:|---:|
| 5 | `(0,2)` | `0` | `2` |
| 7 | `(1,3)` | `0` | `4` |
| 11 | `(3,5)` | `1` at five split primes | `6` |

At `p=5` and `p=11`, the independently reconstructed first virtual trace agrees modulo every coefficient prime with the committed exact value `-p T_p`.

### Rigorous consequence at `p=11`

The reciprocal characteristic polynomials are integral over `Z[zeta_11]`. Any common characteristic-zero Frobenius factor reduces to a common factor of the same degree at every split prime where the displayed leading coefficients remain nonzero. The script checks nonvanishing. Since the modular gcd has degree one, the characteristic-zero common-factor degree is at most one. Therefore, after all possible common-factor cancellation, the total residual degree is at least

\[
3+5-2\cdot1=6.
\]

Hence the particularly attractive strengthening

\[
\text{“the quotient is represented by at most four residual eigenvalues”}
\]

is **false already at `p=11`**.

This does **not** disprove a uniformly bounded residual degree with a larger bound, and it does not disprove the trace bound with `C=4`: six or more eigenvalues may have forced phase cancellation. The sequence `2,4,6` is only **HEURISTIC** evidence that factor cancellation alone may not stabilize.

## 6. Smallest remaining theorem

The exact analytic target is now a cross-symmetric-power Frobenius-correlation theorem:

### OPEN theorem

There is an absolute constant `C` such that, for every prime `p=2 mod 3`,

\[
\boxed{
|\operatorname{Tr}(F_p|V_p)-\operatorname{Tr}(F_p|W_p)|
\le C p^{(p+1)/2}.
}
\]

Equivalently, `|T_p|<=C p^((p-1)/2)`.

The new local theorem removes wild conductor from the list of possible obstructions. What remains must be genuinely global and Frobenius-equivariant. A successful proof must supply at least one of:

1. a Dwork/Frobenius chain map pairing the two cohomology complexes up to a bounded trace defect;
2. an exact cross-`k` functional identity for the two Airy `L`-functions, stronger than their separate functional equations;
3. a valid Jacobi-sum decomposition of the cyclic cubic **linear section**, producing trace cancellation without relying on ambient Fermat character labels.

Separate degree formulas, local monodromy, purity, and virtual Euler characteristic cannot prove the required bound. This is the precise failure certificate.
