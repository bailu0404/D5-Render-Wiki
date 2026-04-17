---
title: "Manual: Workflow Plugins"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/workflow -- sketchup.md"
  - "raw/assets/manual/workflow -- rhino.md"
  - "raw/assets/manual/workflow -- 3ds-max.md"
  - "raw/assets/manual/workflow -- revit.md"
  - "raw/assets/manual/workflow -- blender.md"
  - "raw/assets/manual/workflow -- archicad-1.md"
  - "raw/assets/manual/workflow -- archicad.md"
  - "raw/assets/manual/workflow -- vectorworks.md"
  - "raw/assets/manual/workflow -- general-questions.md"
  - "raw/assets/manual/workflow -- abnormal-situations.md"
tags: [manual, workflow, plugin, sync, livesync, sketchup, rhino, revit, 3ds-max, blender, archicad, vectorworks]
---

The Workflow Plugins chapter of the D5 Render user manual, covering all sync and live sync plugins between modeling software and D5 Render.

## Plugin Types

### D5 Sync (Sync Plugin)
Non-real-time sync that exports model data from modeling software to D5 Render. Supports model updates and replacement.

### D5 LiveSync (Live Sync Plugin)
Real-time sync where modifications in the modeling software are instantly reflected in D5 Render.

## Supported Modeling Software

| Software | Sync | LiveSync | Notes |
|----------|------|----------|-------|
| SketchUp | Yes | Yes | Most complete workflow support |
| Rhino | Yes | Yes | Supports Rhino 6.5+ |
| 3ds Max | Yes | Yes (Beta) | Supports V-Ray/Corona feature comparison table |
| Revit | Yes | No | Non-real-time sync only |
| ArchiCAD | Yes | Yes | Supports ArchiCAD 26/27 |
| Blender | Yes | No | Non-real-time sync only |
| VectorWorks | No | Yes | Live sync only |
| Cinema 4D | Yes | No | Non-real-time sync only |

## 3ds Max Special Notes

- Supports V-Ray feature comparison table, listing how V-Ray features correspond in D5
- Supports Corona feature comparison table
- LiveSync is currently in Beta

## General Questions

- Plugin installation and uninstallation
- Common errors when launching D5 from D5 Converter
- Sync timeout issues
- Top view direction mismatch between modeling software and D5
- `.d5a` file group structure alignment and sync coordinate issues

## Abnormal Situations

### LiveSync Abnormalities
- Handling methods for material picking issues after sync

### Sync Abnormalities
- Handling methods for displacement issues when replacing models using Sync for 3ds Max
