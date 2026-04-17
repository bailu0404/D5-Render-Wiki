# D5 Render Wiki — Schema

This document defines the conventions, structure, and workflows for the D5 Render LLM Wiki. The LLM follows these rules when ingesting sources, answering queries, and maintaining the wiki.

## Directory Structure

```
raw/                  # Raw sources (IMMUTABLE — read only, never modify)
  assets/             # Downloaded images and attachments
  *.md                # Clipped or imported source documents
wiki/                 # LLM-generated wiki pages (the LLM owns this layer)
  index.md            # Content-oriented catalog of all pages
  log.md              # Append-only chronological operation log
  overview.md         # Top-level synthesis of D5 Render
  entities/           # Pages for specific features, tools, components
  concepts/           # Pages for rendering concepts, techniques, principles
  sources/            # Summary pages for each ingested source
  analyses/           # Generated analyses, comparisons, deep dives
```

## Page Conventions

### File naming
- Use lowercase with hyphens: `real-time-rendering.md`, not `Real-Time Rendering.md`
- Source summary pages: match the raw source filename, prefixed with `src-`: `src-d5-render-features.md`
- Entity pages: named after the entity: `pbr-materials.md`, `ai-tools.md`
- Concept pages: named after the concept: `path-tracing.md`, `physically-based-rendering.md`

### Frontmatter
Every wiki page must include YAML frontmatter:

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of source filenames that contributed]
tags: [relevant tags]
---
```

### Cross-references
- Use Obsidian wikilink syntax: `[[page-name]]`
- Link liberally — every mention of a concept or entity that has its own page should be linked
- When creating a new page, ensure it is linked from at least one existing page (no orphans)

### Content style
- Write in clear, concise English
- Lead with a one-sentence definition or summary
- Use headings to organize sections
- Include source citations: reference the raw source file at the end of relevant sections

## Workflows

### Ingest
When a new source is added to `raw/`:

1. Read the source thoroughly
2. Discuss key takeaways with the user
3. Create a source summary page in `wiki/sources/`
4. Create or update entity pages in `wiki/entities/` for each feature/component mentioned
5. Create or update concept pages in `wiki/concepts/` for each technique/principle mentioned
6. Update `wiki/overview.md` if the source affects the top-level synthesis
7. Update `wiki/index.md` — add new pages to the appropriate category
8. Append an entry to `wiki/log.md` with format: `## [YYYY-MM-DD] ingest | Source Title`
9. A single source may touch 10-15 wiki pages — that's expected and good

### Query
When the user asks a question:

1. Read `wiki/index.md` to find relevant pages
2. Read the relevant wiki pages
3. Synthesize an answer with citations (wikilinks to source pages)
4. If the answer is substantial, offer to file it as a new page in `wiki/analyses/`
5. Update `wiki/log.md` with format: `## [YYYY-MM-DD] query | Question topic`

### Lint
Periodically health-check the wiki:

- Find contradictions between pages and flag them
- Identify stale claims that newer sources supersede
- Find orphan pages with no inbound links
- Spot important concepts mentioned but lacking their own page
- Check for missing cross-references
- Identify data gaps that could be filled with a web search
- Suggest new questions to investigate and new sources to look for
- Update `wiki/log.md` with format: `## [YYYY-MM-DD] lint | Summary of findings`

## Link Resolution

Wikilinks `[[pagename]]` resolve to file paths as follows:
- `[[pagename]]` → `wiki/entities/pagename.md` or `wiki/concepts/pagename.md` or `wiki/sources/pagename.md`
- Source summary pages use `src-` prefix in filename but NOT in wikilink: `[[src-manual-ai]]` → `wiki/sources/src-manual-ai.md`
- If uncertain, check `wiki/index.md` for the exact category

## Agent Usage Guide

This wiki is designed for AI agents to understand D5 Render. Recommended usage:

1. **Start from index.md** — Read `wiki/index.md` first to locate relevant pages, then deep-read 2-3 target pages
2. **Use compact.md for global context** — `wiki/compact.md` contains one-line definitions of all entities and concepts; read it once to build a mental model
3. **Follow wikilinks for depth** — Each page links to related concepts; trace links when you need more detail
4. **Respect wiki boundaries** — See the scope declaration at the top of `wiki/index.md`

## Remote Access (GitHub Pages)

The wiki is deployed to GitHub Pages. When the local repository is unavailable, agents can access it remotely via HTTP:

1. **Search index** — `WebFetch https://bailu0404.github.io/D5-Render-Wiki/manifest.json` → search pages by name/tags
2. **Quick reference** — `WebFetch https://bailu0404.github.io/D5-Render-Wiki/wiki/compact.md` → global cheat sheet
3. **Read pages** — `WebFetch https://bailu0404.github.io/D5-Render-Wiki/wiki/entities/xxx.md` → deep-read specific pages

**Wikilink remote resolution**: `[[page-name]]` → find page-name's path in manifest.json → concatenate `base_url + "/" + path`

**Priority**: When the local wiki repository is available, read files directly (faster); when unavailable, use GitHub Pages remote access.

## Rules

- **NEVER** modify files in `raw/` — they are immutable
- **ALWAYS** update `index.md` when creating or significantly modifying a page
- **ALWAYS** append to `log.md` — never delete or modify existing entries
- **ALWAYS** include frontmatter in new wiki pages
- **ALWAYS** link to existing pages when mentioning their topics
- **PREFER** updating an existing page over creating a new one when the topic overlaps
- **PREFER** involving the user in ingest — read the source together, discuss what to emphasize
