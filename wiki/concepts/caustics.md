---
title: Caustics
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- environment -- sky.md"
  - "raw/assets/manual/user-guide -- material -- how-to-achieve-caustics.md"
  - "raw/assets/blog/caustics-in-render.md"
tags: [caustics, light, refraction, reflection, water]
---

焦散 (Caustics) 是光线通过透明或反射表面折射/反射后产生的聚焦光斑效果，如水面波光、玻璃透射光斑等。D5 Render 支持太阳焦散效果。

## 启用条件

焦散效果需**同时在材质和光源两端启用**：

### 光源端
在 Geo Sky / Custom Daytime 的 Caustics 选项中启用：
- **Caustics Intensity**: 焦散效果强度倍增
- **Softness**: 焦散柔化程度（当 Light Source Radius > 0 时生效）

### 材质端
仅以下材质模板支持焦散：

| 材质模板 | 反射焦散 | 折射焦散 |
|----------|----------|----------|
| Custom | ✓ | — |
| Transparent | ✓ | ✓ |
| Water | ✓ | ✓ |

## 实际应用

- 水面波光粼粼的效果
- 玻璃透射的光斑
- 金属反射的聚焦光线
- 游泳池底部的光线图案

*来源: [[src-manual-lighting-environment]], [[src-manual-material]]*
