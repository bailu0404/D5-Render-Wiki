---
title: "Manual: Hardware, Preferences & System"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- hardware.md"
  - "raw/assets/manual/user-guide -- hardware -- system-requirements-for-d5-render.md"
  - "raw/assets/manual/user-guide -- hardware -- what-graphic-cards-does-d5-support.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-view-and-optimize-graphics-card-usage.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-view-and-optimize-memory-usage.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-view-and-upgrade-graphics-card-driver.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-check-memory-usage-graphics-memory-usage-and-graphics-card-driver-version.md"
  - "raw/assets/manual/user-guide -- hardware -- does-the-cpu-have-a-big-impact-on-d5.md"
  - "raw/assets/manual/user-guide -- hardware -- what-is-hardware-testing.md"
  - "raw/assets/manual/user-guide -- hardware -- what-is-the-hardware-test-tool-benchmark.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-choose-the-right-computer-power-for-graphic-cards.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-use-support-tool.md"
  - "raw/assets/manual/user-guide -- hardware -- how-to-use-the-3dconnexion-r-spacemouse-in-d5-render.md"
  - "raw/assets/manual/user-guide -- hardware -- why-are-close-textures-clearer-but-distant-textures-blurry.md"
  - "raw/assets/manual/user-guide -- hardware -- why-is-d5-not-working-properly-when-remote.md"
  - "raw/assets/manual/user-guide -- hardware -- why-need-to-wait-a-long-time-to-open-a-d5-scene.md"
  - "raw/assets/manual/user-guide -- hardware -- what-do-the-parameters-in-the-statistics-represent.md"
  - "raw/assets/manual/user-guide -- preference.md"
  - "raw/assets/manual/user-guide -- preference -- how-to-change-the-default-language.md"
  - "raw/assets/manual/user-guide -- preference -- how-to-set-up-the-web-proxy.md"
  - "raw/assets/manual/user-guide -- preference -- how-to-view-and-change-the-default-shortcuts.md"
  - "raw/assets/manual/user-guide -- preference -- use-with-high-resolution-screen.md"
  - "raw/assets/manual/user-guide -- preference -- save-compressed-project.md"
  - "raw/assets/manual/user-guide -- common-pop-up-windows.md"
  - "raw/assets/manual/user-guide -- resource.md"
  - "raw/assets/manual/user-guide -- view.md"
  - "raw/assets/manual/user-guide -- view -- camera.md"
  - "raw/assets/manual/user-guide -- view -- navigation.md"
  - "raw/assets/manual/user-guide -- view -- display.md"
  - "raw/assets/manual/user-guide -- view -- how-to-set-section-render-section-diagram.md"
  - "raw/assets/manual/user-guide -- view -- how-to-use-parallel-projection.md"
  - "raw/assets/manual/user-guide -- view -- how-to-set-the-depth-of-field-effect.md"
  - "raw/assets/manual/user-guide -- view -- what-is-the-feature-of-horizontal-and-vertical-fov.md"
  - "raw/assets/manual/learn-more -- shortcuts.md"
  - "raw/assets/manual/model -- how-to-import-model-files-into-d5-render.md"
  - "raw/assets/manual/model -- how-to-edit-models.md"
  - "raw/assets/manual/model -- how-to-replace-models-in-the-scene.md"
  - "raw/assets/manual/model -- how-to-sync-update-modified-moved-models-to-d5.md"
tags: [manual, hardware, preference, system, view, camera, shortcuts, model-management]
---

D5 Render 用户手册的硬件配置、偏好设置、视图控制与模型管理章节。

## 硬件

### 系统要求
- **最低**: GTX 1060 6GB, Win10 1809+
- **推荐**: RTX 2060+, 471.68+ 驱动
- CPU 对 D5 影响较小，主要依赖 GPU

### 显卡支持
- 支持 NVIDIA RTX 系列（RTX 20/30/40/50 系列）
- 不支持 AMD 和 Intel 集成显卡

### 诊断工具
- **Hardware Testing**: 启动时自动检测配置是否达标
- **Benchmark**: 硬件测试工具，评估渲染性能
- **Support Tool**: 收集系统信息和日志用于技术支持
- **Statistics**: 实时显示帧率、GPU 使用率、显存占用等参数

### 常见硬件问题
- 近处清晰远处模糊 — Mipmap 机制正常现象
- 远程使用 D5 异常 — 不推荐远程桌面使用
- 打开场景缓慢 — 与场景大小和硬盘速度相关

## 偏好设置

- **语言**: 支持中文/英文等多语言切换
- **网络代理**: 支持设置 Web 代理
- **快捷键**: 支持查看和修改默认快捷键
- **高分辨率屏幕**: 支持 HiDPI 显示
- **压缩项目**: 保存压缩项目减小文件体积
- **渲染设置**: HDRI 分辨率、GI 模式、帧生成等
- **Widget**: 管理 [[widgets|扩展模块]]

## 视图与相机

### Camera（相机）
- 真实相机参数: 曝光、焦距、[[depth-of-field|景深]]、白平衡
- 支持水平/垂直 FOV 切换
- 3.0 新增 Free Mode — 统一 Walk 和 Fly 模式

### Navigation（导航）
- 键盘 + 鼠标组合操作
- 3.0 支持切换到 SketchUp/Rhino/3ds Max 导航预设

### Display（显示）
- 多种预览质量等级
- 线框/实体/材质显示模式

### 特殊视图
- **Parallel Projection**: 平行投影（正交视图）
- **Section**: 剖面渲染/剖面图
- **Depth of Field**: 景深效果
- **Full Screen**: 全屏模式

## 模型管理

### 导入模型
- 支持格式: .d5a, .skp, .3dm, .fbx, .abc
- 可通过 [[workflow-plugins|工作流插件]] 从其他建模软件导入

### 模型操作
- 对齐、复制、翻转/镜像
- 替换模型、同步更新
- Make Unique — 创建独立副本
- Sync Pivot — 同步轴心点（用于门开关动画）

### 资源管理
- **Object List**: 场景对象列表，管理模型和灯光
- **Scene List**: 场景列表
- **Layers**: 图层管理
- **Imported List**: 已导入模型列表
- **Auto-save**: 自动保存和备份机制
- **DRS**: D5 资源系统

## 常见弹窗

- 低 TDR 检测
- DX12 不支持
- 灯光数量超限 (4096)
- 焦散灯光数量超限 (64)
- 植被数量超限
- 自发光达到上限
- 材质无法复用
