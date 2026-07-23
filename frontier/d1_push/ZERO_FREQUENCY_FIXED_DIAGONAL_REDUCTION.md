# Zero-frequency cyclic fixed diagonal: exact geometric reduction

**Date:** 2026-07-23  
**Status:** exact fixed-locus and phase calculation for every prime `p>=5`. The open zero-frequency fixed locus is `A^1 x G_m`; its phase is identically zero. Its punctured nontransverse locus is the known `A1` quadratic/Kummer family, and the unique exceptional point is the cyclic cubic model of `CYCLIC_CUBIC_MILNOR_TRACE_THEOREM.md`. The remaining issue is a Frobenius-equivariant wild Lefschetz/specialization comparison, not an unidentified stratum.

## 1. Open Fourier kernel

On `lambda!=0`, write

`kappa=lambda*t`.

The rank-one full Fourier kernel is

`K_a(t,lambda)=L_psi(-lambda(t^p+a t^3)).`

The p-fold additive convolution at total dual coordinate `(K,L)` is carried by variables

`(t_i,lambda_i)`,  `i=0,...,p-1`,

subject to

`sum_i lambda_i=L`,

`sum_i lambda_i t_i=K`,

with phase

`Phi=-sum_i lambda_i(t_i^p+a t_i^3).`

The p-cycle rotates the indices.

## 2. Fixed locus at zero frequency

Set `(K,L)=(0,0)`. A cyclic fixed point has

`t_i=t`,  `lambda_i=lambda`

for every `i`. Since the ground field has characteristic `p`,

`sum_i lambda_i=p lambda=0`,

`sum_i lambda_i t_i=p lambda t=0`.

Thus every `(t,lambda)` with `lambda!=0` is fixed.

### Theorem ZFFD.1 — open fixed locus

`boxed(Fix(sigma) = A^1_t x G_m,lambda)`

inside the all-`lambda_i!=0` zero-frequency convolution fibre.

The phase restricts to

`Phi|Fix=-p lambda(t^p+a t^3)=0`.

Hence the coefficient sheaf on the fixed locus is geometrically constant. All complexity is in the wild excess normal term.

## 3. Tangent and excess directions

Write

`t_i=t+h_i`,  `lambda_i=lambda+mu_i`.

The linearized zero-sum constraints are

`sum_i mu_i=0`,

`lambda sum_i h_i+t sum_i mu_i=0`.

For `lambda!=0`, these reduce to

`sum_i mu_i=0`,  `sum_i h_i=0`.

Because `p=0`, the diagonal tangent vectors `(h_i=h)` and `(mu_i=mu)` themselves lie in these hyperplanes. This is the exact source of the wild nontransversality: the normal complex is an excess quotient rather than an ordinary transverse normal bundle.

## 4. Stratification along the fixed diagonal

The one-factor normal displacement calculated in `CYCLIC_DIAGONAL_SINGULARITY_THEOREM.md` is

`phi_(a,t)(h)=h^p+3a t h^2+a h^3`

on the nontransverse critical parabola.

- For `t!=0`, the quadratic coefficient is nonzero. The formal germ is `A1` with Milnor number one.
- At `t=0`, the germ is `h^p+a h^3`, formally `A2` in one factor.

The punctured map to the original coefficient line is

`t -> c=-3a t^2`.

Its pushforward is exactly

`Q_l direct_sum L_chi`,

the already isolated main/Tate plus quadratic Kummer class. Therefore no new primitive punctured fixed-diagonal family remains after the established subtraction.

## 5. The exceptional point t=0

For the p-fold cyclic Thom-Sebastiani normal function, impose the additive hyperplane

`sum_i h_i=0`.

In characteristic `p`,

`sum_i h_i^p=(sum_i h_i)^p=0`.

The surviving leading form is

`a sum_i h_i^3`

on the standard cyclic hyperplane. Its tame lift is exactly the isolated cubic singularity treated in `CYCLIC_CUBIC_MILNOR_TRACE_THEOREM.md`.

That theorem proves for every nonidentity cyclic element:

`Tr(sigma^k | Milnor)=1`,

although the ordinary Milnor dimension is `2^(p-1)`.

Thus the unique exceptional finite fixed-diagonal point has bounded cyclic **ordinary trace**. No further finite fixed-diagonal point exists.

## 6. Boundary of the fixed locus

Compactifying the `lambda` coordinate gives two boundary regimes:

- `lambda=0`: the all-origin convolution face, already identified with the main/Tate term; every proper mixed face is annihilated by `CYCLIC_COMPACTIFICATION_ORBIT_CANCELLATION_THEOREM.md`;
- `lambda=infinity`: the weighted Artin-Schreier endpoint, whose complete geometric critical support consists of the two escaping sections of `WEIGHTED_ENDPOINT_DECK_DESCENT_THEOREM.md`.

Therefore the zero-frequency inventory contains only:

1. the punctured `A1` main/Kummer locus;
2. the single `t=0` cyclic cubic excess;
3. the all-origin main/Tate face;
4. the two weighted-infinity escaping sections.

Every item is explicit and of fixed geometric support degree.

## 7. Precise remaining lemma

### Frobenius-equivariant wild diagonal localization lemma

Construct the localized Lefschetz-Verdier term of the p-cycle on the zero-frequency convolution fibre and prove that, after the established main/Kummer and Artin-Schreier/Tate subtractions:

1. the punctured `A1` fixed-diagonal term is zero in the primitive class;
2. the `t=0` local term is represented by an absolutely bounded effective Weil complex, not merely a virtual class of ordinary cyclic trace one;
3. the boundary local term is the Fourier-specialization defect on the two escaping sections, with bounded effective multiplicity;
4. no additional extension term is supported at the intersections of the `lambda=0` and weighted-infinity charts.

This lemma would bound the Fourier zero stalk and the invariant dimension. Combined with the nonzero-frequency rank bound, it gives the conductor-defect lemma.

The distinction in item 2 is essential: `Tr(sigma)=1` alone does not bound `Tr(sigma Frob)` unless the Frobenius-equivariant effective presentation is controlled.

## 8. Audit

`zero_frequency_fixed_diagonal_audit.py` checks exactly:

- the diagonal zero-sum constraints in characteristic `p`;
- vanishing of the restricted phase;
- the linearized constraint equations;
- p-power cancellation on the additive hyperplane;
- uniqueness of the exceptional parameter `t=0` in the `A1/A2` stratification;
- compatibility with the already audited cyclic cubic character identity.

## 9. Epistemic classification

### Exact

- open fixed locus `A^1 x G_m`;
- zero restricted phase;
- wild excess tangent structure;
- punctured `A1` and isolated cubic stratification;
- main/Kummer descent of the punctured locus;
- complete boundary-stratum inventory.

### Open

- Frobenius-twisted cyclic local term at the cubic point;
- effective multiplicity on the two escaping sections;
- absence of chart-intersection extensions;
- conductor-defect lemma and crown.
