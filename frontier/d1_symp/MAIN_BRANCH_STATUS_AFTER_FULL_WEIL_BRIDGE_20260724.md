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

## 5. PROVED: precise sparse hook geometry

For the general half-theorem primes `p>=11`, define

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

The separable open is a free ordered-root `S_p`-torsor over the sparse coefficient surface modulo translation and scaling. The virtual representation

\[
\Lambda_p=\sum_i(-1)^i\bigwedge^i\mathrm{Std}
\]

has character `p` on a `p`-cycle and zero otherwise, so the associated local system has trace exactly `p` times the irreducibility indicator.

The ambient Airy module is also an alternating hook multiplicity:

\[
\mathcal K_{ambient}
=
\sum_i(-1)^i
\operatorname{Hom}_{S_p}
\left(\bigwedge^i\mathrm{Std},H_p\right),
\]

with

\[
\mathcal K_{ambient}^{ss}=\mathcal D_p^{ss},
\qquad
\mathcal R_p^{ss}=\mathcal K_{ambient}(-3)^{ss}.
\]

Thus source and target are explicit alternating-hook objects in one nested root geometry.

The prime `p=5` is exceptional: its full sparse family contains the Airy section rather than being a deeper section. It remains a separately proved base case.

## 6. PROVED: finite normal-form and q-line arithmetic assembly

For

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad
A=\chi(a),
\]

every `c!=0` maps to

\[
q=-3/c,
\qquad
\varepsilon=A\chi(q).
\]

The split and nonsplit changes of variable are defined over `F_p`, preserve irreducibility and give a bijection of constant parameters. The two arithmetic values `A=+1,-1` partition all `2(p-1)` cells.

For generic `q!=2`, let `E_epsilon(q)` be the alternating hook `H_c^1` trace. Then

\[
pI_\varepsilon(q)=p-E_\varepsilon(q).
\]

Define

\[
S_0=\sum_{q\ne0,2}(E_+(q)+E_-(q)),
\]

\[
S_\chi=\sum_{q\ne0,2}\chi(q)(E_+(q)-E_-(q)),
\]

and the two boundary counts

\[
B_A=I_A(\infty)+I_{A\chi(2)}(2).
\]

Then the arithmetic count is exactly

\[
\boxed{
N_A(p)
=(p-2)+B_A
-
\frac{S_0+A S_\chi}{2p}.
}
\]

The parity-protected crown certificate is therefore

\[
(p-2)+B_A-rac{S_0+A S_\chi}{2p}
\notin2p\mathbf Z_{\ge0}
\]

for at least one sign `A`.

The finite arithmetic assembly is complete. The remaining application theorem needs only the two global traces `S_0,S_chi` and the explicit boundary traces.

## 7. OPEN: analytic main theorem

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

## 8. OPEN: exact application theorem

For `p>=11`, the sparse surface is cut out inside `X_p` by the `p-7` successive equations

\[
s_4,\ldots,s_{p-4}.
\]

The degree change from ambient middle cohomology `p-5` to surface middle cohomology `2` is also `p-7`. The required comparison is an iterated vanishing-cycle, or equivalent perverse complete-intersection, theorem along this sequence after alternating hook extraction.

Weight compatibility forces the pure middle normalization

\[
\mathcal K_{ambient}
\left(\frac{p-7}{2}\right)
=
\mathcal R_p
\left(\frac{p-1}{2}\right).
\]

The comparison must identify the invariant and quadratic projectors producing `S_0` and `S_chi`. Its remaining cones must supply, with exact signs and twists:

1. main, Tate and excluded Artin--Schreier terms;
2. punctual/nearby-cycle transport;
3. discriminant fibres;
4. `q=2`;
5. `q=infinity`.

After those traces are known, the q-line formula above gives the final certificate without further geometric invention.

## 9. Verification status

### VERIFIED COMPUTATIONALLY

- first-trace normalization at `p=5,11,17,23,29`;
- direct `p=5` cyclic fixed-point and regular-character model;
- exact `r=3` bridge consequences at `p=11,17,23,29`;
- complete `p=5,r=2` three-Kummer-twist average over `F_25`;
- primitive Betti formula through odd primes `p<=199`;
- split/nonsplit normal-form cells and committed totals at `p=5,7,11`;
- q-line projector reconstruction of `N_+,N_-` at `p=5,7,11`.

These checks test structural consequences. The all-degree Weil identity, sparse-root identification and q-line formulas are symbolic proofs, not extrapolations from the checks.

## 10. Stop rule

Continue only by:

- proving the absolute Airy correlation estimate; or
- constructing the iterated hook vanishing-cycle comparison and its explicit boundary complex.

Do not return to resonance coefficients, raw spectra, generic estimates, larger prime sweeps or surrogate invariants without a new formula directly targeting one of these statements.
