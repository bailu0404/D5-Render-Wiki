# Effect

## LUT‌

Use the LUT (Look-Up-Table) to do color correction.

The LUT is disabled by default, turning on the switch will enable D5 default LUTs:

There are five D5 default LUTs, which can be switched in the drop-down menu, corresponding to different color representations:

****Intensity:**** This parameter controls how much the LUT affects the original image. The default value is 1, and the LUT is at its strongest. Pull the control to the left to weaken the LUT color correction strength. The intensity value of 0 means that the original image is displayed.

Click "+Customize LUT" in the drop-down menu to import a 3D LUT file in .cube format.

Custom imported LUT files are saved to the "customlut" folder under D5 Render installation path, which can be quickly accessed by clicking on the folder icon to manage custom LUT files:

In the drop-down menu you can switch between "default" and "Custom" categories:

## Post-processing

### Exposure

This simulates the exposure function of a real camera and is used to adjust the overall brightness of the image.

#### Manual Exposure

Turn off the "Auto" switch to switch to "manual exposure" mode.You can drag the exposure controls to control the overall light and darkness of the picture, or you can enter a specific value.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkexhKb5NKycim3IAbm%252F-MkextMyoMjz0440dJm3%252F08%2520%25E6%2589%258B%25E5%258A%25A8%25E6%259B%259D%25E5%2585%2589%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3Da46d5c4a-e409-4c34-b100-fbdaba489658&width=768&dpr=3&quality=100&sign=118cddde&sv=2)

The higher the exposure value, the brighter the picture, the lower the exposure value, the darker the picture.Manually adjust the exposure value, you need to pay attention to the amount of information in the picture when adjusting, and try to avoid large areas of "overexposure" or "pure black" in the picture.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkexhKb5NKycim3IAbm%252F-Mkey-Icn6afUD4aWub7%252F%25E6%259B%259D%25E5%2585%2589.png%3Falt%3Dmedia%26token%3D8fa4d0ae-b01c-4735-a279-e74eba34d3c2&width=768&dpr=3&quality=100&sign=dcc21d32&sv=2)

Left: Under Exposure | Middle: Moderate Exposure | Right: Over Exposure

#### Automatic Exposure

Turn on the "Auto" switch, the renderer will automatically analyze the brightness of the screen and adjust to a proper value, similar to the effect of automatic adaptation of the human eye from a bright environment into a dark environment (or from a dark environment to a bright environment), or similar to the automatic exposure of a "Point and shoot camera", which can quickly find a suitable exposure base value for you.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkeyPn9AfJSveDhfVga%252F-MkeyVDGfdtxEYhl7Sgn%252F12%2520%25E8%2587%25AA%25E5%258A%25A8%25E6%259B%259D%25E5%2585%2589%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3Dbfc99bf7-d463-42eb-bca9-76ff7b147e43&width=768&dpr=3&quality=100&sign=aba668ea&sv=2)

### Contrast

Adjusts the brightness difference between the bright and dark areas of the image.

Decreasing the contrast will brighten the dark areas and darken the light areas. As the contrast decreases, the light and dark pixels gradually tend to medium gray, creating a grayish, faded effect, and in the extreme case, the picture becomes completely medium gray. Increasing the contrast will enhance the contrast between the brightness of the light and dark areas, the three-dimensional sense of the image will increase. Too much contrast will make the highlight area overexposed and dark areas pure black.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkeyPn9AfJSveDhfVga%252F-Mkeya3Lejk-S_JxWFV7%252F13%2520%25E5%25AF%25B9%25E6%25AF%2594%25E5%25BA%25A6%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3D36c906db-23ac-4b30-8626-16c8208d45f4&width=768&dpr=3&quality=100&sign=81581c9c&sv=2)

### Tone mapping curve

