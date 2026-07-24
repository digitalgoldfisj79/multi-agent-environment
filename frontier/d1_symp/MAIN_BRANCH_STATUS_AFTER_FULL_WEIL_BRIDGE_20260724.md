# Authoritative d=1 main-branch status

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` sibling only. Integer Fortune is untouched.  
**Status:** supersedes every earlier status note on this branch.

## Route discipline

Only two branches remain admissible:

1. prove the absolute Airy Frobenius-correlation estimate;
2. isolate that Airy constituent and the explicit arithmetic boundaries inside the global `S_p`-equivariant Fourier--Cayley hook complex.

Coefficient resonance, bare-shift localization, generic complete-intersection bounds, common-factor collapse, slope pairing, local vanishing cycles at the smooth sparse zero section and unguided prime sweeps are closed or non-decisive.

## PROVED: geometric and cyclic reduction

For `p=5 mod 6`,

\[
T_p=p^2\operatorname{Tr}
\left(\sigma^{\pm1}F\mid H^{p-5}_{prim}(X_p)\right),
\]

where `X_p` is the smooth cyclic `(2,3)` complete intersection. Its primitive rank is

\[
\frac{2^{p-1}-1}{3}.
\]

The primitive cohomology is regular over the cyclic subgroup:

\[
H_p|_{C_p}\cong\mathbf Q_\ell[C_p]^{\oplus q_p},
\qquad
q_p=\frac{2^{p-1}-1}{3p}.
\]

For the affine normalizer,

\[
H_p\cong M_{0,p}\oplus(\rho_p\otimes M_{1,p}),
\qquad
\dim M_{0,p}=\dim M_{1,p}=q_p.
\]

With

\[
\mathcal D_p=M_{0,p}-M_{1,p},
\]

one has

\[
T_p=p^2\operatorname{Tr}(F|\mathcal D_p).
\]

## PROVED: full Airy--primitive virtual identity

Let

\[
\mathcal R_p=U_p-U_{p-2}(-1).
\]

Kummer averaging and relative degree-`p` Artin--Schreier descent prove, for every `r>=1`,

\[
\operatorname{Tr}(F^r|\mathcal R_p)
=p^{3r}\operatorname{Tr}(F^r|\mathcal D_p).
\]

Therefore, in the Grothendieck group of semisimple Weil representations,

\[
\boxed{\mathcal R_p^{ss}=\mathcal D_p(-3)^{ss}}.
\]

This closes the Airy-to-cyclic-linear-section comparison at every Frobenius power. It is a semisimple virtual identity, not a constructed quasi-isomorphism.

## PROVED: sparse hook geometry

For the general half-theorem primes `p>=11`,

\[
Y_p=\{s_2=s_3=\cdots=s_{p-4}=0\}\subset\mathbf P(H/L),
\qquad s_m=\sum_i x_i^m,
\]

is the ordered-root surface for

\[
Z^p+A Z^3+B Z^2+C Z+D.
\]

Its separable open is a free `S_p`-torsor. The virtual hook representation

\[
\Lambda_p=\sum_i(-1)^i\bigwedge^i\mathrm{Std}
\]

has character `p` on a `p`-cycle and zero otherwise, so the associated local system has trace exactly `p` times the irreducibility indicator.

The ambient Airy module is itself the alternating hook multiplicity

\[
\mathcal K_{ambient}
=\sum_i(-1)^i
\operatorname{Hom}_{S_p}
\left(\bigwedge^i\mathrm{Std},H_p\right),
\]

with

\[
\mathcal K_{ambient}^{ss}=\mathcal D_p^{ss},
\qquad
\mathcal R_p^{ss}=\mathcal K_{ambient}(-3)^{ss}.
\]

The prime `p=5` is exceptional and remains a separately proved base case.

## PROVED: Fourier--Cayley correction

The Jacobian of `s_1,...,s_m` is a truncated Vandermonde matrix and has full rank on the separable root locus. Local vanishing cycles at the sparse zero section therefore vanish on the locus carrying the irreducibility local system. That proposed mechanism is closed.

Put

\[
S=(s_4,\ldots,s_{p-4}),
\qquad c=p-7.
\]

Additive orthogonality gives

\[
\mathbf1_{S(x)=0}
=Q^{-c}\sum_{\lambda\in\mathbf F_Q^c}
\psi(\langle\lambda,S(x)\rangle).
\]

On the dual of

\[
\mathcal E=\bigoplus_{m=4}^{p-4}\mathcal O_{X_p}(m),
\]

the sheaf-theoretic identity is

\[
R\pi_!\mathcal L_\psi(\langle\lambda,S\rangle)
\cong i_!\mathbf Q_\ell(-c)[-2c].
\]

The correct application object is therefore the global Fourier--Cayley complex. Weight compatibility forces its desired pure constituent to be

\[
\mathcal K_{ambient}\left(\frac{p-7}{2}\right)
=\mathcal R_p\left(\frac{p-1}{2}\right).
\]

Isolation of this constituent remains open.

## PROVED: finite q-line assembly

For

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad A=\chi(a),
\]

every `c!=0` maps to

\[
q=-3/c,
\qquad \varepsilon=A\chi(q).
\]

For generic `q!=2`,

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

and

\[
B_A=I_A(\infty)+I_{A\chi(2)}(2).
\]

Then

\[
\boxed{
N_A(p)=(p-2)+B_A-\frac{S_0+A S_\chi}{2p}
}.
\]

The parity-protected crown certificate is that this number is not in

\[
2p\mathbf Z_{\ge0}
\]

for at least one sign `A`.

The finite arithmetic assembly is complete.

## OPEN: analytic theorem

Prove an absolute constant in

\[
|\operatorname{Tr}(F|\mathcal R_p)|\le C p^{(p+1)/2},
\]

or equivalently

\[
|\operatorname{Tr}(F|\mathcal D_p)|\le C p^{(p-5)/2}.
\]

## OPEN: application theorem

Inside the global Fourier--Cayley hook complex:

1. isolate

\[
\mathcal R_p\left(\frac{p-1}{2}\right);
\]

2. identify its invariant and quadratic arithmetic projectors with `S_0` and `S_\chi`;
3. identify complementary strata with exact signs and twists for the main/Tate/Artin--Schreier, discriminant/punctual, `q=2` and `q=\infty` terms;
4. apply the boxed q-line certificate.

## VERIFIED COMPUTATIONALLY

Structural regression checks cover:

- first-trace normalization at `p=5,11,17,23,29`;
- direct cyclic fixed points at `p=5`;
- exact third-power bridge consequences at `p=11,17,23,29`;
- the even `p=5,r=2` Kummer average over `F_25`;
- the primitive Betti formula through odd primes `p<=199`;
- split/nonsplit cells and q-line reconstruction at `p=5,7,11`.

## Stop rule

Continue only on the two open statements above. Do not return to resonance coefficients, local zero-section vanishing cycles, raw spectra, generic estimates, larger prime sweeps or surrogate invariants without a new formula directly targeting one of them.
