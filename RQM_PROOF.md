# Theorem RQM — adjudicated complete proof

**Adjudication note (2026-07-21).** Two agents wrote this assembly
independently; a closure judge then brute-force enumerated all ordered
pair configurations at N = 3..8 and N = 16, verified that both case
taxonomies cover all M(M-1) pairs with zero holes and are in exact
bijection class-by-class, confirmed the direct bias is exactly constant
within each configuration class (so the classification captures the bias
completely), independently recomputed the binding case and all constants,
and ruled CLOSES: YES — either assembly alone constitutes the proof. This
document is Assembly A, designated the primary text. Judge's merge
rulings incorporated by reference: (i) state the frame hypothesis in
Assembly B's weaker form (nondegeneracy: rho not identically zero on the
sampled ratio set, ensuring D_X > 0), of which the (N1) form below is a
sufficient special case; (ii) the Lambda = 28 (here) vs 27 (Assembly B)
difference is definitional, not a discrepancy; (iii) inline the two
standard Gauss-sum facts rather than citing an unretrievable reference.
Epistemic status: PROVED under the stated hypotheses (upgraded from
provable-sketch by the adjudication). The independent Assembly B, the
closure ruling, the Monte Carlo diagnostic, and all verification scripts
are preserved in frontier/rqm_workbench/ and frontier/rqm_mc/. Scope
reminder: this is a model theorem about random orderings of the block
primes; it says nothing about the increasing (primorial) order or
Fortune's conjecture itself.

---

# Theorem RQM: complete assembly of the random-order model theorem

**Status header.** This document is the G1 write-up: the full continuous proof of the RQM statement, assembling the component lemmas adjudicated in `frontier/workbench/v1.final.json`. Component lemmas are restated with condensed complete proofs; the assembly (configuration enumeration, coordinates, matching lemma, ledger, constants) is written in full. Every claim is labelled. Numerical verifications run for this document: `assembly_checks.py` and `e2e_bias_check.py` in the session scratchpad (`/tmp/claude-0/-home-user-multi-agent-environment/53da20a7-5af0-58c9-b6a4-3bdefd3e2c90/scratchpad/`); summaries in Section 9.

---

## 0. Statement and standing conventions

Fix `0 < eta < 1` and a nonnegative even Schwartz function `rho`. Let `X` be large, `L = {ell_1 < ... < ell_K}` the primes of `[X, 2X)`, `A_X = prod_{p < X} p`. For a permutation `sigma` of `{1,...,K}` define the **sigma-path**

    Q_0^s = 1,  Q_j^s = prod_{i <= j} ell_{sigma(i)},  P_j^s = A_X Q_j^s   (0 <= j <= K),

with `N = K + 1` centres. Index pairs are multisets `u = {j,k}`, `0 <= j <= k <= K`; `M = N(N+1)/2`; `S_u^s = P_j^s + P_k^s`. Let `H = eta X^2`, `Q_X` = primes of `[H, 2H)`, and, exactly as Paper II (3.3)/(3.7):

    w_{q,a} = rho(Ha/q),  D_X = sum_{q in Q_X} sum_{a != 0} w_{q,a},  p_{q,a} = w_{q,a}/D_X,
    Psi_a(L) = sum_q p_{q,a} e(aL/q),  m_a = sum_q p_{q,a},
    E_a^s = sum_{u != v} |Psi_a(S_u^s - S_v^s)|^2,

`R_a^s` the distinct-modulus part (Paper II (3.13)) and `F_X^s` the Frobenius energy (3.5), all along the sigma-path.

**Standing normalizations.**

- **(N1) Frame admissibility** *(hypothesis-level; flagged).* We assume `rho >= delta_rho > 0` on `[1/2, 1]`. Since `Ha/q in (a/2, a]` for `q in [H, 2H)`, the harmonic `a = 1` then populates every row: `D_X >= delta_rho #Q_X`. Some such condition is genuinely **necessary** for the Paper II frame to be nonempty: if `rho` were supported in, say, `[0.3, 0.32]`, then `Ha/q` would miss the support for every integer `a >= 1` and every shell `q`, giving `D_X = 0` and an undefined frame. Paper II presupposes `D_X > 0` implicitly; (N1) is the natural explicit form (any positivity interval meeting the attained set `{Ha/q}` works, with adjusted constants). Used **only** in the diagonal and aggregate weight bounds (Sections 7-8), never in the bias machinery.
- **(N2) Block size** *(standard, effective).* By the prime number theorem there is an absolute `X_0` with `X/(2 log X) <= K <= 3X/(log X)` for `X >= X_0`. Hence `X^2/(8 log^2 X) <= M <= 16 X^2/log^2 X`.
- All largeness conditions on `X` (listed in Section 8) are absolute or depend only on `eta, rho`.

**Theorem RQM (unconditional; effective).** Under (N1)-(N2), for all sufficiently large `X` (threshold depending only on `eta, rho`), with `sigma` uniform on `S_K`:

**(i)** uniformly for every integer `1 <= |a| < H`,

    E_sigma[E_a^s] <= C(eta, rho) * M * (log X)^9;

**(ii)** `E_sigma[ sum_{a >= 1} R_a^s / m_a ] <= C M (log X)^9` and `E_sigma[F_X^s] <= C M (log X)^9`.

All constants are effective; the exponent `C_0 = 9` is absolute. By Markov and `E_a >= 0`, for any `omega(X) -> infty` all but an `omega^{-1}` fraction of the `K!` orderings satisfy the sigma-path aggregate target with loss `(log X)^9 omega`.

