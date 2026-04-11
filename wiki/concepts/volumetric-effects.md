---
title: Volumetric Effects
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- environment -- weather.md"
  - "raw/assets/blog/volumetric-clouds-sky-replacement.md"
  - "raw/assets/blog/how-to-realistic-fog-archviz-rendering-d5render.md"
tags: [volumetric, fog, cloud, weather, atmosphere]
---

体积效果 (Volumetric Effects) 是 D5 Render 中模拟大气现象的技术，包括体积雾、体积云和体积光，为场景增加深度和氛围感。

## Volumetric Cloud（体积云）

3.0 版本全新天气系统核心升级：
- 超越简单背景，提供超写实深度和灵活视觉控制
- 精确预设: 积云 (Cumulus)、层积云 (Stratocumulus) 等
- 可调节密度和海拔匹配精确艺术意图
- 自由雕塑天空形态

## Fog（雾效）

3.0 版本雾效升级：
- 独立的颜色和密度控制
- 新增 "Follow Sunlight" 选项
- 确保自然深度和真实的光散射效果
- 无论时间如何变化都保持真实感

## 体积光

雾效开启后，灯光穿过雾气产生可见的体积光束（God Rays）：
- 适合室内/室外氛围营造
- 需在 Environment > Weather > Fog 中先启用雾效

## 天气系统

D5 Render 的天气效果包括：
- **Fog**: 雾效，增强空间深度
- **Rain**: 雨天，雨滴粒子效果
- **Snow**: 雪景，雪花飘落
- **Volumetric Cloud**: 体积云，大气层效果

*来源: [[src-manual-lighting-environment]], [[src-blog-lighting-environment]]*
