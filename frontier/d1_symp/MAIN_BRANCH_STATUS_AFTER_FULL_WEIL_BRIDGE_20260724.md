# Authoritative d=1 main-branch status

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` sibling only. Integer Fortune is untouched.  
**Status:** supersedes every earlier status note on this branch.

## 1. Termination criterion reached

The autonomous continuation was required to stop only at one of:

1. a proof of the crown;
2. rigorous absence of the proposed constituent;
3. a precise theorem-level obstruction.

The crown is not proved. The other two conditions have now been reached:

- **application branch:** the proposed half-codimension Airy constituent is rigorously absent from the canonical zero-frequency Fourier--Cayley summand;
- **analytic branch:** arithmetic Picard--Lefschetz theory reduces all local characteristic-boundary correction to one explicit Tate line, leaving a precisely isolated global Frobenius-correlation theorem between Hodge-disjoint motives.

No further finite computation or bookkeeping closes either wall.

## 2. PROVED: geometric and cyclic reduction

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

## 3. PROVED: full Airy--primitive virtual identity

Let

\[
\mathcal R_p=U_p-U_{p-2}(-1).
\]

For every `r>=1`, Kummer averaging and relative degree-`p` Artin--Schreier descent prove

\[
\operatorname{Tr}(F^r|\mathcal R_p)
=p^{3r}\operatorname{Tr}(F^r|\mathcal D_p).
\]

Therefore

\[
\boxed{\mathcal R_p^{ss}=\mathcal D_p(-3)^{ss}}
\]

in the Grothendieck group of semisimple Weil representations. This closes the Airy-to-cyclic-linear-section bridge at every Frobenius power.

## 4. PROVED: sparse hook geometry and finite arithmetic ledger

For the general half-theorem primes `p>=11`,

\[
Y_p=\{s_2=s_3=\cdots=s_{p-4}=0\}\subset\mathbf P(H/L)
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

The ambient Airy module is the alternating hook multiplicity

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

For

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad A=\chi(a),
\]

every `c!=0` maps to

\[
q=-3/c,
\qquad
\varepsilon=A\chi(q).
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
N_A(p)=(p-2)+B_A-\frac{S_0+A S_\chi}{2p}.
}
\]

The parity-protected crown certificate is that this number is not in

\[
2p\mathbf Z_{\ge0}
\]

for at least one sign `A`. The finite arithmetic assembly is complete.

## 5. PROVED: Fourier--Cayley zero-frequency absence

Put

\[
S=(s_4,\ldots,s_{p-4}),
\qquad c=p-7,
\]

and let `V=Tot(E^vee)` with zero section `z` and nonzero-frequency open `V^times`.

The Fourier delta identity is

\[
R\pi_!\mathcal L_\psi(\langle\lambda,S\rangle)
\cong i_!\mathbf Q_\ell(-c)[-2c].
\]

The zero/nonzero-frequency localization triangle gives, after compact support and alternating hook extraction,

\[
\mathcal K_\times(c)[2c]
\longrightarrow
\mathcal K_Y
\longrightarrow
\mathcal K_X(c)[2c]
\overset{+1}{\longrightarrow}.
\]

Thus the canonical zero-frequency ambient contribution is

\[
\boxed{\mathcal K_{ambient}(p-7),}
\]

not

\[
\mathcal K_{ambient}\left(\frac{p-7}{2}\right).
\]

The first has weight `9-p`; the proposed load-bearing half-twist has weight two. For every `p>=11`, they have distinct weights and no common pure semisimple constituent.

Therefore

\[
\boxed{
\mathcal R_p\left(\frac{p-1}{2}\right)
\text{ is absent from the canonical zero-frequency summand.}
}
\]

If it occurs in the sparse hook complex, it must arise from the positive-dimensional nonzero-frequency sector. Proving that requires a new global stationary-phase, Fourier-support or hook-cancellation theorem.

The exact calibration at `p=11,17,23,29` independently falsifies the simplest formula identifying either `S_0` or `S_chi` with the normalized Airy trace modulo only `q=2` and `q=infinity`.

## 6. PROVED: boundary discriminant theorem

For `p=5 mod 6`,

\[
\boxed{I_+(\infty)=0.}
\]

Indeed, for

\[
f(X)=X^p+aX^3+d
\]

with `chi(a)=+1`, the discriminant square class is

\[
\chi\left((-1)^{(p-1)/2}3a\right)=-1,
\]

whereas an irreducible degree-`p` polynomial has square discriminant because a `p`-cycle is even.

For the split `q=2` cell,

\[
\chi(2)=+1
\quad\Longrightarrow\quad
I_+(2)=0.
\]

The remaining finite boundary values are exact and small, but do not account for the generic Fourier discrepancy.

## 7. EXTERNAL THEOREM APPLIED: exact Airy local correction

Chuang's 2026 arithmetic Picard--Lefschetz theorem gives the `mu_3`-invariant Airy model `A'_k` and, for odd `k=2m+1`, a split correction by one Tate line for every odd integer `a` in `1<=a<=k/p`.

