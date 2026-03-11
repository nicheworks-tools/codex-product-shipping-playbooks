from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
PLAYBOOKS_DIR = ROOT / "playbooks"

REQUIRED_ROOT_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "DISCLAIMER.md",
    ROOT / "LICENSE",
    ROOT / ".gitignore",
    ROOT / ".github" / "FUNDING.yml",
    ROOT / "spec" / "codex_product_shipping_playbooks_spec_ja.md",
    ROOT / "spec" / "codex_product_shipping_playbooks_spec_en.md",
    ROOT / "docs" / "vision.md",
    ROOT / "docs" / "architecture.md",
    ROOT / "docs" / "workflows.md",
    ROOT / "docs" / "roadmap.md",
    ROOT / "docs" / "quality-gates.md",
    ROOT / "docs" / "naming.md",
    ROOT / "flows" / "issue-to-ship.md",
    ROOT / "flows" / "repo-change-flow.md",
    ROOT / "flows" / "release-prep-flow.md",
    ROOT / "flows" / "diff-review-flow.md",
    ROOT / "flows" / "post-ship-retro-flow.md",
    ROOT / "adapters" / "README.md",
]

REQUIRED_PLAYBOOK_FILES = [
    "PLAYBOOK.md",
    "flow-example.md",
]

REQUIRED_ARTIFACTS = [
    ROOT / "artifacts" / "spec-delta-template.md",
    ROOT / "artifacts" / "change-plan-template.md",
    ROOT / "artifacts" / "acceptance-template.md",
    ROOT / "artifacts" / "pre-ship-review-template.md",
    ROOT / "artifacts" / "release-note-template.md",
    ROOT / "artifacts" / "changelog-entry-template.md",
    ROOT / "artifacts" / "diff-review-template.md",
    ROOT / "artifacts" / "retro-template.md",
]

REQUIRED_GATES = [
    ROOT / "gates" / "repo-intake-gate.md",
    ROOT / "gates" / "spec-delta-gate.md",
    ROOT / "gates" / "acceptance-gate.md",
    ROOT / "gates" / "pre-ship-gate.md",
    ROOT / "gates" / "release-artifacts-gate.md",
    ROOT / "gates" / "diff-review-gate.md",
    ROOT / "gates" / "retro-gate.md",
]

REQUIRED_EXAMPLE_FILES = [
    ROOT / "examples" / "issue-driven" / "README.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "README.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "00-issue.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "01-repo-context-memo.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "02-spec-delta.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "03-change-plan.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "04-acceptance-definition.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "05-pre-ship-review.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "06-release-note.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "07-changelog-entry.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "08-diff-review.md",
    ROOT / "examples" / "issue-driven" / "filter-persistence" / "09-retro.md",
]


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_ROOT_FILES + REQUIRED_ARTIFACTS + REQUIRED_GATES + REQUIRED_EXAMPLE_FILES:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")

    if not PLAYBOOKS_DIR.exists():
        errors.append("Missing required directory: playbooks/")
    else:
        for pb_dir in sorted(p for p in PLAYBOOKS_DIR.iterdir() if p.is_dir()):
            for filename in REQUIRED_PLAYBOOK_FILES:
                target = pb_dir / filename
                if not target.exists():
                    errors.append(f"Missing required file: {target.relative_to(ROOT)}")

    if errors:
        print("Required file check failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("All required files are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
