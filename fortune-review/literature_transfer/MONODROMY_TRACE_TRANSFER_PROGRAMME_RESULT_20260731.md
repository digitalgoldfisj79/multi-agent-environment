# Monodromy and trace transfer programme — audited result

**Date:** 31 July 2026  
**Programme branch:** `gpt56/fortune-monodromy-trace-transfer-20260731`  
**Input TFP3 head:** `e5ef12c0f2fa39f50b623f621a998c0f65f99c6e`  
**Latest direct d=1 head audited:** `c331f740e06a95e5596639800c931e2629ff9178`

## 0. Executive ruling

The published literature is technically actionable, but it is not a plug-in
proof of either TFP3 or the function-field `d=1` crown.

Two lines must remain separate:

1. **Paper VII / TFP3:** a fixed-degree bilateral endpoint-incidence geometry
   problem. Published finite-cover, monodromy, Lang--Weil and Chebotarev
   machinery can be used after a custom curve and torsor theorem is proved.
2. **Direct d=1 crown:** a growing-degree Airy first-moment and application
   transport problem. Published short-trace theorems do not remove its two
   remaining theorem-hard walls.

No result in this programme is counted as progress toward integer Fortune
without a separate transfer theorem.

## 1. Corrections discovered before transfer

### 1.1 `rho=1` is allowed in nonzero defect

The prior independent verifier rejected normalized `rho=1`. This was a logic
error. The proved implication is

\[
h=0\Longrightarrow \rho=1,
\]

not its converse.

The classifier contains two `q=97` true-Frobenius records with `rho=1`. Both
have four distinct irreducible cubics, satisfy all four original inverse-free
divisibilities, and have a nonzero common defect polynomial of degree `89`.
The verifier is corrected to require only `rho!=0`.

### 1.2 The sign object is a pair of torsors

The exact q-free orientation identity

\[
\eta_A\eta_D=\eta_B\eta_C
\]

survives unchanged. The earlier global-cover consequence did not.

Let `eta_X^F` be the actual Frobenius orientation and write
`eta_X=sigma_X eta_X^F`. Put

\[
\kappa=\frac{\eta_A^F\eta_D^F}{\eta_B^F\eta_C^F}\in\{\pm1\}.
\]

Then the correct relative-sign equation is

\[
\sigma_A\sigma_D=\kappa\sigma_B\sigma_C.
\]

There are two disjoint eight-element torsors, indexed by `kappa`. The true
all-positive class exists only over `kappa=+1`. A globally regular degree-eight
cover cannot be asserted until `kappa`, etaleness and connectedness are
controlled component by component.

## 2. TFP3 literature transfer

### 2.1 What the large-finite-field literature supplies

Bary-Soroker's Hardy--Littlewood theorem over large finite fields supplies a
reusable architecture:

1. construct a finite etale cover encoding the arithmetic condition;
2. prove regularity and determine geometric monodromy;
3. use Lang--Weil/equidistribution to count the desired Frobenius class.

Bank--Bary-Soroker--Rosenzweig supply the correct exception discipline: thin
or low-dimensional families must have inseparability, discriminant,
derivative and monodromy exceptions audited explicitly rather than absorbed
under the word “generic.”

### 2.2 What remains custom and open

The next theorem is not Chebotarev itself. It is the input needed before
Chebotarev can be invoked:

- saturate the faithful trace-zero-plane model by all nonzero and
  cross-distinct open conditions;
- prove that every arithmetic component is a bounded-degree curve or
  exceptional point;
- normalize those curves;
- determine `kappa` on each component;
- build the relative-sign torsor over the `kappa=+1` locus;
- prove finite etaleness, fields of definition, geometric connectedness and
  monodromy.

Only after these steps may one expect a statement of the form

\[
N_q=\delta(q)q+O(\sqrt q),
\]

or a theorem confining the true class to a bounded exceptional locus.

### 2.3 Exact finite-panel geometry

At the audited true points, the 17-equation coefficient system has full
Jacobian rank `16`, hence tangent dimension one. In the first 152 audited
nonunit records, fixing `rho` retains rank `16` at 150 points and drops to
`15` at two `q=89` points, which are ramification candidates for the rho-map.
This is exact finite-panel evidence for a curve with generically finite rho
map. It is not a global dimension theorem.

## 3. Direct d=1 literature transfer

### 3.1 Authoritative direct target

The latest direct branch proves the exact Airy/complete-intersection object
and then evaluates the strongest Laurent-Airy Spin/Clausen/Hayes route. That
route is algebraically circular: after exact boundary cancellation it gives
`T_p^2=T_p^2`.

