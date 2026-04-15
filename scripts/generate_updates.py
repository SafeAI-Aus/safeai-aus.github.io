#!/usr/bin/env python3
"""Generate updates.json from git commit history.

Parses the git log for commits that modify Markdown content files
(``docs/**/*.md``, excluding internal directories like ``docs/plans/``
and ``docs/brainstorms/``), and produces a structured JSON changelog
feed at ``site/updates.json``.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tomllib
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import List

# Conventional commit prefix pattern
PREFIX_PATTERN = re.compile(r"^(\w+)(?:\(.+?\))?:\s+(.+)$")

# Prefixes that map to their own type in the feed schema
AGENT_FACING_TYPES = {"docs", "feat", "fix"}

# All recognised conventional commit prefixes (others map to "update")
KNOWN_PREFIXES = {"docs", "feat", "fix", "style", "chore", "refactor", "perf", "test", "ci", "build"}

# Directories under docs/ to exclude (internal working files and legacy paths)
EXCLUDED_DIRS = {"plans", "brainstorms", "templates"}


@dataclass
class ChangeEntry:
    date: str
    commit: str
    type: str
    summary: str
    detail: str = ""
    tags: List[str] = field(default_factory=list)
    files: List[str] = field(default_factory=list)


def check_git_history() -> None:
    """Fail loudly if running in a shallow clone."""
    result = subprocess.run(
        ["git", "rev-parse", "--is-shallow-repository"],
        capture_output=True, text=True, check=True,
    )
    if result.stdout.strip() == "true":
        print(
            "Error: shallow git clone detected. "
            "The updates.json generator requires full history. "
            "Set fetch-depth: 0 in the checkout step.",
            file=sys.stderr,
        )
        sys.exit(1)


def read_site_url() -> str:
    """Read and normalise site_url from zensical.toml."""
    config_path = Path("zensical.toml")
    if not config_path.exists():
        print("Error: zensical.toml not found", file=sys.stderr)
        sys.exit(1)

    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    url = config.get("project", {}).get("site_url", "")
    return url.rstrip("/") + "/"


def get_commit_hashes() -> List[str]:
    """Return commit hashes in reverse chronological order (newest first).

    Uses ``--first-parent`` to follow the main branch lineage without
    descending into merged branches (which would cause duplicates).
    Merge commits are *included* — ``get_changed_md_files`` diffs them
    against their first parent, capturing the combined effect of the merge.
    """
    result = subprocess.run(
        ["git", "log", "--first-parent", "--format=%H"],
        capture_output=True, text=True, check=True,
    )
    return [h for h in result.stdout.strip().splitlines() if h]


def get_commit_info(commit_hash: str) -> tuple[str, str, str]:
    """Return (date, subject, body) for a commit.

    The body is the first paragraph of the commit message after the
    subject line, stripped of blank lines. Used as agent-facing detail
    in the changelog feed. Empty when no body is present.
    """
    # Use %x00 as separator between subject and body to avoid ambiguity
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cd%n%s%x00%b", "--date=short", commit_hash],
        capture_output=True, text=True, check=True,
    )
    output = result.stdout.strip()
    lines = output.split("\n", 1)
    commit_date = lines[0] if lines else ""

    rest = lines[1] if len(lines) > 1 else ""
    # Split on the null byte separator
    parts = rest.split("\x00", 1)
    subject = parts[0].strip() if parts else ""
    raw_body = parts[1].strip() if len(parts) > 1 else ""

    # Extract first paragraph only (up to first blank line)
    detail = ""
    if raw_body:
        first_para_lines = []
        for line in raw_body.splitlines():
            stripped = line.strip()
            # Stop at blank line, Co-Authored-By, or other trailers
            if not stripped or stripped.startswith("Co-Authored-By:"):
                break
            first_para_lines.append(stripped)
        detail = " ".join(first_para_lines)

    return commit_date, subject, detail


def _is_merge_commit(commit_hash: str) -> bool:
    """Check if a commit has more than one parent."""
    result = subprocess.run(
        ["git", "rev-parse", f"{commit_hash}^2"],
        capture_output=True, text=True,
    )
    return result.returncode == 0


def get_changed_md_files(commit_hash: str) -> List[str]:
    """Return list of docs/**/*.md files added or modified in a commit.

    For merge commits, diffs against the first parent to capture the
    combined effect of the merge. Deleted files are excluded so the
    feed does not emit dead URLs.
    """
    # For merge commits, diff against first parent; for regular commits
    # use --root to handle the initial commit
    if _is_merge_commit(commit_hash):
        cmd = ["git", "diff-tree", "--no-commit-id", "--name-only",
               "--diff-filter=d", "-r", f"{commit_hash}^1", commit_hash]
    else:
        cmd = ["git", "diff-tree", "--root", "--no-commit-id", "--name-only",
               "--diff-filter=d", "-r", commit_hash]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    files = []
    for line in result.stdout.strip().splitlines():
        if not line.startswith("docs/") or not line.endswith(".md"):
            continue
        # Exclude internal directories
        parts = line.split("/")
        if len(parts) > 1 and parts[1] in EXCLUDED_DIRS:
            continue
        files.append(line)
    return files


def parse_subject(subject: str) -> tuple[str, str]:
    """Parse a commit subject into (type, summary).

    Recognises conventional commit prefixes like ``docs: summary``.
    Falls back to type ``update`` with the full subject as summary.
    """
    match = PREFIX_PATTERN.match(subject)
    if match:
        prefix = match.group(1).lower()
        summary = match.group(2).strip()
        if prefix in KNOWN_PREFIXES:
            # Only docs, feat, fix are agent-facing types; others → update
            commit_type = prefix if prefix in AGENT_FACING_TYPES else "update"
            return commit_type, summary
    return "update", subject


def derive_tag(file_path: str) -> str:
    """Derive a content-area tag from a file path.

    Strips the ``docs/`` prefix and returns the first directory segment.
    Files directly in ``docs/`` (e.g. index.md, about.md) get the tag
    ``site`` to distinguish them from content-area pages.
    """
    rel = file_path.removeprefix("docs/")
    parts = rel.split("/")
    if len(parts) > 1:
        return parts[0]
    return "site"


def file_to_site_path(file_path: str) -> str:
    """Convert a repo file path to a site-relative URL path.

    ``docs/governance-templates/ai-use-policy.md``
    becomes ``governance-templates/ai-use-policy/``

    ``docs/index.md`` becomes ``/`` (site root).
    """
    rel = file_path.removeprefix("docs/")
    # Remove .md extension and add trailing slash for clean URLs
    if rel.endswith(".md"):
        rel = rel[:-3]
    # index files become the directory path
    if rel.endswith("/index") or rel == "index":
        rel = rel.removesuffix("index")
    else:
        rel += "/"
    # Root index produces empty string — normalise to "/"
    return rel if rel else "/"


def build_entries(commit_hashes: List[str]) -> List[ChangeEntry]:
    """Build changelog entries from commit hashes."""
    entries: List[ChangeEntry] = []

    for full_hash in commit_hashes:
        md_files = get_changed_md_files(full_hash)
        if not md_files:
            continue

        commit_date, subject, detail = get_commit_info(full_hash)
        commit_type, summary = parse_subject(subject)
        short_hash = full_hash[:7]

        # Derive tags from file paths (deduplicated, sorted)
        tags = sorted(set(derive_tag(f) for f in md_files))

        # Convert file paths to site-relative URLs
        site_files = sorted(set(file_to_site_path(f) for f in md_files))

        entries.append(ChangeEntry(
            date=commit_date,
            commit=short_hash,
            type=commit_type,
            summary=summary,
            detail=detail,
            tags=tags,
            files=site_files,
        ))

    return entries


def main() -> int:
    check_git_history()
    site_url = read_site_url()

    commit_hashes = get_commit_hashes()
    entries = build_entries(commit_hashes)

    feed = {
        "schema_version": 1,
        "last_updated": date.today().isoformat(),
        "site_url": site_url.rstrip("/"),
        "related": {
            "llms_txt": f"{site_url}llms.txt",
            "llms_full_txt": f"{site_url}llms-full.txt",
        },
        "entries": [
            {
                "date": e.date,
                "commit": e.commit,
                "type": e.type,
                "summary": e.summary,
                **({"detail": e.detail} if e.detail else {}),
                "tags": e.tags,
                "files": e.files,
            }
            for e in entries
        ],
    }

    output_path = Path("site/updates.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(feed, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Generated {output_path} with {len(entries)} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
