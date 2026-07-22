# Configuration-degree cancellation at Frobenius-trace level

**Date:** 2026-07-22  
**Status:** exact theorem. It proves the complete cancellation of the large individual configuration-degree terms at each fixed `q`, but also proves that the resulting identity is exactly the original irreducibility detector. Thus configuration recursion alone supplies no new inequality for the crown.

## 1. Setup

Let `P` be the rank-`p` permutation representation on the roots of the fixed-`q` cover, and let

`G_sigma(u)=det(1+u sigma | P)=sum_(k=0)^p e_k(sigma)u^k`

for `sigma in S_p`. Here `e_k(sigma)=Tr(sigma|exterior^k P)`.

The weight-one configuration object from `CONFIGURATION_CURVE_RECURSION.md` is

`W_1(q)=sum_(k=2)^(p-1)(p-k)(-1)^k C_k(q)`.

## 2. The universal cycle identity

For every permutation `sigma`,

`pG_sigma(-1)+G_sigma'(-1)=sum_(k=0)^p(p-k)(-1)^k e_k(sigma).`

Every permutation has eigenvalue `1`, so `G_sigma(-1)=0`. The derivative can be nonzero only when the eigenvalue `1` has multiplicity one, equivalently when `sigma` consists of one cycle. Since the degree is the prime `p`, this means that `sigma` is a `p`-cycle. For a `p`-cycle,

`G_sigma(u)=1+u^p`, hence `G_sigma'(-1)=p`.

Therefore:

### Theorem CTC.1

`sum_(k=0)^p(p-k)(-1)^k e_k(sigma)=p * 1_(sigma is a p-cycle).`

Removing the `k=0,1` terms gives

`boxed( sum_(k=2)^(p-1)(p-k)(-1)^k e_k(sigma)
       =p*1_(p-cycle)-p+(p-1)X_1(sigma), )`

where `X_1(sigma)` is the number of fixed roots.

This identity holds on every fibre and in every extension degree.

## 3. Finite critical fibres

At `t=+/-1`, inertia is a transposition on the colliding pair. Let `rho` be arithmetic Frobenius on the remaining `p-2` roots and put

`E_rho(u)=det(1+u rho)`.

Averaging over the order-two inertia gives the invariant generating function

`(1/2)[(1+u)^2+(1-u^2)]E_rho(u)=(1+u)E_rho(u).`

Its full weighted value at `u=-1` is zero. After deleting `k=0,1`, the finite-boundary contribution is

`-1+(p-1)X_1(rho).`

If `f_+(q),f_-(q)` are the numbers of rational roots of the two residual degree-`p-2` critical factors, the combined finite-boundary contribution is

`-2+(p-1)(f_+(q)+f_-(q)).`

## 4. Infinity

Geometric inertia is

`I=C_p semidirect C_((p-1)/2)`

inside the affine group on `F_p`. For an arithmetic inertia coset, average CTC.1 over the coset.

- The geometric/even coset contains exactly the `p-1` nontrivial translations, all `p`-cycles. Its full weighted average is `2`.
- The odd coset contains no translation and hence no `p`-cycle. Its full weighted average is `0`.
- In either coset, the averaged trace on `P` is `1`.

After deleting `k=0,1`, the infinity contribution is therefore

`+1` on the even coset and `-1` on the odd coset.

This is exactly the arithmetic Kummer sign

`kappa_q=chi(u_q).`

### Diagnostic: the `C_3` infinity term

For `exterior^3 P`, the two coset traces are

`A_+(p)=(p+2chi(-3))/3-(1+chi(-1))/2,`

`A_-(p)=-(1-chi(-1))/2.`

Consequently the isolated `C_3` q-average contains a quadratic Tate-sized term, with leading value `-(p^2-1)/6`. This explains the exact scans: `C_3` is not individually an `O(p)` object. Its quadratic term cancels only after the configuration degrees are assembled.

## 5. Fixed-q assembly

Let `I(q)` be the number of irreducible degree-`p` fibres over `t in F_p\{+/-1}`. Let `R_U(q)` be the total number of rational roots above the unramified rational base points.

The root map has `p` rational source points, while the two critical fibres contain the double critical root and `f_+(q),f_-(q)` residual rational roots. Hence

`R_U(q)=p-2-f_+(q)-f_-(q).`

Summing CTC.1 over `t in U(F_p)`, subtracting the two finite-boundary terms and the infinity term, gives:

### Theorem CTC.2

`boxed( Tr(Frob_p | W_1(q))=p-pI(q)-kappa_q. )`

Adding the already-proved weight-zero survivor `kappa_q` recovers

`Tr(Frob_p | W_0(q)+W_1(q))=p-pI(q).`

Thus all configuration-degree Tate terms cancel exactly.

## 6. Strategic consequence

The configuration recursion is complete geometrically, and its large individual terms cancel exactly at trace level. However CTC.2 is not a new bound: it is algebraically identical to the original irreducibility detector.

Therefore the following route is closed without a materially new ingredient:

- estimating or classifying `C_3,C_4,...` separately and hoping their assembly automatically proves positivity;
- treating the quadratic term of `C_3` as an independent obstruction;
- using the configuration generating function alone as a substitute for the crown estimate.

A useful configuration-space advance would now have to provide extra structure beyond the trace identity, such as positivity, a pairing with controlled signs, or an independent bound on the remaining primitive trace.

## 7. Epistemic classification

- Cycle-polynomial identity: exact elementary theorem.
- Finite inertia averaging: exact.
- Affine-inertia coset count: exact.
- Fixed-q trace assembly: exact.
- New inequality for `I(q)`: not obtained.
- General function-field crown: open.
