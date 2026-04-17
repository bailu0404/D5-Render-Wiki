#!/usr/bin/env python3
"""Generate manifest.json from wiki pages for agent remote access."""

import json
import os
import re
import sys
from datetime import date
from pathlib import Path

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"
CATEGORIES = {"entities", "concepts", "sources", "analyses"}


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from markdown text."""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    current_key = None
    current_list = None
    for line in m.group(1).splitlines():
        # Multi-line list item: "  - value"
        list_item = re.match(r"^\s+-\s+(.+)$", line)
        if list_item and current_key is not None:
            if current_list is None:
                current_list = []
            current_list.append(list_item.group(1).strip().strip("'\""))
            fm[current_key] = current_list
            continue
        # Key-value line
        if ":" in line and not line.startswith(" "):
            # Flush previous list
            current_key = None
            current_list = None
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
            elif val == "":
                # Value is empty — might be followed by multi-line list
                current_key = key
                current_list = []
                fm[key] = []
                continue
            fm[key] = val
            current_key = key if isinstance(val, list) and not val else None
            current_list = val if isinstance(val, list) else None
    return fm


def build_manifest() -> dict:
    pages = []
    for md in sorted(WIKI_DIR.rglob("*.md")):
        rel = md.relative_to(WIKI_DIR)
        text = md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)

        # Determine category from path
        parts = rel.parts
        category = parts[0] if len(parts) > 1 and parts[0] in CATEGORIES else "root"

        # Page name = stem (without .md)
        name = md.stem

        pages.append({
            "name": name,
            "title": fm.get("title", name),
            "path": f"wiki/{rel}",
            "tags": fm.get("tags", []),
            "sources": fm.get("sources", []),
            "category": category,
            "updated": fm.get("updated", ""),
        })

    return {
        "updated": str(date.today()),
        "base_url": "https://bailu0404.github.io/D5-Render-Wiki",
        "pages": pages,
    }


def main():
    out_dir = Path(__file__).resolve().parent.parent
    manifest = build_manifest()
    out_path = out_dir / "manifest.json"
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated manifest.json with {len(manifest['pages'])} pages")


if __name__ == "__main__":
    main()
