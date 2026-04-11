---
title: "What's real-time Subsurface Scattering and why you need it"
category: "Features"
date: "August 15, 2025"
author: "Hao Wang"
source: "https://www.d5render.com/posts/d5-sss-translucent-materials"
---

# What's real-time Subsurface Scattering and why you need it

## 01 Preface

### 1.1 What is Subsurface Scattering?

In the article [D5 GI | Pursuing offline rendering quality with real-time experience](https://www.d5render.com/post/d5-render-global-illumination), we briefly explained how light bounces off the surface of objects in the real world. Whether this phenomenon can be replicated decides how close the rendering result could come to photos.

Yet it doesn't stop there. When lights hit the surface of some ****translucent**** object, such as wax or marble, some of them will pass through the surface, scatter inside the object and finally exit at different points on the surface. Viewed from a camera, the object inside seems to be "lit up".

This is what we call ****Subsurface Scattering (SSS or 3S for short)****. As shown in the following picture, "sub-surface" refers to the part underneath the surface.

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb3bf_63edaaef1cd7f36b27248dbe_%25E5%258A%25A8%25E7%2594%25BB%2520(1).gif)

‍

### 1.2 What can Subsurface Scattering do?

Mere reproduction of light bouncing off the surface, though enough for most materials, cannot create a good translucent effect for textures including jade, fruit and human skin. That's why we need Subsurface Scattering here to bring more realism. ****The interaction between the light and the sub-surface of tranluscent materials will also breathe life into your scene.****

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66352fea45fb2ced6b2a_Group%2025.png)

In a word, SSS in rendering can improve the material quality, making it look more delicate. A translucent material won't look pitch-black even when it's backlit, thus the scene will be clearer and brighter.

Luckily, this powerful feature will come with D5 Render 2.4. Make sure to give it a try and you'll find that the rendering is taken up a notch.

## 02 The Principle of Subsurface Scattering in D5

### 2.1 Previous solutions

As mentioned above, achieving SSS in rendering, especially in real-time rendering within 0.03 seconds, is a huge challenge due to its large amount of computing. That's why SSS is thought to be an advanced feature of rendering tools.

Look at the prevailing real-time rendering tools on the market, we can find that most of them either lack the SSS feature or use Screen-Space Subsurface Scattering as a substitute.

Screen-Space Subsurface Scattering strikes a balance between speed and quality, which makes it ****a good, yet not perfect, solution**** for real-time rendering. For example, it will fail to compute light info when there are materials occluding the target material. Banding artifacts will appear when you set a large screen to scatter radius.

It seems that current real-time SSS rendering solutions are insufficient in addressing the challenges of practical application and possess various technical limitations and shortcomings that hinder optimal visualization for designers. As such, the D5 team has developed a superior real-time Subsurface Scattering solution, which is known as D5 SSS.

Therefore, real-time SSS still remains a challenge despite many existing solutions. To overcome the technical issues and offer designers better visualization experience, the D5 Team decided to develop their own solution -- ****D5 SSS**** -- for real-time rendering.

### 2.2 D5 SSS

After surveys of techniques and demands, the D5 Team decided to combine the offline rendering algorithm with real-time rendering to achieve real-time SSS.

Random Walk is an offline physically accurate algorithm for SSS that considers how light scatters and travels through the medium within a model, leading to a more accurate display of model volume and surface thickness.

To address this issue, the D5 Team integrated Random Walk SSS into D5's unique hybrid rendering pipeline. By reusing the information of GBuffer, accumulating noise reduction in the time domain, and utilizing hardware acceleration through DXR, the D5 SSS solution ensures high-quality SSS in real time.

In this way, designers only need to tweak a few parameters and they will be able to preview the SSS effect of translucent materials in real time. What's more, D5 SSS ensures consistency between preview and rendering, offering designers a smooth and superb visualization experience.

## 03 D5 Subsurface Scattering Effect and Practice

### 3.1 Where can D5 SSS be used?

The newly added feature of real-time SSS will make D5 Render 2.4 a more advanced rendering tool for different industries.

****For architects****, you can create clear marble or slate materials to better display design ideas, thus making your project more attractive.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb36c_63db8dadb0ab40c69ca8edcb_4.png)

Instead of blocking out all light, the slightly transparent marble slab looks soft and clear.

****For interior/product designers****, you can better deliver the translucent effect of ceramics and jades to improve the visual quality.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f5e35ae05427ceb323_63db8dad7e08da2ab13329a7_5.png)

### ****3.2 How to use D5 SSS****

To create a translucent material, first use the hotkey "I" to select the texture. Go to Inspector > Material Template. There you will find "Subsurface Scattering".

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66efe35ae05427ceb2de_63db8dacef8abaf29dd07cce_6.png)

