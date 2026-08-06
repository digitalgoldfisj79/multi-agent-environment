# B4 — lower-sieve entry obstruction

Consider any classical lower-bound linear-sieve implementation applied to a sequence supported on an interval of length `H`. Let `D` be its level of distribution and `z` the factor cutoff. The lower-sieve parameter is

\[
s=\frac{\log D}{\log z}.
\]

A positive lower linear-sieve coefficient requires `s>2`.

## Optimistic audit

No residue-class decomposition of a length-`H` sequence has a trivial exact level beyond `D=H`. Grant the optimistic ceiling

\[
D=H.
\]

The first admissible output factor already satisfies

\[
z>\ell_j\ge X>\sqrt H.
\]

Therefore

\[
\boxed{
s\le\frac{\log H}{\log z}<2.
}
\]

The obstruction is present even before using the actual distribution of prime offsets. Bombieri–Vinogradov gives only `D=H^{1/2+o(1)}`, for which `s<1` at the first admissible factor.

## Dimension-two formulation

Starting from all offsets rather than prime offsets does not help. The simultaneous conditions that `m` and `P_j+m` avoid small factors form a dimension-two sieve, whose lower-bound threshold is stricter than the dimension-one `s>2` boundary. Exact interval remainders up to `D=H` still do not reach `z>sqrt H`.

## Ruling

There is no nonempty post-primorial factor band accessible to a standard positive lower sieve. The first possible factor is already at the parity boundary, and every larger factor lies beyond it.

This closes:

- direct Brun/Selberg lower bounds;
- beta-sieve factor-band elimination;
- Bombieri–Vinogradov plus linear sieve;
- hypothetical Elliott–Halberstam-level distribution confined to the length-`H` variable.

A successful method must preserve signed Buchstab cancellation or introduce a new selected-centre incidence identity beyond the classical level parameter.
