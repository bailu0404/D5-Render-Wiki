---
title: "CN News — D5 Chinese Market News (2025–2026)"
created: 2026-04-20
updated: 2026-04-20
sources:
  - raw/cn/news/release-3-0.md
  - raw/cn/news/release-2-11.md
  - raw/cn/news/d5-engine.md
  - raw/cn/news/ai-report-2025.md
  - raw/cn/news/design-industry-trend-2025.md
  - raw/cn/news/2025-annual-review.md
  - raw/cn/news/blog-d5-team.md
  - raw/cn/news/panorama-comment.md
  - raw/cn/news/global-plants-4.md
  - raw/cn/news/brand-furniture-2025.md
  - raw/cn/news/asia-student.md
  - raw/cn/news/lan-arc.md
  - raw/cn/news/yszy.md
  - raw/cn/news/d5-thu-plants-database.md
  - raw/cn/news/d5-seu-open-day.md
  - raw/cn/news/d5-campus-partners.md
  - raw/cn/news/chairman-unit-of-alliance.md
  - raw/cn/news/2026-campus-recruitment.md
  - raw/cn/news/2025-year-end.md
  - raw/cn/news/2025-annual-review.md
tags: [cn, news, releases, community, assets, ai, enterprise]
---

D5渲染器 Chinese market official news covering product releases, asset library updates, academic partnerships, case studies, and community events from 2025–2026. Source: d5render.cn/news/.

## Product Releases

### D5 3.0 (2026-01-21)
The major version jump introducing two new products and 29 new features:

- **[[d5-lite]] upgraded**: Now powered by the self-developed [[d5-engine|D5 Engine]], SketchUp plugin with AI + real-time path tracing; one-click sync to D5 Render for deep production. AI inspiration generation from scene geometry.
- **[[d5-works]] launched**: 3D asset platform for AEC professionals integrated into the launcher, enabling co-creation with global users.
- **AI Design Assistant — Scene Boost & Asset Recommendation**: AI analysis of the scene suggests asset placements and material improvements.
- **Volumetric clouds**: Physically-based real-time volumetric cloud system.
- **Ocean system**: Full ocean simulation (waves, foam, reflections).
- **Virtual tour**: In-app 360° immersive walk-through with navigation hotspots.
- **True Displacement (Beta)**: GPU-driven subdivision displacement for extreme surface detail.
- **Urban Generation upgrade**: Enhanced procedural city/block generation.

*Source: raw/cn/news/release-3-0.md*

### D5 2.11 (date from file: 2026-01-21, likely released late 2025)
33 new features and optimizations:

- **AI Design Assistant (AI Agent)**: Natural-language task execution. Launched with three sub-tools:
  - *Flower Garden Generator*: Climate/geography-aware planting plan from text description, 3 style presets, plant list export.
  - *Smart Seedling List*: One-click plant inventory export with name, size, count; auto cost calculation from uploaded price sheet.
  - *D5 Bot*: In-app AI support chatbot for real-time troubleshooting.
- **AI PBR Material Generation & Recommendation**: Upload reference image → AI generates PBR material from full image or selection; recommends similar materials from online library.
- **Advanced Brush** (高级笔刷): Enhanced scatter brush for landscape painting.
- **Custom Paths**: Place assets along arbitrary spline paths.
- **Disk Light** (圆盘灯): New circular area light type.
- **Full IES support**: All light types now support IES profiles.
- **Full Parallel Projection**: Complete support for isometric/parallel camera.
- **Baidu Netdisk integration** (Team Edition): Direct cloud storage integration for Chinese enterprise users.
- **XR Tour** (Team Edition): Extended reality collaborative walk-through.

*Source: raw/cn/news/release-2-11.md*

## D5 Engine — Self-Developed Rendering Engine

Announced 2026-01-15. D5 Engine is D5's proprietary real-time path tracing engine designed specifically for spatial design visualization. See [[d5-engine]] for full details.

