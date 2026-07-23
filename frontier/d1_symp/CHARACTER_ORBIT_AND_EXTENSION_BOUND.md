# Character-orbit decomposition and the best elementary extension-field bound

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling, `p == 2 mod 3`.  
**Status:** exact decomposition and bounds are **PROVED**; bounded period collapse is **FALSIFIED COMPUTATIONALLY** at the calibrated primes.

## 1. Local Dickson form

Let

\[
t_u=-\sum_{x\in\mathbb F_p}\zeta_p^{x^3+ux}
\]

be the cubic Airy trace, with local inverse roots `alpha_u,beta_u` satisfying

\[
\alpha_u+\beta_u=t_u,
\qquad
\alpha_u\beta_u=p.
\]

Let `D_n(X,a)` be the Dickson polynomial characterized by

\[
D_n(\alpha+\beta,\alpha\beta)=\alpha^n+\beta^n.
\]

The rank-two identity gives

\[
h_p(t_u,p)-p h_{p-2}(t_u,p)=D_p(t_u,p),
\]

where `h_k` is the `Sym^k` trace. Therefore

\[
\boxed{-pT_p=\sum_{u\in\mathbb F_p}D_p(t_u,p).}
\]

Since cube map is bijective on `F_p` when `p == 2 mod 3`, `t_0=0`; because `p` is odd, `D_p(0,p)=0`. Only nonzero parameters remain.

## 2. Two exact Galois orbits

For `s in F_p^*`, let `sigma_{s^3}` be the cyclotomic Galois automorphism

\[
\zeta_p\longmapsto\zeta_p^{s^3}.
\]

Because cubing is bijective on `F_p^*`, these are all elements of `Gal(Q(zeta_p)/Q)`. Changing variables `y=sx` gives

\[
\sigma_{s^3}(t_u)=t_{s^2u}.
\]

Thus the nonzero parameters split into two Galois orbits:

- `u` a square;
- `u` a nonsquare.

Each has size `(p-1)/2` in the tested cases, and the virtual trace is exactly the sum of two real-cyclotomic field traces:

\[
\boxed{
-pT_p=
\operatorname{Tr}_{K_p^+/\mathbb Q}D_p(t_{\square},p)
+
\operatorname{Tr}_{K_p^+/\mathbb Q}D_p(t_{\mathrm{ns}},p),
}
\]

where the two generators may define different copies/embeddings of the real cyclotomic field.

This is the terminal exact character decomposition available from base-field Galois symmetry alone.

## 3. Focused period-polynomial test

The script `airy_period_orbit_probe.py` constructs, exactly in `Z[zeta_p]`, the orbit polynomial of `t_u` in each square class and reduces `D_p(X,p)` modulo it.

| `p` | orbit degree | Dickson remainder degree, square | nonsquare |
|---:|---:|---:|---:|
| 11 | 5 | 4 | 4 |
| 17 | 8 | 7 | 7 |
| 23 | 11 | 10 | 10 |
| 29 | 14 | 13 | 13 |

At every tested prime, the Dickson remainder has the maximal possible degree `orbit_degree-1` in both sectors. The corresponding field traces are:

| `p` | square trace | nonsquare trace | sum `=-pT_p` |
|---:|---:|---:|---:|
| 11 | `-1771561` | `-1771561` | `-3543122` |
| 17 | `-174393936025` | `-27903029764` | `-202296965789` |
| 23 | `2817002762528132` | `20423270028328957` | `23240272790857089` |
| 29 | `8049640132707626151791` | `15096569169810953041388` | `23146209302518579193179` |

All totals agree exactly with the committed values of `-pT_p`.

### Consequence

The simplest character proposal

> reduce `D_p(t,p)` to a polynomial of uniformly bounded degree in a Gaussian-period generator

is false in every calibrated nontrivial case through `p=29`. The Dickson value uses the full orbit algebra.

This does not rule out cancellation between the two full field traces. Proving such cancellation is precisely a new global period theorem.

## 4. Independent extension-field representation

Let

\[
K=\mathbb F_{p^p},
\qquad
H=\{x\in K:\operatorname{Tr}_{K/\mathbb F_p}(x)=0\},
\]

and

\[
T_p=\sum_{x\in H}\psi_K(x^3).
\]

Additive orthogonality gives

\[
T_p=
\frac1p\sum_{b\in\mathbb F_p}
\sum_{x\in K}\psi_K(x^3+bx).
\]

The `b=0` term is zero: `gcd(3,p^p-1)=1`, so cubing permutes `K`. For `b!=0`, the degree-three polynomial `x^3+bx` is not Artin--Schreier degenerate and the classical Weil bound gives

\[
\left|\sum_{x\in K}\psi_K(x^3+bx)\right|
\le2|K|^{1/2}=2p^{p/2}.
\]

Hence

\[
\boxed{
|T_p|
\le
\frac{2(p-1)}{p}p^{p/2}
=
\frac{2(p-1)}{\sqrt p}\,p^{(p-1)/2}.
}
\]

Combined with the Chuang `mu_3` reduction, the best current unconditional coefficient is

\[
\boxed{
|T_p|
\le
\min\left\{
\frac{p-5}{3},
\frac{2(p-1)}{\sqrt p}
\right\}
p^{(p-1)/2}.
}
\]

The extension-field estimate is stronger from `p=47` onward. It changes the loss from linear to square-root growth, but it still does not give an absolute constant.

## 5. Why general moment formulas do not finish the argument

Standard Weil-sum moment identities rewrite products or powers of the Airy/Weil sums as point counts on the intersection of a hyperplane and a Fermat variety. Applied at order growing with `p`, this returns to the same cubic linear-section geometry already isolated in this branch. It is an exact reformulation, not an independent cancellation theorem.

## 6. Terminal verdict for the character route

### PROVED

- the virtual trace is a sum of two explicit real-cyclotomic field traces;
- a second exact representation gives an unconditional `O(sqrt(p))` coefficient;
- standard moment conversion returns to the existing linear-section problem.

### VERIFIED COMPUTATIONALLY

The period-polynomial remainder has full degree at `p=11,17,23,29` in both Galois sectors.

### GENUINELY NEW MATH REQUIRED

One must prove a uniform cancellation theorem of the form

\[
\left|
\operatorname{Tr}D_p(t_{\square},p)
+
\operatorname{Tr}D_p(t_{\mathrm{ns}},p)
\right|
\le C p^{(p+1)/2},
\]

or an equivalent Frobenius-correlation theorem for `U_p` and `U_{p-2}(-1)`.

No bounded orbit degree, ordinary Galois symmetry, individual Weil bound, or known fixed-order moment identity supplies this cancellation.
