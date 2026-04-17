---
title: Global Illumination
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- render -- what-is-real-time-path-tracing.md"
  - "raw/assets/blog/d5-render-global-illumination.md"
  - "raw/assets/blog/advanced-d5-gi-ground-truth.md"
  - "raw/assets/blog/d5-render-2-10-real-time-path-tracing.md"
tags: [gi, path-tracing, rendering, lighting]
---

Global Illumination (GI) is a rendering technique that simulates multiple light bounces within a scene, making indirect lighting effects (such as color bleed and reflected light) appear realistic and convincing. D5 Render employs its proprietary real-time path tracing GI solution.

## D5 Render GI Technology Evolution

### ReSTIR Surfel GI (2.9)
The GI solution used in D5 Render version 2.9, based on the ReSTIR sampling algorithm and Surfel caching.

### Real-time Path Tracing (2.10+)
Version 2.10 introduced an entirely new path tracing GI:
- **Improved GI Cache**: Path tracing computes and caches light bounces, improving cache quality
- **Correct Rendering of Highly Reflective Surfaces**: The issue of inaccurate/darkened metal floor reflections in 2.9 has been resolved
- **Optimized GI Bounce Details**: More accurate details at wall-floor junctions, etc.
- **Unbiased Sampling**: Indirect lighting closer to Ground Truth
- **Optimized Vegetation/Fabric Materials**: Fixed color attenuation issues

## Custom GI Parameters

| Parameter | Description |
|-----------|-------------|
| GI Precision | GI precision level (3 tiers); higher levels are more accurate but converge more slowly |
| Refl. Depth | Number of light bounces between highly reflective surfaces |
| SPP | Samples per pixel; increasing this reduces artifacts and improves detail |
| Roughness Limit | Upper limit for roughness calculation, default 0.5 |

## Accumulation Mode

Press F4 to enable accumulation mode, where pixel samples continuously accumulate until final output quality is reached. Moving the camera or pressing ESC terminates accumulation.

## Legacy GI Compatibility Mode

Enable "Legacy D5 GI Compatible Mode" in Preference > Rendering to use the ReSTIR Surfel GI from version 2.9 for visual consistency with older scenes. This option is for compatibility purposes only and will be removed in a future version.

*Sources: [[src-manual-render-output]], [[src-blog-camera-rendering]]*
