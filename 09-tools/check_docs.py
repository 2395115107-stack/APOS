#!/usr/bin/env python3
"""APOS documentation integrity check.

Checks (Gap 6, enforce invariants mechanically):
1. Required files exist.
2. Backtick path references with a numbered directory prefix resolve.
3. Task entries in 02-product/TASKS.md have the required fields.

Usage: python 09-tools/check_docs.py
Exit code 0 = PASS, 1 = FAIL. Standard library only.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    "APOS.md",
    "APOS-SCHEDULING.md",
    "AGENTS.md",
    "QUICKSTART.md",
    "01-core/AGENTS.md",
    "01-core/MANIFESTO.md",
    "01-core/README.md",
    "02-product/PRODUCT.md",
    "02-product/REQUIREMENTS.md",
    "02-product/ROADMAP.md",
    "02-product/TASKS.md",
    "03-design/DESIGN_SYSTEM.md",
    "04-development/TECH_STACK.md",
    "04-development/AGENT_INTERFACE.md",
    "04-development/PERMISSIONS.md",
    "05-memory/DECISIONS.md",
    "05-memory/LESSONS.md",
    "05-memory/PATTERNS.md",
    "05-memory/EVOLUTION.md",
    "05-memory/RUNS.md",
    "05-memory/EVALS.md",
    "06-references/README.md",
    "07-workflows/README.md",
    "07-workflows/initialize.md",
    "07-workflows/new-feature.md",
    "07-workflows/redesign.md",
    "07-workflows/review.md",
    "07-workflows/hotfix.md",
    "07-workflows/release.md",
    "07-workflows/loop.md",
    "07-workflows/evaluation.md",
    "07-workflows/memory-review.md",
    "08-agents/README.md",
    "08-agents/planner.md",
    "08-agents/architect.md",
    "08-agents/designer.md",
    "08-agents/frontend.md",
    "08-agents/backend.md",
    "08-agents/reviewer.md",
    "08-agents/tester.md",
    "10-reports/README.md",
]

# `dir/...` style references, e.g. `07-workflows/loop.md` or `10-reports/`
REF_RE = re.compile(r"`((?:0\d|10)-[a-z]+/[^`\s]+)`")
# Template placeholders such as `10-reports/{RUN-ID}/review.md` are conventions, not files.
TEMPLATE_HINT_RE = re.compile(r"[{}]")

# Planned paths that do not exist yet; each entry needs a reason.
# Keep this list short: a pending item should eventually become real or be removed.
KNOWN_PENDING = {
    "06-references/design/": "ROADMAP v1.2 计划目录",
    "06-references/products/": "ROADMAP v1.2 计划目录",
    "07-workflows/routing.md": "缺口分析 P2 建议项",
    "07-workflows/evaluator-optimizer.md": "缺口分析 P2 建议项（模式已并入 review.md）",
}

TASK_RE = re.compile(r"^### \[(TODO|IN_PROGRESS|REVIEW|TEST|FIXING|DONE|BLOCKED)\]", re.M)
REQUIRED_TASK_FIELDS = ["Owner", "Next", "Inputs", "Outputs", "Writeback"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def check_required_files() -> list[str]:
    missing = [p for p in REQUIRED_FILES if not (REPO / p).is_file()]
    return [f"missing required file: {p}" for p in missing]


def resolve_reference(ref: str) -> bool:
    """A reference resolves if the file exists, or for `dir/*` shorthands, the directory."""
    if ref.endswith("/*") or ref.endswith("/*.md"):
        return (REPO / ref.split("/*", 1)[0]).is_dir()
    return (REPO / ref).exists()


def check_references() -> list[str]:
    problems: list[str] = []
    pending = [p for p in KNOWN_PENDING if not (REPO / p.rstrip("/")).exists()]
    for md in REPO.rglob("*.md"):
        rel = md.relative_to(REPO).as_posix()
        if rel.startswith("09-tools"):
            continue
        for match in REF_RE.finditer(read(md)):
            ref = match.group(1)
            if TEMPLATE_HINT_RE.search(ref) or ref.startswith("http"):
                continue
            if ref in KNOWN_PENDING:
                continue
            target = REPO / ref
            if not resolve_reference(ref):
                problems.append(f"{rel}: broken reference `{ref}`")
    return problems


def check_task_fields() -> list[str]:
    problems: list[str] = []
    text = read(REPO / "02-product" / "TASKS.md")
    headings = list(TASK_RE.finditer(text))
    for i, heading in enumerate(headings):
        start = heading.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        block = text[start:end]
        title = heading.group(0).lstrip("# ")
        for field in REQUIRED_TASK_FIELDS:
            if not re.search(rf"^{field}:", block, re.M):
                problems.append(f"TASKS.md: `{title}` missing field `{field}`")
    return problems


def main() -> int:
    problems = check_required_files() + check_references() + check_task_fields()
    if problems:
        print("APOS doc check: FAIL\n")
        for p in problems:
            print(f"- {p}")
        print(f"\n{len(problems)} problem(s) found.")
        return 1
    print("APOS doc check: PASS")
    print(f"- required files: {len(REQUIRED_FILES)} present")
    print("- references: all resolve")
    print("- task entries: all fields present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
