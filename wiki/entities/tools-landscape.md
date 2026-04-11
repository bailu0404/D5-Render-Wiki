---
title: Landscape & Terrain Tools
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- tool.md"
  - "raw/assets/manual/user-guide -- tool -- how-to-use-ocean.md"
  - "raw/assets/manual/user-guide -- tool -- how-to-use-terrain.md"
  - "raw/assets/manual/user-guide -- tool -- how-to-use-d5-scatter.md"
  - "raw/assets/manual/user-guide -- tool -- how-to-use-city-generator.md"
  - "raw/assets/manual/user-guide -- tool -- how-to-use-cesium.md"
  - "raw/assets/blog/architectural-landscape-terrain-rendering.md"
  - "raw/assets/blog/how-d5-scatter-diagrams-transform-3d-environment-design.md"
  - "raw/assets/blog/realistic-ocean-waves-d5-render.md"
  - "raw/assets/blog/urban-planning-software-city-generator.md"
tags: [landscape, terrain, ocean, scatter, city-generator, cesium, vegetation]
---

D5 Render 的景观与地形工具集，涵盖地形编辑、海洋系统、散布工具、城市生成器和 Cesium 地理空间集成。

## Terrain（地形）

地形编辑工具，支持：
- 升高/降低地形
- 平滑地形表面
- 绘制地形材质
- 导入高度图生成地形

## Ocean（海洋）

3.0 版全新海洋系统：
- 一键生成动态海洋
- 自动分析地形生成有机海岸线过渡
- 滚浪效果
- 湿沙效果
- 不是简单平面，而是"活的环境"

## D5 Scatter（散布）

在场景中随机分布对象：
- 画笔式散布操作
- 可调节密度、缩放、旋转参数
- 适合草地、碎石、落叶等自然散布效果

## City Generator（城市生成器）

快速生成城市背景环境：
- 3.0 新增 Procedural Building（程序化建筑）
- 启用 "Styles" 选项即时生成风格化建筑
- 适合创建密集城市框架作为设计背景

## Cesium 集成

加载精确 3D 地理空间数据：
- 无需手动建模周边城市街区
- 直接加载项目所在位置的实际城市环境
- 3.0 版本开放给所有用户

## 植被工具

| 工具 | 功能 |
|------|------|
| Brush & Scatter | 画笔/散布放置植被 |
| Vegetation Path | 沿路径放置植被 |
| Eraser & Clean | 橡皮擦/清理植被 |
| 一键藤蔓 | 自动生成攀爬藤蔓 |
| 一键绿篱 | 快速填充绿篱叶片 |
| 草坪效果 | 创建逼真草坪 |
| Advanced Brush | 高级画笔（更精细控制） |

所有植被工具支持预设保存和重用。

*来源: [[src-manual-assets-landscape]], [[src-blog-assets-landscape]]*
