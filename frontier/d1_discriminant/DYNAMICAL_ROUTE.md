# Constructive dynamics for the d=1 function-field Fortune problem

**Date:** 2026-07-21  
**Status:** exact equivalence proved; two broad but elementary construction templates eliminated.

## 1. Exact equivalence

Let `p` be prime, let `g in F_p[X]` have degree `< p`, and set

\[
f_g(X)=X^p-g(X).
\]

### Theorem DY.1

The polynomial `f_g` is irreducible of degree `p` over `F_p` if and only if there exists a root `alpha` of

\[
\alpha^p=g(\alpha)
\]

having exact composition period `p` under `g`:

\[
g^{\circ p}(\alpha)=\alpha,
\qquad
g^{\circ k}(\alpha)\ne\alpha\quad(1\le k<p).
\]

### Proof

Because the coefficients of `g` lie in `F_p`, induction gives

\[
\alpha^{p^k}=g^{\circ k}(\alpha).
\]

If `f_g` is irreducible, then `[F_p(alpha):F_p]=p`; hence the least positive `k` for which `alpha^{p^k}=alpha` is `p`, proving exact `g`-period `p`.

Conversely, exact `g`-period `p` says that the least positive `k` for which `alpha^{p^k}=alpha` is `p`. Therefore `alpha` has degree `p` over `F_p`. Its minimal polynomial divides the degree-`p` polynomial `f_g`, so the two coincide and `f_g` is irreducible.

For the Fortune-relevant cubic family,

\[
g(X)=-aX^3-bX^2-cX-d.
\]

A single explicit family `g_p` with a certified Frobenius-compatible orbit of exact period `p` would therefore prove the d=1 function-field target.

## 2. Fixed-point obstruction

### Lemma DY.2

If `g` has a fixed point `r in F_p`, then `f_g` is reducible.

Indeed,

\[
f_g(r)=r^p-g(r)=r-r=0.
\]

Any constructive family must therefore make `g(X)-X` rootless over `F_p`. In the depressed cubic slice, this is exactly the already identified rootless-tail condition.

## 3. Complete classification of affine attempts

Let

\[
g(X)=uX+v.
\]

### Theorem DY.3

The only irreducible affine examples are the Artin--Schreier polynomials

\[
X^p-X-v,
\qquad v\ne0.
\]

They correspond to constant offsets and are excluded from the nonconstant Fortune problem.

### Proof

If `u != 1`, then `g` has the `F_p`-fixed point

\[
r=\frac{v}{1-u},
\]

so `f_g` is reducible by Lemma DY.2.

If `u=1` and `v=0`, then `f_g=X^p-X` splits over `F_p`. If `u=1` and `v != 0`, then

\[
f_g=X^p-X-v
\]

is the standard Artin--Schreier polynomial. Over `F_p`, the Artin--Schreier irreducibility criterion is `Tr_{F_p/F_p}(v)=v != 0`, so it is irreducible of degree `p`. Its offset from `X^p-X` is the constant `-v`.

Thus affine dynamics recovers exactly the trivial constant-offset solution and nothing Fortune-relevant.

## 4. No global rational semiconjugacy from Artin--Schreier translation

A natural idea is to start with the known period-`p` translation

\[
\tau(X)=X+1
\]

and seek a rational change or quotient `R` producing a quadratic or cubic map `g`:

\[
R(X+1)=g(R(X)).
\]

This cannot work globally.

### Theorem DY.4

Let `R in F_p(X)` be nonconstant and suppose `g in F_p(X)` satisfies

\[
R(X+1)=g(R(X))
\]

as a rational-function identity. Then `g` has rational degree `1`.

### Proof

The translation automorphism `tau:X -> X+1` stabilises the subfield

\[
K=F_p(R)\subset F_p(X),
\]

because `tau(R)=g(R)` lies in `K`. Since `tau` has finite order, the inclusion `tau(K) subset K` is equality. Hence `tau` induces an automorphism of the rational function field `K`.

Relative to the generator `R`, every `F_p`-automorphism of `K=F_p(R)` is a Möbius transformation. Therefore

\[
g(Y)=\frac{aY+b}{cY+d}
\]

and has degree `1`.

### Consequence

No global rational conjugacy, quotient, or semiconjugacy of the Artin--Schreier translation can produce the required nonlinear quadratic or cubic `g`. Any successful construction must be genuinely fibre-specific -- for example, an identity only modulo `X^p-X-v` -- or arise from a different dynamical mechanism.

## 5. Common exceptional-map templates

The most obvious low-degree exceptional maps also fail immediately when they possess an `F_p`-fixed point. Examples include

\[
g(X)=X^2,
\qquad g(X)=X^3,
\]

and the standard Dickson/Chebyshev normalisations with an `F_p`-rational fixed point. Their `F_p`-affine conjugates retain an `F_p`-fixed point and therefore give reducible `X^p-g(X)`.

This does not eliminate all quadratic or cubic dynamics. It eliminates the standard algebraic-group templates in their direct and affine-conjugate forms.

## 6. Revised assessment of the constructive route

The constructive route is logically decisive, but the easy source of a period-`p` orbit -- Artin--Schreier translation -- cannot be converted globally into a nonlinear Fortune-relevant map. The route should therefore be divided into two programmes:

1. **Fibre-specific semiconjugacy.** Seek `R_p` and cubic `g_p` satisfying
   \[
   R_p(X+1)\equiv g_p(R_p(X))\pmod{X^p-X-v},
   \]
   without requiring a rational-function identity. The congruence may exploit the single Artin--Schreier fibre and evade Theorem DY.4.

2. **Direct dynatomic factor construction.** Seek a cubic `g_p` for which the degree-`p` polynomial `X^p-g_p(X)` can be exhibited as a factor of the exact period-`p` dynatomic polynomial, together with a degree argument excluding lower periods.

The first is the cleaner computational target. It can be formulated as a sparse polynomial-congruence search and tested against the existing certified witnesses. A successful low-complexity pattern would then require proof; failure across broad ansatz classes would provide a principled negative result rather than undirected coefficient search.

## 7. Immediate next experiment

For each certified irreducible witness `f_g`, choose a root `alpha` and an Artin--Schreier generator `beta` with `beta^p=beta+1` in the same field. Interpolate the unique polynomial `R_p` of degree `<p` satisfying

\[
R_p(\beta+i)=g^{\circ i}(\alpha),
\qquad i\in F_p.
\]

Then measure whether the coefficient support of `R_p` is systematically sparse, concentrated in a small number of binomial-basis terms, or controlled by `p` modulo a small modulus. This is not Monte Carlo: it is an exact structural diagnostic of whether the witness dynamics is a disguised fibre-specific Artin--Schreier semiconjugacy.