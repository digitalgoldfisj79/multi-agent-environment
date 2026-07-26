# The p-cycle projector, fixed-point circularity, and exact q-line bridge

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** function-field Fortune at `d=1`; full four-parameter cubic-tail interval.  
**Status:** The projector, fixed-point, orbit-quantization, and q-line bridge statements below are **PROVED THEOREMS**. The displayed finite counts are **EXACT COMPUTER-ASSISTED THEOREMS**. The proposed primitive p-cycle direct-trace route is closed as an independent reduction: its target inequality is exactly equivalent to the crown.

## 0. Executive ruling

The alternating sum over all hook multiplicity spaces does collapse to one twisted Frobenius trace. The collapse is exact:

\[
\sum_{i=0}^{p-1}(-1)^i
\operatorname{Tr}(F\mid M_i)
=
\operatorname{Tr}(F\sigma\mid H^2_{\mathrm{prim}}(Y_p)),
\]

where `sigma` is a `p`-cycle and

\[
M_i=\operatorname{Hom}_{S_p}
(\wedge^i\operatorname{Std},H^2_{\mathrm{prim}}(Y_p)).
\]

However, the corresponding fixed-point count is exactly the original irreducible count:

\[
\boxed{\#\operatorname{Fix}(F\sigma\mid X_p)=pI_4+p.}
\]

Consequently the proposed one-sided primitive trace inequality is not a new analytic target. It is algebraically equivalent to

\[
I_4>p-1,
\]

which is the function-field `d=1` crown criterion.

The same calculation nevertheless gives a useful exact synthesis with the older normal-form and q-line programmes. If `N_2` is the quadratic normal-form count and `N_+`, `N_-` are the two depressed cubic square-class counts, then

\[
\boxed{
T_{\mathrm{mid}}
=p\left(
N_2+\frac{N_++N_-}{2}-(p+1+s_p)
\right).
}
\]

Equivalently, using the invariant q-line trace `S_0` and finite boundary counts `B_+`, `B_-`,

\[
\boxed{
T_{\mathrm{mid}}
=p\left(N_2-3-s_p+\frac{B_++B_-}{2}\right)
-\frac{S_0}{2}.
}
\]

Thus the aggregate direct-trace route and the invariant q-line route are the same arithmetic wall in two coordinate systems.

## 1. The alternating-hook projector is the p-cycle projector

Let `V` be a finite-dimensional `S_p`-representation over a characteristic-zero field, equipped with an endomorphism `F` commuting with `S_p`. Put

\[
M_i=\operatorname{Hom}_{S_p}(\wedge^i\operatorname{Std},V).
\]

Character projection gives

\[
\sum_i(-1)^i\operatorname{Tr}(F\mid M_i)
=
\frac1{p!}\sum_{g\in S_p}
\left(\sum_i(-1)^i\chi_{\wedge^i\mathrm{Std}}(g^{-1})\right)
\operatorname{Tr}(Fg\mid V).
\]

The parenthesized character is

\[
\det(1-g\mid\operatorname{Std}).
\]

If the cycle lengths of `g` are `lambda_1,...,lambda_r`, then

\[
\det(1-tg\mid\operatorname{Std})
=
\frac{\prod_j(1-t^{\lambda_j})}{1-t}.
\]

At `t=1` this vanishes unless `r=1`. For a `p`-cycle it equals `p`. Since the `p`-cycle class has `(p-1)!` elements and all its elements are conjugate,

\[
\boxed{
\sum_{i=0}^{p-1}(-1)^i\operatorname{Tr}(F\mid M_i)
=
\operatorname{Tr}(F\sigma\mid V).
}
\]

There is no missing factor of `p`: the character value `p`, class size `(p-1)!`, and projector denominator `p!` cancel exactly.

## 2. Work on the affine Sawin variety

Let

\[
X_p=\{e_1=\cdots=e_{p-4}=0\}\subset\mathbf A^p
\]

be Sawin's ordered-root variety for the full interval, and let

\[
\sigma=(1\ 2\ \cdots\ p).
\]

It is preferable to count fixed points on `X_p` directly. Passing first to the projective translation quotient introduces semilinear scaling and translation parameters that obscure, but do not change, the arithmetic count.

A point `x=(x_1,...,x_p)` fixed by `F\sigma` is determined by one element

\[
\alpha\in\mathbf F_{p^p}
\]

and the ordered list of its Frobenius conjugates. The associated monic polynomial is

\[
f_\alpha(T)=\prod_{j=0}^{p-1}(T-\alpha^{p^j}).
\]

The equations defining `X_p` say exactly that `f_alpha` belongs to the full cubic-tail interval.

Because `p` is prime, the degree of `alpha` over `F_p` is either `1` or `p`.

- If the degree is `p`, `f_alpha` is irreducible. Each irreducible polynomial contributes exactly `p` fixed ordered tuples, one for each choice of the first root.
- If the degree is `1`, every coordinate is the same `a in F_p`, and the polynomial is
  \[
  (T-a)^p=T^p-a.
  \]
  There are exactly `p` such fixed points.

Therefore:

### Theorem 2.1 — exact fixed-point count

\[
\boxed{
\#\operatorname{Fix}(F\sigma\mid X_p)=pI_4+p,
}
\]

where `I_4` is the number of irreducibles in the full four-parameter interval.

This is the same exact weighted identity as

\[
\sum_{f\in\mathcal I_4}\Lambda(f)=pI_4+p.
\]

The `p` exceptional points are precisely the degree-`p` prime powers `(T-a)^p`.

## 3. The primitive trace target is exactly the crown

Let

\[
S_{\mathrm{sgn}}=s_p p^2(p-1),
\qquad s_p\in\{0,+1,-1\},
\]

and let `T_mid` be the alternating Frobenius trace after removing the trivial and sign endpoints. The proved Sawin-cone transfer gives

\[
E_{\mathrm{mid}}=p(p-1)T_{\mathrm{mid}}.
\]

The exact full decomposition is

\[
pI_4+p=p^4+s_pp^2(p-1)+p(p-1)T_{\mathrm{mid}}.
\]

Solving for `T_mid` gives:

### Theorem 3.1 — fixed-point circularity identity

\[
\boxed{
T_{\mathrm{mid}}
=
\frac{I_4+1-p^3}{p-1}-s_pp.
}
\]

The proposed target was

\[
T_{\mathrm{mid}}>-p(p+1+s_p).
\]

Substitution gives

\[
T_{\mathrm{mid}}+p(p+1+s_p)
=
\frac{I_4-(p-1)}{p-1}.
\]

Hence:

### Corollary 3.2 — exact equivalence

\[
\boxed{
T_{\mathrm{mid}}>-p(p+1+s_p)
\iff I_4>p-1.
}
\]

The right-hand side is exactly the crown criterion. The sign residue class disappears from the final equivalence. Therefore a proof of the displayed trace inequality by merely rewriting the `F sigma` fixed points would be circular.

## 4. Orbit quantization

Let `N_2(p)` be the exact quadratic normal-form count from the affine-orbit theorem, so that the `a=0` sector contributes

\[
(p-1)+p(p-1)N_2.
\]

For `a nonzero`, translation uniquely removes the quadratic coefficient. For a fixed cubic coefficient of square class `A`, each of the `p` quadratic-coefficient slices is therefore bijective with the depressed family counted by `N_A`. There are `(p-1)/2` cubic coefficients in either square class. Thus:

### Theorem 4.1 — exact orbit decomposition

\[
\boxed{
I_4
=(p-1)+p(p-1)N_2
+\frac{p(p-1)}2(N_++N_-).
}
\]

Put

\[
W_p=N_2+\frac{N_++N_-}{2}.
\]

All three counts are nonnegative integers, and `N_++N_-` is even. Combining with Theorem 3.1 gives:

### Corollary 4.2 — primitive trace quantization

\[
\boxed{
T_{\mathrm{mid}}
=p\bigl(W_p-(p+1+s_p)\bigr).
}
\]

Equivalently,

\[
\boxed{
\frac{T_{\mathrm{mid}}}{p}+p+1+s_p=W_p\in\mathbf Z_{\ge0}.
}
\]

The crown is therefore equivalent to

\[
\boxed{W_p>0.}
\]

Failure would force the simultaneous exact vanishing

\[
N_2=N_+=N_-=0.
\]

This is a useful failure certificate, but it is not itself a proof that simultaneous vanishing cannot occur.

## 5. Exact bridge to the invariant q-line projector

The proved q-line ledger is

\[
N_A=(p-2)+B_A-\frac{S_0+A S_\chi}{2p}.
\]

Adding the two arithmetic classes eliminates the quadratic projector:

\[
N_++N_-
=2(p-2)+B_++B_- -\frac{S_0}{p}.
\]

Substitution into Corollary 4.2 yields:

### Theorem 5.1 — aggregate/q-line bridge

\[
\boxed{
T_{\mathrm{mid}}
=p\left(N_2-3-s_p+\frac{B_++B_-}{2}\right)
-\frac{S_0}{2}.
}
\]

The global aggregate p-cycle trace depends only on:

1. the quadratic normal-form count `N_2`;
2. the sum of the two finite boundary counts;
3. the invariant q-line trace `S_0`.

It is independent of the anti-invariant trace `S_chi`. This does not solve the problem: the one-sided bound on `S_0` needed to make `W_p>0` is exactly the previously isolated q-line error-versus-main-term problem.

Under hypothetical failure, the q-line traces would be forced to the extremal values

\[
S_0=p\bigl(2(p-2)+B_++B_-\bigr),
\qquad
S_\chi=p(B_+-B_-).
\]

Thus a valid nonsaturation or congruence theorem may target these exact extremal values. No such uniform theorem is presently proved.

## 6. The cubic Airy collapse is not this trace

The earlier cubic-hyperplane sum is

\[
T_p^{\mathrm{Airy}}
=
\sum_{\operatorname{Tr}(x)=0}
\psi(\operatorname{Tr}(x^3)).
\]

Its application normalization is

\[
p\rho_p
=\frac{T_p^{\mathrm{Airy}}}{p^{(p-3)/2}}.
\]

At `p=11`, one finds the exact coincidence

\[
p\rho_p=22=T_{\mathrm{mid}}.
\]

The coincidence is not uniform:

\[
\begin{array}{c|c|c}
p&T_{\mathrm{mid}}&p\rho_p\\ \hline
17&-17&29\\
23&-92&-561/23.
\end{array}
\]

In particular, at `p=23` the normalized Airy value is not even an integer while `T_mid` is divisible by `p`. Therefore the proposed direct identification of the primitive p-cycle trace with the normalized cubic Airy collapse is refuted. A more elaborate object-level relation is not logically excluded, but it would have to contain substantial complementary q-line trace.

## 7. Exact regression table

\[
\begin{array}{c|r|r|r|r|r|r}
p&I_4&N_2&N_+&N_-&T_{\mathrm{mid}}&W_p\\ \hline
5&124&1&4&6&0&6\\
7&426&1&10&8&7&10\\
11&1660&1&14&14&22&15\\
13&1572&2&10&6&-52&10\\
17&4640&1&18&14&-17&17\\
23&9636&2&12&22&-92&19
\end{array}
\]

For `p=11,17,23`, the independently committed q-line ledgers reproduce the same `T_mid` through Theorem 5.1.

## 8. Scientific ruling

### PROVED

1. The alternating hook projector is exactly the `p`-cycle projector.
2. The affine `F sigma` fixed-point count is `p I4+p`.
3. The proposed primitive trace threshold is exactly equivalent to the crown.
4. The primitive trace is quantized by the three nonnegative normal-form counts.
5. The aggregate primitive trace and invariant q-line trace satisfy Theorem 5.1.
6. The normalized cubic Airy trace is not uniformly equal to `T_mid`.

### CLOSED

1. Treating the `F sigma` fixed-point formula as a reduction of the crown to an easier trace inequality.
2. Identifying the `p=11` primitive trace with the normalized cubic Airy trace uniformly.
3. Re-entering the absolute-Betti route through the p-cycle projector.
4. Expecting the anti-invariant q-line projector `S_chi` to be required by the full aggregate trace.

### STILL OPEN

1. A theorem excluding `N_2=N_+=N_-=0` for every prime.
2. A one-sided invariant q-line theorem excluding the exact extremal value of `S_0`.
3. A new characteristic-`p` Frobenius-correlation or integral Smith-defect theorem that proves this nonsaturation without merely reconstructing the unknown count.
4. A genuinely different constructive or mass-formula proof.
5. The crown.

## 9. Verification

Run

```bash
python frontier/strategy/p_cycle_projector_fixed_point_bridge_verify.py
```

for exact character, normalization, ledger, Airy-comparison, and stored-census checks.

Compile and run

```bash
g++ -O3 -std=c++17 \
  frontier/strategy/p_cycle_fixed_point_census_verify.cpp \
  -o /tmp/p_cycle_census
/tmp/p_cycle_census --extended
```

for an exhaustive independent census at

\[
p=5,7,11,13,17,23.
\]

The C++ verifier uses the exact criterion for

\[
f(T)=T^p-g(T):
\]

absence of an `F_p` root together with `T^{p^p}=T mod f`. Since `p` is prime, these conditions force the only irreducible-factor degree to be `p`, and hence force `f` itself to be irreducible.
