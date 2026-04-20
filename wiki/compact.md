---
title: D5 Render Quick Reference
created: 2026-04-13
updated: 2026-04-20
sources:
  - wiki/entities/
  - wiki/concepts/
tags:
  - compact
  - reference
---

# D5 Render Quick Reference

> One-line definitions of all entity and concept pages. Agents can read this page to build a global understanding of D5 Render, then deep-read specific pages as needed.

## Product & Ecosystem

| Page | Definition |
|------|-----------|
| [[d5-engine]] | D5's proprietary full-path-tracing real-time engine for spatial design, with GPU SOA optimization and cross-platform DX12/Metal shader compiler |
| [[d5-lite]] | Concept exploration tool providing real-time AI visualization inside SketchUp, now powered by D5 Engine (3.0+), supporting AI image-to-image and real-time rendering |
| [[d5-works]] | AEC professional 3D asset platform with integrated online library browsing and downloading, for architecture/engineering/construction industries |
| [[d5-launcher]] | D5 unified launcher integrating project management, workflow plugins, asset browsing, and account management |
| [[d5-for-teams]] | Team collaboration solution with 9 enterprise features: multi-user editing, SSO, team asset library, app integrations |
| [[d5-studio]] | Cloud preset sharing space supporting personal/team spaces for saving environment, material, and effect presets |

## Core Feature Modules

| Page | Definition |
|------|-----------|
| [[real-time-rendering]] | Core feature — providing instant feedback and photorealistic output quality, covering the complete workflow from design to presentation |
| [[ai-capabilities]] | AI automation feature set, providing more efficient creative methods for design and visualization workflows |
| [[asset-tools]] | Asset tools helping users easily achieve natural or structured landscape designs |
| [[environment-and-effects]] | Environment and effects system providing sky, weather, lighting, and professional post-processing effects |
| [[efficiency-tools]] | One-stop scene building toolset covering basic light sources, plant brushes, and other intuitive tools |
| [[camera-and-view]] | Camera and view control system providing simple camera settings and intuitive viewport manipulation |
| [[lighting-system]] | Lighting system with Geo Sky/Custom/HDRI sky + 7 artificial light types + AI lighting assistant |
| [[render-output]] | Render output supporting image/video/panorama, path tracing accumulation, D5 SR super resolution, frame generation |
| [[tools-landscape]] | Landscape and terrain toolset: terrain editing, ocean, scatter, urban generator, Cesium integration, vegetation tools |
| [[workflow-plugins]] | Workflow plugins supporting SketchUp/Rhino/Revit/3ds Max/Blender/ArchiCAD/VectorWorks sync |
| [[virtual-tour]] | Virtual tours in three types: panorama tour, spatial tour (floor plan + waypoints), XR tour (Gaussian Splatting) |
| [[animation-system]] | Animation system with path animation, keyframe animation, phasing animation, and cinematic animation combos |
| [[widgets]] | Extension modules: advanced image/video rendering, color grading, projector light, stage light, section tool, VR, project merge |

## Rendering Concepts

| Page | Definition |
|------|-----------|
| [[pbr-materials]] | Physically-based rendering material system with 10 simplified PBR templates ensuring accurate visual results under all lighting conditions |
| [[global-illumination]] | Global illumination — D5's proprietary real-time path tracing GI (replaced ReSTIR Surfel GI in 2.10+) |
| [[hdri-lighting]] | High dynamic range environment lighting, 32-bit/channel, serving as both background and light source |
| [[displacement-mapping]] | Displacement mapping — 3.0 adds True Displacement for physically displacing geometry (replacing parallax bump) |
| [[caustics]] | Caustic effects requiring enablement on both material and light source sides, for water surface sparkle and glass transmission patterns |
| [[post-processing]] | Post-processing and color grading including exposure/contrast/lens effects/LUT/Color Grading Widget |
| [[volumetric-effects]] | Volumetric effects including volumetric clouds, fog, volumetric light (God Rays), and weather system |
| [[gaussian-splatting]] | 3D Gaussian Splatting technology using Gaussian ellipsoids to represent 3D space, supporting MP4-to-3D and XR Tour |
| [[xr-technology]] | XR extended reality including VR (SteamVR), AR, MR; D5 implements via XR Tour and VR Widget |
| [[depth-of-field]] | Depth of field and bokeh, controlling in-focus area through focal distance and aperture, with keyframe animation support |

## CN — Chinese Market

| Page | Definition |
|------|-----------|
| [[cn-overview]] | Chinese market overview covering company identity, CN-specific features, academic partnerships, community platforms, and licensing |
| [[cn-account]] | CN-specific account details: student edition verification process, invoicing, AI material generation quota (50 uses/community), cloud storage (10GB personal / 100GB team) |
| [[src-cn-news]] | Source summary of 20 CN news articles (2025–2026): D5 3.0/2.11 releases, AI survey, assets, case studies, academic events |
| [[src-cn-manual-account]] | CN manual: account registration, student edition (学信网 verification), invoicing, AI credits |
| [[src-cn-manual-ai]] | CN manual: AI Design Assistant commands, material generation (50 uses/community), atmosphere match, ultra-HD texture, seamless |
| [[src-cn-manual-teams]] | CN manual: Team Edition — org management, multi-user editing, Showreel, SSO, Baidu Netdisk integration, Cesium integration |
| [[src-cn-manual-system]] | CN manual: hardware requirements, GPU driver notes (Win10 + driver compatibility), scene limits (4096 lights, 64 caustic), error messages |
