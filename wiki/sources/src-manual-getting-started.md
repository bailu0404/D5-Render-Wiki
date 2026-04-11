---
title: "Manual: Getting Started"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/getting-started -- quick-start.md"
  - "raw/assets/manual/getting-started -- d5-workflow.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- interface-shortcuts-camera.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- model-connection.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- material.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- landscape.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- environment-effects.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- image-animation-output.md"
  - "raw/assets/manual/getting-started -- d5-workflow -- ai-features.md"
  - "raw/assets/manual/About D5 Render  User Manual.md"
tags: [manual, getting-started, workflow, installation]
---

D5 Render 用户手册的入门指南部分，涵盖安装配置、界面操作、工作流程概览。

## 系统要求

- **最低 GPU**: NVIDIA GeForce GTX 1060 6GB
- **推荐 GPU**: NVIDIA GeForce RTX 2060 或更高，Quadro RTX 系列
- **系统**: Windows 10 1809 或更高版本
- **驱动**: NVIDIA 471.68 或更高版本（建议最新）
- 渲染管线基于 DX12 和 DXR

## 下载与安装

### 2.5 版本之前
解压安装包，默认安装到 C 盘，支持自定义路径。资产默认下载到安装路径，安装后可在"偏好设置"中迁移。

### 2.5 版本（简化安装）
安装包自动执行下载和安装。支持选择工作区路径，预设资产、本地资源和临时文件位置。

### 2.11+ 版本（D5 Launcher）
- 需先安装 [[d5-launcher]]，再通过 Launcher 下载 D5 Render
- D5 Launcher 取代了原欢迎页面，打开场景时自动最小化到系统托盘
- 集成 D5 Render、D5 Lite、D5 Sync 插件

## D5 Render 界面概览

D5 Render 由三个主要部分组成：
- **主界面**: 创建场景、调整模型、编辑材质
- **渲染模式**: 添加渲染设置和编辑面板
- **资产库**: 独立显示的资产浏览窗口

## 支持的文件格式

- `.d5a` — D5 Render 模型格式
- `.skp` — SketchUp 2017+
- `.3dm` — Rhino 6.5+
- `.fbx` — 支持模型数据，不含材质
- `.abc` — 仅支持导入场景

## D5 Workflow 工作流

D5 Render 的工作流分为六个核心环节：

1. **界面、快捷键、相机** — 操作界面布局、快捷键设置、[[camera-and-view|相机控制]]
2. **模型连接** — 通过 [[workflow-plugins|工作流插件]] 导入模型
3. **材质** — [[pbr-materials|PBR 材质]]编辑与应用
4. **景观** — [[tools-landscape|景观工具]]（地形、散布、植被）
5. **环境与特效** — [[lighting-system|光照]]、[[environment-and-effects|天气]]、[[post-processing|后处理]]
6. **图像与动画输出** — [[render-output|渲染输出]]

## 模型准备建议

- 检查模型面法线方向，确保正确朝向
- 确保模型完整，避免相机中出现破损或重叠面
- 导入前整理好 UV 坐标，导入后可在 D5 中进行拉伸、偏移、旋转、三平面映射等调整
