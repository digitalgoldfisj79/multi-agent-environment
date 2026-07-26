# Secondary Hattori–Stallings trace and the Artin–Schreier root-cycle quotient

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** fixed nonzero cubic slices in the function-field Fortune `d=1` programme.  
**Status:** the Hattori–Stallings coefficient formula, cyclic-transfer construction, Artin–Schreier quotient, reciprocal three-subset model, no-split theorem and finite resolvent obstruction below are **PROVED**. Rational-point existence on the resulting quotient remains **OPEN**. The crown is not proved.

## 1. Arithmetic slice

Fix an odd prime `p>=5` and `a in F_p^*`. Put

\[
f_{a,c,d}(X)=X^p+aX^3+cX+d
\]

and

\[
N_a=\#\{(c,d)\in\mathbf F_p^2:f_{a,c,d}\text{ irreducible}\},
\qquad
M_a=\sum_{f_{a,c,d}\text{ irreducible}}c\pmod p.
\]

Let `X_a` be the ordered-root slice with coordinates

\[
(x_0,\ldots,x_{p-1})
\]

and equations

\[
e_1=\cdots=e_{p-4}=0,
\qquad e_{p-3}=a,
\qquad e_{p-2}=0.
\]

The remaining symmetric functions are

\[
e_{p-1}=c,
\qquad e_p=-d.
\]

Let

\[
\sigma(x_i)=x_{i+1}
\]

with indices modulo `p`.

## 2. The root-cycle action is free

A nonidentity element of `C_p=<sigma>` generates the full cyclic group. If it fixes an ordered tuple, all coordinates are equal to some `r`. Then

\[
e_{p-3}=\binom p3 r^{p-3}=0
\]

in characteristic `p`, contradicting `e_{p-3}=a!=0`.

### Theorem 2.1 — free nonzero cubic slice

The action of `C_p` on `X_a` is free for every `a!=0`.

Consequently the affine quotient

\[
Y_a=X_a/C_p
\]

is a finite étale `C_p` quotient in the root-cycle direction.

## 3. Hattori–Stallings divided trace

Let

\[
A=\mathbf Z[C_p].
\]

For a bounded finite free `A`-complex `P` and an `A`-linear endomorphism `Phi`, let

\[
h_\Phi=\sum_{r=0}^{p-1}h_r\sigma^r\in A
\]

be its alternating Hattori–Stallings trace. Since `C_p` is abelian, no commutator quotient changes this expression.

### Theorem 3.1 — exact coefficient extraction

For every `r`,

\[
\boxed{
\operatorname{Tr}_{\mathbf Z}(\Phi\sigma^{-r}\mid P)=p h_r.
}
\]

Hence

\[
\boxed{
h_r=\frac1p
\operatorname{Tr}_{\mathbf Z}(\Phi\sigma^{-r}\mid P).}
\]

This is the canonical integral divided trace at a fixed root-cycle element. It does not require the nonexistent virtual character `Theta_p/p`.

**Proof.** Write `Phi` as a matrix over `A`. The Hattori–Stallings trace is the sum of its diagonal group-ring entries. On the regular lattice, multiplication by `sigma^j`, followed by `sigma^{-r}`, has ordinary trace `p` when `j=r` and zero otherwise. Summing the diagonal entries proves the formula. `□`

If the normalizer of `C_p` acts and all nonidentity coefficients are equal to `h_*`, then augmentation gives

\[
\operatorname{Tr}(\Phi\mid P_{C_p})
=h_0+(p-1)h_*.
\]

Since

\[
h_0=\frac1p\operatorname{Tr}_{\mathbf Z}(\Phi\mid P),
\]

we obtain:

### Corollary 3.2 — quotient-defect formula

\[
\boxed{
h_*
=
\frac{
\operatorname{Tr}(\Phi\mid P_{C_p})
-\operatorname{Tr}_{\mathbf Z}(\Phi\mid P)/p
}{p-1}.}
\]

This constructs the secondary trace functional that the preceding tangent audit had isolated abstractly.

## 4. Bi-equivariant coefficient tangent

Include the additive coefficient group `C_coeff`. For a bi-equivariant trace

\[
h_\Phi=\sum_{r,s}h_{r,s}\sigma^r\tau^s,
\]

first extract any fixed nonidentity root coefficient `r`, then evaluate

\[
\tau\mapsto\zeta_p=1+\pi.
\]

The expansion

\[
\sum_s h_{r,s}\zeta_p^s
=
\sum_s h_{r,s}
+
\pi\sum_s s h_{r,s}
+O(\pi^2)
\]

shows that the first coefficient Bockstein is

\[
\sum_s s h_{r,s}\pmod p.
\]

On the ordered-root fixed locus this recovers

\[
N_a+\pi M_a\pmod{\pi^2}.
\]

Thus the secondary carrier exists algebraically. The remaining issue is whether its geometric local terms yield a non-tautological nonvanishing theorem.

## 5. A global cyclic transfer

Every `(p-3)`-subset of `F_p` has a free orbit under translation because `p` is prime and

\[
0<p-3<p.
\]

