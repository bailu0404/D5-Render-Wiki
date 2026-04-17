---
title: Render Output
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- render.md"
  - "raw/assets/manual/user-guide -- render -- what-is-real-time-path-tracing.md"
  - "raw/assets/manual/user-guide -- render -- what-is-d5-sr.md"
  - "raw/assets/manual/user-guide -- render -- what-is-fsr-frame-generation.md"
  - "raw/assets/blog/d5-super-resolution-image-rendering.md"
  - "raw/assets/blog/d5-render-2-10-real-time-path-tracing.md"
tags: [render, output, path-tracing, sr, video, image]
---

D5 Render's render output system supports images, videos, and interactive presentations, combining in-house real-time path tracing and super-resolution technology to balance speed and quality.

## Render Modes

When entering render mode, output format, resolution, channel settings, and other parameters are automatically recorded and applied next time.

### Image Rendering
- Single-frame images and panoramas
- Supports multi-channel output (normal, depth, reflection, etc.)
- [[widgets|Advanced Image Rendering Widget]] supports PNG/JPG/TGA/TIF/EXR formats

### Video Rendering
- Supports animation keyframes and path animation
- Output formats: MP4, AVI
- Image sequences: PNG, EXR (with channel selection)
- [[widgets|Advanced Video Rendering Widget]] provides more encoding options

### Render Queue
Batch render multiple tasks.

## Real-time Path Tracing

D5's in-house [[global-illumination|real-time path tracing]] technology:
- **Accumulation (F4)**: Pixel accumulation to final output quality
- **GI Precision**: 3-level precision control
- **Refl. Depth**: Reflection bounce count
- **SPP**: Samples per pixel
- **Roughness Limit**: Roughness calculation upper limit

### New GI Improvements
- Path tracing cache improves reflection quality
- More accurate GI bounce details
- Unbiased sampling approaching ground truth
- Optimized vegetation/fabric color models

## D5 SR (Super Resolution)

In-house super-resolution technology that enhances render resolution and detail.

## Frame Generation

Based on FSR technology, boosts real-time preview frame rate.

## FPS Booster

Frame rate optimization for complex geometry, improving performance while maintaining visual quality.

*Sources: [[src-manual-render-output]], [[src-blog-camera-rendering]]*
