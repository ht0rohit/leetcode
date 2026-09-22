#!/usr/bin/env python3
import requests
import json
import os
import sys
import time
from pathlib import Path
from datetime import datetime

def load_dotenv(path=".env"):
    """Load KEY=VALUE pairs from a local .env file into os.environ, if present."""
    env_path = Path(path)
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())

load_dotenv()

# LeetCode API credentials from environment variables (or .env file)
LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
CSRF_TOKEN = os.environ.get("CSRF_TOKEN")

if not LEETCODE_SESSION or not CSRF_TOKEN:
    print("Error: LEETCODE_SESSION and CSRF_TOKEN must be set (env vars, or in a local .env file)")
    sys.exit(1)

# API endpoint
GRAPHQL_URL = "https://leetcode.com/graphql/"

def fetch_submissions():
    """Fetch all accepted submissions from LeetCode."""
    cookies = {"LEETCODE_SESSION": LEETCODE_SESSION, "csrftoken": CSRF_TOKEN}
    headers = {
        "X-CSRFToken": CSRF_TOKEN,
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/submissions/",
        "Origin": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0",
    }

    query = """
    query getSubmissions($offset: Int, $limit: Int, $lastKey: String) {
        submissionList(offset: $offset, limit: $limit, lastKey: $lastKey) {
            submissions {
                id
                statusDisplay
                lang
                runtime
                timestamp
                url
                isPending
                title
                memory
                titleSlug
            }
            lastKey
            hasNext
        }
    }
    """

    all_submissions = []
    offset = 0
    limit = 20
    last_key = None

    print("Fetching submissions from LeetCode...")

    while True:
        variables = {
            "offset": offset,
            "limit": limit,
            "lastKey": last_key,
        }

        payload = json.dumps({"query": query, "variables": variables})

        try:
            response = requests.post(GRAPHQL_URL, data=payload, headers=headers, cookies=cookies, timeout=10)
            response.raise_for_status()

            data = response.json()

            if "errors" in data:
                print(f"Error: {data['errors']}")
                break

            submissions = data.get("data", {}).get("submissionList", {}).get("submissions", [])
            all_submissions.extend(submissions)

            print(f"Fetched {len(submissions)} submissions (total: {len(all_submissions)})")

            has_next = data.get("data", {}).get("submissionList", {}).get("hasNext", False)
            last_key = data.get("data", {}).get("submissionList", {}).get("lastKey")

            if not has_next:
                break

            offset += limit

        except Exception as e:
            print(f"Error fetching submissions: {e}")
            break

    return all_submissions

