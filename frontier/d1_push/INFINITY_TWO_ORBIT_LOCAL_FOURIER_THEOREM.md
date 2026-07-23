# Infinity wild standard representation: two rank-one local Fourier orbits

**Date:** 2026-07-23  
**Status:** exact representation and Swan calculation for every prime `p>=5`; the rank-one local Fourier conclusion is the standard Laumon rank formula for slopes below one. This proves a genuine exponential-to-constant collapse for the wild standard term. However, that entire wild standard term lies in the explicit affine Artin–Schreier class already subtracted from `E_a^prim`. The theorem therefore checks the completeness of the Artin–Schreier removal but does not bound the primitive rank-four object.

## 1. Affine inertia irreducibles

Let

`I=C_p semidirect C_m`,  `m=(p-1)/2`,

where `C_m` acts on the nonzero characters of `C_p` by multiplication by squares.

The `p-1` nontrivial characters of `C_p` split into exactly two `C_m`-orbits:

- the square orbit;
- the nonsquare orbit.

Choose representatives `psi_+`, `psi_-` and put

`rho_+=Ind_(C_p)^I psi_+`,

`rho_-=Ind_(C_p)^I psi_-`.

Each is irreducible of dimension `m`.

## 2. Standard representation decomposition

The affine permutation representation on `F_p` restricts to `C_p` as its regular representation. Hence its standard quotient restricts as the sum of all nontrivial `C_p` characters.

Grouping those characters into the two square-class orbits gives

### Theorem ITOLF.1

`boxed(V|I=rho_+ direct_sum rho_-.)`

Therefore the infinity Adams class is

`W|I=-rho_+-rho_-+2Q`,

where `Q` is the tame quotient-regular representation.

## 3. Swan conductors

The lower ramification filtration has

`I_0=I`,

`I_i=C_p` for `1<=i<=m-1`,

and `I_i=1` afterward.

For either `rho=rho_+` or `rho_-`:

- `rank(rho)=m`;
- `rho^(C_p)=0`;
- `codim rho^(C_p)=m`.

Thus

`Swan(rho)`

`=sum_(i=1)^(m-1) (|C_p|/|I|) m`

`=(m-1)(1/m)m`

`=m-1.`

### Corollary ITOLF.2

Each wild orbit is isoclinic of slope

`boxed((m-1)/m=1-1/m<1.)`

The total standard Swan conductor is

`2(m-1)=p-3`,

agreeing with the independently proved wild-inertia theorem.

## 4. Local Fourier rank

Laumon's local Fourier transform from infinity to zero sends a representation all of whose slopes are below one to a local representation of rank

`rank-Swan`.

Therefore

`rank F^(infinity,0)(rho_+)`

`=rank F^(infinity,0)(rho_-)`

`=m-(m-1)`

`=1.`

### Theorem ITOLF.3 — two-orbit collapse

`boxed(F^(infinity,0)(V)`

`=one rank-one square-orbit term`

` direct_sum one rank-one nonsquare-orbit term)`

at the level of semisimple local representations, up to the standard Fourier shifts and epsilon-factor twists.

Thus the growing `(p-1)`-dimensional wild standard representation has local Fourier rank exactly `2`.

## 5. Relation to the Artin–Schreier subtraction

The exact infinity splitting is

`W|I=W_AS^aff+2(Q-m1)`,

where

`W_AS^aff=(p-1)1-V.`

Consequently both `rho_+` and `rho_-` occur wholly inside `W_AS^aff`. The explicit weighted Artin–Schreier boundary class removed in the definition of `E_a^prim` removes this complete wild standard term, including the two rank-one local Fourier transforms above.

The residual class

`2(Q-m1)`

is tame. Its weight-zero global boundary contribution collapses to the single quadratic Kummer character, which is also subtracted from `E_a^prim`.

## 6. What the theorem proves—and does not prove

The theorem proves:

- the wild standard term has only two local Fourier orbits;
- the explicit Artin–Schreier model accounts for the complete positive-ramification representation;
- no unidentified wild orbit survives the Artin–Schreier subtraction.

It does **not** prove:

- that `FT_c(E_a^prim)` has rank two or four;
- that the two rank-one orbits attach to the isolated `A_2` term;
- a bound for the primitive conductor defect.

Those statements concern the specialization cone of the residual tame augmentation at the weighted corner, after the Artin–Schreier and Kummer classes have been removed. They require the separate cyclic Thom–Sebastiani/corner comparison.

## 7. Epistemic classification

### Exact

- two character orbits;
- induced irreducible representations `rho_+`,`rho_-`;
- decomposition `V=rho_+ direct_sum rho_-`;
- ranks, Swan conductors and slopes;
- total standard Swan check;
- application of the standard local Fourier rank formula, yielding rank one per orbit;
- inclusion of both orbits in the already subtracted Artin–Schreier class.

### Open

- specialization of the residual tame augmentation at the weighted corner;
- effective rank of the primitive local Fourier transform;
- conductor-defect lemma and crown.
