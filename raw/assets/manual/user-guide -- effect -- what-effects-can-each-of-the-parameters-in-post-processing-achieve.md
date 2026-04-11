# What effects can each of the parameters in post-processing achieve?

### Exposure

This function simulates the exposure function of a real camera and is used to adjust the overall brightness of the image.

#### Manual Exposure

Turn off the "Auto Exposure" switch, that is, enter the "Manual Exposure" mode, the mouse drags the exposure control can control the overall brightness of the screen changes, and you can also enter specific values.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fo3Ddqt96Mno4PBjtfPrg%252F%25E6%259B%259D%25E5%2585%2589.gif%3Falt%3Dmedia%26token%3D86f17076-f8ad-42f1-8a45-a89ae1b1efe2&width=768&dpr=3&quality=100&sign=fb04195d&sv=2)

The higher the exposure value, the brighter the image, and the lower the exposure value, the darker the image. When adjusting the exposure manually, pay attention to the amount of information in the scene and try to avoid large areas of "overexposure" or "dead black" in the image.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FRSbYW4HVnbarA6ISxqb3%252Fimage.png%3Falt%3Dmedia%26token%3D83450b4a-7bbd-4aff-9854-65326bdab92c&width=768&dpr=3&quality=100&sign=7e2e0847&sv=2)

#### Auto Exposure

Auto Exposure in D5 Render automatically analyzes image brightness and adjusts it to a balanced level. This mimics the human eye's natural adaptation to changes in lighting (e.g., moving from a bright to a dark environment, or vice versa) or the functionality of a “dumb camera", which can quickly find a suitable exposure level for the individual using it to base on.

- ****Exposure Compensation:**** allows users to manually fine-tune the overall brightness while Auto Exposure is active. This enables users to brighten or darken the picture as needed, making it easier to achieve the desired visual result with automatic exposure engaged.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFEPBlYn0p0fRn6s857Wu%252Fimage.png%3Falt%3Dmedia%26token%3Ddc3ec2fc-9196-46fe-a602-70cf7d1172b8&width=768&dpr=3&quality=100&sign=c8facc85&sv=2)

### Highlight Local Exposure

Suppress the highlights in the scene to reduce the loss of detail caused by overly bright areas.

### Shadow Local Exposure

Brighten dark areas to reveal sharper details.

### Contrast

Adjust the difference in brightness between the light and dark areas of the image.

Lowering the contrast will brighten the dark areas and darken the bright areas. As the contrast is lowered, the light and dark colour values of the pixels gradually converge to medium grey, creating a greyish, faded effect, and in the extreme case, the picture becomes completely medium grey. Increasing the contrast will enhance the brightness contrast between the light and dark areas, the sketch relationship of the picture will be enhanced, and the sense of three-dimensionality will be increased, too high a contrast value will bring about overexposure of the highlight areas and dead black in the dark areas:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FGGA1Xf9xLi2n2q06gpzz%252F%25E5%25AF%25B9%25E6%25AF%2594%25E5%25BA%25A6.gif%3Falt%3Dmedia%26token%3D53da2857-3ed2-4463-b7ff-09e4660096ba&width=768&dpr=3&quality=100&sign=f3581d05&sv=2)

### Tone Mapping Curve

The Highlight, Shadow, and Contrast parameters together control the "Tone mapping curve", which determines how the high dynamic range information computed by the renderer is mapped to the low dynamic range screen, and the basic shape of the curve is as follows:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FrXc5Gu3fr1EKhL2yxIPd%252Fimage.png%3Falt%3Dmedia%26token%3D1d3e9888-56ec-44b9-9b36-6ba5ce891e89&width=768&dpr=3&quality=100&sign=f5907c02&sv=2)

The horizontal axis represents the information calculated by the renderer and the vertical axis represents the information mapped onto the screen.

The upper right-hand side of the curve flattens out and converges to a value slightly greater than 1, meaning that "the pixels converge to pure white as the brightness rises". Since the highlights are slowly converging to pure white, it is possible to see some more detail in the highlights on the screen with the help of this curve. The shape of the curve in the lower left corner means that the dark areas are slowly converging to dead black, and the gradual flattening of the curve mapping helps us retain more detail in the dark areas.

The area in the upper right corner of the tone mapping curve is called "shoulder" and the area in the lower left corner is called "toe".

The effects of the three control parameters are explained in detail below.

#### Highlight

The "shoulder" pattern at the top right of the control curve affects the highlight areas of the image:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FWGImNkbDBcPjAMTQCH5H%252F16%2520%25E9%25AB%2598%25E5%2585%2589%25E5%258F%2582%25E6%2595%25B0%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3Db3866906-2c19-4b3c-b953-8e1fba0b3e44&width=768&dpr=3&quality=100&sign=13cc73a8&sv=2)

The highlight parameter is useful in two main ways:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FkiIUH5jLZmF2jthkxRqB%252F%25E9%25AB%2598%25E5%2585%2589%25E8%25B0%2583%25E6%2595%25B4.gif%3Falt%3Dmedia%26token%3Dc2d4044b-d213-4d98-916d-4453439860de&width=768&dpr=3&quality=100&sign=8b4ac1ac&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F2wVSC2f0jLv85ISzkDuB%252F%25E9%25AB%2598%25E5%2585%2589%25E8%25B0%2583%25E6%2595%25B40-1.gif%3Falt%3Dmedia%26token%3Df6bfa14e-7c6d-4d9b-aac8-54621186ff7b&width=768&dpr=3&quality=100&sign=a6ec874c&sv=2)

