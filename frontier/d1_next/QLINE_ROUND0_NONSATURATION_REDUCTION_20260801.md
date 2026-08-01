# Q-line Round 0 — exact simultaneous non-saturation reduction

**Date:** 1 August 2026  
**Primary gate:** `D1-QNS` / issue #44  
**Result:** **EXACT REDUCTION COMPLETE; MIDDLE-HOOK NON-SATURATION OPEN**

## 1. Why this is now the main track

Round 1 proved that raw integral Airy transport is obstructed and that a
Tate-normalized virtual transport, even if constructed, would not by itself
prove the crown. The direct crown ledger depends only on the literal q-line
counts. The shortest route is therefore to exclude simultaneous failure of
the two arithmetic classes, without demanding a stronger asymptotic theorem.

## 2. Exact failure point

For `A in {+1,-1}`, define

\[
C_A=p-2+B_A,
\qquad
N_A=C_A-\frac{S_0+A S_\chi}{2p}.
\]

Here `B_A` is the exact q=2 plus q=infinity boundary count. Crown failure in
the present sector forces

\[
N_+=N_-=0.
\]

Solving the two ledger identities gives the single trace point

\[
\boxed{
S_0=p(C_++C_-),
\qquad
S_\chi=p(C_+-C_-).
}
\]

Therefore it is enough to prove

\[
\boxed{
(S_0,S_\chi)
\ne
\bigl(p(C_++C_-),p(C_+-C_-)\bigr).
}
\]

When all four finite boundary readings vanish, as they do at the exact
out-of-sample primes `p=53,71`, the excluded point is simply

\[
\boxed{(S_0,S_\chi)=(2p(p-2),0).}
\]

This non-saturation statement is strictly weaker than
`N_A=p-2+B_A+o(p)` and is the primary theorem target.

## 3. Exact cohomological reduction

For fixed generic q, the hook object has already been reduced as follows.

### Weight zero

All weight-zero alternating hook cohomology cancels except one discriminant
Kummer line. This is proved for every odd prime `p>=5` and every generic q.

### Weight-one end pieces

The following are explicit:

- `V_1`: no weight-one part;
- `V_2`: the anti-invariant Prym of the ordered-pair curve, rank
  `2 floor((p-1)/4)`;
- `V_(p-2)`: the genus-`p-3` discriminant-twist curve, rank `2p-6`;
- `V_(p-1)`: no weight-one part.

These pieces have total effective rank `O(p)` and are not the remaining
uncertainty.

### Middle block

The only unresolved fixed-q weight-one virtual object is

\[
\boxed{
\mathcal M_q
=
\sum_{i=3}^{p-3}(-1)^i
H^1(\mathbf P^1,j_*\bigwedge^i\operatorname{Std}).
}
\]

It must be assembled in both the invariant and quadratic arithmetic q-line
projectors.

## 4. Exact closed routes

1. Boundary-only positivity is false: at `p=53,71` all q=2 and q=infinity
   counts vanish while generic q-line cells still prove the crown.
2. The canonical pre-pushforward deletion/Koszul complex is exact and has the
   wrong Euler class. This does not close post-parabolic or global q-line
   complexes.
3. Low-degree split q-line factors at `p=5,7` are exceptional and fail by
   `p=11`.
4. Split first-trace pattern fitting is not the arithmetic invariant/quadratic
   theorem required by the crown.
5. Termwise Weil bounds on the exponential-rank uncollapsed hook object do
   not give a strict non-saturation constant.

## 5. Live theorem routes

### Route QNS-A — post-parabolic parity reversal

Construct a differential or correspondence after parabolic pushforward, or in
an additive-wild quantum-bar filtration, that pairs the middle hooks and leaves
an effective object of rank/conductor `O(p)` with a strict enough trace bound
to avoid the saturation point.

The order-p quantum-bar resonance and the actual Pascal oscillator supply the
correct terminal two-line skeleton. What is missing is a geometric realization
on the q-line middle-hook complex.

### Route QNS-B — direct global projector trace

Bypass fixed-q effectivity and compute or constrain the assembled pair
`(S_0,S_chi)` directly. A determinant, congruence, one-sided or nonvanishing
theorem excluding the single saturation point is sufficient; a full
Hardy--Littlewood asymptotic is not required.

## 6. Status of Airy/ITD work

Divided-power Airy Rees transport and the integral Tate-diagonal lift remain
valid secondary research. They are no longer the primary crown gate because
neither supplies the q-line non-saturation theorem automatically.

## 7. Exact stopping point

The programme has exhausted the existing reductions. The next result must be
one genuinely new theorem:

\[
\boxed{
\text{middle-hook q-line parity/cancellation}
\quad\text{or}\quad
	ext{direct simultaneous non-saturation}.}
\]

No further unstructured prime census, boundary search or Airy scalar fitting
counts as progress.
