# Main d=1 status after the Pascal--oscillator reduction

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only. Papers V and VI remain frozen.

## Ruling

The function-field crown remains open.

The earlier claim that the canonical relative configuration-space calculation closed Route B has been retracted. That calculation rejects only the pre-pushforward deletion/Koszul candidate.

The corrected configuration/Fourier programme has nevertheless advanced materially. The wild-infinity open sector is no longer an unspecified positive-dimensional Fourier complex. Its complete linear symplectic data are now explicit:

- the sparse frequency quotient is one regular symplectic Jordan block of dimension `p-7`;
- the Laurent/Pascal coefficient--normal map is an exact anti-symplectic isomorphism;
- its graph is a canonical Lagrangian correspondence;
- the cubic-origin affine and projective normalizations are completely calibrated;
- a compatible oscillator model has exactly the required half-codimension Tate size.

The remaining application theorem is one nonlinear nearby-cycle realization statement, written precisely below.

The separate archimedean Airy or q-line terminal estimate remains open.

## 1. Authoritative correction to the face-complex result

Read:

`frontier/d1_push/CONFIGURATION_FACE_COMPLEX_SCOPE_CORRECTION_20260725.md`.

The following remain valid:

1. the canonical ordered-configuration deletion complex is the exact augmentation Koszul complex;
2. its Euler class is zero, not the hook detector;
3. it fails the weight-zero, `p=5`, and `p=7` regressions;
4. the signed middle virtual rank is
   \[
   p-3-2\left\lfloor\frac{p-1}{4}\right\rfloor.
   \]

The following are withdrawn:

- closure of post-parabolic configuration complexes;
- closure of global `(q,t)` or Fourier--Cayley cancellation;
- any claim that the actual semisimplified middle rank was determined;
- the assertion that stopping condition 4 had been reached.

The stale status file has been replaced by a superseded notice.

## 2. Exact affine cubic-origin decomposition

Read:

- `AFFINE_CUBIC_ORIGIN_AIRY_DECOMPOSITION_20260725.md`;
- `affine_cubic_origin_decomposition_verify.py`.

For `q=p^r`, the affine cubic-origin Smith-defect trace is

\[
\boxed{
h_{p,r}(0)
=q^{p-3}-q
+q(q-1)\operatorname{Tr}(F^r\mid\mathcal D_p).
}
\]

Equivalently,

\[
\boxed{
h_{p,r}(0)
=q^{p-3}-q
+\frac{q-1}{q^2}
\operatorname{Tr}(F^r\mid\mathcal R_p).
}
\]

Thus

\[
\boxed{
\mathcal H_{p,0}^{ss}
=
\mathbf Q_\ell(-(p-3))
-
\mathbf Q_\ell(-1)
+
\mathcal D_p(-2)
-
\mathcal D_p(-1).
}
\]

There is no unidentified transcendental family at the cubic origin.

The verifier independently enumerates `F_(5^5)`, obtaining

\[
\#\{\operatorname{Tr}\alpha=\operatorname{Tr}\alpha^2=\operatorname{Tr}\alpha^3=0\}=25,
\qquad h_{5,1}(0)=20,
\qquad T_5=0.
\]

## 3. Exact affine-group quotient calibration

Read:

`AFFINE_GROUP_TORSOR_CALIBRATION_OF_AIRY_ORIGIN_20260725.md`.

The group

\[
\operatorname{Aff}_1(\mathbf F_q)
\]

acts freely on the degree-`p` trace-constraint locus. Every orbit has size `q(q-1)`, and the quotient is the cyclic relative projective ambient complete-intersection object. Therefore

\[
\boxed{
\frac{h_{p,r}(0)}{q(q-1)}
=
1+q+\cdots+q^{p-5}
+
\operatorname{Tr}(F^r\mid\mathcal D_p).
}
\]

The affine object factors as

\[
\boxed{
\mathcal H_{p,0}^{ss}
=
R\Gamma_c(\mathbf A^1\times\mathbf G_m)
\otimes
\left(
\bigoplus_{j=0}^{p-5}\mathbf Q_\ell(-j)
\oplus\mathcal D_p
\right).
}
\]

