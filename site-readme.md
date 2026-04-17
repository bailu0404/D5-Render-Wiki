# D5 Render Wiki — Agent Remote Access

This site is the GitHub Pages deployment of the D5 Render LLM Wiki, designed for AI agents to access remotely.

## Access Instructions

### Step 1: Query the Index

```
https://bailu0404.github.io/D5-Render-Wiki/manifest.json
```

Returns a metadata list of all pages, each entry containing:

| Field | Description |
|-------|-------------|
| `name` | Page identifier (corresponds to wikilink name) |
| `title` | Page title |
| `path` | Relative path, e.g. `wiki/entities/ai-capabilities.md` |
| `tags` | Tag list |
| `sources` | Source list |
| `category` | Category: entities / concepts / sources / analyses / root |
| `updated` | Last updated date |

Search by `name` or `tags` to locate target pages.

### Step 2: Read a Page

Concatenate `base_url` + `/` + `path` to form the full URL:

```
https://bailu0404.github.io/D5-Render-Wiki/{path}
```

### Step 3: Follow Wikilinks

For `[[page-name]]` references within a page, look up that name's path in the manifest, then concatenate and read.

## Common Entry Points

| Purpose | URL |
|---------|-----|
| Search index | https://bailu0404.github.io/D5-Render-Wiki/manifest.json |
| Global quick reference | https://bailu0404.github.io/D5-Render-Wiki/wiki/compact.md |
| Page directory | https://bailu0404.github.io/D5-Render-Wiki/wiki/index.md |
| Overview | https://bailu0404.github.io/D5-Render-Wiki/wiki/overview.md |

## Wiki Scope

- Covers D5 Render versions 2.x through 3.x
- Content: features, rendering concepts, workflow plugins, AI tools, asset library, team collaboration, virtual walkthrough, animation system
- Excludes: internal implementation details, API/SDK documentation, pricing and licensing
