---
title: "Advanced D5 GI with enhanced shadows, reflections, and light bounces"
category: "D5 News"
date: "June 27, 2025"
author: "Hao Wang"
source: "https://www.d5render.com/posts/advanced-d5-gi-ground-truth"
---

# Advanced D5 GI with enhanced shadows, reflections, and light bounces

D5 Render 2.7 comes with an upgraded D5 GI and enhanced reflection algorithms, pushing the quality of real-time preview and output one step closer to Ground Truth.

\*Please note that with the enhancement of ray tracing, scenes from earlier projects may need to be modified. We will provide a detailed walkthrough of the optimizations in this article, enabling designers to better understand the D5 GI and incorporate it into their projects.

‍

## ****Improvements in Direct Lighting****

### Increased limit of artificial light sources in the scene from 1024 to 4096

The new version of D5 introduces Light Grid, an acceleration structure that further enhances the light capacity and sampling efficiency of the lights. This enhancement will not have any impact on old archives.

‍

### Reduced flickering caused by direct lighting (in video rendering)

Benefiting from the light grid technology, it is now possible to sample key light sources more stably in scenes with multiple lights, intense brightness, and complex occlusions. This leads to smoother, more stable, and consistent video rendering, especially evident in illuminating plants during night scenes.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e1dac46e298818a15c0c7_ezgif-3-5b44de5399.gif)

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e203181ceaa312c99f762_ezgif-5-c105dfd75f.gif)

‍

‍

## ****Improvements in Indirect Lighting****

- Interior lighting has been enhanced by incorporating skylight color into the secondary bounces of GI.

- Metal reflections in interior environments become brighter and more precise.

With the introduction of skylight into bounced rays, the GI in interior scenes appears slightly brighter and cooler. The same goes for metal reflections.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6630b53985bd14f3460470ce_2.6%20GI.avif)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6630b890d3c96bc99ac218e2_2.7%20GI%20%E5%8E%8B%E7%BC%A9.avif)

‍

Please note that version 2.7's more accurate GI doesn't inherently cool interiors; it follows your settings. Differences are subtle in new projects and will only be clear when comparing old and new version renders side by side.

‍

### More accurate colors in indirect lighting

In version 2.7, the calculation of GI color no longer averages texture map colors but uses local texture colors directly, with four detailed adjustments for bounced light brightness.

- Realistic contrast and light-shadow details in interior scenes.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e1d0ed04fd80c6d88b266_interior%20backlit.gif)

‍

As shown in the comparison using the same scene file, the new version D5 2.7 exhibits more detailed contrast in the backlit parts of objects, with clearer bounced lighting and darker crevices' occlusion shadows. This is because version 2.7 has higher GI sampling accuracy and more accurate brightness. The new GI is much closer to the realistic representation expected in real life than the old version, in which indirect lighting brightened the whole scene up.

‍

- Richer details in GI for plants.

Following the same principle, details of plants are further improved.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e1e80029301dce4f694b9_2.6%20plant%20gi.avif)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e1e886171df264b2c4aad_2.7%20plant%20gi.avif)

‍

- More realistic bounce lighting for colored textures.

In the old version of D5, the bounced lighting from colored textures was calculated based on the average color of the texture map, resulting in indistinct color differentiation.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e1f1bb17ee6d982b26843_2.6%E9%A2%9C%E8%89%B2.jpg)

‍  
In the 2.7 version, the bounced light color is calculated based on the actual colors of the texture map, achieving a more realistic effect.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e1f308d2cae9757dde738_2.7%20%E9%A2%9C%E8%89%B2.avif)

‍  
**\*Note that for such changes, if you desire an appearance closer to the old version, you can try enabling the "Limit Color Bleeding" option in the material settings to reduce the saturation of bounced light.**

‍

- Increased details in indirect lighting and reflections.

Version 2.7 enhances detail in bounced light and reflections with improved GI algorithms.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e1f68bf9c93c3280f2db5_2.6hezi.avif)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e1f71b9c0894b1b24b0fb_2.7hezi.avif)

‍

### Improved real-time preview

In dimly lit scenes, the spots caused by camera movement are eliminated by the new lighting algorithm in version 2.7, resulting in a more stable and immersive experience.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e2258d04fd80c6d8ceb8b_%E9%BB%91%E7%82%B9%E8%A3%81%E5%89%AA.gif)

‍

### Soft shadows in reflections can now be rendered in videos

Previously limited to image rendering due to high computational cost, rendering soft shadows from multiple light sources in reflections is now available in video renderings for realistic animations.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6630bd2ca32977b3f138158f_Reflections%20of%20Soft%20Shadows%20in%202.6.jpg)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6630bd3d3ee7c5a4916394e6_Reflections%20of%20Soft%20Shadows%20in%202.7.jpg)

‍

**\*Note that for the sake of preview efficiency and effect, soft shadows in reflections are still not supported in the real-time preview, but this effect is calculated correctly in the output images and videos.**

‍

### Light sources produce more accurate Global Illumination (GI)

The upgrade of the GI algorithm also brings more accurate GI representation of lights, which mainly affect the following aspects:

1. The shape of IES lights will accurately affect the GI brightness.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e20e57aef1da0ec052ca9_2.6%20ies.avif)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e21028640cec4bce20656_2.7%20ies.avif)

**‍**

2. The GI of Stage Lights and Projector will change in real time according to their content.

In the old version, the bounced light produced by Stage Lights does not show significant differences based on changes in the Gobo pattern.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e2154650a57bd0765e1bf_2.6%20%E5%BD%A2%E7%8A%B6.avif)

‍

In version 2.7, the bounced light from Stage Lights accurately changes according to the Gobo pattern.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e2165e7a17f6acb480b4e_2.7%E5%BD%A2%E7%8A%B6.avif)

‍

In the old version, the Projector emits white light in addition to the necessary image projection.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6630bd93ccee64dc227a0a7b_Abnormal%20White%20Light%20from%20Projection%20in%202.6.jpg)

‍

In the new version, the Projector provides lighting for image projection only.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6630bda7dc1f2a2aabb7297d_Correct%20GI%20for%20Projection%20in%202.7.jpg)

‍

3. The Attenuation Intensity parameter of Rect Lights correctly affect the GI brightness.

The new "Attenuation Intensity" parameter added to Rect lights and Strip lights is designed to better control the illumination range of Strip Light on walls. In the old version, the "Attenuation Intensity" parameter only affected the direct lighting and did not correctly influence the bounced rays. The new algorithm solves this issue.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e236a6637af1d022590ac_2.6%E8%A1%B0%E5%87%8F.gif)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e237df58e25cc713d3c94_2.7%E8%A1%B0%E5%87%8F.gif)

These above changes are critical and worth noting. It is necessary to generate accurate lighting based on the actual conditions of the light sources. However, when opening earlier scene files having IES lights, Stage Lights, and Projector in D5 2.7, there may be noticeable differences in brightness. In such cases, it is recommended to adjust the light source arrangement, modify the brightness of IES lights, or consider using more suitable IES files according to the specific requirements of the scene.

### ****Note:****

If you are using an older version and have ongoing projects, it is not recommended to upgrade to D5 Render 2.7 at this time to maintain scene consistency. Starting new projects from scratch using D5 Render 2.7 will not encounter these issues, and the new version will provide more accurate rendering results.