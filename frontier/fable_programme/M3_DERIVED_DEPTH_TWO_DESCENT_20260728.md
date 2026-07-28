# M3 continuation: derived depth-two descent on the smooth quotient open

Date: 28 July 2026

## Status labels

- **Exact theorem from Papers V--VI:** the compactified quotient count and unique fixed point.
- **Exact deduction here:** removal of the wild point, the smooth-open depth-two criterion, and the derived-invariant algebraic target.
- **Published input:** finite-length Witt trace formulas and Witt/rigid slope comparison.
- **Open theorem:** construction and nonvanishing of the required integral slope-`<2` derived descent trace.

## 1. Remove the wild point before doing p-adic cohomology

Let `Y_p` be Paper V's smooth projective ordered-root surface and let `C_p` act by cyclic permutation. Paper VI proves that every nonidentity element has the same unique fixed point `y_*`, and that the quotient

`Q_p=Y_p/C_p`

has one isolated wild quotient point `x_*`, the image of `y_*`.

Put

`Y_p^o=Y_p\{y_*}` and `V_p=Q_p\{x_*}`.

### Theorem 1: smooth free quotient

The action of `C_p` on `Y_p^o` is free. The quotient map

`Y_p^o -> V_p`

is a finite etale `C_p`-torsor, and `V_p` is a smooth separated surface over `F_p`.

### Proof

The group has prime order. A point with nontrivial stabiliser is fixed by a nonidentity element and hence, by Paper VI's fixed-point theorem, equals `y_*`. Therefore the action on the complement is free. The constant group scheme `C_p` over `F_p` is finite etale. A free action has finite etale quotient map, and smoothness descends etale-locally from the smooth scheme `Y_p^o`.

This removes the local singularity from the principal cohomological target. The isolated wild point contributes a known count of one, not an unknown correction term.

## 2. Exact depth-two criterion on the smooth open

Paper VI and the preceding M3 note give

`#Q_p(F_p)=1+(p-1)W_p`,

with `0<=W_p<=p^2-1`. Since `x_*` is rational,

`#V_p(F_p)=(p-1)W_p`.

### Theorem 2: smooth-open depth-two crown

For every admitted prime,

`W_p=0  <=>  #V_p(F_p) congruent 0 mod p^2`.

Equivalently, the function-field crown is

`#V_p(F_p) not congruent 0 mod p^2`.

### Proof

Multiplication by `p-1` is invertible modulo `p^2`; hence `p^2` divides `#V_p(F_p)` if and only if `p^2` divides `W_p`. The range `0<=W_p<p^2` then forces `W_p=0`.

## 3. Correction: finite-length W_2 O does not itself reach mod p^2 over F_p

Chatzistamatiou, *On the Frobenius stable part of Witt vector cohomology* (arXiv:1007.5000, Theorem 1 / Corollary 3.7.2), proves under the stated freeness hypothesis that for a proper scheme over `F_{p^a}` the finite-length `W_n O` trace computes the rational-point count modulo

`p^{min(a,n)}`.

At the actual base field `F_p`, one has `a=1`. Therefore even `W_2 O` supplies only a congruence modulo `p`, not modulo `p^2`.

Passing to `F_{p^2}` does not repair this. It gives information about `Frob^2` and `#V_p(F_{p^2})`, whereas the crown needs the trace of `Frob` on `F_p`-points. The two are not recoverable from one another in general: the matrices

`diag(1,1)` and `diag(1,-1)`

have identical trace of the square but different trace of the operator.

### No-go 3

Neither finite-length structure-sheaf Witt cohomology over `F_p` nor extension-field point counts by themselves determine the required mod-`p^2` crown coefficient.

## 4. The correct p-adic object is the full slope-<2 trace

The rigid Lefschetz trace formula gives

`#V_p(F_p)=sum_i (-1)^i Tr(Frob | H^i_rig,c(V_p/K))`.

