# Programme status after the complete prime-modulus frame

Date: 28 July 2026

## Exact progress

The lower-frame problem for the centred integer Fortune source is closed
unconditionally after replacing reciprocal-difference sampling by complete
additive characters modulo critical-shell primes.

For

\[
C_X(\theta)=\sum_{j<N}(\Psi_j(H)-\mu_j)e(P_j\theta),
\]

define

\[
\mathfrak D_X(c)
=\frac1{|\mathcal Q_X|}\sum_{q\in\mathcal Q_X}\frac1q
 \sum_{a\bmod q}|C_X(a/q)|^2.
\]

Complete orthogonality gives the exact Gram kernel

\[
\Delta_X(P_j-P_k)
=\frac1{|\mathcal Q_X|}\#\{q\in\mathcal Q_X:q\mid P_j-P_k\}.
\]

For `j<k`, every shell prime is coprime to `P_j`, so

\[
q\mid P_k-P_j
\Longleftrightarrow
q\mid\prod_{j<u\le k}\ell_u-1.
\]

Factor counting then gives

\[
\|\mathbf D_X-I\|_{\mathrm{op}}\ll1/\log X
\]

and hence

\[
\mathfrak D_X(c)=(1+O(1/\log X))\|c\|_2^2
\]

uniformly for every residual vector.

No reciprocal-fraction cancellation theorem is required for the lower frame.

## Finite validation

The exact complete-character identity was checked directly at `X=5`.
The divisor-count Gram matrix was computed at

\[
X=11,23,53,131,257,503.
\]

At `X=503`:

- `N=73`;
- `H=202407`;
- shell size `16029`;
- frame spectrum `0.9997516527` to `1.0002920196`;
- operator norm `||D-I||=0.0002920196`;
- maximum off-diagonal row sum `0.0004990954`.

The finite panel is corroborative only.  The asymptotic theorem follows from the
proved divisor-count estimate and the prime number theorem.

## Consequence for Fortune

The remaining load-bearing estimate is now the single complete-grid source bound

\[
\mathfrak D_X(c)\ll NHX L(X),
\qquad L(X)=o(\log X).
\]

The unconditional lower frame then gives

\[
\sum_j|\Psi_j(H)-\mu_j|^2\ll NHX L(X),
\]

which excludes every failed centre by the one-sided detector criterion.

## Revised priority

1. Derive the complete-grid source-energy expansion with the baseline cross term
   retained.
2. Identify the exact principal term produced by a Buchstab/Heath--Brown
   decomposition.
3. Determine whether the required `o(log X)` loss can be obtained from currently
   available Type I/II technology.
4. If not, record the precise factor-range or parity obstruction and switch to
   the double-von-Mangoldt source only if it changes that obstruction.

The old coefficient-free pair frame, HTE4 and Paper IV derandomisation remain
secondary.

Fortune's conjecture remains open.