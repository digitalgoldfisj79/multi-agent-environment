# M3 continuation: local tangent action and boundary audit

Date: 28 July 2026

## 1. Setup

Let

`E = F_p^{F_p}`

with coordinates indexed by `i in F_p`. Put

`H = {x in E : sum_i x_i = 0}`

and let `D` be the diagonal line of constant vectors. Paper VI uses

`W = H/D`

and the smooth projective sparse surface

`Y_p = {s_2=...=s_{p-4}=0} subset P(W)`,

where `s_m(x)=sum_i x_i^m`. The unique nontrivial `C_p`-fixed point is represented by

`v=(i)_{i in F_p}`.

The root cycle acts by cyclic translation of the index.

## 2. Exact tangent-space theorem

### Theorem 1

For every prime `p>3`, the tangent representation of `C_p` on `T_[v]Y_p` is the unique nontrivial two-dimensional indecomposable representation over `F_p`. Equivalently, after a choice of basis, a generator acts by

`J_2 = [[1,3],[0,1]]`,

or by its inverse-convention form `[[1,-3],[0,1]]`.

In particular:

- the tangent fixed space is one-dimensional;
- `(sigma-1)^2=0` but `sigma-1 != 0`;
- the local action is wild and minimally unipotent at first order.

### Proof

A tangent vector before quotienting is a function `h:F_p->F_p`. Membership in `H` gives

`sum_i h_i=0`.

For `2<=m<=p-4`, differentiation at `v` gives

`d s_m(h)=m sum_i i^{m-1}h_i`.

Since `m` is a unit, the affine tangent equations are

`sum_i i^r h_i=0` for `0<=r<=p-5`.

The monomials `1,i,...,i^{p-5}` are linearly independent as functions on `F_p`, so their common annihilator has dimension four. The four functions

`1, i, i^2, i^3`

lie in that annihilator, because for `0<=a<=3` and `0<=r<=p-5` one has `a+r<=p-2` and

`sum_{i in F_p} i^{a+r}=0`.

Hence the affine tangent space is exactly

`span{1,i,i^2,i^3}`.

Passing from `H` to `W` quotients by the constant vector `1`; passing to the projective tangent at `[v]` further quotients by the line `i`. Thus

`T_[v]Y_p = span{i^2,i^3} mod span{1,i}`.

Under the convention `sigma(f)(i)=f(i+1)`,

`i^2 -> (i+1)^2 = i^2 + 2i + 1`,

`i^3 -> (i+1)^3 = i^3 + 3i^2 + 3i + 1`.

Modulo `span{1,i}`, this is

`i^2 -> i^2`,

`i^3 -> i^3+3i^2`.

Since `p>3`, the off-diagonal coefficient is nonzero, proving the claim. The opposite cycle convention replaces `3` by `-3` and gives the inverse representation.

## 3. Consequence for the quotient boundary

The wild quotient point is not first-order arbitrary: its tangent representation is always the same Jordan block `J_2`, independently of `p`.

This is useful for constructing an equivariant formal or log model around the deleted boundary point. In particular, any integral compact-support comparison for

`Y_p^o -> V_p`

must match a rank-two unipotent boundary action, rather than an uncontrolled `p`-dimensional local representation.

## 4. Tangent data is not a local quotient theorem

### Proposition 2

The tangent representation alone does not determine the completed local `C_p`-action, its invariant ring, or the integral boundary correction.

### Proof

Over a characteristic-`p` power-series ring, transformations of the form

`u -> u+v+f(v),  v -> v`,

with `f(v) in v^2 F_p[[v]]`, all have order `p` and the same linearisation

`u -> u+v,  v -> v`.

Their higher-order terms differ. Thus first-order Jordan data does not determine the nonlinear action. The isolated-fixed-point condition of the present surface imposes further restrictions, but those restrictions are not encoded by the tangent matrix alone.

Therefore Theorem 1 narrows the boundary model but does not supply the missing depth-two trace comparison.

## 5. Updated boundary task

The next local calculation is the completed action of `C_p` on the formal neighbourhood of `[v]` in `Y_p`, at least through the order needed modulo `p^2`. Concretely:

1. choose formal parameters whose linear action is `J_2`;
2. expand the equations `s_2=...=s_{p-4}=0` to determine the nonlinear cycle action;
3. identify the induced boundary term in the compact-support slope-`<2` derived-invariant complex.

The global crown target remains the smooth-open noncongruence

`#V_p(F_p) not congruent 0 mod p^2`.

The local calculation is auxiliary to constructing the integral comparison; it is not itself equivalent to positivity.