Choose one representative from every orbit and put

\[
t=\sum_{S\text{ representative}}
\prod_{i\in S}x_i.
\]

Then

\[
\boxed{
\operatorname{Tr}_{C_p}(t)
=
\sum_{j=0}^{p-1}\sigma^j(t)
=e_{p-3}=a.}
\]

The number of monomial representatives is

\[
\frac1p\binom p3
=
\frac{(p-1)(p-2)}6.
\]

Define

\[
U=\sum_{j=0}^{p-1}j\,\sigma^j(t).
\]

Reindexing modulo `p` gives

\[
(\sigma-1)U=-\operatorname{Tr}_{C_p}(t)=-a.
\]

Hence

\[
\boxed{y=-U/a}
\]

satisfies

\[
\boxed{\sigma(y)=y+1.}
\]

### Theorem 5.1 — explicit Artin–Schreier quotient

The function

\[
\boxed{g=y^p-y}
\]

is `C_p`-invariant. The quotient map `X_a -> Y_a` is globally represented in the root-cycle direction by the Artin–Schreier equation

\[
\boxed{T^p-T=g.}
\]

The construction is trace-surjective: `t/a` has cyclic trace `1`.

## 6. Frobenius shift and irreducibility

Let `z in Y_a(F_p)` and choose `x` over `z`. There is a unique

\[
r\in\mathbf F_p
\]

with

\[
F(x)=\sigma^r x.
\]

Because `y` is defined over `F_p`,

\[
y(x)^p=y(Fx)=y(\sigma^r x)=y(x)+r.
\]

Therefore

\[
\boxed{g(z)=r.}
\]

For `r!=0`, the tuple is a full Frobenius orbit of an element of degree `p`. Conversely an irreducible polynomial gives, after quotienting cyclic rotations, exactly one rational quotient point for each `r in F_p^*`.

Put

\[
C_{a,r}=\{g=r\}\subset Y_a.
\]

### Theorem 6.1 — exact quotient-level irreducibility section

For every `r!=0`, projection to `(c,d)` gives a bijection

\[
\boxed{
C_{a,r}(\mathbf F_p)
\longleftrightarrow
\{(c,d):f_{a,c,d}\text{ irreducible}\}.}
\]

In particular,

