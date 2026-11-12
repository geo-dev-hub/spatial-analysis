#!/usr/bin/env python3
"""Check relative Markdown links and notebook Markdown links in this repository.

External URLs and same-page anchors are deliberately skipped. This check
validates that local targets exist; it does not validate heading anchors or
the availability of external websites.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,}).*$", re.MULTILINE)


def strip_fenced_code(text: str) -> str:
    """Remove fenced code blocks so example URLs are not treated as links."""
    output: list[str] = []
    in_fence = False
    fence_char = ""
    fence_length = 0

    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_length = len(marker)
                continue
            if marker[0] == fence_char and len(marker) >= fence_length:
                in_fence = False
                continue
        if not in_fence:
            output.append(line)
    return "\n".join(output)


def markdown_sources(path: Path) -> list[tuple[str, str]]:
    if path.suffix.lower() == ".md":
        return [(str(path.relative_to(ROOT)), strip_fenced_code(path.read_text(encoding="utf-8")))]

    if path.suffix.lower() == ".ipynb":
        notebook = json.loads(path.read_text(encoding="utf-8"))
        sources = []
        for index, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") == "markdown":
                source = cell.get("source", [])
                text = "".join(source) if isinstance(source, list) else str(source)
                sources.append((f"{path.relative_to(ROOT)} [markdown cell {index}]", strip_fenced_code(text)))
        return sources

    return []


def resolve_target(source_name: str, raw_target: str) -> Path | None:
    target = raw_target.strip().split()[0].strip("<>")
    if not target or target.startswith("#"):
        return None

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None

    target_path = unquote(parsed.path)
    if not target_path:
        return None

    source = ROOT / source_name.split(" [markdown cell", 1)[0]
    if target_path.startswith("/"):
        resolved = ROOT / target_path.lstrip("/")
    else:
        resolved = source.parent / target_path

    return resolved.resolve()


def main() -> int:
    errors: list[str] = []
    checked = 0

    candidates = sorted(
        path for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.suffix.lower() in {".md", ".ipynb"}
    )

    for path in candidates:
        for source_name, text in markdown_sources(path):
            for match in LINK_RE.finditer(text):
                raw_target = match.group(1)
                resolved = resolve_target(source_name, raw_target)
                if resolved is None:
                    continue
                checked += 1
                if not resolved.exists():
                    errors.append(f"{source_name}: broken local link -> {raw_target}")

    if errors:
        print("\n".join(errors))
        print(f"\nFound {len(errors)} broken local link(s) among {checked} checked.")
        return 1

    print(f"Checked {checked} local links across {len(candidates)} Markdown and notebook files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
