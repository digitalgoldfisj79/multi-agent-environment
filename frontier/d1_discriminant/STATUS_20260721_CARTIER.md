# d=1 cubic crown status after the Cartier programme

**Date:** 2026-07-21  
**Branch:** `gpt56/consolidated-fortune-20260721`  
**Target:** prove that for every prime `p>=5` there is an irreducible

`X^p+aX^3+bX^2+cX+d`, with `(a,b)!=(0,0)`.

Translation reduces every member with `a!=0` to the depressed slice

`X^p+aX^3+cX+d`.

The function-field d=1 crown remains open. The integer Fortune conjecture is a separate and harder problem.

## 1. Strongest new exact theorem

For a monic degree-p polynomial

`F=X^p+sum_(j=0)^(p-1) f_j X^j`,

define the full Cartier matrix

`H_(u,v)=[X^(pu-v)]F^(p-1)`, `1<=u,v<=p`.

Except for the pure inseparable family `X^p-s`, the selected cofactors satisfy

`Cofactor_(p,j)(I-H)=j f_j 1_(F irreducible)`

for every `1<=j<p`.

For the depressed cubic slice this gives, pointwise on the complete coefficient plane,

`Cofactor_(p,3)(I-H)=3a 1_irr`,

`Cofactor_(p,1)(I-H)=c 1_irr`.

The proof is unconditional:

- on the squarefree locus, the residue matrix conjugates Cartier to the Frobenius permutation on roots;
- on reducible or singular members, independent logarithmic differentials `dh_i/h_i` give at least two Cartier-fixed vectors;
- the one-distinct-factor nonreduced exception is impossible when `a!=0`.

Independent exhaustive verification passed for every `a!=0,c,d` at `p=5,7,11,13`.

Files:

- `GENERAL_CARTIER_COFACTOR.md`;
- `ORDINARY_HASSE_WITT_COFACTOR.md`;
- `ordinary_hasse_witt_cofactor_check.py`.

## 2. Consequence for the crown

For each fixed nonzero a,

`3a N_a(p)=sum_(c,d) Cofactor_(p,3)(I-H)`.

Thus the crown is one explicit mod-p cofactor-sum nonvanishing problem. This is simpler than the Berlekamp determinant:

- no polynomial reduction modulo F;
- no extension-field factorisation;
- no dynatomic inclusion--exclusion;
- no p-adic lift.

The higher Hasse--Witt programme produced this ordinary boundary cofactor and then collapsed to it exactly. Its first-Witt and singular-completion notes remain useful provenance, but they are no longer the shortest architecture.

## 3. Translation compression

For the full cubic family, translation from a depressed representative gives

`b_t=3at`,

`c_t=c0+3at^2`,

`d_t=d0+(c0+1)t+at^3`.

If `r+2s+3u=p-1`, then

`sum_t b_t^r c_t^s d_t^u=-(3a)^(r+s)a^u`.

This yields full-coefficient-space crown coefficients with external weight of degree about p/3, rather than the degree-p-1 projector `b^(p-1)`.

The associated occupation conservation law is

`(p-3)A+(p-2)B+(p-1)C+pD`
`=(p-1)sum_(u in S)(p-u)+(p-j)`.

After coefficient orthogonality it forces exactly the two square-class modes in a.

Files:

- `TRANSLATION_WEIGHT_COMPRESSION.md`;
- `CARTIER_OCCUPATION_CONSERVATION.md`.

## 4. Exact constructive obstruction

A fibre-specific Artin--Schreier semiconjugacy

`R(Z+1)=g(R(Z)) mod (Z^p-Z-1)`

with cubic g and rational degree m must satisfy

`m>=p/4`.

If `4m<p`, clearing denominators produces a polynomial identity, contradicting the theorem that a globally translation-stable rational subfield can induce only a Möbius map.

This rules out every bounded-degree rational construction for infinitely many p. Computational sweeps agree:

