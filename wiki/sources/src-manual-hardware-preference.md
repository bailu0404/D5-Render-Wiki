---
title: "Manual: Hardware, Preferences & System"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- hardware.md"
  - "raw/assets/manual/user-guide -- hardware -- system-requirements-for-d5-render.md"
  - "raw/assets/manual/user-guide -- hardware -- what-graphic-cards-does-d5-support.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-view-and-optimize-graphics-card-usage.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-view-and-optimize-memory-usage.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-view-and-upgrade-graphics-card-driver.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-check-memory-usage-graphics-memory-usage-and-graphics-card-driver-version.md"
  - "raw/assets/manual/user-guide -- hardware -- does-the-cpu-have-a-big-impact-on-d5.md"
  - "raw/assets/manual/user-guide -- hardware -- what-is-hardware-testing.md"
  - "raw/assets/manual/user-guide -- hardware -- what-is-the-hardware-test-tool-benchmark.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-choose-the-right-computer-power-for-graphic-cards.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-use-support-tool.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-use-the-3dconnexion-r-spacemouse-in-d5-render.md"
  - "raw/assets/manual/user-guide -- hardware -- why-are-close-textures-clearer-but-distant-textures-blurry.md"
  - "raw/assets/manual/user-guide -- hardware -- why-is-d5-not-working-properly-when-remote.md"
  - "raw/assets/manual/user-guide -- hardware -- why-need-to-wait-a-long-time-to-open-a-d5-scene.md"
  - "raw/assets/manual/user-guide -- hardware -- what-do-the-parameters-in-the-statistics-represent.md"
  - "raw/assets/manual/user-guide -- preference.md"
  - "raw/assets/manual/user-guide -- preference -- how-to-change-the-default-language.md"
  - "raw/assets/manual/user-guide -- preference -- how-to-set-up-the-web-proxy.md"
  - "raw/assets/manual/user-guide -- preference -- how-to-view-and-change-the-default-shortcuts.md"
  - "raw/assets/manual/user-guide -- preference -- use-with-high-resolution-screen.md"
  - "raw/assets/manual/user-guide -- preference -- save-compressed-project.md"
  - "raw/assets/manual/user-guide -- common-pop-up-windows.md"
  - "raw/assets/manual/user-guide -- resource.md"
  - "raw/assets/manual/user-guide -- view.md"
  - "raw/assets/manual/user-guide -- view -- camera.md"
  - "raw/assets/manual/user-guide -- view -- navigation.md"
  - "raw/assets/manual/user-guide -- view -- display.md"
  - "raw/assets/manual/user-guide -- view -- how-to-set-section-render-section-diagram.md"
  - "raw/assets/manual/user-guide -- view -- how-to-use-parallel-projection.md"
  - "raw/assets/manual/user-guide -- view -- how-to-set-the-depth-of-field-effect.md"
  - "raw/assets/manual/user-guide -- view -- what-is-the-feature-of-horizontal-and-vertical-fov.md"
  - "raw/assets/manual/learn-more -- shortcuts.md"
  - "raw/assets/manual/model -- how-to-import-model-files-into-d5-render.md"
  - "raw/assets/manual/model -- how-to-edit-models.md"
  - "raw/assets/manual/model -- how-to-replace-models-in-the-scene.md"
  - "raw/assets/manual/model -- how-to-sync-update-modified-moved-models-to-d5.md"
tags: [manual, hardware, preference, system, view, camera, shortcuts, model-management]
---

The Hardware Configuration, Preferences, View Controls & Model Management chapter of the D5 Render user manual.

## Hardware

### System Requirements
- **Minimum**: GTX 1060 6GB, Win10 1809+
- **Recommended**: RTX 2060+, 471.68+ driver
- CPU has minimal impact on D5; the software primarily relies on GPU

### GPU Support
- Supports NVIDIA RTX series (RTX 20/30/40/50 series)
- Does not support AMD or Intel integrated graphics

### Diagnostic Tools
- **Hardware Testing**: Automatically checks at startup whether the configuration meets requirements
- **Benchmark**: Hardware testing tool that evaluates rendering performance
- **Support Tool**: Collects system information and logs for technical support
- **Statistics**: Real-time display of frame rate, GPU usage, VRAM usage, and other parameters

### Common Hardware Issues
- Clear up close but blurry in the distance — normal behavior due to Mipmap mechanism
- Abnormal behavior when using D5 remotely — remote desktop usage is not recommended
- Slow scene opening — related to scene size and disk speed

## Preferences

- **Language**: Supports multi-language switching including Chinese/English
- **Network Proxy**: Supports Web proxy configuration
- **Shortcuts**: Supports viewing and modifying default shortcut keys
- **High Resolution Screen**: Supports HiDPI display
- **Compressed Project**: Save compressed projects to reduce file size
- **Render Settings**: HDRI resolution, GI mode, frame generation, etc.
- **Widget**: Manage [[widgets|extension modules]]

## View & Camera

### Camera
- Real camera parameters: exposure, focal length, [[depth-of-field|depth of field]], white balance
- Supports horizontal/vertical FOV switching
- 3.0 adds Free Mode — unifies Walk and Fly modes

### Navigation
- Keyboard + mouse combination controls
- 3.0 supports switching to SketchUp/Rhino/3ds Max navigation presets

### Display
- Multiple preview quality levels
- Wireframe/solid/material display modes

### Special Views
- **Parallel Projection**: Orthographic view
- **Section**: Section rendering/section diagram
- **Depth of Field**: Depth of field effect
- **Full Screen**: Full screen mode

## Model Management

### Import Models
- Supported formats: .d5a, .skp, .3dm, .fbx, .abc
- Can be imported from other modeling software via [[workflow-plugins|workflow plugins]]

### Model Operations
- Align, copy, flip/mirror
- Replace models, sync updates
- Make Unique — create independent copies
- Sync Pivot — synchronize pivot points (for door opening/closing animations)

### Resource Management
- **Object List**: Scene object list for managing models and lights
- **Scene List**: Scene list
- **Layers**: Layer management
- **Imported List**: Imported model list
- **Auto-save**: Automatic save and backup mechanism
- **DRS**: D5 Resource System

## Common Pop-up Windows

- Low TDR detection
- DX12 not supported
- Light count limit exceeded (4096)
- Caustics light count limit exceeded (64)
- Vegetation count limit exceeded
- Emissive limit reached
- Material cannot be reused
