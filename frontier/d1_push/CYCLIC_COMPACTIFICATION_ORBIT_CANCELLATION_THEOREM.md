# Cyclic cancellation of proper convolution boundary faces

**Date:** 2026-07-23  
**Status:** exact equivariant-additivity theorem for the p-fold Fourier convolution, for every prime `p>=5`. Every compactification face obtained by placing a proper nonempty subset of factors on the punctual `lambda=0` boundary occurs in a free `C_p`-orbit and has zero cyclic trace. The all-boundary face is the convolution identity/Tate term. This shows that pair, `D` and other lower hooks are not additional boundary faces of the compressed Adams calculation. The frequency-zero fixed diagonal is a different stratum and remains separately analyzed.

## 1. Fourier kernel and its punctual boundary

Let `K_a=FT_(c,d)(P_a)` be the full Fourier transform of the degree-p root permutation sheaf.

`ROOT_SHEAF_FULL_FOURIER_LINE_THEOREM.md` proves:

- on `lambda!=0`, `K_a` is a rank-one Legendre sheaf;
- on `lambda=0,kappa!=0`, `K_a=0`;
- the complete `lambda=0` restriction is supported at the single origin
  `(kappa,lambda)=(0,0)`.

Denote this punctual origin object by `delta_0`. Under additive convolution, `delta_0` is the identity object, up to the fixed normalization shift and twist.

## 2. Faces of the p-fold convolution

Consider

`K_a^(star p)=K_a star ... star K_a`

with the cyclic action

`sigma:(0,1,...,p-1)->(1,2,...,p-1,0)`.

A boundary face on which precisely the factors indexed by a subset

`S subset {0,...,p-1}`

lie at `delta_0` is canonically the corresponding lower-length convolution of the factors outside `S`, with fixed identity factors inserted at `S`.

The p-cycle sends this face to the face indexed by `sigma(S)`.

## 3. Prime cyclic-orbit lemma

The only subsets fixed by a transitive p-cycle, with p prime, are

`S=emptyset`

and

`S={0,...,p-1}`.

Every proper nonempty subset has orbit length exactly p.

Let

`M_S=direct_sum_(j=0)^(p-1) C_(sigma^j S)`

be the direct sum of the complexes carried by one such orbit of faces. The endomorphism `sigma` cyclically permutes the p summands and has zero categorical trace:

`Tr(sigma|M_S)=0.`

This remains true with Frobenius inserted because Frobenius commutes with the cyclic action and preserves the face orbit:

`Tr(sigma Frob|M_S)=0.`

The statement is exact in the Grothendieck group and does not require semisimplicity. Over `Q_ell`, `ell!=p`, it also follows from exact character projection.

### Theorem CCOC.1 — proper-face annihilation

`boxed(Every proper nonempty lambda=0 convolution face`

`      contributes zero to the p-cycle Adams trace.)`

## 4. The two fixed faces

### 4.1 Empty subset

`S=emptyset` is the open convolution in which every `lambda_i` is nonzero. Its stationary equations are treated in

`CYCLIC_CONVOLUTION_STATIONARY_EQUATIONS.md`.

At nonzero total c-frequency it has no generic interior stationary point; its finite exceptions are the already Adams-annihilated collision strata. Its remaining contribution is at root infinity.

### 4.2 Full subset

When every factor equals `delta_0`, the p-fold convolution is again `delta_0`. Its cyclic action is trivial. This is the convolution identity/main punctual term, corresponding under inverse Fourier transform to the unique Tate/main class already removed from the normalized count.

No pair, `D`, or middle-hook object is created by this face.

## 5. Consequence for the extremal hook sectors

The pair and `D` families are genuine geometric constituents after expanding

`Psi^p(P)-P`

back into the alternating hook ledger. Theorem CCOC.1 shows that they are not independent lower-length compactification faces in the compressed cyclic-convolution calculation.

Therefore an endpoint proof for the **full normalized Adams pushforward** need not subtract pair and `D` sheaves before applying cyclic stationary phase. Their traces are internal components of the same cyclic object and cancel or recombine inside its final local Fourier presentation.

This avoids the categorical problem that subtracting a large honest pair or `D` sheaf could artificially enlarge an effective virtual-rank estimate.

## 6. Remaining strata

CCOC.1 does not address:

- the open all-nonzero convolution at total frequency zero;
- the cyclic fixed diagonal inside that zero-frequency stratum;
- the all-infinity weighted face;
- intersections between the weighted infinity charts.

At nonzero c-frequency, the first two are absent by the exact stationary equations, and the all-infinity face reduces to the two escaping A1 branches.

At frequency zero, the cyclic fixed diagonal can support an additional punctual contribution. It must be bounded separately or included in a global four-object specialization theorem.

## 7. Epistemic classification

### Exact

- punctual nature of the one-factor `lambda=0` boundary;
- subset indexing of convolution identity faces;
- prime cyclic-orbit classification;
- zero trace on every proper-face orbit;
- identification of the all-origin face with the main/Tate term;
- absence of additional pair/D faces in the compressed calculation.

### Open

- cyclic fixed-diagonal punctual contribution at zero frequency;
- complete weighted-infinity specialization;
- full four-object effective presentation and crown.
