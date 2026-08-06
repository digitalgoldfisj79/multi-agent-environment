# C8 execution — conditional bridge and diagnostics

**Status:** `PASSED_CONDITIONAL_AND_DIAGNOSTIC`

The inherited row-uniform Hardy--Littlewood factorial-moment hypothesis through order `Theta(log X)`, with the registered exponentially small aggregate error, remains a complete conditional bridge to `INT-AOD`. It is not an established theorem for the primorial path.

Exact execution checks include:

- the corrected factorial-to-ordinary Stirling transform;
- output-prime-power subtraction at the `INT-SCME` scale;
- prime-modulus primorial-walk Parseval and collision bounds;
- local edge-kernel diagnostics;
- a patched selected-centre occupancy panel at `X=100`;
- the inherited corrected occupancy panels through `X=300` from the parent programme;
- the inherited primorial-walk trace diagnostics.

The new panel confirms that the corrected SymPy primorial call executes and contains no zero row. Cumulants vary in sign and magnitude across small strata, confirming that fitted finite-panel temperatures or fixed-order extrapolation are inadmissible. The local edge diagnostic stays well below `X/(log X)^2` on the tested panels.

The larger CPU-XL panel job `6a72d6f1a00abefd4b2932eb` was cancelled after the exact regressions and patched `X=100` panel passed. Its remaining panels were redundant, diagnostic only, and could not affect the terminal theorem ruling.

No finite computation is promoted into an asymptotic statement. The diagnostics support the registered decomposition but do not prove `INT-SCME`, `INT-LCSK`, `INT-PWOC` or `INT-SOCG`.
