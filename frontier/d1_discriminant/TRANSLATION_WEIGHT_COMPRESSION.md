# Translation-weight compression of the depressed cubic slice

**Date:** 2026-07-21  
**Status:** exact orbit identities proved; cofactor coefficient evaluation remains open.

## 1. Full cubic family

Fix `p>=5` and `a!=0`. Consider

`F_(a,b,c,d)(X)=X^p+aX^3+bX^2+cX+d`.

Translation `X->X+t` preserves irreducibility and acts on coefficients by

`b_t=b+3at`,

`c_t=c+2bt+3at^2`,

`d_t=d+(c+1)t+bt^2+at^3`.

Every orbit has size p and contains a unique depressed representative with `b=0`. Starting from that representative `(0,c0,d0)`,

`b_t=3at`,

`c_t=c0+3at^2`,

`d_t=d0+(c0+1)t+at^3`.

Thus the irreducible translation orbits are in bijection with the irreducible members of the depressed family, and their number is `N_a(p)`.

## 2. General orbit-weight lemma

Let `W(b,c,d)=b^r c^s d^u` with nonnegative integers satisfying

`r+2s+3u=p-1`.

On a translation orbit, `W(b_t,c_t,d_t)` is a polynomial in t of degree exactly p-1. Its leading coefficient is

`(3a)^r(3a)^s a^u`.

Every lower positive power has exponent below p-1, and the constant term sums to p=0 in `F_p`. Since

`sum_(t in F_p)t^k=0` for `0<=k<p-1`,

and

`sum_t t^(p-1)=-1`,

one obtains the exact orbit identity

`boxed(sum_t b_t^r c_t^s d_t^u=-(3a)^(r+s)a^u.)`

This is independent of the depressed representative.

Consequently

`sum_(b,c,d) b^r c^s d^u 1_(F irreducible)`

`=-(3a)^(r+s)a^u N_a(p)`.

## 3. Minimal-degree choices

The total ordinary degree `r+s+u` is minimised by using the cubic d-coordinate as much as possible.

### Case p congruent to 1 modulo 3

Put

`m=(p-1)/3`.

Take `(r,s,u)=(0,0,m)`. Then

`boxed(sum_(b,c,d)d^m 1_irr=-a^m N_a(p).)`

Using the constant Cartier cofactor

`C_3(F)=3a 1_irr`,

this becomes

`boxed(sum_(b,c,d)d^m C_3(F)=-3a^(m+1)N_a(p).)`

### Case p congruent to 2 modulo 3

Put

`k=(p-2)/3`, so `1+3k=p-1`.

Take `(r,s,u)=(1,0,k)`. Then

`boxed(sum_(b,c,d)b d^k 1_irr=-3a^(k+1)N_a(p).)`

The column-two Cartier cofactor is

`C_2(F)=2b 1_irr`.

Therefore

`boxed(sum_(b,c,d)d^k C_2(F)=-6a^(k+1)N_a(p).)`

In both congruence classes the depressed count is represented by a full coefficient-space sum with an external weight of degree at most `(p-1)/3`.

## 4. Canonical coefficient targets

Let `C_j^can(a;b,c,d)` be the canonical polynomial function, degree at most p-1 in each of b,c,d, representing the selected Cartier cofactor.

Finite-field orthogonality gives:

### p congruent to 1 modulo 3

`sum d^m C_3 = -[b^(p-1)c^(p-1)d^(p-1-m)]C_3^can`.

Hence

`boxed([b^(p-1)c^(p-1)d^(2(p-1)/3)]C_3^can=3a^(m+1)N_a(p).)`

### p congruent to 2 modulo 3

`sum d^k C_2 = -[b^(p-1)c^(p-1)d^(p-1-k)]C_2^can`.

Hence

`boxed([b^(p-1)c^(p-1)d^((2p-1)/3)]C_2^can=6a^(k+1)N_a(p).)`

These are crown-equivalent coefficients but are less extreme in d than the original complete-plane top coefficient.

## 5. Strategic value

This compression does not prove nonvanishing by itself. Its value is structural:

1. translation replaces the hard condition `b=0` by a low-degree orbit weight;
2. the full cubic coefficient space allows orthogonality in b,c,d simultaneously;
3. the selected cofactor changes with the congruence class so that its own coefficient supplies the missing leading translation factor;
4. the external weight has minimal possible ordinary degree among monomial orbit projectors.

The next target is to compute the displayed canonical coefficient directly from the full Cartier alternant and determine whether its extremal occupation pattern is unique or has a controlled signed family.
