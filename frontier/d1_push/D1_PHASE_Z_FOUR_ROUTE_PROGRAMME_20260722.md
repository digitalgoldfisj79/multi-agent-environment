# d=1 crown push — Phase Z four-route programme

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Starting head:** `784bf0fc3921ed916f9f91460e66039e17c3bd80`  
**Status:** active programme. The p=29 counterexample has closed the hard Cartier support-cutoff route; the function-field d=1 crown remains open.

## Objective

For prime p>=5 and fixed a!=0, let

`N_a(p)=#{(c,d) in F_p^2 : X^p+aX^3+cX+d is irreducible}.`

The Cartier certificate gives an exact congruence

`S_a(p)=3a N_a(p) mod p.`

It is enough to prove that, for at least one square class of a,

`S_a(p)!=0 mod p`,

or otherwise prove `N_a(p)>0` directly.

The former support-cutoff plan is false at p=29. Phase Z pursues four replacement routes without deleting the above-bound tail.

## Route 1 — tail-inclusive Cartier assembly

### Z1.1 Full survivor ledger

For each audited prime and both square classes of a, extract every torus-surviving coefficient

`[c^(alpha(p-1)) d^(beta(p-1))] det(I-H)`

with exact arithmetic. Record:

- `(alpha,beta)` and filtration weight;
- dominant-w=1 and full-w=1..4 values;
- support below/at/above the former boundary;
- square-class dependence in a;
- cumulative low/boundary/tail sums.

Start at p=17,19,23,29 and extend as compute permits.

### Z1.2 Exact assembly object

Use the proved factorisation

`([X^q]G^n)=F(d)E(a,c)`

and Cauchy-Binet to write the complete torus projection as a finite sum of products

`det((n)_m) det(B(q,m))`

over identity selections and degree sets. Seek:

1. a transfer-matrix or exterior-power formula;
2. a recurrence in the identity subset;
3. a complementary-minor/Jacobi reformulation;
4. an involution or pairing only after the complete torus projection;
5. a closed determinant over the group algebra of `(F_p^*)^2`.

A theorem may allow nonzero tail coefficients; it must control their assembled sum.

## Route 2 — quantized nonvanishing

### Z2.1 Exact slice ledger

For both square classes compute or import exact values of `N_+(p),N_-(p)` and the residues `S_+,S_-` over the certified prime range. Record:

- zero and nonzero slices;
- multiples of p;
- ratios `N_a/p`;
- total and difference;
- residues modulo `2p`, `4p`, and small auxiliary moduli;
- character correlations.

### Z2.2 Candidate exact mechanisms

Test and either prove or refute:

1. `0<N_a<2p` for at least one square class;
2. `N_++N_-` lies in a residue class incompatible with both being multiples of p;
3. a parity or orbit refinement stronger than `2|N_a`;
4. a congruence for `S_+ +/- S_-` from the Cartier a-grading;
5. a resultant/discriminant mass congruence excluding simultaneous certificate vanishing.

No statistical fit is a theorem. Computation is used only to identify or refute exact statements.

## Route 3 — geometric direct-image remainder

### Z3.1 Define the primitive remainder

Subtract from the full even/odd hook ledger:

- the proved weight-zero Kummer class;
- the pair-curve factor `H^1(B_q)^-`;
- the discriminant-twist factor `H^1(D_q)`;
- all explicit split/nonsplit q-averages, including the discriminant-24 and discriminant-40 CM motives.

Denote the residual q-family by `P_q`.

### Z3.2 Structural tests

Determine exactly:

1. self-duality and sign of the pairing on `P_q`;
2. root-negation and quadratic-descent actions;
3. whether the q-average of `Tr(Frob|P_q)` has forced divisibility or vanishing;
4. whether `P_q` is induced from lower-degree configuration covers;
5. whether its total-space cohomology has bounded, rather than growing, transcendental rank.

The configuration trace identity itself is circular and cannot be reused as positivity.

## Route 4 — singular-series and mass formula

### Z4.1 Exact factor-degree ledger

For the two-parameter depressed slice, derive exact counts of members with:

- a linear factor;
- two prescribed distinct linear factors;
- a repeated factor/discriminant zero;
- a factor of degree r for small fixed r;
- specified Frobenius cycle statistics expressible through low hooks.

The known exact rootless count `(p^2-1)/3` is the first term.

### Z4.2 Main-term or exact mass target

Seek either:

`N_a(p)=sigma_a(p)p+E_a(p)` with sigma_a bounded below and `|E_a|<sigma_a p`,

or an exact mass/congruence ruling out `N_a=0` simultaneously in both square classes.

Candidate tools:

- inclusion-exclusion over factor degrees;
- Stickelberger/discriminant characters;
- resultants with irreducible polynomials of degree r;
- cycle-index/hook character identities with independently controlled low-degree masses;
- affine-orbit mass formulas.

## Audit and evidence rules

- Exact arithmetic only for determinant and congruence claims.
- Every script, raw result, theorem/counterexample note, and status update is committed.
- Finite evidence is not promoted to a uniform theorem.
- Integer Fortune remains a separate layer.
- Closed routes are not revived: no hard Cartier support cutoff, no configuration identity as positivity, and no generic character-moment diversion detached from a d=1 gate.

## Stop conditions

Stop at the first natural theorem-level point:

1. an exact tail-inclusive Cartier assembly theorem;
2. an exact congruence excluding simultaneous certificate vanishing;
3. a structural theorem reducing the primitive geometric remainder to bounded-rank motives;
4. a singular-series/mass theorem proving `N_a>0`;
5. a precise counterexample closing one of these replacement mechanisms;
6. all four routes reduced to explicit named lemmas with no further computational ambiguity.
