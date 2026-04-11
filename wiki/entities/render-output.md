---
title: Render Output
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- render.md"
  - "raw/assets/manual/user-guide -- render -- what-is-real-time-path-tracing.md"
  - "raw/assets/manual/user-guide -- render -- what-is-d5-sr.md"
  - "raw/assets/manual/user-guide -- render -- what-is-fsr-frame-generation.md"
  - "raw/assets/blog/d5-super-resolution-image-rendering.md"
  - "raw/assets/blog/d5-render-2-10-real-time-path-tracing.md"
tags: [render, output, path-tracing, sr, video, image]
---

D5 Render 的渲染输出系统支持图像、视频和交互式展示，结合自研实时路径追踪和超分辨率技术，在速度与品质间取得平衡。

## 渲染模式

进入渲染模式后，输出格式、分辨率、通道设置等参数自动记录并在下次应用。

### 图像渲染
- 单帧图像和全景图
- 支持多通道输出（法线、深度、反射等）
- [[widgets|高级图像渲染 Widget]] 支持 PNG/JPG/TGA/TIF/EXR 格式

### 视频渲染
- 支持动画关键帧和路径动画
- 输出格式: MP4、AVI
- 序列帧: PNG、EXR（含通道选择）
- [[widgets|高级视频渲染 Widget]] 提供更多编码选项

### 渲染队列
批量渲染多个任务。

## Real-time Path Tracing

D5 自研 [[global-illumination|实时路径追踪]] 技术：
- **Accumulation (F4)**: 像素累积至最终输出质量
- **GI Precision**: 3 级精度控制
- **Refl. Depth**: 反射弹射次数
- **SPP**: 每像素采样数
- **Roughness Limit**: 粗糙度计算上限

### 新 GI 改进
- 路径追踪缓存提升反射质量
- 更准确的 GI 弹射细节
- 无偏采样接近 Ground Truth
- 优化的植被/布料色彩模型

## D5 SR（超分辨率）

自研超分辨率技术，提升渲染分辨率和细节。

## Frame Generation（帧生成）

基于 FSR 技术，提升实时预览帧率。

## FPS Booster

复杂几何体的帧率优化，在保持视觉质量前提下提升性能。

*来源: [[src-manual-render-output]], [[src-blog-camera-rendering]]*
