#!/usr/bin/env python3
from urllib.request import urlopen
from vllm import LLM, SamplingParams

BASE = (
    "https://raw.githubusercontent.com/digitalgoldfisj79/"
    "multi-agent-environment/a4df5de73e31da334431fa327c23655914db1883/"
    "frontier/integer_source_frame_bridge/"
)
prompt = urlopen(BASE + "HOSTILE_REVIEW_PROMPT_COMPLETE_FRAME_AND_PAIR4_20260728.md").read().decode()
note1 = urlopen(BASE + "COMPLETE_PRIME_MODULUS_FRAME_20260728.md").read().decode()
note2 = urlopen(BASE + "PRIMORIAL_PAIR_OF_PAIRS_SINGULAR_SERIES_AVERAGE_20260728.md").read().decode()
messages = [
    {
        "role": "system",
        "content": (
            "You are a hostile independent mathematical referee. Check every finite "
            "identity, asymptotic estimate, normalisation, endpoint and implication. "
            "Quote exact text for every adverse finding. Distinguish genuine errors "
            "from requests for exposition."
        ),
    },
    {
        "role": "user",
        "content": prompt + "\n\n# NOTE 1\n\n" + note1 + "\n\n# NOTE 2\n\n" + note2,
    },
]
llm = LLM(
    model="Qwen/Qwen3-14B-AWQ",
    quantization="awq",
    max_model_len=32768,
    gpu_memory_utilization=0.94,
)
params = SamplingParams(temperature=0.01, top_p=0.9, max_tokens=9000)
out = llm.chat(messages, params, chat_template_kwargs={"enable_thinking": False})
print("\n===BEGIN_REVIEW===\n")
print(out[0].outputs[0].text)
print("\n===END_REVIEW===\n")
