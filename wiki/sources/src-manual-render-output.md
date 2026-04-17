---
title: "Manual: Render & Output"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- render.md"
  - "raw/assets/manual/user-guide -- render -- how-to-render-a-scene.md"
  - "raw/assets/manual/user-guide -- render -- how-to-render-a-video-clip.md"
  - "raw/assets/manual/user-guide -- render -- how-to-render-channel-maps.md"
  - "raw/assets/manual/user-guide -- render -- what-is-d5-sr.md"
  - "raw/assets/manual/user-guide -- render -- what-is-real-time-path-tracing.md"
  - "raw/assets/manual/user-guide -- render -- what-is-fsr-frame-generation.md"
  - "raw/assets/manual/user-guide -- render -- what-is-the-fps-booster-for-complex-geometry.md"
  - "raw/assets/manual/user-guide -- render -- where-can-i-activate-frame-generation.md"
tags: [manual, render, output, path-tracing, sr, video]
---

The Render & Output chapter of the D5 Render user manual, covering image/video rendering, real-time path tracing, super-resolution, and frame generation technologies.

## Render Modes

Render modes record output format, resolution, channel settings, and other parameters, and are automatically applied when entering the mode next time.

### Image Rendering
- Supports single-frame image and panoramic image output
- Selectable resolution and format
- Supports channel map output (normal, depth, reflection, etc.)

### Video Rendering
- Supports animation keyframe parameter settings
- Output formats: MP4, AVI
- Sequence frames support PNG, EXR

### Render Queue
Batch rendering feature that can render multiple render tasks at once.

## Real-time Path Tracing

D5's proprietary [[global-illumination|Global Illumination (GI)]] technology solution, optimizing real-time rendering + image/video output.

### Preferences
- **Legacy D5 GI Compatible Mode**: Enables D5 version 2.9's ReSTIR Surfel GI to maintain visual consistency with older scenes

### Accumulation (Shortcut Key F4)
- When enabled, pixel samples continue to accumulate until the final output quality is reached
- Moving the camera or pressing ESC terminates accumulation

### Custom Parameters
| Parameter | Description |
|-----------|-------------|
| GI Precision | GI precision level, 3 levels; higher levels produce more accurate GI but slower convergence |
| Refl. Depth | Number of light bounces between highly reflective surfaces |
| SPP | Samples per pixel; increasing this reduces artifacts |
| Roughness Limit | Roughness upper limit, default 0.5; higher values make accumulation more accurate |

### Key Improvements in the New GI
1. **Improved GI Cache**: Path tracing calculates and caches light bounces, improving cache quality
2. **Optimized GI Bounce Details**: More accurate at wall-floor junctions and similar details
3. **Unbiased Sampling and Visibility Detection**: Indirect lighting closer to ground truth
4. **Optimized Vegetation and Cloth Materials**: Fixes color attenuation issues in light transport

## D5 SR (Super Resolution)

D5's proprietary super-resolution technology, enhancing rendered image resolution and quality.

## Frame Generation

- Based on FSR (FidelityFX Super Resolution) technology
- Improves real-time preview frame rate
- Can be enabled in Preferences

## FPS Booster

A frame rate optimization tool for complex geometry, improving performance while maintaining visual quality.
