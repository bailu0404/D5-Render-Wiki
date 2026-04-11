---
title: Virtual Tour
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- d5-virtual-tour.md"
  - "raw/assets/blog/how-to-create-virtual-tour-with-d5-render.md"
  - "raw/assets/blog/what-is-xr-d5-render-xr-technology-architecture.md"
tags: [virtual-tour, panorama, xr, gaussian-splatting, presentation]
---

Virtual Tour 是 D5 Render 的交互式展示系统，提供全景漫游、空间漫游和 XR 漫游三种方式，让设计方案以沉浸式方式呈现给客户。

## 三种漫游类型

### Panorama Tour（全景漫游）
- 将 360° 全景图转为可分享的 Web 链接
- 适合快速客户更新
- 速度优先

### Spatial Tour（空间漫游）
- 集成平面图，设置特定航点
- 引导观者按结构化叙事浏览空间
- 提供清晰的空间上下文

### XR Tour（XR 漫游）
- 基于 [[gaussian-splatting|3D Gaussian Splatting]] 技术
- 将场景转换为高保真 3D 空间
- 客户可在浏览器中自由探索空间
- 支持导入 `.ply` 和 `.gs` 文件
- 3D 扫描项目可直接导入场景

## D5 Showreel

- 展示平台，管理和发布漫游项目
- 3.0 版本集成到 MySpace 侧边栏
- 统一管理个人资料和漫游项目

## Tour Editor

- 漫游编辑器，统一管理所有漫游类型
- 3.0 版本已集成到核心界面

*来源: [[src-manual-animation-tour]], [[src-blog-virtual-tour-xr]]*
