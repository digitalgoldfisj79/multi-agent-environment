"""Run an Exa research agent via its OpenAI-compatible Responses API.

Usage:
    export EXA_API_KEY=...
    python exa_agent.py "Find AI infrastructure companies hiring founding designers"
"""
import os
import sys

from openai import OpenAI

DEFAULT_QUERY = "Find AI infrastructure companies hiring founding designers"


def run(query, effort="ultra"):
    client = OpenAI(base_url="https://api.exa.ai", api_key=os.environ["EXA_API_KEY"])
    stream = client.responses.create(
        model="agent",
        input=query,
        stream=True,
        reasoning={"effort": effort},
        text={
            "format": {
                "type": "json_schema",
                "name": "agent_output",
                "schema": {"type": "object"},
            },
        },
    )
    for event in stream:
        if event.type == "response.created":
            print(f"Started response: {event.response.id}", file=sys.stderr)
        elif event.type == "response.completed":
            return event.response.output_text
    return None


if __name__ == "__main__":
    print(run(" ".join(sys.argv[1:]) or DEFAULT_QUERY))
