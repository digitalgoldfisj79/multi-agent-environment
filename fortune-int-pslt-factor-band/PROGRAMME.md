# Programme

## Rule

Every round must improve an exact threshold, prove an implication, or close a method at a reproducible exponent obstruction. Equivalent notation, finite scans, and generic short-interval citations are not progress.

## B0 — source freeze

Pin PR #49, issue #50, the candidate-collapse theorem, the shifted von Mangoldt source, and the kernel-checked lower-tail criterion.

Pass: exact source and one-failure implication reproduced.

## B1 — prime-power threshold compression

For `L_j=log(P_j+H)` and `K_j=floor(L_j/log 2)`, prove the explicit failed-centre cap

\[
R_j(H)\le L_j\sum_{k=2}^{K_j}\frac1k.
\]

Freeze a deterministic threshold

\[
B_j=2L_j\sum_{k=2}^{K_j}\frac1k\asymp X\log X.
\]

Pass: the variable-threshold lower-tail theorem is formally sufficient for eventual Fortune.

Kill: any claimed further improvement that requires an unproved uniform gap theorem between distinct perfect powers.

## B2 — defect propagation

Audit the only natural recurrence map induced by

\[
P_{j+1}=\ell_{j+1}P_j.
\]

The corresponding offset map is `m -> ell_{j+1} m`. Determine whether an admissible offset can remain inside the next window.

Pass: a propagation theorem yielding a growing cluster of failed rows.

Alternative close: prove that the natural map sends every admissible offset outside the window and construct a local-congruence-preserving isolated-defect surrogate.

## B3 — exact least-factor/Buchstab identity

Let

\[
\mathcal A_j=\{m:\ell_j<m\le H,\ m\text{ prime}\}.
\]

For composite `P_j+m`, write `r=P^-(P_j+m)`. Derive the exact partition

\[
|\mathcal A_j|=Z_j(H)+\sum_{\ell_j<r\le\sqrt{P_j+H}}M_j(r),
\]

where `M_j(r)` counts candidate offsets whose output has least prime factor `r`.

Pass: uniqueness, endpoints, and the implication from failure to complete least-factor coverage verified.

## B4 — sieve-level audit

Compare the first admissible factor `r>ell_j` with every available distribution level `D` for a sequence of length `H`.

The decisive parameter is

\[
s=\frac{\log D}{\log r}.
\]

A classical lower linear sieve needs `s>2`. Audit the optimistic ceiling `D=H`, not merely Bombieri–Vinogradov.

Pass: identify a nonempty factor band with a positive lower-sieve coefficient.

Alternative close: prove that `r>ell_j>sqrt(H)` forces `s<2` even at `D=H`; hence no classical lower-bound sieve enters the post-primorial factor range.

## B5 — divisor switching and critical incidence

Derive the dyadic thin-hyperbola form

\[
rs-P_j=m,\qquad 0<m\le H,\qquad m\text{ prime},\qquad r=P^-(rs)>\ell_j.
\]

Separate `ell_j<r<=H` from `r>H`. For `r>H`, prove offset injectivity. For `r<=H`, retain exact congruence multiplicity.

Promotion: a named signed incidence theorem whose estimate resolves one failed row.

Close: isolate one exact post-level incidence theorem and prove that all standard absolute-value, dense-centre, and frame estimates miss its required scale.

## B6 — one-defect resolution

Convert the surviving incidence theorem into

\[
\sum_j(B_j-\Psi_j(H))_+^2=o((\min_j B_j)^2).
\]

Density-one success or `o(N)` failures do not pass.

## B7 — closeout

Allowed terminal statuses:

- `PROVED_INT_PSLT`;
- `REDUCED_TO_ESTABLISHED_THEOREM`;
- `REDUCED_TO_CRITICAL_FACTOR_INCIDENCE`;
- `DEFECT_PROPAGATION_REDUCTION`;
- `METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE`.

Closeout requires a full static/formal build, independent scale scripts, exact consequences for Fortune, and zero active programme compute jobs.