def fetch_submission_code(submission_id):
    """Fetch the code for a specific submission."""
    cookies = {"LEETCODE_SESSION": LEETCODE_SESSION, "csrftoken": CSRF_TOKEN}
    headers = {
        "X-CSRFToken": CSRF_TOKEN,
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/submissions/",
        "Origin": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0",
    }

    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            timestamp
            statusCode
            runtime
            memory
            notes
            flagType
            lang {
                name
                verboseName
            }
            question {
                questionId
                titleSlug
                title
                difficulty
                categoryTitle
            }
        }
    }
    """

    variables = {"submissionId": int(submission_id)}
    payload = json.dumps({"query": query, "variables": variables})

    for attempt in range(4):
        if attempt:
            time.sleep(2 ** attempt)

        try:
            response = requests.post(GRAPHQL_URL, data=payload, headers=headers, cookies=cookies, timeout=10)
            response.raise_for_status()

            data = response.json()

            if "errors" in data:
                print(f"Error fetching submission code: {data['errors']}")
                continue

            details = data.get("data", {}).get("submissionDetails")
            if details:
                return details

        except Exception as e:
            print(f"Error fetching submission code: {e}")

    return None

def get_file_extension(lang):
    """Map language to file extension."""
    extensions = {
        "python": "py",
        "python3": "py",
        "java": "java",
        "cpp": "cpp",
        "c": "c",
        "csharp": "cs",
        "javascript": "js",
        "typescript": "ts",
        "go": "go",
        "rust": "rs",
        "ruby": "rb",
        "swift": "swift",
        "kotlin": "kt",
        "scala": "scala",
        "php": "php",
        "mysql": "sql",
        "sql": "sql",
        "bash": "sh",
    }
    return extensions.get(lang.lower(), lang.lower())

def status_slug(status_display):
    """Turn a LeetCode status display string into a filename-safe slug."""
    return status_display.strip().lower().replace(" ", "_").replace("/", "_")


def save_submissions(submissions):
    """Save every submission (accepted or not) for every problem to files.

    Layout per problem, under submissions/<slug>/:
      - solution.py           latest ACCEPTED submission (kept for backward
                               compatibility with existing tooling)
      - attempts.json         metadata for every submission on this problem,
                               chronological, oldest first
      - attempts/<ts>_<status>_<id>.<ext>   code for every submission

    Top-level submissions/metadata.json keeps its old shape: one entry per
    problem, its latest accepted submission (backward compatible).
    """
    submissions_dir = Path("submissions")
    submissions_dir.mkdir(exist_ok=True)

    # Migration from the pre-attempts.json layout: an old run already saved
    # each problem's latest accepted solution as solution.py + an entry in
    # top-level metadata.json. Reuse that code instead of re-fetching it from
    # the API; only genuinely new submissions (including past failed
    # attempts, never saved before) need a fresh API call.
    old_metadata_by_slug = {}
    old_metadata_file = submissions_dir / "metadata.json"
    if old_metadata_file.exists():
        for entry in json.loads(old_metadata_file.read_text()):
            old_metadata_by_slug[entry["slug"]] = entry

    # Submissions are returned newest-first; process oldest-first per problem
    # so attempts.json and attempts/ end up in chronological order.
    by_slug = {}
    for submission in submissions:
        by_slug.setdefault(submission["titleSlug"], []).append(submission)
    for slug_submissions in by_slug.values():
        slug_submissions.reverse()

    metadata = []
    total_attempts_saved = 0
    total_problems = 0

    print("\nProcessing submissions...")

    for slug_index, (slug, slug_submissions) in enumerate(by_slug.items(), start=1):
        problem_name = slug.replace("-", "_")
        problem_dir = submissions_dir / problem_name
        attempts_dir = problem_dir / "attempts"

        attempts_file = problem_dir / "attempts.json"
        existing_attempts = []
        existing_ids = set()
        if attempts_file.exists():
            existing_attempts = json.loads(attempts_file.read_text())
            existing_ids = {a["id"] for a in existing_attempts}
        elif slug in old_metadata_by_slug:
            old_entry = old_metadata_by_slug[slug]
            old_solution = problem_dir / f"solution.{get_file_extension(old_entry['lang'])}"
            if old_solution.exists() and any(s["id"] == old_entry["id"] for s in slug_submissions):
                ts_prefix = old_entry["timestamp"].replace(":", "").replace("-", "")
                ext = get_file_extension(old_entry["lang"])
                migrated_file = attempts_dir / f"{ts_prefix}_accepted_{old_entry['id']}.{ext}"
                attempts_dir.mkdir(parents=True, exist_ok=True)
                migrated_file.write_text(old_solution.read_text())
                migrated_entry = {
                    "id": old_entry["id"],
                    "status": "Accepted",
                    "lang": old_entry["lang"],
                    "timestamp": old_entry["timestamp"],
                    "runtime": old_entry.get("runtime"),
                    "memory": old_entry.get("memory"),
                    "difficulty": old_entry.get("difficulty"),
                    "category": old_entry.get("category"),
                    "file": str(migrated_file.relative_to(submissions_dir)),
                }
                existing_attempts = [migrated_entry]
                existing_ids = {old_entry["id"]}

        print(f"\n[{slug_index}/{len(by_slug)}] {slug_submissions[0]['title']} ({slug}): "
              f"{len(slug_submissions)} submission(s)")

        attempts = list(existing_attempts)
        latest_accepted = None

        for submission in slug_submissions:
            sub_id = submission["id"]

            if sub_id in existing_ids:
                # Already fetched in a previous run; reuse recorded metadata.
                entry = next(a for a in existing_attempts if a["id"] == sub_id)
                if entry.get("status") == "Accepted":
                    latest_accepted = entry
                continue

            full_submission = fetch_submission_code(sub_id)
            time.sleep(0.3)

            if not full_submission or not full_submission.get("code"):
                print(f"  Skipped {sub_id}: could not fetch code")
                continue

            code = full_submission["code"]
            lang = full_submission.get("lang", {}).get("name") or submission.get("lang", "unknown")
            ext = get_file_extension(lang)
            status = submission["statusDisplay"]
            timestamp = datetime.fromtimestamp(int(submission["timestamp"])).isoformat()

            attempts_dir.mkdir(parents=True, exist_ok=True)
            ts_prefix = timestamp.replace(":", "").replace("-", "")
            code_file = attempts_dir / f"{ts_prefix}_{status_slug(status)}_{sub_id}.{ext}"
            code_file.write_text(code)

            entry = {
                "id": sub_id,
                "status": status,
                "lang": lang,
                "timestamp": timestamp,
                "runtime": submission.get("runtime"),
                "memory": submission.get("memory"),
                "file": str(code_file.relative_to(submissions_dir)),
            }

            if "question" in full_submission:
                q = full_submission["question"]
                entry.update({
                    "difficulty": q.get("difficulty"),
                    "category": q.get("categoryTitle"),
                })

            attempts.append(entry)
            total_attempts_saved += 1

            if status == "Accepted":
                latest_accepted = entry

            print(f"  ✓ [{status}] saved to {code_file}")

        # Persist full attempt history for this problem, chronological.
        attempts.sort(key=lambda a: a["timestamp"])
        problem_dir.mkdir(exist_ok=True)
        attempts_file.write_text(json.dumps(attempts, indent=2))

        # Keep solution.py + top-level metadata.json pointing at the latest
        # accepted submission, for backward compatibility.
        if latest_accepted:
            ext = get_file_extension(latest_accepted["lang"])
            solution_file = problem_dir / f"solution.{ext}"
            accepted_code_file = submissions_dir / latest_accepted["file"]
            solution_file.write_text(accepted_code_file.read_text())

            metadata.append({
                "id": latest_accepted["id"],
                "title": slug_submissions[0]["title"],
                "slug": slug,
                "lang": latest_accepted["lang"],
                "timestamp": latest_accepted["timestamp"],
                "runtime": latest_accepted.get("runtime"),
                "memory": latest_accepted.get("memory"),
                "difficulty": latest_accepted.get("difficulty"),
                "category": latest_accepted.get("category"),
            })
            total_problems += 1

    # Save top-level metadata JSON (accepted-only, one per problem)
    metadata_file = submissions_dir / "metadata.json"
    metadata_file.write_text(json.dumps(metadata, indent=2))

    print(f"\n✓ Saved {total_attempts_saved} new submission(s) across {len(by_slug)} problem(s)")
    print(f"✓ {total_problems} problem(s) have an accepted solution")
    print(f"✓ Saved to {submissions_dir}/ directory")

    return total_problems

if __name__ == "__main__":
    submissions = fetch_submissions()

    if submissions:
        count = save_submissions(submissions)
    else:
        print("No submissions found or error occurred during fetch.")
