# M3 execution: depth-two crown detection and the limit of slope-only arguments

Date: 28 July 2026

## 1. A new exact depth-two reformulation

Paper VI proves

`#Q_p(F_p)=1+(p-1)W_p`,

where

`W_p=N_2+(N_sq+N_ns)/2`.

The paper observes that congruence modulo `p` is blind: positive cases can satisfy `#Q_p(F_p) congruent 1 mod p`. At depth two the situation changes completely.

### Lemma 1: uniform range

For every prime `p>3`,

`0 <= W_p <= p^2-1`.

### Proof

In the quadratic family, `d=0` gives

`X^p+X^2=X^2(X^{p-2}+1)`,

so it is reducible. Hence `N_2<=p-1`.

In either depressed cubic class, `d=0` gives

`X^p+aX^3+cX=X(X^{p-1}+aX^2+c)`,

so it is reducible for every `c`. Therefore each fixed-class count satisfies

`N_a<=p(p-1)`.

It follows that

`W_p <= (p-1)+p(p-1)=p^2-1`.

### Theorem 2: depth-two detection theorem

For every prime `p>3`,

`W_p=0  <=>  #Q_p(F_p) congruent 1 mod p^2`.

Equivalently, the function-field `d=1` crown is exactly

`#Q_p(F_p) not congruent 1 mod p^2`.

Moreover, the integer `W_p` is recovered from the depth-two point count by

`W_p = ((#Q_p(F_p)-1)*(p-1)^(-1)) mod p^2`,

where the residue is taken in `{0,...,p^2-1}`.

### Proof

Since `gcd(p-1,p^2)=1`, multiplication by `p-1` is invertible modulo `p^2`. Thus

`#Q_p(F_p) congruent 1 mod p^2`

is equivalent to `W_p congruent 0 mod p^2`. Lemma 1 places `W_p` in the complete residue interval `0<=W_p<p^2`, so this is equivalent to `W_p=0`.

### Significance

This is stronger than the heuristic statement that `W_p` appears to be of order `p`. No statistical upper bound is required. Depth-two information is unconditionally sufficient because the parameter-space count itself gives the sharp range `W_p<p^2`.

The case `p=17`, where `W_17=17` and the mod-`p` point count is blind, is detected immediately modulo `p^2`:

`#Q_17(F_17)=273`,

which is `1 mod 17` but not `1 mod 17^2`.

## 2. What a p-adic proof must now establish

A successful p-adic route need not estimate the full integer point count. It is sufficient to compute or constrain the compactly supported Frobenius trace modulo `p^2` strongly enough to prove

`#Q_p(F_p) != 1 mod p^2`.

This makes Witt vectors of length two, rigid cohomology modulo `p^2`, or a slope-`<2` trace formula logically load-bearing rather than merely suggestive.

The exact target is a **noncongruence**, not a generic Newton-polygon statement.

## 3. Slopes alone remain insufficient

### Proposition 3: Newton-polygon blindness

The multiset of Frobenius slopes, even together with the assertion that a unit-root part is nonzero, does not determine the relevant trace coefficient.

### Proof

Consider rank-two `F`-crystals with Frobenius matrices

`diag(1,1)` and `diag(1,-1)`

over `Z_p`, with `p>2`. Both have Newton slopes `{0,0}` and the same unit-root rank. Their traces are respectively `2` and `0`. More generally, unit eigenvalues can vary without changing the Newton polygon, and their traces can cancel.

Therefore a theorem saying merely that some family member is ordinary, nonsupersingular, or has a nonzero unit-root subspace does not imply a nonzero Cartier moment, a nonzero depth-two trace, or `W_p>0`.

## 4. Corrected p-adic programme

Paper VI already provides an exact existence certificate:

`M_a != 0 => N_a>0 => W_p>0`.

The missing p-adic comparison is one of the following precise forms:

1. identify `M_a` with the reduction modulo `p` of a specified unit-root Frobenius trace and prove that trace nonzero in one arithmetic class; or
2. compute `#Q_p(F_p) mod p^2` directly from a length-two Witt/rigid-cohomology complex and prove it is not `1`; or
3. prove a family trace identity whose depth-two coefficient equals `(p-1)W_p` and cannot vanish.

A census of Newton polygons should be run only after one such comparison is constructed. Without it, the census can measure geometric variation while remaining logically disconnected from the crown.

## 5. Ruling

M3 survives, but in a sharper form:

- **live:** depth-two Frobenius trace or an exact unit-root coefficient comparison;
- **closed:** nonzero unit-root rank, generic ordinarity, or Newton slopes by themselves.

The new exact target is

`#Q_p(F_p) not congruent 1 mod p^2`.
