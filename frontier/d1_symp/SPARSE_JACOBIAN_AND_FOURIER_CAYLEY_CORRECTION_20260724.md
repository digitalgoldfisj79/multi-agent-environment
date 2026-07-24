# Sparse-section Jacobian audit and Fourier--Cayley correction

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** correction of the proposed application bridge for the function-field `d=1` programme.  
**Status:** the smoothness and Fourier identities below are **PROVED**. The earlier proposal to recover the load-bearing interior hook term from local iterated vanishing cycles at the sparse zero section is **CLOSED**.

## 0. Correction

For `p>=11`, the sparse ordered-root surface is

\[
Y_p=\{s_2=s_3=\cdots=s_{p-4}=0\}
\]

inside the ambient cyclic complete intersection

\[
X_p=\{s_2=s_3=0\}.
\]

The equations `s_4,...,s_{p-4}` cut `Y_p` transversely at every separable ordered-root point. Hence the local vanishing-cycle complexes of these sections vanish on the entire separable locus that carries the irreducibility hook local system.

Therefore the proposed identity

> the load-bearing interior hook module is the local iterated vanishing-cycle complex at the zero section

is false as a mechanism. The correct exact enforcement of all sparse equations is the global additive Fourier, or Cayley, transform of the power-sum map.

## 1. Vandermonde Jacobian

On affine ordered-root space, the Jacobian matrix of

\[
s_1,s_2,\ldots,s_m
\]

with respect to `x_1,...,x_p` is

\[
J_m=
\left(jx_i^{j-1}\right)_{
1\le j\le m,
1\le i\le p}.
\]

Since `m<p`, every scalar `j` is invertible. After dividing row `j` by `j`, this is the truncated Vandermonde matrix

\[
\left(x_i^{j-1}\right).
\]

If the tuple contains at least `m` distinct coordinate values, an `m by m` Vandermonde minor is nonzero. Thus

\[
\operatorname{rank}J_m=m.
\]

In particular, on the separable locus all `p` coordinates are distinct, so the equations

\[
s_1=s_2=\cdots=s_{p-4}=0
\]

form a transverse regular sequence.

After quotienting the free translation and projective scaling directions, the separable sparse root locus remains smooth of dimension two.

## 2. Consequence for local vanishing cycles

For each `m`, the section `s_m` on the previous nested locus is smooth along the separable part of its zero fibre. The local vanishing-cycle functor therefore vanishes there:

\[
\phi_{s_m}(\mathbf Q_\ell)=0
\]

on the separable zero section.

Iterating gives

\[
\phi_{s_{p-4}}\cdots\phi_{s_4}(\mathbf Q_\ell)=0
\]

on `Y_p^sep`.

Any nonzero local vanishing cycles are supported on the discriminant boundary where coordinates collide. They can contribute boundary corrections, but they cannot equal the load-bearing interior hook cohomology of `Y_p^sep`.

This does not refute a global Lefschetz-pencil or Fourier comparison. It refutes only the local-zero-fibre formulation.

## 3. Exact additive Fourier enforcement

Put

\[
c=p-7
\]

and collect the remaining power sums into

\[
S=(s_4,\ldots,s_{p-4}).
\]

On an affine chart where these are ordinary functions, introduce dual variables

\[
\lambda=(\lambda_4,\ldots,\lambda_{p-4})
\]

and the phase

\[
\langle\lambda,S(x)\rangle
=
\sum_{m=4}^{p-4}\lambda_m s_m(x).
\]

For every finite extension `k=F_Q`, additive orthogonality gives the exact pointwise identity

\[
\boxed{
\mathbf 1_{S(x)=0}
=
Q^{-c}
\sum_{\lambda\in k^c}
\psi_k(\langle\lambda,S(x)\rangle).
}
\]

Hence every alternating-hook point sum on the sparse surface is the zero-frequency Fourier coefficient of the corresponding hook-weighted exponential sum on the ambient root space.

This is the exact global mechanism by which `p-7` equations can change the relevant cohomological degree.

## 4. Sheaf-theoretic delta identity

Let

\[
\pi:Z\times\mathbf A^c_\lambda\longrightarrow Z
\]

and let `S:Z->A^c` be any realization of the power-sum map on an affine or vector-bundle chart. Then the fibre over `z` of

