# Papers V and VI: complete-rework review

**Date:** 2026-07-27  
**Branch:** `publication/fortune-papers-ii-vi-20260724`  
**Verdict:** **Both manuscripts require complete replacement, not revision.**

## 1. Series continuity

Papers III and IV establish a coherent integer-side progression:

1. Paper III proves pair-sum rigidity, exact harmonic-energy decompositions, strong Lebesgue tails, and a conditional block-averaged Hardy--Littlewood criterion. Its terminal obstruction is arithmetic transference/derandomisation.
2. Paper IV proves the reciprocal-frame target in the random-order primorial model. Its terminal obstruction is the passage from random order to the unique increasing primorial order.

The present Paper V does not begin from that endpoint. It opens as a separate function-field survey, introduces a broad Weil-RH window without supplying the promised proof ledger, and then compresses several generations of the `d=1` programme into a short catalogue. The present Paper VI is an Airy technical manuscript written against an obsolete frontier in which an absolute Airy correlation theorem and an Airy-to-Fortune transport theorem were described as the two terminal gaps.

A publication sequence labelled Papers I--VI should not make the reader infer the bridge. Paper V must explicitly explain why the function-field problem is the controlled laboratory suggested by the failure of derandomisation in Papers III--IV, what is analogous, and what is not. Paper VI must then continue the exact `d=1` geometry and terminate at the current one-sided Frobenius/nonvanishing wall.

## 2. Paper V: current manuscript assessment

### 2.1 What can be retained

The following material remains suitable in rewritten form:

- the polynomial primorial definition;
- the elementary degree barrier;
- the identification `P_1=T^p-T`;
- the affine normal-form philosophy;
- the exact quadratic and cubic square-class counts as the correct arithmetic coordinates;
- finite exact computation, provided it is demoted to a reproducibility section and updated to the latest certified range.

### 2.2 What must be removed or rebuilt

1. **The general Weil-RH window.** The current theorem is stated in two paragraphs, with the proof deferred to an unspecified supplement. It is the headline general-degree theorem but is not integrated with the later `d=1` programme. It should either receive a complete proof and precise hypotheses in a separate paper, or be removed from Paper V.

2. **The master incidence/Kloosterman narrative.** These sections reflect an early attack and do not lead to the present exact crown. They obscure the later normal-form and quotient geometry.

3. **The old cubic ledger.** The current sufficient inequality `(L)` is no longer the clean endpoint. The manuscript must use the exact crown reduction
   
   `W_p=N_2+(N_++N_-)/2>0`,
   
   with failure certificate `N_2=N_+=N_-=0`.

4. **The Airy half-sector as the closing section.** Later work proved that the advertised absolute Airy theorem is not the load-bearing final obstacle. The Airy contribution is a special trace component; the residual gate unwinds to the original q-line error-versus-main-term problem. Paper V must not end by directing the reader to an Airy companion as though it contains the final two missing steps.

5. **The status statement.** The current conclusion says the theorem is open for two independent Airy/application reasons. This is obsolete. The current exact wall is one-sided nonvanishing or nonsaturation on the cubic Kummer quotient/q-line invariant mode.

### 2.3 Replacement Paper V

**Proposed title**  
*Fortunate Polynomials over Finite Fields: Exact Normal Forms, Sparse Geometry, and the Function-Field `d=1` Crown*

**Purpose**  
This should be the bridge paper from the integer programme to the finite-field laboratory.

**Proposed structure**

1. **From Papers III--IV to the function-field laboratory**
   - integer-side deterministic transference wall;
   - random-order success and increasing-order failure;
   - why finite fields replace archimedean prime detection by exact irreducibility geometry;
   - explicit warning that the function-field theorem does not imply the integer conjecture.

2. **Polynomial primorials and the exact degree barrier**
   - definitions;
   - barrier `2d+2`;
   - scope of the paper restricted to `d=1` after a concise general discussion.

3. **The full `d=1` interval and affine normal forms**
   - `T^p-T+aT^3+bT^2+cT+d`;
   - translation and scaling orbits;
   - quadratic count `N_2` and cubic counts `N_+`, `N_-`.

4. **Exact crown theorem**
   - full interval count;
   - `W_p=N_2+(N_++N_-)/2`;
   - equivalence of the crown to `W_p>0`;
   - exact failure certificate.

5. **The sparse ordered-root surface**
   - equations `s_1=...=s_{p-4}=0`;
   - translation quotient and projective surface;
   - global smoothness;
   - complete-intersection geometry and Lefschetz concentration.

6. **Alternating hooks and the `p`-cycle projector**
   - exact hook character collapse;
   - fixed-point formula `#Fix(F sigma)=pI_4+p`;
   - theorem that the apparent trace inequality is exactly equivalent to the crown;
   - this is a structural theorem and a closed proof route.

7. **q-line and normal-form synthesis**
   - invariant and anti-invariant traces;
   - class-sum/class-difference formulas;
   - exact saturation identity;
   - statement of the one-sided nonsaturation wall.

8. **Exact computations and reproducibility**
   - clearly separated machine-certified results;
   - current range and scripts;
   - no heuristic data in theorem statements.

9. **Boundary for Paper VI**
   - ordinary semisimple/projector methods recover the unknown count;
   - the next paper studies integral first-order and quotient refinements.

## 3. Paper VI: current manuscript assessment

### 3.1 What remains mathematically valuable

The present Airy manuscript contains publishable technical material:

- cubic fibre collapse for `p=2 mod 3`;
- the Adams identity;
- local Swan-conductor cancellation;
- the modular symmetric-power exact sequence;
- full-rank defect and Hodge obstruction;
- exact low-rank spectra and independent trace reconstruction.

