# Cartier weighted filtration: dominant-block theorem and exact remaining gap

> **Superseded in part on 2026-07-22.** The dominant no-identity determinant theorem below remains exact. The filtered-minor lemma and the proposed full survivor-support law are refuted at `p=29`; see `CARTIER_SUBSTITUTION_MINOR_IDENTITY.md`, `P29_CARTIER_SUPPORT_COUNTEREXAMPLE.md`, and `D1_PUSH_PHASE_Y_STATUS_20260722.md`.

**Date:** 2026-07-22  
**Status:** exact theorem for the dominant Cartier block. The original reduction to a uniform support lemma is retained below for provenance, but that lemma is now known to be false.

## 1. The Cartier minor and the `w`-decomposition

Let

`F(X)=X^p+aX^3+cX+d`

over `F_p`, and let `M_3(F)` be the `(p-1) x (p-1)` minor of `I-H(F)` obtained by deleting row `p` and column `3`.

Write

`G(X)=aX^3+cX+d.`

The binomial expansion of `F^(p-1)` gives, for rows `1<=u<=p-1`,

`H_(u,v)=sum_(w=1)^min(4,u) (-1)^(p-1-u+w)`

`           [X^(pw-v)]G(X)^(p-1-u+w).`

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

`boxed( det A_p(G)`

`       =-c^(p(p-3)/2)d^(p-3)`

`          ((p-3)ad^2-c^3). )`

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

## 3. Weighted consequence for the no-identity block

Under `c->tc`, `d->t^2d`, Theorem CWFR.1 becomes

`det A_p(G_t)`

` =-c^(p(p-3)/2)d^(p-3)`

`   t^((p^2+p-6)/2)`

`   ((p-3)ad^2 t-c^3).`

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

the entire dominant no-identity block obeys the proposed support bound. The `p=29` counterexample comes from an identity-selected minor, not this evaluated block.

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

The already-proved grading law imposes, for an orthogonality survivor,

`sum i = 1 mod (p-1)/2.`

## 5. Original filtered-minor lemma — refuted

The original proposed statement was:

> For every prime `p>=5`, every admissible identity subset `S`, and every nonzero falling-factorial alternant arising from the `w=1,2,3,4` terms with `sum i = 1 mod (p-1)/2`, its total `(1,2)`-weight is at most `(p^2-1)/2`.

The individual-alternant version was first refuted at `p=23`: a weight-`286` assignment has nonzero alternant and nonzero individual contribution.

The strengthened grouped-coefficient version is also false. At `p=29`, omitted falling-factorial row values

`{1,2,4,5,7,8}`

and `I=43` give the orthogonality survivor

`a^43 c^224 d^112`

of weight `448>420`. The identity minor has coefficient `7 mod 29`, and after cofactor and row signs contributes `22 mod 29`.

An independent full-determinant Fourier extraction proves

`[c^224 d^112]det(I-H)=22a chi_29(a).`

The same coefficient occurs with `w=1` alone. Hence neither the dominant identity-selected support statement nor the full `w=1,2,3,4` support law is valid.

## 6. Correct algebraic replacement

For a fixed identity subset and degree set `M`, the factorial-weighted signed scalar is exactly a minor of the substitution matrix

`B_(q,m)=1/m! [X^q](X+X^3)^m.`

This follows from the matrix factorization and Cauchy-Binet identity proved in `CARTIER_SUBSTITUTION_MINOR_IDENTITY.md`.

It explains the complete grouped cancellation in the selected `p=17,19,23` examples, but the relevant substitution minors become nonzero at `p=29`.

## 7. Machine audits

The original audit constructs `A_p(G)` iteratively, computes its determinant over `F_p`, and checks CWFR.1 at four deterministic parameter triples for every prime `5<=p<=199`.

All `176` determinant comparisons pass exactly.

The superseding audits additionally verify:

- `p=17`: `476` assignments in `2` degree sets, both grouped scalars zero;
- `p=19`: `7,054` assignments in `5` degree sets, all grouped scalars zero;
- `p=23`: `332,192` assignments in `18` degree sets, all grouped scalars zero;
- `p=29`: `2,166,022,375` assignments in `2,177` degree sets, `15` nonzero grouped scalars, identity-minor coefficient `7 mod 29`;
- complete `p=29` coefficient `22a chi_29(a)` by exact Fourier inversion in two quadratic field models.

No floating point is used.

## 8. Epistemic classification

- `w`-decomposition: exact binomial expansion.
- Dominant no-identity determinant formula: exact theorem.
- Weighted degree and no-identity orthogonality consequence: exact.
- Identity-selected falling-factorial reduction: exact.
- Substitution-minor/Cauchy-Binet formula: exact.
- Original filtered-minor lemma: refuted.
- Full proposed Cartier support law: refuted at `p=29`.
- Evaluation or nonvanishing of the complete survivor sum: open.
- General function-field crown: open.
