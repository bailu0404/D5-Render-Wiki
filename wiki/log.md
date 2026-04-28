# D5 Render Wiki Log

> Append-only chronological record of wiki operations.
> Format: `## [YYYY-MM-DD] operation | Description`

## [2026-04-28] ingest | CN Official Website (d5render.cn pricing / download / homepage)

- Sources: `raw/cn/official/pricing.md`, `raw/cn/official/download.md`, `raw/cn/official/homepage.md`
- Tool used: cn_official_scraper.py (new script for periodic re-scraping on version releases)
- Created 3 source summary pages:
  - [[src-cn-official-pricing]] — four pricing tiers, feature comparison table
  - [[src-cn-official-download]] — plugin compatibility matrix, CN CDN download links
  - [[src-cn-official-homepage]] — product matrix, industry solutions, community channels
- Created 4 CN wiki pages:
  - [[cn-pricing]] — full pricing breakdown (Community free / Pro ¥200/月 / Team / Student free)
  - [[cn-support]] — support channels, learning resources, community platforms
  - [[cn-industry-solutions]] — architecture, landscape, interior, real estate workflows; plugin-to-industry mapping
  - [[cn-sales-faq]] — sales FAQ covering pricing, features, competitor Q&A, enterprise purchasing
- Updated [[index]] with new pages (total: 62 pages, 38 sources)

## [2026-04-10] ingest | D5 Render Features (Official Website)

- Source: `raw/D5 Render.md`
- Created source summary: [[src-d5-render-features]]
- Created overview: [[overview]]
- Created entity pages: [[real-time-rendering]], [[ai-capabilities]], [[asset-tools]], [[environment-and-effects]], [[efficiency-tools]], [[camera-and-view]]
- Created concept page: [[pbr-materials]]
- Updated index with 8 pages total

## [2026-04-11] ingest | D5 Render User Manual (raw/assets/manual/)

- Source: ~200 manual pages in `raw/assets/manual/`
- Created 10 source summary pages:
  - [[src-manual-getting-started]], [[src-manual-ai]], [[src-manual-material]], [[src-manual-lighting-environment]], [[src-manual-render-output]], [[src-manual-animation-tour]], [[src-manual-assets-landscape]], [[src-manual-workflow-plugins]], [[src-manual-teams-ecosystem]], [[src-manual-hardware-preference]]
- Created 9 entity pages: [[d5-lite]], [[d5-works]], [[d5-launcher]], [[d5-for-teams]], [[d5-studio]], [[lighting-system]], [[render-output]], [[tools-landscape]], [[workflow-plugins]], [[virtual-tour]], [[animation-system]], [[widgets]]
- Created 9 concept pages: [[global-illumination]], [[hdri-lighting]], [[displacement-mapping]], [[caustics]], [[post-processing]], [[volumetric-effects]], [[gaussian-splatting]], [[xr-technology]], [[depth-of-field]]
- Updated [[overview]] with manual-sourced ecosystem and feature details

## [2026-04-11] ingest | D5 Render Blog (raw/assets/blog/)

- Source: ~300 blog posts in `raw/assets/blog/`
- Created 13 source summary pages:
  - [[src-blog-ai-features]], [[src-blog-workflow-plugins]], [[src-blog-materials-textures]], [[src-blog-lighting-environment]], [[src-blog-camera-rendering]], [[src-blog-animation]], [[src-blog-assets-landscape]], [[src-blog-case-studies]], [[src-blog-product-updates]], [[src-blog-architecture-industry]], [[src-blog-tips-techniques]], [[src-blog-virtual-tour-xr]], [[src-blog-d5-ecosystem]]
- Updated index with 40 pages total

## [2026-04-13] lint | Agent optimization: added usage guide and quick reference

- Added Link Resolution and Agent Usage Guide to CLAUDE.md
- Added Wiki Scope and Quick Start for Agents to index.md
- Created [[compact]] — quick reference with one-line definitions of all entities and concepts
- Updated index.md with compact.md entry, total pages now 41

