---
title: Post-Processing
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- effect.md"
  - "raw/assets/blog/color-grading-d5-effect-panel-guide.md"
  - "raw/assets/blog/one-click-3d-post-processing-d5-render.md"
  - "raw/assets/blog/postprocessing-vignette-chromatic-aberration-for-photorealistic-3d-rendering.md"
tags: [post-processing, effect, lut, vignette, bloom, color-grading]
---

Post-Processing is the system in D5 Render for adjusting tone, lens effects, and artistic style of rendered results, helping elevate renders from a "digital" to a "photographic" quality.

## Effect Panel Parameters

### Basic Adjustments
- **Exposure**: Exposure level
- **Contrast**: Contrast
- **Highlight / Shadow**: Highlight/shadow control
- **White Balance**: White balance

### Lens Effects
- **Bloom**: Bloom/glow effect, simulates highlight overflow
- **Vignette**: Vignette, natural darkening at edges
- **Chromatic Aberration**: Chromatic aberration, simulates color separation at lens edges

### Stylization
- **AO**: Ambient occlusion enhancement
- **Z-Depth**: Depth-based effects
- **Outline Mode**: Outline mode

## LUT (Look-Up Table)

- Apply preset or custom color grading
- Change the overall tone style with one click
- Supports standard LUT formats such as .cube

## Color Grading (Widget)

[[widgets|Color Grading Widget]] provides more precise tone control:
- **Midtones**: Midtone tint
- **Shadows**: Shadow tint
- **Highlights**: Highlight tint
- **Global**: Global tint

## Preset Saving

Environment and post-processing presets can be saved and reused via [[d5-studio|D5 Studio]]:
- Save to My Space (personal) or Team Space (team)
- Option to save effects only (without environment information)

*Sources: [[src-manual-lighting-environment]], [[src-blog-camera-rendering]]*
