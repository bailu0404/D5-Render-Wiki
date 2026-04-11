---
title: "Manual: Material System"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- material.md"
  - "raw/assets/manual/user-guide -- material -- car-paint.md"
  - "raw/assets/manual/user-guide -- material -- cloth.md"
  - "raw/assets/manual/user-guide -- material -- custom-alpha.md"
  - "raw/assets/manual/user-guide -- material -- displacement.md"
  - "raw/assets/manual/user-guide -- material -- foliage.md"
  - "raw/assets/manual/user-guide -- material -- grass.md"
  - "raw/assets/manual/user-guide -- material -- transparent.md"
  - "raw/assets/manual/user-guide -- material -- water.md"
  - "raw/assets/manual/user-guide -- material -- video.md"
  - "raw/assets/manual/user-guide -- material -- velvet.md"
  - "raw/assets/manual/user-guide -- material -- how-to-achieve-caustics.md"
  - "raw/assets/manual/user-guide -- material -- how-to-achieve-round-corner.md"
  - "raw/assets/manual/user-guide -- material -- how-to-control-the-bump-effect.md"
  - "raw/assets/manual/user-guide -- material -- how-to-control-the-reflection-effect.md"
  - "raw/assets/manual/user-guide -- material -- how-to-make-the-emissive-effect.md"
  - "raw/assets/manual/user-guide -- material -- what-is-invisible-in-raytracing.md"
  - "raw/assets/manual/user-guide -- material -- how-to-adjust-the-material-map.md"
  - "raw/assets/manual/user-guide -- material -- how-do-i-adjust-the-material-uv.md"
  - "raw/assets/manual/user-guide -- material -- what-materials-are-the-subsurface-scattering-templates-suitable-for.md"
  - "raw/assets/manual/user-guide -- material -- what-materials-are-the-flowing-water-templates-suitable-for.md"
tags: [manual, material, pbr, texture, uv, displacement]
---

D5 Render 用户手册的材质系统章节，涵盖 10 种材质模板、贴图通道、UV 控制和各模板特有参数。

## 材质参数面板

通过点击模型表面或使用"材质拾取器"工具（快捷键 `I`）选择材质，右侧面板显示材质检查器。

### 基本工具
- **Duplicate**: 复制当前材质参数
- **Add to local**: 将材质添加到本地库
- **Reset**: 恢复材质参数到初始状态

## 10 种材质模板

1. **Custom** — 自定义模板，完整 PBR 参数控制
2. **Transparent** — 透明材质（玻璃等），支持 [[caustics|焦散]]
3. **Water** — 水材质，带流动动画效果
4. **Displacement** — [[displacement-mapping|置换贴图]]材质
5. **Foliage** — 植被材质，支持次表面散射
6. **Grass** — 草地材质
7. **Cloth** — 布料材质
8. **Car Paint** — 车漆材质，带清漆层
9. **Video** — 视频材质，支持 mp4 等格式
10. **Custom Alpha** — 自定义透明度材质

## 核心贴图通道

### Base Color / Base Color Map
- 非金属 (Metallic=0): 漫反射颜色
- 金属 (Metallic=1): 反射颜色
- 贴图与纯色以 Multiply 模式混合；使用贴图原色时需确保纯色为白色
- 详细参数: 反转、对比度、色相、饱和度、亮度、独立 UV

### Normal
- 法线贴图产生表面凹凸效果
- D5 自动根据 Base Color Map 生成法线信息
- 支持法线强度调节（可为负值翻转凹凸）

### Specular
- 控制非金属的反射率 (F0)
- Specular 0→1 对应 F0 0%→8%
- 水为 0.25，玻璃/塑料约 0.5，宝石为 1

### Roughness
- 表面微观粗糙度，影响反射模糊程度
- Roughness 是 Glossiness 的反向

### Metallic
- PBR 金属/粗糙度工作流的核心参数
- 0 = 非金属，1 = 金属
- 0~1 之间的值用于锈蚀、灰尘等混合材质

### AO
- 环境光遮蔽通道，与 Base Color 相乘增强角落和缝隙阴影
- AO Multiplier 范围 0-1

### Emissive
- 材质自发光
- 参数: 强度、颜色、是否投射阴影

## UV 控制

全局 UV 参数：
- **Stretch**: 沿 UV 方向拉伸纹理
- **Offset**: UV 偏移
- **Rotate**: 纹理旋转 (0-360°)
- **Triplanar**: 复杂物体三平面映射
- **Blend Amount**: 三平面接缝混合

## 特殊材质模板参数

### Water 模板
- 带流动动画效果
- 特殊参数: Flow Velocity（流速）、Depth（深度，控制光线吸收）
- Specular 固定为 0.25，IOR 固定为 1.33
- 水面模型需为单面，下方需有平面作为水底

### Displacement 模板
- 支持 Parallax 和 True Displacement 两种模式
- True Displacement 参数: Subdivision Level、Vertical Offset、Maintain Continuity、Remesh
- 支持 Opacity Map 实现镂空效果

### SSS（次表面散射）模板
- 适用于皮肤、蜡、玉石等半透明材质
- 特殊参数: Subsurface Color、Scatter Radius

## Invisible in Raytracing

勾选后材质不参与光照（漫反射）计算，可见于相机和反射，但不投射阴影和反弹光。开启 Emissive 时自发光同样不参与 GI 计算。
