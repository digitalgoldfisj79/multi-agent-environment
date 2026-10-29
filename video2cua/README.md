# video2cua: screen recordings → runbooks → computer-use agent (Microsoft Foundry)

Colleagues record themselves doing a task (MP4, ideally narrated). This pipeline turns
the recording into a **runbook**, a person reviews and approves it, and a **computer-use
agent** follows it inside an isolated sandbox. The default model for both the runbook and
the agent is **GPT-6.1 Terra** on Foundry; Claude on Foundry is available with `--backend claude`.

```
MP4 ──► 1 extract ──► 2 transcribe ──► 3 synthesize ──► runbook.json/.md ──► human review ──► 4 execute
        ffmpeg key      Teams VTT or      GPT-6.1 Terra      (approved: true)                 GPT-6.1 Terra
        frames + audio  Whisper on        (Responses API,                                     + `computer` tool
                        Foundry           structured output)                                  in a sandbox VM/container
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

| Piece | Default (`--backend openai`) | `--backend claude` |
|---|---|---|
| Runbook model | Foundry deployment `gpt-6.1-terra`, Responses API, `text.format` json_schema (strict) | `claude-opus-5-5`, Messages API, `output_config.format` |
| Agent model | `gpt-6.1-terra` with the GA `{"type": "computer"}` tool: batched `actions`, screenshot replies, `pending_safety_checks` | `claude-opus-5` with the beta `computer_20251124` tool (the only Claude computer use on Foundry; the 5.5 models reject it there) |
| Client | `openai` SDK against `https://<resource>.openai.azure.com/openai/v1/` | `anthropic` SDK `AnthropicFoundry` |
| Refusal handling | Refusal content part → run stops as `failed` | Client-side `BetaRefusalFallbackMiddleware` → `claude-opus-4-8` (`V2C_FALLBACK_DEPLOYMENT=""` turns it off) |

Shared by both: narration from a Teams/Stream `.vtt` file or a Whisper deployment in the
same Foundry resource; video intake via Blob Storage + Event Grid → a Container Apps job
running `analyze` (not included; the CLI is the job body); and a sandbox — Container Apps /
AKS pod for browser apps, an Azure VM or Azure Virtual Desktop session for desktop apps —
with no production credentials beyond what the task needs and an egress allow-list.

Neither model takes video: Terra's catalog entry lists text and image input, so stage 1's
frame extraction is needed either way.

### Setup (GPT-6.1 Terra)

1. In the Foundry portal, deploy `gpt-6.1-terra` (Global Standard, or Data Zone Standard in
   US/EU/APAC). Optionally deploy `whisper`.
2. Give the job's managed identity a role that can call the deployment (or use the key).
3. Environment:

   ```bash
   export AZURE_OPENAI_ENDPOINT=https://my-foundry-resource.openai.azure.com   # or AZURE_OPENAI_BASE_URL=.../openai/v1/
   export AZURE_OPENAI_API_KEY=...            # omit to use Entra ID (DefaultAzureCredential)
   # optional overrides if your deployment names differ:
   export V2C_OPENAI_SYNTH_DEPLOYMENT=gpt-6.1-terra V2C_OPENAI_AGENT_DEPLOYMENT=gpt-6.1-terra
   export AZURE_WHISPER_DEPLOYMENT=whisper    # optional narration
   pip install -r requirements.txt
   ```

For the Claude backend, deploy `claude-opus-5-5`, `claude-opus-5` and `claude-opus-4-8`
(Hosted on Azure) and set `ANTHROPIC_FOUNDRY_RESOURCE` + `ANTHROPIC_FOUNDRY_API_KEY`
(or Entra ID); deployment overrides are `V2C_SYNTH_DEPLOYMENT`, `V2C_AGENT_DEPLOYMENT`,
`V2C_FALLBACK_DEPLOYMENT`.

### Use

```bash
# 1-3: recording -> runbook (resumable: each stage writes a checkpoint in --work)
python -m video2cua.cli analyze demo.mp4 --work work/demo --vtt demo.vtt \
    --notes "SAP Fiori invoice approval, EU tenant"

# review work/demo/runbook.md; fix runbook.json if needed; then set "_meta": {"approved": true}

# 4: follow it in a sandboxed browser (asks you before any requires_confirmation step
#    and before acknowledging any Terra safety check)
python -m video2cua.cli run work/demo/runbook.json --param invoice_id=INV-1234 \
    --start-url https://app.example.internal --chromium /path/to/chrome
```

Add `--backend claude` to either command to use Claude instead.

Each run writes `run_<timestamp>/log.jsonl` (every action, reasoning summary,
confirmation and safety-check decision) and every screenshot, for audit.

The Terra loop chains turns with `previous_response_id`, so responses are stored by the
service; check your data-retention requirements for colleague screen content.

## Files

| File | Stage |
|---|---|
| `extract.py` | ffmpeg samples frames at 2 fps; keeps frames where ≥2 32-px tiles changed at up to 1280-px width; caps at 60, dropping the smallest changes first |
| `transcribe.py` | WebVTT parser, or Whisper via Azure OpenAI |
| `synthesize.py` | Interleaves `[t=…] narration` + frame, asks the model for a runbook against `runbook.RUNBOOK_SCHEMA` (Terra or Claude) |
| `runbook.py` | Schema, extra validation (parameter references, secrets), Markdown rendering |
| `computer.py` | `Computer` interface + `PlaywrightComputer` (browser). Write an xdotool or Windows implementation for desktop apps. |
| `execute.py` | Shared agent pieces (system prompt, `report_step` / `request_confirmation` / `type_secret` / `finish`, `Session`) and the Claude loop |
| `execute_openai.py` | The Terra loop: `computer` tool, batched actions, safety-check acknowledgement, function tools |
| `azure_openai.py` / `foundry.py` | Clients for Terra (Azure OpenAI v1) / Claude (Foundry) |

## Known limits

- **Frame sampling misses fast actions.** At 2 fps, a click that opens and closes a menu
  within 0.5 s can be lost. Raise `--fps` for fast demonstrators.
- **Typing is sampled, not keylogged.** Characters are seen in batches as tiles change;
  the final value is usually visible in the next kept frame, but check parameters in review.
- **Long videos.** Default cap is 60 frames per runbook. Split long recordings into one task each.
- **Desktop apps** need your own `Computer` implementation and a VM; only the browser one is included.
- **Prompt injection.** The agent reads whatever is on screen. Keep it in a sandbox with an
  egress allow-list and least-privilege accounts, and keep confirmation on for state-changing steps.

## Tests

`pytest tests/` runs offline: a synthetic MP4 for extraction, scripted fake models for
synthesis and both agent loops (Terra and Claude), and a real headless Chromium page that
each loop types into and submits.
