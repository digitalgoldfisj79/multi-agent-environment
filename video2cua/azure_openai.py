"""OpenAI client for models deployed in Microsoft Foundry (Azure OpenAI v1 API).

Auth: set AZURE_OPENAI_ENDPOINT (https://<resource>.openai.azure.com) or
AZURE_OPENAI_BASE_URL (full .../openai/v1/ URL), plus either AZURE_OPENAI_API_KEY,
or nothing else to use Entra ID via DefaultAzureCredential.
"""

import os

from openai import OpenAI

# Both stages default to GPT-6.1 Terra: image input, structured outputs, and the
# GA `computer` tool. Override if your deployments are named differently.
SYNTH_DEPLOYMENT = os.environ.get("V2C_OPENAI_SYNTH_DEPLOYMENT", "gpt-6.1-terra")
AGENT_DEPLOYMENT = os.environ.get("V2C_OPENAI_AGENT_DEPLOYMENT", "gpt-6.1-terra")


def make_client() -> OpenAI:
    base_url = os.environ.get("AZURE_OPENAI_BASE_URL") or (
        os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/") + "/openai/v1/"
    )
    api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    if not api_key:
        from azure.identity import DefaultAzureCredential, get_bearer_token_provider

        api_key = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
    # Synthesis over dozens of high-detail frames can take several minutes.
    return OpenAI(base_url=base_url, api_key=api_key, timeout=900)
