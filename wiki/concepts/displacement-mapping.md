---
title: Displacement Mapping
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- material -- displacement.md"
  - "raw/assets/blog/displacement-maps-material-d5-render.md"
  - "raw/assets/blog/a-quick-easy-way-to-make-displacement-texture.md"
tags: [displacement, material, texture, height-map]
---

置换贴图 (Displacement Mapping) 通过修改模型几何结构来表现材质的真实凹凸细节，比法线贴图 (Normal Map) 和视差贴图 (Parallax) 提供更真实的表面效果。

## 两种模式

### Parallax（视差）
D5 Render 之前的默认凹凸方案，通过视觉错觉模拟深度，不修改几何结构。

### True Displacement（真实置换）
3.0 版本新增，通过高度图物理置换几何体：
- 白色 = 凸起部分
- 黑色 = 凹陷部分

## True Displacement 参数

| 参数 | 说明 |
|------|------|
| Subdivision Level | 网格细分级别，越高越精细但增加面数和渲染时间 |
| Vertical Offset | 垂直偏移，补偿置换后模型的悬浮或穿插 |
| Maintain Continuity | 保持模型实体结构闭合完整 |
| Remesh | 对拓扑差的模型进行网格重建 |

> 注意: 更高的细分级别可达到更精细的效果，但会增加模型面数、内存占用和渲染时间。过度使用可能导致闪退。

## Opacity Map（不透明度贴图）

Displacement 材质模板新增不透明度贴图，实现镂空效果：
- 适用于绿篱、栅栏、竹编表面等
- 精确控制材质切割

## 限制

- LiveSync 模型不支持 True Displacement（UI 开关禁用）
- 如需使用，需将模型转换为非实时同步模型

*来源: [[src-manual-material]], [[src-blog-materials-textures]]*
