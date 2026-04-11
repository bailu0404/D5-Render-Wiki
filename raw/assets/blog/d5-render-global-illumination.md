---
title: "D5 GI | What's Global Illumination and Why We Need It?"
category: "Features"
date: "August 1, 2025"
author: "Hao Wang"
source: "https://www.d5render.com/posts/d5-render-global-illumination"
---

# D5 GI | What's Global Illumination and Why We Need It?

## 01 Preface

### 1.1 What is GI?

Designers often strive to create renderings so realistic that they are indistinguishable from photographs. Detailed modeling plays a significant role in achieving realism, but advanced rendering software capable of accurately simulating light and materials in the real world is essential to take renderings to the next level.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fea476df2e458ac868_greenkitchen.png)

Global Illumination (GI) is the technique in computer graphics that replicates realistic lighting interactions. It calculates not only the direct lighting from a source but also the indirect lighting that reaches a surface after multiple bounces.

In the real world, light continues to bounce off surfaces until its energy dissipates. Simulating this phenomenon is crucial for producing renderings with realistic brightness, contrast, and detail.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c9f6b32dded2f44b4c3c6_Group%2032.png)

GI aims to solve the problem of light bouncing in the scene twice and afterwards, which can bring better brightness and detail to the parts that are not illuminated by direct lighting. It plays a crucial role in creating photorealistic renderings that can trick the human eye.

### 1.2 Why real-time GI?

Given its importance, GI has been a persistent technical challenge in the rendering industry. Over the years, various solutions, including ray tracing, have been developed to implement GI effectively. However, achieving real-time GI is particularly difficult due to the limited computational time available.

- ‍****Offline rendering****: It allows algorithms to spend a significant amount of time solving the indirect lighting of a scene and producing high-quality results. Images in an animated movie, for example, require hundreds of hours of offline computation.****‍****
- ****Real-time rendering****: It has to render at least 30 frames per second, namely one frame within 0.03 seconds.

Real-time GI represents the forefront of rendering technology, offering immediate feedback and enabling seamless creative workflows. [D5 Render](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=global-illumination) has tackled these challenges by developing an advanced GI solution that combines quality and speed.

## 02 The logic behind D5 GI solution

### 2.1 Previous solutions

The rendering equation, introduced by Kajiya, underpins GI algorithms. It models how light interacts with a scene, adhering to the laws of physics and energy conservation. Solving this equation in real-time (less than 0.03 seconds) is highly complex.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fba476df2e458ac769_63c52c7a8cd0753c3c2403ab_5-p-800.png)

Previous real-time GI solutions have issues including light leakage, excessive occlusion and a lot of noise due to inadequate sampling rates.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fea476df2e458ac862_63c52c7bf6343e118c9f1388_6-p-800.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fea476df2e458ac865_63c52c89e7665096fef1ba74_7-p-800.png)

[D5 Render](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=global-illumination) overcame these limitations with a groundbreaking approach called ****ReSTIR Surfel GI****, which delivers high-quality results at real-time speeds.

### 2.2 ****ReSTIR Surfel GI****

#### ****2.2.1 ReSTIR GI****

[D5](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=global-illumination) uses ReSTIR on GI to store the paths of rays rather than sampling light sources. ReSTIR GI reduces the variance of the sampling results by reusing sample information between frames and between neighboring pixels, allowing it to achieve high-quality results even when there're only a small number of samples.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fba476df2e458ac7a1_63c52c8bad4d63a3da09d356_8.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1faa476df2e458ac72b_63c52c7cd5b1e4388492f05d_9.png)

[D5 Render](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=global-illumination) applies ReSTIR to GI by:- Storing ray paths rather than sampling light sources directly.- Minimizing temporal lag with ****Path Validation****, which adjusts reused samples when brightness or object positions change dynamically.

#### ****2.2.2 Surfel GI****

While ReSTIR excels at initial bounces, subsequent bounce calculations present additional challenges. Therefore, the D5 GI solution applied a Surfel Caching solution for subsequent bounce calculations.

Surfel is a spatial caching technique that can be iteratively generated based on screen space and efficiently accumulate and cache irradiance, allowing GI rays to simply query the lighting results for subsequent bounces. However, this solution introduces some new problems, such as being unable to obtain results outside of the screen space.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fda476df2e458ac84e_63c52c7bd4a4c3293847be25_10-p-800.png)

