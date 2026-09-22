# LeetCode Submissions Extractor

Extract the full history of your LeetCode submissions — accepted and failed
(Wrong Answer, TLE, Runtime Error, etc.) — locally, organized by problem.

## Setup

1. **Install dependencies:**
   ```bash
   pip install requests
   ```

2. **Get your LeetCode credentials:**
   - Log into leetcode.com in your browser
   - Open DevTools (F12) → Application/Storage → Cookies → leetcode.com
   - Copy the value of `LEETCODE_SESSION` cookie
   - Copy the value of `csrftoken` cookie

3. **Run the extraction script:**
   ```bash
   LEETCODE_SESSION="<your-session-token>" CSRF_TOKEN="<your-csrf-token>" python3 extract_submissions.py
   ```

## Output

The script creates a `submissions/` directory with, per problem:
- **`solution.<ext>`** — your latest *accepted* code (kept for backward
  compatibility with existing tooling)
- **`attempts.json`** — every submission on that problem, oldest first, with
  status (`Accepted`, `Wrong Answer`, `Time Limit Exceeded`, `Runtime Error`,
  etc.), language, timestamp, runtime, and memory
- **`attempts/`** — the actual code for every submission, one file per
  attempt, named `<timestamp>_<status>_<id>.<ext>`

Plus, at the top level:
- **`metadata.json`** — one entry per problem: its latest accepted
  submission's info (problem, timestamp, runtime, memory stats)

Example structure:
```
submissions/
├── two_sum/
│   ├── solution.py
│   ├── attempts.json
│   └── attempts/
│       ├── 20260101_090000_wrong_answer_1111111111.py
│       └── 20260101_090412_accepted_1111111112.py
├── longest_substring_without_repeating_characters/
│   ├── solution.py
│   ├── attempts.json
│   └── attempts/
│       └── ...
└── metadata.json
```

Re-running the script is safe and incremental: it skips any submission ID
already saved in a problem's `attempts.json`, and (for problems extracted
before this full-history format existed) reuses the already-downloaded
`solution.py` instead of re-fetching it, so only genuinely new submissions
cost an API call.

## Related tooling

- `scripts/enrich_metadata.py` regenerates `submissions/<slug>/metadata.yaml`
  for every problem: heuristic pattern/topic tags from the code, plus (once
  `attempts.json` exists for a problem) an objective `debugging_history` built
  from the real recorded submission outcomes — not inferred, since LeetCode
  actually recorded them. `initial_approach`, `historical_mistakes`, and
  `hints_used` stay `UNKNOWN` for problems solved before this system existed,
  since no submission record captures the reasoning behind them. See
  `CLAUDE.md` for the full coaching workflow for new problems.

## Security

- Never commit your session token or CSRF token
- Credentials are passed via environment variables, or a local `.env` file, which is gitignored and never committed
- Extracted `submissions/` output is tracked in this repository
