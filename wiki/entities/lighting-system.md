---
title: Lighting System
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- lights.md"
  - "raw/assets/manual/user-guide -- lights -- what-types-of-light-sources-are-offered-by-d5.md"
  - "raw/assets/manual/user-guide -- lights -- what-are-the-meanings-of-each-parameter-in-the-light-panel.md"
  - "raw/assets/manual/user-guide -- environment -- sky.md"
  - "raw/assets/blog/d5-render-smart-lighting-system-guide.md"
  - "raw/assets/blog/4-best-tips-of-realistic-environmental-lighting-for-architecture.md"
tags: [lighting, sky, hdri, lights, gi]
---

D5 Render's lighting system comprises two major systems — natural light (sky system) and artificial light sources — combined with [[global-illumination|Global Illumination]] technology for realistic lighting.

## Sky System

### Geo Sky
Precisely simulates sun angles based on geographic location, supports latitude/longitude, time, and date input, and can correct north offset.

### Custom
Manually set sun/moon altitude angle and azimuth angle; customize celestial body parameters.

### HDRI
[[hdri-lighting|HDRI]] serves as both background and light source, supporting rotation, flipping, color temperature/hue adjustment, and resolution control (2K/4K/8K/Actual).

## Artificial Light Sources

D5 Render provides 7 light source types:

| Light Source | Use Case | Special Parameters |
|--------------|----------|--------------------|
| Point Light | Simulates light bulbs | Light source radius |
| Spotlight | Spotlight | IES file, cone angle |
| Strip Light | Strip light | Barn Door |
| Rect Light | Rectangular area light | Barn Door |
| Disc Light | Disc light | — |
| Stage Light | Stage light | Gobo, prism, smoke |
| Projector | Projector light | Image/video projection |

### Common Parameters
- **Intensity**: 0~8,000,000 cd
- **Attenuation Radius**: Light attenuation range
- **Temperature**: 3000K~8000K color temperature
- **Color**: Custom color
- **Visible in Reflection**: Visibility in reflections

## AI Lighting Assistance

D5 3.0's AI Agent provides light source adjustment assistance:
- Adjust light source parameters with natural language commands
- Automatically optimize scene lighting
- Supports area lighting optimization and overexposure prevention

*Sources: [[src-manual-lighting-environment]], [[src-blog-lighting-environment]]*