To address this issue, [D5](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=global-illumination) made improvements to the Surfel Caching solution. It generates Surfel from the intersection of the ray emitted by GBuffer, storing the Surfel of the location outside the view and thus obtaining the correct result.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fba476df2e458ac74b_63c52c7b739f8d6e34b6ecab_11.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fba476df2e458ac757_63c52c7cc092f82ba7b4ee70_12-p-500.png)

Besides, the scene is divided into cascadinBesides, the scene is divided into cascading Grids to manage Surfels and thus reduce VRAM usage. Light leakage is solved by sorting and comparing the times of ray bounces. Other artifacts are also improved.g Grids to manage Surfels and thus reduce VRAM usage. Light leakage is solved by sorting and comparing the times of ray bounces. Other artifacts are also improved.

#### ****2.2.3 Other optimisations****

The [D5](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=global-illumination) Team has also developed a series of solutions for multiple light source sampling, reflection, and denoise, allowing the ReSTIR Surfel GI to function efficiently and reliably in various scenarios.

## 03 Improved Global Illumination (GI) for Realistic Rendering

### 3.1 Enhanced Interior Illumination and Color Rendering

The D5 GI solution has been significantly enhanced to incorporate skylight into both primary and secondary GI bounces, resulting in realistic lighting even in spaces with substantial depth.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca0243d4f8d9261ae1eb0_Group%2033.png)

This improvement ensures brighter interiors with smooth transitions between light and shadow. GI calculations now use local texture colors directly, providing more accurate color transitions and enhancing the realism of indirect lighting and reflections. These updates eliminate the overly brightened look of previous versions while achieving realistic color differentiation. Users seeking controlled saturation can enable the "[****Limit Color Bleeding****](https://www.d5render.com/posts/advanced-d5-gi-ground-truth)" option.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6630b53985bd14f3460470ce_2.6%20GI.avif)

**In the older version, interior lighting appeared warmer and metals darker.**

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6630b890d3c96bc99ac218e2_2.7%20GI%20%E5%8E%8B%E7%BC%A9.avif)

**The updated version has neutral color temperature and brighter metals.**

### ****3.2 Realistic Contrast, Shadows, and Color Rendering****

[****The newest version****](https://www.d5render.com/posts/advanced-d5-gi-ground-truth) features higher GI sampling accuracy, delivering better contrast in backlit areas, clearer bounce lighting, and more defined occlusion shadows in crevices. These refinements bring lighting effects closer to real-life expectations, improving both subtle and high-contrast scenarios.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fba476df2e458ac778_677791c43c4f7c8fa3253f3f_663e1d0ed04fd80c6d88b266_interior%2520backlit.gif)

### ****3.3 High-Frequency Shadow Details and Soft Shadows****

Previous versions prioritized strong denoising, leading to flat images. The new GI solution integrates NVIDIA's real-time denoiser and low-variance Restir sampling, offering sharper high-frequency shadow details. Additionally, soft shadows from multiple light sources in reflections—previously limited to still images—are now available for video rendering. While not visible in real-time previews, these shadows are correctly calculated in final outputs, enhancing realism.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca06e2b37723fffff9f74_Group%2034.png)

## 04 Realism Enhancements Across Materials and Textures

### ****4.1 Improved Plant Rendering****

The new [D5](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=global-illumination) GI solution and skylight simulation realistically replicate the semi-transparency of leaves when illuminated, enhancing the natural appearance of plants. [****D5 updated version****](https://www.d5render.com/posts/advanced-d5-gi-ground-truth) improved GI sampling and brightness deliver lighting effects that closely mirror real-life conditions, eliminating the overly brightened look of previous versions.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca0b7cf56707fdaa08ac7_Group%2035.png)

### ****4.2 Emissive Materials as Light Sources****

Earlier versions calculated only the direct lighting of emissive materials, rendering them unsuitable as main light sources. [****On D5 latest version****](https://www.d5render.com/posts/groundbreaking-3d-update-d5-render-2-4-release-note), the GI solution calculates light bounces, enabling emissive materials to perform more effectively as light sources.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca0f2cf56707fdaa0d123_Group%2036.png)

## 05 Enhanced Light Management and Rendering Efficiency

### ****5.1 Increased Light Source Capacity****

The new version introduces a Light Grid structure, raising the artificial light source limit from 1,024 to 4,096. This improves light sampling efficiency without impacting older archives.

### ****5.2 Reduced Flickering in Video Rendering****

Thanks to Light Grid technology, direct lighting is now more stable in scenes with multiple light sources, intense brightness, and complex occlusions, reducing flickering and ensuring smoother video rendering, particularly for plants in night scenes.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fba476df2e458ac79e_677793999cae0c775836e70f_663e1dac46e298818a15c0c7_ezgif-3-5b44de5399.gif)

**In the older version, videos having plants illuminated by a very bright light source had flickers.**

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fba476df2e458ac7a4_677793fa202d5aa733b00ff7_663e203181ceaa312c99f762_ezgif-5-c105dfd75f.gif)

**In the** [**D5**](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=global-illumination) **latest version, stable video rendering of plants in the same night scene.**

### ****5.3 Preview, Rendering, and Animation****

Brightness discrepancies between previews and renders have been resolved, ensuring consistency. Soft shadows in reflections are now supported for video rendering, adding realism to animations.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca13bb684cdbcdf40e472_Group%2037.png)

