# Programme-local remote compute protocol

This protocol is mandatory for every remotely billed CPU or GPU job in the direct `d=1` programme. It supplements repository PR #40.

## Before launch

1. State the exact gate and decision the job can change.
2. Run the cheapest local or GitHub Actions smoke test first.
3. Freeze the command, input commit, expected output marker and cancellation condition.
4. Choose the cheapest adequate hardware.
5. Permit at most one paid job for the live gate.
6. Set both:
   - provider timeout;
   - shorter in-container `timeout` or equivalent.

Default ceilings:

- smoke: 10 minutes;
- ordinary exact audit: 30 minutes;
- heavy algebra: 60 minutes;
- exceptional hard maximum: 120 minutes.

No job may exceed 120 minutes without an explicit new user instruction.

## At launch

Immediately record:

- provider;
- job ID;
- start time;
- hardware/flavour;
- gate;
- expected marker;
- provider timeout;
- in-container timeout;
- cancellation condition.

## While running

- Inspect status and logs at least once within the first 10 minutes.
- Cancel after 10 minutes without meaningful progress or a changing diagnostic.
- Cancel immediately if:
  - the mathematical premise is invalidated;
  - a cheaper discriminator answers the gate;
  - another job makes it redundant;
  - the job is using the wrong commit, model or input;
  - the response is otherwise ready;
  - output is not being persisted and cannot affect the gate.
- Do not launch speculative parallel jobs merely to occupy compute.

## After completion or cancellation

1. Confirm terminal provider status.
2. Save the decisive output, hashes and logs needed for audit.
3. Remove the job from the live ledger.
4. Check the provider job list again.

## End-of-turn invariant

A final response after remote compute is prohibited until the provider list has been checked and every current-turn job is terminal.

The final operational marker is:

```text
RUNNING_REMOTE_JOBS=0
```

If the provider cannot confirm terminal status, report the uncertainty and do not describe the compute phase as complete.

## Research discipline

Remote compute may:

- verify an exact proposed identity;
- calculate a preregistered invariant;
- falsify a defined route;
- produce a machine certificate.

Remote compute may not:

- replace an all-primes theorem with a larger finite panel;
- turn first-trace agreement into an object identity;
- reopen a closed route without a new mathematical ingredient;
- continue after the relevant decision has already been made.
