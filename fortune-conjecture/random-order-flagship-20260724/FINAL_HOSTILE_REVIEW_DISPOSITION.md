# Disposition of final hostile review

## Reviewed object

- Manuscript: `publications/fortune-papers-ii-vi-20260724/paper4_random_order/manuscript.md`
- Manuscript SHA-256: `548460849cc9c6125fbe59d0a4f2f37ec680761174c25556b5e781a8ae9372f1`
- Model: `Qwen/Qwen3-14B-AWQ`
- Hugging Face job: `6a6325e7db23d7a7ec1ca14a`
- Archived raw output: `FRESH_HOSTILE_REVIEW_FINAL_QWEN3_14B_AWQ.md`
- Headline verdict: **proved**

The model nevertheless listed one “major” and two “minor” defects. Each is disposed of below against the exact reviewed manuscript and independent reconstruction.

## Finding 1 — alleged failure of the multiplicity identity

**Raw claim.** Equation (3.3) allegedly does not equal `M(M-1)`.

**Disposition: false; rebutted algebraically and computationally.**

The manuscript states

`N^2(N-1) + N(N-1) + 6*C(N,3) + 6*C(N,4)`.

The first two terms equal

`N(N-1)(N+1)`.

The last two terms equal

`N(N-1)(N-2)(N+1)/4`.

Their sum is

`N(N+1)(N-1)(N+2)/4`.

Since `M=N(N+1)/2` and

`N(N+1)-2=(N-1)(N+2)`, one has

`M(M-1)=N(N+1)(N-1)(N+2)/4`.

The identity is exact. In addition, `INDEPENDENT_LEDGER_RECONSTRUCTION.md` enumerates every ordered pair of two-element multisets for `N=3,...,10`, reproduces `M(M-1)`, and verifies the exact multiplicity `N` for type S and `1` otherwise. No defect remains.

## Finding 2 — alleged missing largeness condition in Lemma 5.2

**Raw claim.** The manuscript allegedly fails to state the condition needed for `8X^3 < eta^2 X^4 <= qr`.

**Disposition: false; the condition is explicit.**

Lemma 5.2 begins: **“For `X>8/eta^2`”**. Under that condition,

`8X^3 < eta^2 X^4 = H^2 <= qr`.

The proof also states that all six block primes are units modulo `qr`, converts the congruence to integer equality, and counts at most `6K^3` ordered solutions, with fewer rather than more when primes repeat. No repair is required.

## Finding 3 — alleged unquantified constants in Lemma 6.3

**Raw claim.** The proof allegedly does not rigorously bound the contour prefactor or number of patterns.

**Disposition: false; both quantities are explicit.**

The reviewed proof defines `U(P)` as the right-hand side of the matching bound and establishes

`U(P)/U(P0) <= C_* K^2 X^{-30f} product L1/(beta SUP)`.

It then states:

- `C_*K^2 <= 540X^2` from (2.4);
- `L1/(beta SUP) <= 4 eta^2 X^4` for either group size;
- therefore `U(P)/U(P0) <= X^{-23f}` for sufficiently large `X`;
- there are at most four ratio coordinates, hence exactly at most `2^4-1=15` non-all-bad patterns; and
- `sum_P Sigma(P) <= sum_P U(P) <= (1+15X^{-23})U(P0) <= 2U(P0)`.

The model's objection repeats constants already present in the proof. No defect remains.

## Gate decision

The final fresh hostile review has no unresolved fatal or major mathematical issue. Its headline verdict is **proved**, and every listed objection is rebutted by explicit text, exact algebra, or the independent configuration enumeration.

This closes the manuscript-only hostile-review gate. It does **not** constitute human peer review and does not close compiled-artifact integrity or specialist-review gates.