**Reduction to the key proposition.** Expanding (Paper II Prop. 3.2, valid verbatim on every sigma-path):

    E_a^s = M(M-1) kappa_{2,a} + sum_{q != r} p_{q,a} p_{r,a} sum_{u != v} e_{qr}(b (S_u^s - S_v^s)),
    b = a(r - q),   e_{qr}(x) := e(x/qr),

since `a/q - a/r = a(r-q)/(qr)`. The diagonal `q = r` is deterministic; taking `E_sigma` and `sum_{q != r} p_{q,a} p_{r,a} <= m_a^2 <= 1`, Theorem RQM(i) follows (Section 7) from:

**Proposition A (per-modulus-pair bias sum).** For all `q != r` in `Q_X` and all integers `1 <= |a| < H`, with `b = a(r-q)`:

    sum_{ordered pairs u != v} | E_sigma[ e_{qr}( b (S_u^s - S_v^s) ) ] |  <=  C(eta) * M * (log X)^9.

Sections 1-6 prove Proposition A. Throughout, `q != r` are fixed shell primes, `qr in [H^2, 4H^2] = [eta^2 X^4, 4 eta^2 X^4]`, `phi(qr) = (q-1)(r-1) >= qr/2`.

---

## 1. Arithmetic preliminaries (proved)

**Lemma 1.1 (path rigidity; Addendum A.1, pathwise).** Every sigma-path satisfies `P_{j+1}^s >= X P_j^s`. Hence if `c_0..c_K` are integers, `|c_t| <= B`, `X > B + 1`, and `sum c_t P_t^s = 0`, then all `c_t = 0`. *Proof:* as in the Addendum: the top nonzero coefficient dominates the geometric tail `sum_{i<t} P_i <= P_t/(X-1)`. QED. Consequently `u != v  =>  D_uv := S_u^s - S_v^s != 0` for every `sigma` (coefficients bounded by 2). **Dependency audit:** rigidity is load-bearing only for this nonvanishing (frame semantics) and for the distinctness bookkeeping of the sliding family; **no bias estimate below uses it**.

**Lemma 1.2 (gcd nonvanishing).** For `q != r` in `Q_X`, `1 <= |a| < H`, `b = a(r-q)`: `b != 0`, `0 < |b| < H^2 <= qr`, and `gcd(b c A_X, qr) = 1` for every integer `0 < |c| <= 2`. *Proof:* `q >= H > |a|` so `q` does not divide `a`; `0 < |r - q| < H <= q` so `q` does not divide `r - q`; every prime factor of `A_X` is `< X < H <= q`; `|c| <= 2 < q`. Symmetrically for `r`. Also every block prime `ell < 2X < H <= q` is a unit mod `qr`, hence so is any product of block primes. QED.

---

## 2. Configuration enumeration (new; complete)

Fix an ordered pair `(u, v)`, `u = {i, j}`, `v = {k, l}`, `u != v` as multisets. For each index `t` let `c(t)` = (multiplicity of `t` in `u`) - (multiplicity in `v`), so `c(t) in {-2,...,2}` and `sum_t c(t) = 2 - 2 = 0`. Let `t_1 < ... < t_m` be the indices with `c(t) != 0` and `c_s := c(t_s)`. Since `u != v`, `m >= 1`; since the coefficients sum to `0`, `m >= 2`. Since `|u| + |v| = 4`, `sum_s |c_s| <= 4`, so `m <= 4`. Then

    D_uv = sum_s c_s P_{t_s}^s = A_X * (prod W_0) * ( c_1 + c_2 R_1 + c_3 R_1 R_2 + ... + c_m R_1...R_{m-1} ),

where (cells) `W_0` = primes at sigma-positions `1..t_1` (empty iff `t_1 = 0`), `W_s` = positions `(t_s, t_{s+1}]` for `1 <= s <= m-1` (nonempty: `n_s = t_{s+1} - t_s >= 1`), `W_m` = positions `(t_m, K]` (the **tail cell**, empty iff `t_m = K`), and `R_s = prod(W_s)`. Cell sizes `n = (n_0, ..., n_m)`, `n_0 = t_1`, `n_m = K - t_m`, `sum n_s = K`, are deterministic functions of `(u,v)`; the cell **contents** are random.

**Lemma 2.1 (complete pattern list).** The possible coefficient vectors `(c_1,...,c_m)` are exactly:

- `m = 2`: `(1,-1), (-1,1)` [type S] and `(2,-2), (-2,2)` [type D];
- `m = 3`: the six vectors `±(1,1,-2), ±(1,-2,1), ±(-2,1,1)`;
- `m = 4`: the six vectors with two entries `+1` and two entries `-1`.

*Proof.* Entries are nonzero, in `[-2,2]`, sum to 0, with `sum |c_s| <= 4`. For `m = 4` this forces all `|c_s| = 1`, two of each sign: `C(4,2) = 6` vectors. For `m = 3`: `sum|c_s| in {4}` (parity: an odd count of odd entries cannot sum to zero with `sum|c| <= 4` unless one entry is `±2`), giving one `∓2` and two `±1`: 6 vectors. For `m = 2`: `(c, -c)`, `c in {±1, ±2}`. Each listed vector is realized: `m=4`: `u` = the two `+1` indices, `v` = the two `-1` indices; `m=3`, e.g. `(1,1,-2)`: `u = {t_1,t_2}`, `v = {t_3,t_3}`; `m=2` type S: `u = {t_1, t}`, `v = {t_2, t}` (any `t`), type D: `u = {t_1,t_1}`, `v = {t_2,t_2}`. QED.

