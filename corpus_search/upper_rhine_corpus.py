"""Exa agent run: Upper Rhine / Lake Constance / Swabia mixed-manuscript corpus, 1400-1455.

Usage:
    export EXA_API_KEY=...
    python upper_rhine_corpus.py > upper_rhine_corpus_output.json
"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.exa.ai",
    api_key=os.environ["EXA_API_KEY"],
)

QUERY = r"""
Build as complete a corpus as possible of digitised manuscripts relevant to the
following historical search space.

DATE:
Manuscripts produced, copied, compiled, or substantially assembled between
1400 and 1455. If a catalogue gives a range overlapping 1400-1455, include it
but record the uncertainty.

GEOGRAPHY:
The Upper Rhine–Lake Constance–Swabia corridor broadly construed:
Alsace / Strasbourg / Haguenau, the Upper Rhine, Basel, the southern Black
Forest, Lake Constance / Konstanz, Schaffhausen, St Gallen, Swabia,
Augsburg, and Vorarlberg, plus immediately connected neighbouring centres
where there is documented contemporary movement into this corridor.

A manuscript qualifies geographically if there is positive evidence that it
was produced, copied, compiled, owned, used, commissioned, or documented in
this region during the relevant period. Do NOT infer provenance merely from
its present repository.

CONTENT:
Find mixed manuscripts, Sammelbände, Hausbücher, practical compilations or
working books containing at least TWO of the following:

1. herbal, botanical, materia-medica or plant material
2. medical, pharmaceutical, apothecary or recipe material
3. astrology, astronomy, calendrical, zodiacal or computistical material
4. natural philosophy, cosmology, meteorology or related diagrammatic material

Give particular attention to manuscripts containing THREE OR MORE categories,
but do not exclude two-category witnesses.

The objective is exhaustive DISCOVERY, not a selection of famous examples.
Search manuscript catalogues, library databases, digitisation portals,
scholarly catalogues, manuscript descriptions, older printed catalogues,
incunabula/manuscript research resources, and relevant German-, French-,
Italian- and Latin-language sources.

For every candidate:

- identify repository and current shelfmark
- manuscript/common title if any
- catalogue date and dating evidence
- stated place of origin
- documented provenance before 1455 where available
- exact geographic reason for inclusion
- identify which content categories are actually present
- provide evidence for EACH assigned content category
- provide a direct digitisation URL if one exists
- provide the best catalogue/metadata URL
- distinguish fully digitised / partially digitised / catalogue-only
- distinguish catalogue fact from scholarly inference
- record languages
- record whether illustrations or diagrams are present if documented
- note relevant named scribes, owners, physicians, students, clerics,
  apothecaries or institutions where documented
- record uncertainty explicitly

Do not treat modern location as medieval provenance.
Do not infer contents from a manuscript title alone.
Do not merge distinct shelfmarks.
Deduplicate mirrors of the same manuscript.
Do not claim that a manuscript resembles the Voynich Manuscript.
Do not search for "Voynich-like" manuscripts: this is an independent corpus
construction exercise.

After building the corpus, actively search for missing classes and geographic
gaps. Continue searching until additional search strategies produce mostly
duplicates or no new qualifying manuscripts.

Finally report:
1. the complete candidate corpus
2. the strict subset containing 3+ content categories
3. geographical and chronological coverage gaps
4. rejected near-misses and the reason each failed
5. search strategies/databases that yielded no qualifying material
6. an assessment of how close the search came to exhaustion.
"""

_NS = ["string", "null"]
schema = {
    "type": "object",
    "properties": {
        "manuscripts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "repository": {"type": _NS},
                    "shelfmark": {"type": "string"},
                    "title": {"type": _NS},
                    "date": {"type": _NS},
                    "date_evidence": {"type": _NS},
                    "origin": {"type": _NS},
                    "pre1455_provenance": {"type": _NS},
                    "geographic_basis": {"type": "string"},
                    "languages": {"type": "array", "items": {"type": "string"}},
                    "content_categories": {"type": "array", "items": {"type": "string"}},
                    "content_evidence": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "category": {"type": "string"},
                                "evidence": {"type": "string"},
                                "source_url": {"type": "string"},
                            },
                            "required": ["category", "evidence", "source_url"],
                        },
                    },
                    "illustrations_or_diagrams": {"type": _NS},
                    "named_people_or_institutions": {"type": "array", "items": {"type": "string"}},
                    "digitisation_status": {"type": "string"},
                    "digitisation_url": {"type": _NS},
                    "catalogue_url": {"type": _NS},
                    "uncertainties": {"type": "array", "items": {"type": "string"}},
                },
                "required": [
                    "repository", "shelfmark", "title", "date", "date_evidence",
                    "origin", "pre1455_provenance", "geographic_basis", "languages",
                    "content_categories", "content_evidence", "illustrations_or_diagrams",
                    "named_people_or_institutions", "digitisation_status",
                    "digitisation_url", "catalogue_url", "uncertainties",
                ],
            },
        },
        "strict_three_plus_subset": {"type": "array", "items": {"type": "string"}},
        "rejected_near_misses": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "manuscript": {"type": "string"},
                    "reason_rejected": {"type": "string"},
                    "source_url": {"type": _NS},
                },
                "required": ["manuscript", "reason_rejected", "source_url"],
            },
        },
        "coverage_gaps": {"type": "array", "items": {"type": "string"}},
        "unsuccessful_search_areas": {"type": "array", "items": {"type": "string"}},
        "exhaustion_assessment": {"type": "string"},
    },
    "required": [
        "manuscripts", "strict_three_plus_subset", "rejected_near_misses",
        "coverage_gaps", "unsuccessful_search_areas", "exhaustion_assessment",
    ],
}

if __name__ == "__main__":
    stream = client.responses.create(
        model="agent",
        input=QUERY,
        stream=True,
        reasoning={"effort": "ultra"},
        text={"format": {"type": "json_schema", "name": "upper_rhine_manuscript_corpus", "schema": schema}},
    )
    for event in stream:
        if event.type == "response.created":
            print(f"Started response: {event.response.id}", file=__import__("sys").stderr)
        elif event.type == "response.completed":
            print(event.response.output_text)
