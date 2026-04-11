---
title: "How to Render Glass Materials?"
category: "How to"
date: "August 7, 2025"
author: "Hao Wang"
source: "https://www.d5render.com/posts/all-you-need-to-know-about-glass-material-in-d5-render"
---

# How to Render Glass Materials?

******Table of content******

- Adjustable parameters of glass material in [D5 Render](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=all-you-need-to-know-about-glass-material-in-d5-render)
- How to make fluted glass
- How to make black-tinted glass
- How to make frosted glass
- Rendering showcase

Glass is one of the most common materials in modern architecture/interior design. It is like a bridge connecting the exterior and interior spaces. Though creating beautiful glasses with clear reflection and refraction might be hard in traditional rendering engines, it's actually a piece of cake in D5 Render.

In this article, we are going to introduce in detail how you can make the glass material you need in [D5](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=all-you-need-to-know-about-glass-material-in-d5-render).

## ****Adjustable parameters of D5 glass material****

### Thickness

Basically, there are two ways of modeling: one is solid-modeling, which means building models in a geometrically correct way; the other is surface-modeling with only visible facets in order to keep the model file light.

When glass materials are applied onto the latter, they may have incorrect refractions. To fix this, you don't need to model in DCC software again. Turn on the "Thickness" option in [D5 Render](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=all-you-need-to-know-about-glass-material-in-d5-render) instead. The glass will immediately have a correct refraction, which is quite convenient.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c6b67a51acf74d502e193_6395db88d27fb658ad567ce8_Thickness_off-transcode-ezgif.com-video-to-gif-converter.gif)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c6b7dc7b3ebcce41ec69d_6396976a67bb25c25afd7f49_Thickness_on-transcode-ezgif.com-video-to-gif-converter.gif)

‍

### Transparency

By adjusting Transparency, you can decide how much light can pass through the glass material.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c62fea45fb2cf45d4d_6395dd20883c85edebdf8da1_Transparency.png)

Achieve stunning effects like colored gradient glass by enabling the 'Affected by Light' option. Adjusting the opacity value and using black-and-white maps to control the opacity pattern allows for dynamic light interaction.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c62fea45fb2cf45d50_6690a8f1cdf7bef71422a58e_%25E5%258D%258A%25E9%2580%258F2.gif)

### Roughness

It controls how smooth the glass surface is.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c62fea45fb2cf45d59_6395dd22eaa1f273431dbdc2_Roughness.png)

For now, the effect of frosted glass made with Roughness may not be evident. So we'll introduce a method of making it in the later part of "how to make frosted glass".

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c62fea45fb2cf45d63_6395dd224389cb50b7e6bdf7_Frosted_Glass.png)

### Specular

The Specular parameter influences how much light will be reflected by the glass material.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c6c92ae2729ccb0dacd10_6396b518aa7b425cc542e864_12121-transcode-ezgif.com-video-to-gif-converter.gif)

### Color

You can create solid-colored glasses by changing the base color, or gradient-colored glasses with a map.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c6ca362e133c79827ebf2_6395e432831ce2c889b4fb01_Coloredandgradientglass-transcode-ezgif.com-video-to-gif-converter.gif)

## How to make fluted glass

Observing the glass facades in the real world, we can see that they have a reflection looking like waves. That's because glasses usually have slight bumps on their surface due to the processing technology.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70bd2fea45fb2cf45ce1_6395e4b74389cb65bae73417_%25E7%2585%25A7%25E7%2589%2587.jpeg)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c02fea45fb2cf45cfa_6395e4b8831ce23a33b4ffb7_%25E7%2585%25A7%25E7%2589%25872.jpeg)

So, how to achieve this effect?

You just need one ****Normal map****.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c42fea45fb2cf45d23_6395db63d27fb64db1567a1b_%25E6%25B3%2595%25E7%25BA%25BF.png)

Take this building for example. To simulate those wavy reflections in glass, you just need to import a Normal map, reduce its UV value, and ****increase the**** ****Normal Intensity**** ****a bit****.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c6d09a51acf74d503975b_Group%2026.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c62fea45fb2cf45d4a_6395e69dd53b2cd04f98350f_Unknown2.png)

A normal map can also play magic when you want to make fluted glasses.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c62fea45fb2cf45d86_6395db67d27fb664d8567a7f_%25E9%2595%25BF%25E8%2599%25B92.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c62fea45fb2cf45d3a_639694484d8563a5ed74f9f9_%25E9%2595%25BF%25E8%2599%25B92.png)

These tiny changes could be the finishing touch on your scene.

## How to make black-tinted glass

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c62fea45fb2cf45d69_6396925d027db0273b1de5f7_236.png)

Actually, it's quite easy to make a gradient glass facade as shown above.

First offset the surface of the facade model. Change the material of the offset surface to Custom with a black-to-white normal map.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c6d51a51acf74d503cf63_639692cbd53b2cc44ea7ea05_-transcode-ezgif.com-video-to-gif-converter.gif)

After importing it into [D5 Render](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=all-you-need-to-know-about-glass-material-in-d5-render), you can give the offset surface the texture of Cloth. Then add a black-to-white gradient map into the Opacity column. Align the surface model and the facade model.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c42fea45fb2cf45d20_6395db646204a08576979929_%25E5%258D%258A%25E9%2580%258F1.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c42fea45fb2cf45d26_6395db662721b3d6567a5dc0_%25E5%258D%258A%25E9%2580%258F2.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70c62fea45fb2cf45d73_6395db63eaa1f24a391d9a36_%25E5%258D%258A%25E9%2580%258F3.png)

## How to make frosted glass

Here's a trick to make frosted glass in [D5 Render](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=all-you-need-to-know-about-glass-material-in-d5-render):

Add a Normal map, stretch its UV and turn up the intensity.

Done! That's all you need to do.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70796fa9d0a8ac62eb53_63969654d53b2c7cbba83dab_2-transcode-ezgif.com-optimize.gif)

Here's the Normal map we used in the article:

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c70abca473988eb2c33d6_Group%2027.png)