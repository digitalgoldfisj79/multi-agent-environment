# video2cua: screen recordings → runbooks → computer-use agent (Microsoft Foundry)

Colleagues record themselves doing a task (MP4, ideally narrated). This pipeline turns
the recording into a **runbook**, a person reviews and approves it, and a **Claude
computer-use agent** follows it inside an isolated sandbox.

```
MP4 ──► 1 extract ──► 2 transcribe ──► 3 synthesize ──► runbook.json/.md ──► human review ──► 4 execute
        ffmpeg key      Teams VTT or      Claude Opus 5.5    (approved: true)                 Claude Opus 5
        frames + audio  Whisper on        on Foundry,                                         + computer_20251124
                        Foundry           structured output                                   in a sandbox VM/container
```

Why a runbook in the middle instead of "video in, clicks out":

- **Review point.** A wrong step is far cheaper to catch in a table than in a live system.
- **Different screens.** Steps name targets by label and context, never pixel coordinates,
  so they survive a different resolution, theme or window layout.
- **Reuse.** Values typed in the demo become parameters (`{{invoice_id}}`), so one
  recording becomes a reusable procedure.
- **Secrets stay out.** Passwords seen in a demo are never transcribed; the agent types
  them through a `type_secret` tool whose value it never sees.

## What runs where in Azure

| Piece | Foundry / Azure service | Notes |
|---|---|---|
| Synthesis model | Foundry deployment `claude-opus-5-5` (Hosted on Azure) | Vision + structured outputs. Claude takes images, not video, so we send key frames. |
| Agent model | Foundry deployment `claude-opus-5` (Hosted on Azure) | On Foundry, Claude computer use is only the **beta `computer_20251124`** tool. Opus 5.5 / Sonnet 5.5 / Haiku 5.5 reject it on Foundry; Opus 5, Sonnet 5, Opus 4.8 accept it. |
| Refusal fallback | Foundry deployment `claude-opus-4-8` | Client-side `BetaRefusalFallbackMiddleware` (Foundry has no server-side `fallbacks`). Set `V2C_FALLBACK_DEPLOYMENT=""` to turn off. |
| Narration | Teams/Stream `.vtt` file, or a Whisper deployment in the same Foundry resource | Optional. |
| Video intake | Blob Storage container + Event Grid → Container Apps job running `analyze` | Not included here; the CLI is the job body. |
| Sandbox | Azure Container Apps / AKS pod (browser apps) or an Azure VM / Azure Virtual Desktop session (desktop apps) | No access to production credentials or data beyond what the task needs; egress allow-list. |

### Setup

1. In the Foundry portal, create (or reuse) a Foundry resource and deploy
   `claude-opus-5-5`, `claude-opus-5` and `claude-opus-4-8` (Model catalog → Deploy →
   Custom settings → Hosted on Azure). Optionally deploy `whisper`.
2. Give the job's managed identity the **Foundry User** role on the resource (or use the key).
3. Environment:

   ```bash
   export ANTHROPIC_FOUNDRY_RESOURCE=my-foundry-resource      # or ANTHROPIC_FOUNDRY_BASE_URL
   export ANTHROPIC_FOUNDRY_API_KEY=...                        # omit to use Entra ID (DefaultAzureCredential)
   # optional overrides if your deployment names differ:
   export V2C_SYNTH_DEPLOYMENT=claude-opus-5-5 V2C_AGENT_DEPLOYMENT=claude-opus-5 V2C_FALLBACK_DEPLOYMENT=claude-opus-4-8
   # optional Whisper:
   export AZURE_OPENAI_ENDPOINT=https://my-foundry-resource.openai.azure.com AZURE_OPENAI_API_KEY=... AZURE_WHISPER_DEPLOYMENT=whisper
   pip install -r requirements.txt
   ```

### Use

```bash
# 1-3: recording -> runbook (resumable: each stage writes a checkpoint in --work)
python -m video2cua.cli analyze demo.mp4 --work work/demo --vtt demo.vtt \
    --notes "SAP Fiori invoice approval, EU tenant"

# review work/demo/runbook.md; fix runbook.json if needed; then set "_meta": {"approved": true}

# 4: follow it in a sandboxed browser (asks you before any requires_confirmation step)
python -m video2cua.cli run work/demo/runbook.json --param invoice_id=INV-1234 \
    --start-url https://app.example.internal --chromium /path/to/chrome
```

Each run writes `run_<timestamp>/log.jsonl` (every action, thinking summary,
confirmation decision) and every screenshot, for audit.

## Files

| File | Stage |
|---|---|
| `extract.py` | ffmpeg samples frames at 2 fps; keeps frames where ≥2 32-px tiles changed at up to 1280-px width; caps at 60, dropping the smallest changes first |
| `transcribe.py` | WebVTT parser, or Whisper via Azure OpenAI |
| `synthesize.py` | Interleaves `[t=…] narration` + frame, asks Claude for a runbook against `runbook.RUNBOOK_SCHEMA` |
| `runbook.py` | Schema, extra validation (parameter references, secrets), Markdown rendering |
| `computer.py` | `Computer` interface + `PlaywrightComputer` (browser). Write an xdotool or Windows implementation for desktop apps. |
| `execute.py` | The computer-use loop: `computer_20251124` + `report_step`, `request_confirmation`, `type_secret`, `finish` |

## Known limits

- **Frame sampling misses fast actions.** At 2 fps, a click that opens and closes a menu
  within 0.5 s can be lost. Raise `--fps` for fast demonstrators.
- **Typing is sampled, not keylogged.** Characters are seen in batches as tiles change;
  the final value is usually visible in the next kept frame, but check parameters in review.
- **Long videos.** Default cap is 60 frames per runbook. Split long recordings into one task each.
- **Desktop apps** need your own `Computer` implementation and a VM; only the browser one is included.
- **Prompt injection.** The agent reads whatever is on screen. Keep it in a sandbox with an
  egress allow-list and least-privilege accounts, and keep confirmation on for state-changing steps.

## Alternative: OpenAI computer-use model in Foundry Agent Service

Foundry Agent Service has its own Computer Use tool (preview) backed by the
`computer-use-preview` model, which needs a registration/approval form. The same split
applies: this repo's stages 1–3 produce the runbook, and the runbook becomes that agent's
instructions. The executor loop would need rewriting for the Responses API.

## Tests

`pytest tests/` runs offline: a synthetic MP4 for extraction, scripted fake models for
synthesis and the agent loop, and a real headless Chromium page that the loop types into
and submits.
