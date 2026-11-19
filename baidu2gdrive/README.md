# baidu2gdrive

Copy a Baidu Pan (百度网盘) share link straight into Google Drive, **one file at
a time**, on a machine that isn't yours (Google Colab). Multi-GB shares never
touch your computer, and the machine doing the work only needs room for the
biggest single file.

```
share link ──transfer──▶ your Baidu Pan /b2g_staging/<id>
                              │ list (JSON API)
                              ▼  for each file:
                 BaiduPCS-Go download ─▶ size check ─▶ move to Drive ─▶ save progress ─▶ delete temp
```

## Easiest: Google Colab (no install)

1. Open `baidu2gdrive_colab.ipynb` in Colab (File → Upload notebook).
2. Get your cookies: log in at pan.baidu.com in Chrome → F12 → Application →
   Cookies → `https://pan.baidu.com` → copy **BDUSS** and **STOKEN**.
   (STOKEN is not the same as `bdstoken`.) You can put them in Colab Secrets as
   `BAIDU_BDUSS` / `BAIDU_STOKEN` so you don't have to paste them each time.
3. Fill in the share link, extraction code and Drive folder, then run every cell.
4. If Colab disconnects, run all the cells again. Finished files are skipped,
   because progress is saved at `My Drive/.baidu2gdrive_state/<id>.json`.

## Command line (VPS or any Linux box)

```bash
pip install requests
export BAIDU_BDUSS='...'  BAIDU_STOKEN='...'      # or BAIDU_COOKIES='full cookie string'

# Destination can be an rclone remote (run `rclone config` once to set up "gdrive")
python3 baidu2gdrive.py "https://pan.baidu.com/s/1XXXX?pwd=abcd" gdrive:Baidu --install-pcs

# ...or any local/mounted folder
python3 baidu2gdrive.py "https://pan.baidu.com/s/1XXXX" /mnt/gdrive/Baidu --code abcd --install-pcs
```

| Option | Meaning |
|---|---|
| `--code` | 4-character extraction code. You can also use `?pwd=` in the link, or paste the whole "链接… 提取码…" text as the link |
| `--threads N` | Threads per file. **Keep at 1 without SVIP**: the BaiduPCS-Go docs warn that more than 1 gets the account throttled. With SVIP, 10–20 |
| `--dry-run` | Transfer the share and list its files and sizes, but download nothing |
| `--delete-from-baidu` | Delete each file from the Baidu staging folder once it is in Drive (it goes to Baidu's recycle bin) |
| `--state PATH` | Progress file. Re-running with the same state file resumes |
| `--workdir PATH` | Local temp folder. Needs room for the largest file; this is checked before starting |
| `--pcs PATH` / `--install-pcs` | Use your own BaiduPCS-Go, or download the pinned v4.0.2 (sha256-checked, linux-amd64) |

Exit codes: `0` all done · `1` some files failed (re-run to retry) · `2` setup error.

## Things to know

- **Speed without SVIP is the bottleneck.** Baidu throttles non-paying accounts,
  and BaiduPCS-Go says it does not get around this. A multi-GB share can take
  many hours. Colab only removes the load from your own computer and connection;
  it does not make Baidu faster.
- **The share goes into your Baidu Pan first** (`/b2g_staging/<id>`). You need
  enough free Baidu space for it. Delete the folder afterwards, or use
  `--delete-from-baidu`.
- **Colab limits.** Free sessions disconnect when idle and have a maximum
  runtime. The state file on Drive makes re-running safe.
- **Your cookies give full access to your Baidu account.** The script reads them
  from environment variables or Colab Secrets and never writes them to the
  notebook, logs or state file.
- Google Drive has a daily upload limit per account (stated as 750 GB/day; not
  checked in this build).

## Tests

```bash
python -m pytest -q tests      # 20 offline tests; Baidu, BaiduPCS-Go and rclone are stubbed
```

The tests cover link parsing, list pagination, transfer into the staging
folder, per-file download, size check and retry, sidecar/nested-path handling,
temp cleanup, resume, skipping files already in the destination, the rclone
destination, `--delete-from-baidu`, `--dry-run`, and empty-transfer handling.
**They do not exercise real Baidu servers.**

`build_notebook.py` regenerates the Colab notebook after `baidu2gdrive.py` changes.
