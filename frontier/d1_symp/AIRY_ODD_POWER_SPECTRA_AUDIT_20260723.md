# Odd-power Airy spectra at the characteristic boundary

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling, primes `p ≡ 5 (mod 6)`.  
**Status:** one general trace-extraction lemma is proved; the displayed low-rank spectra are exact computer-assisted theorems; the proposed uniform absolute trace bound remains open.

## 1. Sign convention frozen

With

\[
T_p=\sum_{\operatorname{Tr}_{\mathbf F_{p^p}/\mathbf F_p}(x)=0}
\psi(\operatorname{Tr}(x^3))
\]

as positively defined in `COLLAPSE_LEMMA.md`, the correct sign chain is

\[
\boxed{pT_p=\sum_{u\in\mathbf F_p}D_p(t_u,p)
=\operatorname{Tr}(F|U_p)-p\operatorname{Tr}(F|U_{p-2}).}
\]

The two negative-sign displays in the earlier terminal note are mutually consistent with each other, but both are globally sign-reversed relative to this explicit definition of `T_p`.

The exact separated first traces are

\[
\begin{array}{c|rr}
p&\operatorname{Tr}(F|U_p)&\operatorname{Tr}(F|U_{p-2})\\ \hline
11&1771561&-161051\\
17&202296965789&0\\
23&-9735230135207515&587175767636938\\
29&-17221580757743000101634&204297536026744106605.
\end{array}
\]

## 2. Proved odd-power trace-extraction lemma

Let

\[
H_k=H_c^1(\mathbf A^1_{\overline{\mathbf F}_p},\operatorname{Sym}^k\mathcal A),
\qquad U_k=H_k^{\mu_3}.
\]

For `p ≡ -1 (mod 3)`, arithmetic Frobenius sends a nontrivial character `χ` of `μ_3` to `χ^p=χ^{-1}`. Hence every odd power `F^m` interchanges `H_{k,χ}` and `H_{k,χ^{-1}}`; its trace on their direct sum is zero. Therefore

\[
\boxed{\operatorname{Tr}(F^m|H_k)=\operatorname{Tr}(F^m|U_k)
\quad(m\text{ odd}).}
\]

This avoids the projector defect that invalidates a raw `F^2` computation. In particular, `m=3` is the first new power trace obtainable from ordinary complete Airy sums without twisted `μ_3` Lefschetz terms.

## 3. Exact computation and certification

For each `p=11,17,23,29`, `airy_odd_power_spectra.py`:

1. constructs `F_{p^3}` from a monic irreducible cubic;
2. forms `Tr(x^3)` for every field element;
3. computes all additive Airy sums by an exact three-dimensional `p`-ary DFT modulo coefficient primes `ell ≡ 1 (mod p)`;
4. applies the complete-homogeneous recurrence for `Sym^k` with determinant `p^3`;
5. sums over all parameters and uses Grothendieck--Lefschetz plus the odd-power lemma;
6. reconstructs the unique signed integer by CRT.

The CRT product exceeds twice the Deligne-purity bound in every case. `airy_odd_power_independent_check.py` uses a different irreducible cubic and fresh coefficient primes at `p=23,29`; every residue agrees. The run also reproduces the rank-one cubes at `p=11`.

The exact third traces are

\[
\begin{array}{c|r|r}
p&\operatorname{Tr}(F^3|U_p)&\operatorname{Tr}(F^3|U_{p-2})\\ \hline
11&5559917313492231481&-4177248169415651\\
17&-255944298171217376101202104309234&0\\
23&24420035557874291486685783320490312291163556150933&1811942529812491726048499913466581810789054457\\
29&-624252554084396763440186646610590357883743693997978553242566200210&52044691388847887475857027569042615828726415261418059755550020.
\end{array}
\]

## 4. Self-duality and exact low-rank spectra

For odd `k`, `Sym^k A` has its natural alternating self-pairing. Cup product in degree one changes the sign, so the induced pairing on `H_c^1` is symmetric with similitude factor `p^{k+1}`. Its restriction to the `μ_3`-invariant summand is nondegenerate. Eigenvalues on `U_k` therefore occur in pairs

