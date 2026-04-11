---
title: "Manual: Render & Output"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- render.md"
  - "raw/assets/manual/user-guide -- render -- how-to-render-a-scene.md"
  - "raw/assets/manual/user-guide -- render -- how-to-render-a-video-clip.md"
  - "raw/assets/manual/user-guide -- render -- how-to-render-channel-maps.md"
  - "raw/assets/manual/user-guide -- render -- what-is-d5-sr.md"
  - "raw/assets/manual/user-guide -- render -- what-is-real-time-path-tracing.md"
  - "raw/assets/manual/user-guide -- render -- what-is-fsr-frame-generation.md"
  - "raw/assets/manual/user-guide -- render -- what-is-the-fps-booster-for-complex-geometry.md"
  - "raw/assets/manual/user-guide -- render -- where-can-i-activate-frame-generation.md"
tags: [manual, render, output, path-tracing, sr, video]
---

D5 Render 用户手册的渲染输出章节，涵盖图像/视频渲染、实时路径追踪、超分辨率和帧生成技术。

## 渲染模式

渲染模式记录输出格式、分辨率、通道设置等参数，下次进入自动应用。

### 图像渲染
- 支持单帧图像和全景图输出
- 可选分辨率和格式
- 支持通道图输出（法线、深度、反射等）

### 视频渲染
- 支持动画关键帧参数设置
- 输出格式: MP4、AVI
- 序列帧支持 PNG、EXR

### 渲染队列
批量渲染功能，可一次性渲染多个渲染任务。

## Real-time Path Tracing（实时路径追踪）

D5 自研 [[global-illumination|全局光照 (GI)]] 技术方案，优化实时渲染 + 图像/视频输出。

### 偏好设置
- **Legacy D5 GI Compatible Mode**: 启用 D5 2.9 版本的 ReSTIR Surfel GI，保持旧场景视觉一致性

### Accumulation（累积模式，快捷键 F4）
- 启用后像素样本持续累积直至达到最终输出质量
- 移动相机或按 ESC 终止

### 自定义参数
| 参数 | 说明 |
|------|------|
| GI Precision | GI 精度级别，3 级，越高级 GI 质量越准确但收敛越慢 |
| Refl. Depth | 光线在高反射面之间的反弹次数 |
| SPP | 每像素采样数，增大可优化伪影 |
| Roughness Limit | 粗糙度上限，默认 0.5，更高值使累积更准确 |

### 新 GI 主要改进
1. **改进的 GI 缓存**: 路径追踪计算并缓存光线反弹，提升缓存质量
2. **优化的 GI 弹射细节**: 墙地交接处等细节更准确
3. **无偏采样和可见性检测**: 间接光照更接近 Ground Truth
4. **优化的植被和布料材质**: 修复光传输中的色彩衰减问题

## D5 SR（超分辨率）

D5 自研超分辨率技术，提升渲染图像分辨率和质量。

## Frame Generation（帧生成）

- 基于 FSR (FidelityFX Super Resolution) 技术
- 提升实时预览帧率
- 支持在偏好设置中启用

## FPS Booster

复杂几何体的帧率优化工具，在保持视觉质量的前提下提升性能。