SSS template has two more parameters than the Custom template:

1. SubSurface Color

2. Scattering Intensity

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66efe35ae05427ceb2e4_63db8dac4bea1bca3cba1e05_7.png)

Furthermore, there are three parameters that are commonly used for SSS materials:

1. Base Color/Base Color Map

2. Specular

3. Roughness

Here we use "jade" as an example to show how to create SSS materials in D5 Render.

#### Initial look

This rabbit has a custom material with a white base color. We set Specular and Roughness to 0, so they won't affect the following process.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb35c_6569c120909cb9881f050f94_sss-initial%2520state%25201%2520(2).jpeg)

#### Base Color/Base Color Map

First, add a texture map of jade to Base Color Map.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f5e35ae05427ceb329_63db8daf6187930100e6d8d7_9.jpeg)

Turn on "Triplanar", so we can get a nice UV effect without having to set it manually.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb36f_63db8db0a21f7911a1d54fe8_10.gif)

#### ****Subsurface Scattering Settings****

Change the material template to "Subsurface Scattering".

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb372_63db8db0cd4604f9ad5ce2c4_11.png)

- ****SubSurface Color****

The Base Color/Base Color Map defines the color of the surface, while SubSurface Color decides the color when light scatters inside the model.

By default, the "SubSurface Color" is 50% grey. In this case, the material begins to have an SSS effect, but it needs some color to look more obvious.

Change the "SubSurface Color". We can see how it affects the material:

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb3c9_63db8ead29a69e52e492824a_12.gif)

The SubSurface Color appears to be emitted from the model inside and is more visible in the shadows.

The SubSurface Color essentially controls how far the light is scattered inside the model. The larger the RGB value, the more visible the scattered light in red, green or blue will be, and the more translucent the material will appear.

- ****Scattering Intensity****

The Scattering Intensity is a multiplier of the SubSurface Color. It increases/decreases the distance the scattered light travels on the basis of SubSurface Color, further enhancing or reducing the translucent effect of the material.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb38d_63db8eacc8f8240fb3aaf8e3_13%2520(3).gif)

In this example, we are creating a realistic jade material, so the "SubSurface Color" is set to a low saturated green and the "Scattering Intensity" is left at its default value of 1.0.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb390_63db8db0ac6dec1a3d63a29f_14.png)

#### ****Specular and Roughness****

Jade and gemstone are highly reflective non-metallic materials and typically have a Specular value of 1.0.

> **The "Specular" parameter controls the reflectivity of non-metallic materials. Most non-metallic materials have a reflectivity between 0.25 and 0.625. For example, water with 0.25 and jade/gem with 1.0.   
> More info about Specular:** [**Material Template > Map > Specular**](https://support.d5render.com/support/solutions?type=4)

When Specular is set to 1.0, the model looks more like jade.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb37e_63db8db124c0a668a5cc50a0_15.png)

Roughness decides how rough the material surface is, affecting whether the reflection is blurred or not. By changing its value, we can clearly see how the jade texture changes.

With high Roughness, the jade looks like an unpolished one; with low value, especially when it's close to 0, a highly polished one.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb396_63db8ead28204d2129132e0a_16.gif)

We set the Roughness at 0.05 and here's the final rendering:

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb3c3_63db8db375590167866a17d6_17.png)

### ****3.3 Notes****

For now, D5 Render supports point light, spotlight, rectangular light and sunlight for the SSS effect. HDRI ambient lighting for SSS will be included in future updates.

#### ****Accurate size****

The look of SSS material is influenced by the model volume and thickness. So the smaller and thinner the model, the more translucent it will be for the same parameters.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c66f9e35ae05427ceb399_63db8db2f50503ed8fd1a0e7_18.png)

Therefore, it is recommended to model at the size of real objects. For example, don't model a jade decoration too large. A few centimeters are just appropriate. If you want to further increase or decrease the translucency of the material, use the SubSurface Color brightness or Scattering Intensity to adjust its visual effect.

## 04 Conclusion

The capability of D5 Render 2.4 to realize real-time SSS will provide architects, interior and product designers with much more realistic renderings. Now, they have opportunities to create more kinds of materials, which makes visualization an enjoyable journey.

For D5 Render, D5 SSS is a milestone, but never a terminus. The D5 Team will keep optimizing SSS to bring better effects. Stay tuned and you won't be disappointed.

D5 Asset Library has updated dozens of models with SSS materials, including fruits, candles and jades. You can quickly find them by searching "sss/3s".

Or, you can customize your own translucent materials and enjoy the beauty of flowing light in real-time rendering.