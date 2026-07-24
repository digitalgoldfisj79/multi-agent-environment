# Main-branch status after the full Airy--primitive Weil bridge

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only. Integer Fortune remains untouched.  
**Status:** this file supersedes the two earlier main-branch status notes on this branch.

## 1. Route discipline

Only two branches remain admissible:

1. the absolute Frobenius-correlation estimate;
2. transport of that virtual object into the post-pushforward hook/irreducibility ledger.

The coefficient-resonance, bare-shift localization, generic complete-intersection, common-factor, slope-pairing and prime-sweep routes remain closed or non-decisive.

## 2. PROVED: exact geometric reduction

For `p=5 mod 6`, the cubic trace sum satisfies

\[
T_p
=
p^2\operatorname{Tr}
\left(
\sigma^{\pm1}F
\mid H^{p-5}_{prim}(X_p^{perm})
\right),
\]

where `X_p^perm` is the smooth cyclic `(2,3)` complete intersection.

Its primitive rank is

\[
\frac{2^{p-1}-1}{3}.
\]

## 3. PROVED: cyclic regularity and two equal multiplicity spaces

As a representation of the cyclic `p`-subgroup,

\[
H_p|_{C_p}
\cong
\mathbf Q_\ell[C_p]^{\oplus q_p},
\qquad
q_p=\frac{2^{p-1}-1}{3p}.
\]

For the affine normalizer `N_p=C_p\rtimes F_p^*`,

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

Thus the exponential primitive trace is exactly a rank-zero difference of two equal-rank Frobenius multiplicity spaces.

## 4. PROVED: full virtual Weil identity with the Airy boundary pair

Let

\[
\mathcal R_p
=
U_p-U_{p-2}(-1),
\]

where `U_k` is the `mu_3`-invariant cubic-Airy cohomology.

Kummer averaging over cubic coefficient twists and the relative degree-`p` Artin--Schreier descent prove, for every `r>=1`,

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

in the Grothendieck group of semisimple Weil representations, and

\[
\frac{\det(1-TF|U_p)}
     {\det(1-TF|U_{p-2}(-1))}
=
\frac{\det(1-p^3TF|M_{0,p})}
     {\det(1-p^3TF|M_{1,p})}.
\]

This closes the Airy-to-cyclic-linear-section comparison at the full Frobenius-character level. It is stronger than equality of the first or odd power traces. It is a semisimple virtual identity, not a constructed quasi-isomorphism of complexes.

## 5. Corrections resolved by the full bridge

### Even powers

A single cubic coefficient does not project to the `mu_3`-invariant sector in even degree. Averaging the three Kummer coefficient twists is exactly the invariant projector.

### Degrees divisible by `p`

The Airy moment uses a fresh relative degree-`p` extension over each `F_{p^r}`. It is not the base change of one fixed Artin--Schreier form. The relative twist retains the nontrivial cyclic descent when `p|r` and gives the same multiplicity difference `D_p`.

These distinctions close the two omissions in the earlier odd-extension bridge.

## 6. OPEN: analytic main theorem

The required estimate remains

\[
|\operatorname{Tr}(F|\mathcal R_p)|
\le C p^{(p+1)/2},
\]

or equivalently

\[
|\operatorname{Tr}(F|\mathcal D_p)|
\le C p^{(p-5)/2}.
\]

The virtual identity explains the exact exponential cancellation from the full primitive motive to the small Airy pair. It does not prove the absolute constant governing the remaining difference between `U_p` and `U_{p-2}(-1)`.

A valid continuation must construct a Frobenius correlation, bounded-trace cone or direct uniform trace theorem for this pair.

## 7. OPEN: application main theorem

The remaining application problem is now strictly the Airy/hook comparison. It must identify the semisimple virtual module above with the load-bearing post-pushforward even--odd hook constituent and explicitly assemble:

1. the main, Tate and excluded Artin--Schreier lines;
2. the punctual/nearby-cycle transport;
3. the arithmetic quadratic twist at infinity;
4. the `q=2` boundary cell;
5. the `q=infinity` boundary cell;
6. the final parity-protected irreducibility certificate.

The earlier claim that an Airy-to-linear-section bridge was missing is superseded. The hook/nearby-cycle comparison remains theorem-hard and is not supplied by the present virtual identity.

## 8. Verification status

### VERIFIED COMPUTATIONALLY

- first-trace normalization at `p=5,11,17,23,29`;
- direct `p=5` cyclic fixed-point and regular-character model;
- exact `r=3` divisibility consequences at `p=11,17,23,29`;
- complete `p=5,r=2` three-Kummer-twist average over `F_25`;
- primitive Betti formula through odd primes `p<=199`.

These checks test concrete consequences. The all-degree Weil identity is proved symbolically and does not rest on extrapolation from the checks.

## 9. Stop rule

Continue only by:

- proving the absolute Airy correlation estimate; or
- constructing the exact Airy-to-hook virtual comparison and boundary ledger.

Do not return to resonance coefficients, raw spectra, generic estimates, larger prime sweeps or surrogate invariants without a new structural formula directly targeting one of these two statements.