The remaining analytic theorem is

\[
|T_p|\le C p^{(p-1)/2}
\]

with absolute `C`, equivalently an absolute Frobenius correlation between
adjacent equal-weight invariant Airy moment motives.

Separately, an application theorem must transport the normalized Airy
constituent into the irreducibility hook/nearby-cycle ledger, including the
`q=2` and `q=infinity` cells, the arithmetic quadratic twist at infinity,
Tate and Artin--Schreier subtractions, and the punctual endpoint term.

### 3.2 Why the 2025 short-trace theorem does not close it

The short-sum theorem of Sawin--Shusterman assumes a fixed sufficiently large
base field, squarefree modulus, no finitely supported sections, no trivial or
Artin--Schreier factors, slopes at infinity at most one, and a controlled
rank/conductor penalty.

The direct d=1 problem does not currently meet this interface:

- `p` is the varying characteristic and also controls the growing degree;
- the pre-collapse hook parity sectors have rank at least `2^(p-2)` each;
- the exact total hook cohomology is exponential in `p`;
- even replacing it conjecturally by rank `O(p)` leaves the q-line complete
  sum at the critical `p^2` scale, so a strict crown constant or exact Tate
  subtraction is still required;
- the final survivor's conductor, slopes, trivial constituents and
  Artin--Schreier constituents have not been proved uniformly.

The theorem is therefore a hypothesis checklist and possible final tool after
collapse, not the collapse theorem itself.

### 3.3 Exact q-line falsification of a simple Tate formula

For the direct normal-form family, define

\[
E_1(q)=p(1-I_1(q)),
\]

where `I_1(q)` is the exact number of irreducible fibres over the generic
`t`-line. The tempting identity

\[
\sum_{q\ne0,2}E_1(q)=-p
\]

holds at `p=5,7,11` and fails at `p=13`.

The exact quotients `p^{-1} sum E_1` for

`p=5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67`

are

`-1,-1,-1,3,3,1,3,-7,-5,3,11,1,1,7,7,9,-7`.

Thus the q-line surface has a nontrivial algebraic/transcendental trace; it is
not governed by a universal one-line Tate identity. The correct remaining
object is the exact surface-cohomology decomposition and its constant, not
another pointwise Weil estimate.

## 4. Publication consequences for Papers V--VII

The seven-paper series remains useful, but the literature must be integrated
selectively:

- **Paper V:** position the sparse family against generic large-q prime-tuple
  and short-interval theorems, and state precisely why those theorems do not
  cover the endpoint family.
- **Paper VI:** formulate the remaining trace theorem using rank, conductor,
  slopes, geometric monodromy and Artin--Schreier exclusions; do not imply
  that a generic trace theorem supplies the missing collapse.
- **Paper VII:** retain the exact defect and quadratic results, but correct
  the sign-cover language to the two-torsor formulation above.

A Paper VIII is justified only after a theorem is obtained: either the
faithful cubic curve/Chebotarev theorem or a genuinely new Airy first-moment
or application-transport theorem.

## 5. Admissible next work

### TFP3 lane

1. Finish the saturated faithful curve theorem.
2. Compute `kappa` and normalize each component.
3. Prove the relative-sign torsor is finite etale and determine monodromy.
4. Apply effective finite-field Chebotarev.
5. Only then study the literal `Delta_PS` weight on those components.

### Direct d=1 lane

Only two outputs count as closure work:

1. a new theorem proving the Airy first-moment bound with an absolute
   constant; or
2. a different application-side certificate that avoids that absolute bound
   and closes the full irreducibility ledger.

Further raw prime sweeps, generic point-count theorems, relaxation geometry,
or another Hayes/Clausen repackaging do not count as progress.

## 6. Status ledger

### Proved exactly in this programme

- the `rho=1` verifier correction and two nonzero-defect q=97 certificates;
- the corrected two-torsor sign statement;
- the rank/conductor scale obstruction to direct short-trace import;
- the finite q-line sums listed above and falsification of the universal
  `-p` identity.

### Exact finite-panel evidence

- tangent dimension one at all audited true TFP3 points;
- generic rho transversality with two q=89 ramification candidates;
- curve-scale TFP3 count growth.

### Conditional on new custom geometry

- linear-density Chebotarev count for the true cubic class.

### Open and theorem-hard

- saturated faithful curve and monodromy;
- literal `Delta_PS` cancellation;
- direct Airy first-moment theorem;
- Airy-to-hook application transport;
- d=1 crown;
- every function-field-to-integer transfer and Fortune's conjecture.
