---
title: Post-Processing
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- effect.md"
  - "raw/assets/blog/color-grading-d5-effect-panel-guide.md"
  - "raw/assets/blog/one-click-3d-post-processing-d5-render.md"
  - "raw/assets/blog/postprocessing-vignette-chromatic-aberration-for-photorealistic-3d-rendering.md"
tags: [post-processing, effect, lut, vignette, bloom, color-grading]
---

后处理 (Post-Processing) 是 D5 Render 中对渲染结果进行色调、镜头效果和艺术风格调整的系统，帮助将渲染从"数字化"提升到"摄影化"的质感。

## Effect 面板参数

### 基础调整
- **Exposure**: 曝光度
- **Contrast**: 对比度
- **Highlight / Shadow**: 高光/阴影控制
- **White Balance**: 白平衡

### 镜头效果
- **Bloom**: 泛光/光晕，模拟高光溢出
- **Vignette**: 暗角，边缘自然变暗
- **Chromatic Aberration**: 色差，模拟镜头边缘色彩分离

### 风格化
- **AO**: 环境光遮蔽增强
- **Z-Depth**: 基于深度的效果
- **Outline Mode**: 轮廓线模式

## LUT (查找表)

- 应用预设或自定义颜色分级
- 一键改变整体色调风格
- 支持 .cube 等标准 LUT 格式

## Color Grading (Widget)

[[widgets|Color Grading Widget]] 提供更精确的色调控制：
- **Midtones**: 中间调色调
- **Shadows**: 阴影色调
- **Highlights**: 高光色调
- **Global**: 全局色调

## 预设保存

环境和后处理预设可通过 [[d5-studio|D5 Studio]] 保存和重用：
- 保存到 My Space（个人）或 Team Space（团队）
- 可选择仅保存特效（不含环境信息）

*来源: [[src-manual-lighting-environment]], [[src-blog-camera-rendering]]*
