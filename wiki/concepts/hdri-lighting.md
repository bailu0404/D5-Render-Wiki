---
title: HDRI Lighting
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- environment -- sky.md"
  - "raw/assets/blog/best-free-hdri-download-resources-d5-render.md"
tags: [hdri, sky, lighting, environment]
---

HDRI (High Dynamic Range Image) lighting is the most commonly used natural lighting method in D5 Render — an HDRI serves not only as a sky background but also illuminates the entire scene, providing realistic environmental lighting.

## HDRI Principles

### High Dynamic Range vs Low Dynamic Range
- **HDRI**: 32 bits/channel, captures extremely bright and dark information, pixel values are proportional to real-world light intensity
- **LDRI**: 8 bits/channel (JPEG/PNG), loses detail in overexposed areas

### Why Use HDRI
- The sun in an HDRI can cast shadows
- Richer sky details (clouds, blue sky, etc.)
- More realistic material reflections
- More natural lighting effects

## HDRI in D5 Render

### Criteria for Selecting HDRI
- Spherical projection panoramic image
- Image aspect ratio 2:1
- Horizon typically at the vertical center of the image

### HDRI Parameters
| Parameter | Description |
|-----------|-------------|
| Light | Overall brightness; separately controls Skylight (diffuse light) and Background (background/reflections) |
| Rotate | Horizontally rotates the HDRI environment |
| Flip Horizontal | Horizontally flips the image |
| Sky Temperature | Sky color temperature, default 6500K |
| Sky Color | Hue and saturation adjustment |
| HDRI Resolution | 2K/4K/8K/actual resolution/adaptive |

### HDRI Resolution Control
- **Adaptive (recommended)**: Viewport compressed to 2K for better frame rate, render output supports up to 8K
- Higher resolutions consume more VRAM

*Sources: [[src-manual-lighting-environment]], [[src-blog-lighting-environment]]*
