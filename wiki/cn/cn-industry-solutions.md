---
title: D5 Render — CN Industry Solutions
created: 2026-04-28
updated: 2026-04-28
sources:
  - raw/cn/official/homepage.md
  - raw/cn/news/lan-arc.md
  - raw/cn/news/d5-seu-open-day.md
  - raw/d5render-knowledge-base.md
tags: [cn, industry, architecture, landscape, interior, sales, use-cases]
---

D5 Render serves four primary design industries in the Chinese market. This page documents the value proposition, key workflows, and recommended tools per industry — structured for sales and pre-sales use.

## 建筑设计 Architecture Design

### Value Proposition
D5 positions itself as an all-in-one platform for architectural visualization: not just a rendering tool, but a unified environment for design optimization, team collaboration, and client communication.

### Key Capabilities
- **Large scene handling**: Stable performance on building-scale and urban-scale models
- **Live-sync plugins**: Real-time connection to Revit, ArchiCAD, Rhino, SketchUp — no export/import cycle
- **Team collaboration** ([[d5-for-teams]]): Multi-user editing, project library, admin controls
- **Animation + virtual tours**: Walkthrough videos and [[virtual-tour|XR spatial tours]] for project presentations
- **D5 Lite**: Conceptual massing and early-stage design exploration within the modeling environment

### Common Workflows
1. Design in Revit/ArchiCAD → D5 Render via live-sync → real-time visualization
2. Concept exploration with D5 Lite in Rhino/SketchUp
3. Final delivery: 4K/8K renders + animated walkthrough + interactive virtual tour

### CN Market Context
- Many large CN architectural firms (CSCEC, CCDI, goa, Jiangsu Institute, etc.) use D5 for client presentations
- Key differentiator vs Lumion: better large-scene performance; vs Enscape: standalone capability + asset library; vs Twinmotion: AI features + CN ecosystem
- **G2 ranking**: #1 architectural rendering software (confirmed 2026)

### Reference Clients (CN)
AECOM, BIG (global, mentioned in CN site), 奥雅设计, UNStudio, and dozens of leading CN architecture firms.

---

## 景观设计 Landscape Design

### Value Proposition
D5 is purpose-built for landscape work via PCG (Procedural Content Generation) tools and AI-powered planting workflows. It is the only major rendering tool with a dedicated landscape PCG toolset natively integrated.

### Key Capabilities
- **Plant brush, path, scatter tools**: Place thousands of plants with realistic distribution ([[tools-landscape]])
- **AI Smart Planting** (AI智能种植): Automated planting based on ecosystem rules
- **Flower Garden Generator** (花境生成器): Generates planting schemes; supports CN climate zones and export of procurement-compatible plant lists
- **Smart Seedling List** (智能苗木清单): Auto-generates species, size, count, cost data matching CN construction documentation requirements
- **Tsinghua plant database**: 3,900+ plant assets (1,100+ species) with accurate botanical metadata (see [[cn-overview]])
- **Terrain system**: Terrain sculpting, ocean simulation, terrain painting
- **Cesium integration**: Urban-scale 3D geospatial data overlay

### Common Workflows
1. Import landscape design from SketchUp/Rhino → D5 Render
2. Use plant brush and AI planting to populate vegetation
3. Export smart seedling list for procurement documentation
4. Deliver animated seasonal variation videos + virtual tours for client approval

### CN Market Context
- **30% of D5's CN users are landscape/garden professionals** — the highest concentration of any single segment
- Dominant software pairing: SketchUp + D5 Render
- Key competitive advantage: no other major rendering tool offers integrated smart planting + procurement list export

### Reference Clients (CN)
SWA Shanghai, 山水比德, ASPECT Studios, 上海D+H, 奥雅设计.

---

## 室内设计 Interior Design

### Value Proposition
High-quality real-time rendering enables rapid iteration on material, lighting, and furniture selections. Client presentations via photorealistic stills, animations, and virtual tours increase project win rates.

### Key Capabilities
- **PBR material system**: [[pbr-materials|Physically-based materials]] for accurate fabric, wood, stone, metal representation
- **Lighting system**: 7 light types, IES profiles, HDRI; realistic interior lighting simulation ([[lighting-system]])
- **D5 Works asset library**: 16,000+ models including brand furniture (Flexform, Natuzzi, BoConcept, Kettal — relevant to high-end CN interior projects)
- **AI material generation**: Generate custom surface materials from text or image prompts
- **Virtual tour**: Clients can explore the design in an interactive walkthrough before construction

### Common Workflows
1. Model in 3ds Max/SketchUp → D5 Render via live-sync
2. Iterate materials, lighting, camera angles in real-time
3. Deliver: photorealistic renders + walkthrough animation + virtual tour link

### CN Market Context
- Interior design is the #3 user segment in CN after architecture and landscape
- Key software pairings: 3ds Max + D5, SketchUp + D5
- Competitive advantage vs V-Ray/Corona: real-time iteration speed; vs Lumion: more precise interior material control

---

## 园林与地产 Garden & Real Estate Visualization

### Value Proposition
Residential and commercial property developers use D5 for sales center presentations, model room visualization, and project marketing materials.

### Key Capabilities
- City generation tools for residential compound visualization
- High-quality plant assets (Global Plants Vol. 4 — SW China focus, native species)
- Asia Student Characters asset pack for realistic population of scenes
- Virtual tour for property showroom replacement or supplement
- D5 Lite for quick conceptual iterations

### CN Market Context
- Real estate marketing is a significant CN-specific use case, driven by pre-sale visualization needs
- Virtual tours replace or supplement physical show flats
- Virtual tour sharing via Showreel platform — accessible within China without VPN

---

## Industry-to-Plugin Mapping (Quick Reference)

| Industry | Primary Modeling Tool | Recommended Plugin |
|----------|----------------------|-------------------|
| Architecture (China) | Revit, ArchiCAD, Rhino | Revit sync / ArchiCAD LiveSync / Rhino LiveSync |
| Architecture (concept) | SketchUp | SketchUp LiveSync |
| Landscape | SketchUp, Rhino | SketchUp LiveSync / Rhino LiveSync |
| Interior | 3ds Max, SketchUp | 3ds Max LiveSync / SketchUp LiveSync |
| Animation / film | Cinema 4D, Blender | C4D sync / Blender sync |
| BIM-heavy | Revit, ArchiCAD | Revit sync / ArchiCAD LiveSync |

## See Also

- [[workflow-plugins]] — Full plugin compatibility matrix
- [[tools-landscape]] — Landscape and terrain tools detail
- [[virtual-tour]] — Virtual tour and XR detail
- [[d5-for-teams]] — Team Edition for enterprise design firms
- [[cn-pricing]] — Pricing tiers and which tier suits each use case
- [[src-cn-official-homepage]] — Homepage source with industry quotes