The ****Highlight****, ****Shadow****, and ****Slope**** parameters together control the "Tone mapping curve", which determines how the high dynamic range information calculated by the renderer is mapped to the low dynamic range screen. The basic shape of the curve is as follows:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkeyPn9AfJSveDhfVga%252F-MkeyfcGDMPCw5MiHSug%252F15%2520Tone%2520mapping%2520%25E6%259B%25B2%25E7%25BA%25BF.png%3Falt%3Dmedia%26token%3Dfb1ea97f-e6c1-44fb-9f9f-5f2b19c89490&width=768&dpr=3&quality=100&sign=2347e029&sv=2)

The horizontal axis of the coordinates represents the information calculated by the renderer, and the vertical axis represents the information mapped to the screen.

As you can see, the upper right side of the curve flattens out and converges to a value slightly greater than 1, meaning that "as the brightness rises, the pixels gradually converge to pure white". Since the highlight areas are slowly converging to pure white, we can see more detail in the highlight areas on the screen with the help of this curve. The curved shape in the lower left corner means that the dark areas are slowly converging to pure black, and the gradual flattening of the curve mapping helps us to retain more detail in the dark areas.

The area in the upper right corner of the tone mapping curve is called the "shoulder" and the area in the lower left corner is called the "toe".

The impact of the 3 control parameters is explained in detail below.

- ****Highlight:**** Control the "shoulder" shape at the top right of the curve, which affects the highlight area of the image.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkXLsE0RLY0-aQLkJ5Y%252F-MkXNrrUvvGUmG-3JjpX%252F16%2520%25E9%25AB%2598%25E5%2585%2589%25E5%258F%2582%25E6%2595%25B0%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3Dd0cb9f9a-0ffc-445b-b77c-e2e60be40f71&width=768&dpr=3&quality=100&sign=2a09b149&sv=2)

The role of highlight parameters in practice is mainly reflected in two aspects：

- ****Shadows:**** Control the "toe" shape at the bottom left of the curve, which affects the darker parts of the image:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkXNuau0rrnbgVRdRZm%252F-MkXO0l91d1_TYvLUOH9%252F19%2520%25E9%2598%25B4%25E5%25BD%25B1%25E5%258F%2582%25E6%2595%25B0%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3D5204c3fb-d2dc-49c4-bab9-95bab597ca2a&width=768&dpr=3&quality=100&sign=a6dc143&sv=2)

In practice, the effect of the shadows parameter is obvious, lower the value, you will see more dark details, while the overall contrast of the dark areas decreased, turning gray. Pulling up the value will press more dark details into "pure black", correspondingly increasing the contrast of the dark content.

- ****Slope:**** Control the slope of the diagonal part of the curve, which will affect the contrast between the highlights and the dark areas of the picture:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkXO2mtZ9eLvIO32eGg%252F-MkXO8K03bprJzVqy7Gh%252F21%2520%25E5%258F%258D%25E5%25B7%25AE%25E5%258F%2582%25E6%2595%25B0%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3D83e66095-4aa6-4715-bca4-a8c25ae83b63&width=768&dpr=3&quality=100&sign=ed7b9c09&sv=2)

In practice, the effect of Slope parameters is easy to grasp. Pulling down the parameters to the left will make the picture grayish and eventually black, pulling to the right will make the gap bigger between light and dark. Extreme values tend to make the picture appear pure black and overexposed, try to find the right value.

### White Balance

The white balance parameter has two roles:

This is actually a control related to color temperature, with a default value of 6500 in Kelvin (K).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkeyPn9AfJSveDhfVga%252F-MkeyuWXepfcL_-n0uYw%252F24%2520%25E7%2599%25BD%25E5%25B9%25B3%25E8%25A1%25A1%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3Dabb7da45-a953-4e70-8518-227fa0f68759&width=768&dpr=3&quality=100&sign=510e7ae3&sv=2)

It is worth noting the color of the white balance control and the effect of the parameter on the image: White Balance is a post-processing parameter, and the color of the control is the ****opposite**** of the color of the physical color temperature.

