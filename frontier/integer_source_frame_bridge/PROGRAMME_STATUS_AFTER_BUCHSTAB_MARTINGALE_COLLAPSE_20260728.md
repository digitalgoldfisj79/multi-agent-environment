# Programme status after the Buchstab-martingale collapse

Date: 28 July 2026  
Status: exact detector and coefficient architecture complete; one deterministic sampling theorem remains load-bearing.

## 1. Correct detector

For each primorial centre `P_j`, candidate prime offset `m`, and

\[
Y_j=\sqrt{P_j+H},
\]

the exact Euler--Buchstab detector is

\[
\mathbf1_{P_j+m\text{ prime}}
=
V(z_j,Y_j)
\prod_{z_j<r\le Y_j}(1+\xi_r(P_j+m)).
\]

The natural logarithmically weighted coefficient satisfies

\[
\log(P_j+m)V(z_j,Y_j)\asymp\log X.
\]

Thus the old `X`-sized certificate normalization is not the normalization of the
correct centred prime-output detector.

## 2. Principal subtraction

The smooth primitive rational frequencies give an exact finite centring

\[
\mu_{P_j}^{\mathrm{prim}}.
\]

It satisfies

\[
\mu_{P_j}^{\mathrm{prim}}
=
\frac{P_j}{\varphi(P_j)}
\bigl(\pi(H)-\pi(z_j)\bigr)+o(H)
=
\left(\frac{e^\gamma}{2}+o(1)\right)H.
\]

The additive zero mode alone is not the correct principal term; coherent smooth
nonzero frequencies supply a main-order correction.

## 3. Physical first-order theorem

The physical first-order term is an exact sum of locally centred prime-progression
discrepancies

\[
\Delta_{j,r}
=
\sum_{m\equiv-P_j\pmod r}b_{j,m}
-
\frac1{r-1}\sum_{m\ne r}b_{j,m},
\qquad
z_j<r\le H.
\]

Its diagonal Gram energy is now proved unconditionally:

\[
\boxed{
\mathcal D_X^{(1)}
\ll
\frac{NHX}{\log X}.
}
\]

Therefore the diagonal is no longer load-bearing.  The unresolved physical term is
only the cross-modulus covariance

\[
\mathcal O_X^{(1)}.
\]

Complete finite blocks through `X=211` give

\[
\frac{\mathcal D_X^{(1)}}{NHX}:
0.108\ \text{at }X=19
\quad\longrightarrow\quad
0.023\ \text{at }X=211.
\]

The complete first-order square at `X=211` is approximately `0.028 NHX`.
These figures are empirical and use a Mertens continuation for the distant tail
normalization.

## 4. Higher-order collapse

After the physical sieve is absorbed exactly, the full tail Euler chaos has both an
orthonormal product representation and a one-index ordered Buchstab representation.

The ordered form is

\[
\boxed{
V(H,Y)
\prod_{H<r\le Y}(1+\xi_r(n))
=
V(H,Y)
+
\sum_{H<r\le Y}
V[r,Y]R_{<r}(n)\xi_r(n).
}
\]

For an `H`-rough composite output, there is exactly one active negative hit—the least
tail prime factor.  The apparent exponentially deep parity chaos has therefore
collapsed to a prime-indexed martingale.

## 5. Exact energy budget

In the complete product-residue model, the ordered increments are martingale
differences and have exact total quadratic variation

\[
\boxed{
V(H,Y)(1-V(H,Y)).
}
\]

For the logarithmically weighted detector, summing over all candidate offsets and
all centres gives the coefficient/quadratic-variation budget

\[
\boxed{
O(NHX).
}

There is no remaining loss from:

1. decomposition depth;
2. divisor-function order;
3. coefficient magnitude;
4. construction of the principal term;
5. lower-frame stability.

## 6. The one remaining theorem

Define the exact centred detector residual

\[
E_j
=
\sum_{m\le H}\Lambda(P_j+m)-\mu_{P_j}^{\mathrm{prim}}.
\]

The programme now requires one deterministic martingale sampling theorem:

\[
\boxed{
\sum_{j<N}|E_j|^2
\ll
NHX\,L(X),
\qquad
L(X)=o(\log X).
}
\tag{6.1}

An equivalent proof may be formulated as a joint estimate for:

1. the physical first-order cross-modulus Gram;
2. the normalized `H`-rough principal coordinate;
3. the ordered tail martingale;
4. all cross covariances among them.

The theorem must exploit arithmetic cancellation in the moving residue classes
`-P_j mod r`.  Column support and column norms alone cannot prove it.

## 7. Why existing routes do not yet close it

### Standard level of distribution

Bombieri--Vinogradov reaches approximately `r<=H^{1/2}=X`, while the physical
prime-modulus frame occupies

\[
X<r\le H\asymp X^2.
\]

### Current Kloosterman-fraction technology

Published bilinear and trilinear results give fixed-complexity savings in restricted
dyadic parameter ranges, but do not directly supply the full moving-class level of
distribution or the tail martingale sampling inequality.

### Shrinking-target sparsity

It is strong in the exponential far tail, but near `H` the visit-gap bound is
trivial.  The martingale baseline is also nonsparse.  A support-only proof is therefore
impossible.

### Zeta-zero duality

Primorial ratios make the Landau dual zero Gram nearly tridiagonal, but the actual
short-interval block square depends on differences of zeros.  RH alone does not supply
the required pair-correlation estimate.

## 8. Correct next research target

The next push should attack the deterministic sampling theorem directly in its
locally centred form.  The preferred order is:

1. dyadically expand the physical cross-modulus Gram as a reciprocal-difference
   Linnik dispersion form;
2. isolate the ranges covered by current bilinear/trilinear estimates;
3. quantify the uncovered near-physical and far-tail ranges;
4. use the ordered martingale and shrinking-target recurrence to couple those ranges
   rather than majorising them separately;
5. either prove (6.1) or produce a parameter-sharp theorem-level obstruction.

## 9. Consequence for Fortune

If (6.1) holds, every failed centre costs `Omega(H^2)`, while

\[
NHX/H^2\asymp1/\log X.
\]

Since `L(X)=o(log X)`, the number of failures is eventually less than one.  Hence
every sufficiently large primorial centre has a prime output below the square threshold,
and the corresponding Fortunate number is prime.  A finite computation then completes
the remaining initial range.

## 10. Boundary

Proved exactly or unconditionally:

1. source-to-frame and complete lower frame;
2. primitive rational-frequency source;
3. exact finite principal centring;
4. Euler--Buchstab detector;
5. physical first-order discrepancy and character frame;
6. first-order diagonal theorem;
7. normalized tail-chaos coefficient identity;
8. ordered Buchstab martingale and exact complete-model quadratic variation;
9. support-only no-go.

Computationally supported:

1. first-order aggregate energy through `X=211`;
2. near-cancellation of the aggregate cross term in most tested blocks.

Open:

1. deterministic martingale/orbit sampling theorem (6.1);
2. Fortune's conjecture.