- one-term monomial images: only small accidental cases;
- two-term monomial or binomial images: only small accidental cases;
- normalized cubic images: no cases for `p>=7` through the tested ranges;
- allowing the quadratic recurrence term did not create a stable family.

File: `FIBRE_SEMICONJUGACY_DEGREE_BARRIER.md`.

## 5. Moore/Hilbert--90 reduction and its boundary

For a prospective root x, put

`delta=x^p-x`, `t=delta^(p-1)`, `y=x/delta`.

The cubic coefficient recovered from three Frobenius rows is

`lambda=delta^(-2)(t^p-t)/((1+t)(3y+2+t))`.

The complete incidence condition is equivalent to the single scalar equation

`lambda^p=lambda`.

This is an exact reduction. However, following its rational invariant through to the variables

`R=-a delta^2`, `D=d/delta`

produces the singular cubic

`D^3+(1+(c+1)y)D^2-Iy^3=0`, `I=-ad^2`.

Its rational parameter is `x/d`, and the induced recurrence is exactly the original scaled equation. Thus the apparent low-genus reduction is birationally tautological, not a new compression.

File: `MOORE_CUBIC_COEFFICIENT.md`.

## 6. Empirical results retained and rejected

Exact complete sweeps through every prime `p<=379`, both square classes, show:

- the count residues remain nonzero throughout the tested range;
- the nonsquare first c-moment `sum_irr c` is nonzero for all 73 tested primes;
- the only first-moment zero is the square class at p=5.

This moment is not structurally sparse: at p=11, 226 and 223 of 512 eligible Cartier minors survive in the two square classes. It is therefore not promoted to the main route.

The proposed fixed low-genus trace bounds were falsified:

- `|A_p|<=4sqrt(p)` fails at p=167;
- `|B_p|<=2sqrt(p)` fails at p=149;
- no elliptic curve of conductor at most 9999, or tested small quadratic twist, matches the square-class difference sequence.

File: `CARTIER_MOMENT_EMPIRICAL.md`.

## 7. Routes now closed

The following are not active crown routes:

1. extending fixed dynatomic degrees one by one;
2. a bounded-support or bounded-degree Artin--Schreier construction;
3. a finite catalogue of fixed small quadrinomials;
4. the special lines `c=0` or `c=-1` as universal constructions;
5. fixed-rank genus-two plus elliptic trace models;
6. direct subset pruning of the Cartier alternant;
7. treating p-density Hasse-polynomial results for additive exponential sums as if they directly evaluated the modular p-cycle cofactor.

## 8. Current wall

The ordinary Cartier theorem has compressed irreducibility to the best exact mod-p object found so far. The unresolved task is still to show that its complete coefficient sum is nonzero.

Two credible fronts remain:

### A. Corrected Cartier constant-term/transfer operator

Evaluate the selected cofactor sum as a whole, preserving cancellations between the many surviving Toeplitz minors. The occupation law should be built into the state space from the outset. Any method that enumerates subsets individually is exponential and has already failed at p=11.

### B. The original full-family character-sum Lemma L

The D1 attack already reduces the complete four-parameter target to an explicit inequality for the aggregated cubic Weil sums. The Cartier cofactor is a new exact presentation of the same obstruction and may supply a more efficient algebraic transform, but no saving over the growing-dimension wall has yet been proved.

## 9. Honest bottom line

The programme made genuine theorem-level progress:

- a new general Cartier cofactor irreducibility theorem;
- an ordinary mod-p crown indicator simpler than both Berlekamp and higher Hasse--Witt formulations;
- low-degree translation-weight compression;
- a termwise occupation conservation law;
- a rigorous linear complexity barrier for constructive semiconjugacy.

It did not prove FF-Fortune(p,1). The remaining obstruction is no longer lack of a correct indicator; it is evaluating the complete modular full-cycle cofactor after the cancellations that distinguish one p-cycle from every reducible factor partition.