**Lemma 2.2 (multiplicities; ordered-pair form of the dichotomy).** The number of ordered pairs `(u,v)` realizing a given configuration (ranks + coefficient vector) is: `N` for `m = 2` type S (the **sliding family** `(u,v) = ({t_a, t}, {t_b, t})`, `t = 0..K`, where `t_a` is the `+1` rank), and `1` for every other configuration. Completeness:

    M(M-1) = N^2(N-1) + N(N-1) + 6*C(N,3) + 6*C(N,4).

*Proof.* Given the net coefficients, in every non-S configuration the multiset `u` (resp. `v`) is forced: `m = 4`: `u` = plus-indices; `m = 3`: the `∓2` index appears doubled on one side and the `±1` indices on the other; `m = 2` type D: `u = {t_+,t_+}`, `v = {t_-,t_-}`. In type S the cancelled index `t` is free over `{0..K}`: exactly `N` ordered pairs; these are precisely the representations of `D = P_{t_a} - P_{t_b}`, matching Addendum Theorem A.3 (which holds verbatim on every sigma-path by Lemma 1.1). The identity: `2 C(N,2) * N + 2 C(N,2) + 6 C(N,3) + 6 C(N,4) = M(M-1)`; checked exactly at `N = 3` (`30 = 18 + 6 + 6 + 0`) and `N = 4` (`90 = 48 + 12 + 24 + 6`); both sides are quartic... [both sides are polynomials in `N` of degree 4; equality at 5 points `N = 0,1,2,3,4` (degenerate cases trivially checked) proves it identically]. QED.

Therefore

    sum_{u != v} |E_sigma e_{qr}(b D_uv)| = sum_{configurations} mult(config) * |E_sigma e_{qr}(b D_config)|,     (2.1)

with `mult = N` on type S and `1` otherwise.

---

## 3. The partition identity and the contour bound (proved)

**Lemma 3.1 (exact rank-conditioning partition identity).** Let `psi_0, ..., psi_m : L -> C` be any functions, extended completely multiplicatively to products, and let `(W_0,...,W_m)` be the cells of the sigma-path at fixed ranks. Under uniform `sigma`, `(W_0,...,W_m)` is a uniform ordered set partition of `L` with sizes `(n_0,...,n_m)`, and **exactly**

    Phi(psi; n) := E_sigma[ prod_s psi_s(prod W_s) ] = ( K! / prod_s n_s! )^{-1} [x_0^{n_0}...x_m^{n_m}] prod_{ell in L} ( sum_s x_s psi_s(ell) ).

*Proof.* The positions `1..t_1, (t_1,t_2], ..., (t_m, K]` are fixed; a uniform permutation of `L` induces the uniform distribution on ordered set partitions with these sizes. Expanding `prod_ell (sum_s x_s psi_s(ell))` indexes assignments `f: L -> {0..m}`; the coefficient of `prod x_s^{n_s}` is the sum of `prod_s psi_s(prod f^{-1}(s))` over assignments with `|f^{-1}(s)| = n_s`, whose number is the multinomial. QED.

*(Verified against the true permutation law: all `7! = 5040` orderings, 6 configurations including empty and singleton cells; max error `2e-15`. Verified again end-to-end inside the full bias formula, Section 9.)*

Empty cells: if `n_s = 0`, delete cell `s` (set `x_s = 0`); the identity persists over the nonempty cells.

