---
title: Displacement Mapping
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- material -- displacement.md"
  - "raw/assets/blog/displacement-maps-material-d5-render.md"
  - "raw/assets/blog/a-quick-easy-way-to-make-displacement-texture.md"
tags: [displacement, material, texture, height-map]
---

Displacement Mapping modifies the model's geometry to represent realistic surface bump details, providing more authentic surface effects than Normal Maps and Parallax mapping.

## Two Modes

### Parallax
The previous default bump solution in D5 Render, which simulates depth through visual illusion without modifying geometry.

### True Displacement
Newly added in version 3.0, physically displaces geometry using a height map:
- White = raised areas
- Black = recessed areas

## True Displacement Parameters

| Parameter | Description |
|-----------|-------------|
| Subdivision Level | Mesh subdivision level; higher values produce finer detail but increase polygon count and render time |
| Vertical Offset | Vertical offset, compensates for model floating or intersection after displacement |
| Maintain Continuity | Keeps the model's solid structure closed and intact |
| Remesh | Rebuilds the mesh for models with poor topology |

> Note: Higher subdivision levels achieve finer results but increase model polygon count, memory usage, and render time. Excessive use may cause crashes.

## Opacity Map

The Displacement material template now includes an opacity map for cutout effects:
- Suitable for hedges, fences, woven bamboo surfaces, etc.
- Precise control over material cutouts

## Limitations

- LiveSync models do not support True Displacement (UI toggle is disabled)
- To use True Displacement, the model must be converted to a non-real-time sync model

*Sources: [[src-manual-material]], [[src-blog-materials-textures]]*
