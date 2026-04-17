---
title: Volumetric Effects
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- environment -- weather.md"
  - "raw/assets/blog/volumetric-clouds-sky-replacement.md"
  - "raw/assets/blog/how-to-realistic-fog-archviz-rendering-d5render.md"
tags: [volumetric, fog, cloud, weather, atmosphere]
---

Volumetric Effects are techniques in D5 Render that simulate atmospheric phenomena, including volumetric fog, volumetric clouds, and volumetric light, adding depth and atmosphere to scenes.

## Volumetric Cloud

Core upgrade in the 3.0 weather system:
- Goes beyond simple backgrounds, providing hyper-realistic depth and flexible visual control
- Precise presets: Cumulus, Stratocumulus, etc.
- Adjustable density and altitude to match precise artistic intent
- Freely sculpt sky formations

## Fog

Fog upgrade in version 3.0:
- Independent color and density controls
- New "Follow Sunlight" option
- Ensures natural depth and realistic light scattering effects
- Maintains realism regardless of time of day

## Volumetric Light

When fog is enabled, lights passing through the fog produce visible volumetric light beams (God Rays):
- Suitable for indoor/outdoor atmosphere creation
- Requires enabling fog first in Environment > Weather > Fog

## Weather System

D5 Render's weather effects include:
- **Fog**: Fog effect, enhances spatial depth
- **Rain**: Rainy weather, raindrop particle effects
- **Snow**: Snow scene, falling snowflakes
- **Volumetric Cloud**: Volumetric clouds, atmospheric layer effects

*Sources: [[src-manual-lighting-environment]], [[src-blog-lighting-environment]]*
