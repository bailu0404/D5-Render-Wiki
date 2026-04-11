---
title: Workflow Plugins
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/workflow -- sketchup.md"
  - "raw/assets/manual/workflow -- rhino.md"
  - "raw/assets/manual/workflow -- 3ds-max.md"
  - "raw/assets/manual/workflow -- revit.md"
  - "raw/assets/manual/workflow -- blender.md"
  - "raw/assets/manual/workflow -- archicad-1.md"
  - "raw/assets/manual/workflow -- vectorworks.md"
  - "raw/assets/blog/sketchup-rendering-with-d5-render.md"
  - "raw/assets/blog/best-real-time-rhino-rendering-workflow-for-you-with-d5-render.md"
  - "raw/assets/blog/d5-render-for-revit-best-real-time-3d-rendering-workflow.md"
  - "raw/assets/blog/blender-archviz-with-d5-workflow.md"
  - "raw/assets/blog/archicad-d5-large-scale-architecture-design.md"
tags: [workflow, plugin, sync, livesync, sketchup, rhino, revit, 3ds-max, blender, archicad]
---

D5 Render 的全系列工作流插件，支持主流建模软件与 D5 Render 之间的模型同步和实时同步。

## 两种同步模式

### D5 Sync（同步插件）
非实时同步 — 将模型数据从建模软件导出到 D5 Render，支持模型更新和替换。

### D5 LiveSync（实时同步插件）
实时同步 — 建模软件中的修改即时反映在 D5 Render 视口中，实现"所见即所得"的工作流。

## 支持的建模软件

| 软件 | Sync | LiveSync | 备注 |
|------|------|----------|------|
| **SketchUp** | ✓ | ✓ | 最完整支持，2017+ |
| **Rhino** | ✓ | ✓ | Rhino 6.5+ |
| **3ds Max** | ✓ | ✓ (Beta) | 支持 V-Ray/Corona 对照表 |
| **Revit** | ✓ | — | 非实时同步 |
| **ArchiCAD** | ✓ | ✓ | ArchiCAD 26/27 |
| **Blender** | ✓ | — | 非实时同步 |
| **VectorWorks** | — | ✓ | 仅实时同步 |
| **Cinema 4D** | ✓ | — | 非实时同步 |

## 3ds Max 特殊功能

- **V-Ray 功能对照表**: 列出 V-Ray 材质/灯光在 D5 中的对应情况
- **Corona 功能对照表**: Corona 材质/灯光的兼容性映射
- LiveSync 目前为 Beta 版本

## D5 Converter

D5 Sync 插件的核心组件，负责模型转换和同步：
- 支持 `.d5a` 格式输出
- 支持材质自动转换
- 支持模型更新和替换

## 通用问题处理

- 插件安装与卸载
- 从 Converter 启动 D5 的常见错误
- 同步超时问题
- 坐标系方向不一致
- 文件组结构对齐问题

*来源: [[src-manual-workflow-plugins]], [[src-blog-workflow-plugins]]*