\[
\lambda,\quad p^{k+1}/\lambda,
\]

with one central eigenvalue `±p^{(k+1)/2}` in odd dimension. Newton identities applied to the exact first and third traces determine the following polynomials.

Write `y=λ/p^{(k+1)/2}`. For `U_{p-2}(-1)`, use the common weight `p+1`; the normalized phases are unchanged by the Tate twist.

### `p=17`, rank 2

\[
\boxed{\bar P_{17}(y)=y^2-\frac{29}{17}y+1.}
\]

Equivalently,

\[
\lambda=17^8\frac{29\pm3i\sqrt{35}}2,
\]

so the individual complex absolute values are exactly `17^9`. This is a per-eigenvalue purity check, not merely a trace inequality.

For `U_15`, both first and third traces vanish. Self-duality and purity leave exactly

\[
\bar P_{15}(y)=y^2-1\quad\text{or}\quad y^2+1.
\]

Odd traces cannot distinguish the determinant sign. It is not load-bearing.

### `p=23`, rank 3

\[
\boxed{\bar P_{23}(y)=(y-1)\left(y^2+\frac{764}{529}y+1\right),}
\]

and, after twisting `U_21` by `p`,

\[
\boxed{\bar P_{21(-1)}(y)=(y-1)\left(y^2+\frac{203}{529}y+1\right).}
\]

Thus the central eigenvalue `+23^12` cancels exactly between the two terms. This is a real common Frobenius factor, but the residual quadratic factors are distinct.

### `p=29`, rank 4

\[
\boxed{\bar P_{29}(y)=y^4+\frac{48674}{24389}y^3
+\frac{1531538}{707281}y^2+\frac{48674}{24389}y+1,}
\]

\[
\boxed{\bar P_{27(-1)}(y)=y^4-\frac{16745}{24389}y^3
+\frac{140088}{707281}y^2-\frac{16745}{24389}y+1.}
\]

Their exact gcd is one. The alternative anti-reciprocal determinant signs give roots off the purity circle and are excluded.

## 5. Common-factor route: exact ruling

After the Tate twist, exact gcds are

\[
\begin{array}{c|c}
p&\gcd(P_{U_p},P_{pU_{p-2}})\\ \hline
11&1\\
17&1\text{ for either determinant sign of }U_{15}\\
23&X-23^{12}\\
29&1.
\end{array}
\]

The `p=23` central cancellation is therefore occasional, not evidence for a uniform growing common factor. The previously tested bounded-residual-by-wholesale-factor-cancellation route remains closed. The spectra also have non-torsion normalized phases: at `p=17`, a root-of-unity phase would have algebraic-integral trace `y+y^{-1}`, whereas `29/17` is not an integer.

This does not rule out a subtler trace correlation without common factors.

## 6. Exact p-adic Newton polygons

The coefficient valuations give

\[
\begin{array}{c|c|c}
p&U_p&U_{p-2}\\ \hline
11&(6)&(5)\\
17&(8,10)&(8,8)\\
23&(10,12,14)&(9,11,13)\\
29&(12,14,16,18)&(11,13,15,17).
\end{array}
\]

At `p=11,23,29`, twisting `U_{p-2}` by `p` makes the slope multisets coincide. At `p=17` it gives `(9,9)`, not `(8,10)`. Exact slope-by-slope matching is therefore not a uniform theorem; the `p=17` trace-zero factor is a concrete supersingular exception.

## 7. Ruling

**Proved:** odd-power trace extraction and reciprocal/self-dual constraints.

**Exact computer-assisted theorem:** all third traces and low-rank characteristic polynomials above, with independent residue checks and CRT uniqueness certificates.

**New positive fact:** one exact central common factor at `p=23`.

**New negative facts:** no uniform common factor through ranks `1--4`; no uniform matched-slope theorem; no root-of-unity phase collapse.

**Still open:**

\[
|\operatorname{Tr}(F|U_p)-p\operatorname{Tr}(F|U_{p-2})|
\le C p^{(p+1)/2}
\]

with absolute `C`. The exact spectra make the wall concrete but provide no uniform mechanism for this estimate.
