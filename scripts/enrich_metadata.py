#!/usr/bin/env python3
"""Generate per-problem metadata.yaml baseline records from submissions/metadata.json.

Pattern/topic tags here are heuristic guesses derived from keywords in the
final accepted solution's code. They are a first pass for triage, not a
verified classification -- review and correct them as you revisit problems.
Historical reasoning fields are left UNKNOWN per policy: an accepted final
solution cannot tell us the approach path, failed attempts, or hints used.
"""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SUBMISSIONS = ROOT / "submissions"
META_JSON = SUBMISSIONS / "metadata.json"

# (pattern label, regex) -- order matters, first match(es) win, checked independently
PATTERN_RULES = [
    ("Dynamic Programming", r"\blru_cache\b|\bmemo\b|\bdp\s*=|\bdp\[\d*\]\[?"),
    ("Backtracking", r"\bdef backtrack|\bbacktrack\("),
    ("Union-Find", r"\bfind\(.*\).*\bunion\(|\bparent\[|\bunion_find\b|\bDSU\b"),
    ("Trie", r"\bTrie\b|\bis_end\b|\bisEnd\b"),
    ("Heap / Priority Queue", r"\bheapq\b|\bheappush\b|\bheappop\b"),
    ("Binary Search", r"\bbisect\b|\bwhile\s+lo\s*<=?\s*hi\b|\bwhile\s+left\s*<=?\s*right\b.*mid"),
    ("BFS / Graph Traversal", r"\bdeque\(\)|\bfrom collections import deque\b"),
    ("DFS / Graph Traversal", r"\bdef dfs\b|\bdfs\("),
    ("Two Pointers", r"\bleft\s*,\s*right\s*=\s*0\s*,|\bleft\s*=\s*0\b.*\bright\s*="),
    ("Sliding Window", r"\bwindow\b"),
    ("Linked List", r"\bListNode\b"),
    ("Tree / Binary Tree", r"\bTreeNode\b"),
    ("Graph", r"\badj\b|\badjacency\b|\bgraph\s*=\s*(defaultdict|\{|\[)"),
    ("Stack", r"\bstack\s*=\s*\[\]"),
    ("Hash Map / Set", r"\bdefaultdict\b|\bCounter\(|\bset\(\)|\{\}\s*#|\bdict\(\)"),
    ("Greedy", r"\bgreedy\b"),
    ("Bit Manipulation", r"\bxor\b|\b<<\b.*\b>>\b|\bbin\("),
]


def guess_patterns(code: str) -> list[str]:
    hits = []
    for label, pattern in PATTERN_RULES:
        if re.search(pattern, code, re.IGNORECASE):
            hits.append(label)
    return hits or ["UNKNOWN"]


def main() -> None:
    entries = json.loads(META_JSON.read_text())
    written = 0
    for entry in entries:
        slug_dir = SUBMISSIONS / entry["slug"].replace("-", "_")
        sol = slug_dir / "solution.py"
        if not sol.exists():
            print(f"WARN: no solution file for {entry['slug']} at {sol}")
            continue

        code = sol.read_text()
        patterns = guess_patterns(code)

        attempts_file = slug_dir / "attempts.json"
        if attempts_file.exists():
            attempts = json.loads(attempts_file.read_text())
            # Real recorded outcomes from LeetCode, not inferred: safe to use.
            debugging_history = [
                {"timestamp": a["timestamp"], "status": a["status"]} for a in attempts
            ]
        else:
            debugging_history = "UNKNOWN"

        record = {
            "id": entry["id"],
            "title": entry["title"],
            "slug": entry["slug"],
            "url": f"https://leetcode.com/problems/{entry['slug']}/",
            "difficulty": entry.get("difficulty", "UNKNOWN"),
            "topics": ["UNKNOWN"],
            "solution_language": "Python",
            "pattern": patterns,
            "pattern_source": "heuristic-from-code (unverified, review before trusting)",
            "time_complexity": "UNKNOWN",
            "space_complexity": "UNKNOWN",
            "status": "solved",
            "date_solved": entry.get("timestamp", "UNKNOWN"),
            "runtime": entry.get("runtime", "UNKNOWN"),
            "memory": entry.get("memory", "UNKNOWN"),
            "initial_approach": "UNKNOWN",
            "historical_mistakes": "UNKNOWN",
            "debugging_history": debugging_history,
            "hints_used": "UNKNOWN",
        }

        out = slug_dir / "metadata.yaml"
        out.write_text(yaml.dump(record, sort_keys=False, allow_unicode=True))
        written += 1

    print(f"Wrote {written} metadata.yaml files")


if __name__ == "__main__":
    main()
