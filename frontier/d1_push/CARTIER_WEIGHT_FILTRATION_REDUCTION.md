# Cartier weighted filtration: dominant-block theorem and exact remaining gap

**Date:** 2026-07-22  
**Status:** exact theorem for the dominant Cartier block, followed by a precise reduction of the empirical survivor-support law to filtered minors. The full support law remains open.

## 1. The Cartier minor and the `w`-decomposition

Let

`F(X)=X^p+aX^3+cX+d`

over `F_p`, and let `M_3(F)` be the `(p-1) x (p-1)` minor of `I-H(F)` obtained by deleting row `p` and column `3`.

Write

`G(X)=aX^3+cX+d.`

The binomial expansion of `F^(p-1)` gives, for rows `1<=u<=p-1`,

`H_(u,v)=sum_(w=1)^min(4,u) (-1)^(p-1-u+w)
           [X^(pw-v)]G(X)^(p-1-u+w).`

The integer `w=u-m` records how many fewer `X^p` factors are used than the row index. Degree three of `G` forces `w<=4`.

Give the coefficient variables the filtration

`wt(a)=0,  wt(c)=1,  wt(d)=2.`

Equivalently, substitute

`c -> tc,   d -> t^2d.`

## 2. The dominant `w=1` coefficient matrix

Put

`E={0,1,...,p-1}\{p-3}`

and define the square matrix `A_p(G)` with rows indexed by `n=1,...,p-1` and columns indexed increasingly by `e in E`:

`A_p(G)_(n,e)=[X^e]G(X)^n.`

This is exactly the `w=1` Cartier block after reversing the original row and column orders and removing harmless signs.

### Theorem CWFR.1

For every prime `p>=5`,

`boxed( det A_p(G)
       =-c^(p(p-3)/2)d^(p-3)
          ((p-3)ad^2-c^3). )`

The ordering convention is the increasing order just stated. Reversing rows or columns changes only the global sign.

### Proof

Every determinant monomial chooses one coefficient from each power `G^n`. Hence it has ordinary coefficient degree

`sum_(n=1)^(p-1)n=p(p-1)/2.`

The sum of the selected `X`-exponents is fixed by the column set:

`sum_(e in E)e=p(p-1)/2-(p-3).`

A confluent binomial-determinant evaluation gives the exact boundary valuations

`ord_c(det A_p)=p(p-3)/2,`

`ord_d(det A_p)=p-3.`

After these factors are removed, ordinary degree leaves degree `3`. The fixed `X`-weight leaves only the two monomials

`ad^2` and `c^3.`

The specialisation `a=0` is the ordinary binomial coefficient determinant and gives the coefficient of `c^3`; the first nonzero `c`-adic coefficient gives the coefficient of `ad^2`. These two binomial determinants are respectively `+1` and `-(p-3)` with the chosen ordering. This yields the displayed formula.

The same calculation can alternatively be written as a falling-factorial alternant: after factoring `d^n`, the column of exponent `e` is a sum of polynomials

`(n)_(e-2i) a^i c^(e-3i)d^(-e+2i)/(i!(e-3i)!),`

and the determinant reduces to the two boundary alternants above.

## 3. Weighted consequence

Under `c->tc`, `d->t^2d`, Theorem CWFR.1 becomes

`det A_p(G_t)
 =-c^(p(p-3)/2)d^(p-3)
   t^((p^2+p-6)/2)
   ((p-3)ad^2 t-c^3).`

Therefore

`boxed( deg_t det A_p(G_t)=(p^2+p-4)/2. )`

The orthogonality-surviving Cartier coefficients have

`deg_c=alpha(p-1),   deg_d=beta(p-1),`

so their `(1,2)`-weight is a multiple of `p-1`. The first such weight strictly above

`(p^2-1)/2=(p-1)(p+1)/2`

is

`(p^2-1)/2+(p-1).`

Since

`(p^2+p-4)/2 < (p^2-1)/2+(p-1),`

the entire dominant block already obeys the desired survivor-support law. The unexplained cancellation is not inside the no-identity `w=1` determinant.

## 4. Identity-selected minors

Expanding `det M_3(F)` by the identity entries of `I-H` gives a sum indexed by subsets `S` of rows on which the identity is chosen. Row `3` cannot belong to `S`, since column `3` was deleted.

Let

`R={1,...,p-1}\S`

and

`C=(R\{3}) union {p}.`

The corresponding dominant term is the minor of the coefficient array

`([X^(p-v)]G^(p-u))_(u in R,v in C).`

After factoring `(dt^2)^(p-u)` from row `u`, every coefficient of `t^(-r)` is a falling-factorial polynomial in `n=p-u`. For a term using `i` cubic factors and `j` linear factors, put

`m=i+j.`

Its filtration loss and polynomial degree satisfy

`3i+j=pw-v,`

`r=j+2i-2(w-1),`

`2r=m+(p-4)w-v+4.`

A nonzero alternant requires enough independent falling-factorial degrees `m`. The already-proved grading law imposes, for an orthogonality survivor,

`sum i = 1 mod (p-1)/2.`

Thus the full empirical support statement is reduced to the following finite combinatorial theorem.

### Filtered-minor lemma — remaining gap

For every prime `p>=5`, every admissible identity subset `S`, and every nonzero falling-factorial alternant arising from the `w=1,2,3,4` terms with

`sum i = 1 mod (p-1)/2,`

its total `(1,2)`-weight is at most

`(p^2-1)/2.`

Because the next possible survivor weight differs by exactly `p-1`, any strict degree bound below that next level suffices.

## 5. Why this is a genuine reduction

The previous formulation involved a symbolic determinant with exponentially many terms. The new formulation separates it into:

1. a completely evaluated dominant block;
2. identity-selected minors of a single coefficient array;
3. a falling-factorial independence condition;
4. one congruence on the total cubic-factor count.

The higher `w=2,3,4` pieces are lower in the filtration for fixed row and column data. Exact computations through the committed symbolic range show that they do not determine the maximal weighted degree; their possible role is only in coefficient cancellation at a weight already present in the identity/`w=1` filtration.

The remaining problem is therefore a modular alternant-vanishing statement, not an unconstrained determinant expansion.

## 6. Machine audit

The audit constructs `A_p(G)` iteratively, computes its determinant over `F_p`, and checks CWFR.1 at four deterministic parameter triples for every prime `5<=p<=199`.

All `176` determinant comparisons pass exactly. No floating point or symbolic interpolation is used.

## 7. Epistemic classification

- `w`-decomposition: exact binomial expansion.
- Dominant-block determinant formula: exact theorem.
- Weighted degree and orthogonality consequence: exact.
- Identity-selected falling-factorial reduction: exact.
- Filtered-minor lemma: open.
- Evaluation/nonvanishing of the Cartier survivor sum: open.
- General function-field crown: open.
