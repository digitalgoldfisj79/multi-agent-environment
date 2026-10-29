"""The runbook: the reviewed, structured hand-off between the video and the agent.

A runbook describes *what* to do in terms a person can check (labels, intent,
expected result), never screen coordinates, because the agent's screen will not
match the recording's resolution or layout.
"""

import re

ACTION_TYPES = [
    "navigate", "click", "double_click", "right_click", "type", "key",
    "select", "scroll", "drag", "wait", "verify", "other",
]

RUNBOOK_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "goal": {"type": "string"},
        "applications": {"type": "array", "items": {"type": "string"}},
        "preconditions": {"type": "array", "items": {"type": "string"}},
        "parameters": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "example_from_video": {"type": "string"},
                    "sensitive": {"type": "boolean"},
                },
                "required": ["name", "description", "example_from_video", "sensitive"],
                "additionalProperties": False,
            },
        },
        "steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "intent": {"type": "string"},
                    "action_type": {"type": "string", "enum": ACTION_TYPES},
                    "target": {"type": "string"},
                    "value": {"type": "string"},
                    "expected_result": {"type": "string"},
                    "evidence_t": {"type": "number"},
                    "requires_confirmation": {"type": "boolean"},
                    "uncertainty": {"type": "string"},
                },
                "required": [
                    "id", "intent", "action_type", "target", "value",
                    "expected_result", "evidence_t", "requires_confirmation", "uncertainty",
                ],
                "additionalProperties": False,
            },
        },
        "success_criteria": {"type": "array", "items": {"type": "string"}},
        "open_questions": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "title", "goal", "applications", "preconditions", "parameters",
        "steps", "success_criteria", "open_questions",
    ],
    "additionalProperties": False,
}


def validate(rb: dict) -> list[str]:
    """Checks the schema cannot express. Returns a list of problems (empty = OK)."""
    problems = []
    ids = [s["id"] for s in rb["steps"]]
    if ids != list(range(1, len(ids) + 1)):
        problems.append(f"step ids must be 1..N in order, got {ids}")
    names = {p["name"] for p in rb["parameters"]}
    for s in rb["steps"]:
        for ref in _param_refs(s["value"]) | _param_refs(s["target"]):
            if ref not in names:
                problems.append(f"step {s['id']} references undefined parameter {{{{{ref}}}}}")
    for p in rb["parameters"]:
        if p["sensitive"] and p["example_from_video"]:
            problems.append(f"sensitive parameter {p['name']} must not carry a value from the video")
    return problems


def _param_refs(text: str) -> set[str]:
    return set(re.findall(r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}", text))


def unresolved_params(rb: dict, values: dict) -> list[str]:
    return sorted({p["name"] for p in rb["parameters"]} - set(values))


def to_markdown(rb: dict) -> str:
    out = [f"# {rb['title']}", "", f"**Goal:** {rb['goal']}", ""]
    if rb["applications"]:
        out += ["**Applications:** " + ", ".join(rb["applications"]), ""]
    if rb["preconditions"]:
        out += ["## Preconditions", *[f"- {p}" for p in rb["preconditions"]], ""]
    if rb["parameters"]:
        out += ["## Parameters", "", "| Name | Description | Example from video | Sensitive |", "|---|---|---|---|"]
        out += [
            f"| `{p['name']}` | {p['description']} | {p['example_from_video'] or '—'} | {'yes' if p['sensitive'] else ''} |"
            for p in rb["parameters"]
        ]
        out.append("")
    out += ["## Steps", "", "| # | t (s) | Action | Target | Value | Expected result | Confirm | Uncertainty |",
            "|---|---|---|---|---|---|---|---|"]
    for s in rb["steps"]:
        out.append(
            f"| {s['id']} | {s['evidence_t']:.1f} | {s['action_type']} | {s['target']} | {s['value'] or ''} | "
            f"{s['expected_result']} | {'**yes**' if s['requires_confirmation'] else ''} | {s['uncertainty']} |"
        )
    out.append("")
    if rb["success_criteria"]:
        out += ["## Success criteria", *[f"- {c}" for c in rb["success_criteria"]], ""]
    if rb["open_questions"]:
        out += ["## Open questions for the reviewer", *[f"- {q}" for q in rb["open_questions"]], ""]
    return "\n".join(out)
