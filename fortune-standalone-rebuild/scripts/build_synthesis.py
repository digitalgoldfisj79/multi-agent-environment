#!/usr/bin/env python3
"""Rebuild the conditional-and-barriers synthesis without internal programme labels."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE_COMMIT = "be42a5c80d2189df2f20c8055ee7107768cb7299"
SOURCE_PATH = "publications/fortune-conditional-and-barriers-20260806/MANUSCRIPT.md"
OUT = ROOT / "publications/fortune-standalone-20260811/synthesis_conditional_and_barriers"

HEADER = r'''# An Exact Conditional Criterion for Fortune's Conjecture and Barriers to Standard Prime-Detection Mechanisms

## Abstract

Let \(P_n=p_n\#\) and let \(F_n\) be the least integer \(m>1\) for which \(P_n+m\) is prime. Below the square threshold, a successful offset must itself be prime. Thus eventual Fortune can be formulated as rowwise occupancy by prime pairs \((m,P_j+m)\) in windows of length comparable to the square of the next prime.

This paper gives an exact finite sufficient criterion for that occupancy. A deterministic stratification and an even-Bonferroni expansion convert the zero-row problem into factorial moments through order \(\Theta(\log X)\). If the **jointly signed** factorial-moment error against a fixed prime-tuple model is smaller than an explicit one-row margin, then every sufficiently large row succeeds. For \(\varepsilon=0.10\), model-mean ratio \(U_b/L_b\le1.10\), and even truncation \(K_b\) at approximately \(5\log(n_bB)\), the truncation error has more than the required inverse-row saving.

The implication is exact; its arithmetic hypothesis is open. We prove several obstruction results showing why familiar absolute-value implementations do not currently supply it. Termwise absolute control already demands additive \(O(1)\) accuracy for a selected-centre mean of order \(X\). Pairwise local dependency graphs fail at third order because a same-residue triple has connected coefficient of order \(1/p\), whereas every fixed pair-tree budget is of order \(1/p^2\). Absolute higher-body aggregation loses every fixed logarithmic saving at order \(\Theta(\log X)\). Fixed-order squarefree collision bounds are valid but lack a source decomposition connecting them to the detector. Heath--Brown's generalized Vaughan identity yields an exact cutoff dichotomy and an exponentially weighted residual requirement; coefficient growth alone is not an impossibility theorem.

The result is therefore a conditional theorem and a rigorously delimited obstruction analysis. The remaining direct input is a jointly signed selected-centre prime-tuple theorem through logarithmic order. Fortune's conjecture is not proved.

## 1. Scope, notation, and logical status

Fortune's conjecture states that the least positive offset producing a prime above a primorial is itself prime [1]. Write
\[
P_n=\prod_{r\le n}p_r,
\qquad
F_n=\min\{m>1:P_n+m\in\mathbb P\}.
\]
Every prime divisor of \(F_n\) exceeds \(p_n\), hence a composite \(F_n\) is at least \(p_{n+1}^2\). The relevant window is therefore at logarithmic-square scale in the size of the primorial.

The paper proves the exact implication
\[
\boxed{
\text{signed factorial-moment bound}
\Longrightarrow
\text{adaptive zero-row bound}
\Longrightarrow
\text{eventual Fortune}.
}
\tag{1.1}
\]
The first premise is an open arithmetic estimate, specified quantitatively in Sections 3--5. The second arrow is deterministic and exact. None of the finite-field or random-order models developed elsewhere is used in this chain.

Throughout, Hardy--Littlewood prime-tuple expressions are model calibrations rather than proved asymptotics [2]. Exact algebraic, combinatorial and finite calculations are distinguished from open asymptotic input.

'''

REFERENCES = r'''## References

1. R. K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Springer, 2004.
2. G. H. Hardy and J. E. Littlewood, "Some Problems of Partitio Numerorum. III. On the Expression of a Number as a Sum of Primes," *Acta Mathematica* **44** (1923), 1--70.
3. D. R. Heath-Brown, "Prime numbers in short intervals and a generalized Vaughan identity," *Canadian Journal of Mathematics* **34** (1982), 1365--1377.
4. J. Friedlander and H. Iwaniec, *Opera de Cribro*, American Mathematical Society Colloquium Publications 57, 2010.
'''


def source() -> str:
    return subprocess.check_output(
        ["git", "show", f"{SOURCE_COMMIT}:{SOURCE_PATH}"],
        cwd=ROOT,
        text=True,
    )


def main() -> None:
    src = source()
    marker = "## 2. Candidate collapse and row occupancy\n"
    p = src.find(marker)
    if p < 0:
        raise RuntimeError("synthesis source marker missing")
    text = HEADER + src[p:]

    replacements = [
        ("registered scale", "fixed scale"),
        ("registered primorial row", "fixed primorial row"),
        ("registered stratum", "fixed stratum"),
        ("registered tuple model", "chosen prime-tuple model"),
        ("registered geometry", "chosen stratification geometry"),
        ("RUHL requires", "termwise absolute factorial-moment control requires"),
        ("termwise-absolute RUHL", "termwise absolute factorial-moment control"),
        ("does not transfer to RUHL", "does not transfer to the signed factorial-moment condition"),
        ("unconditional proof of RUHL-FM, `INT-AOD` or Fortune", "unconditional proof of the signed factorial-moment hypothesis or Fortune"),
        ("`INT-SCME`", "a selected-centre linear-mean lower bound"),
        ("RUHL first-order implications", "signed factorial-moment first-order implications"),
        ("The logical spine is", "The logical spine is"),
        ("the final supported result of this programme", "the final supported result of this analysis"),
        ("throughout the programme", "throughout the analysis"),
        ("in the repository", "in the present argument"),
        ("the present package", "the present proof package"),
        ("seven-paper corpus", "supporting corpus"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)

    # Replace the internal arithmetic-interface heading/phrasing if still present.
    text = text.replace("The missing analytic theorem is uniform control of the jointly signed aggregate of `A_{b,k}` and `S_{b,k}` through `k=Theta(log X)` at the one-row scale in (3.1).",
                        "The missing analytic theorem is uniform control of the jointly signed aggregate of \(A_{b,k}\) and \(S_{b,k}\) through \(k=\Theta(\log X)\) at the one-row scale in (3.1).")
    text = text.replace("At `r=Theta(log X)`", "At \(r=\Theta(\log X)\)")
    text = text.replace("through `k=Theta(log X)`", "through \(k=\Theta(\log X)\)")
    text = text.replace("through order `Theta(log X)`", "through order \(\Theta(\log X)\)")
    text = text.replace("on `n<=z^J`", "on \(n\le z^J\)")
    text = text.replace("logarithmic `J`", "logarithmic \(J\)")
    text = text.replace("`z` exponentially", "\(z\) exponentially")
    text = text.replace("`z<=H`", "\(z\le H\)")
    text = text.replace("If `R_r` denotes", "If \(R_r\) denotes")
    text = text.replace("the `r`th", "the \(r\)-th")
    text = text.replace("For three offsets in one residue class modulo a post-terminal prime `p`", "For three offsets in one residue class modulo a post-terminal prime \(p\)")
    text = text.replace("with fixed edge constant `C`", "with fixed edge constant \(C\)")

    # Correct source-facing/project-facing phrasing.
    text = text.replace("This is a valid finite-order theorem. It does not transfer to the signed factorial-moment condition because no actual source decomposition in the present argument supplies the required coefficient family, conductor partition and row-preserving map into this energy.",
                        "This is a valid finite-order collision theorem. It does not imply the signed factorial-moment condition because no source decomposition established here supplies the required coefficient family, conductor partition and row-preserving map into this energy.")
    text = text.replace("No theorem in the present proof package proves such decay", "No theorem proved here supplies such decay")

    # Formalization section: remove unrelated Paper VII trust boundary from this standalone integer article.
    old_formal = "The current package kernel-checks the corrected detector implications, centred moment identities, selected Paper VII algebra, fixed-order collision criteria, the local tree obstruction, the signed factorial-moment first-order implications and the exact telescoping arithmetic interface. One Paper VII normalization/certificate axiom remains explicitly ledgered."
    new_formal = "For the integer chain considered in this article, the formal package kernel-checks the detector implications, centred moment identities, fixed-order collision criteria, the local third-order tree obstruction, the signed first-order implications and the exact telescoping arithmetic interface. These integer implications do not rely on the separate finite-field normalization axiom elsewhere in the repository."
    if old_formal in text:
        text = text.replace(old_formal, new_formal, 1)

    # Replace the final frontier and nonclaims with publication-facing wording, preserving mathematical content.
    a = text.find("## 12. Final frontier\n")
    if a < 0:
        raise RuntimeError("final frontier marker missing")
    text = text[:a] + r'''## 12. Final frontier

The exact conditional theorem is useful because the missing arithmetic input is unambiguous:

> **Selected-centre signed prime-tuple problem.** Prove, uniformly in every fixed terminal-prime stratum, a jointly signed prime-tuple estimate through order \(\Theta(\log X)\) whose weighted factorial-moment aggregate satisfies the margin in (3.1).

Current methods established in this article do not supply that theorem. Pair-only dependency graphs, termwise absolute factorial moments, fixed-order squarefree collision bounds without a source map, and triangle-inequality implementations of long divisor identities do not replace it. The obstruction results are scoped to those mechanisms; they are not impossibility theorems for all future signed methods.

## 13. Nonclaims and reproducibility boundary

This paper does not claim an unconditional proof of the signed factorial-moment hypothesis or Fortune's conjecture; a universal impossibility theorem for divisor identities or signed prime-tuple methods; a random-order-to-increasing-order transfer; a function-field-to-integer transfer; or complete formalisation of every result in the broader supporting corpus.

The numerical \(\beta=5\) truncation certificate always assumes
\[
\varepsilon=0.10,
\qquad
U_b/L_b\le1.10.
\]
Exact finite regressions check the local connected coefficients, finite collision ledgers and parameter arithmetic. They do not establish the selected-centre prime-tuple hypothesis. The relevant deterministic implications have Lean counterparts; open analytic premises remain explicit hypotheses.

## 14. Conclusion

At primorial centres below the next-prime square threshold, the existence problem is a prime-pair occupancy problem. Even Bonferroni truncation gives an exact route from rowwise occupancy to factorial moments, and logarithmic truncation is sufficient provided the jointly signed aggregate error is smaller than a one-row margin. This implication is elementary and exact; obtaining the signed factorial moments at selected primorial centres is not.

The barrier analysis explains why taking absolute values too early is particularly destructive. It forces constant-scale first-moment accuracy, misses third-order connected coefficients, loses fixed logarithmic savings at growing order, or creates exponentially weighted residual requirements. These results narrow the target without proving it. The remaining direct integer frontier is the selected-centre signed prime-tuple problem stated above. Fortune's conjecture remains open.

## AI-assistance disclosure

Large language models were used for symbolic and computational cross-checking, adversarial review, software drafting, formal-assurance work and editorial assembly. Exact, conditional, computational and open statements are separated explicitly. The named author takes responsibility for the mathematical content, citations, code and final presentation.

''' + REFERENCES

    forbidden = ["RUHL", "INT-AOD", "INT-SCME", "P7-CUBIC", "Paper VII", "seven-paper", "programme", "registered tuple", "registered stratum"]
    bad = [x for x in forbidden if x in text]
    if bad:
        raise RuntimeError(f"internal programme vocabulary remains: {bad}")

    # The synthesis intentionally has one numbered theorem.
    labels = re.findall(r"^### Theorem ([0-9]+\.[0-9]+)", text, re.M)
    if labels != ["3.1"]:
        raise RuntimeError(f"unexpected theorem sequence: {labels}")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "manuscript.md").write_text(text.rstrip() + "\n", encoding="utf-8")
    status = """# Standalone conditional-and-barriers synthesis — claim status

