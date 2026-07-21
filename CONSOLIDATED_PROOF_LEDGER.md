# Consolidated Fortune proof ledger

**Date:** 2026-07-21  
**Branch:** `gpt56/consolidated-fortune-20260721`  
**Parents:** Claude RQM and novelty head `30703f06...`; GPT discriminant and dynamics head `b2d0e266...`.

## 1. Closed theorem fronts

### RQM: random-order reciprocal-frame model

`RQM_PROOF.md` proves, under its stated frame-nondegeneracy and effective prime-count hypotheses,

`E_sigma E_a^sigma <= C(eta,rho) M (log X)^9`

uniformly for `1 <= |a| < H`, together with the weighted aggregate and Frobenius-energy bounds. The load-bearing arithmetic input is the exact sixth-moment count of characters with block-prime correlation at least `3/4`; the finite configuration and matching ledger closes with a polylogarithmic margin.

**Scope:** this is a theorem about uniformly random orderings of the block primes. It does not imply the estimate for the increasing primorial order and does not prove Fortune's conjecture.

### Function-field d=1: exact algebraic and sieve layers

The following are proved or machine-certified as labelled in `D1_ATTACK.md` and `frontier/d1_discriminant/`:

1. reduction to the sparse cubic family;
2. master root-incidence identity;
3. affine orbit structure;
4. quantized Kloosterman and root-count identity;
5. exact four-slice ledger and Lemma-L reduction;
6. machine certification through the stated finite range;
7. exact degree-p discriminant formula;
8. exact complete-slice Mobius mass and zero-discriminant count;
9. local admissibility implies squarefreeness;
10. exact count `(p^2 - 1)/3` of locally admissible members per nonzero cubic slice;
11. exact restricted discriminant-mass decomposition;
12. unconditional `O(p^(3/2))` factor-parity estimate;
13. exact degree-2 and degree-3 unconditioned factor-incidence formulas;
14. exact parity-breaking sieve reduction;
15. exact locally admissible quadratic-incidence formula with `O(p)` error;
16. exact signed quadratic-incidence decomposition with an effective `O(p^(3/2))` bound;
17. universal oriented-cubic parameterization by the trace-zero plane;
18. unsigned locally admissible cubic incidence `p^2/9 + O(p^(3/2))`;
19. signed cubic incidence `O(p^(3/2))`;
20. exact reduced Frobenius determinant indicator `J_a(c,d)=3a 1_irred`.

The quantized identity's method is classical. Novelty of the exact object and result remains provisional pending manual inspection of the offline sources listed in `NOVELTY_VERDICT.md`.

## 2. Consolidation correction

There is no direct mathematical interface between Theorem RQM and the function-field odd-reducible sector. RQM uses entropy from random orderings of integer block primes. The function-field problem has no such ordering variable.

The correct function-field companions are the parity-weighted factor sieve and the exact Frobenius determinant indicator.

## 3. Parity-breaking reduction

For

`F_(a,c,d)(X) = X^p + aX^3 + cX + d`

and

`H_(a,c,d)(X) = aX^3 + (c+1)X + d`,

let `A_a` be the coefficient pairs for which `H` is rootless. Every such F is squarefree and has no linear factor.

Pellet gives

`chi(Disc F)=(-1)^(r+1)`,

where r is the number of irreducible factors. Hence a positive-discriminant reducible member has at least three factors and therefore a factor of degree at most `p/3`. Thus

> F is irreducible if and only if it is locally admissible, has positive discriminant character, and has no factor of degree from 2 through `floor(p/3)`.

## 4. Completed quadratic sieve level

Every irreducible quadratic

`h_(s,n)(X)=X^2-sX+n`

divides exactly one member of the cubic slice, with

`c=1-a(s^2-n)`, `d=s(an-1)`.

The associated local cubic satisfies

`H_(s,n)(X)=a(X+s)h_(s,n)(X)+(2X-s)`.

This gives the exact unsigned formula

`L_(a,2)=p(p-1)/6 + [1+chi(a)(p chi(-1)-K_p)-2T_a]/6`,

where `K_p` is the trace of a fixed K3 surface. Hence

`L_(a,2)=p^2/6+O(p)`.

For the signed incidence,

`|L_(a,2)^chi| <= 30p^(3/2)+131p+1`.

Therefore

