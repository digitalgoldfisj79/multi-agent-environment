# Exact low-degree factor-mass ledger for the depressed cubic slice

**Date:** 2026-07-22  
**Status:** exact assembly of the factor-degree 1, 2 and 3 masses. Degree-one formulas are elementary refinements of the previously proved cubic-tail rootless theorem; degree-two and degree-three inputs are the new Phase-Z theorems. The ledger does not yet control all reducible members.

## 1. Setup

Fix prime `p>=5`, `a!=0`, and

`F_(c,d)(X)=X^p+aX^3+cX+d`.

Let

`L(c,d)=#{linear factors over F_p}`,  
`Q_2(c,d)=#{monic irreducible quadratic factors}`,  
`Q_3(c,d)=#{monic irreducible cubic factors}`.

All sums below are over `(c,d) in F_p^2`.

## 2. Complete linear-factor distribution

For `x in F_p`,

`F_(c,d)(x)=a x^3+(c+1)x+d.`

As `(c,d)` vary, this is the complete two-parameter family of depressed cubics with fixed nonzero leading coefficient. Hence `0<=L<=3`.

The factorial moments are elementary.

### First moment

For each pair `(x,c)`, there is a unique `d` making `x` a root. Therefore

`sum L=p^2.`

### Second factorial moment

For every unordered pair of distinct roots `{x,y}`, subtraction determines uniquely

`c+1=-a(x^2+xy+y^2),`

`d=a xy(x+y).`

Thus

`sum binom(L,2)=binom(p,2).`

### Third factorial moment

Three distinct roots of a depressed cubic satisfy

`x+y+z=0`.

The number of ordered pairs `(x,y)` for which `x,y,-x-y` are pairwise distinct is

`p^2-(3p-2)=(p-1)(p-2).`

Dividing by `3!` gives

`sum binom(L,3)=(p-1)(p-2)/6.`

Since `L<=3`, the full distribution follows.

### Theorem LFM.1 — linear-root distribution

`boxed( #{L=0}=(p^2-1)/3, )`

`boxed( #{L=1}=(p^2-p+2)/2, )`

`boxed( #{L=2}=p-1, )`

`boxed( #{L=3}=(p-1)(p-2)/6. )`

The first formula is the previously proved exact rootless count; the remaining three refine it to the complete distribution.

## 3. Quadratic-factor masses

From `QUADRATIC_FACTOR_MASS_THEOREM.md`:

`boxed( sum Q_2=p(p-1)/2, )`

`boxed( sum binom(Q_2,2)=binom((p-chi(a))/2,2), )`

`boxed( sum LQ_2=p(p-1)/2. )`

The last identity is equivalently

`boxed( sum (L-1)Q_2=0. )`

Using the linear distribution, this gives the exact balance

`sum_(L=0)Q_2=sum_(L=2)Q_2+2sum_(L=3)Q_2.`

Thus quadratic-factor incidence on rootless members is exactly balanced by the excess linear-root incidence among members with two or three roots.

The remaining quadratic third factorial moment is the explicit additive correlation `T_3(a,p)` described in QFM.3; it determines the complete `Q_2` multiplicity distribution.

## 4. Cubic-factor mass

From `CUBIC_FACTOR_MASS_THEOREM.md`:

`boxed( sum Q_3=(p^2-1)/3. )`

This value is independent of `a`. It is obtained by one satisfying degree-three root in each of the `p^2-1` additive translation orbits, followed by division by the three roots of each irreducible cubic.

The value coincides numerically with `#{L=0}`, but no bijection between rootless members and cubic-factor incidences is asserted. Cubic factors can occur with multiplicity, as the exact audit already shows.

## 5. Random-permutation comparison made exact at first order

The normalized first moments are

`(1/p^2)sum L=1,`

`(1/p^2)sum Q_2=(p-1)/(2p),`

`(1/p^2)sum Q_3=(p^2-1)/(3p^2).`

They approach

`1, 1/2, 1/3`,

which are the cycle-count means for cycles of lengths `1,2,3` in a random permutation. Here these are exact finite-field mass formulas with explicit lower-order corrections, not a probabilistic assumption.

This rigorously identifies the first three local factors of the singular-series model.

## 6. Why the crown does not yet follow

A reducible degree-p polynomial has a factor of degree at most `(p-1)/2`. The present ledger controls only degrees `1,2,3`.

Moreover, first moments do not determine the union of factor loci. To obtain a rigorous sieve lower bound for irreducibles one needs:

1. higher factorial moments within each factor degree;
2. mixed moments between different degrees;
3. uniform control as the factor degree grows with `p`;
4. or an exact cycle-index identity whose remainder has a controlled sign.

The next low-degree exact targets are

`sum binom(Q_3,2),`

`sum LQ_3,`

`sum Q_2Q_3.`

The oriented-discriminant surface in CFM.2 and the six-line correlation in QFM.3 are the precise geometric objects for these moments.

## 7. Epistemic classification

- Complete linear-factor distribution: exact elementary theorem.
- Quadratic first, second and linear-mixed moments: exact theorem.
- Cubic first incidence: exact theorem.
- Random-permutation comparison: interpretation of exact formulas.
- Higher mixed/factor-degree masses: open.
- Singular-series positivity: open.
- Function-field d=1 crown: open.