This material should not be discarded. It should become a separately titled technical companion or appendix package, after a fresh theorem audit against the later sign, normalisation, residual-gate, Pascal, quantum-bar, and p-adic-integrality work.

### 3.2 Why it cannot remain Paper VI

1. The abstract says the programme reduces to an absolute Airy correlation bound at the characteristic boundary. That is no longer the programme endpoint.
2. The final section names an analytic Airy theorem and an object-level application theorem as the two terminal gaps. Later work showed that the application residual gate is the original q-line count problem, while the Airy term lies below the load-bearing ledger scale.
3. It does not contain the strongest subsequent `d=1` theorems: the fixed Cartier moment, cyclotomic tangent, divided-hook nonexistence theorem, Hattori--Stallings secondary trace, explicit Artin--Schreier quotient, no-split theorem, Kummer correction, projective quotient count, and compactification obstruction.
4. It therefore neither continues Paper V nor closes the six-paper sequence.

### 3.3 Replacement Paper VI

**Proposed title**  
*Secondary Traces and Kummer Quotients for the Function-Field Fortune Crown*

**Purpose**  
This should continue directly from replacement Paper V and present the final exact frontier of the `d=1` programme.

**Proposed structure**

1. **Input from Paper V**
   - frozen definitions of `N_2,N_+,N_-`, `W_p`;
   - q-line saturation identity;
   - exact objective: exclude simultaneous zero.

2. **Fixed-class Cartier moments**
   - cofactor indicator;
   - first moment `M_a=sum c`;
   - translation projector;
   - reciprocal q-line formula;
   - three-mode dependence on the cubic coefficient;
   - exact computational evidence, explicitly non-theorem.

3. **Cyclotomic tangent and integral obstruction**
   - Fourier value `F_a`;
   - first tangent `(F_a-N_a)/pi=M_a mod pi`;
   - tangent Tate complex and Bockstein;
   - Frobenius scalar ambiguity;
   - precision order `pi^(p+1)` for the raw hook trace.

4. **No ordinary divided-hook complex**
   - character identity `Theta_p=p*1-Reg`;
   - proof that `Theta_p/p` is not a virtual characteristic-zero character;
   - precise consequence for integral perfect-complex strategies.

5. **Hattori--Stallings secondary trace**
   - coefficient extraction `Tr(Phi sigma^{-r})=p h_r`;
   - quotient-defect formula;
   - bi-equivariant coefficient derivative.

6. **Explicit Artin--Schreier quotient**
   - cyclic transfer and coordinate `y` with `sigma(y)=y+1`;
   - invariant `g=y^p-y`;
   - `g=r` as the Frobenius-shift level;
   - exact bijection between `g=1` points and irreducible fibres.

7. **No-split theorem**
   - logarithmic-derivative argument;
   - `X_a(F_p)=empty` for `p>5`;
   - `#Y_a(F_p)=(p-1)N_a`.

8. **Correct Kummer classification**
   - `mu_(p-3)` forms;
   - proof that sign is the nontrivial form only for `p=1 mod 4`;
   - rejection of the universal quadratic-twist picture;
   - common Kummer quotient and exact class-sum count.

9. **Projective quotient and compactification obstruction**
   - unique projective fixed point `[0,1,...,p-1]`;
   - isolated wild quotient point;
   - exact formula `#Q_p(F_p)=1+(p-1)W_p`;
   - boundary formula;
   - proof that a standard `1 mod p` congruence cannot distinguish failure from success;
   - careful non-assumption of `Q`-Gorenstein/Witt-rational properties at the wild point.

10. **Terminal theorem and closed routes**
    - one-sided compactly-supported Frobenius/nonsaturation theorem;
    - exact equivalence to `N_++N_->0` or `W_p>0` after the quadratic sector;
    - audited list of closed approaches;
    - no claim that the crown is proved.

## 4. Disposition of the current Airy manuscript

The current Paper VI should be renamed and removed from the numbered main sequence. Suggested disposition:

**Technical companion title**  
*Characteristic-Boundary Cubic Airy Moments: Adams Cancellation, Resonant Defects, and Exact Spectra*

Before circulation it must be updated to include:

- corrected sign conventions;
- the actual Pascal-graph oscillator;
- terminal quantum-bar theorem;
- divided-Adams Hasse coefficient and p-adic valuation ledger;
- the correction that an absolute Airy constant is not itself the Fortune crown;
- the residual-gate circularity theorem;
- explicit separation between standalone Airy results and Fortune implications.

This companion may be publishable independently, but it should not be advertised as the sixth and concluding Fortune paper.

## 5. Publication decision

- Freeze the existing Paper V and Paper VI manuscripts as **superseded working drafts**.
- Do not spend time line-editing or building new release artefacts from them.
- Rebuild Paper V from the exact normal-form/sparse-surface/p-cycle/q-line chain.
- Rebuild Paper VI from the Cartier-tangent/secondary-trace/Artin--Schreier/Kummer/compactification chain.
- Preserve the Airy manuscript as a separate technical companion after a new audit.
- Reopen source-fidelity, hostile-review, proof-verification and compiled-artifact gates for both replacement papers.

## 6. Final verdict

The user's suspicion is correct. Incremental repair would leave the series conceptually discontinuous and scientifically outdated. The correct action is a complete two-paper rewrite, with Paper V beginning explicitly at the derandomisation boundary of Papers III--IV and Paper VI continuing Paper V to the current exact `d=1` stopping point.