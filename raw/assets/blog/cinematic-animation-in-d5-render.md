---
title: "Full guide on how to make cinematic animation in D5 Render"
category: "How to"
date: "August 7, 2025"
author: "Hao Wang"
source: "https://www.d5render.com/posts/cinematic-animation-in-d5-render"
---

# Full guide on how to make cinematic animation in D5 Render

### ******Table of content******‍

What's cinematic animation

How to create the vibe for cinematic animation in [D5 Render](https://www.d5render.com/downloading?utm_source=seo&utm_medium=blog&utm_campaign=d5-animation)

Animation making

[******The cover image courtesy: DIFOCA GROUP ARCH******](https://forum.d5render.com/t/restyling-agriturismo-osteria/12861)

‍

Speaking of today's media form, what's off the top of your head?

Short videos. That's my answer.

Looking around the world, we can see that tech giants are investing and marketing more on short video platforms. That's underlied by the fact that nowadays people prefer short videos which can deliver more interesting info in a shorter time.

So, to attract a larger audience, ****it's time for architectural/interior/landscape designers to follow up with the trend****. Fortunately, D5 Render has made animation creation easy and pleasant. In this article, you will learn how to make cinematic animation with D5 Render with detail, including the preparations, the creation of the vibe, and the final render.

[Embedded video](https://www.youtube.com/embed/aqSGcxh7MxM)

[Embedded video](https://cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FaqSGcxh7MxM%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DaqSGcxh7MxM&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FaqSGcxh7MxM%2Fhqdefault.jpg&key=96f1f04c5f4143bcb0f2e68c87d65feb&type=text%2Fhtml&schema=youtube)

**Thanks to Aung Kyaw who made this tutorial.**

## What should we know about cinematic animation

- ******The contrast between architecture animation and cinematic animation******

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/684809ce41013742c814e521_638349b9e52e4430c9a7dbc2_contrast.png)

In a word, imagine you are the one who is in the scene. Focus on how you feel, instead of what the room looks like. Then create the atmosphere around your feelings.

- ******The preparations needed******

In this tutorial, Aung wanted to tell the story of a person ****who enjoys reading books on a rainy day****. After setting the theme, he began to look for references and inspirations to have a general idea of how the scene should look. The colors, the plants, the decorations... All were put on a mood board. Now the scene became vivid in his mind.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/684809d041013742c814e5a0_638349be41973c3e99714131_mood%2520board.png)

Just as we've said before, the vibe comes first for cinematic animations. You should bear this in mind when modeling the layout of the room.

## How to create the vibe in D5 Render

### 1. Set the environment

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/684809ce41013742c814e54e_638349bee52e447ba2a7dbcf_HDRI.png)

Here Aung used HDRI "Partly Cloudy" with a cold tone, as well as Fog with a tint of blue, making the room look hazy and dark on a rainy day.

‍

### 2. Adjust Highlight and Contrast

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/684809ce41013742c814e53c_638349bdf12be13e978fb126_effect.png)

This means color correction and grading at the same time in the post-processing panel. Aung also turned on Bloom to make the outside shine a bit more. The built-in LUT "Desert" helped a lot as well.

‍

‍

‍

‍

‍

### 3. Adding accent lighting

Move on to light editing. Aung hoped the room would look cozy for a reading man. So he put a warm yellow Point light in the bedside lamp. Reduce the lighting intensity a bit, and scale down its radius. Now it can light up the area beside the bed.

Duplicate the light and put it into other lamps, such as the one next to the chair.

Check whether the room is just bright for reading. If not, put an area light (rectangular light) on the roof and illuminate the whole space. Low intensity fitting the vibe, don't forget it.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/684809ce41013742c814e51e_638349beb1250220331b713a_%25E6%2588%25AA%25E5%25B1%258F2022-11-27%252016.25.09.png)

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/684809ce41013742c814e524_638349be0b97f6cef3d1f8f8_artificial%2520light.png)

### 4. Create outdoor mood

After finishing the inner space, it's time for the exterior.

It was very convenient for Aung to create the raining effect in D5 Render. Just one click in the weather system > Precipitation, and it would start to rain.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/684809ce41013742c814e542_638349be210b9580628e9813_foliage.png)

To make the plants on the balcony become more realistic, he changed their material template to Foliage, which gave them a bright, shiny look in the rain.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/684809ce41013742c814e53f_638349bedac77c16217845fd_grass.png)

Then he changed the ground material template to Grass. Adjust the UV, height and density of Grass material to make it more natural.

Done! A lively balcony was born.

## Animation making in D5 Render

Aung was all set to create a touching story through animation.

First, Aung defined the start and end points of the camera movement and added two shots to the timeline for them.

Then he set different Depth of Field for the camera shots to achieve a smooth shift of focus. To learn more about how to use DOF for cinematic animation, you can read [this article](https://www.d5render.com/post/how-to-create-animation-in-d5-render-with-depth-of-field).

To create the effect of lights being turned on, he selected the timeline points when he wanted them to light up and added a keyframe for switching on the light.

![](https://cdn.prod.website-files.com/62ce5d829e01c60b7c148396/684809ce41013742c814e530_638349bedac77cb6f87845fe_light-on.png)

Then he made more clips. Add them to render queue for batch rendering and edit them in a video clipping tool.

Here's the final work he got:

[Embedded video](https://www.youtube.com/embed/bFvF9X10W6Y)

[Embedded video](https://cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FbFvF9X10W6Y%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DbFvF9X10W6Y&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FbFvF9X10W6Y%2Fhqdefault.jpg&key=96f1f04c5f4143bcb0f2e68c87d65feb&type=text%2Fhtml&schema=youtube)

For more tips of using keyframes in animation making, please read this article: [******How to use keyframes to create animations in D5 Render******](https://www.d5render.com/post/how-to-use-keyframes-to-create-animations-in-d5-render).