`L_(a,2,+)=p^2/12+O(p^(3/2))`,

`L_(a,2,-)=p^2/12+O(p^(3/2))`.

## 5. Completed cubic single-factor level

Choose an irreducible base cubic `X^3+X+b` and identify its trace-zero plane with `F_p^2`. Frobenius acts universally by

`tau(x,y)=(-y,x-y)`.

The invariant forms

`u=x^2-xy+y^2`,

`v=bR+(W0/2)S`,

`V=W0R-(27b/2)S`

parameterize oriented irreducible depressed cubics, three plane points per cubic.

The unique compatible translate and coefficients are rational fixed-degree functions of `(u,v,V)`. The shifted local-root equation is the degree-six surface

`G_a=2aV(z^3+uz+v)-6uz^2+(3V+9v)z-4u^2=0`.

A characteristic-zero genericity certificate proves that the root surface is geometrically irreducible and that all local and degree-p discriminant weights are geometrically nonsquare outside a finite bad-base set. Fixed-degree Weil and Lang-Weil estimates therefore give

`L_(a,3)=p^2/9+O(p^(3/2))`,

`L_(a,3)^chi=O(p^(3/2))`.

Consequently

`L_(a,3,+)=p^2/18+O(p^(3/2))`,

`L_(a,3,-)=p^2/18+O(p^(3/2))`.

A vectorized exact Hugging Face sweep over every prime below 1200 and both square classes found

`max |L_(a,3)-p^2/9|/p < 1.05`,

`max |L_(a,3)^chi|/p < 1.66`,

strongly supporting the sharper `O(p)` bounds.

## 6. Exact full-cycle determinant indicator

Let B be the matrix of `Phi-I`, where `Phi(z)=z^p` on

`F_p[X]/(F_(a,c,d))`

in the basis `1,X,...,X^(p-1)`. Delete the constant column and the row indexed by `X^(p-3)`, and call the determinant `J_a(c,d)`.

For an arbitrary, possibly non-squarefree F, the Frobenius-fixed subspace has dimension equal to the number of distinct irreducible factors. Since `deg F=p` and `a != 0`, rank `p-1` occurs exactly on the irreducible locus.

On an irreducible member, conjugating Frobenius to the permutation matrix of a p-cycle gives

`adj(Phi-I)=e_0 Tr`.

Newton's identities give

`Tr(X^(p-3))=3a`.

Therefore the selected cofactor has the exact value

`J_a(c,d)=3a * 1_(F irreducible)`.

This has been exhaustively verified pointwise for both square classes at `p=5,7,11,13`.

## 7. Sharpest current reduction to the function-field crown

Let

`N_a(p)=#{(c,d):X^p+aX^3+cX+d is irreducible}`.

Then in `F_p`,

`sum_(c,d) J_a(c,d)=3a N_a(p)`.

Thus the full d=1 function-field theorem follows from the single congruence

`sum_(c,d) J_a(c,d) != 0 mod p`.

Equivalently, let `J_a^can(c,d)` be the canonical polynomial function with degree at most `p-1` in each variable. Finite-field orthogonality gives

`sum_(c,d)J_a(c,d)=[c^(p-1)d^(p-1)]J_a^can`.

Therefore it is enough to prove that one top coefficient is nonzero.

This is currently the shortest plausible route to the function-field crown. It replaces a positive integer count of size about p by one exact coefficient computation modulo p.

## 8. Ranked open fronts

1. **Top determinant coefficient.** Compute or prove nonzero
   `[c^(p-1)d^(p-1)]J_a^can` without expanding the full determinant. This would prove FF-Fortune `(p,1)` directly.
2. **O(p) cubic and signed-quadratic sharpening.** Audit the fixed global surfaces to remove possible weight-three cohomology.
3. **Multiplicative parity sieve.** Compress products of small factors without term-by-term inclusion-exclusion through degree `p/3`.
4. **Increasing-order transfer from RQM.** This remains the original integer Fortune wall.

## 9. Immediate next action

Attack the determinant top coefficient by determinant multilinearity and finite-field orthogonality, using the Frobenius columns generated by powers of

`-aX^3-cX-d`.

The first acceptable outcome is either a closed nonzero formula or an exact recurrence in p. Failure should be documented as a structural obstruction before returning to the multiplicative parity sieve.