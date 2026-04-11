---
title: Lighting System
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- lights.md"
  - "raw/assets/manual/user-guide -- lights -- what-types-of-light-sources-are-offered-by-d5.md"
  - "raw/assets/manual/user-guide -- lights -- what-are-the-meanings-of-each-parameter-in-the-light-panel.md"
  - "raw/assets/manual/user-guide -- environment -- sky.md"
  - "raw/assets/blog/d5-render-smart-lighting-system-guide.md"
  - "raw/assets/blog/4-best-tips-of-realistic-environmental-lighting-for-architecture.md"
tags: [lighting, sky, hdri, lights, gi]
---

D5 Render 的光照系统包含自然光（天空系统）和人工光源两大体系，结合 [[global-illumination|全局光照]] 技术实现真实感光照。

## 天空系统

### Geo Sky（地理天空）
基于地理位置精确模拟太阳角度，支持经纬度、时间、日期输入，可校正北方偏移。

### Custom（自定义天空）
手动设置太阳/月亮的高度角、方位角，自定义天体参数。

### HDRI
[[hdri-lighting|HDRI]] 既是背景也是光源，支持旋转、翻转、色温/色相调节、分辨率控制（2K/4K/8K/实际）。

## 人工光源

D5 Render 提供 7 种光源类型：

| 光源 | 用途 | 特殊参数 |
|------|------|----------|
| Point Light | 模拟灯泡 | 光源半径 |
| Spotlight | 聚光灯 | IES 文件、锥角 |
| Strip Light | 条形灯 | Barn Door |
| Rect Light | 矩形面光 | Barn Door |
| Disc Light | 圆盘光 | — |
| Stage Light | 舞台灯 | 图案片、棱镜、烟雾 |
| Projector | 投影灯 | 图片/视频投影 |

### 通用参数
- **Intensity**: 0~8,000,000 cd
- **Attenuation Radius**: 光照衰减范围
- **Temperature**: 3000K~8000K 色温
- **Color**: 自定义颜色
- **Visible in Reflection**: 反射中可见性

## AI 光照辅助

D5 3.0 的 AI Agent 提供光源辅助调整功能：
- 自然语言指令调整光源参数
- 自动优化场景光照
- 支持区域照明优化和防过曝

*来源: [[src-manual-lighting-environment]], [[src-blog-lighting-environment]]*
