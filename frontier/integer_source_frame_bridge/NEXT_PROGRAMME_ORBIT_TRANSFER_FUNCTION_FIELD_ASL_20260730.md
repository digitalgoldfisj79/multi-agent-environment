# Next programme: orbit transfer, function-field laboratory and endpoint asymptotic large sieve

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

## Objective

Attack the theorem that now decides the first physical band:

\[
\sum_{j\in B}
\left|\sum_{p\in\mathcal P_R}w_pD_p(-P_j)\right|^2,
\qquad
D_p(a)=\psi(H;p,a)-\frac{\Psi_p(H)}{p-1}.
\]

The programme must distinguish:

- the all-residue scale gate `PBDH_P(X)`;
- diagonal sampling on the primorial orbit `PORS(X)`;
- cross-modulus cancellation on that orbit `PORC(X)`;
- signed recombination with the one-point higher conductors.

No step may replace the deterministic orbit by arbitrary residues after an absolute value has been taken.

## Gate O0 -- standing covariance verifier

Maintain the committed empirical falsification test over increasing `X`, multiple consecutive-centre blocks and random controls.

Failure criterion:

- `R_sample` grows polynomially or logarithmically away from one; or
- `R_coh` grows with the physical band cardinality.

Either would refute the intended transfer mechanism before theorem work is attempted.

Passage of finite panels is diagnostic only.

## Gate O1 -- exact orbit covariance kernel

Expand

\[
\sum_j\left|\sum_pw_pD_p(-P_j)\right|^2
=
\sum_{p,s}w_pw_s
\sum_jD_p(-P_j)\overline{D_s(-P_j)}.
\]

For `p != s`, rewrite the centre sum by the exact consecutive-primorial relation

\[
P_k=L_{jk}P_j,
\]

and the CRT residue pair

\[
(-P_j\bmod p,-P_j\bmod s).
\]

Deliverables:

1. an exact `p,s,j,k` kernel with all density and self terms present;
2. a proof of the maximum residue-pair multiplicity on blocks `K << log X`;
3. a decomposition into a complete-CRT model term and a deterministic sampling defect;
4. a finite exact verifier.

Stop criterion: if the defect contains a positive diagonal of Fortune size or larger, state the obstruction exactly.

## Gate O2 -- `PORS(X)`

Prove or reduce the diagonal sampling theorem

\[
\sum_{j,p}w_p^2|D_p(-P_j)|^2
\ll
\frac KX\sum_{p,a}w_p^2|D_p(a)|^2X^{o(1)}.
\]

Required route order:

1. exact residue-pair counting from primorial-prefix rigidity;
2. Fourier expansion in the centre index only after centring;
3. test whether the existing common-base hybrid Gram supplies the needed Bessel factor;
4. use `PBDH_P(X)` only as the final all-residue input.

Do not use Cauchy across `p` in this gate.

## Gate O3 -- `PORC(X)`

Prove or isolate the cross-modulus theorem

\[
\sum_j\left|\sum_pw_pD_p(-P_j)\right|^2
\ll X^{o(1)}\sum_{j,p}w_p^2|D_p(-P_j)|^2+E_{\rm self}.
\]

Highest-value attacks:

1. a two-modulus dispersion identity retaining the signed `-1/(p-1)` and `-1/(s-1)` terms;
2. a primorial-prefix Cotlar--Stein estimate for the operators `T_p:j mapsto D_p(-P_j)`;
3. a centred four-point kernel over `ps` before any source or modulus diagonalization;
4. a counterexample search using adversarial consecutive-centre blocks, not random residues.

A theorem with a fixed logarithmic saving over Cauchy is already valuable. Record the exact saving required after all frozen coefficients are restored.

## Gate FF -- function-field laboratory

### FF0: parameter dictionary

Write the integer/function-field dictionary for

- `H=eta X^2`;
- prime physical moduli `p asymp X`;
- all-residue variance;
- consecutive primorial centres;
- higher conductors whose product exceeds the source length.

### FF1: published all-residue theorem

Map Keating--Rudnick literally, including:

- squarefree modulus hypotheses;
- fixed degrees and large-base limit;
- the range corresponding to `1<beta<2`;
- normalization and diagonal terms.

Classify precisely which function-field version of `PBDH_P` follows.

### FF2: orbit sampling

Define polynomial primorial centres and formulate `PORS_FF` and `PORC_FF`.

Test whether the relevant Frobenius conjugacy classes vary in a family to which Katz equidistribution applies. If not, identify the missing monodromy/equidistribution theorem exactly.

### FF3: higher-conductor coupling

Reinsert polynomial conductors whose degree exceeds the source degree. Determine whether their one-point terms admit a signed trace interpretation coupled to the physical family.

Success criterion: an end-to-end function-field first-band theorem, not merely the all-residue variance.

## Gate ASL -- endpoint prime-conductor audit

### ASL0: literal theorem map

For each Conrey--Iwaniec--Soundararajan theorem, record:

- modulus support;
- primitive/imprimitive character convention;
- coefficient length;
- smoothness and Mellin-transform requirements;
- permitted coefficient Euler products;
- main and off-diagonal terms;
- uniformity as `N/Q^2` approaches a positive constant.

### ASL1: prime-band extraction

Determine whether restricting `q` to primes can be achieved by an admissible coefficient or a Vaughan/Heath--Brown decomposition without losing the required logarithm or destroying the asymptotic off-diagonal.

### ASL2: endpoint obstruction

The published long-polynomial range `N <= Q^{2-epsilon}` leaves a power gap from `N=eta Q^2`. Prove one of:

1. the argument is uniform to `N=eta Q^2` for fixed `eta<1` and the required coefficient family;
2. a specific step fails at the endpoint and yields the minimal new endpoint ASL theorem;
3. the prime-band restriction creates an additional independent obstruction.

### ASL3: orbit insertion

Even an endpoint all-character theorem does not automatically imply `PORS` or `PORC`. Identify whether the primorial residues can be incorporated as a trace weight or whether a second deterministic sampling theorem remains.

## Gate H -- signed higher-conductor contraction

After the physical orbit theorem is available, return to

\[
\mathcal F_{j,R}=\mathcal F^{(1)}_{j,R}+\mathcal F^{(\ge2)}_{j,R}.
\]

Preserve the cross term. Use the exact one-point candidate formula for conductors `Q>H` and seek a common trace/kernel representation with the physical orbit. Positive separation remains prohibited.

## Execution boundary

### Existing input

- exact full-source completion;
- centred physical determinant identity;
- common-base and primorial-prefix frames;
- exact all-order survivor inclusion--exclusion;
- empirical standing covariance verifier.

### First genuinely new theorem

Either `PORS(X)` or a nontrivial logarithmic-saving form of `PORC(X)` for the actual primorial block.

### Final dependency chain

\[
\mathrm{PBDH}_{\mathbb P}
+\mathrm{PORS}
+\mathrm{PORC}
+\text{signed higher-conductor contraction}
\Longrightarrow
\text{first physical-band theorem}
\Longrightarrow
\mathrm{NSMT}(X).
\]

This programme does not claim that the function-field or asymptotic-large-sieve routes already close the integer problem. They are now the two highest-value laboratories for the orbit-transfer theorem.
