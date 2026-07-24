# The critical `k=p` Haessig resonance: exact two-divisor audit

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-haessig-kp-resonance-20260724`  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** the coefficient-matrix and denominator statements below are **PROVED**. Their use in a Frobenius trace estimate remains **OPEN**.

## 0. Result

Haessig's effective decomposition for odd symmetric power `k<p` fails for the first time at `k=p`. The failure is more structured than the phrase “the denominators cease to be units” suggests.

After removing the common `pi` and parameter-power growth factors from the Airy connection matrix, the critical coefficient operator is

\[
H_p q_i=(p-i)q_{i+1}+i q_{i-1},
\qquad 0\le i\le p,
\]

with missing terms omitted.

The exact `p`-local statement is

\[
\boxed{
\operatorname{SNF}_{\mathbf Z_{(p)}}(H_p)
=
\operatorname{diag}
(\underbrace{1,\ldots,1}_{p-1},p,p)
}
\]

up to multiplication of diagonal entries by `p`-adic units.

Equivalently:

1. `rank(H_p mod p)=p-1`;
2. `v_p(det H_p)=2`;
3. the boundary resonance has exactly two elementary `p`-divisors.

This does **not** mean that only two columns of Haessig's reduction are affected. Both elementary divisors occur at terminal endpoints of the two parity chains, and elimination through those endpoints broadcasts a `1/p` loss into every sufficiently deep column reduction. Thus:

\[
\boxed{
\text{two-dimensional integral resonance}
\quad\text{and}\quad
\text{full-column propagation}
}
\]

are simultaneously true.

This resolves an apparent tension between the modular rank-two Adams sequence and the previously proved full-rank characteristic-zero lift defect. They are different statements at different levels.

## 1. Source formulas

Use Haessig's basis

\[
q_i=v^{p-i}w^i,\qquad 0\le i\le p,
\]

for the `p`-th symmetric power of the cubic Airy differential module. The connection is

\[
\partial_p=a\frac d{da}-G_p,
\]

where

\[
G_pq_i=\pi a(p-i)q_{i+1}
-\frac{\pi a^2}{3}i q_{i-1}.
\]

For the arithmetic obstruction, the factors `pi`, `a`, and `-a/3` belong to the already tracked growth bookkeeping. The integer coefficient skeleton is `H_p` above.

Haessig's Lemma 6.4 reduces odd and even columns recursively. For `k<p`, every rational coefficient used there is a `p`-adic unit. At `k=p`, the terminal step in each parity chain reaches exactly one factor `p`.

The rising-factorial convention is

\[
(c)_m=c(c+1)\cdots(c+m-1).
\]

## 2. PROVED: rank modulo `p`

Modulo `p`,

\[
H_pq_0=0,\qquad H_pq_p=0.
\]

Hence the kernel has dimension at least two.

Now take the internal minor on rows and columns indexed by

\[
q_1,\ldots,q_{p-1}.
\]

It is a zero-diagonal tridiagonal matrix of even size `p-1`. Its determinant has the unique perfect-matching product. Modulo `p` this determinant is

\[
(-1)^{(p-1)/2}
\prod_{j=1}^{(p-1)/2}(2j)(2j-1)
=
(-1)^{(p-1)/2}(p-1)!.
\]

Wilson's theorem gives

\[
(-1)^{(p-1)/2}(p-1)!\ne0\pmod p.
\]

In fact the value is a sign, so the minor is a unit modulo `p`. Therefore

\[
\boxed{\operatorname{rank}_{\mathbf F_p}(H_p)=p-1.}
\]

Thus exactly two Smith factors are divisible by `p`.

## 3. PROVED: determinant valuation

The full matrix has even size `p+1`, zero diagonal, and a unique perfect matching

\[
(q_0,q_1),(q_2,q_3),\ldots,(q_{p-1},q_p).
\]

Up to sign,

\[
\det H_p
=
\prod_{j=0}^{(p-1)/2}(p-2j)(2j+1).
\]

Among the factors `p-2j`, exactly the first is divisible by `p`. Among the factors `2j+1`, exactly the last is divisible by `p`. No factor is divisible by `p^2`. Hence

\[
\boxed{v_p(\det H_p)=2.}
\]

Since exactly two Smith factors are non-units and their total valuation is two, each has valuation one. This proves the stated `p`-local Smith form.

## 4. PROVED: exact denominator locations in Lemma 6.4

### 4.1 Odd-column high-degree branch

For a column indexed by `2j+1`, Haessig's high-degree reduction contains

\[
\frac{1}{2\pi(j+\tfrac12)_m},
\qquad
1\le m\le\frac{p+1}{2}-j.
\]

Ignoring the powers of two, the integer denominator is

\[
\prod_{t=0}^{m-1}(2j+1+2t).
\]

For

\[
m<\frac{p+1}{2}-j,
\]

the largest factor is below `p`, so the denominator is a `p`-adic unit. At the terminal value

\[
m=\frac{p+1}{2}-j,
\]

the last factor is exactly `p`, occurring once. Therefore every odd-column chain encounters precisely one `1/p` loss, and only at its terminal elimination.

### 4.2 Even-column branch

For the even column indexed by `2j`, the reduction contains

\[
\frac{1}{\pi(\tfrac p2-j+1)_{m+1}},
\qquad
0\le m\le j-1.
\]

Ignoring powers of two, its integer denominator is

\[
\prod_{t=0}^{m}(p-2j+2+2t).
\]

For `m<j-1`, every factor is strictly between `0` and `p`. At the terminal value `m=j-1`, the last factor is exactly `p`, occurring once.

Thus every even-column chain also encounters precisely one `1/p` loss, only at its terminal backward elimination.

## 5. Reconciliation with the existing full-rank defect theorem

The repository already proves that the natural characteristic-zero lift

\[
P_p:\operatorname{Sym}^p\longrightarrow
\det\otimes\operatorname{Sym}^{p-2}
\]

has connection defect

\[
P_p\partial_p-\partial_{p-2}P_p
=
-p\pi aJ_p+\frac{p(p-1)\pi a^2}{3}E_p,
\]

and that the principal defect projects with full rank onto the target primitive cohomology, including after the exact `mu_3` projection.

There is no contradiction:

- the Smith calculation concerns the intrinsic integral resonance of the single matrix `G_p`;
- the full-rank theorem concerns the failure of a characteristic-zero cross-symmetric-power lift to intertwine two different differential modules;
- a rank-two modular kernel can generate a full-rank lifted cohomology defect after recursive elimination and division by the two terminal `p`-factors.

The present result therefore **does not reopen** the closed bounded-cone version of the Adams-lift route.

## 6. What this changes

### PROVED

1. The first `k=p` obstruction in Haessig's effective decomposition is not an uncontrolled collection of bad denominators.
2. It is generated by exactly two elementary `p`-divisors.
3. Every bad recursive coefficient is the propagation of one of these two endpoint divisors.
4. Any resonance-corrected Dwork decomposition needs exactly two additional integral generators before Frobenius closure.

### NOT proved

1. The two-generator resonance module need not be Frobenius-stable.
2. Its Frobenius orbit or mapping cone may still have rank growing with `p`.
3. It does not imply the observed valuation
   \[
   v_p(T_p)=\frac{p+4}{3}.
   \]
4. It does not imply the archimedean target
   \[
   |T_p|\le C p^{(p-1)/2}.
   \]
5. It does not provide the separate Airy-to-irreducibility application bridge.

## 7. Exact next theorem

The next justified Dwork task is now finite and explicit.

### OPEN resonance-corrected Frobenius theorem

Construct an integral, completed effective decomposition at `k=p` of the form

\[
M^{(p)}_a
=
V_p+\partial_pM^{(p)}_a+\mathcal R_p,
\]

where `mathcal R_p` is generated integrally by two endpoint resonance classes, and determine the Frobenius closure of `mathcal R_p` after projection to the exact `mu_3` trace sector.

The useful outcomes would be one of:

1. **valuation theorem:** prove that the resonance filtration forces
   \[
   v_p(T_p)=\frac{p+4}{3};
   \]
2. **bounded trace block:** identify the normalized quotient
   \[
   T_p/p^{(p+4)/3}
   \]
   as the trace of a uniformly bounded Frobenius block;
3. **failure certificate:** prove that Frobenius generates a linearly growing block, closing this refined Dwork route.

Only the second outcome would directly approach the required absolute archimedean bound. The first would still be a genuine theorem but is insufficient alone.

## 8. Verification

`haessig_kp_resonance_verify.py` independently checks:

- `rank(H_p mod p)=p-1`;
- `v_p(det H_p)=2`;
- the unique terminal non-unit in every odd-column chain;
- the unique terminal non-unit in every even-column chain.

The script uses only exact integer arithmetic and no third-party packages. Testing multiple primes is a regression check of closed formulas, not empirical support for the theorem.
