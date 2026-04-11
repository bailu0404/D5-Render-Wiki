---
title: D5 Render 概览
created: 2026-04-10
updated: 2026-04-11
sources:
  - D5 Render.md
  - raw/assets/manual/
  - raw/assets/blog/
tags:
  - overview
  - d5-render
---

# D5 Render 概览

D5 Render 是一款面向建筑与设计领域的实时渲染软件，基于 Unreal Engine 和 NVIDIA RTX 技术，搭载自研高精度 [[global-illumination|GI]] 和降噪技术，集成实时路径追踪、15+ AI 辅助工具、丰富资产库和全流程场景构建功能，覆盖从概念设计到最终展示的完整工作流。

## D5 全流程生态 (3.0)

D5 Render 3.0 引入 "Flow State" 全流程概念，统一三大产品：

1. **[[d5-lite]]** — 概念探索工具，在 SketchUp 内实时 AI 可视化
2. **[[d5-works]]** — AEC 专业 3D 资产平台
3. **D5 Render 3.0** — 高品质最终渲染引擎

全部通过 [[d5-launcher|D5 Launcher]] 统一入口管理。

## 核心功能模块

- **[[real-time-rendering]]** — 实时渲染与照片级输出，自研路径追踪 GI
- **[[ai-capabilities]]** — 15+ AI 功能，包括 AI Agent、材质生成、氛围匹配
- **[[asset-tools]]** — 资产工具，在线库含 2,000+ 材质、12,000+ 模型
- **[[environment-and-effects]]** — 环境与特效，Geo Sky/HDRI/体积云/雾/雨/雪
- **[[pbr-materials]]** — 10 种 PBR 材质模板，含 [[displacement-mapping|True Displacement]]
- **[[efficiency-tools]]** — 效率工具，地形/海洋/散布/城市生成器/Cesium
- **[[camera-and-view]]** — 相机与视图，真实相机参数 + 3.0 Free Mode
- **[[lighting-system]]** — 7 种光源类型 + AI 光照辅助
- **[[render-output]]** — 图像/视频渲染 + D5 SR 超分辨率
- **[[workflow-plugins]]** — 全系列建模软件插件 (SketchUp/Rhino/Revit/3ds Max/Blender/ArchiCAD/VectorWorks)
- **[[virtual-tour]]** — 全景/空间/XR 漫游展示
- **[[animation-system]]** — 路径动画 + 关键帧 + 渐变动画

## 核心渲染概念

- **[[global-illumination]]** — 自研实时路径追踪 GI
- **[[hdri-lighting]]** — 高动态范围环境光照
- **[[caustics]]** — 太阳焦散效果
- **[[post-processing]]** — 后处理与颜色分级
- **[[volumetric-effects]]** — 体积云/雾/体积光
- **[[gaussian-splatting]]** — 3D Gaussian Splatting 技术
- **[[xr-technology]]** — XR 扩展现实展示
- **[[depth-of-field]]** — 景深与散景

## 团队协作

- **[[d5-for-teams]]** — 9 大企业级功能：多人编辑/SSO/资产共享
- **[[d5-studio]]** — 云端预设共享空间
- **[[widgets]]** — 扩展模块 (舞台灯/投影灯/VR/颜色分级/项目合并)

## 定位

D5 Render 的核心优势在于将实时渲染的性能与易用性结合，使设计师无需深入技术细节即可产出高质量的可视化成果。3.0 版本通过全流程生态和 AI 智能核心，进一步消除了工具间的摩擦，让创意从概念到最终渲染无缝流转。
