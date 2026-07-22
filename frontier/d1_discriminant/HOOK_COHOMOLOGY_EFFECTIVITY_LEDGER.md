# Exact hook-cohomology effectivity ledger

**Date:** 2026-07-22  
**Status:** exact consequence of the proved fixed-q local inertia and Grothendieck--Ogg--Shafarevich. It quantifies the remaining cancellation theorem. It does not prove or refute cancellation of common Frobenius factors across hooks.

## 1. Setup

For generic fixed `q`, let

`U=P^1_t minus {+1,-1,infinity}`

and let `Std=Perm_p-1` for the generic `S_p` root cover. Put

`V_i=exterior^i Std`,  `0<=i<=p-1`.

Then

`rank(V_i)=r_i=binomial(p-1,i)`

and

`Lambda_p=sum_i (-1)^i V_i`.

The exact fixed-q inertia proved elsewhere is:

- a transposition at each of `t=+1,-1`;
- `I_infinity=C_p semidirect C_((p-1)/2)`;
- one positive lower jump `j=(p-3)/2`.

Only the wild point enters the Euler characteristic.

## 2. C_p invariants of a hook

On restriction to the wild subgroup `C_p`, the standard representation is the sum of all nontrivial characters of `C_p`. Therefore `dim V_i^(C_p)` is the number of i-element subsets of `F_p^*` whose sum is zero.

A character average gives an exact closed form.

For the identity element, the exterior-power generating polynomial is

`(1+t)^(p-1)`.

For every nonidentity element of `C_p`, it is

`product_(r=1)^(p-1)(1+t zeta^r)`
` =(1+t^p)/(1+t)`
` =sum_(i=0)^(p-1)(-1)^i t^i.`

Hence:

### Theorem HCE.1

`boxed(a_i:=dim V_i^(C_p)`
` =(binomial(p-1,i)+(p-1)(-1)^i)/p.)`

## 3. Individual Swan conductors

With one lower jump, the Swan conductor is

`Swan_infinity(V_i)`
` = j * |C_p|/|I_infinity| * codim V_i^(C_p)`
` = (p-3)/(p-1) * (r_i-a_i).`

Thus:

### Theorem HCE.2

`boxed(s_i:=Swan_infinity(V_i)`
` =(p-3)/(p-1)`
`  *(binomial(p-1,i)`
`    -(binomial(p-1,i)+(p-1)(-1)^i)/p).)`

This expression is an integer for every i.

The alternating sum is

`sum_i (-1)^i s_i=-(p-3)`,

recovering the previously proved virtual Swan conductor of `Lambda_p`.

## 4. Exact individual middle-cohomology dimensions

Grothendieck--Ogg--Shafarevich on the three-punctured line gives

`chi_c(U_bar,V_i)=-r_i-s_i.`

Compactly supported `H^0` vanishes. The only hook with a global invariant is `V_0=1`, so

`dim H_c^2(U_bar,V_i)=1 if i=0, else 0.`

Therefore:

### Theorem HCE.3

`boxed(h_i:=dim H_c^1(U_bar,V_i)`
` =r_i+s_i+1_(i=0).)`

Every term is an actual nonnegative vector-space dimension.

## 5. Closed form for the raw effective size

Summing Theorem HCE.1 over i gives

`sum_i a_i=(2^(p-1)+p-1)/p`.

Consequently

`sum_i s_i=(p-3)(2^(p-1)-1)/p`.

Adding the ranks and the single `H_c^2` correction yields:

### Theorem HCE.4

`boxed(sum_(i=0)^(p-1) h_i`
` =((2p-3)2^(p-1)+3)/p.)`

This is asymptotic to `2^p`.

On the other hand,

`sum_i (-1)^i h_i=4-p`,

which is exactly the previously proved virtual middle-cohomology dimension.

Let

`H_even=sum_(i even)h_i`,

`H_odd=sum_(i odd)h_i`.

Then

`boxed(H_even=(H_total+4-p)/2,)`

`boxed(H_odd =(H_total-4+p)/2.)`

Both are exponential in p, while their difference is linear.

## 6. Interpretation

The fixed-q virtual collapse is now completely quantified:

- raw actual middle cohomology in the canonical hook model has total dimension
  `((2p-3)2^(p-1)+3)/p`;
- the alternating virtual dimension is only `4-p`.

Therefore Euler characteristic, virtual rank, and virtual conductor cannot by themselves yield an effective L-function bound. A crown proof must establish cancellation of Frobenius eigenvalues between the even-hook and odd-hook cohomologies after semisimplification.

The required cancellation is not merely polynomial bookkeeping: it removes all but `O(p)` effective degrees from two spaces whose dimensions are each asymptotic to `2^(p-1)`.

## 7. Precise surviving theorem

Let

`H_even(q)=direct_sum_(i even) H_c^1(U_bar,V_i)`,

`H_odd(q)=direct_sum_(i odd) H_c^1(U_bar,V_i)`.

The remaining fixed-q effectivity theorem is equivalent to proving that, after cancelling common semisimple Frobenius constituents between these two q-families, the uncancelled total rank and conductor are `O(p)`.

Equivalently, one needs a geometric correspondence or derived quasi-isomorphism pairing all but `O(p)` of the even and odd hook cohomology.

No such pairing is supplied by:

- the virtual GOS calculation;
- the rank-two Airy Fourier transform;
- the geometric cyclic diagonal;
- ordinary hook-by-hook Deligne bounds.

## 8. Strategic stopping point

The pre-cohomology Cyclic Airy shortcut is closed, and the post-cohomology burden is now exact:

`boxed(find an explicit parity-reversing pairing between hook cohomologies,`
`       with only O(p) unpaired vanishing cycles.)`

Absent such a pairing or an equivalent derived cancellation theorem, the constant virtual boundary conductor cannot be converted into a bounded numerator-plus-denominator degree.