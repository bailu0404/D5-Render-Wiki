---
title: "Manual: AI Features"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- ai.md"
  - "raw/assets/manual/user-guide -- ai -- ai-agent.md"
  - "raw/assets/manual/user-guide -- ai -- how-to-use-ai-atmosphere-match.md"
  - "raw/assets/manual/user-guide -- ai -- how-to-use-ai-generated-texture-maps.md"
  - "raw/assets/manual/user-guide -- ai -- how-to-use-ai-make-seamless.md"
  - "raw/assets/manual/user-guide -- ai -- how-to-use-ai-material-match.md"
  - "raw/assets/manual/user-guide -- ai -- how-to-use-ai-material-snap.md"
  - "raw/assets/manual/user-guide -- ai -- how-to-use-ai-post-processing.md"
  - "raw/assets/manual/user-guide -- ai -- how-to-use-ai-ultra-hd-texture.md"
  - "raw/assets/manual/user-guide -- ai -- how-to-use-the-ai-model-generation-feature.md"
  - "raw/assets/manual/user-guide -- ai -- account-access-to-ai-features.md"
tags: [manual, ai, agent, material-generation, atmosphere]
---

D5 Render 用户手册的 AI 功能章节，涵盖 AI Agent、AI 材质工具、AI 后处理等所有 AI 驱动功能。

## AI Agent

AI Agent 门户位于顶部菜单栏，包含三大功能模块：

### 1. SmartPlanting（智能种植）

输入场地位置和偏好，AI Agent 利用植物数据库和气候模型，即时生成定制化的花境设计方案。设计面积上限 30m²。

三种设计风格模式：
- **季节性花境**: 针对特定季节观赏需求优化
- **自然多年生花境**: 使用多年生植物构建可持续生态系统
- **极简无花花园**: 多样叶形与微妙灰度调色板

### 2. Design Assistant Toolkit（设计助手工具包）

#### AI Scene Match（场景匹配）
- 描述期望的氛围（如"秋日黄昏"、"雪天冬季"），AI 生成参考图
- 自动匹配光照和后处理参数到当前场景
- 参考图支持语义迭代生成

#### AI Asset Recommendation（资产推荐）
- 支持图像识别和文本检索
- 上传参考图或输入关键词，AI 智能推荐匹配的模型

#### Light Source Assisted Adjustment（光源辅助调整）
- 通过自然语言指令精确调整场景光源参数
- 支持自动调整和手动选择调整
- 可优化特定区域照明、防止过曝

#### Export（导出）
- 自动导出场景中使用的所有 D5 在线材质库植物列表
- 支持上传植物报价文件，自动匹配成本并智能计算

### 3. D5 Bot

AI 驱动的支持助手，回答 D5 Render 使用问题。
- 支持自动 AI 生成问题摘要和描述
- 支持手动截图上传，创建提交给 D5 支持团队的报告

### 权限说明

Pro、EDU 和 Team 用户在有效期内可无限次使用 AI Agent 功能。

## AI 材质工具

- **AI PBR Material Snap**: 将照片转换为精确的 PBR 材质
- **AI Material Match**: 智能匹配材质参数
- **AI Generated Texture Maps**: 一键生成完整 PBR 贴图集
- **AI Make Seamless**: 消除纹理拼接缝隙
- **AI Ultra HD Texture**: 提升纹理分辨率，适合近距离细节
- **AI Model Generation**: 从参考图生成 3D 模型

## AI 后处理

- **AI Post-Processing**: 智能优化渲染图像质量
- **AI Atmosphere Match**: 从参考图转移光照、天气和环境氛围到当前场景
