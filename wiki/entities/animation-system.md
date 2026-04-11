---
title: Animation System
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- animation-path.md"
  - "raw/assets/manual/user-guide -- animation-path -- draw-path.md"
  - "raw/assets/manual/user-guide -- animation-path -- character-path.md"
  - "raw/assets/manual/user-guide -- animation-path -- vehicle-path.md"
  - "raw/assets/blog/how-to-use-keyframes-to-create-animations-in-d5-render.md"
  - "raw/assets/blog/how-to-create-animation-in-d5-render-with-depth-of-field.md"
  - "raw/assets/blog/the-easiest-way-to-phasing-animations.md"
  - "raw/assets/blog/cinematic-animation-in-d5-render.md"
tags: [animation, keyframe, path, phasing, video]
---

D5 Render 的动画系统支持路径动画、关键帧动画和渐变动画，可直接输出视频格式的动画效果。

## 动画路径

### Draw Path（绘制路径）
自由绘制运动路径，物体沿路径运动。

### Character Path（人物路径）
人物沿指定路径行走，支持多人物动画场景。

### Vehicle Path（车辆路径）
车辆沿路径行驶，配合运动模糊效果增加真实感。

## 关键帧动画

- 在时间轴上设置关键帧
- 支持相机运动、光照变化、材质动画
- 支持景深动画（焦点距离随时间变化）

## 渐变动画（Phasing Animation）

D5 Render 提供最简便的渐变动画创建方式：
- 展示建筑从无到有的建造过程
- 适合设计演示和客户汇报

## 电影级动画

结合相机控制、景深、运动模糊和后处理特效，创建电影级别的动画效果。

*来源: [[src-manual-animation-tour]], [[src-blog-animation]]*
