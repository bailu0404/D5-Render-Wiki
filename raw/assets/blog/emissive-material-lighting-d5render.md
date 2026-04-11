---
title: "How to Use Emissive Material in D5 for Better Lighting?"
category: "How to"
date: "August 15, 2025"
author: "Hao Wang"
source: "https://www.d5render.com/posts/emissive-material-lighting-d5render"
---

# How to Use Emissive Material in D5 for Better Lighting?

[Embedded video](https://www.youtube.com/embed/8_V_NTaT7FE)

**In D5 Render, there are two ways to set up the overall lighting for the scene:   
1. Geo & Sky system to simulate the sunlight situation in real world.  
2. HDRI system to choose from default HDRIs for different time periods/weather conditions.**

**Apart from these two sunlight settings, an archviz professional would take it one step further with emissive lights.  In this article, we'll talk about the use of Emissive Materials in D5 Render, and how it makes your 3d rendering more** ******realistic****** **and** ******atmospheric********.**

## What is emissive material

When it comes to lighting in rendering, we are not unfamiliar with adding light sources, be it point light, spotlight or rectangular light. However, there's one more trick that a lot of architects miss out on, which is emissive material.

**Emissive** material refers to the kind of ****self-illuminated**** material, emitting light across its surface. Although it may sound like another type of light source, there are certain differences:

- Light rays coming from emissive materials do not have subsequent bounces as artificial light sources do, which leads to a smaller range of illumination.
- The lighting effect of emissive material is somewhat similar to ****LED lights****, so you can simply turn anything into a glowing light source by applying emissive material to the objects regardless of size or shape. This has opened up more possibilities, becasue artificial light sources usually don't include irregular shapes, and it can be time-consuming to manually add light strips for an extended area.
- Emissive lighting also works like a charm when adding glow to surfaces like ****television screens**** or other ****electronic devices**** that are supposed to give off light.

When ****Bloom**** effect is turned on, your'll find a ****dazzling glow**** to the emissive materials in the scene, taking the rendering up a notch. For facade rendering in archviz, you can turn on Emissive with a little bit of intensity for the glasses or part of the structures of the architecture to glow beautifully in aerial view.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c777c913433f6ce61113a_634396d9c2d4ac392e57ca89_578335_dad8b945a1864d859a8f9510fb46826a_mv2.webp)

In a word, using emissive material is an effective and low-cost way of making illuminated objects and lighting up a certain area.

## Where and How to use emissive material

No custom maps. No material nodes. In D5 Render, emissive is a button in material editing tab. So you can just switch on "Emissive" for any material you picked to make it glow. Adjustable paramters include:

****Intensity****, controls the luminous intensity.****Emissive color****, controls the color of light emitted by the emissive material.(You can change its color by RGB, HSV, or HEX, or use the 'Color Picker' in the shape of a dropper in the 'Color' menu to get any color shown in the scene. Color temperature is available as well.)****Cast Shadow****, controls whether or not the emissive material participates in lighting (diffuse light) calculations. When this option is turned on, the material will be visible in camera and other material reflections, but it will no longer cast shadows and bounce light.

### How to make/use emissive materials in D5 Render:

#### Decorate a night scene with emissive neon light signs

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7779913433f6ce61108c_6343978123de296e53e397c0_578335_46f467e679254ae485eef0eb5d4317bd_mv2.webp)

Neon light signs are part of a prosperous urban night street, and to create a lively night city render, you can try emissive materials.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c777a913433f6ce6110d5_634397f4941d59e49e25929a_578335_dd173b4ac94544f8b757cdecd49e532b_mv2.webp)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c777a913433f6ce611110_63439804b9d4ce8fa5b70bfc_578335_d35d5088dfda46a69a44af1af9e3f36b_mv2.png)

#### Use emissive materials with light sources to light up the whole scene

This is especially helpful when you want to create various kinds of lamps. In this rainy open courtyard, switch on Emissive for the lamps, and adjust the temperature to a warm yellow tone, so the scene does not look too cold.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c777c913433f6ce611137_6343983d941d59478f259436_578335_fa07b0caa8ed4ab9ba92c7b4f002ab68_mv2.webp)

Then let's add 3 point lights upon the emissive materials to illuminate the pavilion and surrounding plants, making them stand out from the dark background. Adjust parameters including intensity, attenuation radius and temperature properly to match the overall atmosphere. If you want a softer shadow cast on the wall, pull the Light Source Radius higher.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c777c913433f6ce611141_6343985a859df6eaf19c0083_578335_27a2ad3ce812472d8a0d398adebce218_mv2.webp)

‍

#### Light up a specific area with emissive material for a better balance of the scene

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c777a913433f6ce6110bf_6343989d44f1dc740c89f915_578335_39b8b3a8c6184b4983551fdfaeb58d47_mv2.webp)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c777a913433f6ce6110e1_634398ad98f0f6a8bf5f303a_578335_f4c1250ae03d43f49a2f5c51fe457a39_mv2.webp)

Lighting is an efficient method to enhance the sense of depth for a scene. While emssive materials alone can't light up the main building far away from the camera, they are just right for lamps close by as supplementary lighting for the whole scene. Turning off emissive would make the scene look dark and dull, and if you use light sources instead, it might distract attention from the visual focus.

## Showcase

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c777c913433f6ce61113d_634398fc22ea714f5e418cfd_578335_d0a556b8864d46dd822c9bec3ab08551_mv2.webp)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c777a913433f6ce6110b0_634398fa76d01447fa220ccb_578335_7ec97eccd7f5459fbe9103bf74fde048_mv2.webp)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7779913433f6ce611092_634398fa1a977d52ff9d9575_578335_552c9bd7a80f4183a5aa25e983ee1ce9_mv2.webp)

You can download the two demo scenes [****City Street****](https://forum.d5render.com/t/scene-express-vol-118-d5-render-2-3-trailer-video-demo-scene-city-street-by-showing-inspiration/11497), [****Rainy Courtyard****](https://forum.d5render.com/t/scene-express-vol-140-free-d5-render-scene-of-rainy-courtyard/11964)on D5 Forum for free.