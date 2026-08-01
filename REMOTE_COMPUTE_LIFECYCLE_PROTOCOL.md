# Remote Compute Lifecycle Protocol

**Effective:** 1 August 2026  
**Scope:** every remotely billed compute job started for this repository, including Hugging Face Jobs, GPU jobs, scheduled jobs and equivalent external runners.

## Governing rule

A research turn is not complete while a remotely billed job started during that turn is still running.

Before any final report, the operator must either:

1. obtain a terminal state (`COMPLETED`, `FAILED` or `CANCELLED`) for every job started during the turn; or
2. cancel the job explicitly and verify that it is no longer running.

A detached job is a monitoring mechanism, not permission to leave compute running after the interaction ends.

## Mandatory controls

### 1. Two independent time limits

Every job must have both:

- a provider-level timeout; and
- an in-container timeout around the expensive command.

Default ceilings:

| Job class | Provider timeout | In-container command timeout |
|---|---:|---:|
| syntax, unit or smoke check | 10 minutes | 8 minutes |
| ordinary exact audit | 30 minutes | 25 minutes |
| justified heavy computation | 60 minutes | 50 minutes |
| exceptional computation | 120 minutes maximum | 105 minutes maximum |

Anything above 60 minutes requires an explicit written justification in the run ledger before launch. No job may be launched with an open-ended timeout.

### 2. Cost-minimal compute selection

Use the least expensive flavour adequate for the task.

- `cpu-basic` is the default.
- `cpu-performance`, `cpu-xl` or GPU compute requires a stated reason.
- Exploratory or falsification jobs must use a small sentinel first.
- A larger panel may run only after the sentinel succeeds and the result would alter the research decision.

### 3. Immediate registration

Immediately after launch, record:

- job ID;
- purpose;
- compute flavour;
- provider timeout;
- internal timeout;
- expected terminal marker;
- cancellation condition.

No unregistered job may remain active.

### 4. Active monitoring

After launch:

1. inspect the job immediately;
2. read logs after the first meaningful interval;
3. continue checking until terminal state;
4. cancel on any stall, unexpected expansion, repeated dependency installation, missing progress marker or invalidated hypothesis.

A job is presumed stalled when there is no meaningful progress for 10 minutes, unless the command is a known silent algorithm with an independently enforced shorter timeout.

### 5. Cancellation triggers

Cancel immediately when:

- the mathematical premise is corrected or invalidated;
- a cheaper discriminator answers the decision question;
- the job exceeds its preregistered stage budget;
- output is no longer needed for the current theorem gate;
- the user interrupts or redirects the task;
- an equivalent job has already succeeded;
- the job is still running when the response is otherwise ready.

Do not retain a job merely because it might eventually produce additional data.

### 6. End-of-turn zero-job sweep

Before the final response:

1. list all running remote jobs;
2. match them against the current-turn ledger;
3. cancel every current-turn job not already terminal;
4. inspect cancelled jobs until cancellation is confirmed;
5. run the job list again;
6. state the final count of running jobs.

The required final state is:

```text
RUNNING_REMOTE_JOBS=0
```

If unrelated pre-existing jobs are discovered, do not cancel them blindly. Identify them, report them, and obtain user direction unless they were started by the same programme and are demonstrably abandoned.

## Research-report requirements

Every report involving remote compute must state:

- job IDs used;
- terminal status of each relevant job;
- whether any job was cancelled;
- the final running-job count.

A successful mathematical result does not excuse an incomplete compute lifecycle.

## Operational anti-patterns

The following are prohibited:

- launching a detached job and moving on without a terminal-state check;
- using a multi-hour timeout for a task expected to finish in minutes;
- leaving a failed or superseded job running while starting replacements;
- reporting a result from one validator while another redundant validator continues billing;
- assuming provider timeout or shell timeout alone is sufficient;
- ending a response with a job in `RUNNING`, `QUEUED` or unknown state.

## Operator checklist

Before launch:

- [ ] Decision question is explicit.
- [ ] Cheapest adequate flavour selected.
- [ ] Sentinel run considered.
- [ ] Provider timeout set.
- [ ] Internal timeout set.
- [ ] Cancellation condition written.

During run:

- [ ] Job ID registered.
- [ ] Initial inspection completed.
- [ ] Logs checked for meaningful progress.
- [ ] Redundant or invalidated jobs cancelled.

Before final response:

- [ ] Every current-turn job is terminal.
- [ ] `ps`/job-list sweep completed.
- [ ] Running-job count is zero.
- [ ] Job terminal states reported.
