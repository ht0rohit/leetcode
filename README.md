# LeetCode Submissions Extractor

Extract all your accepted LeetCode submissions locally and save them organized by problem.

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

The script creates a `submissions/` directory with:
- **Subdirectories** for each problem (by slug, e.g., `two_sum/`, `longest_substring/`)
- **solution.<ext>** file containing your accepted code
- **metadata.json** with problem info, timestamps, runtime, and memory stats

Example structure:
```
submissions/
├── two_sum/
│   └── solution.py
├── longest_substring_without_repeating_characters/
│   └── solution.py
└── metadata.json
```

## Security

- Never commit your session token or CSRF token
- Credentials are passed via environment variables, not stored in files
- `submissions/` is gitignored and won't be committed
