# Consultation package: characteristic-boundary cubic Airy correlation

**Prepared:** 2026-07-24  
**Project:** function-field \(d=1\) Fortune sibling  
**Author/contact for the project:** Edward Stewart Anthony Bozzard,
ORCID `0009-0002-4052-0994`

## Executive statement

For primes \(p\equiv5\pmod6\), the programme reduces a function-field Fortune
sector to two explicit open theorems. The analytic theorem is the absolute
correlation bound
\[
 \left|\operatorname{Tr}(F\mid U_p)
 -p\operatorname{Tr}(F\mid U_{p-2})\right|
 \le C p^{(p+1)/2},
\]
where
\[
 U_k=H_c^1(\mathbf A^1_{\overline{\mathbf F}_p},
           \operatorname{Sym}^k\mathcal A)^{\mu_3}
\]
for the rank-two cubic Airy sheaf. Both spaces have rank
\((p-5)/6\). The application theorem must then identify this Airy boundary
complex with the load-bearing nearby-cycle/hook component in the exact
irreducibility ledger.

## What is already proved

1. Cubing symmetry collapses the full nonzero cubic-fibre deviation to one
   integer:
   \[
   D_*=-T_p/p,\qquad D_0=(p-1)T_p/p.
   \]
2. The Airy identity is exact:
   \[
   pT_p=\operatorname{Tr}(F\mid U_p)
        -p\operatorname{Tr}(F\mid U_{p-2}).
   \]
3. The \(p\)-th Adams virtual sheaf has zero Swan conductor at infinity, but
   the characteristic-zero global class has negative irreducible
   multiplicity; local rank-two collapse does not globalize.
4. The canonical lift of the modular Adams sequence has full-rank defect,
   including full rank after the \(\mu_3\) projection.
5. Hodge spectra of the two characteristic-zero motives are disjoint, so a
   characteristic-zero cross-\(k\) correspondence is obstructed.
6. Exact \(F\) and \(F^3\) traces determine the low-rank spectra at
   \(p=17,23,29\), now reproduced by a second implementation.
7. Common-factor cancellation, matched Newton slopes, torsion phases,
   bounded-degree Gaussian periods and bare cyclic localization have exact
   failure certificates.

## Two questions for Airy/Dwork specialists

### Question A: boundary correlation

Is there a Frobenius-dependent identity at the exceptional boundary
\(k=p\) that can pair the \(\mu_3\)-invariant parts of
\(\operatorname{Sym}^p\mathcal A\) and
\(\operatorname{Sym}^{p-2}\mathcal A(-1)\) with \(O(1)\) trace defect, even
though their characteristic-zero Hodge structures admit no morphism?

Equivalent formulations available in the package are:

- square-root cancellation in
  \(\sum_{u\ne0}\cos(p\theta_u)\);
- cancellation between two full real-cyclotomic Dickson field traces;
- a Frobenius-equivariant cancellation on Haessig's explicit Dwork basis.

### Question B: root numbers and motive recognition

For \(p\equiv11\pmod{12}\), odd rank forces a rational central Frobenius
eigenvalue. At \(p=23\), the central signs of \(U_p\) and \(U_{p-2}(-1)\)
agree and cancel; at \(p=11\), they are opposite.

Can the sign be computed from an epsilon-factor/root-number formula for the
Airy moment motive?

At \(p=17\),
\[
 \lambda=17^8\frac{29\pm3i\sqrt{35}}2,
\]
and the factor \((29\pm3i\sqrt{35})/2\) is an algebraic integer of norm
\(17^2\) in \(\mathbf Q(\sqrt{-35})\). Is this rank-two motive recognizable
within an existing Airy-moment or modular/CM construction?

## Question for nearby-cycle specialists

Can one construct an object-level comparison between the cubic
trace-zero/Airy boundary complex and the post-pushforward even--odd hook
complex controlling irreducible fibres, including:

- main/Tate/Artin--Schreier subtraction;
- the punctual \(b=0\) term;
- the arithmetic quadratic twist at infinity;
- \(q=2\) and \(q=\infty\) boundary cones?

The first quantitative output needed is the exact transport coefficient of
\(T_p\) in the irreducibility ledger. Without it, it is unknown whether the
crown needs an absolute constant or tolerates logarithmic slack.

## Suggested routing

1. **C. Douglas Haessig** — explicit \(p\)-adic Airy decomposition and the
   denominator boundary at \(k=p\). University of Arizona,
   `haessig@arizona.edu`.
2. **Antonio Rojas-León** — \(\ell\)-adic Airy sheaves, local factors,
   monodromy and symmetric-power degrees. Universidad de Sevilla,
   `arojas@us.es`.
3. **Ping-Hsun Chuang** — arithmetic Picard--Lefschetz corrections and the
   global-versus-local scope of arXiv:2607.05757.
4. **Claude Sabbah, Jeng-Daw Yu, Yichen Qin** — Hodge structures, central
   signs and motive recognition for Airy moments.
5. **Will Sawin** — uniform trace cancellation when rank/frequency grows with
   the characteristic.

The first contact should be Haessig/Rojas-León with Question A. The second
should be Chuang with the application and central-sign questions. Hodge/motive
recognition and the general uniformity question can follow with the exact
spectral table attached.

## Attachments/read order

1. `CURRENT_STATUS_20260724.md`
2. `GATE0_PRIME_DEPENDENCY_AUDIT_20260724.md`
3. `BRIDGE_ASSESSMENT_20260724.md`
4. `F3_PREREG8_INDEPENDENT_VERIFICATION_20260724.md`
5. `AIRY_ODD_POWER_SPECTRA_AUDIT_20260723.md`
6. `APPLICATION_LEDGER_AND_ROUTE_EXHAUSTION_20260723.md`
7. `CHUANG_2607_05757_END_TO_END_AUDIT.md`
8. reproducibility scripts under `prereg8/`

## Primary references

- C. D. Haessig and A. Rojas-León, *L-functions of symmetric powers of the
  generalized Airy family of exponential sums: ell-adic and p-adic methods*,
  arXiv:0908.1240.
- C. Sabbah and J.-D. Yu, *Hodge properties of Airy moments*,
  arXiv:2112.13405.
- Y. Qin, *Hodge numbers of motives attached to Kloosterman and Airy
  moments*, arXiv:2302.05365.
- P.-H. Chuang, *On the Generalized Arithmetic Picard--Lefschetz Formula*,
  arXiv:2607.05757.
