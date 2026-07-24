# Gate \(0'\): exact dependency audit for logarithmic slack

**Date:** 2026-07-24  
**Scope:** function-field \(d=1\) Fortune sibling.  
**Status:** audit complete; the dependency needed to answer the slack question
is absent from the repository.

## 1. The two statements that must not be conflated

The current Airy theorem target is
\[
 |T_p|\le C\,p^{(p-1)/2}
\]
with an absolute constant \(C\). A factor such as \(\sqrt{\log p}\) does not
prove that statement.

The exact Fortune ledger in `D1_ATTACK.md` has a different sufficient
condition:
\[
 \left|\sum_{a\ne0}R_a\right|<(p-1)(p^p-p).
\]
The repository does not contain an identity transporting \(T_p\) into this
quantity, or into the later per-cell certificate
\(N_a\notin2p\mathbf Z_{\ge0}\).

Therefore the absolute constant is required by the *named Airy half-theorem*,
but its necessity for the *Fortune crown* is not established.

## 2. Exact dependency interface

Any completed bridge can be written, after all main, Tate,
Artin--Schreier, endpoint and boundary terms are separated, in the form
\[
 \mathcal R_p=S_p+M_pT_p,
\]
where:

- \(\mathcal R_p\) is the exact load-bearing irreducibility error;
- \(S_p\) contains every non-Airy residual term;
- \(M_p\) is the exact transport multiplicity, including Tate powers and
  parameter-cell multiplicities.

If the admissible ledger margin is \(L_p\), a bound
\[
 |T_p|\le C(p)p^{(p-1)/2}
\]
is guaranteed by the triangle inequality whenever
\[
 C(p)<B_p:=
 \frac{L_p-|S_p|}{|M_p|p^{(p-1)/2}},
 \qquad L_p>|S_p|.
\]

This is the robust decision gate when no sign correlation between \(S_p\) and
\(T_p\) is available. It is sufficient, not logically necessary: the actual
terms may cancel. It shows that, for this magnitude-only strategy:

- an absolute \(C\) is forced only if \(B_p\) stays bounded;
- \(\sqrt{\log p}\) slack is harmless if
  \(B_p/\sqrt{\log p}\) stays bounded below;
- a \(p^\varepsilon\) loss is harmless only if \(B_p\) has the corresponding
  power growth.

## 3. Repository search result

The committed files provide:

1. the exact cubic-hyperplane collapse
   \(D_*=-T_p/p\), \(D_0=(p-1)T_p/p\);
2. the exact Airy trace identity;
3. the general irreducibility ledger and its positivity threshold;
4. a list of the missing categorical and boundary obligations.

They do **not** provide \(M_p\), \(S_p\), or an equivalent exact formula.
Consequently \(B_p\) cannot be evaluated.

## 4. Ruling

`Gate 0'` is unresolved for a structural reason, not because a numerical
estimate was overlooked.

- Do not weaken the analytic target in the current theorem statement.
- Do not claim that absolute \(C\) is necessary for the Fortune crown.
- The first quantitative output demanded from any application bridge is the
  exact pair \((M_p,S_p)\), or an equivalent explicit ledger formula.
- Once that formula exists, the slack question becomes elementary.

The consultation package should therefore ask experts first whether the bridge
can be made object-level and coefficient-exact, not whether
\(\sqrt{\log p}\) can be removed from an analytic estimate in isolation.