The contribution of every Frobenius eigenvalue of p-adic slope at least two is divisible by `p^2`. Therefore the crown is controlled by the alternating Frobenius trace on the full slope-`<2` compactly supported rigid cohomology.

Berthelot--Bloch--Esnault identify Witt-vector structure-sheaf cohomology, after inverting `p`, with the slope-`<1` part of rigid cohomology. That is only the first half of the required interval. For a smooth proper variety, the de Rham--Witt slope spectral sequence places the additional interval `[1,2)` in the degree-one de Rham--Witt terms. For the smooth nonproper surface `V_p`, the analogous implementation must use compactly supported rigid cohomology or an overconvergent de Rham--Witt realisation.

### Corrected target DT2

Construct an integral Frobenius-stable compact-support complex `C_<2(V_p)` whose rationalisation is the slope-`<2` part of `RΓ_rig,c(V_p/K)` and prove

`Tr(Frob | C_<2(V_p)) not congruent 0 mod p^2`.

This statement implies the crown by Theorem 2.

Generic ordinarity, a nonzero unit-root rank, or a Newton polygon alone remains insufficient: these data do not determine the trace inside a fixed slope interval.

## 5. Derived C_p descent is the load-bearing algebra

Because `Y_p^o -> V_p` is a finite etale `C_p`-torsor, the relevant cohomology satisfies Cartan--Leray descent. Rationally, division by `p` makes invariants exact. Integrally modulo `p^2`, invariants are not exact, and the higher group-cohomology columns are precisely the information lost by semisimplification.

Let `C_<2(Y_p^o)` denote the corresponding integral slope-`<2` compact-support complex, once constructed. The expected descent object is

`RΓ(C_p, C_<2(Y_p^o))`.

For a `W_2(F_p)[C_p]`-module, derived invariants are represented by the periodic resolution with alternating maps

`σ-1` and `N=1+σ+...+σ^{p-1}`.

Thus the depth-two quotient problem has an explicit integral carrier: the total complex formed from `C_<2(Y_p^o)` and the two operators `σ-1` and `N`.

### Target DDT2: derived depth-two descent theorem

Prove a Frobenius-compatible comparison

`C_<2(V_p) ≃ RΓ(C_p, C_<2(Y_p^o))`

at the level required for traces modulo `p^2`, and then prove

`Tr(Frob | RΓ(C_p,C_<2(Y_p^o))) not congruent 0 mod p^2`.

This is stronger and more precise than asking for a generic Newton polygon. It also explains why Paper VI's ordinary invariant and tangent constructions were blind: the decisive coefficient lives in the integral derived-invariant complex.

## 6. What has and has not been achieved

### Achieved

1. The isolated wild point is removed from the unknown part of the problem.
2. The crown is an exact mod-`p^2` noncongruence on a smooth quasi-projective surface.
3. Standard `W_2 O` trace formulas are proved insufficient at the base field.
4. The required slope range is exactly `<2`, not merely `<1`.
5. The integral descent obstruction is localised to the periodic `C_p` derived-invariant complex.

### Still open

1. Constructing a usable integral slope-`<2` compact-support lattice for this family.
2. Proving Frobenius-compatible derived descent modulo `p^2` in a form that permits trace extraction.
3. Computing or proving nonvanishing of the resulting periodic-complex trace.

The next computational task is to build the finite linear-algebra shadow of the `σ-1,N` complex from the existing root-cycle and Cartier data for small primes. The next theorem task is the integral comparison DDT2.

## Primary references

- A. Chatzistamatiou, *On the Frobenius stable part of Witt vector cohomology*, arXiv:1007.5000.
- P. Berthelot, S. Bloch, H. Esnault, *On Witt vector cohomology for singular varieties*, arXiv:math/0510349.
- C. Davis, A. Langer, T. Zink, *Overconvergent Witt Vectors*, arXiv:1008.0305, and subsequent overconvergent de Rham--Witt/rigid comparison work.
