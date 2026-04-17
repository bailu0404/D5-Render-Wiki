---
title: XR Technology
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/blog/what-is-xr-d5-render-xr-technology-architecture.md"
  - "raw/assets/blog/d5-render-3-0-ai-rendering-design-workflow.md"
tags: [xr, vr, ar, mixed-reality, spatial]
---

XR (Extended Reality) is the umbrella term for VR, AR, and MR. D5 Render converts rendered scenes into immersive experiences that can be freely explored in browsers/VR devices through the [[virtual-tour|XR Tour]] feature.

## XR Technology Components

### VR (Virtual Reality)
- Fully virtual immersive experience
- D5 supports SteamVR devices (HTC Vive, Oculus Rift)
- Enabled via [[widgets|VR Widget]]

### AR (Augmented Reality)
- Virtual content overlaid onto the real world
- Viewed through mobile devices

### MR (Mixed Reality)
- Interactive experience blending virtual and real elements

## XR Implementation in D5 Render

### XR Tour
- Based on [[gaussian-splatting|3D Gaussian Splatting]] technology
- Converts scenes into high-fidelity 3D spaces
- Free exploration in the browser
- Supports importing 3D scan data

### Technical Advantages
- Freer viewpoint than Panorama Tour
- More realistic 3D feel than Spatial Tour
- Visual clarity and performance superior to traditional photogrammetry
- Suitable for client presentations and remote collaboration

*Sources: [[src-blog-virtual-tour-xr]]*