\[
\boxed{N_a=\#C_{a,1}(\mathbf F_p)}
\]

and

\[
\boxed{
M_a=
\sum_{z\in C_{a,1}(\mathbf F_p)}c(z)\pmod p.}
\]

This is the point-level local-term formula for the secondary trace.

## 7. Reciprocal three-subset model

On the irreducible locus `d!=0`. Put

\[
z_i=x_i^{-1}.
\]

Since `e_p(x)=-d`,

\[
e_3(z)
=
\frac{e_{p-3}(x)}{e_p(x)}
=-\frac ad.
\]

Choose one representative from every cyclic orbit of triples and set

\[
t_3=
\sum_{S\text{ triple representative}}
\prod_{i\in S}z_i.
\]

Then

\[
\operatorname{Tr}_{C_p}(t_3)=e_3(z)=-a/d.
\]

For

\[
U_3=\sum_jj\sigma^j(t_3)
\]

we have

\[
(\sigma-1)U_3=a/d.
\]

Therefore

\[
\boxed{y=(d/a)U_3}
\]

again satisfies `sigma(y)=y+1`.

This replaces `(p-3)`-fold root monomials by reciprocal triple monomials, but it does not produce a bounded-degree equation in the coefficient variables: multiplying by `d` returns products of the complementary `p-3` roots.

## 8. No split torsors for p>5

The identity coefficient `r=0` would correspond to a polynomial in the slice that splits completely over `F_p`.

Suppose

\[
f=X^p+aX^3+cX+d,
\qquad a!=0,
\]

splits over `F_p`. For `x in F_p`,

\[
f(x)=a x^3+(c+1)x+d.
\]

Hence all distinct roots of `f` lie among the roots of one nonzero cubic. Let

\[
R=\prod_{\alpha\text{ distinct root of }f}(X-\alpha).
\]

Then

\[
\deg R\le3.
\]

Writing the logarithmic derivative in reduced form gives

\[
\frac{f'}f=\frac PR,
\qquad P!=0,
\]

because

\[
f'=3aX^2+c
\]

is nonzero. Thus

\[
\boxed{f'R=Pf.}
\]

The left side has degree at most `5`, while the right side has degree at least `p`. Therefore `p<=5`.

### Theorem 8.1 — no-split-torsor theorem

For every prime

\[
\boxed{p>5}
\]

and every `a!=0`,

\[
\boxed{X_a(\mathbf F_p)=\varnothing.}
\]

At `p=5` the boundary is sharp:

\[
X^5+X^3=X^3(X-2)(X+2),
\]

\[
X^5+2X^3+X=X(X-2)^2(X+2)^2.
\]

Since the `r=0` quotient fibre is empty and every nonzero fibre has `N_a` points:

### Corollary 8.2 — quotient point-count formula

For `p>5`,

\[
\boxed{
\#Y_a(\mathbf F_p)=(p-1)N_a.}
\]

Equivalently,

\[
\boxed{
N_a=rac{\#Y_a(\mathbf F_p)}{p-1}.}
\]

Thus the identity/free-orbit subtraction in the Hattori–Stallings formula vanishes completely on the actual nonzero cubic slice.

## 9. What this gains—and what it does not

The secondary-trace milestone has passed in a precise sense:

1. the divided root-cycle coefficient is an explicit Hattori–Stallings coefficient;
2. the coefficient tangent is its ordinary first cyclotomic derivative;
3. the root-cycle quotient has an explicit global Artin–Schreier coordinate;
4. the `g=1` level is exactly the irreducibility section;
5. the split `g=0` level is empty for every `p>5`.

However, the remaining point-existence statement is still

\[
\boxed{Y_a(\mathbf F_p)!=\varnothing}
\]

or equivalently

\[
\boxed{C_{a,1}(\mathbf F_p)!=\varnothing.}
\]

General Artin–Schreier or trace-surjective structure cannot force this. For example,

\[
g(x)=x^p-x
\]

is nonconstant but equals zero at every `x in F_p`; its level `g=1` has no `F_p` point. More generally, modular Galois/trace-surjective extensions permit essentially arbitrary invariant rings. Any proof must use the special sparse symmetric geometry of `X_a`, not the existence of the Artin–Schreier coordinate alone.

## 10. Exact low-degree resolvent probe

The most immediate possible gain was that eliminating the cyclic coordinate might produce a uniformly low-degree relation in `(c,d)`, or after the involution `d -> -d`, in `(c,u=d^2)`.

An exact finite-field linear-algebra probe found the smallest total degree of any nonzero polynomial vanishing on every irreducible point:

| `p` | class | degree in `(c,d)` | dimension-forced degree | degree in `(c,d^2)` | dimension-forced degree |
|---:|:---:|---:|---:|---:|---:|
| 5 | + | 2 | 2 | 1 | 1 |
| 5 | - | 2 | 3 | 2 | 2 |
| 11 | + | 4 | 4 | 3 | 3 |
| 11 | - | 4 | 4 | 3 | 3 |
| 17 | + | 5 | 5 | 3 | 3 |
| 17 | - | 4 | 4 | 3 | 3 |
| 23 | + | 4 | 4 | 3 | 3 |
| 23 | - | 5 | 6 | 4 | 4 |
| 29 | + | 7 | 8 | 5 | 5 |
| 29 | - | 6 | 7 | 4 | 4 |

By `p=29`, no total-degree-at-most-three relation survives even after passing to `d^2`; the square class requires degree `5`. Except for the two direct `p=5` cases, every first relation also vanishes at additional `F_p` points not corresponding to irreducibles.

### Ruling 10.1 — low-degree elimination is closed

The first plane equations track the interpolation threshold set by the number of points and do not isolate the irreducibility locus. The quotient does not collapse to a uniform conic, cubic or similarly bounded plane curve.

This does not prove that no useful high-degree compactification exists. It closes only the proposed immediate simplification through a bounded-degree coefficient resolvent.

## 11. Decisive status

### Proved in this phase

1. The exact Hattori–Stallings divided coefficient formula.
2. Its normalizer quotient-defect form.
3. The bi-equivariant first coefficient tangent.
4. Freeness of the root-cycle action on every `a!=0` slice.
5. The explicit cyclic transfer and Artin–Schreier coordinate.
6. The exact `g=1` irreducibility-section theorem.
7. The reciprocal three-subset formula.
8. The no-split-torsor theorem for every `p>5`.
9. The quotient identity `#Y_a(F_p)=(p-1)N_a`.
10. The finite obstruction to a uniformly low-degree plane resolvent.

### Still open

1. A proof that `Y_a(F_p)` is nonempty for at least one cubic square class.
2. A geometry-specific local-term formula that forces that nonemptiness.
3. Uniform nonvanishing of `M_a` or `N_a mod p`.
4. The function-field `d=1` crown.

### Exact next theorem

The only surviving continuation of this route is:

> **Sparse quotient rational-point theorem.** Use the defining sparse symmetric complete intersection—not generic Artin–Schreier theory—to prove that at least one of the two quotient surfaces `Y_+`, `Y_-` has an `F_p`-point for every admitted prime.

Equivalently, prove that one level scheme `C_{a,1}` has an `F_p` point. A proof that only reconstructs the fixed-point count, the q-line ledger or the first Cartier moment is circular.

## 12. Verification

Run:

```bash
python frontier/strategy/secondary_hattori_stallings_trace_verify.py
python frontier/strategy/root_cycle_transfer_artin_schreier_verify.py
python frontier/strategy/split_torsor_log_derivative_verify.py
python frontier/strategy/artin_schreier_resolvent_degree_probe.py
```

Frozen outputs:

- `secondary_hattori_stallings_trace_results_20260726.json`;
- `root_cycle_transfer_artin_schreier_results_20260726.json`;
- `split_torsor_log_derivative_results_20260726.json`;
- `artin_schreier_resolvent_degree_results_20260726.json`.
