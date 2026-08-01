# ABT Round 1 — invariant gate and formal pivot

**Date:** 1 August 2026  
**Gate:** `ABT-1`  
**Result:** **RAW INTEGRAL LANE CLOSED; TATE-NORMALIZED VIRTUAL REES LANE OPEN**

## 1. Weight gate

The canonical Fourier zero-frequency contribution carries the full twist
`p-7`. Its primitive ambient hook part has weight `9-p`, whereas the desired
normalized Airy object

\[
\mathcal R_p\left(\frac{p-1}{2}\right)
=\mathcal K_{\mathrm{ambient}}\left(\frac{p-7}{2}\right)
\]

has weight two. Hence the Airy object is absent from zero frequency. Any
transport must come from the nonzero-frequency complex `K_times(p-7)`.

## 2. Whole-projector gate

The committed exact values at `p=11,17,23,29` prove that neither raw projector
`S_0` nor `S_chi` is uniformly equal, up to sign, to the normalized Airy trace
plus only the finite `q=2` and `q=infinity` boundary counts. The missing term is
a genuine nonzero-frequency Fourier contribution.

## 3. p-adic integrality gate

Write

\[
p\rho_p=\frac{T_p}{p^{(p-3)/2}}.
\]

The corrected application audit gives the exact valuation

\[
v_p(p\rho_p)=-\frac{p-17}{6}.
\]

At the committed prime `p=23` this valuation is `-1`. Therefore a uniform
identity

\[
S_A=\epsilon_A p\rho_p+E_A,
\qquad \epsilon_A\in\{+1,-1\},
\]

cannot have `E_A` equal to the trace of an honest untwisted integral q-line or
boundary complex: `S_A` and `E_A` would be algebraic integers, while the Airy
term has negative `p`-adic valuation. One exact admitted prime is enough to
exclude such a uniform raw-integral identity.

The stronger recorded valuation theorem yields the same conclusion for every
`p>17` in the sector:

\[
\boxed{\epsilon_A=0}
\]

whenever the complementary residual is an honest untwisted integral trace.

## 4. Surviving virtual possibility

A nonzero Airy coefficient remains possible only in a Tate-normalized virtual
decomposition whose complementary term carries the exact compensating
valuation. This is compatible with the Fourier localization triangle because
its zero- and nonzero-frequency pieces are individually Tate normalized even
though their sum recovers an integral raw projector.

The surviving application theorem is therefore not a direct-summand theorem
inside `S_0` or `S_chi`. It is:

> Construct a Frobenius-compatible divided-power Rees model of the wild
> nonzero-frequency phase at root infinity, identify the Airy-isotypic
> terminal quotient with the actual Pascal oscillator, and prove the exact
> Tate/integrality ledger of every complementary q-line, discriminant,
> Artin--Schreier, affine and punctual cone.

The associated-graded oscillator is already exact in every Frobenius degree:
its complete and punctured sums are `q^m` and `q^m-1`, with no Kummer or
metaplectic sign. What is open is invariance under specialization from the
nonlinear divided-power phase.

## 5. Formal programme decision

The preregistered pivot condition was a proved invariant mismatch. That
condition is met for the proposed raw-integral Airy-to-projector transport.

Consequently:

- `ABT-0`: **PASS**;
- `ABT-1`, raw integral lane: **CLOSED BY WEIGHT AND p-ADIC INTEGRALITY**;
- `ABT-2` through `ABT-4`: not opened on the raw lane;
- divided-power virtual Rees transport: preserved as a secondary genuinely
  new theorem, not treated as completed transport;
- `ITD-0`: **ACTIVATED**.

## 6. Crown boundary

Even a successful virtual Rees comparison would not by itself prove the
crown. The exact ledger shows that the remaining numerical condition is the
original q-line error-versus-main-term problem

\[
N_A-(p-2+B_A)=o(p)
\]

for at least one class, or a weaker one-sided/congruence certificate excluding
simultaneous failure. The Pascal oscillator identifies the terminal skeleton;
it does not supply this q-line estimate.
