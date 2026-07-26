# Global Cartier mass and naive `p^2` lift obstruction

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** function-field Fortune `d=1`, depressed cubic family  
**Status:** the Fourier-collapse theorem and the naive-lift counterexamples below are **PROVED**. The crown remains **OPEN**.

## 1. Setup

For an odd prime `p` and `a != 0`, write

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d
\]

and

\[
N_a(p)=\#\{(c,d)\in\mathbf F_p^2:F_{a,c,d}\text{ is irreducible}\}.
\]

The proved general Cartier-cofactor theorem gives the pointwise identity

\[
\boxed{
C_3(F_{a,c,d})=3a\,1_{F_{a,c,d}\text{ irreducible}}
}
\qquad\text{in }\mathbf F_p.
\]

The count depends only on the quadratic class of `a`. Denote the two values by

\[
N_+(p),\qquad N_-(p).
\]

The proposed global-mass route was to sum the cofactor over all `a,c,d`, with a multiplicative weight in `a`, and then lift the resulting invariant `p`-adically if its first digit vanished.

## 2. Complete multiplicative Fourier collapse

For an integer `r`, define

\[
\mathcal M_r(p)
=
\sum_{a\in\mathbf F_p^*}\sum_{c,d\in\mathbf F_p}
 a^{r-1}C_3(F_{a,c,d}).
\]

Using the pointwise cofactor theorem,

\[
\mathcal M_r(p)=3\sum_{a\ne0}a^rN_a(p).
\]

Write

\[
N_a=A_p+B_p\chi(a),
\qquad
A_p=\frac{N_++N_-}{2},
\qquad
B_p=\frac{N_+-N_-}{2}.
\]

The standard power sums on `F_p^*` give

\[
\sum_{a\ne0}a^r
=
\begin{cases}
-1,&r\equiv0\pmod{p-1},\\
0,&\text{otherwise},
\end{cases}
\]

and

\[
\sum_{a\ne0}\chi(a)a^r
=
\begin{cases}
-1,&r\equiv(p-1)/2\pmod{p-1},\\
0,&\text{otherwise}.
\end{cases}
\]

Therefore:

### Theorem 2.1 (global Cartier Fourier collapse)

\[
\boxed{
\mathcal M_0(p)=-\frac32\bigl(N_+(p)+N_-(p)\bigr),
}
\]

\[
\boxed{
\mathcal M_{(p-1)/2}(p)
=-\frac32\bigl(N_+(p)-N_-(p)\bigr),
}
\]

and

\[
\boxed{
\mathcal M_r(p)=0
}
\]

for every other residue class of `r mod p-1`.

Thus the complete `a`-average has exactly two multiplicative Fourier modes: the already-known class sum and class difference. It creates no third invariant capable of excluding simultaneous vanishing.

More generally, any weighted sum over `a` is a linear combination of `N_+` and `N_-`, because `N_a` is constant on the two square classes. Parameter averaging cannot by itself add arithmetic information beyond those two counts.

## 3. The trivial global mass is not uniformly nonzero

The exact committed cubic counts include

\[
p=5:\quad (N_+,N_-)=(4,6),
\]

and

\[
p=19:\quad (N_+,N_-)=(22,16).
\]

Hence

\[
N_++N_-=2p
\]

at both primes, and therefore

\[
\boxed{
\mathcal M_0(p)=0\quad\text{in }\mathbf F_p
}
\]

although both cubic classes contain irreducibles.

Consequently, the proposed theorem “the global mod-`p` Cartier mass is always nonzero” is false. A first-digit aggregate criterion would miss genuine positive counts that are multiples of `p`.

The quadratic Fourier mode does not repair this structurally: it is merely the class difference. Simultaneous vanishing of the two modes says

\[
p\mid N_+,\qquad p\mid N_-,
\]

not that either integer count is zero.

## 4. Why the obvious `p^2` lift is invalid

One might try to retain the same coefficient formula over `Z/p^2`:

1. choose integer representatives of `a,c,d`;
2. form `F^{p-1}` modulo `p^2`;
3. define `H_(u,v)=[X^(pu-v)]F^{p-1}`;
4. take the same selected cofactor of `I-H` modulo `p^2`.

Call this the **naive integral lift**.

The ordinary cofactor theorem is a characteristic-`p` Cartier/Frobenius statement. It does not assert that this coefficientwise lift remains an irreducibility indicator over `Z/p^2`.

The exact exhaustive verifier `global_cartier_mass_p2_verify.py` establishes the following.

### Theorem 4.1 (naive `p^2` lift obstruction)

At both `p=5` and `p=7`:

1. reducible fibres have nonzero naive lifted cofactors modulo `p^2`;
2. replacing the integer lift `a` by `a+p`, which defines the same element of `F_p`, changes the naive lifted cofactor on many fibres;
3. the completely weighted naive lifted mass is not `3` times the lifted irreducible count modulo `p^2`.

The exact results are:

| `p` | reducible fibres with nonzero naive lift | fibres changed by `a -> a+p` | naive weighted mass | `3 x` indicator total |
|---:|---:|---:|---:|---:|
| 5 | 42 | 40 | 0 mod 25 | 10 mod 25 |
| 7 | 76 | 120 | 22 mod 49 | 15 mod 49 |

Therefore the naive integral cofactor is neither supported on irreducibles nor independent of arbitrary lift choices.

## 5. Exact ruling

The proposed global Cartier-mass programme is closed in the following form:

- averaging over the cubic coefficient `a` produces only the existing class sum and class difference;
- the trivial aggregate first digit can vanish at primes where the cubic counts are positive;
- the same determinant formula cannot simply be read modulo `p^2` to recover the next digit.

A valid higher-digit theorem would require a **canonical Witt/Frobenius construction**, together with explicit reducible and singular correction terms. That would be a new characteristic-`p` theorem, not a routine continuation of the ordinary Cartier cofactor.

## 6. What is not refuted

This result does **not** refute:

1. the pointwise ordinary Cartier cofactor theorem;
2. a fixed-square-class proof that `N_a not congruent 0 mod p`;
3. a canonical higher-Witt irreducibility indicator with the correct correction complex;
4. another exact invariant not obtained by multiplicative averaging of `C_3`;
5. a constructive or q-line nonsaturation proof of the crown.

The fixed-class determinant residue remains an exact and potentially load-bearing object. What is refuted is the claim that summing over `a` or taking the coefficient formula naively modulo `p^2` makes that object simpler.

## 7. Verification

Run

```bash
python frontier/strategy/global_cartier_mass_p2_verify.py
```

The script uses no external packages and exhaustively checks every `a != 0,c,d` at `p=5,7`. Its frozen output is

```text
frontier/strategy/global_cartier_mass_p2_results_20260726.json
```
