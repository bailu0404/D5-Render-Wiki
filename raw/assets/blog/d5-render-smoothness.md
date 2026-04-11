---
title: "D5 Smoothness｜Large Scene Capability and Real-time Interactivity"
category: "Features"
date: "October 7, 2024"
author: "Hao Wang"
source: "https://www.d5render.com/posts/d5-render-smoothness"
---

# D5 Smoothness｜Large Scene Capability and Real-time Interactivity

Real-time interactivity with photo-realism quality is the core value of D5 Render. [D5 GI ensures the performance of real-time rendering](https://www.d5render.com/post/d5-render-global-illumination/), but as the complexity of the scene increases, the rendering overhead will gradually increase and the real-time FPS inevitably decrease.  
With a large number of faces, lights, models and textures, whether D5 can still guarantee responsiveness and FPS in real-time is of great importance for the user experience.

### Optimization of Model loading

Many 3D assets have an extremely large number of faces, and some consist of countless sub-objects that affect rendering efficiency. D5 Render automatically merges models of the specific kinds of asset, combining multiple small models into one large model for a reduced DrawCall\* and improved efficiency.

Since D5 version 2.0, models have been loaded with a more efficient polygon rendering method, which has greatly improved real-time performance. Version 2.0 has seen a significant improvement in FPS and responsiveness comparing with version 1.9.

\*DrawCall: The rendering command sent from CPU to GPU. Too many DrawCalls will cause the GPU to wait for a long time and hinder the efficiency.

### Optimization of Material Texture

The new version of D5 Render uses Texture Streaming to dynamically load texture maps, ensuring that material textures are loaded only when they are in the camera, and store other textures temporarily on the disk. This technique, together with mipmap, ensures that material textures look just right at all distances with minimal overhead.

In a comparative test, both RAM and VRAM usage are reduced and frame rate is slightly improved with texture streaming enabled. For some scenes, the memory usage was saved by more than 40% (from 11G to 6.2G).

‍

### Optimization of Scenes with Many Lights

In general, the number of light sources will have a direct impact on the live preview responsiveness (frame rate).

In this night scene below, there are several hundreds of light sources:

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6703b0a888bdb0c593586a04_63c0fa0763fad4b232bcddde_633c5ac26e5bff640e61f65c_578335_f097459e3363496c98111827842a3e1a_mv2.webp)

In the old version, the memory cannot be dynamically allocated according to the number of lights when calculating shading, so it must be allocated in advance according to the maximum number of lights (e.g. 1024 lights). Higher screen resolution means higher memory overhead, which poses a challenge to the performance of the real-time preview.

To solve this problem, D5 optimized the strategy of sampling lights. First, D5 divides 1024 lights into groups, calculating the total brightness of lights in each group, and then further sampling the specific lights in the groups that contribute more to the scene. With this optimization, the time of calculating GI for a scene with 1024 lights drops from 23.84 ms to 11.54 ms, and memory usage is reduced by about 150MB.

‍

### Optimization of GI algorithm

The optimization of the new D5 GI sampling algorithm above will also improve the frame rate for large scenes. Version 2.1 is enabled with 2-4 times faster reflection calculations and nearly 4 times faster GI calculations. That's why D5 2.1 always has a higher frame rate than 2.0 in the same scene.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/6703b0a888bdb0c5935869f7_63c0f9a0370b51e8e6562ffb_devide.png)

‍

## ****D5 "Smoothness" Summary****

“Smoothness” can be measured with 2 indicators:

- ****The time between the mouse click on the user interface to the first frame of response from the D5 viewport preview.****
- ****The frame rate for real-time rendering when the viewport changes dynamically.****

The example below shows a comparison of the "smoothness" of D5 version 1.9 and D5 version 2.1:

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/63c0fa08f02e2d7eb8730b82_633c5c5a79cc77304ecf9903_smooth.gif)

Note: You can see that the new version of D5 on the right responds to commands (click to move camera views) significantly faster than the old version (it always moves faster than the left one). And, the frame rate of the new version is nearly doubled when shaking the viewport.

‍