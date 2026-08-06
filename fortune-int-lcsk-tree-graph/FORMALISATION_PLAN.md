# Formalisation plan

## Kernel-checked claims

The new module `FortuneFormal.Integer.LocalConnectedTreeObstruction` proves only exact real-algebra statements:

1. the normalized equal-residue pair coefficient is `1/(p-1)`;
2. the normalized equal-residue triple cumulant is `-(p-2)/(p-1)^2`;
3. for every fixed edge constant `C`, the triple coefficient exceeds the three-tree budget whenever `p-2>3C^2`;
4. the absolute hyperedge log exponent `r` is smaller than the required exponent `(1+delta)(r-1)` whenever `delta(r-1)>1`.

## Explicit boundary

Lean does not assert:

- the prime number theorem;
- Brun--Titchmarsh;
- existence of candidate triples for all `X`;
- an asymptotic local-factor expansion;
- `INT-LCSK` or its negation;
- `INT-SOCG`, `INT-AOD` or Fortune.

The finite candidate witness and exact residue-pattern enumeration are checked by Python.

## Trust requirements

- Lean 4.32.0;
- targeted module build;
- package-root import;
- full package build;
- no placeholder proof, new trust declaration or unsafe declaration in the new module.