The reason is: first of all, we need to know that light with low color temperature is yellowish (e.g. 3000K) and light with high color temperature is blueish (e.g. 8000K), while the white balance parameter in post-processing requires the user to specify the color temperature of the scene light source in order to cancel out its color tendency.

For example, if a scene is illuminated by a warm 3000K main light source, then theoretically you only need to enter 3000K in the post-processing white balance parameter, and the camera will be able to cancel out the warming tendency and shoot white objects as white.

Therefore, the lower the color temperature value in the post white balance control, the more blue tendency will be added to the picture; the higher the color temperature value, the more yellow tendency will be added to the picture.

### ****Tint****

By adjusting the green and magenta range, it can cooperate with the color temperature parameter to adjust the white balance tone of the scene.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FIPqiABQKYwUYkiSCTRzv%252Ftint.jpg%3Falt%3Dmedia%26token%3D0e75e01e-3851-45bf-a1eb-cc44029cf4eb&width=768&dpr=3&quality=100&sign=96e226b4&sv=2)

Tint +0.5 | normal | Tint -0.5

### Bloom

Gives the picture a halo effect. The image will be blurred and haloed, especially with bright objects on darker backgrounds. The higher the value, the more pronounced the Bloom effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkeyPn9AfJSveDhfVga%252F-Mkez-TGKwQpGYl1CA5x%252F25%2520%25E6%25B3%259B%25E5%2585%2589%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3Dc7787b7e-fcf4-4ef6-b8da-946fcaf98a77&width=768&dpr=3&quality=100&sign=75bb8f11&sv=2)

### Lens flare

Simulates the flare produced by a real camera lens when shooting a bright light source. On the screen, a series of flare effects are distributed along an axis through the center of the screen. Larger values will make the effect stronger:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkeyPn9AfJSveDhfVga%252F-Mkez3R_FaAL3uiLEyDp%252F26%2520%25E9%2595%259C%25E5%25A4%25B4%25E5%2585%2589%25E6%2599%2595%25E5%258A%25A8%25E7%2594%25BB3.gif%3Falt%3Dmedia%26token%3D582d6da0-81d1-471f-ad85-32611c0cb0fe&width=768&dpr=3&quality=100&sign=7acbced2&sv=2)

### ****Vignette****

An artistic darkening of a photo's corners compared to its center, which simulates the gradient effect of gently decreasing the brightness of the corners of the camera lens in the real world

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F0Ug7L0q4wjZT66vlwAvd%252FVignette.jpg%3Falt%3Dmedia%26token%3D0acf1495-c4e4-4c4d-8e86-961fe337e9af&width=768&dpr=3&quality=100&sign=e93e5b90&sv=2)

Vignette 0.5 | normal | Vignette1.0

### ****Chromatic Aberration****

Also known as “color fringing”, it simulates the dispersion phenomenon of real-world camera lens color transformation.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FIih4f04Y50H3vWYGgR7U%252FChromatic.jpg%3Falt%3Dmedia%26token%3D2fdc726e-6086-4a4d-a4c8-fc11311db4cb&width=768&dpr=3&quality=100&sign=b6c31ed3&sv=2)

Chromatic Aberration 2.5 | normal | Chromatic Aberration 5.0

### Saturation

Control the vibrancy and purity of the colors in the picture.

The higher the saturation, the purer the color. This means that the values of the three RGB color components become more different from each other. The lower the saturation, the more the color tends to be gray, i.e., the values of the three RGB color components tend to be equal. When the saturation value is pulled down to the lowest value, the pixel's RGB values are completely equal and lose their color tendency, only light and dark changes, and the picture becomes a "black and white picture":

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkeyPn9AfJSveDhfVga%252F-MkezCdHpLImHE4-e1if%252F27%2520%25E9%25A5%25B1%25E5%2592%258C%25E5%25BA%25A6%25E5%258A%25A8%25E7%2594%25BB.gif%3Falt%3Dmedia%26token%3D9f2b6456-948c-4666-9baa-b254b6f17386&width=768&dpr=3&quality=100&sign=4a08b06&sv=2)