## [2026-04-13] query | D5 Render vs Lumion vs Enscape Comparison

- User asked about differences between D5 Render and Lumion/Enscape
- Used Brave Search API for external comparison resources (5 English + 5 Chinese results)
- Synthesized wiki pages and search results into a 10-dimension systematic comparison
- Created analysis page: [[d5-vs-lumion-vs-enscape]]
- Updated index.md, total pages now 42

## [2026-04-17] ingest | Sales Framework, Competitor Comparison, Knowledge Base, Legal Documents

- Sources: `raw/d5-sales-framework.md`, `raw/d5render-competitor-comparison.md`, `raw/d5render-knowledge-base.md`, `raw/D5 Render Terms of Service.md`, `raw/General Terms of Service.md`, `raw/Privacy Policy _ D5 Render.md`
- Created 4 source summary pages:
  - [[src-sales-framework]], [[src-competitor-comparison]], [[src-knowledge-base]], [[src-legal-terms]]
- Updated [[overview]] with market position, user base, and data security info from knowledge base
- Updated index.md with new source pages and updated scope, total pages now 46

## [2026-04-17] translate | Full wiki English translation

- Translated all wiki content from Chinese to English
- Affected: all entity pages (18), concept pages (10), source pages (28), analysis page (1)
- Translated root pages: index.md, overview.md, compact.md, log.md
- Translated site-readme.md and updated CLAUDE.md content style rule
- All new pages created directly in English

## [2026-04-20] ingest | CN News — Batch 1 (raw/cn/news/, 20 articles)

- Sources: 20 articles from `raw/cn/news/` covering D5 3.0, D5 2.11, D5 Engine, AI report, assets, case studies, education
- Created source summary: [[src-cn-news]] — comprehensive summary of all 20 CN news articles
- Created new directory `wiki/cn/` for Chinese-market-specific content
- Created overview page: [[cn-overview]] — Chinese market overview (company, community, CN features, academic partnerships, licensing)
- Created new entity page: [[d5-engine]] — D5 proprietary real-time path tracing engine (full path tracing, GPU SOA, DX12/Metal shader)
- Updated [[d5-lite]] entry in compact.md to note D5 Engine integration (3.0+)
- Updated index.md: added CN section, d5-engine to entities, updated scope and page count (49 pages, 28 sources)
- Updated compact.md: added d5-engine, cn-overview, src-cn-news entries
- Key new content: D5 3.0 features (volumetric clouds, ocean, virtual tour, true displacement), AI Design Assistant sub-tools, 2025 AI survey data (85.8% adoption), brand furniture (1206 items), global plants Vol.4, Asia student characters

## [2026-04-20] ingest | CN Manual — Batch 2 (raw/cn/manual/ modules)

- Sources: ~200 files across 30+ modules in `raw/cn/manual/` (docs.d5render.cn)
- Created 4 source summary pages:
  - [[src-cn-manual-account]] — account, student edition verification, invoicing, AI credits/cloud quotas
  - [[src-cn-manual-ai]] — AI Design Assistant commands, material generation quota (50 uses), atmosphere match, ultra-HD texture, seamless
  - [[src-cn-manual-teams]] — Team Edition: org management, multi-user editing, Showreel, SSO, Baidu Netdisk, Cesium integrations
  - [[src-cn-manual-system]] — hardware requirements, GPU driver compatibility (Win10 + NVIDIA), scene limits (4096 lights, 64 caustic), error messages
- Created CN detail page: [[cn-account]] — student edition process (学信网 steps), invoicing, quota tables
- Updated [[cn-overview]] sources to include manual references
- Updated index.md CN section with new pages; total pages 55, sources 32
- Updated compact.md with CN manual source entries
- Key CN-unique content captured: student verification workflow, material generation 50-use limit, 10GB/100GB cloud quotas, scene hard limits, Win10 + NVIDIA driver warnings, Baidu Netdisk (CN-exclusive) integration
