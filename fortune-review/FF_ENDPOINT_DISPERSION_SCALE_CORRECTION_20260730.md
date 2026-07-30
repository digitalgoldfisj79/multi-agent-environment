# Correction: sampled diagonal scale in the endpoint dispersion audit

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

This note corrects the status language in `FF_ENDPOINT_DISPERSION_AUDIT_AND_CENTERED_DOUBLE_GATE_20260730.md`, especially Sections 0, 2, 3 and 10. The authoritative formulation is now in `FORTUNE_MECHANISM_MAP_CORRECTED_20260730.md`.

## Exact identity

The first dispersion contains the positive diagonal

`D_diag(theta)=q^m M_samp(theta)`,

where

`M_samp(theta)=sum_{P!=S}|Ahat_P(mu_PS)|^2`.

This identity is **PROVED EXACTLY**.

If the class correlation satisfies `C(theta)=O(Diag)`, source Cauchy gives a bound of the form

`|T(theta)| << q^m M_samp(theta)^(1/2) poly(k,m)`.

Consequently, class control alone implies endpoint `FFPR` only if

`M_samp(theta) << q^(3k) poly(k,m)`.

This logical insufficiency of `C=O(Diag)` by itself is **PROVED EXACTLY**.

## Conditional natural-scale ledger

The full all-frequency Plancherel mass is on the `q^(m+k)` scale in the relevant large-field regime. If the deterministic sampled frequencies have the corresponding natural scale

`M_samp(theta) ~ q^(m+2k) poly(k,m)`,

then first dispersion gives

`|T(theta)| << q^(3m/2+k) poly(k,m)`,

leaving `q^((m-k)/2)` above the target, or `q^((k-1)/2)` at `m=2k-1`.

This exponent ledger is **CONDITIONAL** on the sampled-frequency scale. Keating–Rudnick controls the all-residue variance in its literal regime; it does not prove a lower bound or asymptotic for the deterministic subset `mu_PS`. The committed finite panels support the natural sampled scale but cannot establish it asymptotically.

## Correct endpoint alternatives

There are therefore two logically possible endpoint routes:

1. prove the exceptional sampled-diagonal saving
   
   `M_samp(theta) << q^(3k) poly(k,m)`,
   
   together with class control and the exact `Delta_PS` correction; or
2. prove a centered bilateral theorem that removes both source diagonals before positivity and retains the Lambda weights, reciprocity and `Delta_PS`.

The first route is much stronger than ordinary `FFV-generic`; the second is `CBEA_FF`. Neither is presently proved.

## Status correction

### PROVED EXACTLY

- the positive-diagonal identity;
- the required sampled-mass threshold `q^(3k)` for a post-Cauchy/class-control proof;
- the logical statement that `C=O(Diag)` alone does not imply `FFPR`.

### CONDITIONAL

- the `q^((m-k)/2)` deficit under the natural sampled-frequency scale.

### RETRACTED OR CORRECTED

- any claim that `M_samp(theta) ~ q^(m+2k)` is an unconditional theorem;
- any claim that the first-dispersion exponent deficit is unconditional.

### OPEN

- the actual scale of `M_samp(theta)` uniformly at deterministic primorial frequencies;
- the exceptional `q^(3k)` sampled-diagonal bound;
- `CBEA_FF` and the exceptional bilateral-incidence components;
- corrected endpoint `FFPR`.
