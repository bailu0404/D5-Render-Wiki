---
title: "Manual: Getting Started"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/getting-started -- quick-start.md"
  - "raw/assets/manual/getting-started -- d5-workflow.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- interface-shortcuts-camera.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- model-connection.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- material.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- landscape.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- environment-effects.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- image-animation-output.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- ai-features.md"
  - "raw/assets/manual/About D5 Render  User Manual.md"
tags: [manual, getting-started, workflow, installation]
---

The Getting Started chapter of the D5 Render user manual, covering installation and configuration, interface operations, and workflow overview.

## System Requirements

- **Minimum GPU**: NVIDIA GeForce GTX 1060 6GB
- **Recommended GPU**: NVIDIA GeForce RTX 2060 or higher, Quadro RTX series
- **System**: Windows 10 1809 or higher
- **Driver**: NVIDIA 471.68 or higher (latest recommended)
- The rendering pipeline is based on DX12 and DXR

## Download & Installation

### Before Version 2.5
Extract the installation package, install to the C drive by default, with support for custom paths. Assets are downloaded to the installation path by default and can be migrated in Preferences after installation.

### Version 2.5 (Simplified Installation)
The installation package automatically executes download and installation. Supports selecting workspace paths for preset assets, local resources, and temporary file locations.

### Version 2.11+ (D5 Launcher)
- Requires installing [[d5-launcher]] first, then downloading D5 Render through the Launcher
- D5 Launcher replaces the original welcome page and automatically minimizes to the system tray when opening a scene
- Integrates D5 Render, D5 Lite, and D5 Sync plugins

## D5 Render Interface Overview

D5 Render consists of three main parts:
- **Main Interface**: Create scenes, adjust models, edit materials
- **Render Mode**: Add render settings and editing panels
- **Asset Library**: A separately displayed asset browsing window

## Supported File Formats

- `.d5a` — D5 Render model format
- `.skp` — SketchUp 2017+
- `.3dm` — Rhino 6.5+
- `.fbx` — Supports model data, no materials
- `.abc` — Import to scene only

## D5 Workflow

The D5 Render workflow is divided into six core stages:

1. **Interface, Shortcuts, Camera** — Interface layout, shortcut key settings, [[camera-and-view|camera controls]]
2. **Model Connection** — Import models via [[workflow-plugins|workflow plugins]]
3. **Materials** — [[pbr-materials|PBR material]] editing and application
4. **Landscape** — [[tools-landscape|landscape tools]] (terrain, scatter, vegetation)
5. **Environment & Effects** — [[lighting-system|lighting]], [[environment-and-effects|weather]], [[post-processing|post-processing]]
6. **Image & Animation Output** — [[render-output|render output]]

## Model Preparation Tips

- Check model face normal directions to ensure correct orientation
- Ensure the model is complete, avoiding broken or overlapping faces in the camera view
- Organize UV coordinates before import; after import, you can adjust stretch, offset, rotation, triplanar mapping, etc. in D5
