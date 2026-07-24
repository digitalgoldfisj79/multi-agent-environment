# Main-branch status after the full Weil bridge and sparse hook identification

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only. Integer Fortune remains untouched.  
**Status:** this file supersedes the earlier main-branch status notes on this branch.

## 1. Route discipline

Only two branches remain admissible:

1. the absolute Frobenius-correlation estimate;
2. the explicit nested-section/nearby-cycle comparison into the hook irreducibility ledger.

Coefficient resonance, bare-shift localization, generic complete-intersection bounds, common-factor collapse, slope pairing and unguided prime sweeps remain closed or non-decisive.

## 2. PROVED: exact geometric reduction

For `p=5 mod 6`,

\[
T_p
=
p^2\operatorname{Tr}
\left(
\sigma^{\pm1}F
\mid H^{p-5}_{prim}(X_p^{perm})
\right),
\]

where `X_p^perm` is the smooth cyclic `(2,3)` complete intersection. Its primitive rank is

\[
\frac{2^{p-1}-1}{3}.
\]

## 3. PROVED: cyclic regularity and two multiplicity spaces

As a `C_p` representation,

\[
H_p|_{C_p}
\cong
\mathbf Q_\ell[C_p]^{\oplus q_p},
\qquad
q_p=\frac{2^{p-1}-1}{3p}.
\]

For the affine normalizer,

\[
H_p
\cong
M_{0,p}\oplus(\rho_p\otimes M_{1,p}),
\qquad
\dim M_{0,p}=\dim M_{1,p}=q_p.
\]

Define

\[
\mathcal D_p=M_{0,p}-M_{1,p}.
\]

Then

\[
T_p=p^2\operatorname{Tr}(F|\mathcal D_p).
\]

## 4. PROVED: full Airy--primitive virtual Weil identity

Let

\[
\mathcal R_p=U_p-U_{p-2}(-1).
\]

Kummer averaging over cubic coefficient twists and relative degree-`p` Artin--Schreier descent prove, for every `r>=1`,

\[
\operatorname{Tr}(F^r|\mathcal R_p)
=
p^{3r}\operatorname{Tr}(F^r|\mathcal D_p).
\]

Consequently,

\[
\boxed{
\mathcal R_p^{ss}=\mathcal D_p(-3)^{ss}
}
\]

in the Grothendieck group of semisimple Weil representations, with equality of the complete Frobenius determinant ratios.

This closes the Airy-to-cyclic-linear-section comparison at all Frobenius powers. It is a semisimple virtual identity, not a constructed quasi-isomorphism.

## 5. PROVED: the precise geometric hook target

For the general half-theorem primes `p>=11`, define the sparse ordered-root surface inside `X_p` by

\[
Y_p
=
\{s_2=s_3=\cdots=s_{p-4}=0\}
\subset\mathbf P(H/L),
\qquad
s_m=\sum_i x_i^m.
\]

Newton identities identify its affine ordered-root tuples exactly with the roots of

\[
Z^p+A Z^3+B Z^2+C Z+D.
\]

The separable open `Y_p^sep` is a free `S_p`-torsor over the sparse coefficient surface modulo translation and scaling. The virtual hook representation

\[
\Lambda_p=\sum_i(-1)^i\bigwedge^i\mathrm{Std}
\]

has character `p` on a `p`-cycle and zero otherwise. Hence its associated local system has trace exactly `p` times the irreducibility indicator.

The ambient Airy module is also an alternating hook multiplicity:

\[
\mathcal K_{ambient}
=
\sum_i(-1)^i
\operatorname{Hom}_{S_p}
\left(\bigwedge^i\mathrm{Std},H_p\right),
\]

and

\[
\mathcal K_{ambient}^{ss}=\mathcal D_p^{ss},
\qquad
\mathcal R_p^{ss}=\mathcal K_{ambient}(-3)^{ss}.
\]

Thus the source and target of the application theorem are now two alternating-hook objects in the same nested root geometry.

The prime `p=5` is exceptional: its full sparse family contains the Airy section rather than being a deeper section. It is already proved directly and is excluded from the general nested-section theorem.

## 6. OPEN: analytic main theorem

The estimate remains

\[
|\operatorname{Tr}(F|\mathcal R_p)|
\le C p^{(p+1)/2},
\]

or equivalently

\[
|\operatorname{Tr}(F|\mathcal D_p)|
\le C p^{(p-5)/2}.
\]

The virtual identity explains the exponential cancellation but does not prove the absolute constant governing the remaining difference between `U_p` and `U_{p-2}(-1)`.

## 7. OPEN: exact application theorem

For `p>=11`, the sparse surface is cut out inside `X_p` by

\[
s_4,\ldots,s_{p-4},
\]

exactly `p-7` successive equations. The degree change from ambient middle cohomology `p-5` to surface middle cohomology `2` is also `p-7`.

The required comparison is therefore now specific: an iterated vanishing-cycle, or equivalent perverse complete-intersection, theorem along this sequence after alternating hook extraction.

Weight compatibility forces the pure middle normalization

\[
\mathcal K_{ambient}
\left(\frac{p-7}{2}\right)
=
\mathcal R_p
\left(\frac{p-1}{2}\right).
\]

The target identity must have the form

\[
\mathcal K_{sparse}^{load}
=
\mathcal K_{ambient}
\left(\frac{p-7}{2}\right)
+
\mathcal B_p,
\]

where `B_p` explicitly contains:

1. main, Tate and excluded Artin--Schreier terms;
2. punctual/nearby-cycle transport;
3. the arithmetic quadratic twist;
4. discriminant fibres;
5. `q=2`;
6. `q=infinity`;
7. finite normalization from geometric coefficient orbits to the two arithmetic classes.

After this identity, the remaining positivity/certificate implication is finite ledger work.

## 8. Verification status

### VERIFIED COMPUTATIONALLY

- first-trace normalization at `p=5,11,17,23,29`;
- direct `p=5` cyclic fixed-point and regular-character model;
- exact `r=3` divisibility consequences at `p=11,17,23,29`;
- complete `p=5,r=2` three-Kummer-twist average over `F_25`;
- primitive Betti formula through odd primes `p<=199`;
- committed normal-form and per-cell counts at `p=5,7,11` independently agree with the hook census.

These checks test concrete structural consequences. The all-degree Weil identity and sparse-root identification are symbolic proofs, not extrapolations from the checks.

## 9. Stop rule

Continue only by:

- proving the absolute Airy correlation estimate; or
- constructing the iterated hook vanishing-cycle comparison and its explicit boundary complex.

Do not return to resonance coefficients, raw spectra, generic estimates, larger prime sweeps or surrogate invariants without a new formula directly targeting one of these statements.
