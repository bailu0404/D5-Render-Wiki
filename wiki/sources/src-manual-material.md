---
title: "Manual: Material System"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- material.md"
  - "raw/assets/manual/user-guide -- material -- car-paint.md"
  - "raw/assets/manual/user-guide -- material -- cloth.md"
  - "raw/assets/manual/user-guide -- material -- custom-alpha.md"
  - "raw/assets/manual/user-guide -- material -- displacement.md"
  - "raw/assets/manual/user-guide -- material -- foliage.md"
  - "raw/assets/manual/user-guide -- material -- grass.md"
  - "raw/assets/manual/user-guide -- material -- transparent.md"
  - "raw/assets/manual/user-guide -- material -- water.md"
  - "raw/assets/manual/user-guide -- material -- video.md"
  - "raw/assets/manual/user-guide -- material -- velvet.md"
  - "raw/assets/manual/user-guide -- material -- how-to-achieve-caustics.md"
  - "raw/assets/manual/user-guide -- material -- how-to-achieve-round-corner.md"
  - "raw/assets/manual/user-guide -- material -- how-to-control-the-bump-effect.md"
  - "raw/assets/manual/user-guide -- material -- how-to-control-the-reflection-effect.md"
  - "raw/assets/manual/user-guide -- material -- how-to-make-the-emissive-effect.md"
  - "raw/assets/manual/user-guide -- material -- what-is-invisible-in-raytracing.md"
  - "raw/assets/manual/user-guide -- material -- how-to-adjust-the-material-map.md"
  - "raw/assets/manual/user-guide -- material -- how-do-i-adjust-the-material-uv.md"
  - "raw/assets/manual/user-guide -- material -- what-materials-are-the-subsurface-scattering-templates-suitable-for.md"
  - "raw/assets/manual/user-guide -- material -- what-materials-are-the-flowing-water-templates-suitable-for.md"
tags: [manual, material, pbr, texture, uv, displacement]
---

The Material System chapter of the D5 Render user manual, covering 10 material templates, texture map channels, UV controls, and template-specific parameters.

## Material Parameters Panel

Select a material by clicking on the model surface or using the Material Picker tool (shortcut key `I`); the right panel displays the material inspector.

### Basic Tools
- **Duplicate**: Copy current material parameters
- **Add to local**: Add the material to the local library
- **Reset**: Restore material parameters to their initial state

## 10 Material Templates

1. **Custom** — Custom template with full PBR parameter control
2. **Transparent** — Transparent material (glass, etc.), supports [[caustics|caustics]]
3. **Water** — Water material with flowing animation effects
4. **Displacement** — [[displacement-mapping|Displacement map]] material
5. **Foliage** — Vegetation material, supports subsurface scattering
6. **Grass** — Grass material
7. **Cloth** — Cloth material
8. **Car Paint** — Car paint material with clear coat layer
9. **Video** — Video material, supports mp4 and other formats
10. **Custom Alpha** — Custom transparency material

## Core Texture Map Channels

### Base Color / Base Color Map
- Non-metallic (Metallic=0): Diffuse color
- Metallic (Metallic=1): Reflection color
- Map and solid color are blended in Multiply mode; use solid color white to preserve the map's original colors
- Detailed parameters: Invert, Contrast, Hue, Saturation, Brightness, Independent UV

### Normal
- Normal map creates surface bump/indentation effects
- D5 automatically generates normal information from the Base Color Map
- Supports normal strength adjustment (can be negative to flip bumps/indentations)

### Specular
- Controls non-metallic reflectance (F0)
- Specular 0 to 1 corresponds to F0 0% to 8%
- Water is 0.25, glass/plastic approximately 0.5, gemstones are 1

### Roughness
- Surface micro-roughness, affecting reflection blurriness
- Roughness is the inverse of Glossiness

### Metallic
- Core parameter of the PBR metalness/roughness workflow
- 0 = non-metallic, 1 = metallic
- Values between 0 and 1 are used for mixed materials such as rust, dust, etc.

### AO
- Ambient occlusion channel, multiplied with Base Color to enhance shadows in corners and crevices
- AO Multiplier range 0-1

### Emissive
- Material self-illumination
- Parameters: Intensity, Color, Cast Shadow toggle

## UV Controls

Global UV parameters:
- **Stretch**: Stretch texture along the UV direction
- **Offset**: UV offset
- **Rotate**: Texture rotation (0-360 degrees)
- **Triplanar**: Triplanar mapping for complex objects
- **Blend Amount**: Triplanar seam blending

## Special Material Template Parameters

### Water Template
- Features flowing animation effects
- Special parameters: Flow Velocity, Depth (controls light absorption)
- Specular is fixed at 0.25, IOR is fixed at 1.33
- The water surface model must be single-sided; a plane below is needed as the water bottom

### Displacement Template
- Supports Parallax and True Displacement modes
- True Displacement parameters: Subdivision Level, Vertical Offset, Maintain Continuity, Remesh
- Supports Opacity Map for cutout effects

### SSS (Subsurface Scattering) Template
- Suitable for translucent materials such as skin, wax, jade, etc.
- Special parameters: Subsurface Color, Scatter Radius

## Invisible in Raytracing

When checked, the material does not participate in lighting (diffuse) calculations. It is visible to the camera and in reflections, but does not cast shadows or bounce light. When Emissive is enabled, self-illumination similarly does not participate in GI calculations.
