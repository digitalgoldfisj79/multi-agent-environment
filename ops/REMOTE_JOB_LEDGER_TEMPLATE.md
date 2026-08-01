# Remote Job Ledger

Use one row per remotely billed job. Complete the terminal-state and cancellation fields before reporting the research result.

| Job ID | Purpose | Flavour | Provider timeout | Internal timeout | Expected marker | Cancellation condition | Final state | Cancelled? | Final inspection time |
|---|---|---|---:|---:|---|---|---|---|---|
| | | | | | | | | | |

## End-of-turn sweep

```text
job_list_checked_at=
running_jobs_before_cleanup=
jobs_cancelled=
running_jobs_after_cleanup=
RUNNING_REMOTE_JOBS=0
```

## Certification

- [ ] Every job started in this turn appears above.
- [ ] Every listed job has a terminal state.
- [ ] Every cancellation has been inspected and confirmed.
- [ ] The final provider job list contains no current-turn running jobs.
