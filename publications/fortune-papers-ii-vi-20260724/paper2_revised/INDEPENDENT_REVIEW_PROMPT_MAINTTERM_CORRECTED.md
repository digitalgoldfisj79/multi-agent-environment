# Independent mathematical referee prompt — corrected Paper II

Review the complete manuscript supplied after this prompt as a hostile, manuscript-only mathematical referee. The reviewed text is the 27 July 2026 corrected edition of *Prime Detection at Primorial Centres*.

Do not infer missing arguments from repository context, earlier editions, or general plausibility. Every claimed theorem must be justified by the manuscript itself or clearly labelled as conjectural, conditional, computational, architectural, or open.

Concentrate especially on the following load-bearing questions.

1. Does candidate collapse really justify replacing the ordinary shifted-prime interpretation by a two-prime detector below the square threshold?
2. Are the unweighted, weighted, and double-von-Mangoldt all-centres variance criteria correctly scaled and proved without assuming the Hardy--Littlewood conjecture?
3. Are the quantities `lambda_j`, `mu_j`, and `nu_j` consistently labelled as conjectural calibrations rather than proved asymptotics?
4. Is the proper-prime-power contamination bound valid uniformly over the block?
5. Is the corrected Fourier source identity exact, with signs and finite support handled correctly?
6. Does the manuscript honestly distinguish the single-walk source kernel from the older pair-sum reciprocal model?
7. Are any surviving statements that the reciprocal-frame estimate proves Fortune unsupported after the correction?
8. Are the retained reciprocal-frame moment, Möbius, character, coherence, and no-go results still internally valid and accurately scoped?
9. Do the introduction, abstract, theorem summaries, conclusion, and appendices consistently reflect the corrected logical boundary?
10. Identify any theorem whose proof uses an unproved transference step, incorrect main term, missing endpoint term, or invalid variance normalisation.

For every adverse finding:

- quote the exact manuscript wording;
- identify the theorem/equation/section;
- explain the mathematical failure precisely;
- classify it as load-bearing, material but repairable, expository, or false alarm;
- state the minimum repair.

Output exactly these sections:

1. `VERDICT` — one of `PROVED AS STATED`, `REQUIRES AMENDMENT`, or `NOT PROVED`.
2. `LOAD-BEARING FINDINGS`.
3. `OTHER FINDINGS`.
4. `CLAIM-BY-CLAIM STATUS` — concise table of the principal corrected claims.
5. `PUBLICATION BOUNDARY` — state explicitly what the paper does and does not prove.

A verdict of `PROVED AS STATED` requires no unresolved load-bearing or material finding. Do not reward caution or extensive qualification if an actual proof gap remains.