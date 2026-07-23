# Wild trace-cubic reduction: Artin–Schreier coordinates, null quadric and cubic Kummer sectors

**Date:** 2026-07-23  
**Status:** exact algebraic theorem for every prime `p>=5`. The characteristic-`p` zero-frequency trace model is reduced to one explicit cubic on the null cone of a nondegenerate quadratic form. All nonuniformity is supported there. On nonzero cubic values the trace function is constant on cube classes, so its multiplicative Fourier support contains only the characters of order dividing three. The sizes of those Frobenius coefficients remain to be bounded uniformly.

## 1. Artin–Schreier generator

Let

`K=F_(p^p)`

and choose `theta in K` with

`theta^p-theta=1`.

Then `K=F_p(theta)` and arithmetic Frobenius acts by

`theta -> theta+1`.

Every `x in K` has a unique expression

`x=sum_(j=0)^(p-1) a_j theta^j`,  `a_j in F_p`.

For a polynomial `F(theta)` of degree below `p`,

`Tr_(K/F_p)(F(theta))=sum_(s in F_p) F(theta+s).`

Using

`sum_(s in F_p) s^k=0`

unless `k>0` is divisible by `p-1`, in which case the sum is `-1`, together with Lucas' theorem, gives the trace-power table needed below:

- `Tr(theta^n)=0` for `0<=n<p-1`;
- `Tr(theta^(p-1))=-1`;
- `Tr(theta^n)=0` for `p<=n<=2p-3`;
- `Tr(theta^(2p-2))=Tr(theta^(2p-1))=-1`;
- `Tr(theta^n)=0` for `2p<=n<=3p-4`.

The value at `3p-3` is also `-1`, but it is not reached by the cube of a trace-zero element of degree at most `p-2`.

## 2. Trace-zero coordinates

The linear trace is

`Tr(x)=-a_(p-1)`.

Hence on the trace-zero hyperplane we set `a_(p-1)=0` and write

`x=a_0+sum_(j=1)^(p-2) a_j theta^j`.

Put

`Q_2(x)=Tr(x^2)`,  `Q_3(x)=Tr(x^3)`.

The trace-power table gives:

### Theorem WTCK.1 — exact quadratic form

`boxed(Q_2=-sum_(i+j=p-1) a_i a_j.)`

The variable `a_0` does not occur. On

`W=span{a_1,...,a_(p-2)}`

the associated bilinear form is nondegenerate; it is the anti-diagonal trace pairing. Thus the radical of `Q_2` on the full trace-zero space is exactly the translation line `F_p*1`.

For the cubic, define on `W`

`C_p(a_1,...,a_(p-2))`

`=-sum_(i+j+k=p-1) a_i a_j a_k`

` -sum_(i+j+k=2p-2) a_i a_j a_k`

` -sum_(i+j+k=2p-1) a_i a_j a_k`,

where every index lies in `{1,...,p-2}`.

Then:

### Theorem WTCK.2 — translation-linear cubic

`boxed(Q_3=3 a_0 Q_2+C_p.)`

Equivalently, for every `t in F_p`,

`Q_3(x+t)=Q_3(x)+3t Q_2(x)`.

## 3. Exact orbit cancellation

Translation by `F_p` acts freely on the trace-zero hyperplane and preserves `Q_2`.

If `Q_2(x)!=0`, the map

`t -> Q_3(x+t)`

is an affine bijection of `F_p`. Therefore every translation orbit with nonzero `Q_2` contributes exactly once to every cubic value.

### Corollary WTCK.3 — null-cone localization

Let

`N_b=#{x in K:Tr(x)=0,Tr(x^3)=b}`.

Then

`boxed(N_b-p^(p-2)`

` =p[ M_b-(1/p)sum_c M_c ],)`

where

`M_b=#{w in W:Q_2(w)=0,C_p(w)=b}.`

Thus all deviation from perfect uniformity is confined to the intersection of one nondegenerate quadric with one explicit cubic in `p-2` variables.

## 4. Cubic scaling and Kummer support

For `s in F_p^*`,

`Q_2(sw)=s^2Q_2(w)`,

`C_p(sw)=s^3C_p(w)`.

Hence on the null cone,

`M_(s^3 b)=M_b`.

### Corollary WTCK.4 — cubic Kummer reduction

On `F_p^*`, the function

`b -> N_b-p^(p-2)`

is constant on cubic residue classes.

Consequently its multiplicative Fourier expansion contains only:

- the trivial character;
- when `p=1 mod 3`, the two nontrivial cubic characters.

The value at `b=0` is a separate punctual term.

For `p=2 mod 3`, cubing is a permutation of `F_p^*`, so all nonzero values are equal and the entire trace function is a combination of the constant function and the punctual delta at zero.

This is an exact fixed-complexity statement about the **support of the trace function**. It does not by itself bound the Frobenius multiplicity carried by a cubic Kummer sector.

## 5. Degree-two L-function recurrence

For `u,v in F_p`, let

`S_r(u,v)=sum_(x in F_(p^r)) psi(Tr_(F_(p^r)/F_p)(u x+v x^3)).`

For `v!=0`, the cubic additive-sum L-function has degree two. Write its inverse roots as `alpha_(u,v), beta_(u,v)`. Then

`S_r(u,v)=-(alpha^r+beta^r).`

The first two sums determine

`P_1=alpha+beta=-S_1`,

`P_2=alpha^2+beta^2=-S_2`,

`E_2=alpha beta=(P_1^2-P_2)/2`,

and the exact recurrence

`P_r=P_1 P_(r-1)-E_2 P_(r-2)`.

Fourier inversion gives

`boxed(N_b-p^(p-2)`

` =p^(-2) sum_(v!=0,u) psi(-vb) S_p(u,v).)`

This computes every `N_b` using only fields of sizes `p` and `p^2`, rather than enumerating `p^p` elements.

## 6. Exact examples

The recurrence gives:

- `p=5`: `N_b=5^3` for every `b`;
- `p=7`: after division by `7^2`, the deviations are
  `[12,-1,-7,2,2,-7,-1]`;
- `p=11`: after division by `11^4`, the deviations are
  `[20,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]`.

For larger primes the value at zero can grow substantially, while the nonzero values remain arranged in at most three cubic residue classes exactly as WTCK.4 predicts.

## 7. Consequence for the Fortune endpoint

The relevant nearby Milnor fibre is nonzero, so the large punctual value `b=0` must not be conflated with the primitive nonzero-fibre local term. The nonzero-fibre term lies entirely in the constant/cubic-Kummer sectors.

The remaining proof task is to:

1. identify which constant line is already included in the main/Tate and Artin–Schreier ledger;
2. bound the two cubic-character Frobenius coefficients after the correct weight normalization;
3. compare those coefficients with the two escaping endpoint sections.

This is narrower than a general wild characteristic-class calculation.

## 8. Epistemic classification

### Exact

- Artin–Schreier coordinate system;
- trace-power table through the required range;
- explicit quadratic and cubic trace forms;
- perfect translation cancellation off `Q_2=0`;
- reduction to a cubic on a nondegenerate null quadric;
- cubic-residue/Kummer support on nonzero values;
- degree-two L-function recurrence and exact small-prime values.

### Open

- uniform bound for the normalized cubic-character coefficients;
- exact matching with endpoint/main/AS subtractions;
- zero-frequency primitive conductor bound and crown.
