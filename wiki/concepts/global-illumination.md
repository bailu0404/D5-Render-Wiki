---
title: Global Illumination
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- render -- what-is-real-time-path-tracing.md"
  - "raw/assets/blog/d5-render-global-illumination.md"
  - "raw/assets/blog/advanced-d5-gi-ground-truth.md"
  - "raw/assets/blog/d5-render-2-10-real-time-path-tracing.md"
tags: [gi, path-tracing, rendering, lighting]
---

全局光照 (Global Illumination, GI) 是模拟光线在场景中多次弹射的渲染技术，使间接光照（如色彩溢出、反射光）效果真实可信。D5 Render 采用自研实时路径追踪 GI 方案。

## D5 Render 的 GI 技术演进

### ReSTIR Surfel GI (2.9)
D5 Render 2.9 版本使用的 GI 方案，基于 ReSTIR 采样算法和 Surfel 缓存。

### Real-time Path Tracing (2.10+)
2.10 版本引入全新路径追踪 GI：
- **改进的 GI 缓存**: 路径追踪计算并缓存光线弹射，提升缓存质量
- **高反射地面正确渲染**: 2.9 中金属地板反射不准确/偏黑的问题得到解决
- **优化的 GI 弹射细节**: 墙地交接处等细节更准确
- **无偏采样**: 间接光照更接近 Ground Truth
- **优化的植被/布料材质**: 修复色彩衰减问题

## 自定义 GI 参数

| 参数 | 说明 |
|------|------|
| GI Precision | GI 精度，3 级，越高级越准确但收敛越慢 |
| Refl. Depth | 光线在高反射面之间的弹射次数 |
| SPP | 每像素采样数，增大可优化伪影和细节 |
| Roughness Limit | 粗糙度计算上限，默认 0.5 |

## Accumulation 模式

快捷键 F4 启用累积模式，像素样本持续累积直至达到最终输出质量。移动相机或按 ESC 终止。

## Legacy GI 兼容模式

在 Preference > Rendering 中可启用 "Legacy D5 GI Compatible Mode"，使用 2.9 版本的 ReSTIR Surfel GI 保持旧场景视觉一致性。此选项仅为兼容目的，将在未来版本移除。

*来源: [[src-manual-render-output]], [[src-blog-camera-rendering]]*
