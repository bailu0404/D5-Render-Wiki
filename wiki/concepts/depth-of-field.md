---
title: Depth of Field
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- view -- how-to-set-the-depth-of-field-effect.md"
  - "raw/assets/blog/how-to-create-animation-in-d5-render-with-depth-of-field.md"
tags: [dof, camera, bokeh, photography]
---

景深 (Depth of Field, DoF) 是模拟真实相机镜头的焦点范围效果 — 焦点外区域自然模糊，引导观者视线聚焦于关键设计元素。

## D5 Render 中的景深

### 设置方法
- 在视图控制面板中启用
- 调整焦点距离 (Focus Distance)
- 调整光圈大小 (Aperture / F-Stop)

### 参数控制
- **Focus Distance**: 焦点距离，决定清晰区域的位置
- **Aperture**: 光圈大小，控制模糊程度和范围
- **Bokeh**: 散景效果，焦点外高光的模糊形状

## 景深动画

景深参数可作为关键帧进行动画：
- 焦点距离随时间变化
- 实现焦点转移的电影级效果
- 适合建筑漫游动画

## 摄影级渲染

结合景深与其他相机效果（曝光、白平衡、色差、暗角等），D5 Render 帮助艺术家实现从数字化到摄影化的渲染质感。

*来源: [[src-manual-hardware-preference]], [[src-blog-animation]]*
