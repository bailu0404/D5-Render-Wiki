---
title: XR Technology
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/blog/what-is-xr-d5-render-xr-technology-architecture.md"
  - "raw/assets/blog/d5-render-3-0-ai-rendering-design-workflow.md"
tags: [xr, vr, ar, mixed-reality, spatial]
---

XR (Extended Reality) 是 VR、AR 和 MR 的统称，D5 Render 通过 [[virtual-tour|XR Tour]] 功能将渲染场景转换为可在浏览器/VR 设备中自由探索的沉浸式体验。

## XR 技术构成

### VR (Virtual Reality)
- 完全虚拟的沉浸式体验
- D5 支持 SteamVR 设备 (HTC Vive, Oculus Rift)
- 通过 [[widgets|VR Widget]] 启用

### AR (Augmented Reality)
- 虚拟内容叠加到真实世界
- 通过移动设备查看

### MR (Mixed Reality)
- 虚实融合的交互体验

## D5 Render 的 XR 实现

### XR Tour
- 基于 [[gaussian-splatting|3D Gaussian Splatting]] 技术
- 场景转换为高保真 3D 空间
- 浏览器端自由探索
- 支持导入 3D 扫描数据

### 技术优势
- 比 Panorama Tour 更自由的视角
- 比 Spatial Tour 更真实的 3D 感
- 视觉清晰度和性能优于传统摄影测量
- 适合客户演示和远程协作

*来源: [[src-blog-virtual-tour-xr]]*
