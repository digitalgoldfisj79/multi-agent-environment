# The divided hook is not a perfect complex: exact secondary-trace target

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Status:** the character obstruction and secondary trace formula below are **PROVED**. The geometric evaluation of the secondary trace remains **OPEN**. The `d=1` crown is not proved.

## 1. Root-cycle hook class

Let

\[
C_p=\langle\sigma\rangle
\]

act regularly on `p` roots, and let `V` be the `(p-1)`-dimensional augmentation representation. The alternating hook class is

\[
\Theta_p
=
\lambda_{-1}(V)
=
\sum_{i=0}^{p-1}(-1)^i\bigwedge^i V.
\]

Its character is

\[
\operatorname{Tr}(g\mid\Theta_p)
=
\det(1-g\mid V).
\]

At the identity this determinant is zero. At any nonidentity element of `C_p`, the eigenvalues on `V` are all nontrivial `p`-th roots of unity, so

\[
\det(1-g\mid V)
=
\prod_{j=1}^{p-1}(1-\zeta_p^j)
=p.
\]

Therefore

\[
\boxed{
\chi_{\Theta_p}(1)=0,
\qquad
\chi_{\Theta_p}(g)=p\quad(g\ne1).
}
\]

The regular character is `p` at the identity and zero elsewhere. Hence, in the characteristic-zero representation ring,

\[
\boxed{
\Theta_p=p\cdot\mathbf1-\operatorname{Reg}_{C_p}.
}
\]

This is the representation-theoretic source of both the exact `p`-cycle detector and the free-orbit Smith obstruction.

## 2. Normalized cycle indicator

The irreducibility indicator requires division by `p`. Its root-cycle class function is

\[
\vartheta_p(g)
=
\frac1p\chi_{\Theta_p}(g)
=
\begin{cases}
0,&g=1,\\
1,&g\ne1.
\end{cases}
\]

The Fourier multiplicity of the trivial character is

\[
\langle\vartheta_p,\mathbf1\rangle
=
\frac{p-1}{p}.
\]

For any nontrivial character `chi`,

\[
\langle\vartheta_p,\chi\rangle
=
\frac1p\sum_{g\ne1}\overline{\chi(g)}
=-\frac1p.
\]

Neither number is an integer.

### Theorem 2.1 — no ordinary divided-hook object

The normalized nonidentity indicator `vartheta_p` is not the character of a virtual finite-dimensional representation of `C_p` over any characteristic-zero field.

Consequently there is no ordinary perfect integral complex whose generic character is the divided hook `Theta_p/p`.

The obstruction is not ramification, compactification or failure to choose the correct lattice. It is already present in the rational character ring.

## 3. Consequence for the proposed mod-pi-squared construction

Let

\[
\mathcal F_a
=
\sum_{c,d}1_{F_{a,c,d}\mathrm{\ irr}}\zeta_p^c
=N_a+\pi M_a+O(\pi^2).
\]

The undivided alternating-hook Fourier trace is

\[
\mathcal H_a=p\mathcal F_a.
\]

Since

\[
p=u\pi^{p-1},
\qquad u\in\mathcal O^*,
\]

one has

\[
\mathcal H_a
=pN_a+p\pi M_a+O(p\pi^2).
\]

The desired first moment is the exact secondary coefficient

\[
\boxed{
M_a
\equiv
\frac{\mathcal H_a-pN_a}{p\pi}
\pmod\pi.
}
\]

This formula is integral for the actual arithmetic trace, but the operation is not represented by tensoring with an ordinary divided-hook complex.

## 4. What can exist

The correct construction must be trace-level or secondary. There are two equivalent formats.

### Raw high-precision format

Construct the undivided integral Fourier-hook complex through

\[
\mathcal O/(\pi^{p+1}).
\]

Extract `N_a` from the coefficient of order `p-1`, subtract `pN_a`, and extract `M_a` from order `p`.

### Divided secondary-trace format

Construct a secondary trace on the free root-cycle part that performs the arithmetic operation

\[
\frac{\mathcal H_a-pN_a}{p\pi}\pmod\pi
\]

without pretending that `Theta_p/p` is an object of the ordinary derived category.

For a finite free group-ring model, the natural carrier is the Hattori--Stallings trace of Frobenius. The previously isolated free-orbit defect is exactly the difference between its character evaluations. The first coefficient moment requires the coefficient-character derivative of that group-ring trace after the root-cycle division.

## 5. Bi-equivariant secondary invariant

Let `C_root` be the root-cycle group and `C_coeff` the additive coefficient Fourier group. A prospective integral model is naturally a complex over

\[
\mathcal O[C_{\rm root}\times C_{\rm coeff}].
\]

Let

\[
h_\Phi\in
\mathcal O[C_{\rm root}\times C_{\rm coeff}]
\]

be its alternating Hattori--Stallings Frobenius trace. The coefficient tangent is the canonical derivative

\[
\partial_{\rm coeff}h_\Phi
=
\left.
\frac{h_\Phi(\sigma,1+\pi)-h_\Phi(\sigma,1)}{\pi}
\right\pmod\pi.
\]

What is missing is a canonical root-cycle **secondary functional** on this derivative whose fibrewise value is the normalized nonidentity indicator. Theorem 2.1 proves that this functional cannot arise from an ordinary virtual representation.

The target is therefore not “find the correct divided sheaf.” It is:

> construct and evaluate a root-cycle secondary trace, compatible with Fourier pushforward, whose coefficient Bockstein equals the Cartier moment.

## 6. Why ordinary Smith theory is insufficient

Modulo `pi^2`, the hook identity becomes

\[
\Theta_p
=p\mathbf1-\operatorname{Reg}
\equiv-\operatorname{Reg},
\]

because `p=0`. The regular term is free over the root-cycle group ring and is killed by modular Tate/Smith localization.

Thus the modular Smith image is zero even though the divided arithmetic trace can be nonzero. This is precisely the phenomenon exhibited abstractly by the pure free-orbit Frobenius counterexample.

The coefficient tangent extension and its Bockstein do not repair this: they detect the coefficient Jordan class, but the required Frobenius scalar lives on the root-cycle free summand.

## 7. Exact build verdict

### Constructed

1. The coefficient character modulo `pi^2` as a nonsplit tangent extension.
2. Its Tate complex and Bockstein.
3. The exact root-hook identity
   \[
   \Theta_p=p\mathbf1-\operatorname{Reg}.
   \]
4. The proof that `Theta_p/p` is not an integral virtual character.
5. The exact secondary moment formula
   \[
   M_a=(\mathcal H_a-pN_a)/(p\pi)\pmod\pi.
   \]
6. The correct bi-equivariant Hattori--Stallings carrier for any future construction.

### Impossible in the proposed ordinary form

There is no ordinary perfect mod-`pi^2` divided-hook complex. Any claim to have constructed one would contradict the nonintegral Fourier multiplicities in Theorem 2.1.

### Still open

1. A geometric secondary trace compatible with the actual Fourier/Adams complex.
2. Its wild-infinity and finite-boundary local terms.
3. Nonvanishing of its coefficient tangent in either cubic square class.
4. The `d=1` crown.

## 8. Verification

Run

```bash
python frontier/strategy/divided_hook_character_secondary_trace_verify.py
```

Frozen output:

`frontier/strategy/divided_hook_character_secondary_trace_results_20260726.json`.