\[
R\pi_!\mathcal L_\psi(\langle\lambda,S(z)\rangle)
\]

is zero when `S(z)!=0`, while for `S(z)=0` it is

\[
R\Gamma_c(\mathbf A^c,\mathbf Q_\ell)
=
\mathbf Q_\ell(-c)[-2c].
\]

If `i:S^{-1}(0)->Z` is the zero-section inclusion, this gives the exact identity

\[
\boxed{
R\pi_!\mathcal L_\psi(\langle\lambda,S\rangle)
\cong
i_!\mathbf Q_\ell(-c)[-2c].
}
\]

Equivalently,

\[
\boxed{
i_!\mathbf Q_\ell
\cong
R\pi_!\mathcal L_\psi(\langle\lambda,S\rangle)(c)[2c].
}
\]

The construction is `S_p`-equivariant because every power sum is symmetric. Alternating hook extraction may therefore be applied before or after the Fourier integration.

## 5. Projective Cayley form

The functions `s_m` have different homogeneous degrees. Globally on `X_p`, regard them as sections of

\[
\mathcal E
=
\bigoplus_{m=4}^{p-4}\mathcal O_{X_p}(m).
\]

On the total space of the dual bundle `E^vee`, the canonical pairing with the section

\[
S\in H^0(X_p,\mathcal E)
\]

is a single global phase. The previous affine identity glues to the Fourier--Cayley transform on this vector bundle.

Thus the correct global application object is

\[
R\Gamma_c
\left(
\operatorname{Tot}(\mathcal E^\vee),
\mathcal L_\psi(\langle\lambda,S\rangle)
\otimes\mathcal L_{hook}
\right),
\]

with the separable/discriminant compactification and arithmetic class projectors attached.

## 6. Normalization

The exact delta identity contributes the Tate factor `(c)` and cohomological shift `[2c]` after integration over the `c` dual variables.

Independently, comparison of the pure ambient middle weight `p-5` with a pure surface middle weight `2` forces the net pure-term normalization

\[
\left(\frac c2\right)
=
\left(\frac{p-7}{2}\right).
\]

These are not contradictory statements. The Fourier phase space has `c` additional variables and carries `c` additional units of oscillatory weight; removing that oscillatory contribution and applying the delta normalization leaves the net half-codimension Tate shift on any pure ambient-to-surface constituent.

The existence of the required pure ambient constituent inside the Fourier--Cayley complex remains the open theorem.

## 7. Correct remaining application theorem

Let

\[
\mathcal K_{Fourier}
=
\sum_i(-1)^i
R\operatorname{Hom}_{S_p}
\left(
\bigwedge^i\mathrm{Std},
R\Gamma_c(\operatorname{Tot}(\mathcal E^\vee),
\mathcal L_\psi(\langle\lambda,S\rangle))
\right).
\]

The exact delta identity identifies its zero-frequency specialization with the sparse hook complex, after the displayed shifts and boundary restriction.

The main missing theorem is now:

> isolate inside `K_Fourier` the semisimple constituent `K_ambient((p-7)/2)` and prove that the complementary Fourier strata are exactly the invariant/quadratic q-line boundary complex appearing in `S_0`, `S_chi`, `q=2`, `q=infinity`, the discriminant and the punctual ledger.

Equivalently, on the Airy side the desired pure constituent is

\[
\mathcal R_p\left(\frac{p-1}{2}\right).
\]

## 8. What is closed and what remains

### PROVED

1. The sparse equations are transverse on the full separable root locus.
2. Local vanishing cycles at the sparse zero section vanish there.
3. The naïve local iterated-vanishing-cycle bridge cannot carry the interior hook term.
4. The global Fourier--Cayley delta identity enforces all sparse equations exactly and equivariantly.
5. The prior half-codimension Tate power is the only possible pure ambient-to-surface normalization.

### OPEN

1. Isolation of the ambient alternating-hook constituent in the Fourier--Cayley complex.
2. Decomposition of the complementary Fourier strata into the two q-line projectors and explicit boundaries.
3. The final parity certificate.
4. The separate absolute Airy trace bound.

The application branch remains live, but its correct mechanism is global Fourier transform, not local nearby cycles at a smooth section.
