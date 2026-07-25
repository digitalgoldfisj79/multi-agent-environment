# Odd-extension bridge from the cyclic primitive motive to the Airy virtual module

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling, primes `p=5 mod 6`.  
**Status:** the trace identities below are **PROVED**. They give an exact bridge on every extension degree coprime to `2p`. A full equality of Weil modules is **NOT PROVED** because the even-power and `p`-divisible sectors remain different.

## 0. The two virtual objects

Let

\[
H_p=H^{p-5}_{\mathrm{prim}}(X_p^{\mathrm{perm}},\mathbf Q_\ell)
\]

and use the normalizer decomposition proved in
`CYCLIC_REGULARITY_AND_TWO_BLOCK_REDUCTION_20260724.md`:

\[
H_p\cong M_{0,p}\oplus(\rho_p\otimes M_{1,p}).
\]

Define the rank-zero primitive multiplicity difference

\[
\mathcal D_p=M_{0,p}-M_{1,p}.
\]

On the Airy side, let

\[
U_k=H_c^1
(\mathbf A^1_{\overline{\mathbf F}_p},\operatorname{Sym}^k\mathcal A)^{\mu_3}
\]

and define the common-weight virtual module

\[
\mathcal R_p
=
U_p-U_{p-2}(-1).
\]

The Tate twist is normalized so that geometric Frobenius on `(-1)` is multiplied by `p`. Thus both terms in `R_p` have weight `p+1`.

## 1. Extension-field cubic sum

For `r>=1`, put

\[
Q=p^r,
\qquad
k_r=\mathbf F_Q,
\qquad
L_r=\mathbf F_{Q^p}.
\]

Let

\[
\psi_r=\psi\circ\operatorname{Tr}_{k_r/\mathbf F_p}
\]

and define

\[
T_{p,r}
=
\sum_{x\in L_r,\ \operatorname{Tr}_{L_r/k_r}(x)=0}
\psi_r\left(\operatorname{Tr}_{L_r/k_r}(x^3)\right).
\]

For `r=1`, this is the committed sum `T_p`.

## 2. PROVED: Airy trace extraction for every odd `r`

Let the local inverse roots of the cubic Airy sheaf at `u in k_r` be `alpha_u,beta_u`, with determinant `Q`. The rank-two Adams identity gives

\[
\alpha_u^p+\beta_u^p
=
\operatorname{Tr}(\operatorname{Sym}^p)
-Q\operatorname{Tr}(\operatorname{Sym}^{p-2}).
\]

Additive orthogonality over `u in k_r` gives

\[
Q T_{p,r}
=
\sum_{u\in k_r}
D_p(t_u,Q),
\]

with the sign convention frozen in
`AIRY_ODD_POWER_SPECTRA_AUDIT_20260723.md`.

For odd `r`, arithmetic Frobenius interchanges the two nontrivial `mu_3` character sectors, so their traces vanish. The ordinary complete Airy sum therefore extracts the invariant summands exactly. Grothendieck--Lefschetz then yields

\[
\boxed{
\operatorname{Tr}(F^r\mid\mathcal R_p)
=Q T_{p,r}
\qquad(r\text{ odd}).
}
\]

For `r=1`, this is the existing identity

\[
pT_p
=
\operatorname{Tr}(F\mid U_p)
-p\operatorname{Tr}(F\mid U_{p-2}).
\]

## 3. PROVED: the trace-form variety over coprime extensions

Let

\[
K=\mathbf F_{p^p}.
\]

The Artin--Schreier form `X_p^AS` is built from the finite etale algebra `K/F_p`. After extension to `k_r`,

\[
K\otimes_{\mathbf F_p}k_r
\]

is a field exactly when `p` does not divide `r`; in that case it is canonically isomorphic, as a `k_r`-algebra, to `L_r=F_{Q^p}`.

Assume now

\[
\gcd(r,2p)=1.
\]

Then `r` is odd, `p` does not divide `r`, and

\[
Q=p^r=2\pmod3.
\]

Hence cubing is a bijection of `k_r^*`. The affine-fibre argument from the twisted-descent theorem applies verbatim with `p` replaced by the base-field cardinality `Q` while the geometric dimension remains `p-5`. It gives

\[
\boxed{
\#X_p^{AS}(k_r)
-
\#\mathbf P^{p-5}(k_r)
=
\frac{T_{p,r}}{Q^2}.
}
\]

By the trace formula and twisted descent,

