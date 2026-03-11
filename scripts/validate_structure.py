from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_TOP_LEVEL = [
    "AGENTS.md",
    "README.md",
    "DISCLAIMER.md",
    "LICENSE",
    ".gitignore",
    ".github",
    "spec",
    "docs",
    "playbooks",
    "artifacts",
    "gates",
    "flows",
    "examples",
    "scripts",
    "adapters",
    "archive",
]

REQUIRED_PLAYBOOKS = [
    "intake-repo",
    "spec-delta",
    "plan-change",
    "define-acceptance",
    "ship-check",
    "write-release-artifacts",
    "review-diff",
    "post-ship-retro",
]

REQUIRED_PLAYBOOK_FILES = [
    "PLAYBOOK.md",
    "flow-example.md",
]


def main() -> int:
    errors: list[str] = []

    for name in REQUIRED_TOP_LEVEL:
        path = ROOT / name
        if not path.exists():
            errors.append(f"Missing top-level item: {name}")

    playbooks_dir = ROOT / "playbooks"
    if playbooks_dir.exists():
        for playbook in REQUIRED_PLAYBOOKS:
            pb_dir = playbooks_dir / playbook
            if not pb_dir.exists():
                errors.append(f"Missing playbook directory: playbooks/{playbook}")
                continue

            for item in REQUIRED_PLAYBOOK_FILES:
                target = pb_dir / item
                if not target.exists():
                    errors.append(f"Missing playbook file: playbooks/{playbook}/{item}")

    if errors:
        print("Structure validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Structure validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