**Lemma 3.2 (contour decay).** Let `t_chi := |sum_{ell in L} chi(ell)| / K in [0,1]` for any unimodular `chi` on `L`. With empty cells deleted and at most 5 nonempty cells,

    |Phi(psi; n)| <= min( 1 ,  C_* K^2 exp( - sum_{s < s'} (n_s n_{s'} / K) (1 - t_{psi_s bar-psi_{s'}}) ) ),   C_* = e^5 / sqrt(2 pi) < 60.

*Proof.* `|Phi| <= 1` is trivial (average of unimodular numbers). Cauchy's integral formula on the polydisc `|x_s| = rho_s := n_s/K` gives

    |Phi| <= ( multinom(K;n) prod_s rho_s^{n_s} )^{-1} * max_theta prod_{ell} | sum_s rho_s e^{i theta_s} psi_s(ell) |.

*Prefactor:* with `K! >= sqrt(2 pi K) K^K e^{-K}` and `n! <= e n^{n + 1/2} e^{-n}`,

    multinom(K;n) prod rho_s^{n_s} >= sqrt(2 pi K) e^{-j} / prod_s sqrt(n_s) >= sqrt(2 pi) e^{-5} K^{-2}

for `j <= 5` nonempty cells (`prod sqrt(n_s) <= K^{5/2}`, one factor `sqrt K` cancels). So the reciprocal is `<= C_* K^2`.

*Max term:* for unimodular `z_s` and weights `rho_s` summing to 1, the exact identity

    | sum_s rho_s z_s |^2 = 1 - sum_{s<s'} rho_s rho_{s'} | z_s - z_{s'} |^2

holds (expand both sides). With `z_s = e^{i theta_s} psi_s(ell)` and `log y <= (y^2 - 1)/2` for `y in (0,1]`:

    log prod_ell |...| <= -(1/2) sum_{s<s'} rho_s rho_{s'} sum_ell | e^{i theta_s} psi_s(ell) - e^{i theta_{s'}} psi_{s'}(ell) |^2,

and `sum_ell |...|^2 = 2K - 2 Re( e^{i(theta_s - theta_{s'})} sum_ell psi_s bar-psi_{s'}(ell) ) >= 2K (1 - t_{psi_s bar-psi_{s'}})` **uniformly in the phases** (only the modulus of the ratio-character sum enters). Combining gives the exponent `sum_{s<s'} rho_s rho_{s'} K (1 - t) = sum (n_s n_{s'}/K)(1-t)`. QED.

*(Verified numerically; the tested `|Phi|/bound` never exceeded `0.002`.)*

---

## 4. Character expansion and coefficient norms (proved)

By Lemma 1.2, for each slot `s = 1..m` the multiplier `m_s := b c_s A_X` is a unit mod `qr` and, additively splitting the bracket,

    e_{qr}(b D_uv) = prod_{s=1}^m e_{qr}( m_s V_s ),   V_s := (prod W_0) R_1 ... R_{s-1}  (a unit mod qr).

**Lemma 4.1 (Gauss/CRT coefficients).** For `gcd(m, qr) = 1` and units `v`: `e_{qr}(m v) = sum_{chi mod qr} c_chi(m) chi(v)` with `c_chi(m) = chi(m) tau(bar-chi)/phi(qr)`, `tau(chi) = sum_w chi(w) e_{qr}(w)`. By CRT (`chi = chi_q chi_r`), `tau(chi) = chi_q(r) chi_r(q) tau_q(chi_q) tau_r(chi_r)`, `|tau_p(chi_p)| = sqrt p` (nonprincipal), `tau_p(chi_{0,p}) = mu(p) = -1`. Hence:

    sup_chi |c_chi(m)| <= sqrt(qr)/phi(qr) <= 2/sqrt(qr) <= 2/(eta X^2);
    ||c(m)||_2 = 1   (Parseval:  sum_chi |c_chi|^2 = phi^{-1} sum_v |e_{qr}(mv)|^2 = 1);
    ||c(m)||_1 <= sqrt(qr) <= 2H = 2 eta X^2.

Principal components give **smaller** coefficients (`sqrt q / phi(qr)`, `1/phi(qr)`): the all-principal tuple contributes `phi(qr)^{-m} <= X^{-8+o(1)}` — **there is no main term in the `q != r` sector**; the exact centring is entirely the `q = r` diagonal. *(All standard; Davenport Ch. 9. Verified numerically mod 35: `||c||_2 = 1.000000` exactly.)*

Expanding every slot and multiplying:

    E_sigma[ e_{qr}(b D_uv) ] = sum_{(chi^{(1)},...,chi^{(m)})} ( prod_s c_{chi^{(s)}}(m_s) ) * Phi(psi; n),      (4.1)

where the **cell characters** are `psi_i = prod_{s > i} chi^{(s)}` (cell `i = 0..m`; `psi_m = 1`, the **tail cell carries the principal character**), because `chi^{(s)}(V_s)` contributes `chi^{(s)}` to every cell `W_0, R_1, ..., R_{s-1}`. Key structural facts: `psi_{i-1} bar-psi_i = chi^{(i)}` and generally `psi_i bar-psi_{i'} = prod_{i < s <= i'} chi^{(s)}`.

**Empty `W_0` (`t_1 = 0`).** Then `V_1 = 1` and slot 1 collapses to the deterministic unimodular constant `e_{qr}(m_1)`: do not expand it. The active slot set is `S = {1..m}` minus `{1}` iff `n_0 = 0`; `|S| in {m-1, m}`. (Note the tail slot `m` never collapses: `chi^{(m)}` acts on all earlier cells even when the tail cell is empty.)

**Lemma 4.2 (group sums).** For slots `s, s'` and `B(rho) := sum_{chi chi' = rho} |c_chi(m_s)| |c_{chi'}(m_{s'})|` (a `g = 2` group): `sup_rho B(rho) <= ||c(m_s)||_2 ||c(m_{s'})||_2 = 1` (Cauchy-Schwarz) and `sum_rho B(rho) = ||c(m_s)||_1 ||c(m_{s'})||_1 <= 4 eta^2 X^4`. For a single slot (`g = 1` group): `sup <= 2/(eta X^2)`, `sum = ||c||_1 <= 2 eta X^2`. *(Verified: the toy pairing sum equals `1.000000`.)*

*(The entire chain (4.1) — slots, `psi` bookkeeping, empty-`W_0` collapse, tail principal character — was verified end-to-end this session: direct average over all `720` orderings at `K = 6`, `qr = 15`, `A = 2`, `b = 4`, against the character formula, for 8 configurations covering `m = 2, 3, 4`, empty `W_0`, empty tail, and micro gaps; max error `4.1e-16`.)*

---

## 5. Counting non-cancelling characters (proved)

**Lemma 5.1 (bad-character count).** Call `chi mod qr` **bad** if `t_chi >= 3/4` (the principal character is bad, `t = 1`); let `beta = #Bad`. For `X > 8/eta^2`:

    beta <= 6 (4/3)^6 phi(qr) / K^3 <= 1100 eta^2 X (log X)^3.

*Proof.* Block primes are distinct units mod `qr`. By orthogonality, `sum_chi |sum_ell chi(ell)|^6 = phi(qr) * #{(a_1..a_6) in L^6 : a_1 a_2 a_3 ≡ a_4 a_5 a_6 (mod qr)}`. Both products are positive integers `< (2X)^3 = 8 X^3 < eta^2 X^4 <= qr`, so the congruence is an equality; by unique factorization the multisets agree, giving at most `3! = 6` ordered solutions per left triple: count `<= 6 K^3`. Chebyshev at level `(3K/4)^6`: `beta (3K/4)^6 <= 6 phi(qr) K^3`. Insert `phi(qr) <= 4 eta^2 X^4` and `K >= X/(2 log X)`: `beta <= 6 (4/3)^6 * 4 eta^2 X^4 * 8 (log X)^3 / X^3 <= 1100 eta^2 X (log X)^3`. QED.

*(The orthogonality identity was verified exactly at toy scale: `sum_chi |sum|^6 = 163656 = phi * 6819` mod 77.)* **This is the only arithmetic input.** Good characters (`t < 3/4`) have deficit `1 - t > 1/4`. No zero-density theorem, explicit formula, or GRH appears anywhere in the proof. *(Optional cosmetic strengthening to `beta = X^{o(1)}` via the verified log-free density of Chen, arXiv:2507.08296 Thm 1.4, is available but unused.)*

---

## 6. Coordinates and the matching lemma (new; complete)

Fix a configuration with `<= 1` cell of size `< w_0`, where

    w_0 := C_3 log X,   C_3 := 600.

Cells of size `>= w_0` are **big**; since `sum n_s = K` over `<= 5` cells, some cell `s*` (the **macro cell**) has `n_{s*} >= K/5 >= w_0` (for `X >= X_0(C_3)`). List the big cells `i_0 < i_1 < ... < i_p`; by hypothesis at most one cell (possibly empty) is not big, so `p >= m - 1` and consecutive big cells differ by at most 2 in index. *(If the macro cell is the tail cell, `psi_{s*}` is built from all slots `> s*`; if `s* = m` then the coordinates below are `sigma_i = psi_i` themselves — the tail's principal character needs no separate treatment.)*

**Coordinates.** For each big cell `i != s*` define the **ratio character** `sigma_i := psi_i bar-psi_{s*}` (`sigma_{s*} := 1`). Slots between consecutive big cells form **groups**: `G_j = { s : i_{j-1} < s <= i_j }`, `g_j = |G_j| in {1, 2}` (`g_j = 2` exactly when the unique micro cell lies between `i_{j-1}` and `i_j`), with group product `prod_{s in G_j} chi^{(s)} = psi_{i_{j-1}} bar-psi_{i_j} = sigma_{i_{j-1}} bar-sigma_{i_j}`. Active slots outside all groups are **orphans**: slot 1 when `0 < n_0 < w_0` (cell 0 micro; absent when `n_0 = 0`), or slot `m` when `n_m < w_0` (tail micro or empty). In the `<= 1`-micro-cell regime there is **at most one orphan**. An orphan's character appears in no `sigma_i` (front orphan: `chi^{(1)}` appears only in `psi_0`, and cell 0 is not a coordinate; back orphan: `chi^{(m)}` appears in every `psi_i`, `i < m`, but cancels in every ratio `psi_i bar-psi_{s*}`).

**Lemma 6.1 (triangular bijection).** Designate in each group `G_j` one slot `d_j`. The map

    (chi^{(s)})_{s in S}  |-->  ( (sigma_{i_j})_{i_j != s*} ; (chi^{(s)})_{s in G_j, s != d_j} ; (chi^{(s)})_{s orphan} )

is a bijection of the full product of character groups mod `qr`. *Proof.* The map is a homomorphism given, in additive notation on the dual group, by a square integer matrix which is triangular with `±1` diagonal after ordering coordinates by distance from `s*` (each `sigma_{i_j}` equals the adjacent-to-`s*` group product times the previous `sigma`, and each designated slot is solved from its group product and the free slots). Invertible, hence bijective. QED.

**Pattern partition.** For each character tuple, mark each coordinate `sigma_{i_j}` **bad** or **good** per Lemma 5.1; this partitions the tuples into `2^p` **patterns** `P`; `f(P)` = number of good ("free") coordinates, `k(P) = p - f`. For any tuple of pattern `P`, keep in Lemma 3.2 only the deficits of the pairs `(i_j, s*)` with `sigma_{i_j}` good: each such pair contributes rate `(n_{i_j} n_{s*}/K)(1 - t_{sigma_{i_j}}) >= (w_0/5)(1/4) = (C_3/20) log X = 30 log X`. Hence

    |Phi| <= 1  if f = 0;   |Phi| <= C_* K^2 X^{-30 f}  if f >= 1.       (6.1)

**Lemma 6.2 (matching lemma on the path).** Root the path `i_0 - i_1 - ... - i_p` (vertices = big cells, edges = groups) at `s*`; it splits into two arms. For each vertex `v != s*` let `e_v` be its **inner edge** (toward `s*`); each edge has exactly one outer endpoint, so `v |-> e_v` is a bijection between non-root vertices and edges. Then for every pattern `P`,

    Sigma(P) := sum_{tuples of pattern P} ( prod_{s in S} |c_{chi^{(s)}}(m_s)| ) * [decay (6.1)]
             <=  Orph * ( prod_{v bad} beta * sup_rho B_{e_v}(rho) ) * ( prod_{v free} l1(B_{e_v}) ) * D(f),

where `Orph <= 2 eta X^2` per orphan (`= 1` if none), `l1(B_e) = sum_rho B_e(rho)`, and `D(f) = 1` if `f = 0`, `= C_* K^2 X^{-30 f}` if `f >= 1`.

*Proof.* Sum over orphan characters first: each contributes `||c||_1 <= 2 eta X^2` (Lemma 4.1), independently of everything else, and no decay factor is attached to them. Next, for fixed `sigma`-coordinates, sum over the group-internal free slots: this produces exactly `prod_j B_j(sigma_{i_{j-1}} bar-sigma_{i_j})` (Lemma 4.2). Finally sum over the `sigma`-coordinates arm by arm, **outermost vertex first**: when vertex `v` is processed, its inner neighbour's coordinate is still unsummed (fixed), so

    sum over sigma_v of B_{e_v}(sigma_{inner} bar-sigma_v) = l1(B_{e_v})           (v free: full range),
    sum over sigma_v in Bad of B_{e_v}(...) <= beta * sup_rho B_{e_v}(rho)          (v bad).

Every edge is consumed exactly once (by its outer endpoint); the decay factor `D(f)` is a constant over the summation and multiplies through. QED.

**Lemma 6.3 (pattern domination).** With `SUP(e) = 2/(eta X^2)` for `g = 1` edges and `1` for `g = 2` edges, and `L1(e) = 2 eta X^2` resp. `4 eta^2 X^4`, define the ledger bound `U(P) = Orph * prod_{bad} beta SUP(e_v) * prod_{free} L1(e_v) * D(f)`. Then for `X >= X_0(eta)`,

    sum over all 2^p patterns of U(P)  <=  2 U(all-bad).

*Proof.* `U(P)/U(all-bad) = prod_{v free} [ L1(e_v) / (beta SUP(e_v)) ] * C_* K^2 X^{-30 f}`. Using `beta >= 1` (the principal character is bad) and `K <= 3X/log X`: per free vertex, for `g = 1`: `(2 eta X^2)/(2/(eta X^2)) * (C_* K^2)^{1/f} X^{-30} <= eta^2 C_* 9 X^{4 + 2 - 30} <= X^{-23}`; for `g = 2`: `4 eta^2 X^4 * (C_* K^2)^{1/f} X^{-30} <= X^{-23}`. Hence `U(P) <= X^{-23 f} U(all-bad)` and the sum over `2^p <= 16` patterns is `<= (1 + 16 X^{-23}) U(all-bad) <= 2 U(all-bad)`. QED.

Combining (4.1), Lemma 6.2, Lemma 6.3:

**Proposition B (master per-configuration bound).** For any configuration with at most one cell of size `< w_0`,

    | E_sigma[ e_{qr}(b D) ] |  <=  min( 1 ,  2 * Orph * beta^p * prod_{edges e} SUP(e) ),

with `p` = (number of big cells) - 1 edges, `SUP(e) = 2/(eta X^2)` (`g=1`) or `1` (`g=2`), `Orph = 2 eta X^2` if an orphan slot is present, else `1`.

---

## 7. The ledger (complete case enumeration) and proof of Proposition A

Recall `beta <= 1100 eta^2 X log^3 X` (write `beta <= C_b X log^3 X`, `C_b = 1100 eta^2`), `N <= 4X/log X`, `w_0 = 600 log X`, `M >= X^2/(8 log^2 X)`. All bounds below are per fixed `(q, r, a)`.

**Trivial classes** (bias `<= 1`, counted with multiplicity):

- **T1** (any `m`; `>= 2` cells of size `< w_0`, empties included). Configurations: choose the two constrained cells (`<= 10` ways), their sizes (`< w_0` each), the remaining `<= m - 2 <= 2` free rank parameters (`<= N^2`), pattern (`<= 6`); multiplicity `<= N` only in the `m = 2` sub-case, which has no free rank parameter left. Total pairs `<= C N^2 w_0^2 <= C * 16 X^2/log^2 X * 360000 log^2 X <= C' X^2 <= 8 C' M log^2 X`. **Contribution `<= C M (log X)^2`.**
- **T2** (`m = 2`, any cell `< w_0`, incl. empty `W_0` and empty tail). Configurations `<= 3 * w_0 * N * 4`; multiplicity `<= N` (type S). Total pairs `<= 12 N^2 w_0 <= C X^2/log X`. **Contribution `<= C M (log X)`.** *(These are the near-diagonal short-window classes of the sliding family; the multiplicity-`N` dichotomy enters here and in C4 only, and never meets the character machinery.)*
- **T3** (`m = 3`, any cell `< w_0`, incl. empties). Configurations `<= 4 * w_0 * N^2 * 6`, multiplicity 1. Total `<= 24 N^2 w_0`. **Contribution `<= C M (log X)`.**

**Character classes** (all remaining configurations have `<= 1` cell `< w_0`; apply Proposition B):

- **C1** (`m = 4`, all five cells `>= w_0`). `p = 4`, four `g=1` edges, no orphan. Bound `2 beta^4 (2/(eta X^2))^4 <= C(eta) X^{-4} log^{12} X`. Count `<= 6 C(N,4) <= 64 X^4/log^4 X`. **Contribution `<= C(eta) (log X)^8.`**
- **C2a** (`m = 4`, exactly one micro cell, **interior** — cell 1, 2 or 3; `n_s >= 1` automatic). Four big cells, `p = 3`; one `g = 2` edge bridging the micro cell (Cauchy-Schwarz sup `<= 1`), two `g = 1` edges; no orphan. Bound `2 beta^3 * 1 * (2/(eta X^2))^2 = 8 beta^3/(eta^2 X^4) <= 8 C_b^3 eta^{-2} X^{-1} log^9 X`. Count `<= 3 * 6 * N^3 w_0 <= 18 * 64 X^3/log^3 X * 600 log X = C X^3 / log^2 X`. **Contribution `<= C(eta) M (log X)^9.` — THE BINDING CASE.** The margin is polylog only: with `beta = X^{4/3}` the same arithmetic would give `X^3 log^{-2} X * X^{4 - 4} = X^3`, exceeding the `M X^{o(1)} = X^{2 + o(1)}` budget — the adjudication's refutation of the earlier `X^{1/3}`-margin claim, reproduced and machine-checked. Lemma 5.1's `beta <= C X log^3 X` is exactly strong enough; the exponent 9 (`= 3 * 3` from `beta^3`) fixes `C_0 = 9`.
- **C2b** (`m = 4`, cell 0 micro, `0 < n_0 < w_0`). Big cells `1,2,3,4`, `p = 3`, three `g=1` edges, **front orphan** slot 1. Bound `2 * 2 eta X^2 * beta^3 (2/(eta X^2))^3 = 32 beta^3/(eta^2 X^4) <= C(eta) X^{-1} log^9 X`. Count `<= 6 N^3 w_0`. **Contribution `<= C(eta) M (log X)^9.`**
- **C2c** (`m = 4`, `n_0 = 0`, all others big). Slot 1 collapses to a unimodular constant (no orphan); `p = 3`, three `g=1` edges. Bound `2 beta^3 (2/(eta X^2))^3 <= C(eta) X^{-3} log^9 X`. Count `<= 6 N^3`. **Contribution `<= C(eta) (log X)^6.`**
- **C2d** (`m = 4`, tail cell `< w_0`, including empty tail `t_4 = K`). Big cells `0..3`, `p = 3`, three `g=1` edges, **back orphan** slot 4 (present even when the tail cell is empty, since slot `m` never collapses). Bound as C2b: `<= C(eta) X^{-1} log^9 X`. Count `<= 6 N^3 w_0 + 6 N^3`. **Contribution `<= C(eta) M (log X)^9.`**
- **C3** (`m = 3`, all four cells `>= w_0`). `p = 3`... [big cells = all 4 cells; `p = 3` coordinates? No: `p = |Big| - 1 = 3` vertices besides the root — three `g=1` edges]. Bound `2 beta^3 (2/(eta X^2))^3 <= C(eta) X^{-3} log^9 X`; count `<= 6 C(N,3) <= N^3`. **Contribution `<= C(eta) (log X)^6.`**
- **C4** (`m = 2`, all three cells `>= w_0`; multiplicity `N` for type S, 1 for type D). `p = 2`, two `g=1` edges. Bound `2 beta^2 (2/(eta X^2))^2 <= C(eta) X^{-2} log^6 X`; pairs `<= 2 C(N,2) (N + 1) <= 2 N^3`. **Contribution `<= C(eta) X (log X)^3 <= C(eta) M.`**

Every configuration lies in exactly one of T1-T3, C1-C4 (by `m` and the number/position of sub-`w_0` cells; overlaps of the T-classes only inflate constants). Summing:

    sum_{u != v} | E_sigma e_{qr}(b D_uv) |  <=  C(eta) M (log X)^9,

uniformly in `q != r in Q_X` and `1 <= |a| < H`. **Proposition A is proved.**

---

## 8. Assembly: proof of Theorem RQM

**(i) Fixed harmonic.** For `1 <= |a| < H` (negative `a` by symmetry `Psi_{-a} = conj(Psi_a)`):

    E_sigma[E_a] = M(M-1) kappa_{2,a} + sum_{q != r} p_{q,a} p_{r,a} * E_sigma[ sum_{u != v} e_{qr}(b D_uv) ]
                <= M(M-1) kappa_{2,a} + m_a^2 * C(eta) M (log X)^9.

Diagonal: `kappa_{2,a} = sum_q p_{q,a}^2 <= m_a max_q p_{q,a}`, and by (N1) `max_q p_{q,a} <= ||rho||_inf / D_X <= ||rho||_inf / (delta_rho #Q_X)` with `#Q_X >= eta X^2/(8 log X)` (PNT for the shell), so `M max_q p_{q,a} <= 128 ||rho||_inf / (delta_rho eta log X)`. Hence `M(M-1) kappa_{2,a} <= C(eta,rho) M m_a / log X` and

    E_sigma[E_a] <= C(eta, rho) M (log X)^9   uniformly for 1 <= |a| < H.   **(i) proved.**

**(ii) Aggregate.** `R_a` is the `q != r` part, so for `a < H`: `E_sigma[R_a] <= m_a^2 C(eta) M (log X)^9`, hence `sum_{1 <= a < H} E_sigma[R_a]/m_a <= C M (log X)^9 sum_a m_a = C M (log X)^9 / 2` (Paper II (3.9): `sum_{a>=1} m_a = 1/2`). For `a >= H`: `|R_a| <= M^2 m_a^2` trivially, and by Schwartz decay (`rho(t) <= C_rho t^{-6}`) plus (N1), `m_a <= (#Q_X/D_X) sup_{t > a/2} rho(t) <= C_rho' a^{-6}`, so `sum_{a >= H} M^2 m_a <= C X^4 H^{-5} = o(1)`. This proves the first half of (ii). Frobenius: by Paper II Prop. 3.1, `F_X <= 2 sum_{a >= 1} E_a / m_a`; termwise, `E_a/m_a = M(M-1) kappa_{2,a}/m_a + R_a/m_a <= M^2 max_q p_{q,a} + R_a/m_a`, and `sum_a max_q p_{q,a} <= (1/D_X) sum_a sup_{(a/2, a]} rho <= C_rho / D_X`, so `M^2 sum_a max_q p_{q,a} <= C(eta,rho) M / log X`. Hence `E_sigma[F_X] <= C(eta, rho) M (log X)^9`. **(ii) proved.** QED (Theorem RQM).

**Constants ledger.** `w_0 = C_3 log X`, `C_3 = 600`; decay per free coordinate `X^{-C_3/20} = X^{-30}`; `Lambda = C_3/20 - 2 = 28` (absorbing `C_* K^2 <= 60 X^2`); pattern-domination margin `X^{-23}` per free vertex; `beta <= 1100 eta^2 X log^3 X`; `SUP(g1) = 2/(eta X^2)`, `SUP(g2) = 1`, `L1(slot) = 2 eta X^2`; `C_* = e^5/sqrt(2 pi) < 60`; **`C_0 = 9`** (absolute; sourced entirely from `beta^3` in the binding class C2a/C2b/C2d); `C(eta, rho)` effective, polynomial in `eta^{±1}, ||rho||_inf, delta_rho^{-1}, C_rho`. Largeness: `X > 8/eta^2` (Lemma 5.1); `K/5 >= w_0`, i.e. `X >= 6000 log^2 X`-scale; `X >= X_0` for (N2) and Lemma 6.3's `X^{-23}` absorption — all effective.

---

## 9. Numerical verification (this session; scripts in scratchpad)

1. **Partition identity vs the true sigma-path law** (`assembly_checks.py`, CHECK 1): all `7!` orderings, `q = 11` characters, 6 cell configurations (including sizes `(4,3)`, `(1,1,5)`, `(1,2,2,1,1)`): max `|direct - identity| = 2e-15`. *(Independent of, and consistent with, the workbench's 5040-permutation check.)*
2. **Contour bound** (CHECK 2): `|Phi| <=` bound in all cases; worst ratio `0.002`.
3. **Gauss/CRT norms and Cauchy-Schwarz pairing** (CHECK 3, mod 35): `||c||_2 = 1.000000` exactly for all tested `m`; `sup|c| = sqrt(qr)/phi(qr)` exactly; pairing sum `sum_chi |c(1)_chi||c(2)_chi| = 1.000000 <= 1`.
4. **Ledger exponent arithmetic** (CHECK 4, symbolic in `(X-exponent, log-exponent)`): binding case `X^2 log^7` vs budget `X^2 * polylog` (PASS, polylog margin); the refuted `beta = X^{4/3}` scenario reproduces the judge's FAIL (`X^3`); `|T|=0` all-bad `X^0 log^8`; end-orphan case `X^2 log^7`; trivial class `X^2 log^0`. *(Note: the per-class `log` exponents there are relative to the raw count normalization; expressed against `M = X^2 log^{-2} X` they are the `log^9` of Section 7.)*
5. **Sixth-moment orthogonality** (CHECK 5, mod 35 and mod 77): `sum_chi |sum_ell chi|^6 = phi * #collisions` exactly (integer match `163656`); Chebyshev count holds.
6. **End-to-end bias formula** (`e2e_bias_check.py`, new): `E_sigma[e_{qr}(b D)]` by direct average over all `720` orderings (`K = 6`, `qr = 15`, `A_X`-surrogate `= 2`, `b = 4`) vs the full Section-4 character expansion, for 8 configurations covering: `m = 2` sliding, `m = 2` doubled `(2,-2)`, empty `W_0` (slot-1 constant), two `m = 3` patterns, `m = 4` with empty tail (`t_m = K`), `m = 4` with empty `W_0`, `m = 4` with micro gaps. Max error `4.1e-16`. This verifies every structural claim of Sections 2 and 4 simultaneously.

---

## 10. Honest scope (to be stated verbatim in any publication)

The sigma-path centres are not primorials except for the identity ordering; this is a **model theorem about the architecture**. It is the first unconditional PGD2-type estimate in any model; it removes GRH from the i.i.d.-model input (vector B2) by converting "pointwise smallness of `sum chi(ell)` (GRH)" into "a *count* of non-cancelling characters (orthogonality + unique factorization)"; and it certifies that the reciprocal-frame target is true generically at the critical length. It says nothing about Fortune, PGD2, or the increasing order, and it **relocates rather than shrinks** the Fortune-relevant difficulty: a single order has zero entropy, and the order-averaging mechanism that manufactures the decay contributes nothing pointwise. The forward-looking mathematics it opens is the variance version `E_sigma[(E_a)^2] << M^2 X^{o(1)}` (same machinery, ~8 cells), which would upgrade expectation to concentration over orderings.

## 11. Residual-item ledger

- **(N1)** `rho >= delta_rho` on `[1/2, 1]`: hypothesis-level frame-admissibility normalization, stated in the theorem; genuinely necessary in some form (Section 0); not a mathematical gap. *Label: proved-under-stated-hypothesis.*
- **(N2)** Effective `K ~ X/log X` and shell `#Q_X ~ H/log H` bounds: standard, effective (PNT/Chebyshev). *Label: standard.*
- Gauss-sum facts (Lemma 4.1): standard, three-line proofs, inlineable (Davenport Ch. 9). *Label: standard.*
- Everything else — the configuration enumeration (Lemma 2.1-2.2 with the exact completeness identity), the coordinates bijection (6.1), the matching lemma (6.2), pattern domination (6.3), the ledger (Section 7), and the assembly (Section 8) — is proved above in full. **No GAP labels remain.**