# Current Kloosterman technology map

Date: 28 July 2026  
Status: published-theorem parameter comparison; no direct closure of the source--orbit dispersion theorem.

## 1. Target form

The physical first-order cross-modulus term is

\[
\begin{aligned}
\mathcal O_{X,\mathrm{Fourier}}^{(1)}
={}&
\sum_j
\sum_{\substack{X<r,s\le H\\r\ne s}}
\frac{(r-1)(s-1)}{rs(r-2)(s-2)}\\
&\times
\sum_{a=1}^{r-1}\sum_{b=1}^{s-1}
T_{j,r}(a)\overline{T_{j,s}(b)}
 e\!\left(P_j\left(\frac ar-\frac bs\right)\right),
\end{aligned}
\tag{1.1}
\]

with

\[
H\asymp X^2.
\]

The required estimate is the signed aggregate

\[
\boxed{
\mathcal O_{X,\mathrm{Fourier}}^{(1)}
\ll NHX\,L(X),
\qquad L(X)=o(\log X).
}
\tag{1.2}
\]

The diagonal `r=s` is already proved to be `O(NHX/log X)`.

## 2. Wright's 2026 range

Thomas Wright's *Trilinear Kloosterman Fractions I: Partially Fixed Moduli and
Unbalanced Convolutions* proves an improved Fouvry--Radziwill distribution theorem.
In the extremal unbalanced range, the modulus parameter satisfies

\[
Q\le\mathcal X^{1/2+1/66-\varepsilon},
\tag{2.1}
\]

where `mathcal X` is the ambient convolution size.  A wider theorem permits

\[
Q\le\mathcal X^{45/89-\varepsilon}
\tag{2.2}
\]

under additional restrictions on the shorter convolution variable.

Reference: arXiv:2604.25177, Corollary 2.2.

If the physical prime source is viewed at ambient size

\[
\mathcal X=H,
\]

then (2.1) reaches only

\[
\boxed{
Q\le H^{1/2+1/66-\varepsilon}
=X^{1+1/33-2\varepsilon}.
}
\tag{2.3}

Thus it covers a narrow band immediately above the lower endpoint `r=X`; it does
not approach the full physical range `r<=H=X^2`.

## 3. Norm mismatch

The published distribution statement controls a quantity of the shape

\[
\sum_{q\sim Q}|E(q,a)|
\ll_A
\mathcal X(\log\mathcal X)^{-A}
\tag{3.1}
\]

for one residue class `a`, after decomposing the source into admissible convolutions.

The Fortune target is not (3.1).  It is:

1. quadratic across centres;
2. bilinear across two independent modulus variables `r,s`;
3. signed across dyadic modulus blocks;
4. coupled through the phases `P_j(a/r-b/s)`;
5. centred before squaring.

Applying (3.1) separately for each centre and taking an absolute modulus sum loses the
cross-modulus cancellation that (1.2) requires.  Even an arbitrarily large logarithmic
saving in (3.1) does not by itself replace the missing factor of order `X` between a
pointwise `H`-scale error and the required square-root `sqrt(HX)` scale.

## 4. Source-condition mismatch

Wright's theorem assumes a fixed-complexity convolution in which one coefficient
sequence satisfies a Siegel--Walfisz condition and the variables occupy full dyadic
ranges.  The source in (1.1) has additional features:

1. prime offsets in the microscopic interval `[1,H]` relative to the centre `P_j`;
2. centre-dependent candidate cutoff `m>z_j`;
3. Euler--Buchstab centring that must be preserved;
4. a residue class moving with the primorial prefix;
5. a second modulus variable introduced by the block square.

A Vaughan or Heath--Brown decomposition can create admissible local convolutions, but
using the published theorem on each piece does not reconstruct the signed source--orbit
square without a new recombination argument.

## 5. Bilinear Kloosterman-fraction results

Dong, Robles and Zeindler's *Bilinear Forms with Kloosterman Fractions and Applications*
(arXiv:2601.00292) supplies fixed-dyadic bilinear Kloosterman-fraction savings.  These
estimates are relevant after reciprocity and completion of selected pieces of (1.1), but
they do not include:

1. the complete primorial-prefix centre average;
2. the full range `X<r,s<=X^2`;
3. the rough-coordinate/tail-martingale covariance;
4. the exact signed recombination required by the detector.

They are therefore candidate local inputs, not a black-box proof of (1.2).

## 6. What current technology can legitimately do

Published Kloosterman-fraction estimates can be used to:

1. control selected dyadic pieces just beyond `H^{1/2}`;
2. bound fixed-complexity bilinear or trilinear transforms after source decomposition;
3. reduce the uncovered parameter region;
4. test whether the primorial phase gives an additional saving inside those proofs.

They cannot currently be cited to prove the complete source--orbit dispersion theorem.

## 7. Exact missing extension

The needed extension is not simply a larger exponent in (2.1).  It is a theorem for a
signed two-modulus form with an extra sparse multiplicative walk:

\[
\boxed{
\sum_j
\sum_{r\sim R}\sum_{s\sim S}
\alpha_{j,r}\overline{\alpha_{j,s}}
 e\!\left(P_j\left(\frac{a}{r}-\frac{b}{s}\right)\right)
}
\tag{7.1}
\]

at the coefficient scale supplied by the locally centred prime source, uniformly over

\[
X<R,S\le X^2.
\]

An acceptable theorem may average over `j`, exploit the recurrence
`P_{j+1}=p_{j+1}P_j`, and retain signed dyadic recombination.  This is the actual
source--orbit extension missing from current published inputs.

## 8. Boundary

Published input:

1. Wright's modest extension beyond level one half for selected unbalanced
   convolutions;
2. fixed-dyadic bilinear Kloosterman-fraction estimates of Dong--Robles--Zeindler.

Not justified by those papers:

1. the complete physical first-order cross-modulus estimate;
2. the deterministic Buchstab-martingale sampling theorem;
3. Fortune's conjecture.

Next task:

1. enter the proof of a covered dyadic Kloosterman range and test whether the
   primorial-prefix phase can be retained as an additional averaging variable rather
   than discarded by absolute values.
