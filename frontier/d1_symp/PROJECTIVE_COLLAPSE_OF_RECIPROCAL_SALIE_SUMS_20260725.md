# Projective collapse of the reciprocal Salié sums

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic `d=1` Airy wall, primes `p congruent 5 mod 6`.  
**Status:** **PROVED**.

## 1. Setup

Retain the notation of

`CUBIC_WEYL_DIFFERENCING_TO_RECIPROCAL_SALIE_SUMS_20260725.md`:

\[
E=\mathbf F_{p^p},
\qquad
H=\ker\operatorname{Tr}_{E/\mathbf F_p},
\]

\[
C(h)=\operatorname{Tr}(h^3),
\qquad
\delta(h)=\operatorname{Tr}(h^{-1})\quad(h\ne0).
\]

Let

\[
\mathbf P(H)=H^*/\mathbf F_p^*.
\]

For a regular line `L=[h]` with `delta(h)!=0`, define

\[
w(L)=\chi_E(h)\chi(\delta(h)).
\]

This is independent of the representative because, for `lambda in F_p^*`,

\[
\chi_E(\lambda)=\chi(\lambda)
\]

and

\[
\chi(\delta(\lambda h))
=\chi(\lambda^{-1})\chi(\delta(h)).
\]

Define the projective sums

\[
\mathcal R_{\mathrm{all}}(p)
=
\sum_{\substack{L=[h]\in\mathbf P(H)\\ \delta(h)\ne0}}w(L),
\]

\[
\mathcal R_0(p)
=
\sum_{\substack{L=[h]\in\mathbf P(H)\\ \delta(h)\ne0\\ C(h)=0}}w(L),
\]

and

\[
\mathcal D(p)
=
\sum_{\substack{L=[h]\in\mathbf P(H)\\ \delta(h)=0\\ C(h)\ne0}}
\chi_E(h)\chi(C(h)).
\]

The last summand is also representative-independent because scaling changes the two characters by

\[
\chi(\lambda)
\quad\text{and}\quad
\chi(\lambda^3),
\]

whose product is one.

## 2. Collapse of the regular sum

### Theorem 2.1

\[
\boxed{
\mathcal S_{\mathrm{reg}}(p)
=p\mathcal R_0(p)-\mathcal R_{\mathrm{all}}(p).
}
\]

### Proof

Fix a regular projective line `L=[h]`. The character weight is invariant under `h -> lambda h`, while

\[
\operatorname{Tr}((\lambda h)^3/4)
=\lambda^3\operatorname{Tr}(h^3/4).
\]

Since cubing is a bijection of `F_p^*`,

\[
\sum_{\lambda\ne0}
\psi\left(\lambda^3\operatorname{Tr}(h^3/4)\right)
=
\begin{cases}
p-1,&C(h)=0,\\-1,&C(h)\ne0.
\end{cases}
\]

Summing over projective lines gives the formula.

## 3. Collapse of the degenerate sum

### Theorem 3.1

\[
\boxed{
\mathcal S_{\mathrm{deg}}(p)
=G_p\mathcal D(p).
}
\]

### Proof

For a degenerate line `L=[h]`, its scalar orbit contributes

\[
\chi_E(h)
\sum_{\lambda\ne0}
\chi(\lambda)
\psi\left(\lambda^3 C(h)/4\right).
\]

The inverse of `3` modulo `p-1` is odd, so under `mu=lambda^3`,

\[
\chi(\lambda)=\chi(\mu).
\]

If `C(h)=0`, the orbit sum is zero. If `C(h)!=0`, it is

\[
\chi_E(h)\chi(C(h))G_p,
\]

because `4` is a square. Summing the projective contributions proves the theorem.

## 4. Fully projective second-moment identity

Using

\[
G_p^2=\chi(-1)p,
\]

the reciprocal Salié identity becomes:

### Theorem 4.1

\[
\boxed{
\begin{aligned}
|T_p|^2
={}&p^{p-1}
+\chi(-1)p^{(p-1)/2}
\left(p\mathcal R_0(p)-\mathcal R_{\mathrm{all}}(p)\right)\\
&+\chi(3)p^{(p+1)/2}\mathcal D(p).
\end{aligned}
}
\]

All quantities on the right are rational integers.

## 5. Polynomial interpretation

For `h!=0`,

\[
\operatorname N(h)\operatorname{Tr}(h^{-1})
=e_{p-1}(h,h^p,\ldots,h^{p^{p-1}}).
\]

Thus

\[
w([h])=\chi(e_{p-1}(h)).
\]

Moreover, since `Tr(h)=0`, Newton's identity gives

\[
C(h)=\operatorname{Tr}(h^3)=3e_3(h).
\]

Therefore:

- `R_all` is the quadratic-character sum of `e_(p-1)` on `P(H)`;
- `R_0` is its restriction to the cubic section `e_3=0`;
- `D` is the quadratic-character sum of `Norm(h) C(h)` on the divisor `e_(p-1)=0`, with `C!=0`.

The additive Artin--Schreier phase has disappeared entirely.

## 6. Sharp sufficient theorem

The natural projective square-root estimates are

\[
\boxed{
|\mathcal R_{\mathrm{all}}(p)|
\le C_1p^{(p-2)/2},
}
\]

\[
\boxed{
|\mathcal R_0(p)|
\le C_2p^{(p-3)/2},
}
\]

and

\[
\boxed{
|\mathcal D(p)|
\le C_3p^{(p-3)/2}.
}
\]

Absolute constants in these three estimates imply

\[
|T_p|^2\ll p^{p-1}
\]

and hence the required Airy bound.

## 7. Scientific interpretation

The analytic wall has now been stripped to pure projective quadratic-character cancellation. There is:

- no symmetric-power local system in the final statement;
- no additive phase;
- no reciprocal denominator;
- no finite boundary ambiguity.

The remaining difficulty is uniform topology: the forms `e_(p-1)` and the associated double covers have degree growing with `p`, so a generic Weil bound carries growing Betti constants. A successful proof must exploit their Frobenius-conjugate elementary-symmetric origin.

## 8. Exact new terminal lemma

> **Uniform projective elementary-symmetric character theorem.** Prove the three displayed projective square-root estimates with constants independent of `p`, using the trace/norm structure of the degree-`p` Artin--Schreier extension.

This theorem implies the analytic half-theorem and, after the separate application transport, the function-field `d=1` crown.

## 9. Verification

`projective_salie_collapse_verify.py` verifies all three projective collapses and the final second-moment identity by exact enumeration in `F_(5^5)`.
