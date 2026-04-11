---
title: Gaussian Splatting
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/blog/gaussian-splatting-mp4-to-3d.md"
  - "raw/assets/blog/d5-render-3-0-ai-rendering-design-workflow.md"
tags: [gaussian-splatting, 3d-scan, xr, point-cloud]
---

3D Gaussian Splatting 是一种新兴的 3D 场景表示技术，通过数百万个带有颜色和透明度的高斯椭球体重建真实场景，比传统摄影测量更快速、更清晰。D5 Render 3.0 原生支持此技术。

## 技术原理

- 用大量高斯椭球体 (Gaussians) 表示 3D 空间
- 每个高斯体具有: 位置、颜色、透明度、尺寸、旋转
- 从视频/照片中自动提取并优化
- 渲染速度快于传统点云/网格方法

## D5 Render 中的支持

### MP4 转 3D
- 上传 MP4 视频自动生成 3D Gaussian Splatting 场景
- 适合快速获取场地现状 3D 模型

### 文件导入
- 支持 `.ply` 格式文件
- 支持 `.gs` 格式文件
- 3D 扫描项目可直接导入 D5 Render 场景

### XR Tour 集成
- [[virtual-tour|XR Tour]] 使用 Gaussian Splatting 技术
- 将场景转换为高保真 3D 空间
- 客户可在浏览器中自由探索
- 视觉更清晰，性能更流畅

## 应用场景

- 场地现状 3D 扫描导入
- 建筑周边环境建模
- 室内空间数字化
- 沉浸式虚拟漫游

*来源: [[src-blog-virtual-tour-xr]]*
