---
title: Gaussian Splatting
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/blog/gaussian-splatting-mp4-to-3d.md"
  - "raw/assets/blog/d5-render-3-0-ai-rendering-design-workflow.md"
tags: [gaussian-splatting, 3d-scan, xr, point-cloud]
---

3D Gaussian Splatting is an emerging 3D scene representation technique that reconstructs real-world scenes using millions of Gaussian ellipsoids with color and transparency, delivering faster and clearer results than traditional photogrammetry. D5 Render 3.0 natively supports this technology.

## Technical Principles

- Represents 3D space with a large number of Gaussian ellipsoids (Gaussians)
- Each Gaussian has: position, color, transparency, size, rotation
- Automatically extracted and optimized from video/photos
- Rendering is faster than traditional point cloud/mesh methods

## Support in D5 Render

### MP4 to 3D
- Upload an MP4 video to automatically generate a 3D Gaussian Splatting scene
- Ideal for quickly capturing the current site conditions as a 3D model

### File Import
- Supports `.ply` format files
- Supports `.gs` format files
- 3D scan projects can be directly imported into D5 Render scenes

### XR Tour Integration
- [[virtual-tour|XR Tour]] uses Gaussian Splatting technology
- Converts scenes into high-fidelity 3D spaces
- Clients can freely explore in the browser
- Clearer visuals and smoother performance

## Application Scenarios

- 3D scan import of existing site conditions
- Modeling of surroundings around buildings
- Digitalization of interior spaces
- Immersive virtual walkthroughs

*Sources: [[src-blog-virtual-tour-xr]]*
