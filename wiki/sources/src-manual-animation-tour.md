---
title: "Manual: Animation & Virtual Tour"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- animation-path.md"
  - "raw/assets/manual/user-guide -- animation-path -- character-path.md"
  - "raw/assets/manual/user-guide -- animation-path -- draw-path.md"
  - "raw/assets/manual/user-guide -- animation-path -- vehicle-path.md"
  - "raw/assets/manual/user-guide -- d5-virtual-tour.md"
  - "raw/assets/manual/user-guide -- d5-virtual-tour -- d5-showreel.md"
  - "raw/assets/manual/user-guide -- d5-virtual-tour -- panorama-tour.md"
  - "raw/assets/manual/user-guide -- d5-virtual-tour -- spatial-tour.md"
  - "raw/assets/manual/user-guide -- d5-virtual-tour -- xr-tour.md"
  - "raw/assets/manual/user-guide -- d5-virtual-tour -- d5-render-tour-editor.md"
tags: [manual, animation, virtual-tour, panorama, xr, keyframe]
---

D5 Render 用户手册的动画与虚拟漫游章节，涵盖动画路径、关键帧和三种虚拟漫游类型。

## 动画路径

### Draw Path（绘制路径）
自由绘制路径，用于物体沿路径运动。

### Character Path（人物路径）
人物沿指定路径行走，支持多人物动画。

### Vehicle Path（车辆路径）
车辆沿路径行驶，支持运动模糊效果。

## 虚拟漫游

### Panorama Tour（全景漫游）
将 360° 全景图转为可分享链接，适合快速客户更新。

### Spatial Tour（空间漫游）
集成平面图并设置特定航点，引导观者按结构化叙事浏览空间。

### XR Tour（XR 漫游）
基于 [[gaussian-splatting|3D Gaussian Splatting]] 技术，将场景转换为高保真 3D 空间：
- 支持浏览器自由探索
- 支持 `.ply` 和 `.gs` 文件导入
- 3D 扫描项目可直接导入场景

### D5 Showreel
展示平台，管理和编辑漫游项目。

### Tour Editor
漫游编辑器，统一管理全景、空间和 XR 漫游项目。