### ****5.4 Improved Real-Time Preview****

The new lighting algorithm eliminates spot artifacts caused by camera movement in dim scenes, offering a more stable and immersive real-time preview experience. Brightness differences between previews and rendered outputs, an issue in previous versions, have also been resolved.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fba476df2e458ac7b6_677794bde28f5a0d2cffc10d_663e2258d04fd80c6d8ceb8b_%25E9%25BB%2591%25E7%2582%25B9%25E8%25A3%2581%25E5%2589%25AA.gif)

## 06 Improved Light Source GI Representation

### ****6.1 Accurate Light Behavior****

The upgrade enhances GI representation for various light types:

****1. IES Lights:**** Correctly affect GI brightness based on shape.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1f6a476df2e458ac6e8_677798b3e28f5a0d2c030903_ezgif.com-avif-to-jpg-converter%2520(1).jpeg)

**In D5 older versions, IES light bounce doesn't noticeably change with IES file shape variations.**

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1f5a476df2e458ac6cc_67779912f609f1ebe50242a7_ezgif.com-avif-to-jpg-converter%2520(2).jpeg)

**In D5 latest version, the bounced light from IES lights accurately changes according to the shape of IES files.**

‍

****2. Stage Lights and Projectors:**** Real-time GI updates according to content, including Gobo patterns for Stage Lights and accurate projection lighting for Projectors.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/663e2154650a57bd0765e1bf_2.6%20%E5%BD%A2%E7%8A%B6.avif)

**In the old version, the bounced light produced by Stage Lights does not show significant differences based on changes in the Gobo pattern.**

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1f5a476df2e458ac6d3_6777983f451ab49ece2ff8a1_ezgif.com-avif-to-jpg-converter.jpeg)

**In D5 latest version, the bounced light from Stage Lights accurately changes according to the Gobo pattern.**

‍

****3. Rect and Strip Lights:**** New "Attenuation Intensity" parameter accurately influences GI brightness and illumination range.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1fba476df2e458ac77b_677795c7ac8a567a46d257f3_663e236a6637af1d022590ac_2.6%25E8%25A1%25B0%25E5%2587%258F.gif)

**In older version, indirect lighting could light up the wall even with a low attenuation intensity.**

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688ca1ffa476df2e458ac88f_6777964b60878581ba03f903_663e237df58e25cc713d3c94_2.7%25E8%25A1%25B0%25E5%2587%258F.gif)

**In D5 latest version, the bounced light is accurately calculated based on the actual attenuation intensity.**

## 07 Important Notes for Transitioning to The Latest Version

For ongoing projects, it is recommended to retain the current D5 version to maintain consistency. Starting new projects with [****D5 Render updated version****](https://www.d5render.com/download) will ensure optimal results and accurate rendering. When updating older scene files, adjustments to light arrangements and brightness may be necessary to account for enhanced GI accuracy.