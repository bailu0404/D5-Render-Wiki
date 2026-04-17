---
title: Workflow Plugins
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/workflow -- sketchup.md"
  - "raw/assets/manual/workflow -- rhino.md"
  - "raw/assets/manual/workflow -- 3ds-max.md"
  - "raw/assets/manual/workflow -- revit.md"
  - "raw/assets/manual/workflow -- blender.md"
  - "raw/assets/manual/workflow -- archicad-1.md"
  - "raw/assets/manual/workflow -- vectorworks.md"
  - "raw/assets/blog/sketchup-rendering-with-d5-render.md"
  - "raw/assets/blog/best-real-time-rhino-rendering-workflow-for-you-with-d5-render.md"
  - "raw/assets/blog/d5-render-for-revit-best-real-time-3d-rendering-workflow.md"
  - "raw/assets/blog/blender-archviz-with-d5-workflow.md"
  - "raw/assets/blog/archicad-d5-large-scale-architecture-design.md"
tags: [workflow, plugin, sync, livesync, sketchup, rhino, revit, 3ds-max, blender, archicad]
---

D5 Render's full suite of workflow plugins supports model sync and real-time sync between mainstream modeling software and D5 Render.

## Two Sync Modes

### D5 Sync
Non-real-time sync — exports model data from modeling software to D5 Render, supporting model updates and replacement.

### D5 LiveSync
Real-time sync — modifications in the modeling software are instantly reflected in the D5 Render viewport, enabling a WYSIWYG workflow.

## Supported Modeling Software

| Software | Sync | LiveSync | Notes |
|----------|------|----------|-------|
| **SketchUp** | Yes | Yes | Most complete support, 2017+ |
| **Rhino** | Yes | Yes | Rhino 6.5+ |
| **3ds Max** | Yes | Yes (Beta) | Supports V-Ray/Corona comparison tables |
| **Revit** | Yes | — | Non-real-time sync |
| **ArchiCAD** | Yes | Yes | ArchiCAD 26/27 |
| **Blender** | Yes | — | Non-real-time sync |
| **VectorWorks** | — | Yes | LiveSync only |
| **Cinema 4D** | Yes | — | Non-real-time sync |

## 3ds Max Special Features

- **V-Ray Feature Comparison Table**: Lists V-Ray material/light mappings in D5
- **Corona Feature Comparison Table**: Corona material/light compatibility mapping
- LiveSync is currently in Beta

## D5 Converter

The core component of the D5 Sync plugin, responsible for model conversion and synchronization:
- Supports `.d5a` format output
- Supports automatic material conversion
- Supports model updates and replacement

## Common Troubleshooting

- Plugin installation and uninstallation
- Common errors when launching D5 from Converter
- Sync timeout issues
- Coordinate system orientation inconsistencies
- File group structure alignment issues

*Sources: [[src-manual-workflow-plugins]], [[src-blog-workflow-plugins]]*
