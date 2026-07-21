# Exact discriminant and Möbius mass for the d=1 cubic slices

**Date:** 2026-07-21  
**Status:** proved algebraically; independently machine-checked by Sylvester-resultant determinants for every `(a,c,d)` at `p=5,7,11,13`.

## 1. Setup

Let `p >= 5` be prime, let `a in F_p^*`, and consider the depressed cubic slice

\[
f_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad c,d\in\mathbf F_p.
\]

Write `chi` for the quadratic character of `F_p`, extended by `chi(0)=0`, and put

\[
s_p=(-1)^{(p-1)/2}\in\mathbf F_p^*.
\]

This is the normal-form slice used in the d=1 function-field Fortune programme after the quadratic term has been killed by translation.

## 2. Exact discriminant formula

### Theorem DM.1

For `c != 0`, define

\[
\varepsilon_c=\chi\!\left(-\frac{c}{3a}\right)\in\{\pm1\}.
\]

Then

\[
\boxed{
\operatorname{Disc}(f_{a,c,d})
=s_p\left(3ad^2+c\left(\varepsilon_c+\frac{2c}{3}\right)^2\right).
}
\]

For `c=0`, the same formula is interpreted as

\[
\boxed{
\operatorname{Disc}(f_{a,0,d})=s_p\,3ad^2.
}
\]

### Proof

In characteristic `p`,

\[
f'_{a,c,d}(X)=3aX^2+c.
\]

Let `u^2=-c/(3a)`. For `c != 0`,

\[
u^p=\chi(u^2)u=\varepsilon_cu.
\]

Also

\[
au^3+cu=\frac{2c}{3}u.
\]

Hence

\[
f(u)=d+\left(\varepsilon_c+\frac{2c}{3}\right)u,
\qquad
f(-u)=d-\left(\varepsilon_c+\frac{2c}{3}\right)u.
\]

Since

\[
\operatorname{Res}(f,f')=(3a)^p f(u)f(-u)
=3a f(u)f(-u),
\]

and

\[
\operatorname{Disc}(f)=(-1)^{p(p-1)/2}\operatorname{Res}(f,f')
=s_p\operatorname{Res}(f,f'),
\]

the displayed formula follows. The case `c=0` follows directly from `f'=3aX^2`.

## 3. Exact full-slice character mass

Define

\[
M_a(p)=\sum_{c,d\in\mathbf F_p}
\chi\bigl(\operatorname{Disc}(f_{a,c,d})\bigr).
\]

Put

\[
\delta_a=\chi(2a),
\qquad
\iota=\chi(-1),
\]

and

\[
m_a=\mathbf 1_{\delta_a=1}
+\mathbf 1_{\iota\delta_a=-1}.
\]

### Theorem DM.2

\[
\boxed{
M_a(p)=p\,m_a\,\chi(s_p3a).
}
\]

Equivalently,

\[
\boxed{
M_a(p)=
\begin{cases}
p\chi(3a),&p\equiv1\pmod4,\\
-2p\chi(3a),&p\equiv3\pmod4\text{ and }\chi(2a)=1,\\
0,&p\equiv3\pmod4\text{ and }\chi(2a)=-1.
\end{cases}
}
\]

### Proof

For fixed `c`, the discriminant has the form

\[
A d^2+B_c,
\qquad A=s_p3a\ne0.
\]

The standard quadratic-character identity gives

\[
\sum_{d\in\mathbf F_p}\chi(Ad^2+B_c)
=
\begin{cases}
-\chi(A),&B_c\ne0,\\
(p-1)\chi(A),&B_c=0.
\end{cases}
\]

Besides `c=0`, a zero `B_c` requires

\[
\varepsilon_c+\frac{2c}{3}=0,
\qquad c=-\frac{3\varepsilon_c}{2}.
\]

The consistency conditions are

\[
\varepsilon_c=1:\quad \chi(2a)=1,
\]

and

\[
\varepsilon_c=-1:\quad \chi(-1)\chi(2a)=-1.
\]

Thus there are exactly `1+m_a` values of `c` with `B_c=0`. Summing the two cases over all `p` values of `c` yields

\[
M_a(p)=p\,m_a\chi(A).
\]

## 4. Exact discriminant-zero count

Let

\[
Z_a(p)=\#\{(c,d):\operatorname{Disc}(f_{a,c,d})=0\}.
\]

Then

\[
\boxed{
Z_a(p)=
\begin{cases}
p-\chi(2a),&p\equiv1\pmod4,\\
p,&p\equiv3\pmod4.
\end{cases}
}
\]

Consequently the numbers of nonzero square and nonsquare discriminants are determined exactly by

\[
N_++N_-=p^2-Z_a(p),
\qquad
N_+-N_-=M_a(p).
\]

## 5. Möbius interpretation

Pellet's formula over an odd finite field states

\[
\mu(f)=(-1)^{\deg f}\chi(\operatorname{Disc}f).
\]

Here `deg f=p` is odd, so, including the nonsquarefree cases where both sides vanish,

\[
\boxed{
\sum_{c,d}\mu(f_{a,c,d})=-M_a(p).
}
\]

Thus the proposed Stickelberger/discriminant route is not merely a parity observation: the complete two-parameter cubic slice has an exact Möbius mass of order `p`, the same scale as the empirically observed irreducible count.

## 6. What this proves, and what it does not

The formula is a genuine new exact layer for the programme. It reduces the full-slice discriminant character sum to elementary local data and shows that the Möbius mass is naturally on the target `~p` scale.

It does **not** by itself prove that an irreducible member exists. Squarefree reducible polynomials also contribute `+1` or `-1`, and their net contribution can cancel or reinforce the irreducible contribution.

The correct next target is the rootless-tail restriction

\[
\mathcal R_a=\{(c,d):aX^3+cX+d\text{ has no root in }\mathbf F_p\}.
\]

Since a rootless cubic is irreducible, `|R_a|=(p^2-1)/3` exactly. The restricted mass

\[
M_a^{(0)}(p)=
\sum_{(c,d)\in\mathcal R_a}
\chi(\operatorname{Disc}(f_{a,c,d}))
\]

is the first nontrivial mass capable of interacting directly with the necessary local condition for degree-`p` irreducibility. It should be attacked through the trace/norm parametrisation of irreducible depressed cubics over `F_{p^3}`. The verification script records this restricted mass as diagnostic data but makes no theorem claim for it.

## 7. Reproducibility

Run:

```bash
python frontier/d1_discriminant/discriminant_mass_check.py
```

The script uses only the Python standard library. It:

1. verifies the pointwise discriminant formula against independently constructed Sylvester determinants for every coefficient tuple at `p=5,7,11,13`;
2. verifies the closed full-slice mass and zero-count formulas for both square classes at all primes up to a configurable bound;
3. prints the rootless-tail restricted masses as explicitly labelled diagnostics.

## 8. Literature boundary

Pellet's formula is standard; a convenient modern proof is Ardavan Afshar, *A Proto-Pellet's Formula for the Möbius Function*, arXiv:2001.05641. No novelty claim is made here for the use of discriminants in sparse finite-field families. The exact specialised formulas DM.1--DM.2 should be checked against the sparse-polynomial parity literature before publication.