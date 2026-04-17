---
title: Caustics
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- environment -- sky.md"
  - "raw/assets/manual/user-guide -- material -- how-to-achieve-caustics.md"
  - "raw/assets/blog/caustics-in-render.md"
tags: [caustics, light, refraction, reflection, water]
---

Caustics are focused light patterns produced when light refracts or reflects through transparent or reflective surfaces, such as shimmering water surfaces or light spots transmitted through glass. D5 Render supports sun caustics effects.

## Enabling Requirements

Caustics must be **enabled on both the material and light source sides**:

### Light Source Side
Enable in the Caustics option under Geo Sky / Custom Daytime:
- **Caustics Intensity**: Caustics effect intensity multiplier
- **Softness**: Caustics softness level (takes effect when Light Source Radius > 0)

### Material Side
Only the following material templates support caustics:

| Material Template | Reflection Caustics | Refraction Caustics |
|-------------------|---------------------|----------------------|
| Custom | ✓ | — |
| Transparent | ✓ | ✓ |
| Water | ✓ | ✓ |

## Practical Applications

- Shimmering water surface effects
- Light spots transmitted through glass
- Focused light from metal reflections
- Light patterns on swimming pool bottoms

*Sources: [[src-manual-lighting-environment]], [[src-manual-material]]*
