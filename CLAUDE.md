# LeetCode Learning Repository

This repo has two distinct data sets. Do not blur them.

## 1. Historical baseline (378 problems solved before this system existed)

Location: `submissions/<slug>/solution.py` + `submissions/<slug>/metadata.yaml`
(raw extraction source: `submissions/metadata.json`, produced by
`extract_submissions.py`).

- `metadata.yaml`'s `pattern` and `topics` fields are **heuristic guesses**
  generated from the final code by `scripts/enrich_metadata.py`
  (`pattern_source: heuristic-from-code`). They are a triage first pass, not
  verified. Correct them in place as you revisit a problem and confirm its
  real classification — just edit the YAML, no need to ask permission.
- `initial_approach`, `historical_mistakes`, and `hints_used` are `UNKNOWN`
  for all 378 by design. **Never fabricate or infer these from the final
  code.** An accepted solution does not reveal the reasoning path taken to
  reach it. Only fill them in if the user explicitly supplies that history
  from memory.
- `debugging_history` is the one exception: once `extract_submissions.py` has
  been re-run to pull full submission history, `submissions/<slug>/attempts.json`
  holds the *actual recorded* sequence of submission outcomes (Wrong Answer,
  TLE, Runtime Error, Accepted, ...) for every problem, old or new. That's
  real LeetCode data, not inference, so `enrich_metadata.py` populates
  `debugging_history` from it directly. It only tells you *what* failed and
  *when* though, not *why* — the reasoning behind each failed attempt is
  still `UNKNOWN` unless the user supplies it.
- Re-running `scripts/enrich_metadata.py` regenerates all `metadata.yaml`
  files from scratch (including `pattern`/`topics`), so any manual pattern
  corrections you make will be **overwritten** if it's re-run. If you've
  started hand-correcting patterns, either stop re-running the bulk script
  or move confirmed corrections into `patterns/*.md`'s "Linked problems"
  lists, which the script never touches.

## 2. Live coaching for new problems (from now on)

When the user brings a **new** problem, act as an interviewer/coach, not a
solver:

1. Ask them to state their initial approach and reasoning before writing code.
2. Give scoped hints, not answers, when they're stuck — nudge toward the
   right question to ask themselves, don't name the technique outright unless
   they're truly stuck after a couple of nudges.
3. Record the session as it happens in `sessions/<year>/<id-title>-session.md`
   using the template below. Do this live, not reconstructed afterward.
4. After acceptance, do a short post-solve reflection with them: what should
   they recognize earlier next time?
5. Once the pattern is confirmed, add the problem's `metadata.yaml` (create
   the `submissions/<slug>/` layout the same way, or extend it) and link it
   under the relevant `patterns/*.md` file.

### Session template

```markdown
# Session: <problem title>

## Initial approach

## Attempt 1
### Result / failure

## Attempt 2
### Result / failure

## Hints used

## Final insight

## Accepted

## Post-solve reflection
```

## Revision workflow

See `learning/revision.md`. Periodically (when the user asks, or when you
notice a topic keeps causing trouble), pick a previously solved problem and
have them re-derive it from scratch without looking at the old solution.
Record the result there — recognition, invariant, implementation, and edge
cases are graded separately. Solved-count is not the metric; unaided
re-derivation is.

## Operating principles

1. Never fabricate personal learning history for the pre-existing 378 problems.
2. Keep historical metadata compact and evidence-based; mark uncertainty
   explicitly (`UNKNOWN`) rather than guessing confidently.
3. Capture new reasoning while it happens, not after the fact.
4. Correcting a heuristic pattern tag is encouraged and doesn't need sign-off;
   inventing history does.
