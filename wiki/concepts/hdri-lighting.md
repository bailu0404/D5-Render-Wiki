---
title: HDRI Lighting
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- environment -- sky.md"
  - "raw/assets/blog/best-free-hdri-download-resources-d5-render.md"
tags: [hdri, sky, lighting, environment]
---

HDRI (High Dynamic Range Image) 照明是 D5 Render 中最常用的自然光照方式 — HDRI 不仅是天空背景，还照亮整个场景，提供真实的环境光照。

## HDRI 原理

### 高动态范围 vs 低动态范围
- **HDRI**: 32 bits/channel，记录极亮和极暗信息，像素值与自然界真实光强成正比
- **LDRI**: 8 bits/channel (JPEG/PNG)，过曝区域丢失细节

### 为什么使用 HDRI
- HDRI 中的太阳可以投射阴影
- 天空细节更丰富（云、蓝天等）
- 材质反射更真实
- 光照效果更自然

## D5 Render 中的 HDRI

### 选择 HDRI 的标准
- 球形投影全景图
- 图像长宽比 2:1
- 地平线通常在画面中间高度

### HDRI 参数
| 参数 | 说明 |
|------|------|
| Light | 整体亮度，分别控制 Skylight（漫反射光）和 Background（背景/反射） |
| Rotate | 水平旋转 HDRI 环境 |
| Flip Horizontal | 水平翻转 |
| Sky Temperature | 天空色温，默认 6500K |
| Sky Color | 色相和饱和度调整 |
| HDRI Resolution | 2K/4K/8K/实际分辨率/自适应 |

### HDRI 分辨率控制
- **Adaptive (推荐)**: 视口压缩至 2K 提升帧率，渲染输出支持至 8K
- 更高分辨率消耗更多显存

*来源: [[src-manual-lighting-environment]], [[src-blog-lighting-environment]]*