At the characteristic boundary:

\[
\boxed{
U_p^{gen}
\cong
U_p^{sp}
\oplus
\mathbf Q_\ell\left(-\frac{p+1}{2}\right),
}
\]

whereas

\[
\boxed{U_{p-2}^{gen}\cong U_{p-2}^{sp}.}
\]

Consequently,

\[
\operatorname{Tr}(F|U_p^{sp})
-p\operatorname{Tr}(F|U_{p-2}^{sp})
=
\operatorname{Tr}(F|U_p^{gen})
-p\operatorname{Tr}(F|U_{p-2}^{gen})
-p^{(p+1)/2}.
\]

The entire local correction is one explicit eigenvalue already on the allowed scale. There is no hidden growing local vanishing-cycle term that can supply the missing cancellation.

The common-weight characteristic-zero Hodge spectra of

\[
U_p^{gen}
\quad\text{and}\quad
U_{p-2}^{gen}(-1)
\]

are disjoint, so no characteristic-zero algebraic correspondence can pair them. The remaining analytic theorem is therefore a genuinely characteristic-`p`, Frobenius-dependent numerical correlation.

## 8. Exact terminal frontier

### Analytic theorem-level obstruction

Prove

\[
\left|
\operatorname{Tr}(F|U_p^{gen})
-p\operatorname{Tr}(F|U_{p-2}^{gen})
\right|
\le C' p^{(p+1)/2}
\]

for an absolute `C'`, between equal-weight, linearly growing, Hodge-disjoint motives. Local Picard--Lefschetz theory supplies only the explicit Tate line and no cross-motive correlation.

### Application theorem-level obstruction

On the nonzero-frequency Fourier bundle `V^times`, prove that alternating hook extraction produces the required weight-two Airy constituent and that every other surviving stratum is exactly the invariant/quadratic q-line and explicit boundary complex.

The constituent is absent from the canonical zero-frequency term. The open sector has positive-dimensional frequency space and cannot be reduced to finite boundary bookkeeping by the Fourier delta identity.

## 9. Verification

Structural regression checks cover:

- first-trace normalization at `p=5,11,17,23,29`;
- direct cyclic fixed points at `p=5`;
- exact third-power bridge consequences at `p=11,17,23,29`;
- the even `p=5,r=2` Kummer average over `F_25`;
- primitive Betti ranks through odd primes `p<=199`;
- split/nonsplit cells and q-line reconstruction at `p=5,7,11`;
- exact boundary/projector calibration at `p=11,17,23,29`.

## 10. Ruling

### PROVED

- every reduction and virtual identity above;
- absence of the proposed constituent from the canonical zero-frequency Fourier summand;
- the boundary discriminant vanishing;
- the explicit one-line Airy Picard--Lefschetz correction.

### NOT PROVED

- that the Airy constituent occurs in the nonzero-frequency sector;
- the absolute Airy correlation;
- the crown.

### STOP CONDITION

Both admitted branches have reached precise theorem-level obstructions, and the proposed canonical zero-frequency constituent is rigorously absent. Further autonomous algebraic manipulation of the present decompositions would only restate one of these two new global theorems.

Resume only with a genuinely new stationary-phase/hook Fourier theorem or a genuinely new characteristic-`p` Frobenius-correlation theorem. Do not return to resonance coefficients, local zero-section vanishing cycles, raw spectra, generic estimates, larger prime sweeps or surrogate invariants.