#### Shadow

The "toe" pattern in the lower left of the control curve will affect the darker parts of the image:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FkPYdbm10an8qby1XVh5e%252F19%2520%25E9%2598%25B4%25E5%25BD%25B1%25E5%258F%2582%25E6%2595%25B0%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3Dc3c2fc85-cd80-49ca-b1bc-6ac9bbc1bbf9&width=768&dpr=3&quality=100&sign=83bb3426&sv=2)

In practice, lowering the value will result in more detail in the dark areas, while the overall contrast in the dark areas is reduced and greyish. Raising the value, more dark details will be pressed into "dead black", which correspondingly improves the contrast of the dark content:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FuFsWKBYhmjaVFFf6Javd%252F%25E9%2598%25B4%25E5%25BD%25B1%25E8%25B0%2583%25E6%2595%25B40-1.gif%3Falt%3Dmedia%26token%3D0829fd88-115d-4e79-ac8d-ace20b11d9c1&width=768&dpr=3&quality=100&sign=23797da8&sv=2)

### White Balance

The white balance parameter serves two functions.

This is actually a control related to the colour temperature, the default value is 6500 in Kelvin (K).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FiwLTn5aLW1P5AR9lsUeQ%252F%25E7%2599%25BD%25E5%25B9%25B3%25E8%25A1%25A1.gif%3Falt%3Dmedia%26token%3D36e5c368-74ef-479c-8ebd-6b9c31dc1b82&width=768&dpr=3&quality=100&sign=6ed5f70&sv=2)

### Tint

In conjunction with the colour temperature parameter, the white balance tint of the scene is adjusted by adjusting the cyan and magenta ranges.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FR0eYjrfue6NiIyXrofKZ%252Fimage.png%3Falt%3Dmedia%26token%3D9a0659db-e5fd-4002-864a-7dc11216d214&width=768&dpr=3&quality=100&sign=46a351dc&sv=2)

Post Tint +0.5 | Normal | Post Tint -0.5

### Bloom

Make the scene appear to have a glowing effect. The image will be blurred and vignetted, especially for bright objects on darker backgrounds, and a more pronounced flooding phenomenon can be seen, the higher the value of the control, the more obvious the bloom effect will be:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F3OEw1XT9mILKv47kvpTB%252F%25E6%25B3%259B%25E5%2585%2589.gif%3Falt%3Dmedia%26token%3D4a78d1c3-7488-4706-b50d-42d5ca31ff58&width=768&dpr=3&quality=100&sign=14728564&sv=2)

### Rainbow Flare

Simulates the colorful glow around the sun when shot by a camera.

Note: This effect ****is only supported for Geo and Sky**** and is disabled in HDRI.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FOR3UfTlOsrjelH4vlUZW%252F3209f99aafa73a111e23acd68e517859f6151283.gif%3Falt%3Dmedia%26token%3D93e957b6-a48b-47b7-a2b8-2f31c0deee13&width=768&dpr=3&quality=100&sign=a722061b&sv=2)

Rainbow Flare

### Lens flare

Simulates the halo effect (also translated as "lens flare") produced by a real camera lens when backlighting a bright light source, in which a series of halo effects are distributed along an axis through the centre of the frame, with the larger the value of the controls, the more pronounced the effect:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FamWp206D5CoEC0pXgex5%252F%25E9%2595%259C%25E5%25A4%25B4%25E5%2585%2589%25E6%2599%2595.gif%3Falt%3Dmedia%26token%3Dcb94e803-6013-4fcc-bda2-e82a8b4c8144&width=768&dpr=3&quality=100&sign=a67996e4&sv=2)

### Vignette

Simulates a real-world gradient effect of gently decreasing brightness at the corners of a camera lens.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FmRS4GrhFNbNnAMdf4ZkR%252Fimage.png%3Falt%3Dmedia%26token%3D2af4e201-7e1b-499f-953b-c8aee86dd009&width=768&dpr=3&quality=100&sign=eafd286a&sv=2)

Post Vignette 0.5 | Normal | Post Vignette 1.0

### Chromatic Aberration

Simulates the Chromatic Aberration phenomenon of colour shifts in real-world camera lenses.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FlilvX1EXAmp98EVesngp%252Fimage.png%3Falt%3Dmedia%26token%3D8a2f613c-aad8-4ea9-979c-59569a9e15bb&width=768&dpr=3&quality=100&sign=1a125df6&sv=2)

Post Chromatic Aberration 2.5 | Normal | Post Chromatic Aberration 5.0

### Saturation

To control the vividness and purity of the colours in the picture.

The higher the saturation, the closer the colours are to pure colours, i.e. the difference between the values of the three RGB colour components becomes larger; the lower the saturation, the closer the colours are to grey, i.e. the values of the three RGB colour components tend to be equal. The saturation value is pulled to the lowest, the pixel RGB value is completely equal to the loss of colour tendency, only dark and light changes, the picture becomes a "black and white picture":

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fm80i8cl6nKPvHx89kyAK%252F%25E9%25A5%25B1%25E5%2592%258C%25E5%25BA%25A6.gif%3Falt%3Dmedia%26token%3D537da3e0-81fd-40c7-95b9-46e7efdd0d41&width=768&dpr=3&quality=100&sign=830ae5ed&sv=2)