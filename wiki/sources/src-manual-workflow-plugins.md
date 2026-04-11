---
title: "Manual: Workflow Plugins"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/workflow -- sketchup.md"
  - "raw/assets/manual/workflow -- rhino.md"
  - "raw/assets/manual/workflow -- 3ds-max.md"
  - "raw/assets/manual/workflow -- revit.md"
  - "raw/assets/manual/workflow -- blender.md"
  - "raw/assets/manual/workflow -- archicad-1.md"
  - "raw/assets/manual/workflow -- archicad.md"
  - "raw/assets/manual/workflow -- vectorworks.md"
  - "raw/assets/manual/workflow -- general-questions.md"
  - "raw/assets/manual/workflow -- abnormal-situations.md"
tags: [manual, workflow, plugin, sync, livesync, sketchup, rhino, revit, 3ds-max, blender, archicad, vectorworks]
---

D5 Render 用户手册的工作流插件章节，涵盖所有建模软件与 D5 Render 之间的同步和实时同步插件。

## 插件类型

### D5 Sync（同步插件）
非实时同步，将模型数据从建模软件导出到 D5 Render。支持模型更新和替换。

### D5 LiveSync（实时同步插件）
实时同步，建模软件中的修改即时反映在 D5 Render 中。

## 支持的建模软件

| 软件 | Sync | LiveSync | 说明 |
|------|------|----------|------|
| SketchUp | ✓ | ✓ | 最完整的工作流支持 |
| Rhino | ✓ | ✓ | 支持 Rhino 6.5+ |
| 3ds Max | ✓ | ✓ (Beta) | 支持 V-Ray/Corona 功能对照表 |
| Revit | ✓ | ✗ | 非实时同步 |
| ArchiCAD | ✓ | ✓ | 支持 ArchiCAD 26/27 |
| Blender | ✓ | ✗ | 非实时同步 |
| VectorWorks | ✗ | ✓ | 仅实时同步 |
| Cinema 4D | ✓ | ✗ | 非实时同步 |

## 3ds Max 特殊说明

- 支持 V-Ray 功能对照表，列出 V-Ray 功能在 D5 中的对应情况
- 支持 Corona 功能对照表
- LiveSync 目前为 Beta 版本

## 通用问题

- 插件安装与卸载
- 从 D5 Converter 启动 D5 时的常见错误
- 同步超时问题
- 建模软件与 D5 顶视图方向不一致
- `.d5a` 文件组结构对齐同步坐标问题

## 异常情况处理

### LiveSync 异常
- 同步后材质拾取异常的处理方法

### Sync 异常
- 使用 Sync for 3ds Max 替换模型时位移问题的处理方法
