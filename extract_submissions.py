#!/usr/bin/env python3
import requests
import json
import os
import sys
from pathlib import Path
from datetime import datetime

# LeetCode API credentials from environment variables
LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
CSRF_TOKEN = os.environ.get("CSRF_TOKEN")

if not LEETCODE_SESSION or not CSRF_TOKEN:
    print("Error: LEETCODE_SESSION and CSRF_TOKEN environment variables must be set")
    sys.exit(1)

# API endpoint
GRAPHQL_URL = "https://leetcode.com/graphql/"

def fetch_submissions():
    """Fetch all accepted submissions from LeetCode."""
    cookies = {"LEETCODE_SESSION": LEETCODE_SESSION}
    headers = {
        "X-CSRFToken": CSRF_TOKEN,
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/submissions/",
    }

    query = """
    query getSubmissions($offset: Int, $limit: Int, $lastKey: String, $representativeId: Int) {
        submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, representativeId: $representativeId) {
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
            "representativeId": None
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
    cookies = {"LEETCODE_SESSION": LEETCODE_SESSION}
    headers = {
        "X-CSRFToken": CSRF_TOKEN,
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/submissions/",
    }

    query = """
    query getSubmission($id: ID!) {
        submission(id: $id) {
            code
            lang
            langName
            timestamp
            statusDisplay
            runtime
            memory
            hasNotes
            notes
            flagType
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

    variables = {"id": submission_id}
    payload = json.dumps({"query": query, "variables": variables})

    try:
        response = requests.post(GRAPHQL_URL, data=payload, headers=headers, cookies=cookies, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "errors" in data:
            print(f"Error fetching submission code: {data['errors']}")
            return None

        return data.get("data", {}).get("submission", {})

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

def save_submissions(submissions):
    """Save accepted submissions to files."""
    # Create submissions directory
    submissions_dir = Path("submissions")
    submissions_dir.mkdir(exist_ok=True)

    accepted_count = 0
    metadata = []

    print("\nProcessing submissions...")

    for i, submission in enumerate(submissions):
        # Only process accepted submissions
        if submission["statusDisplay"] != "Accepted":
            continue

        print(f"\n[{i+1}/{len(submissions)}] Processing {submission['title']} ({submission['titleSlug']})...")

        # Fetch full submission code
        full_submission = fetch_submission_code(submission["id"])

        if not full_submission or not full_submission.get("code"):
            print(f"  Skipped: Could not fetch code")
            continue

        code = full_submission["code"]
        lang = full_submission.get("lang", submission.get("lang", "unknown"))
        ext = get_file_extension(lang)

        # Create problem directory
        problem_name = submission["titleSlug"].replace("-", "_")
        problem_dir = submissions_dir / problem_name
        problem_dir.mkdir(exist_ok=True)

        # Save code file
        code_file = problem_dir / f"solution.{ext}"
        code_file.write_text(code)

        # Save metadata
        timestamp = datetime.fromtimestamp(submission["timestamp"]).isoformat()
        metadata_entry = {
            "id": submission["id"],
            "title": submission["title"],
            "slug": submission["titleSlug"],
            "lang": lang,
            "timestamp": timestamp,
            "runtime": submission.get("runtime"),
            "memory": submission.get("memory"),
        }

        if "question" in full_submission:
            q = full_submission["question"]
            metadata_entry.update({
                "difficulty": q.get("difficulty"),
                "category": q.get("categoryTitle"),
            })

        metadata.append(metadata_entry)

        print(f"  ✓ Saved to {code_file}")
        accepted_count += 1

    # Save metadata JSON
    metadata_file = submissions_dir / "metadata.json"
    metadata_file.write_text(json.dumps(metadata, indent=2))

    print(f"\n✓ Successfully extracted {accepted_count} accepted submissions")
    print(f"✓ Saved to {submissions_dir}/ directory")

    return accepted_count

if __name__ == "__main__":
    submissions = fetch_submissions()

    if submissions:
        count = save_submissions(submissions)
    else:
        print("No submissions found or error occurred during fetch.")
