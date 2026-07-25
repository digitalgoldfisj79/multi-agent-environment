# Artin--Schreier low-degree Tschirnhaus no-go

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-boulders-hayes-first-20260725`  
**Scope:** constructive bypass for function-field `d=1`, primes `p congruent 5 mod 6`, `p>=11`.  
**Status:** **PROVED**.

## 1. Artin--Schreier model and trace formula

Let

\[
E=\mathbf F_p(\alpha),
\qquad
\alpha^p-\alpha=1.
\]

The conjugates of `alpha` are

\[
\alpha+i,
\qquad i\in\mathbf F_p.
\]

For every integer `N>=0`,

\[
\operatorname{Tr}_{E/\mathbf F_p}(\alpha^N)
=
-\sum_{\substack{j>0\\p-1\mid j\\j\le N}}
\binom Nj\alpha^{N-j}.
\]

Indeed, expand

\[
\sum_{i\in\mathbf F_p}(\alpha+i)^N
\]

and use

\[
\sum_{i\in\mathbf F_p}i^j
=
\begin{cases}
-1,&j>0,\ p-1\mid j,\\
0,&\text{otherwise}.
\end{cases}
\]

The critical special values are

\[
\boxed{
\operatorname{Tr}(\alpha^{p-1})=-1,
}
\]

\[
\boxed{
\operatorname{Tr}(\alpha^{2p-2})=-1,
}
\]

and

\[
\boxed{
\operatorname{Tr}(\alpha^{2p-1})=-1.
}
\]

For `2p-2`, Lucas' theorem gives

\[
\binom{2p-2}{p-1}=0,
\]

so only `j=2p-2` contributes. For `2p-1`,

\[
\binom{2p-1}{p-1}=1,
\qquad
\binom{2p-1}{2p-2}=-1
\quad\text{in }\mathbf F_p,
\]

and therefore

\[
\operatorname{Tr}(\alpha^{2p-1})
=-\alpha^p+\alpha=-1.
\]

## 2. Why the trace conditions matter

If `beta in E` has degree `p`, its conjugates have power sums

\[
\operatorname{Tr}(\beta^m).
\]

Newton identities show that the minimal polynomial of `beta` has the cubic-tail form

\[
T^p+AT^3+BT^2+CT+D
\]

only if

\[
\operatorname{Tr}(\beta^m)=0
\qquad(1\le m\le p-4).
\]

Thus a Tschirnhaus construction from the Artin--Schreier extension must satisfy these trace equations.

Adding a base-field constant and multiplying by a nonzero base-field scalar do not affect simultaneous vanishing of the first `M` traces. This follows inductively from

\[
\operatorname{Tr}((\beta+c)^m)
=
\operatorname{Tr}(\beta^m)
+
\sum_{j<m}\binom mjc^{m-j}\operatorname{Tr}(\beta^j),
\]

because `Tr(1)=p=0`.

Replacing `alpha` by `alpha+s`, with `s in F_p`, also preserves the Artin--Schreier equation.

## 3. Quadratic polynomial transforms

### Theorem 3.1

Let `h in F_p[X]` have degree two. For `p>=7`, the element

\[
\beta=h(\alpha)
\]

cannot satisfy

\[
\operatorname{Tr}(\beta^m)=0
\qquad(1\le m\le p-4).
\]

### Proof

After translating the input, scaling the output and deleting an output constant, reduce to

\[
\beta=\alpha^2.
\]

Put

\[
m=\frac{p-1}{2}.
\]

For `p>=7`, `m<=p-4`. But

\[
\operatorname{Tr}(\beta^m)
=
\operatorname{Tr}(\alpha^{p-1})
=-1.
\]

This contradicts the required vanishing. \(\square\)

## 4. Cubic polynomial transforms

### Theorem 4.1

Let `p congruent 2 mod 3`, `p>=11`, and let `h in F_p[X]` have degree three. Then

\[
\beta=h(\alpha)
\]

cannot satisfy

\[
\operatorname{Tr}(\beta^m)=0
\qquad(1\le m\le p-4).
\]

### Proof

Depress the cubic by translating the input. After scaling and deleting a constant, reduce to

\[
\beta=\alpha^3+r\alpha
\]

for some `r in F_p`.

Write

\[
p=3h_0+2
\]

and put

\[
m=h_0+1=\frac{p+1}{3}.
\]

The polynomial

\[
(X^3+rX)^m
\]

has degree `p+1`. In the trace, the monomials of degrees `p` and `p+1` contribute zero because

\[
\binom p{p-1}
=
\binom{p+1}{p-1}
=0
\quad\text{in }\mathbf F_p.
\]

The coefficient of `X^(p-1)` is obtained by replacing exactly one cubic factor by its linear term. It is

\[
mr.
\]

Therefore

\[
\boxed{
\operatorname{Tr}(\beta^m)=-mr.
}
\]

Since `m` is nonzero modulo `p`, the required vanishing forces

\[
r=0.
\]

Now put

\[
n=2h_0+1=\frac{2p-1}{3}.
\]

For `p>=11`,

\[
n\le p-4.
\]

With `r=0`,

\[
\operatorname{Tr}(\beta^n)
=
\operatorname{Tr}(\alpha^{3n})
=
\operatorname{Tr}(\alpha^{2p-1})
=-1.
\]

This is the desired contradiction. \(\square\)

## 5. Quartic polynomial transforms

### Theorem 5.1

Let `p>=11` be an odd prime and let `h in F_p[X]` have degree four. Then

\[
\beta=h(\alpha)
\]

cannot satisfy

\[
\operatorname{Tr}(\beta^m)=0
\qquad(1\le m\le p-4).
\]

### Proof

Translate the input to remove the cubic coefficient. After scaling and deleting an output constant, reduce to

\[
\beta=\alpha^4+r\alpha^2+s\alpha.
\]

There are two cases.

### Case 1: `p congruent 1 mod 4`

Put

\[
m=\frac{p-1}{4}.
\]

Then `m<=p-4`, and `beta^m` has degree exactly `p-1` with leading coefficient one. Hence

\[
\operatorname{Tr}(\beta^m)=-1.
\]

### Case 2: `p congruent 3 mod 4`

Put

\[
m=\frac{p+1}{4}.
\]

The polynomial `beta^m` has degree `p+1`. As in the cubic case, only its `X^(p-1)` coefficient contributes to the trace. That coefficient is

\[
mr,
\]

so vanishing forces `r=0`.

Now use the next moment

\[
m+1=\frac{p+5}{4}.
\]

The polynomial

\[
(X^4+sX)^{m+1}
\]

has degree `p+5`. Since `p+5<2p-2` for `p>=11`, only its `X^(p-1)` coefficient contributes. The required deficit from the top degree is six, obtained by choosing the linear term in exactly two factors. Therefore

\[
\operatorname{Tr}(\beta^{m+1})
=-\binom{m+1}{2}s^2.
\]

The binomial coefficient is nonzero modulo `p`, so vanishing forces `s=0`.

Finally put

\[
n=\frac{p-1}{2}.
\]

Then `n<=p-4`, and for the remaining pure fourth power

\[
\operatorname{Tr}(\beta^n)
=
\operatorname{Tr}(\alpha^{2p-2})
=-1.
\]

Both cases contradict the trace conditions. \(\square\)

## 6. Möbius transforms

### Theorem 6.1

Let

\[
\beta=\frac{a\alpha+b}{c\alpha+d},
\qquad ad-bc\ne0.
\]

If `c ne 0`, then

\[
\boxed{
\operatorname{Tr}(\beta)\ne0.
}
\]

If `c=0`, the transform is affine and gives only another Artin--Schreier generator, whose minimal polynomial has a linear-plus-constant tail and is therefore the excluded degree-one-offset family.

### Proof

For `c ne0`, write

\[
\beta=A+\frac B{\alpha-r}
\]

with `B ne0` and `r in F_p`.

Let

\[
f(X)=X^p-X-1
=
\prod_{i\in F_p}(X-\alpha-i).
\]

At `r in F_p`,

\[
f(r)=-1,
\qquad
f'(r)=-1,
\]

so

\[
\sum_{i\in F_p}\frac1{r-\alpha-i}
=
\frac{f'(r)}{f(r)}=1.
\]

Consequently

\[
\sum_{i\in F_p}\frac1{\alpha+i-r}=-1
\]

and

\[
\operatorname{Tr}(\beta)=-B\ne0.
\]

Thus every non-affine Möbius transform fails the first trace condition. \(\square\)

## 7. Consequence for the constructive route

For `p congruent 5 mod 6`, `p>=11`, none of the following can produce a cubic-tail witness from the canonical Artin--Schreier extension:

1. a quadratic polynomial transform;
2. a cubic polynomial transform;
3. a quartic polynomial transform;
4. a non-affine Möbius transform.

Affine transforms produce only

\[
T^p-T-c,
\]

the excluded constant/linear-offset Artin--Schreier family.

Therefore a surviving constructive route must use a polynomial transform of degree at least five, a genuinely multivariate construction, a more complicated rational transform, or a different extension.

## 8. Verification

`artin_schreier_low_degree_no_go_verify.py` checks the critical trace identities and the quadratic, cubic and quartic gates at all admitted primes below `200`.
