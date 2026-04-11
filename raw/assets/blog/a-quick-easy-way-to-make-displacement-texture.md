---
title: "Quick Displacement Textures in D5 Render: Easy 3D Detail Boost"
category: "How to"
date: "August 1, 2025"
author: "Hao Wang"
source: "https://www.d5render.com/posts/a-quick-easy-way-to-make-displacement-texture"
---

# Quick Displacement Textures in D5 Render: Easy 3D Detail Boost

![Architectural render with displacement maps](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c88ac1487498945c103ab_6387326d6f201c4f3fc02244_oscarhharo_arquitecto.jpeg)

Displacement, one of the built-in material templates in D5 Render, can help simulate the 3d bump effects. When you need to create embossed stones, brick walls or other rugged materials, this template will play a big role. Today, we will show you how to create your own displacement textures.

Take this emoji for example.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c88aa1487498945c10370_6387326a46c35f8d35538a21_1.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c88ac1487498945c10405_6387336961c68e8c0ba89bf1_2.gif)

First, open the image on which you want bumps in Photoshop. Choose Filter > 3D > ****Generate Bump (Height) Map****.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c88aa1487498945c10376_6387326b1a49fb1713f2fbb4_3.png)

Adjust the parameters in the pop-up window according to your need, and you can see the change in the left window.

Before getting down to making the map, you need to understand the logic here: the whiter the area, the more it bulges.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c88aa1487498945c10379_6387326bcd1c0557f13091d1_4.png)

Then go to Filter > 3D > ****Generate Normal Map**** (generally speaking, the default parameters do not need to be modified) to create a normal map for it.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c88aa1487498945c10373_6387326cac142f8516883c3e_5.png)

Now we have three texture maps:Normal map which controls how bumps and dents reflect light;Displacement map which simulates model bumps and dents;Base color map. Export them as .png files.

In D5 Render, select a material and then change it into the Displacement template.Put the three texture maps into the corresponding slots.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c87c94fec60bb2b13e09f_Group%2028.png)

We can see that the displacement effect looks realistic with appropriate light reflection.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c88ac1487498945c10405_6387336961c68e8c0ba89bf1_2.gif)

Now you know how the Displacement material works and how to make one. Let's see some nice works containing displacement textures：

![facade render with displacement maps](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c88ac1487498945c103a5_6387326bb348d1450f3d1ed5_1280X1280.png)

![Interior render with displacement maps](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/688c88ac1487498945c103b4_6387383e3ef92b40345b6422_jimmy%25203d.jpeg)

‍