## Exact proved implication

The even-Bonferroni detector criterion (Theorem 3.1) is deterministic: the stated signed factorial-moment margin implies every sufficiently large row succeeds and hence eventual Fortune.

## Exact obstruction results

- first-order absolute-strength inversion;
- fixed-order squarefree collision bound;
- third-order failure of fixed pair-tree domination;
- absolute higher-body logarithmic-radius loss;
- Heath--Brown weighted-residual requirement.

## Conditional/open

The jointly signed selected-centre prime-tuple estimate through logarithmic order is open. Hardy--Littlewood model means are calibrations, not proved selected-centre asymptotics. Fortune's conjecture is not proved.

## Numerical certificate assumptions

The beta=5 truncation certificate assumes epsilon=0.10 and U_b/L_b<=1.10.
"""
    (OUT / "CLAIM_STATUS.md").write_text(status, encoding="utf-8")
    manifest = {
        "paper": "conditional-and-barriers synthesis",
        "source_commit": SOURCE_COMMIT,
        "source_path": SOURCE_PATH,
        "standalone": str((OUT / "manuscript.md").relative_to(ROOT)),
        "numbered_theorem_count": 1,
        "logical_cross_paper_dependencies": 0,
        "fortune_proved": False,
        "primary_open_input": "jointly signed selected-centre prime-tuple estimate through Theta(log X)",
        "beta_certificate_assumptions": {"epsilon": 0.10, "U_over_L_max": 1.10, "beta": 5},
    }
    (OUT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (OUT / "REFEREE_READ.md").write_text("""# Independent-standalone referee read — conditional/barriers synthesis

**Disposition:** `PASS_AS_CONDITIONAL_SYNTHESIS`

The internal programme labels have been removed and replaced by their mathematical content. The one exact numbered theorem remains conditional on a clearly stated signed factorial-moment premise. The beta=5 certificate states both epsilon=0.10 and U_b/L_b<=1.10. The obstruction theorems are scoped to absolute/pair-tree/divisor-identity implementations and are not advertised as universal impossibility results. A local bibliography has been added.
""", encoding="utf-8")
    print(f"SYNTHESIS_STANDALONE_BUILD_OK words={len(text.split())}")


if __name__ == "__main__":
    main()
