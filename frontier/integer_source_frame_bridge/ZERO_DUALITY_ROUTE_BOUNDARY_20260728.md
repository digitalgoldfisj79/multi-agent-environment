# Zero-duality route boundary

Date: 28 July 2026  
Status: promising dual Gram observation proved; RH alone does not supply the required block variance.

## 1. The appealing ratio structure

The primorial centres satisfy

\[
P_k=P_jQ_{j,k},
\qquad
Q_{j,k}=\prod_{j<u\le k}p_u.
\]

For a zero ordinate `gamma`, the dual zero-sampling Gram contains sums of the form

\[
\sum_{0<\gamma\le T}
\left(\frac{P_k}{P_j}\right)^{i\gamma}
=
\sum_{0<\gamma\le T}Q_{j,k}^{i\gamma}.
\tag{1.1}
\]

Under the Riemann hypothesis, the uniform Landau--Gonek formula gives, for an integer
`Q>1`,

\[
\sum_{0<\gamma\le T}Q^{i\gamma}
=
-\frac{T}{2\pi}\frac{\Lambda(Q)}{\sqrt Q}
+
O\!\left(\sqrt Q\,\log(2QT)\log\log(3Q)\right)
	ag{1.2}
\]

up to the standard additional uniform terms, which are absorbed for integer `Q` in
the parameter range considered here.

Among the ratios `Q_{j,k}`:

1. `Q_{j,j+1}` is one prime;
2. every ratio with `k-j>=2` is a product of at least two distinct primes and is not
a prime power.

Therefore the resonant main term in (1.2) occurs only on the nearest-neighbour bands.
At the natural height `T asymp P_j/H`, the uniform remainder is exponentially small
relative to the diagonal zero count for all ratios within one dyadic primorial block.

This makes the **dual centre Gram** essentially tridiagonal.

## 2. Why this does not prove the short-interval variance

Let a smoothed explicit formula have schematic zero contribution

\[
E_j=\sum_{\gamma}a_j(\gamma)e^{i\gamma\log P_j}.
\]

The desired block square is

\[
\sum_j|E_j|^2
=
\sum_{\gamma,\gamma'}
\sum_j
a_j(\gamma)\overline{a_j(\gamma')}
 e^{i(\gamma-\gamma')\log P_j}.
\tag{2.1}
\]

Equation (2.1) samples **differences of zeros**.  Its kernel is

\[
F_X(\gamma-\gamma')
=
\sum_je^{i(\gamma-\gamma')\log P_j},
\]

not the same-zero ratio sum (1.1).

The Landau--Gonek formula controls the Gram obtained after dualizing against
arbitrary centre coefficients:

\[
\sum_\gamma
\left|
\sum_jc_jP_j^{i\gamma}
\right|^2.
\]

An operator-norm bound for this dual Gram, however, applied to the all-ones zero
coefficient vector, retains a factor equal to the number of zeros and gives only the
trivial coherent bound.  It does not establish cancellation between distinct zero
ordinates in (2.1).

## 3. Required extra input

To exploit the explicit formula at physical length

\[
H\asymp(\log P)^2,
\]

one needs quantitative control of zero differences at the corresponding height.  This
is a pair-correlation or weighted pair-correlation theorem of essentially the same
strength as the desired short-interval prime variance.

The Riemann hypothesis alone controls the horizontal location of zeros but does not
provide this zero-difference cancellation.

Thus the nearest-neighbour Landau resonance is a genuine structural observation, but
not a replacement for the Buchstab sampling theorem.

## 4. Unconditional difficulty

Without RH, factors `P_j^{\beta-1/2}` from zeros off the critical line enter the
short-interval explicit formula.  Existing zero-density estimates do not yield the
required `O(NHX o(log X))` block scale at intervals of length `(log P)^2`.

Therefore the unconditional zero route is strictly harder with currently available
zero-density technology.

## 5. Boundary

Proved structurally:

1. only adjacent primorial ratios create a Landau prime-power resonance;
2. the dual centre Gram is near tridiagonal at the natural height;
3. the actual block variance depends on zero differences and is not controlled by
that observation alone.

Potential conditional route:

1. RH plus a sufficiently uniform weighted pair-correlation theorem could recover the
Fortune-scale block variance.

Not supplied by this route:

1. an RH-only proof;
2. an unconditional block variance theorem;
3. Fortune's conjecture.
