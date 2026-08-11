#!/usr/bin/env python3
"""Apply referee-level publication fixes after deterministic Paper II rebuild."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "publications/fortune-standalone-20260811/paper2_prime_pair_detection"
MAN = OUT / "manuscript.md"


def once(text: str, old: str, new: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"expected one occurrence of {old!r}; found {n}")
    return text.replace(old, new, 1)


def main() -> None:
    text = MAN.read_text(encoding="utf-8")
    text = once(
        text,
        "The remaining theorem is adjacent to several mature bodies of analytic number theory, but does not fit any of them directly.",
        "The remaining analytic task is adjacent to several mature bodies of analytic number theory, but does not fit any of them directly.",
    )
    text = once(
        text,
        "All asymptotic statements in this paper are proved symbolically. Computation was used for independent validation of exact identities and for diagnostics that are explicitly excluded from the proofs.",
        "Every asymptotic statement presented as a proved result is established analytically in the text. The Hardy--Littlewood mean formulae are conjectural calibrations and are explicitly excluded from that claim. Computation was used for independent validation of exact identities and for diagnostics that are not proof inputs.",
    )
    text = once(
        text,
        "The supplementary archive contains the source manuscript, validators, phase reports, data summaries, a manifest, and checksums. The numerical panels are descriptive and are not used to establish any theorem.",
        "The accompanying reproducibility archive separates proof text from validation material and records the source manuscript, validators, data summaries, manifests and checksums. The numerical panels are descriptive; no theorem in this article depends on a finite numerical panel.",
    )
    MAN.write_text(text, encoding="utf-8")

    referee = """# Independent-standalone referee read — Paper II

**Disposition:** `PASS_AFTER_PUBLICATION_FIXES`

The rebuilt manuscript was read as if no other Fortune manuscript were available. The theorem/proposition/lemma/corollary sequence is unchanged from the authoritative corrected source (24 statements). No load-bearing definition or proof refers to Paper I, Paper III, an internal programme label, or a superseded centring convention.

## Publication fixes made after the read

1. Replaced the ambiguous phrase `the remaining theorem` by `the remaining analytic task`.
2. Narrowed the reproducibility claim from `all asymptotic statements` to asymptotic statements actually presented as proved results, explicitly excluding the conjectural Hardy--Littlewood calibrations.
3. Clarified that finite numerical panels are validation/diagnostic material and are not proof dependencies.

## Remaining mathematical boundary

The manuscript proves exact detector implications and reciprocal-frame structural results. It does **not** prove any of the sparse-centre variance targets (12.1)--(12.3), a source-to-reciprocal transference theorem, a prime-pair asymptotic at primorial centres, or Fortune's conjecture.

## Referee risk still requiring human specialist review

The exact identities and elementary implications are comparatively low risk. The most appropriate external review is analytic-number-theory scrutiny of the positioning of the open variance target, the claimed scope of the no-go mechanisms, and literature priority for the reciprocal-frame structural results.
"""
    (OUT / "REFEREE_READ.md").write_text(referee, encoding="utf-8")

    reproducibility = """# Reproducibility boundary — Paper II

The manuscript is mathematically readable without executing code. Computation has only the following roles:

- exact finite enumeration checking the pair-sum fourth-moment count;
- floating-point residual checks of algebraic/Fourier identities;
- finite CRT/character reconstruction checks;
- finite coherence and reciprocal-pair diagnostics.

None of these computations establishes an asymptotic theorem. The Hardy--Littlewood baseline formulae are conjectural analytic calibrations, not computational findings. The final publication bundle must include the corresponding validators and checksums under a separate reproducibility-support directory; their absence from a reader's environment does not change any theorem statement or proof in `manuscript.md`.
"""
    (OUT / "REPRODUCIBILITY.md").write_text(reproducibility, encoding="utf-8")

    print("PAPER2_REFEREE_POSTPROCESS_OK")


if __name__ == "__main__":
    main()
