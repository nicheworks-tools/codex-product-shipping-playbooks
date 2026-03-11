from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
MARKDOWN_EXTENSIONS = {".md"}


def find_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in MARKDOWN_EXTENSIONS:
            files.append(path)
    return sorted(files)


def lint_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines:
        errors.append("file is empty")
        return errors

    if not lines[0].startswith("# "):
        errors.append("first line should start with a level-1 heading ('# ')")

    for index, line in enumerate(lines, start=1):
        if line.rstrip() != line:
            errors.append(f"line {index}: trailing whitespace")

    if text and not text.endswith("\n"):
        errors.append("file should end with a newline")

    return errors


def main() -> int:
    errors_found = False

    for path in find_markdown_files(ROOT):
        # Skip archived material for now.
        if "archive" in path.parts:
            continue

        errors = lint_file(path)
        if errors:
            errors_found = True
            print(f"{path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")

    if errors_found:
        return 1

    print("Markdown lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())