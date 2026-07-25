# Local Airy--Adams cyclotomic initial term and maximal Galois orbit

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic `d=1` Airy wall, primes `p congruent 5 mod 6`.  
**Status:** **PROVED**.

## 1. Setup

Write

\[
p=3h+2=6r+5,
\qquad
e=h+1=\frac{p+1}{3}.
\]

Let `zeta` be a primitive `p`-th root of unity and put

\[
\pi=\zeta-1.
\]

For `u in F_p`, define the local cubic Airy trace

\[
t_u=-\sum_{x\in\mathbf F_p}\zeta^{x^3+ux}
\]

and its rank-two Adams trace

\[
f_p(u)=D_p(t_u,p),
\]

where the Dickson polynomial is characterized by

\[
D_p(\alpha+\beta,\alpha\beta)=\alpha^p+\beta^p.
\]

The repository already proves

\[
\sum_{u\in\mathbf F_p}f_p(u)=pT_p.
\]

## 2. Initial term of the local Airy trace

### Theorem 2.1

For every `u in F_p`,

\[
\boxed{
t_u
\equiv
\frac{u}{h!}\pi^e
\pmod{\pi^{e+1}}.}
\]

### Proof

Choose the standard representatives of the exponents in `{0,...,p-1}`. Since

\[
\zeta^y=(1+\pi)^y,
\]

the coefficient of `pi^k` in `t_u` is

\[
-\sum_{x\in\mathbf F_p}\binom{x^3+ux}{k}.
\]

For `k<e`, this is the sum of a polynomial in `x` of degree at most

\[
3k\le3(e-1)=p-2.
\]

Every monomial sum of degree below `p-1`, including the constant term, vanishes in `F_p`. Hence all coefficients below `pi^e` vanish.

For `k=e`, every lower term in the falling-factorial polynomial has `x`-degree at most `p-2`. Only the leading term

\[
\frac{(x^3+ux)^e}{e!}
\]

can contribute. Since

\[
3e=p+1,
\]

the unique term of `x`-degree `p-1` is obtained by choosing one factor `ux`:

\[
\frac{e u}{e!}x^{p-1}.
\]

Using

\[
\sum_{x\in\mathbf F_p}x^{p-1}=-1
\]

and the outer minus sign gives

\[
\frac{eu}{e!}=\frac{u}{(e-1)!}=\frac{u}{h!}.
\]

This proves the theorem.

## 3. Initial term after the Adams operation

### Theorem 3.1

The quotient `f_p(u)/p^e` is integral in the cyclotomic local ring and

\[
\boxed{
\frac{f_p(u)}{p^e}
\equiv
\frac{u}{h!}\pi^e
\pmod{\pi^{e+1}}.}
\]

### Proof

The Dickson polynomial has the explicit expansion

\[
D_p(X,p)
=
X^p+
\sum_{j=1}^{(p-1)/2}
\frac{p}{p-j}\binom{p-j}{j}(-p)^jX^{p-2j}.
\]

Theorem 2.1 gives `v_pi(t_u)>=e`. For `j>=1`, the `j`-th non-leading term has `pi`-valuation at least

\[
(j+1)(p-1)+(p-2j)e.
\]

Relative to the leading valuation `pe`, the difference is

\[
(p-1)+j((p-1)-2e)
=(p-1)+j(h-1)>0.
\]

Thus

\[
f_p(u)\equiv t_u^p\pmod{\pi^{pe+1}}.
\]

Moreover

\[
\frac{p}{\pi^{p-1}}\equiv-1\pmod\pi.
\]

Because `h` is odd, `e=h+1` is even, so

\[
\frac{p^e}{\pi^{e(p-1)}}\equiv1\pmod\pi.
\]

Dividing the leading term of `t_u^p` by `p^e` therefore leaves

\[
\left(\frac{u}{h!}\right)^p\pi^e
\equiv
\frac{u}{h!}\pi^e
\pmod{\pi^{e+1}}.
\]

## 4. Uniform distinctness and maximal real-cyclotomic degree

### Corollary 4.1

For distinct `u,v in F_p`,

\[
f_p(u)\ne f_p(v).
\]

Indeed, after division by `p^e`, their difference has nonzero initial coefficient

\[
\frac{u-v}{h!}\pi^e.
\]

### Corollary 4.2

For every `u!=0`,

\[
\boxed{
\mathbf Q(f_p(u))=\mathbf Q(\zeta_p)^+.
}
\]

In particular,

\[
\boxed{
[\mathbf Q(f_p(u)):\mathbf Q]=\frac{p-1}{2}.}
\]

### Proof

For `a in F_p^*`, let `sigma_a(zeta)=zeta^a`, and let `c` be the unique cube root of `a` in `F_p^*`. Rescaling `x` gives

\[
\sigma_a(t_u)=t_{c^2u},
\qquad
\sigma_a(f_p(u))=f_p(c^2u).
\]

The map `a -> c^2` has image the square subgroup and kernel `{1,-1}`. The values in that square-class orbit are pairwise distinct by Corollary 4.1, so the Galois orbit has size `(p-1)/2`. The trace is real: complex conjugation corresponds to `a=-1` and fixes `u`. Hence the generated field is exactly the maximal real cyclotomic subfield.

## 5. Consequences for the analytic programme

### Proved

1. Every nonzero local divided-Adams value has maximal possible real-cyclotomic orbit degree.
2. There is no nontrivial exact multiplicative period within either square-class orbit.
3. The previously observed real-cyclotomic rank `(p-1)/2` is uniform and structural, not a low-prime numerical pattern.
4. Any bounded-orbit, bounded-field-degree or fixed finite list of Gaussian-period values cannot represent the local trace function uniformly.

### Not proved

This theorem does not bound the complete sum

\[
\sum_u f_p(u)=pT_p.
\]

The leading local term is linear in `u` and cancels in the complete sum. The required estimate concerns the much deeper first surviving global coefficient. Thus maximal local orbit degree sharpens the correlation wall but does not solve it.

## 6. Programme ruling

A useful transfer theorem cannot rely on bounded local algebraic complexity: the local values already generate a field of degree `(p-1)/2`. Any surviving transfer mechanism must create global cancellation across this full Galois orbit, rather than compressing each value into a bounded collection of local periods.

## 7. Verification

`local_airy_adams_initial_verify.py` checks the exact cyclotomic coefficient statement and pairwise distinctness at the calibrated primes.