Key differentiators vs. game-engine-based renderers:
- Full path tracing as the sole rendering pipeline (not a hybrid)
- Radiance Cache + ReSTIR + Multi-Layer Denoise for real-time performance
- SOA data optimization for GPU parallel efficiency
- 8–hundreds of light bounces (vs. 1–3 in traditional real-time)
- Self-developed cross-platform shader compiler: same codebase compiles to DX12 (Windows) and Metal (macOS)

*Source: raw/cn/news/d5-engine.md*

## Research & Industry Analysis

### 2025 AI Survey Report (co-published with Tencent Research Institute)
Survey of 2490 design professionals (1825 China, 665 overseas), conducted May–July 2025.

Key findings:
1. **85.8% AI adoption rate** in 2025 (up 23.7% from 2024)
2. **Ease-of-use** is the primary driver of adoption growth (tools like Tencent Yuanbao, Doubao, DeepSeek lowered barrier)
3. **Cost** replaced technical complexity as the main adoption barrier
4. AI adoption positively correlates with company size (66.2% of 100+ person firms deploy AI in real projects vs. 33.5% for smaller firms)
5. **91.6%** of AI-using designers have submitted AI-generated content as deliverables to clients
6. **58.2%** believe AI will not threaten design jobs (up from 50% in 2024)
7. **64.3%** feel their role has expanded through AI; **77.2%** report increased design control
8. ~10% use AI in most projects; concentration at early concept phase

*Source: raw/cn/news/ai-report-2025.md, raw/cn/news/design-industry-trend-2025.md*

### D5 2025 Annual Review
- 50+ useful features released in 2025
- 2160+ new asset items
- 830+ scene submissions in community forum
- 7300+ forum members
- Key 2025 technologies: real-time path tracing, AI Design Assistant, advanced brush, AI material workflow, AI image post-processing

*Source: raw/cn/news/2025-annual-review.md*

## Team Edition Features

[[d5-for-teams|D5 Team Edition]] highlights from blog post:
- **Admin dashboard**: Role-based permissions, member management, data analytics dashboard
- **Enterprise project library**: Local LAN-based deployment, version control, no-copy file access for team members
- **Team asset library**: Shared custom material/model libraries across the organization
- **Baidu Netdisk integration**: Chinese cloud storage for file sharing (CN-specific)
- **XR tour**: Team-based extended reality review sessions
- **D5 Showreel**: Presentation layer for client sharing
- **Rendering farm**: Distributed render via team machines

*Source: raw/cn/news/blog-d5-team.md*

## Collaboration Features

### Panorama Tour Comments (D5 Showreel)
Real-time collaborative annotation system inside D5 Showreel:
- Comment directly in 3D Dollhouse view or 2D panorama
- Four annotation types: text, location pin, image attachment, mixed
- External collaborators (clients) join via shared link or QR code; must authenticate D5 account to leave comments
- Traceable and actionable feedback tied to spatial coordinates

*Source: raw/cn/news/panorama-comment.md*

## Asset Library Updates

### Global Plants Vol. 4 (2026-01-21)
- 61 species, 269 high-quality animated plants
- Focus: Southwest China native plants + global landscape project needs
- Categories: ornamental grasses, flowering herbs, broadleaf trees, flowering trees, shrubs
- Species include: nephrolepis, sedum lineare, Woodwardia japonica, bromeliad, golden sweet flag, four-night sage, creeping phlox, oxalis, Veronica, hosta, pennywort, etc.

*Source: raw/cn/news/global-plants-4.md*

### Brand Furniture 2025 (2026-01-21)
1206 brand furniture models from five international luxury brands:
- **Flexform** (Italy) — sofas, tables, chairs, lighting, accessories
- **Natuzzi Italia** (Italy) — leather sofas, ergonomic seating
- **&Tradition** (Denmark) — Nordic design furniture
- **BoConcept** (Denmark) — urban modern furniture
- **Kettal** (Spain) — outdoor furniture and lighting

