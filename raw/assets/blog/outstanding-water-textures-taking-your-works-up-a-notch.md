---
title: "Outstanding Water Textures Taking Your Renderings up a Notch"
category: "How to"
date: "August 1, 2025"
author: "Hao Wang"
source: "https://www.d5render.com/posts/outstanding-water-textures-taking-your-works-up-a-notch"
---

# Outstanding Water Textures Taking Your Renderings up a Notch

Whether in archviz or landscape design industry, the use of water is always the finishing touch to make your scene more atmospheric. Many will go to post-processing tools like Photoshop to achieve a satisfactory look of water. Yet the effort could be spared with D5 Render, as we have a user-oriented texture editing system with both a water template on whose basis users can create whichever kind of water they want, or out-of-the-box water material assets in D5 built-in Asset Library.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/680b8ad197fdaaf1de092146_5eecdaf48460cde5a704f81193ce5cc73c13919b420ac68675b8339e1c4c2483f728f271dbcdaa6639e8703ac5556d0d7a936c7509af19e73424c95f7b90186b993681156c480384fe91d5ad95a372ff23c2af163e90abad1520c1543fdae858.gif)

**Note that the Water template can only be used on a** ******single-sided model********. It's also necessary to place a plane underneath the water surface when the pond is not very deep, such as a bathtub or a swimming pool.**

## How to set the parameters of water texture properly

- With Base Color, you can change the hue, saturation and brightness of the water texture.
- The ****Normal**** map decides the appearance of ripples or waves. You can change how strong the wave is by adjusting its intensity and how dense it is by adjusting UV. These parameters play a key role in affecting whether the water texture looks realistic or not.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7eee4b2865f19f66c9a8_63468769ba96de530b1ea748_109.png)

- ****Specular**** controls the reflectance of the material surface. When it's set as 1, the material, a gem for example, will have a very strong reflection. When set as 0, there will be no specular reflection but only diffuse. In this case, the water will look very dark. We recommend 0.25 for water texture based on how its specular works in the real world.
- Similar with Specular, ****Refraction**** should also be adjusted to create the effect as close to reality as possible. The preset value 1.33 is ideal for most of the water textures.
- ****Flow Velocity**** controls the rate of the flowing animation of water. It will not work when Normal value is set at 0.
- Depth controls the water texture's ability to absorb incident light. The higher the parameter, the murkier the water will be.

## How to render a swimming pool with clear water

After changing the material template to "Water", you will find that the water texture seems out of tune with the soothing morning vibe we want to create, thus needing further adjustments.

### ****Step1: Adjust the overall look of water waves****

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7ef04b2865f19f66c9c1_634688c6844df55caf191a03_110.png)

After importing a proper Normal map, you will see that the present water texture still looks rough and bright, more like sea. That's because you need to turn down the Normal intensity and Specular a bit. Now the waves become gentler and milder.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7bf61487498945b97c36_63468918ba474e81f6771a8c_111-ezgif.com-optimize.gif)

### ****Step 2: Further improvements on the details of water texture****

As we have mentioned above, ****1.33**** is an ideal value for water ****refraction**** as it tends to give results close to the real world. So there's no need to change the default Refraction setting.Now there's only one step left to create realistic water texture for this scene: reducing the flow rate by lowering ****Flow Velocity****.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7ef24b2865f19f66ca28_63468a102ef5c80f05c5f1e9_113.gif)

Now it's all set.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7eeb4b2865f19f66c98e_63468a0eabf4cb1abbf6f279_114.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7eeb4b2865f19f66c98b_63468a0deabc88e292aa0f8a_115.png)

## How to render a lake with deep water

First thing first, change the material template to "Water".

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7ef04b2865f19f66c9c4_63468afc9440e557c1ac374d_116.gif)

****Step 1****‍

Similar to what you have done before, import a Normal map and adjust its intensity as you need.In this lovely sunset scene, if you want to see a clear reflection of the surroundings on the water surface, try to set ****specular**** to maximum.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7ecc4806affeca1547f5_6346907cdcea8145e251114c_118-ezgif.com-optimize.gif)

****Step 2****‍

Think about the lake or sea at dusk. It's usually hard to see through the water surface what's underneath. So you need to pull the Depth slider to the right. When the Depth value is low, the lake will look shallow and unnatural.

Now you can see the change of atmosphere before and after the adjustment.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7ef24b2865f19f66ca0c_63468afc41b0a6754a7ac653_120.png)

## How to adjust water in aerial view renderings

Here is a quite useful yet effortless trick to create lively water in an aerial view like this one:

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7ef14b2865f19f66c9db_63469157affb596daeceafc5_121.png)

You can just duplicate the model of water and place it underneath the surface. Then attach to it a texture map and adjust the UV. Quick as a flash, the water now looks crystalline and vibrant.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7ef24b2865f19f66ca13_634692bab7bd099c3712d1d7_map.jpeg)

## Showcase

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7ef24b2865f19f66c9fc_6346932a64a47c1fcb95693f_122.png)

‍

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7eee4b2865f19f66c9a5_6346932a759e2a2a907a7591_123.jpeg)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c7eeb4b2865f19f66c988_6346933c078f2f2be0edb5de_124.jpeg)

‍