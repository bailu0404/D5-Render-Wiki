---
title: "CN Manual — AI Features (docs.d5render.cn/ai)"
created: 2026-04-20
updated: 2026-04-20
sources:
  - raw/cn/manual/ai.md
  - raw/cn/manual/ai -- 1148.md
  - raw/cn/manual/ai -- 7fa4.md
  - raw/cn/manual/ai -- 6d0a.md
  - raw/cn/manual/ai -- 293a.md
  - raw/cn/manual/ai -- ai-atmosphere-match.md
  - raw/cn/manual/ai -- ultra-hd-texture.md
  - raw/cn/manual/ai -- make-seamless.md
  - raw/cn/manual/ai -- a7f9.md
  - raw/cn/manual/ai -- 6080.md
  - raw/cn/manual/ai -- 7abe.md
tags: [cn, ai, material-generation, atmosphere-match, design-assistant, ultra-hd]
---

CN documentation for D5's AI feature suite, covering Design Assistant, AI material tools, image post-processing, and operational notes. Source: docs.d5render.cn/ai.

## AI Features Overview

CN manual organizes AI features into:
- AI 设计助手 (AI Design Assistant)
- AI 材质生成与推荐 (AI Material Generation & Recommendation)
- AI 图像后期 (AI Image Post-Processing)
- 氛围匹配 (Atmosphere Match)
- 材质超清纹理 (Ultra-HD Texture)
- 材质无缝化 (Make Seamless)
- AI 材质通道图生成 (AI Material Channel Map Generation)
- AI 材质模板识别 (AI Material Template Recognition)

## AI Design Assistant (AI设计助手)

Accessed via the AI panel. Supports natural-language commands to control scene lighting and elements. Example commands from official documentation:

- "场景右边区域太暗了，调亮一点" (The right area is too dark, brighten it a bit)
- "请帮我优化场景中的灯光" (Please optimize the lighting in the scene)
- "关闭客厅的全部光源" (Turn off all light sources in the living room)
- "调整为色彩斑斓的灯光氛围" (Set a colorful lighting atmosphere)

The AI Design Assistant launched in D5 2.11 with three sub-tools:
- **花境生成器** (Flower Garden Generator): climate/geography-aware planting
- **智能苗木清单** (Smart Seedling List): automated plant inventory and cost estimation
- **D5 Bot**: in-app AI support chatbot for software questions

*Source: raw/cn/manual/ai -- 1148.md*

## AI Material Generation & Recommendation

Entry point: **Asset Library → Online → Materials → "AI Material Generation"** section.

**Workflow:**
1. Upload a reference image (max 6K resolution on the shortest edge; ≥2048px shortest or ≥4K longest sides already not supported for ultra-HD, but upload itself accepts images for material generation)
2. Choose to generate from the full image or select a specific region
3. AI analyzes the image content and generates a high-quality, immediately-usable PBR material
4. Apply to the current scene immediately, or save to local library for reuse
5. D5 additionally recommends similar materials from the online library based on the image's material characteristics

**Quota**: Material generation is counted within the **Community Edition 50-use limit** per quota period.

*Source: raw/cn/manual/ai -- 7fa4.md*

## AI Material Channel Map Generation

Generates individual PBR channel maps (roughness, metallic, normal, etc.) from a base color image using AI analysis.

*Source: raw/cn/manual/ai -- a7f9.md*

## AI Material Template Recognition

AI automatically recognizes the material type of an uploaded image and maps it to the appropriate D5 material template (e.g., glass, metal, wood, fabric).

*Source: raw/cn/manual/ai -- 6080.md*

## AI Image Post-Processing

Full AI post-processing workflow for rendered images. Feature accessible from the render output panel.

*Source: raw/cn/manual/ai -- 293a.md*

## Atmosphere Match (氛围匹配)

AI-driven atmosphere matching that adjusts the scene's lighting, sky, and post-processing to match a reference image's mood.

**Usage notes:**
1. **Composition**: Framing with a significant sky proportion yields the best results
2. **Processing time**: Depends on network download speed; allow time to complete
3. **Accuracy**: The system applies both local and global matching — can set lighting/post-processing based on a reference image or adapt environment conditions to the reference's atmosphere

*Source: raw/cn/manual/ai -- ai-atmosphere-match.md*

## Ultra-HD Texture (材质超清纹理)

Upscales texture maps to ultra-high resolution using AI.

**Limitations (not supported when):**
- Material has no base color texture map
- Material is from the D5 online asset library (no upscaling needed/supported)
- Image shortest edge ≥ 2048 px, OR longest edge ≥ 4K

*Source: raw/cn/manual/ai -- ultra-hd-texture.md*

## Make Seamless (材质无缝化)

AI converts a non-seamless texture into a tileable seamless texture.

**Limitation**: Not supported when there is no base color texture map.

*Source: raw/cn/manual/ai -- make-seamless.md*

## AI Model Generation

AI-powered 3D model generation from text or image prompts. Entry: Asset Library → AI area.

*Source: raw/cn/manual/ai -- 7abe.md*

## See Also

- [[ai-capabilities]] — AI features overview (English wiki)
- [[src-cn-manual-account]] — AI credits and quota details
- [[src-cn-news]] — CN news (AI Design Assistant launch coverage)
