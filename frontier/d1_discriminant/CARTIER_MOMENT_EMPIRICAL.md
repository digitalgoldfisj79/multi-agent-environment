# Empirical Cartier moments through p=379

**Date:** 2026-07-21  
**Status:** exact computation over the tested range; no asymptotic theorem asserted.

## 1. Sweep

For every one of the 73 primes `5<=p<=379`, both square classes of `a` were represented and the complete family

`F=X^p+aX^3+cX+d`

was factored for all `c,d in F_p`. The involution `d->-d` was used to halve the factorisations and restore exact even moments.

For each class the computation recorded:

- the exact irreducible count `N_+(p),N_-(p)`;
- the moments `sum_irr c^r d^s mod p` for `0<=r<=4` and `s=0,2,4,6`.

Hugging Face jobs:

- full moment sweep: `6a5fe533d09dc1f57c6c0505`;
- compact independent audit: `6a5fed09d09dc1f57c6c05fe`.

## 2. First c-moment

Put

`M_+(p)=sum_(irreducible, chi(a)=+1)c mod p`,

`M_-(p)=sum_(irreducible, chi(a)=-1)c mod p`.

The complete zero list through p=379 is

`(p,M_+,M_-)=(5,0,1)`.

Thus:

- the nonsquare-class moment `M_-(p)` is nonzero for every tested prime;
- the square-class moment is nonzero for every tested prime except p=5.

By the general Cartier cofactor theorem this is the canonical coefficient

`[c^(p-2)d^(p-1)] C_3^can = 3a sum_irr c`.

This is a credible exact target, but the nonvanishing is empirical only.

## 3. Falsified low-genus hypotheses

Define

`A_p=p+1-(N_+(p)+N_-(p))/2`,

`B_p=(N_-(p)-N_+(p))/2`.

The apparent bounds

`|A_p|<=4 sqrt(p)`, `|B_p|<=2 sqrt(p)`

hold for a substantial initial range but fail before p=200:

- at p=167, `(N_+,N_-)=(104,118)` and `A_p=57`, so
  `|A_p|/(4sqrt(p))=1.102698...`;
- at p=149, `(N_+,N_-)=(106,168)` and `B_p=31`, so
  `|B_p|/(2sqrt(p))=1.269809...`.

Therefore the data do not support a fixed genus-two plus elliptic decomposition with those trace normalisations.

A Cremona database search also found no elliptic curve of conductor at most 9999, and no quadratic twist by squarefree `|D|<=100`, matching the initial `B_p` sequence.

These low-genus interpretations are closed and must not be used in proofs or status summaries.

## 4. Largest tested class-scale deviation

The compact audit also measured

`max(|p+1-N_+|,|p+1-N_-|)/(6sqrt(p))`.

The maximum through p=379 is

`0.825411...` at p=167,

where the two class traces are 64 and 50. This observation is not promoted to a `6sqrt(p)` conjecture; the constant was selected after inspecting the data and has no identified geometric source.

## 5. Final ten count records

`p : (N_+,N_-)`

- 317: `(304,300)`
- 331: `(332,286)`
- 337: `(294,316)`
- 347: `(362,330)`
- 349: `(282,286)`
- 353: `(310,364)`
- 359: `(306,308)`
- 367: `(300,320)`
- 373: `(380,388)`
- 379: `(352,356)`

## 6. Strategic conclusion

The exact counts remain of order p, but the tested data no longer justify a bounded-rank motive hypothesis at ranks four and two. The only low-complexity empirical lead retained is the nonsquare first c-moment. It should be pursued only through a structural Cartier/translation formula; extending the prime range alone has little value.
