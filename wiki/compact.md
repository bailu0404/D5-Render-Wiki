---
title: D5 Render 速查表
created: 2026-04-13
updated: 2026-04-13
sources:
  - wiki/entities/
  - wiki/concepts/
tags:
  - compact
  - reference
---

# D5 Render 速查表

> 所有实体与概念页面的一句话定义。Agent 读完此页即可对 D5 Render 建立全局认知，再按需深读具体页面。

## 产品与生态

| 页面 | 定义 |
|------|------|
| [[d5-lite]] | 概念探索工具，在 SketchUp 内实时 AI 可视化，支持 AI 图生图与实时渲染引擎 |
| [[d5-works]] | AEC 专业 3D 资产平台，集成在线资产库浏览与下载，面向建筑/工程/施工行业 |
| [[d5-launcher]] | D5 统一启动器，集成项目管理、工作流插件、资产浏览和账户管理 |
| [[d5-for-teams]] | 团队协作方案，含 9 大企业级功能：多人编辑、SSO、团队资产库、应用集成 |
| [[d5-studio]] | 云端预设共享空间，支持个人/团队空间保存环境、材质和特效预设 |

## 核心功能模块

| 页面 | 定义 |
|------|------|
| [[real-time-rendering]] | 核心功能——提供即时反馈与照片级输出质量，覆盖从设计到展示的完整工作流 |
| [[ai-capabilities]] | AI 自动化功能集，为设计和可视化工作流提供更高效的创作方式 |
| [[asset-tools]] | 资产工具，帮助用户轻松实现自然或规整的景观设计 |
| [[environment-and-effects]] | 环境与特效系统，提供天空、天气、光影及专业后期特效 |
| [[efficiency-tools]] | 一站式场景构建工具集，涵盖基础光源、植物笔刷等直观易用工具 |
| [[camera-and-view]] | 相机与视图控制系统，提供简洁的相机设置与直观的视角操控 |
| [[lighting-system]] | 光照系统，含 Geo Sky/Custom/HDRI 天空 + 7 种人工光源 + AI 光照辅助 |
| [[render-output]] | 渲染输出，支持图像/视频/全景、路径追踪累积、D5 SR 超分辨率、帧生成 |
| [[tools-landscape]] | 景观与地形工具集：地形编辑、海洋、散布、城市生成器、Cesium 集成、植被工具 |
| [[workflow-plugins]] | 工作流插件，支持 SketchUp/Rhino/Revit/3ds Max/Blender/ArchiCAD/VectorWorks 同步 |
| [[virtual-tour]] | 虚拟漫游，三种类型：全景漫游、空间漫游（平面图+航点）、XR 漫游（Gaussian Splatting） |
| [[animation-system]] | 动画系统，含路径动画、关键帧动画、渐变动画（Phasing）和电影级动画组合 |
| [[widgets]] | 扩展模块：高级图像/视频渲染、颜色分级、投影灯、舞台灯、剖面工具、VR、项目合并 |

## 渲染概念

| 页面 | 定义 |
|------|------|
| [[pbr-materials]] | 基于物理的渲染材质系统，10 种简化 PBR 模板确保各类光照下准确视觉效果 |
| [[global-illumination]] | 全局光照，D5 自研实时路径追踪 GI（2.10+ 取代 ReSTIR Surfel GI） |
| [[hdri-lighting]] | 高动态范围环境光照，32 位/通道，既是背景也是光源 |
| [[displacement-mapping]] | 置换贴图，3.0 新增 True Displacement 物理置换几何体（取代视差凹凸） |
| [[caustics]] | 焦散效果，需同时在材质端和光源端启用，用于水面波光和玻璃透射光斑 |
| [[post-processing]] | 后处理与颜色分级，含曝光/对比度/镜头效果/LUT/Color Grading Widget |
| [[volumetric-effects]] | 体积效果，含体积云、雾效、体积光（God Rays）和天气系统 |
| [[gaussian-splatting]] | 3D Gaussian Splatting 技术，用高斯椭球体表示 3D 空间，支持 MP4 转 3D 和 XR Tour |
| [[xr-technology]] | XR 扩展现实，含 VR（SteamVR）、AR、MR，D5 通过 XR Tour 和 VR Widget 实现 |
| [[depth-of-field]] | 景深与散景，通过焦点距离和光圈控制清晰区域，支持关键帧动画 |
