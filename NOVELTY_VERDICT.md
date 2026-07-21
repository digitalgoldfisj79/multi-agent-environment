# Novelty verdict: the quantized Kloosterman identity (Theorem D1.3)

**Date:** 2026-07-21.
**Object under review:** for odd prime \(p\), \(Q=p^p\),
\(N(p)=\#\{d:\ x^p+x^2+d\ \text{irreducible over }\mathbb F_p\}\);
the identities \(N(p)=p^{-p}G_QS(p)\),
\(T_u=\eta(-1)G_Q(R(u)-1)\), \(S(p)=\eta(-1)G_QN(p)\)
(D1_ATTACK.md, Theorem D1.3), equivalently the exact count of
irreducibles of degree \(p\) over \(\mathbb F_p\) with the top \(p-3\)
coefficients vanishing.
**Process:** a retrieval agent read the reachable corpus; an independent
auditor re-retrieved every quoted source, verified all quotations
verbatim, re-verified the numerics with its own code, and ran four fresh
searches under different terminology. Full records:
`frontier/rqm_workbench/{novelty,litaudit}.json`.

## Verdict

**METHOD KNOWN, RESULT NEW AS STATED** — formally: *novel pending manual
inspection of the named offline sources below*.

- The proof mechanism is classical and was retrieved verbatim in
  multiple places: orthogonality double-evaluation, Gaussian collapse,
  Hasse–Davenport; the phenomenon class of twisted Kloosterman/Weil sums
  taking values on a Gauss-sum-times-integer lattice appears in Salié's
  evaluation, in Katz–Livné / Lachaud–Wolfmann (Kloosterman sums as
  elliptic-curve point counts, via Moisio arXiv:0706.2112, whose exact
  hyper-Kloosterman identity for degree \(p^k\) with prescribed
  trace+norm was independently re-verified numerically at \(q=p=5\)),
  and in Weil-sum quantization via incidence counts (Nguyen
  arXiv:2006.15726, Prop 4.1).
- The specific objects — the \(\eta\)-twisted sum over
  \(\ker\mathrm{Tr}\) in \(\mathbb F_{p^p}\) with Frobenius-negative-power
  argument \(\mathrm{Tr}(\tau^{2-p})\), the per-hyperplane collapse to
  root counts, and the application to the extreme-sparse family
  \(x^p+x^2+d\) (degree = characteristic, \(p-3\) prescribed
  coefficients) — appear **nowhere in the retrievable literature**.
- Strong corroboration that the regime itself is recognized as open:
  Granger (arXiv:1610.06878; FFA 2019) requires \(n\) coprime to \(p\),
  states verbatim that his method "breaks for \(l\ge p\) due to the
  failure of Newton's identities in positive characteristic", and his
  Problem 4 declares the \(n\equiv0\pmod p\) cases open; the best
  existence technology (Ha, arXiv:1601.06867) caps prescribed
  coefficients at \(n/4\); the exact-count corpus stops at \(\le7\)
  prescribed coefficients over tiny fields; and the auditor's fresh
  search surfaced Kolekar (arXiv:2512.08994, Dec 2025), whose main
  theorem itself requires \(n<p\) and whose Question 5.1 explicitly
  lists \(p\ge n\) as open. (Note: our identity evades the
  Newton-identity obstruction because only \(k\le p-3<p\) power sums are
  used — the reformulation was independently re-proved and verified at
  \(p=5,7,11,13\).)
- Honest caveat retained from the review: the identity is analytically
  self-referential — its content is diagnostic (it explains why the
  quadratic family is criticality-quantized), not evaluative; it does
  not by itself count anything new.

## Sources requiring manual inspection before a publication-grade novelty claim

Unreachable in this environment; each named with what must be checked:

1. Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups* (1988) —
   any exact lattice-valued evaluation of trace-restricted twisted sums.
2. Katz (1993, Soto-Andrade sums) — quantized evaluations over
   extension fields.
3. Coulter, Acta Arith. 83 and 86 (1998) — explicit Weil-sum
   evaluations in characteristic \(p\); closest classical antecedents to
   the Gaussian-collapse step.
4. Kuz'min (1990/1991) — irreducibles with several prescribed
   coefficients; Russian school.
5. Carlitz (1952/1969/1979 originals) — prescribed-trace counts;
   verify no sparse-family corollary.
6. Fitzgerald–Yucas (2003) — prescribed trace/norm counts.
7. Kononen–Rintala–Vaskouski — prescribed trace and norm exact counts.
8. Salié (1932 original) — the evaluation method at its source.

## Consequence for the manuscripts

D1_ATTACK.md's novelty caveat stands in refined form: the identity may
be presented as *new as stated, with the method classical*, provided the
eight sources above are checked before submission and the
Granger/Kolekar open-problem statements are cited as evidence that the
counting regime itself is recognized as open.
