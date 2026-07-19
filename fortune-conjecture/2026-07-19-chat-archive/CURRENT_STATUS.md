# Fortune's Conjecture Programme — Current Status

Date: 2026-07-19

## Objective

Let \(P_n=p_n\#\) and let \(F_n\) be the least \(m>1\) such that \(P_n+m\) is prime. Every prime factor of \(F_n\) exceeds \(p_n\); hence, if \(F_n\) is composite,

\[
F_n\ge p_{n+1}^2.
\]

It is therefore enough to prove that every sufficiently large primorial has a prime within an interval of length below \(p_{n+1}^2\).

## Active reduction chain

Within the current fourth-moment / reciprocal-frame architecture, the active sufficient chain is

\[
\mathrm{PGD2}
\Longrightarrow
\mathrm{SHF2}
\Longrightarrow
\mathrm{PC\!-FROB2}
\Longrightarrow
\text{centred connected traces}
\Longrightarrow
\mathrm{PC\!-PSLF2}
\Longrightarrow
\mathrm{LFAM4}
\Longrightarrow
\mathrm{PC\!-ADFSR4}
\Longrightarrow
\text{Fortune for all sufficiently large }n.
\]

These are sufficient targets within this chosen architecture, not logically necessary conditions for every possible proof of Fortune's conjecture.

## Immediate target: one-harmonic prime-gap dispersion

Let

\[
F(\theta)=\sum_{j<N}e(\theta P_j),
\qquad
H_2(\theta)=\frac{F(\theta)^2+F(2\theta)}2,
\qquad
M=\frac{N(N+1)}2.
\]

For the positive harmonic \(a\), define

\[
\Psi_a(L)=\sum_{q\sim Q}p_{q,a}e(aL/q).
\]

After Schwartz-tail truncation and Cauchy-Schwarz, it is sufficient to prove uniformly for \(a\le X^{o(1)}\)

\[
\mathcal E_a
=
\sum_{u\ne v}|\Psi_a(S_u-S_v)|^2
\ll MX^{o(1)}.
\tag{SHF2}
\]

Writing \(r=q+h\), the unresolved distinct-prime part is

\[
\mathcal R_a
=
\sum_{0<|h|<Q}
\sum_{\substack{q\sim Q\\q,\ q+h\ \mathrm{prime}}}
p_{q,a}p_{q+h,a}
\left(
\left|H_2\!\left(\frac{ah}{q(q+h)}\right)\right|^2-M
\right).
\]

The current sufficient target is

\[
\boxed{
\mathcal R_a\ll MX^{o(1)}
\quad\text{uniformly for }a\le X^{o(1)}.
}
\tag{PGD2}
\]

The change \((q,r)\mapsto(q,h)\) is only a bijection. It has not yet been shown to lower the analytic rank. The next programme must apply a strict stop rule: continue only if fixing \(a\) exposes a real averaging mechanism in \(h\), a centred prime-pair majorant, or a bilinear structure with a genuine rank surplus; stop if the result merely restates PC-FROB2.

## What has been established exactly

The following items have exact proofs or exact algebraic validation in the archived packages:

1. FC4 high-moment implication and the all-distinct fourth-moment reduction.
2. Exact collision-partition identity for ordered all-distinct offsets.
3. Large-factor ownership in the four-copy CRT kernel.
4. Unique owned-frame zero frequency.
5. Stable zero mode equals the modified singular-series contribution.
6. Exact pair lift
   \[
   F_{q,a}(c)^2=\sum_{j\le k}d_{jk}(c)e(a(P_j+P_k)/q),
   \]
   with
   \[
   \|d(c)\|_2^2=2\|c\|_2^4-\|c\|_4^4.
   \]
7. Integer pair-sum Sidon theorem for the primorial prefix path.
8. Correction of PSLF2: the zero frequency \(a=0\) must be removed. The active target is principal-cancelled PC-PSLF2.
9. Exact dual-row identity
   \[
   (VV^*)_{t,t'}=
   \frac{\sqrt{w_tw_{t'}}}{2}
   \left(F(\alpha_t-\alpha_{t'})^2+F(2\alpha_t-2\alpha_{t'})\right).
   \]
10. Bounded primorial-relation rigidity.
11. Exact PC-FROB2 endpoint-sector decomposition and collapse to the single \(H_2\) polynomial.
12. Exact same-modulus closure, small reciprocal-numerator closure, and polylogarithmic endpoint-span closure.
13. Exact row-denominator dissociation for bounded low-frequency rows.
14. Exact fixed-numerator CRT identity and proof that \(ar-bq\) is only a relabelling, not a rank reduction.
15. Valid harmonic diagonal reduction from all numerator pairs to separate positive harmonics.

## Route-specific no-go results

These are closures of particular proof routes, not impossibility theorems for Fortune itself:

- multiplicative-character expansion loses the full product-character dimension;
- the original unrestricted PSLF2 including \(a=0\) is false;
- complete-frequency additive fourth moment loses \(H^{1/4}/\log H\) at the critical shell;
- raw growing traces cannot bypass the base second-moment target;
- positive rough-number majorants introduce strong rank-one resonances;
- separate exact pre-sieve or Möbius/Vaughan bands are badly conditioned in every tested operator, Frobenius, and scalar formulation;
- fixed \((a,b)\) and the variable \(ar-bq\) do not lower rank;
- finite-coordinate phase-alignment certificates do not capture the diffuse high-value mechanism;
- generic fixed-base or sparse-modulus large-sieve theorems do not directly cover the consecutive-prime-product chain.

Some no-go statements are exact algebraic losses; others are finite conditioning diagnostics. Consult each package's report for its epistemic status.

## Finite complete-shell evidence

The finite calculations are diagnostics, not asymptotic proofs.

- PC-PSLF2 normalized spectral edge:
  - \(X=350\): actual about 1.57, matched control about 1.57.
  - \(X=700\): actual about 1.53, matched control about 1.53.
- Complete maximum coherence:
  \[
  N\max_{u\ne v}|\Phi_X(S_u-S_v)|
  =1.6924,\ 1.8014,\ 1.9955
  \]
  at \(X=350,700,1200\).
  These are consistent with the independent-unit random-floor extreme-value law, not evidence by themselves for an \(X^{o(1)}\) theorem.
- Real-Gaussian entry moments through order 16 agree closely with the matched null at \(X=350,700\).
- At \(X=700\), the first three positive harmonics account for about 99.7% of measured one-harmonic surrogate energy, and each harmonic is almost entirely explained by its exact row-diagonal null.

## Key caution on terminology

PC-FROB2, U4RF, HRPS4, SHF2, PGD2 and ECM are unproved targets or hypotheses. Do not call them theorems. PC-FROB2 is sufficient and unavoidable within the present local trace/cumulant chain, but no result proves that every possible proof of Fortune's conjecture must establish it.

## Recommended next analytic programme

1. Freeze one harmonic \(a\), initially \(a=1\).
2. Expand the centred prime-gap expression without splitting signed prime-detection pieces absolutely.
3. Partition by prime gap \(h\), endpoint transport, and any genuine stationary/nonstationary phase parameter.
4. Search for a centred dispersion identity in which the exact \(-M\) term removes the diagonal before Cauchy-Schwarz.
5. Test whether a prime-pair correlation or Selberg-sieve majorant can preserve centring. Positive uncentred majorants are forbidden by the earlier resonance counterexamples.
6. Maintain an exact exponent ledger. The required total scale is \(MX^{o(1)}\).
7. Stop if the resulting form is just PC-FROB2, HTE4, or the full two-prime reciprocal kernel with renamed variables.
8. Use Hugging Face only for theorem-directed diagnostics after the algebra is frozen.

## Archive contents

The complete 160-file workspace is preserved in the persistent ChatGPT Library as `Fortune-Conjecture/2026-07-19-chat-archive/fortune_conjecture_chat_workspace_20260719.zip`. GitHub contains the calibrated handover, full file manifest and checksums. The binary ZIP could not be committed through the connector's text-only write endpoint.
