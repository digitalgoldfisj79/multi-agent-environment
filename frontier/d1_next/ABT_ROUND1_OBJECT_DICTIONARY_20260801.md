# ABT Round 1 — literal object dictionary

**Date:** 1 August 2026  
**Gate:** `ABT-0`  
**Result:** **PASS**  
**Remote compute:** none

## 1. Exact source and carrier

The direct application source is the sparse alternating-hook complex

\[
\mathcal K_{\mathrm{sparse}}
=R\Gamma_c(\mathcal U_p,\mathcal L_{\mathrm{hook}}),
\]

where the ordered separable sparse-root cover is the exact `S_p`-torsor of
polynomials

\[
T^p+AT^3+BT^2+CT+D.
\]

The first `p-4` coefficient directions have already been eliminated by the
Frobenius-compatible integral Fourier-delta identity. Their only contribution
is the forced Tate and even cohomological shift. The residual coefficient
coordinates are literally `(3A,2B,C)`, while `D` is the translation/punctual
direction.

The global carrier is not a local vanishing-cycle object on the smooth sparse
zero section. It is the nonzero-frequency Fourier--Cayley complex

\[
\mathcal K_\times
=\operatorname{HookAlt}R\Gamma_c(V^\times,j^*\mathcal L),
\]

in the localization triangle

\[
\mathcal K_\times
\longrightarrow
\mathcal K_{\mathrm{sparse}}(-(p-7))[-2(p-7)]
\longrightarrow
\mathcal K_X
\overset{+1}{\longrightarrow}.
\]

The desired weight-two Airy candidate, if present, must occur in
`K_times(p-7)`. It is absent from the canonical zero-frequency term by the
proved weight calculation.

## 2. Dictionary

| Item | Literal object | Degree / normalization | Arithmetic reading | Status |
|---|---|---|---|---|
| Sparse detector | `K_sparse = RΓ_c(U_p,L_hook)` | alternating hook; trace `p` on irreducible fibres | both coefficient classes | exact |
| Fixed q cell | `H_(q,epsilon)=Σ_i(-1)^i H_c^1(U_q,L_(i,epsilon))` | `U_q=P^1-{+1,-1,infinity}`; `pI_epsilon(q)=p-E_epsilon(q)` | `epsilon=A chi(q)` | exact |
| Constant projector | `S_0=Σ_(q!=0,2)(E_+(q)+E_-(q))` | raw integral q-line trace | invariant reading | exact |
| Quadratic projector | `S_chi=Σ_(q!=0,2)chi(q)(E_+(q)-E_-(q))` | raw integral q-line trace | anti-invariant reading | exact |
| Arithmetic class | `S_A=S_0+A S_chi` | `N_A=(p-2)+B_A-S_A/(2p)` | `A=+1,-1` | exact |
| `q=2` | finite coefficient slice `c=-3/2` | critical-value coordinate degenerates | reading `A chi(2)` | exact boundary object |
| `q=infinity` | coefficient slice `c=0` | count `I_A(infinity)` | class `A` | exact boundary object |
| Discriminant | fibres `t=+1,-1` | collision boundary of every generic root cover | nonsplit quadratic descent included | exact boundary object |
| Quadratic descent | split/nonsplit root-scaling torsor | unramified arithmetic quadratic twist | converts `epsilon` readings | exact |
| Main/Tate term | virtual invariant line `Q_l(-1)` in fixed-q hook formula | trace `p`; produces `p-2` after q assembly | common to both classes | exact |
| Fourier zero frequency | `K_X(p-7)` | full-codimension twist; weight `9-p` | common | exact; Airy candidate absent |
| Fourier nonzero frequency | `K_times(p-7)` | only possible weight-two transport carrier | decomposes into class projectors and boundaries | literal carrier; decomposition open |
| Airy target | `R_p((p-1)/2)` or equivalently `K_ambient((p-7)/2)` | weight two after normalization | proposed projected constituent | exact object; occurrence open |
| Artin--Schreier phase | `L_psi(<lambda,S>)` on `Tot(E^vee)` | Frobenius-compatible Fourier kernel | global, before class projection | exact |
| Affine orbit | translation/depression/root scaling on `(A,B,C,D)` | removes `B`, normalizes open `AC!=0` | creates q chart and square-class reading | exact |
| Punctual term | constant coefficient / diagonal direction `D` and deleted cyclic diagonal | endpoint correction | must be retained in crown ledger | exact carrier; final trace attachment open |
| Wild-infinity model | divided-power/Jordan Rees degeneration of the nonzero-frequency phase | associated graded is the actual Pascal graph oscillator | cyclic and arithmetic projectors required | exact proposed theorem; not constructed |

## 3. Exact boundary of the pass

`ABT-0` asks whether every source summand and correction term has a literal
carrier independent of first-trace numerics. The answer is yes.

It does **not** prove that the Airy target occurs in the nonzero-frequency
complex, with what multiplicity, or with what Tate normalization. Those are
`ABT-1` and later gates.

## 4. Source ruling

The dictionary also records two closed mechanisms:

1. local iterated vanishing cycles at the sparse zero section vanish on the
   separable locus and cannot carry the interior detector;
2. zero Fourier frequency has the wrong forced weight and cannot contain the
   normalized Airy constituent.

The only live application carrier is therefore the wild, nonzero-frequency,
divided-power Fourier sector.
