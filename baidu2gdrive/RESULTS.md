# baidu2gdrive — running results log

## Retracted findings
(none)

---

## 2026-11-19 — build session 1

### Verified externally (live pages fetched this session)
| Fact | Source | Status |
|---|---|---|
| BaiduPCS-Go latest = v4.0.2, asset `BaiduPCS-Go-v4.0.2-linux-amd64.zip`, sha256 b5f51388…62339 | github.com/qjfoidnh/BaiduPCS-Go/releases | verified (release page) |
| `login -cookies=` / `login -bduss= -stoken=` | README | verified |
| `transfer <link> <code>` saves to the current working dir, and the target cannot be specified | README + transfer.go (`GetActiveUser().Workdir`) | verified |
| `cd` persists Workdir via `pcsconfig.Config.Save()` | cd.go | verified |
| Config dir env var `BAIDUPCS_GO_CONFIG_DIR` | pcsconfig.go + README | verified |
| `download --saveto DIR -p N -l N` | README | verified |
| `--saveto` layout = `SaveTo/PreBase/basename` (PreBase not resolved) | download.go | partial; the code does not depend on it |
| Sidecar/resume-file name during download | not found | unverified; the code does not depend on it |
| Non-SVIP: threads >1 → throttling | README | verified |

### Unverified (could not reach Baidu from the build container)
- `https://pan.baidu.com/api/list` JSON shape (`errno`, `list[].path/isdir/size`), and errno -6 = auth failure.
  This comes from prior knowledge, not tested here. **Highest-risk component.**
- That BaiduPCS-Go's login output does not contain "error/fail/失败/错误" on success.
- End-to-end run against a real share. **Not done.**
- The sha256 is pinned only for amd64. arm64 downloads without a checksum and logs a warning.

### Test results (offline, stubbed)
- 20/20 pytest pass (`python -m pytest -q tests`).
- The tests found a real bug: temp cleanup removed only the file's parent folder, so per-file temp folders and sidecars leaked onto the disk. Fixed by returning the temp root from `download_one` and deleting that.

### Confidence
- Orchestration logic (resume, retries, cleanup, destinations): P(works as designed on first real run) ≈ 80%.
- Full first real run succeeds without any fix: P ≈ 50%. The main risks are the list-API response shape and the login-output check.
