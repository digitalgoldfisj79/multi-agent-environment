# Fourier--Cayley zero-frequency obstruction

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling, application main branch only.  
**Status:** the localization triangle, Tate normalization and absence statement below are **PROVED**. The open nonzero-frequency sector remains a theorem-level obstruction.

## 0. Correction to the previous formulation

Let

\[
X=X_p^{\mathrm{sep}},
\qquad
S=(s_4,\ldots,s_{p-4}),
\qquad
c=p-7,
\]

and let

\[
\mathcal E=\bigoplus_{m=4}^{p-4}\mathcal O_X(m).
\]

Write

\[
\pi:V=\operatorname{Tot}(\mathcal E^\vee)\longrightarrow X,
\]

let `z:X->V` be the zero section, and put

\[
j:V^\times=V\setminus z(X)\hookrightarrow V.
\]

On `V`, set

\[
\mathcal L=\mathcal L_\psi(\langle\lambda,S\rangle).
\]

The exact Fourier delta identity

\[
R\pi_!\mathcal L\cong i_!\mathbf Q_\ell(-c)[-2c],
\qquad i:Y=S^{-1}(0)\hookrightarrow X,
\]

enforces the sparse equations. It does **not** put the half-codimension twist of the ambient Airy module in the zero-frequency summand.

The canonical zero-frequency contribution carries the full twist `(c)`, not `(c/2)`.

## 1. Exact localization triangle

The open--closed decomposition of `V` gives

\[
j_!j^*\mathcal L\longrightarrow\mathcal L
\longrightarrow z_*\mathbf Q_\ell\overset{+1}{\longrightarrow}.
\]

Apply `R pi_!`. Since `pi o z=id_X` and the Fourier delta identity gives the middle term,

\[
R\pi_!j_!j^*\mathcal L
\longrightarrow
i_!\mathbf Q_\ell(-c)[-2c]
\longrightarrow
\mathbf Q_{\ell,X}
\overset{+1}{\longrightarrow}.
\]

Now apply compactly supported cohomology and the alternating hook projector. Define

\[
\mathcal K_\times
=
\operatorname{HookAlt}
R\Gamma_c(V^\times,j^*\mathcal L),
\]

\[
\mathcal K_Y
=
\operatorname{HookAlt}R\Gamma_c(Y,\mathbf Q_\ell),
\qquad
\mathcal K_X
=
\operatorname{HookAlt}R\Gamma_c(X,\mathbf Q_\ell).
\]

Then there is an exact distinguished triangle

\[
\boxed{
\mathcal K_\times
\longrightarrow
\mathcal K_Y(-c)[-2c]
\longrightarrow
\mathcal K_X
\overset{+1}{\longrightarrow}.
}
\]

Equivalently,

\[
\boxed{
\mathcal K_\times(c)[2c]
\longrightarrow
\mathcal K_Y
\longrightarrow
\mathcal K_X(c)[2c]
\overset{+1}{\longrightarrow}.
}
\]

In the Grothendieck group, the even shift disappears and

\[
\boxed{
[\mathcal K_Y]
=
[\mathcal K_\times(c)]
+
[\mathcal K_X(c)].
}
\]

This is the canonical Fourier--Cayley decomposition attached to zero versus nonzero dual frequency.

## 2. The zero-frequency Tate power is forced

The pointwise orthogonality formula is

\[
\mathbf 1_{S(x)=0}
=Q^{-c}\sum_{\lambda\in\mathbf F_Q^c}
\psi(\langle\lambda,S(x)\rangle).
\]

The term `lambda=0` is therefore multiplied by `Q^{-c}`. In the repository convention, this is the Tate twist `(c)`. The sheaf localization triangle gives the same normalization exactly.

Consequently, the primitive ambient hook module contributes from the zero section as

\[
\boxed{
\mathcal K_{\mathrm{ambient}}(c)
=
\mathcal K_{\mathrm{ambient}}(p-7),
}
\]

not as

\[
\mathcal K_{\mathrm{ambient}}(c/2).
\]

## 3. PROVED absence of the proposed Airy constituent at zero frequency

The ambient primitive hook module has pure weight

\[
p-5.
\]

Its canonical zero-frequency twist has weight

\[
(p-5)-2(p-7)=9-p.
\]

The previously proposed load-bearing surface normalization

\[
\mathcal K_{\mathrm{ambient}}
\left(\frac{p-7}{2}\right)
=
\mathcal R_p\left(\frac{p-1}{2}\right)
\]

has weight two.

For every general half-theorem prime `p>=11`,

\[
9-p\ne2.
\]

Pure semisimple Weil representations of distinct weights have no common constituent. Therefore

\[
\boxed{
\mathcal K_{\mathrm{ambient}}
\left(\frac{p-7}{2}\right)
\text{ is absent from the canonical zero-frequency summand.}
}
\]

Equivalently,

\[
\boxed{
\mathcal R_p\left(\frac{p-1}{2}\right)
\text{ cannot be obtained from }\lambda=0
\text{ by the Fourier delta identity.}
}
\]

This is an absence theorem for the proposed constituent in the only canonical zero-frequency term. It does not assert that the same Weil representation cannot occur noncanonically elsewhere in the total Fourier complex.

## 4. The only remaining location is the open nonzero-frequency sector

The exact triangle shows that any weight-two copy of

\[
\mathcal K_{\mathrm{ambient}}
\left(\frac{p-7}{2}\right)
\]

inside the sparse hook complex must come from

\[
\mathcal K_\times(c),
\]

the compactly supported Fourier cohomology over `V^times`.

This is not a finite boundary correction. The dual bundle has rank

\[
c=p-7>=4
\]

for `p>=11`; its nonzero projectivized frequency space has positive dimension. The phase

\[
\sum_{m=4}^{p-4}\lambda_m s_m
\]

therefore defines a genuine family of oscillatory root problems. Whether alternating hook extraction cancels its generic part is not decided by the delta identity.

The remaining application theorem is now precise:

> Prove a global stationary-phase, Fourier-support or cancellation theorem for the alternating hook transform on `V^times` that isolates the weight-two Airy constituent and identifies every other surviving stratum with the invariant/quadratic q-line and explicit boundary ledger.

Without that theorem, the Fourier--Cayley transform is an exact reformulation of the sparse restriction, not a transport theorem from the ambient Airy trace to irreducibility.

## 5. Consequence for the programme

### PROVED

1. The zero/nonzero-frequency localization triangle.
2. The full-codimension twist `(p-7)` on the canonical zero-frequency contribution.
3. The half-codimension Airy constituent is absent from that contribution by weights.
4. Any successful Fourier--Cayley application proof must arise from the open nonzero-frequency sector.

### THEOREM-LEVEL OBSTRUCTION

The application branch is no longer missing bookkeeping or a choice of boundary signs. It requires a new global theorem controlling the alternating-hook Fourier transform over a positive-dimensional nonzero-frequency parameter space.

The finite terms `q=2`, `q=infinity`, discriminant and punctual strata remain necessary, but they cannot by themselves manufacture the absent half-twist from the zero-frequency term.

### NOT PROVED

- that the desired Airy constituent actually occurs in `K_times`;
- that it is absent from the entire Fourier complex;
- the final crown.

The canonical zero-frequency route is rigorously closed. The open-sector theorem is the exact remaining application wall.