*Source: raw/cn/news/brand-furniture-2025.md*

### Asia Student Characters (2026-01-21)
- 124 dynamic + static character assets
- Based on real Asian model 3D scans (photogrammetry)
- Clothing: standard uniform, casual, seasonal (short/long sleeve)
- Poses: classroom (standing, raising hand), corridor (walking, talking), library (sitting, reading), playground (running, exercise)
- Use case: campus, education, school building visualization projects

*Source: raw/cn/news/asia-student.md*

## Case Studies & User Stories

### Lan Architecture × D5 (BIM Workflow)
Lan Architecture (founded by two Swiss-educated architects) integrated D5 with Archicad and Revit BIM workflows. Key outcomes:
- Eliminated workflow fragmentation: D5 plugin syncs live with BIM models
- Real-time material verification under varying lighting conditions
- Complete visualization + post-processing in single software

*Source: raw/cn/news/lan-arc.md*

### Yisheng Zaoyuan (壹生造园) — Garden Design Company
- Chinese traditional mountain-water garden design company
- Uses D5 for 3D spatial validation before construction
- Covers architectural + interior + garden combined scenes
- D5 landscape tools + real-time rendering enable design-to-construction continuity

*Source: raw/cn/news/yszy.md*

## Academic & Education Partnerships

### D5 × Tsinghua Landscape Department — Global Plant Database
Joint project: "D5 Global Landscape Plant Intelligent 3D Database Fundamental Research"
- Partners: Tsinghua University School of Architecture – Landscape Architecture, Tsinghua Architectural Design Research Institute
- Provides professional botanical reference data for D5's asset library plants
- D5 has 3M+ global users; 30% are landscape professionals
- Current library: 3900+ plant assets across 1100+ species
- Partner clients include AECOM, ASPECT Studios, SWA Shanghai, 奥雅, 山水比德, 上海D+H, UNStudio

*Source: raw/cn/news/d5-thu-plants-database.md*

### D5 × Southeast University Architecture School Open Day (2025-11-12)
- SEU Architecture School visit to D5 offices
- Introduced D5 Student Edition (free core features + full asset library)
- Showcased D5 Cup University Design Competition
- Showcased D5 Campus Partners program

*Source: raw/cn/news/d5-seu-open-day.md*

### D5 Campus Partners Program
Ongoing campus ambassador program:
- Target: students in architecture, landscape, urban planning, interior design, digital media, product design, film/animation programs
- Benefits: official support for campus events, exclusive training, branded merchandise, recruitment referral access, dedicated community

*Source: raw/cn/news/d5-campus-partners.md*

### National Vocational Education Alliance — Vice Chairman
D5 (江苏维伍喔飞信息科技有限公司) appointed vice-chairman of the Cultural & Arts Domain Community of the National Vocational School Teacher Innovation Development Alliance (全国职业学校教师创新发展联盟文化艺术领域共同体).
- Ceremony: 2025-09-26, Shanghai Institute of Arts and Crafts
- Alliance covers 329 schools and 42 enterprises
- D5's role: integrate digital technology with art design education, AI-empowered teacher training

*Source: raw/cn/news/chairman-unit-of-alliance.md*

### D5 2026 Campus Recruitment
Global recruitment for graduates (Sep 2023 – Aug 2026 graduation window).
- Positions in engineering (rendering, AI, engine) and design
- Contact: recruitment portal on official website

*Source: raw/cn/news/2026-campus-recruitment.md*

### 2025 Year-End Community Submission Event
Open call for 2025 community works:
- Animation submissions via email to event@d5render.com
- Image submissions via Xiaohongshu (小红书) with #D5社区精选
- Story submissions via DingTalk form
- Selected works featured on domestic and international platforms

*Source: raw/cn/news/2025-year-end.md*