Translation and scaling at the cubic origin are therefore closed bookkeeping.

## 4. Canonical symplectic sparse-frequency geometry

Read:

- `SPARSE_FREQUENCY_SYMPLECTIC_POLARIZATION_20260725.md`;
- `SPARSE_FREQUENCY_SYMPLECTIC_JORDAN_THEOREM_20260725.md`;
- `WILD_INFINITY_RESIDUE_FORM_IDENTIFICATION_20260725.md`;
- `sparse_frequency_symplectic_verify.py`;
- `sparse_frequency_jordan_verify.py`.

The sparse coefficient quotient is

\[
\mathcal V_p
=k[T]_{\le p-4}/k[T]_{\le3},
\qquad
\dim\mathcal V_p=p-7=2m.
\]

It carries the nondegenerate alternating form

\[
\boxed{
\omega_p([f],[g])
=[T^{p-1}](f'g-fg').
}

On monomials,

\[
\omega_p(T^a,T^b)
=(a-b)\mathbf1_{a+b=p}.
\]

At root infinity, with `z=T^(-1)`, this is exactly

\[
\boxed{
\omega_p(f,g)
=
\operatorname{Res}_{z=0}
 z^p(F\,dG-G\,dF).
}
\]

Translation acts by one regular nilpotent block `J_(p-7)`, and

\[
\mathcal L_p
=
\ker D^m
=
\operatorname{span}
\{T^4,\ldots,T^{(p-1)/2}\}
\]

is a canonical affine-invariant Lagrangian. The affine-conformal alternating form is unique up to scalar.

## 5. Exact anti-symplectic Pascal theorem

Read:

- `PASCAL_SPARSE_BLOCK_ANTI_SYMPLECTIC_THEOREM_20260725.md`;
- `pascal_sparse_antisymplectic_verify.py`.

For

\[
H=\{4,\ldots,p-4\},
\]

the Laurent expansion has matrix

\[
D_{j,m}
=(-1)^j\binom{m+j-1}{j}.
\]

Let

\[
W_{a,b}=(a-b)\mathbf1_{a+b=p}.
\]

A binomial/hockey-stick calculation proves

\[
\boxed{D^tWD=-W.}
\]

Thus the actual high Pascal coefficient--normal map is anti-symplectic, and its graph

\[
\Gamma_D
\subset
(\mathcal V_p\oplus\mathcal V_p,
\omega_p\oplus\omega_p)
\]

is Lagrangian.

## 6. Compatible oscillator model and its limitation

Read:

- `CANONICAL_QUADRATIC_OSCILLATOR_ON_SPARSE_FREQUENCIES_20260725.md`;
- `canonical_quadratic_oscillator_verify.py`;
- `GEOMETRIC_WEIL_KERNEL_APPLICABILITY_AUDIT_20260725.md`.

Degree reversal supplies one explicit anti-symplectic polarization and the nondegenerate model

\[
Q_p=
\sum_{a=4}^{p-4}a x_a^2.
\]

For every `q=p^r`,

\[
\boxed{
\sum_{v\in\mathcal V_p(\mathbf F_q)}
\psi_q(Q_p(v))
=q^{(p-7)/2}.
}
\]

The punctured model has virtual class

\[
\mathbf Q_\ell(-(p-7)/2)-\mathbf Q_\ell,
\]

and therefore its Airy tensor has the formally required class

\[
\boxed{
\mathcal D_p(-(p-7)/2)-\mathcal D_p.
}
\]

However, the actual Pascal map is `D`, not degree reversal. The branch has **not** proved that the wild Smith-defect phase is right-equivalent to the displayed quadratic form. This is an exactly evaluated compatible model, not the identification theorem.

Published geometric Weil theory supplies the canonical oscillator kernel and its normalization once the wild nearby-cycle complex is realized as the Lagrangian kernel attached to `Gamma_D`. It does not prove that realization.

## 7. Exact independent p=11 q-line verification

Read:

- `Q_LINE_P11_R3_INDEPENDENT_VERIFICATION_20260725.md`;
- `qline_p11_r3_parallel_verify.py`.

A fresh CPU-XL calculation factored all

\[
(11^3-2)11^3=1,769,899
\]

generic `(q,t)` cells. It returned

\[
\boxed{
\sum_q I_3(q)=161446,
\qquad
S_3=-7007.
}
\]

Under the standard assumption that the algebraic cubic-power contribution is an integral multiple of `11^3`, the nearest algebraic value leaves residual `-352`, forcing a pure weight-one rank at least `10`. This is a conditional lower bound, not a proof of growth with `p`.

## 8. Exact remaining application lemma

Put

\[
m=\frac{p-7}{2}.
\]

The Fourier localization triangle gives

\[
[\mathcal K_Y]
=[\mathcal K_\times(p-7)]
+[\mathcal K_X(p-7)].
\]

The ambient primitive Airy block in `K_X` is `D_p`. To obtain

\[
\mathcal D_p(m)
=
\mathcal R_p\left(\frac{p-1}{2}\right),
\]

the open sector must contribute exactly

\[
\boxed{
[\mathcal K_\times]_{\mathcal D_p}
=
\mathcal D_p(-m)-\mathcal D_p.
}
\]

All linear symplectic data and the required oscillator normalization are now proved. The missing statement is:

> **Wild-infinity Pascal oscillator realization and boundary theorem.** On the formal completion of the cyclic diagonal at root infinity, identify the cyclic trivial-minus-nontrivial nearby-cycle complex of the Smith-defect phase with the canonical geometric Weil/intertwining kernel attached to the proved Lagrangian graph `Gamma_D`. Prove that its punctured Airy-isotypic class is `D_p(-m)-D_p`, with the calibrated Frobenius orientation, and identify every complementary constituent with the already committed Tate, affine, discriminant, `q=2`, `q=infinity`, invariant and quadratic q-line boundary ledger.

This is one sharply stated new geometric theorem. It is not supplied by the ordinary Fourier delta identity, tame stationary phase, or geometric Weil theory alone.

## 9. What this lemma would and would not finish

If proved, the lemma completes the missing **application-side transport** from the ambient Airy module into the sparse/q-line irreducibility complex.

It would not by itself prove

\[
|T_p|\le C p^{(p-1)/2}
\]

or an alternative terminal q-line certificate. The analytic wall remains:

- prove the absolute Airy estimate; or
- prove a weaker one-sided, congruence or nonvanishing theorem sufficient to exclude simultaneous failure of both arithmetic classes.

## 10. Verification record

Remote exact runs:

1. `6a64cb547ef3c0846496861f`: all new affine-origin, symplectic, Jordan and quadratic-model verifiers passed.
2. `6a64cc947ef3c08464968642`: Pascal anti-symplectic verifier passed through the tested prime range.
3. `6a64c6c87ef3c084649685c3`: independent `p=11,r=3` q-line census passed.

## 11. Scientific position

### Proved theorem

- exact affine cubic-origin Airy/Tate decomposition;
- free affine-group quotient calibration;
- sparse residue symplectic form and regular Jordan structure;
- anti-symplectic Pascal coefficient--normal theorem;
- exact oscillator normalization for a compatible quadratic model.

### Published external theorem

- canonical geometric Weil/intertwining kernels and their normalization for finite symplectic/Lagrangian data in odd characteristic.

### Exact computer-assisted result

- independent `p=11,r=3` q-line trace `S_3=-7007`;
- deterministic verification of the new finite linear identities over the stated prime ranges.

### Open

- wild-infinity realization of the actual nearby cycles as the Pascal oscillator kernel;
- complementary boundary identification at object/all-power level;
- terminal Airy or q-line estimate;
- the function-field crown.

The configuration/Fourier route has reached a theorem-level reduction to one explicit new geometric lemma. The overall crown has not been reduced to that lemma alone because the separate analytic terminal wall remains.
