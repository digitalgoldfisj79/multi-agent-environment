# Gate I6 — falsification and adversarial models

**Date:** 4 August 2026  
**Ruling:** PASSED; LOCAL DENSITY, FIRST MOMENT, RELATIVE SECOND MOMENT AND DENSE AVERAGING ARE INSUFFICIENT

## 1. One-defect count model

Let every centre have nominal count `K`.  Compare:

- balanced model: `Z_j=K` for all `j`;
- one-defect model:
  \[
  Z_0=0,\qquad Z_1=2K,\qquad Z_j=K\ (j\ge2).
  \]

The total first moment is identical:

\[
\sum_j Z_j=NK.
\]

The raw second moment changes only by

\[
2K^2,
\]

which is relative size `2/N=o(1)` compared with the main scale `NK^2`.  Nevertheless the
model contains a failed centre and its lower-tail energy is exactly `K^2`.

Thus:

- an exact or asymptotic first moment does not exclude failure;
- a relative `o(1)` second-moment asymptotic does not exclude failure;
- the theorem must resolve an absolute one-defect gap, not merely a relative main term.

The identities are checked in `scripts/i6_adversarial_models.py`.

## 2. Dense ambient invisibility

The primorial block has only

\[
N\asymp X/\log X
\]

centres in an ambient region whose scale is exponential in `X`.  Altering every registered
centre changes a dense-centre average by a negligible proportion.  Consequently an
exceptional-set theorem without a restriction estimate can be perfectly correct while all
primorial centres remain exceptional.

## 3. Local sieve data

Each centre has the same automatic small-prime structure: for every `q|A_X`,

\[
P_j\equiv0\pmod q.
\]

A surrogate may preserve:

- the number of offsets coprime to `A_X`;
- the local singular factors at every prime up to `X`;
- the total number of marked candidates;
- the smooth-modulus Fourier data;

while moving all marks away from one selected row.  None of these aggregate invariants
records which individual centre failed.

Classical parity constructions strengthen the point: purely sieve-theoretic divisor data
can be shared by sequences with different prime-factor parity.  Friedlander–Iwaniec's
asymptotic sieve succeeds only after adding an additional parity-breaking axiom, and the
Polymath8 parity analysis proves sharp limitations for purely sieve-theoretic prime-tuple
arguments.

## 4. Required discriminator

Any surviving method must contain information not present in the registered surrogates.
At least one of the following is required:

1. an absolute lower-tail estimate below the one-defect gap;
2. a restriction theorem specific to the increasing primorial centres;
3. parity-breaking information for the output form beyond local divisibility;
4. a zero/source correlation theorem resolving the individual primorial rows after the
   full local main term is removed.

A theorem with only relative error `o(1)`, density-one output or smooth-modulus local data
cannot close Fortune.

## 5. Gate ruling

I6 passes as a no-go classification.  It does not create a counterexample to Fortune or to
the prime model.  It proves that the following input package is logically insufficient:

- local admissibility and singular series;
- exact block first moment;
- relative second-moment accuracy;
- dense-centre almost-all control;
- smooth-modulus centre geometry.

The missing theorem must have **one-defect resolution** on the actual selected centres.
`INT-PSLT` has exactly that resolution and is therefore retained as the terminal new
theorem.
