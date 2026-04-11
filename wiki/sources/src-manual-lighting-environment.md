---
title: "Manual: Lighting & Environment"
created: 2026-04-11
updated: 2026-04-11
sources:
  - "raw/assets/manual/user-guide -- lights.md"
  - "raw/assets/manual/user-guide -- lights -- what-types-of-light-sources-are-offered-by-d5.md"
  - "raw/assets/manual/user-guide -- lights -- what-are-the-meanings-of-each-parameter-in-the-light-panel.md"
  - "raw/assets/manual/user-guide -- lights -- how-to-edit-multiple-lights-at-once.md"
  - "raw/assets/manual/user-guide -- lights -- how-to-make-a-light-invisible-in-the-reflection.md"
  - "raw/assets/manual/user-guide -- lights -- other-faqs.md"
  - "raw/assets/manual/user-guide -- environment.md"
  - "raw/assets/manual/user-guide -- environment -- sky.md"
  - "raw/assets/manual/user-guide -- environment -- weather.md"
  - "raw/assets/manual/user-guide -- environment -- other-common-issues.md"
  - "raw/assets/manual/user-guide -- effect.md"
  - "raw/assets/manual/user-guide -- effect -- how-is-ao-used-in-style.md"
  - "raw/assets/manual/user-guide -- effect -- how-is-z-depth-used-in-style.md"
  - "raw/assets/manual/user-guide -- effect -- how-to-use-lut.md"
  - "raw/assets/manual/user-guide -- effect -- what-effects-can-each-of-the-parameters-in-post-processing-achieve.md"
  - "raw/assets/manual/user-guide -- effect -- how-to-save-and-reuse-environment-and-post-effect-presets.md"
tags: [manual, lighting, environment, sky, hdri, weather, effect, post-processing]
---

D5 Render 用户手册的光照、环境与特效章节，涵盖 7 种光源类型、天空系统、天气效果和后处理参数。

## 光源类型

D5 Render 提供 7 种光源：

### 基础光源
1. **Point Light** — 点光源，模拟灯泡，均匀向各方向发光
2. **Spotlight** — 聚光灯，锥形角度内发光，支持 IES 文件
3. **Strip Light** — 条形灯，可调长宽，带 Barn Door 挡光板
4. **Rect Light** — 矩形面光源，模拟矩形发光区域

### 扩展光源
5. **Disc Light** — 圆盘光源，柔和均匀照明
6. **Stage Light** — 舞台灯（Widget），支持图案片、棱镜分光、烟雾效果
7. **Projector** — 投影灯（Widget），支持图片/视频投影

## 通用光源参数

| 参数 | 说明 |
|------|------|
| Intensity | 发光强度，单位 cd (坎德拉)，最大 8,000,000 |
| Attenuation Radius | 衰减半径，范围外停止光照计算 |
| Visible in Reflection | 控制光源是否出现在反射中 |
| Temperature | 色温 (K)，3000K 偏黄，5500-6500K 白光，8000K 偏蓝 |
| Color | 自定义光源颜色 |

### 特殊参数
- **Point Light**: 光源半径（影响阴影柔和度）
- **Spotlight**: IES 文件、锥角
- **Strip/Rect Light**: Barn Door Angle (0°-90°) 和 Barn Door Length (0-100)
- **Stage Light**: 图案、棱镜分光、旋转、烟雾
- **Projector**: 投影画面/视频、UV 控制、薄雾效果

## 天空系统

### Geo Sky（地理天空）
基于地理位置精确模拟太阳角度：
- **North Offset**: 校正北方方向
- **Time / Date**: 时间和日期
- **Latitude / Longitude**: 经纬度坐标（十进制度数）
- **自定义参数**: 太阳强度、太阳盘半径、月光强度、月亮盘半径、星光强度
- **[[caustics|Caustics]]**: 太阳焦散，需同时在材质和光源端启用

### Custom（自定义天空）
- 白天: 太阳强度、高度角、方位角、焦散
- 夜间: 月光强度、月亮盘半径、月相、月相方向、高度角、方位角、星光强度

### HDRI

[[hdri-lighting|HDRI]]（高动态范围图像）不仅是背景，还照亮整个场景：
- **Light**: 整体亮度控制，分别调节 Skylight（漫反射光）和 Background（背景亮度）
- **Rotate**: 旋转 HDRI 环境
- **Flip Horizontal**: 水平翻转
- **Sky Temperature**: 天空色温，默认 6500K
- **Sky Color**: 色相和饱和度调整
- **HDRI Resolution**: 支持 2K、4K、8K 和实际分辨率

## 天气效果

- **Fog**: 雾效，支持体积光
- **Rain**: 雨天效果
- **Snow**: 雪景效果
- **Volumetric Cloud**: 体积云 (3.0+)，支持预设和密度/海拔调节

## 后处理特效

### AO（环境光遮蔽）
在 Style 面板中使用，增强角落和缝隙的阴影细节。

### Z-Depth（Z 深度）
在 Style 面板中使用，基于深度的效果控制。

### LUT
查找表颜色分级，支持自定义 LUT 文件。

### 后处理参数
- **Exposure**: 曝光
- **Contrast**: 对比度
- **Highlight / Shadow**: 高光/阴影
- **White Balance**: 白平衡
- **Vignette**: 暗角
- **Chromatic Aberration**: 色差
- **Bloom**: 泛光
- **Color Grading** (Widget): 精确控制中间调、阴影、高光和全局色调
