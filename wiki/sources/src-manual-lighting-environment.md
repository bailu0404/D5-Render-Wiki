---
title: "Manual: Lighting & Environment"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- lights.md"
  - "raw/assets/manual/user-guide -- lights -- what-types-of-light-sources-are-offered-by-d5.md"
  - "raw/assets/manual/user-guide -- lights -- what-are-the-meanings-of-each-parameter-in-the-light-panel.md"
  - "raw/assets/manual/user-guide -- lights -- how-to-edit-multiple-lights-at-once.md"
  - "raw/assets/manual/user-guide -- lights -- how-to-make-a-light-invisible-in-the-reflection.md"
  - "raw/assets/manual/user-guide -- lights -- other-faqs.md"
  - "raw/assets/manual/user-guide -- environment.md"
  - "raw/assets/manual/user-guide -- environment -- sky.md"
  - "raw/assets/manual/user-guide -- environment -- weather.md"
  - "raw/assets/manual/user-guide -- environment -- other-common-issues.md"
  - "raw/assets/manual/user-guide -- effect.md"
  - "raw/assets/manual/user-guide -- effect -- how-is-ao-used-in-style.md"
  - "raw/assets/manual/user-guide -- effect -- how-is-z-depth-used-in-style.md"
  - "raw/assets/manual/user-guide -- effect -- how-to-use-lut.md"
  - "raw/assets/manual/user-guide -- effect -- what-effects-can-each-of-the-parameters-in-post-processing-achieve.md"
  - "raw/assets/manual/user-guide -- effect -- how-to-save-and-reuse-environment-and-post-effect-presets.md"
tags: [manual, lighting, environment, sky, hdri, weather, effect, post-processing]
---

The Lighting, Environment & Effects chapter of the D5 Render user manual, covering 7 light source types, the sky system, weather effects, and post-processing parameters.

## Light Source Types

D5 Render offers 7 types of light sources:

### Basic Lights
1. **Point Light** — Point light source, simulates a light bulb, emits light uniformly in all directions
2. **Spotlight** — Spotlight, emits light within a cone angle, supports IES files
3. **Strip Light** — Strip light, adjustable length and width, with Barn Door light blockers
4. **Rect Light** — Rectangular area light, simulates a rectangular emissive area

### Extended Lights
5. **Disc Light** — Disc light, soft and uniform illumination
6. **Stage Light** — Stage light (Widget), supports gobos, prism splitting, and smoke effects
7. **Projector** — Projector light (Widget), supports image/video projection

## Common Light Parameters

| Parameter | Description |
|-----------|-------------|
| Intensity | Emission intensity, unit cd (candela), maximum 8,000,000 |
| Attenuation Radius | Attenuation radius; lighting calculations stop beyond this range |
| Visible in Reflection | Controls whether the light source appears in reflections |
| Temperature | Color temperature (K); 3000K is warm/yellow, 5500-6500K is neutral white, 8000K is cool/blue |
| Color | Custom light source color |

### Special Parameters
- **Point Light**: Light source radius (affects shadow softness)
- **Spotlight**: IES file, cone angle
- **Strip/Rect Light**: Barn Door Angle (0-90 degrees) and Barn Door Length (0-100)
- **Stage Light**: Gobo, prism splitting, rotation, smoke
- **Projector**: Projected image/video, UV control, mist effect

## Sky System

### Geo Sky
Accurately simulates sun angles based on geographic location:
- **North Offset**: Corrects the north direction
- **Time / Date**: Time and date
- **Latitude / Longitude**: Latitude and longitude coordinates (decimal degrees)
- **Custom Parameters**: Sun intensity, sun disk radius, moonlight intensity, moon disk radius, starlight intensity
- **[[caustics|Caustics]]**: Sun caustics, requires enabling on both the material and light source sides

### Custom Sky
- Daytime: Sun intensity, elevation angle, azimuth, caustics
- Nighttime: Moonlight intensity, moon disk radius, moon phase, moon phase direction, elevation angle, azimuth, starlight intensity

### HDRI

[[hdri-lighting|HDRI]] (High Dynamic Range Image) is not just a background — it also illuminates the entire scene:
- **Light**: Overall brightness control, separately adjusts Skylight (diffuse light) and Background (background brightness)
- **Rotate**: Rotate the HDRI environment
- **Flip Horizontal**: Flip horizontally
- **Sky Temperature**: Sky color temperature, default 6500K
- **Sky Color**: Hue and saturation adjustments
- **HDRI Resolution**: Supports 2K, 4K, 8K, and native resolution

## Weather Effects

- **Fog**: Fog effect, supports volumetric lighting
- **Rain**: Rain effect
- **Snow**: Snow effect
- **Volumetric Cloud**: Volumetric clouds (3.0+), supports presets and density/altitude adjustments

## Post-Processing Effects

### AO (Ambient Occlusion)
Used in the Style panel to enhance shadow details in corners and crevices.

### Z-Depth
Used in the Style panel for depth-based effect control.

### LUT
Lookup table color grading, supports custom LUT files.

### Post-Processing Parameters
- **Exposure**: Exposure
- **Contrast**: Contrast
- **Highlight / Shadow**: Highlights/shadows
- **White Balance**: White balance
- **Vignette**: Vignette
- **Chromatic Aberration**: Chromatic aberration
- **Bloom**: Bloom
- **Color Grading** (Widget): Precise control over midtones, shadows, highlights, and global tone
