# PREREG-8 independent \(F^3\) verification package

This directory preserves the four artifacts supplied after the cross-model
quarantine run.

## Files

- `predict.py`: locks the six \(F^3\) trace predictions from the proposed
  low-rank spectra and checks the five level-one trace anchors.
- `f3_verify.py`: independently measures the six traces with a separate
  finite-field implementation, nine-prime signed CRT reconstruction, and a
  tenth unused coefficient prime as an overdetermination check.
- `f3_predictions.json`, `f3_verify.json`: safe, human-readable transcriptions
  of the two pickle checkpoints.
- `f3_predictions.pkl.b64`, `f3_verify.pkl.b64`: exact base64 encodings of the
  original pickle bytes. Decode with `base64 -d`. Do not load untrusted pickle
  files.
- `PROVENANCE_MANIFEST.json`: SHA-256 hashes and sizes of the original uploads.

The scripts retain their original paths (`checkpoints/...`) to preserve
provenance. To rerun them, place the decoded checkpoints in `checkpoints/`
and provide the pre-existing `trace_separation.pkl` required by `predict.py`.

## Locked result

All five \(s_1\) anchors passed. All six measured \(F^3\) traces matched the
locked predictions exactly. Every tenth-prime check and every internal DFT
anchor passed.
