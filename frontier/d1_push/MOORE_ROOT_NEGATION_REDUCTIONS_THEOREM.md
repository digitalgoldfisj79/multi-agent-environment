# Moore–Artin–Schreier and root-negation reductions

**Date:** 2026-07-23  
**Status:** exact for every prime `p>=5` and every `a in F_p^*`. These are algebraic equivalences; no asymptotic estimate is claimed.

## 1. Setup

Let

`K=F_(p^p)`,

and for `a in F_p^*` define

`F_(c,d)(X)=X^p+aX^3+cX+d`,

`N_a(p)=#{(c,d) in F_p^2 : F_(c,d) is irreducible over F_p}`.

Because `p` is prime, every element of `K\F_p` has degree exactly `p` over `F_p`.

## 2. Root incidences and the Moore determinant

Put

`R_a={(c,d,x) in F_p^2 x (K\F_p): F_(c,d)(x)=0}`.

Every irreducible member contributes its `p` conjugate roots, while any member having a root in `K\F_p` is the degree-`p` minimal polynomial of that root. Hence

### Theorem MRN.1 — root-incidence identity

`boxed(#R_a=p N_a(p).)`

For `x in K\F_p`, put

`y=x^p+a x^3`.

There is a unique `(c,d) in F_p^2` with `F_(c,d)(x)=0` if and only if

`y in span_(F_p){1,x}`.

The coefficient of `y` in any dependence among `1,x,y` is nonzero because `1,x` are independent. Therefore the condition is exactly the vanishing of the `3x3` Moore determinant

`M(x,y)=det[[1,x,y],[1,x^p,y^p],[1,x^(p^2),y^(p^2)]].`

## 3. One-variable semilinear reduction

For `u in K^*`, write

`v=u^p`, `w=u^(p^2)`,

and define

`Xi_a(u)`

`=[v^2-u w-a u v(2u^2+3uv+v^2)]/[3a u v(u+v)].`

### Lemma MRN.2 — denominator

For every `u in K^*`,

`3a u v(u+v) != 0`.

Indeed, only `u+v` requires proof. If `u^p=-u`, then `u^(p^2)=u`, so

`u in F_(p^2) intersect F_(p^p)=F_p`

because `gcd(2,p)=1`. Then `u^p=u=-u`; as `p` is odd, `u=0`, a contradiction.

### Lemma MRN.3 — linearized Moore determinant

Suppose `x^p-x=u`. Then

`x^p=x+u`,

`x^(p^2)=x+u+v`,

`x^(p^3)=x+u+v+w`.

Substituting `y=x^p+a x^3` into the Moore determinant gives exactly

`M(x,y)`

`=3a u v(u+v)x`

` +a u v(2u^2+3uv+v^2)+u w-v^2.`

Consequently

`M(x,y)=0 iff x=Xi_a(u).`

### Theorem MRN.4 — Moore–Artin–Schreier reduction

For every prime `p>=5` and `a in F_p^*`,

`boxed(p N_a(p)`

`=#{u in K^*: Xi_a(u)^p-Xi_a(u)=u}. )`

### Proof

Take a root incidence `(c,d,x) in R_a` and set `u=x^p-x`. Since `x notin F_p`, `u!=0`. The root condition is equivalent to `M(x,x^p+a x^3)=0`; Lemma MRN.3 therefore gives `x=Xi_a(u)`. By definition, `Xi_a(u)^p-Xi_a(u)=u`.

Conversely, suppose `u!=0`, put `x=Xi_a(u)`, and assume `x^p-x=u`. Then `x notin F_p`, and Lemma MRN.3 gives `M(x,x^p+a x^3)=0`. The Moore criterion implies

`x^p+a x^3 in span_(F_p){1,x}`.

Thus unique `c,d in F_p` satisfy `F_(c,d)(x)=0`. Since `x in K\F_p`, it has degree `p`, and the degree-`p` polynomial `F_(c,d)` is its minimal polynomial and is irreducible.

The two constructions are inverse because `u=x^p-x` determines `x` through the explicit formula `Xi_a(u)`. Combining with MRN.1 proves the count identity.

## 4. Root-negation quadratic descent

Put

`m=(p-1)/2`,

`H_c(Y)=Y^m+aY+c`,

and

`G_(c,e)(Y)=Y H_c(Y)^2-e`.

Then

`F_(c,d)(X)=X H_c(X^2)+d`.

Therefore

### Lemma MRN.5 — exact composition factorization

`boxed(G_(c,d^2)(X^2)=F_(c,d)(X)F_(c,-d)(X).)`

Moreover

`F_(c,-d)(X)=-F_(c,d)(-X)`,

so the two factors are simultaneously irreducible.

### Theorem MRN.6 — root-negation descent

For every `d!=0`,

`boxed(F_(c,d) irreducible over F_p`

` iff F_(c,-d) irreducible over F_p`

` iff G_(c,d^2) irreducible over F_p.)`

### Proof: forward direction

Assume `F_(c,d)` is irreducible and let `alpha` be a root. Then

`beta=alpha^2`

is a root of `G_(c,d^2)`. Since

`[F_p(alpha):F_p(beta)]<=2`

and `[F_p(alpha):F_p]=p` is odd, `beta` also has degree `p`. The monic polynomial `G_(c,d^2)` has degree

`1+2m=p`,

so it is the minimal polynomial of `beta` and is irreducible.

### Proof: reverse direction

Assume `G_(c,d^2)` is irreducible and let `beta` be a root in `F_(p^p)`. Since `d!=0`, the relation

`beta H_c(beta)^2=d^2`

implies `H_c(beta)!=0` and

`beta=(d/H_c(beta))^2`.

Set

`alpha=-d/H_c(beta)`.

Then `alpha^2=beta` and

`F_(c,d)(alpha)=alpha H_c(alpha^2)+d=0`.

Because `beta` has degree `p`, so does `alpha`; hence the degree-`p` polynomial `F_(c,d)` is irreducible.

The case `d=0` is excluded naturally: both `F_(c,0)` and `G_(c,0)` have the root zero.

### Corollary MRN.7 — exact count descent

Let `Sq_p^*` be the set of nonzero squares in `F_p`. Then

`boxed(N_a(p)`

`=2 #{(c,e) in F_p x Sq_p^* :`

`      Y(Y^((p-1)/2)+aY+c)^2-e is irreducible}. )`

Each `e in Sq_p^*` has exactly two square roots `+-d`, and MRN.6 identifies both with the same irreducible degree-`p` polynomial in `Y`.

## 5. Consequences and limitations

The two reductions are exact and complementary:

1. MRN.4 replaces the two-parameter irreducibility count by one semilinear equation over `F_(p^p)`.
2. MRN.6 replaces root-negation pairs by a degree-`p` polynomial in the square variable.
3. Both explain the evenness of `N_a(p)` without appealing to the earlier orbit theorem.
4. Neither theorem alone proves positivity or the bound `N_a=p+O(sqrt(p))`.

The remaining analytic-geometric task is to identify a fixed-complexity trace object for the primitive middle contribution exposed by these formulations.

## 6. Audit

`moore_root_negation_symbolic_audit.py` verifies:

- the exact Moore-determinant expansion and its linear coefficient in `x`;
- the formula for `Xi_a(u)`;
- the composition identity `G(X^2)=F_d(X)F_(-d)(X)`;
- exhaustive finite-field factorization equivalence for both square classes through a user-selected prime bound.
