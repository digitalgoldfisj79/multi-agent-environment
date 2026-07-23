# Infinity wild standard representation: two rank-one local Fourier orbits

**Date:** 2026-07-23  
**Status:** exact representation and Swan calculation for every prime `p>=5`; the rank-one local Fourier conclusion is the standard Laumon rank formula for slopes below one. This proves a genuine exponential-to-constant local collapse for the wild standard term. Relating these two rank-one pieces to the complete c-pencil primitive transform still requires the corner specialization diagram.

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

## 5. Tame quotient term

The term

`2Q`

is entirely tame. It is responsible for the puncture/cyclotomic boundary complex. The exact general-p Weight-Zero Collapse Theorem proves that, after the global invariant line is removed, this tame list collapses to the single quadratic Kummer character.

After subtraction of that Kummer line, no growing weight-zero local Fourier term remains.

## 6. Relation to the rank-four target

The two rank-one wild Fourier pieces are arithmetic square-class readings. The isolated A2 Adams difference has an effective presentation containing the original and p-th Adams transforms of a two-dimensional local object, hence effective dimension at most four.

The current representation calculation proves the underlying constant-rank mechanism:

- two wild square-class orbits, each Fourier rank one;
- one exact Kummer line from the tame quotient;
- no finite-inertia contribution.

The remaining corner diagram must identify how the two rank-one local transforms and their Adams readings assemble into `FT_c(E_a^prim)`. The expected effective generic rank is four.

## 7. Epistemic classification

### Exact

- two character orbits;
- induced irreducible representations `rho_+`,`rho_-`;
- decomposition `V=rho_+ direct_sum rho_-`;
- ranks, Swan conductors and slopes;
- total standard Swan check;
- application of the standard local Fourier rank formula, yielding rank one per orbit.

### Open

- arithmetic epsilon/twist identification of the two rank-one transforms;
- their exact attachment to the c-pencil A2 specialization;
- rank-four global local-Fourier theorem and crown.
