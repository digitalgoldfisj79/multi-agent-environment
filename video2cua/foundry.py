"""Claude client for Microsoft Foundry.

Auth: set ANTHROPIC_FOUNDRY_RESOURCE (or ANTHROPIC_FOUNDRY_BASE_URL) plus either
ANTHROPIC_FOUNDRY_API_KEY, or nothing else to use Entra ID via DefaultAzureCredential
(managed identity in Azure, `az login` locally).

Deployment names default to the model IDs, which is also Foundry's default when
you deploy a model. Override them if you named your deployments differently.
"""

import os

from anthropic import AnthropicFoundry, BetaRefusalFallbackMiddleware

# Reads the video and writes the runbook. Vision + structured outputs.
SYNTH_DEPLOYMENT = os.environ.get("V2C_SYNTH_DEPLOYMENT", "claude-opus-5-5")
# Drives the computer. Must accept the beta computer_20251124 tool on Foundry:
# Claude Opus 5, Sonnet 5, Opus 4.8 and Fable 5/5.1 do; the 5.5 models do not there.
AGENT_DEPLOYMENT = os.environ.get("V2C_AGENT_DEPLOYMENT", "claude-opus-5")
# Re-serves a request when the main model declines it. Empty string disables.
FALLBACK_DEPLOYMENT = os.environ.get("V2C_FALLBACK_DEPLOYMENT", "claude-opus-4-8")


def make_client() -> AnthropicFoundry:
    kwargs = {}
    if os.environ.get("ANTHROPIC_FOUNDRY_BASE_URL"):
        kwargs["base_url"] = os.environ["ANTHROPIC_FOUNDRY_BASE_URL"]
    else:
        kwargs["resource"] = os.environ["ANTHROPIC_FOUNDRY_RESOURCE"]

    if os.environ.get("ANTHROPIC_FOUNDRY_API_KEY"):
        kwargs["api_key"] = os.environ["ANTHROPIC_FOUNDRY_API_KEY"]
    else:
        from azure.identity import DefaultAzureCredential, get_bearer_token_provider

        kwargs["azure_ad_token_provider"] = get_bearer_token_provider(
            DefaultAzureCredential(), "https://ai.azure.com/.default"
        )

    if FALLBACK_DEPLOYMENT:
        # Foundry has no server-side `fallbacks` parameter; this middleware retries
        # refused client.beta.messages requests on the fallback deployment.
        kwargs["middleware"] = [BetaRefusalFallbackMiddleware([{"model": FALLBACK_DEPLOYMENT}])]
    return AnthropicFoundry(**kwargs)
