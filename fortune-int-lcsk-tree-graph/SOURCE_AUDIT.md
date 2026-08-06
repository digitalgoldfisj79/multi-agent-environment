# Source audit

## Authoritative inherited inputs

The programme is based on the validated PWOC head

`ca68b980e7222712ed0b46f939befd8ecda7f4e4`.

The local-factor inputs are inherited from `fortune-int-socg-stratified-cumulants`:

- `C1_EXECUTION.md`: common candidate universe `M_b={m:U_b<m<=H, m prime}`;
- `C3_EXECUTION.md`: exact factorial-to-ordinary Stirling transform with additive radius cost one;
- `C4_EXECUTION.md`: normalized post-terminal local factor and pair edge radius `O(X/(log X)^2)`;
- `C6_EXECUTION.md`: required factorial/ordinary cumulant radius for `INT-SOCG`.

## Exact local object

For a nonempty index set `S`, let `nu_p(S)` be the number of distinct residue classes occupied by its offsets modulo `p`. The normalized local moment is

\[
G_p(S)=\frac{1-\nu_p(S)/p}{(1-1/p)^{|S|}}.
\]

The connected prime-local coefficient is the exact partition Möbius transform

\[
\kappa_p([r])=
\sum_{\pi\in\Pi_r}(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{B\in\pi}G_p(B).
\]

No Hardy--Littlewood asymptotic, source decomposition or observed occupancy is used in the obstruction.

## Scope discipline

The programme does not modify or rely on:

- `INT-SCME`;
- the unknown PWOC source coefficient family;
- RUHL-FM source residuals;
- function-field Fortune;
- Paper VII incidence work.

The only question is whether the inherited local pair bound can be lifted to all orders by absolute tree or hyperedge domination.
