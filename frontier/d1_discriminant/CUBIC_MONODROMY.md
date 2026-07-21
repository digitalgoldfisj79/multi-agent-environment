# Generic monodromy of the cubic orientation eliminant

**Date:** 2026-07-21  
**Status:** generic arithmetic and geometric Galois groups proved to be `S_8`.

## 1. The degree-eight eliminant

Let `E_(c,d)(V)` be the monic degree-eight orientation eliminant of `CUBIC_FIBRE_DEGREE.md`. It is obtained by eliminating the depressed-cubic coefficient u from the exact compatibility equations for

`X^p + X^3 + cX + d`.

Over the generic coefficient field `Q(c,d)`, let G be the Galois group of E acting on its eight roots.

## 2. A misleading special fibre

At `(c,d)=(2,3)`, the specialized polynomial is

`V^8 + 261V^6 - 567V^5 - 1890V^4 - 1863V^3`
`    + 54135V^2 - 141588V + 114723`.

Sage computes its Galois group as transitive group `8T47`, of order 1152 and structure

`(S_4 x S_4) : C_2`.

It has a block system of two blocks of size four. This is a special degeneration and not the generic group.

## 3. An S8 specialization

At `(c,d)=(-2,-2)`, the eliminant is

`f(V) = V^8 - 10V^6 - 270V^5 + 4857V^4 - 25974V^3`
`       + 50684V^2 - 40986V + 11779`.

Its discriminant is nonzero modulo each of 5, 13, and 293. The exact squarefree modular factorizations are:

### Modulo 5

`f = V^8 + 2V^4 + V^3 - V^2 - V - 1`.

This polynomial is irreducible, so the Galois group of f is transitive and contains an 8-cycle.

### Modulo 13

`f = (V+3)`
`    (V^7 - 3V^6 - V^5 + 6V^4 + 3V^3 + 4V^2 - 2V - 4)`.

Thus the group contains a 7-cycle.

### Modulo 293

`f = (V+52)(V+93)(V+145)(V-111)(V-110)(V-86)`
`    (V^2 + 17V + 2)`.

Thus the group contains a transposition.

By Dedekind's theorem, these factorisation types occur as cycle types in the Galois group.

### Lemma CM.1

A transitive subgroup of `S_8` containing a 7-cycle is primitive.

### Proof

A nontrivial block system in degree eight has blocks of size two or four. A 7-cycle induces a permutation of the set of blocks. The number of blocks is respectively four or two, so this induced permutation must be trivial. The 7-cycle would then preserve each block setwise, impossible because neither `S_2` nor `S_4` contains an element of order seven. QED.

### Lemma CM.2

A primitive subgroup of `S_n` containing a transposition is `S_n`.

### Proof

Take the graph whose edges are the conjugates of the transposition under the group. Its connected components form a block system. Primitivity and the presence of an edge force the graph to be connected. Transpositions along the edges of a connected graph generate `S_n`. QED.

### Theorem CM.3

The Galois group of the specialization `f` is `S_8`.

## 4. Generic arithmetic monodromy

For a good specialization, the specialized Galois group embeds into the generic arithmetic Galois group. Since the specialization above has group `S_8` and the generic group is a subgroup of `S_8`, the generic arithmetic group is exactly

`G_arith = S_8`.

In particular, E is irreducible over `Q(c,d)` and the compatible orientation map has generic degree eight.

## 5. Generic geometric monodromy

The geometric group over `Qbar(c,d)` is a normal subgroup of the arithmetic `S_8`.

To determine its sign, specialize the generic discriminant at `d=0`. Exact factorization gives

`Disc_V(E_(c,0)) = constant`
`  * (c-3)^4 c^8 (c^2-c+1)`
`  * (4c^2+14c+13)^2`
`  * (3c^2-4c+3)^4`
`  * (70c^3+57c^2-72c+53)^4`
`  * (4c^8-16c^7-35c^6+206c^5-113c^4`
`     -376c^3+715c^2-1690c+2197)^2`.

The factor `c^2-c+1` occurs to odd multiplicity. Hence the discriminant is not a square in `Qbar(c,d)`. The geometric group therefore contains an odd permutation and is not contained in `A_8`.

The only normal subgroups of `S_8` are `1`, `A_8`, and `S_8`. The geometric group is nontrivial and is not contained in `A_8`; consequently:

### Theorem CM.4

`G_geom = S_8`.

Thus the degree-eight orientation cover has full symmetric geometric monodromy.

## 6. Consequences for cubic factorial moments

For every `1 <= j <= 8`, the ordered distinct j-fold fibre power of the generic orientation cover is geometrically irreducible, because `S_8` is j-transitive on ordered distinct j-tuples.

The coefficient locus where the compatible map has more than eight algebraic points is contained in the fixed discriminant and subresultant divisor. It has only `O(p)` rational points. Therefore factorial moments of order greater than eight contribute only lower-dimensional errors, despite the uniform exceptional bound `nu_3 <= 24`.

This converts complete cubic deletion into a finite fixed-geometry programme:

1. orders `j=1,...,8` have one generic top-dimensional component each;
2. orders `j=9,...,24` are supported on the exceptional divisor;
3. cubic irreducibility, local admissibility, degree-p discriminant parity, and the quadratic-deletion weight are imposed by fixed finite root-incidence and Kummer covers on these fibre powers.

The remaining difficulty is no longer uncontrolled multiplicity or unknown monodromy. It is the finite audit of those arithmetic twists and mixed covers.

## 7. Verification

The companion script `cubic_monodromy_audit.py` verifies the three modular factorizations, the nonzero discriminant residues, and the odd discriminant factor at `d=0`.

Independent Sage computation for the special fibre `(2,3)` was run as Hugging Face job `6a5f9748d09dc1f57c6bf956`; it returned group order 1152 and transitive group `8T47`, confirming that this fibre is exceptional rather than generic.