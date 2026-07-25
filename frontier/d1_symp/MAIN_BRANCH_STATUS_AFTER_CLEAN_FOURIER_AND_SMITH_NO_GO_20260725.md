# Authoritative d=1 status after clean Fourier elimination and the Smith no-go theorem

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` sibling only.  
**Status:** supersedes the proposed integral-Smith completion in all earlier frontier notes.

## 1. Ruling

The crown remains open.

The requested continuation had two logically distinct components:

1. eliminate the first `p-4` Fourier/Jordan directions and reduce to the cubic-tail/q-line complex;
2. deduce an absolute characteristic-zero Frobenius bound from modular Smith contraction.

The first component is now **PROVED**, in a stronger global form that controls all extension data and Frobenius before passing to the Jordan associated graded.

The second component does **not** follow. A pure, integral, affine-normalizer-equivariant free cyclic lattice gives an exact counterexample to the required inference. Modular Smith can be zero while the generic trivial-minus-nontrivial trace is one full Weil-scale eigenvalue per free copy.

## 2. PROVED: global clean Fourier elimination

Let

\[
X=(A^1)^p,
\qquad
A=A^{p-4},
\qquad
S=(s_1,\ldots,s_{p-4}),
\]

and put

\[
\mathcal L
=
\mathcal L_\psi\left(\sum_{m=1}^{p-4}a_ms_m\right).
\]

For `ell != p`, over an integral coefficient ring containing the additive-character values,

\[
\boxed{
R\pi_!\mathcal L
\cong
i_!\mathcal O(-(p-4))[-2(p-4)],
}
\]

where `i:S^{-1}(0)->X`.

This is a stalkwise Fourier-delta identity on the full complex. It is `S_p`-equivariant and Frobenius-compatible. Since `p` is a unit in the coefficient ring, the cyclic trivial and nontrivial character projectors commute with the pushforward.

Therefore every nonsplit Jordan extension is already included in the calculation: the first `p-4` directions contribute only the forced Tate shift and no hidden summand.

## 3. PROVED: exact residual cubic-tail trace

For every `q=p^r`,

\[
\boxed{
q^{-(p-4)}
\sum_{a\in F_q^{p-4}}
Def_q(f_a)
=
\#\{\alpha\in F_{q^p}:Tr(\alpha^m)=0,\ 1\le m\le p-4\}-q.
}
\]

The subtracted `q` is the Smith diagonal. Newton identities identify every remaining degree-`p` element with an irreducible polynomial

\[
T^p+AT^3+BT^2+CT+D.
\]

Hence

\[
\boxed{
q^{-(p-4)}
\sum_a Def_q(f_a)
=pN_{cubic}(q).
}
\]

The residual characteristic-zero Fourier object is exactly the finite-flat cubic-tail ordered-root cover, and its normal-form decomposition is the existing q-line plus explicit boundary ledger.

This closes the application-side coefficient transport. It does not isolate or bound the distinguished cubic-origin Airy fibre.

## 4. PROVED: pure free-orbit Smith obstruction

Let

\[
M=\mathcal O[C_p],
\qquad
J=\sum_{g\in C_p}g,
\]

with the natural `AGL_1(F_p)` action. For `m>=1`, put

\[
Q=p^{2m},
\qquad
b=p^{m-1},
\]

and on `M tensor O^2` define

\[
\Phi
=
1\otimes
\begin{pmatrix}0&-Q\\1&0\end{pmatrix}
+
J\otimes
\begin{pmatrix}0&0\\0&b\end{pmatrix}.
\]

On a nontrivial cyclic character, the characteristic polynomial is

\[
X^2+Q.
\]

On the trivial character, it is

\[
X^2-p^mX+Q.
\]

Every root in both sectors is an algebraic integer of complex absolute value `p^m`, so the Frobenius is pure of one common weight. Nevertheless,

\[
\boxed{
Tr(\Phi|M^C)-Tr(\Phi|M_\xi)=p^m.
}
\]

Modulo the maximal ideal, `M` is free over `k[C_p]`, so its modular Tate/Smith localization is zero. Direct sums give an arbitrarily large multiple of the Weil scale while remaining invisible to Smith.

Taking

\[
m=(p+1)/2
\]

makes one invisible copy contribute exactly

\[
p^{(p+1)/2}.
\]

Thus modular rank two, integrality, purity, Frobenius, affine-normalizer equivariance and a unimodular associated-graded pairing do not imply an absolute coefficient.

## 5. Coefficient-category boundary

The proved Fourier elimination is integral `ell`-adic with `ell != p`. In that category the Artin--Schreier kernel exists and `C_p` is semisimple.

Modular Smith localization requires residue characteristic `p`, where free `k[C_p]`-modules disappear. Ordinary reduction of the Artin--Schreier character loses its phase, and ordinary etale `p`-adic coefficients are not the relevant Weil cohomology on a characteristic-`p` base.

A Dwork or arithmetic-D-module theory can retain the phase, but the required integral lattice and compatibility between Fourier pushforward, Smith localization and Frobenius at `k=p` have not been constructed. Existing effective Dwork decomposition stops at `k<p`; the audited `k=p` lift has linearly growing residual support.

The two integral statements cannot be spliced across coefficient categories.

## 6. Exact remaining analytic theorem

Let `K_free` be the free cyclic part of the actual integral Airy complex and let `Phi` be Frobenius. The missing invariant is

\[
\delta_\Phi(K_{free})
=
Tr(\Phi|K_{free}^C)
-
Tr(\Phi|(K_{free})_\xi).
\]

A proof must establish, from the specific Airy/Dwork geometry rather than abstract Smith theory,

\[
\boxed{
|\delta_\Phi(K_{free})|
\le C p^{(p+1)/2}
}
\]

with absolute `C`, or an exact vanishing/cancellation theorem implying it.

This is equivalent to the remaining Airy correlation

\[
\boxed{
|Tr(F|R_p)|
\le C p^{(p+1)/2}.
}
\]

No such theorem has been proved here or located in the existing Fourier, Smith, nearby-cycle or Dwork literature.

## 7. Closed and open

### PROVED

- full integral `ell`-adic Fourier elimination of the first `p-4` directions;
- control of all extension data and Frobenius in that elimination;
- exact reduction of the averaged characteristic-zero defect to the cubic-tail/q-line cover;
- a pure normalizer-equivariant counterexample to the Smith-to-absolute-bound inference.

### CLOSED

- claiming that modular Smith rank controls the generic characteristic-zero trace;
- combining `ell`-adic Fourier and mod-`p` Smith as if they were one integral coefficient theory;
- deriving the absolute Airy bound from the unimodular Pascal pairing alone.

### OPEN

- Airy-specific cancellation of the free-orbit Frobenius trace;
- the absolute Airy bound;
- the crown.

Papers V and VI remain frozen. The next valid research input must control the actual group-ring Frobenius trace on the Airy free cyclic part; another associated-graded or modular-rank calculation cannot close the theorem.
