# Lights

D5 Render provides seven types of light sources: ****Point Light****, ****Spotlight****, ****Strip Light****, ****Rect Light, Disc Light, Stage Light**** and ****Projector.****（The first four are basic light sources.）

> Go to ****"Menu > Preference > Widget"**** to activate Projector, then it can be inserted into scenes from "the Navigation bar > Add Lights".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSTtdXPftMTCR1H9TO3l5%252Fimage.png%3Falt%3Dmedia%26token%3Dd1ab6867-b95b-4c9c-93b2-4f5cd060f63e&width=768&dpr=3&quality=100&sign=5424c742&sv=2)

## Overview of light types

### ****Point Light****

A Point Light emits light in a similar manner to a real-world light bulb, from a point in space, emitting light uniformly in all directions.

### ****Spotlight****

The Spotlight emits light from a point in space, within a specific cone angle.

- By default, spotlights are emitting light uniformly in the cone.
- You can also control the distribution of light using ****IES files****. D5 Render comes with 6 IES files, or you can import custom IES files.

### ****Strip Light****

A strip of rectangular light that can be further adjusted in length and width, using Barn Door parameters to control the directionality of the light.

### ****Rect Light****

A rectangular planar light source of specified width and height dimensions, used to complement or simulate any rectangular area of luminous objects, such as top lighting fixtures, etc.

### Disc Light

A Disc Light simulates the light emitted from a circular plane and is a type of light source used to create a soft, even lighting effect.

---

## Light source parameters

When we select the light source, the corresponding inspector will appear on the right side.

First, let's introduce the parameters that are available for all four light sources:

### Common parameters

#### ****1.Duplicate****

Select a light and click the "Duplicate" button, a copy of the light with the same parameters will appear at the mouse cursor, click to place it into the scene. Hold Shift and drag the red, green or blue axis to copy along the axial direction.

****2.Focus on****

Click the Focus on button and the camera will move in front of the selected light source.

#### ****3.Reset****

The position of the light source in space remains unchanged, and all others are restored to the default parameters, including the rotation angle.

---

The following five parameters are also common to all four light sources:

#### ****1.Intensity****

the luminous intensity of the light source, in cd (candela), the maximum intensity can be 8000000.

Two units support luminous intensity and luminous flux:

- ****Luminous Intensity****: Light strength in a direction from a source, measured in candela (cd).
- ****Luminous flux****: Total light emitted from a source over time, measured in lumens (lm).

#### ****2.Attenuation Radius****

Limit the influence range of the light.

Within this range, the light decays according to the inverse square law, beyond which the light calculation stops. The size of the spherical range can be visualized by the wireframe.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6D1qIPDBWg5BCZmKMBga%252F%25E8%25A1%25B0%25E5%2587%258F%25E5%258D%258A%25E5%25BE%25841.gif%3Falt%3Dmedia%26token%3D25df9660-9aa7-4bb6-8331-55720b08efa3&width=768&dpr=3&quality=100&sign=a49fb278&sv=2)

#### ****3.Visible in Reflection****

Controls whether the light source appears in the material reflection, and the "Blend Amount" control allows you to adjust how much the light source affects the reflection.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FieBVkauVdqzS2MZdcTnf%252Flight.gif%3Falt%3Dmedia%26token%3Deb1deaaf-bc1f-4738-ae2e-5e88c6481d3d&width=768&dpr=3&quality=100&sign=e7bccdb6&sv=2)

#### ****4.Temperature****

Scientifically set the color of the light.

The unit of color temperature is K, Kelvin. Low color temperature such as: 3000K light source appears yellow.

> - Light color temperature is 5500-6500K, is considered to be the "white" light.
> - High color temperature such as: 8000K light source appears blue.

#### ****5.Color****

freely specify the color of the light.

---

### Special parameters

Next, we explain the parameters specific to each light source:

#### 1.Point Light

- ****Light source radius:**** Control the radius of the imaginary point light. The radius of the light affects the softness of the shadow edges, the larger the light source, the softer the shadow edges.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSLUq0u2nVIdoXGGNodVw%252F%25E5%2585%2589%25E6%25BA%2590%25E5%258D%258A%25E5%25BE%2584.gif%3Falt%3Dmedia%26token%3D9286e079-e15d-4110-98da-0618a347ab97&width=768&dpr=3&quality=100&sign=6f7183c9&sv=2)

#### 2.Spotlight

- ****IES:**** Use the 6 IES built into D5, or choose a custom IES file to control the light distribution of the spotlight. A light source placed close to a wall will shine a specific shape on the wall. Click + Customize IES to add a custom IES file.
- ****Cone Angle:**** Controls the cone angle range of the spotlight's light-emitting cone.

> Note that if an IES file is used while adjusting the cone angle parameter, IES lighting outside the cone angle range will be clamped.

- ****Light Source Radius:**** Same as point light source radius. The radius of the light affects the softness of the shadow edges.

#### 3.Strip Light and Rect Light

The reason for putting these two together is that they are both essentially rectangular lights, the only difference is that the initial parameters are set differently.

- ****Strip Light**** is a rectangular light with a large initial aspect ratio (long strip) and a certain Barn Door Length (Means that it will emit light in a specific direction).
- ****Rect Light**** is a planar light source with equal initial length and width, and a Barn Door Length of 0.

The parameters unique to these two light sources are the "Barn Door" parameters.

- ****Barn Door Angle:**** The angle between the imaginary "Barn Door" plate and the direction of the light's normal, the value range is 0 ° - 90 °.

> - Smaller values focus the light;
> - at 90°, the Barn Door is wide open and the wireframe in the viewport provides a visual representation of the "Barn Door".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FHn6l2sCMWE1HZAQGHito%252F%25E9%2581%25AE%25E5%2585%2589%25E6%259D%25BF%25E8%25A7%2592%25E5%25BA%25A6.gif%3Falt%3Dmedia%26token%3D11859e9d-c582-4c33-9b80-03922388755b&width=768&dpr=3&quality=100&sign=e32934bd&sv=2)

- ****Barn Door Length:**** Controls the length of the imaginary "Barn Door", ranging from 0-100.

> Larger values focus the light, and the wireframe in the viewport provides a visual representation of the "Barn Door".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLsRk7krPFDjc9DhR9sCy%252F%25E9%2581%25AE%25E5%2585%2589%25E6%259D%25BF%25E9%25AB%2598%25E5%25BA%25A6.gif%3Falt%3Dmedia%26token%3Deaae115f-e2f2-4abd-8d9e-218c9ac5c5e2&width=768&dpr=3&quality=100&sign=3b15adba&sv=2)

---

## Light source visibility control

- Use the shortcut `L` or the "Light Source" button in the upper right "Display Mode" to toggle light carrier icon. Toggling carrier icons does not affect light rendering.
- To temporarily turn off a light source, turn off the visibility of that light source in the scene resources list on the left (click on the eye icon) :

> ⚠️ > Note: All light sources themselves are not visible to the camera. The lighting of the light source can only be seen when there is a model near the light or when the fog effects are turned on.