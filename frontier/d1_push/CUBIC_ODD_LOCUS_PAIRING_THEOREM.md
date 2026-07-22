# Cubic factors on the odd locus d=0

**Date:** 2026-07-22  
**Status:** exact factorisation theorem for every prime `p>=5`. It isolates the root-negation component responsible for the largest cubic-factor fibers in the depressed slice.

## 1. Odd slice

For `d=0`,

`F_(c,0)(X)=X^p+aX^3+cX`

is odd. Put

`m=(p-1)/2`

and

`H_c(Y)=Y^m+aY+c.`

Then

`boxed(F_(c,0)(X)=X H_c(X^2).)`

Let `R_3(c)` be the number of monic irreducible cubic factors

`g(Y)=Y^3-tY^2+sY-n`

of `H_c(Y)` whose norm `n` is a square in `F_p^*`.

## 2. Cubic factorisation under Y=X^2

Let `y` be a root of an irreducible cubic `g`. Then `y` lies in `F_(p^3)` and has norm `n`.

Because the extension degree is odd,

`chi_(p^3)(y)=chi_p(Norm_(p^3/p)(y))=chi_p(n).`

Therefore `y` has a square root in `F_(p^3)` exactly when `n` is a square in `F_p`.

If `n` is a square, choose `alpha in F_(p^3)` with `alpha^2=y`. Since `y` has degree three, so does `alpha`. Let `h(X)` be the irreducible cubic minimal polynomial of `alpha`. The other square root `-alpha` has minimal polynomial

`h^-(X)=-h(-X)`.

The two cubics are distinct: equality would make `h` odd, hence divisible by `X`, contradicting irreducibility. Their product is

`boxed(g(X^2)=h(X)h^-(X).)`

If `n` is nonsquare, `y` is nonsquare in `F_(p^3)`, a square root has degree six, and `g(X^2)` is irreducible of degree six.

### Theorem COLP.1 — odd-locus cubic pairing

For every `c in F_p`,

`boxed(Q_3(c,0)=2R_3(c).)`

Thus every irreducible cubic factor of an odd slice member occurs in a forced root-negation pair

`{h(X),-h(-X)}.`

## 3. Exact factorial-moment consequences

For any integer `R>=0`,

`binom(2R,2)=4binom(R,2)+R`,

`binom(2R,3)=8binom(R,3)+4binom(R,2).`

Hence the entire contribution of `d=0` to the cubic pair and triple moments is

`boxed( sum_c binom(Q_3(c,0),2)`

`       =4sum_c binom(R_3(c),2)+sum_c R_3(c), )`

and

`boxed( sum_c binom(Q_3(c,0),3)`

`       =8sum_c binom(R_3(c),3)+4sum_c binom(R_3(c),2). )`

In particular all odd-locus values of `Q_3` are even.

## 4. Geometric interpretation

The odd locus is not part of the generic off-diagonal cubic-pair surface. It is the one-variable family

`H_c(Y)=Y^((p-1)/2)+aY+c`

with a quadratic-norm projector on its degree-three factors.

The large fibers visible in the complete cubic ledger are explained by two mechanisms:

1. every admissible degree-three factor `g(Y)` contributes two cubics in `X`;
2. several admissible factors of one `H_c` multiply the fiber size by two simultaneously.

Therefore the correct primitive decomposition of `M_33` must subtract the formulas above before analysing `d!=0`.

## 5. Consequence for the programme

The exceptional high multiplicities at `p=23,29,61,79,101` are not evidence of a high-rank generic surface. They are partly forced by the odd involution.

The next odd-locus task is the exact degree-three factor mass and pair mass of `H_c(Y)` with the square-norm projector. This is a one-parameter factor problem and is strictly smaller than the full two-parameter cubic-pair surface.

## 6. Epistemic classification

- Factorisation `F=XH(X^2)`: exact.
- Square/norm equivalence in the odd cubic extension: exact.
- Factorisation of `g(X^2)`: exact.
- Root-negation pairing and moment identities: exact.
- Uniform evaluation of the projected `R_3` moments: open.
- Generic cubic-pair surface and d=1 crown: open.