\[
\frac{T_{p,r}}{Q^2}
=
\operatorname{Tr}
\left(
\sigma^{\pm r}F^r
\mid H_p
\right).
\]

Because `p` does not divide `r`, `sigma^r` is nontrivial. The exact two-block reduction therefore gives

\[
\boxed{
T_{p,r}
=Q^2\operatorname{Tr}(F^r\mid\mathcal D_p)
\qquad(\gcd(r,2p)=1).
}
\]

## 4. The exact Airy--primitive bridge

Combining the two proved identities,

\[
\operatorname{Tr}(F^r\mid\mathcal R_p)
=Q T_{p,r}
=Q^3\operatorname{Tr}(F^r\mid\mathcal D_p)
\]

for every `r` coprime to `2p`.

Since a `(-3)` Tate twist multiplies geometric `F^r` traces by `Q^3`, one obtains

\[
\boxed{
\operatorname{Tr}(F^r\mid\mathcal R_p)
=
\operatorname{Tr}(F^r\mid\mathcal D_p(-3))
\qquad(\gcd(r,2p)=1).
}
\]

This is the first exact trace-level comparison between the cyclic primitive motive and the cross-symmetric-power Airy virtual module beyond the first Frobenius trace.

In particular, at `r=1`,

\[
\boxed{
\operatorname{Tr}(F\mid\mathcal R_p)
=p^3\operatorname{Tr}(F\mid\mathcal D_p).
}
\]

Therefore the Airy estimate and the primitive two-block estimate are not merely numerically equivalent: their Frobenius traces agree after the exact Tate normalization on every extension degree coprime to `2p`.

## 5. Precise remaining discrepancy

Define

\[
\mathcal E_p
=
\mathcal R_p-\mathcal D_p(-3).
\]

Then

\[
\boxed{
\operatorname{Tr}(F^r\mid\mathcal E_p)=0
\qquad(\gcd(r,2p)=1).
}
\]

Equivalently, the logarithmic Frobenius series

\[
\sum_{r\ge1}
\operatorname{Tr}(F^r\mid\mathcal E_p)\frac{T^r}{r}
\]

has no terms in degrees coprime to `2p`.

There are two exact reasons the proof does not cover the missing powers.

### Even `r`

When `r` is even,

\[
p^r=1\pmod3.
\]

Cubing on the base field has three nonzero residue classes, and ordinary Airy sums no longer isolate the `mu_3`-invariant sector without twisted projectors. This is the already identified even-power/projector defect and is where the arithmetic quadratic-twist ambiguity enters.

### `p` divides `r`

When `p|r`,

\[
K\otimes_{F_p}F_{p^r}
\]

splits into `p` factors rather than remaining the degree-`p` field. The descent cocycle untwists because

\[
(\sigma F)^r=F^r.
\]

The trace then sees the full exponentially large primitive cohomology rather than the cyclic difference `D_p`.

Thus the omitted powers are not a technical gap in the calculation. They are exactly the two structural sectors already known to obstruct a naive global isomorphism.

## 6. Consequence for the application branch

The application bridge can now be stated specifically.

The Airy virtual module `R_p` and the Tate-shifted primitive multiplicity difference `D_p(-3)` have identical Frobenius characters on every degree coprime to `2p`. Any full object-level comparison must therefore account only for a correction `E_p` invisible on those degrees.

A valid completion must determine the even and `p`-divisible local factors and show that their correction is precisely absorbed by the already listed application terms:

- the arithmetic quadratic twist;
- the `q=2` boundary cell;
- the `q=infinity` cell;
- the Artin--Schreier/main/Tate terms;
- the endpoint/punctual contribution.

This is narrower than constructing an unrestricted correspondence from the full primitive cohomology to the hook complex.

## 7. Exact computational checks

`odd_extension_bridge_verify.py` checks the two available coprime odd powers:

- `r=1`, using the committed exact `T_p` and separated first Airy traces;
- `r=3`, using the independently certified third Airy traces.

For `p=11,17,23,29`, it verifies

\[
\operatorname{Tr}(F\mid\mathcal R_p)
=p^3(T_p/p^2)
\]

and the new divisibility

\[
\boxed{
p^9\mid
\left[
\operatorname{Tr}(F^3\mid U_p)
-p^3\operatorname{Tr}(F^3\mid U_{p-2})
\right].
}
\]

The quotients are the predicted integral third traces of `D_p`.

These checks certify the arithmetic consequences at the calibrated primes. The all-`r` identity is proved symbolically above.
