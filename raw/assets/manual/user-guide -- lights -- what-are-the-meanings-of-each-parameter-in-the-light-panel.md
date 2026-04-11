# What are the meanings of each parameter in the light panel?

When we select a light, the corresponding light parameter panel will appear on the right sidebar.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLHncmtW9O6X2DlZJiX8U%252FDingtalk_20240125155839.jpg%3Falt%3Dmedia%26token%3Db2782a72-ca15-4e29-8c31-c15f772c4831&width=768&dpr=3&quality=100&sign=277d8d92&sv=2)

### Duplicate

Select a light and click the ''Duplicate'' button will make a copy of the light with the same parameters as the selected one at the mouse position, and can be placed in the scene by clicking. Drag the red-green-blue axes with Shift held down to duplicate along the axes.

### Focus on

Click the ''Focus on'' button, and the camera will move in front of the selection.

### Reset

The position of the light in space remains unchanged, while all other parameters will reset to the default parameters of the light, including the rotation angle.

---

### Light Type Switch

Supports directly switching a light type into another one, retaining the parameters and keyframe information, without having to select or adjust the position and parameters again. Undo supported.

> **Note: The light name remains the same even after the light type is switched.**

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FNwK7DA0uWviODQVvCtm7%252Fimage.png%3Falt%3Dmedia%26token%3D432db7bc-20f4-4c4f-a200-24ada6f2a461&width=768&dpr=3&quality=100&sign=4fcbaf17&sv=2)

### Intensity

The luminous intensity of the light, the larger the value, the stronger the brightness. For Rect Light and Strip Light, the brightness of the light is related to the size of their area with the unit of cd/㎡, which Indicates the intensity of light per unit area in a particular direction.

Two units support luminous intensity and luminous flux:

- Luminous Intensity: Light strength in a direction from a source, measured in candela (cd).
- Luminous flux: Total light emitted from a source over time, measured in lumens (lm).

### Attenuation Radius

Limits the impact range of the light. Within this range, the light decays according to normal inverse square law, outside of which the light calculation will stop. The size of the spherical calculation range can be visualized in the wireframe illustration.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F2IuMyjqtwkW9xOlmVYa2%252F%25E8%25A1%25B0%25E5%2587%258F%25E5%258D%258A%25E5%25BE%25841.gif%3Falt%3Dmedia%26token%3D01340523-8bbc-4c14-9f3b-e663c678e118&width=768&dpr=3&quality=100&sign=610be86a&sv=2)

### Attenuation Intensity

Used to control the light attenuation distance and adjust the illumination range of rectangular lights. The smaller the parameter, the less the brightness is attenuated. It is mainly used to control the attenuation effect at the end of the light. A larger value will result in a closer approximation to rectangular attenuation.

> Note: Attenuation intensity is only supported by Strip Light and Rect Light.

### Show Light Shape

When this option is enabled, you can not only observe the lighting effect, but also view the concrete shape and size of the light within the scene.

### Visible in Reflection

It's used to control if the light appears in the reflection of the material. The "Intensity" parameter can be used to adjust the influence of the light on reflections.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fpv2Iz8RDneZ0fE1DQ6LA%252Flight.gif%3Falt%3Dmedia%26token%3Dd2e01695-546d-4b34-a248-d54500de7608&width=768&dpr=3&quality=100&sign=1d34999f&sv=2)

### Temperature

To scientifically specify the color of light, the unit of color temperature is K, Kelvin. A light with a low color temperature, e.g. 3000K, is yellowish, a light with a color temperature of 5500-6500K is considered to be close to "white", and a light with a high color temperature, e.g. 8000K, is bluish.

### Color

Specify the color of light freely.

### Caustics

When this option is switched on, the light can perform a caustic projection.

---

## Point Light

### Light Source Radius

To control the radius size of the imaginary point light source, the radius size of the light source will affect the degree of vignetting of the shadow edges of the illuminated objects, the larger the radius of the light source, the softer the shadow edges will be.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSLUq0u2nVIdoXGGNodVw%252F%25E5%2585%2589%25E6%25BA%2590%25E5%258D%258A%25E5%25BE%2584.gif%3Falt%3Dmedia%26token%3D9286e079-e15d-4110-98da-0618a347ab97&width=768&dpr=3&quality=100&sign=6f7183c9&sv=2)

---

## Spotlight

### IES

Use the D5's six built-in ****IES****, or choose a custom IES file to control the light distribution of the spotlight. The light source placed close to a wall will illuminate a specific shape on the wall. Click here to add a custom IES file:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FlfEkupke0uBDRp7vPmgj%252Fimage.png%3Falt%3Dmedia%26token%3Dbdd83815-b080-43b3-b9ba-be352a8906f1&width=768&dpr=3&quality=100&sign=232bdf4a&sv=2)

### Cone Angle

To control the cone angle of the spotlight cone, note that if an IES file is used and the cone angle parameter is also adjusted, IES illumination outside the cone angle range will be truncated.

### Light Source Radius

The principle is the same as the radius of a point light source. The radius size of the light source affects how much the shadow edges of the illuminated object are defocused.

---

## Strip Light and Rect Light

Both are essentially rectangular light sources, the only distinction is that the initial parameters are set differently. Strip Light is a rectangular light with a large initial aspect ratio ( long strip ) and a certain barn door length ( meaning that the light emitted has a certain directionality ). Rect Light is a rectangular light with an equal initial aspect ratio and zero barn door length. The peculiar parameter of these two light sources is the "barn door" parameter.

### Barn Door Angle

The angle between the surface of the hypothetical "barn door" and the light's normal direction, the value range is 0 ° - 90 °, the smaller the angle, the more concentrated the light; in the value of 90 °, the barn door will be completely open, the wireframe in the viewport can be visualised to represent the shape of the "barn door" and its effect on the light source.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FHn6l2sCMWE1HZAQGHito%252F%25E9%2581%25AE%25E5%2585%2589%25E6%259D%25BF%25E8%25A7%2592%25E5%25BA%25A6.gif%3Falt%3Dmedia%26token%3D11859e9d-c582-4c33-9b80-03922388755b&width=768&dpr=3&quality=100&sign=e32934bd&sv=2)

### Barn Door Length

To control the length of the imaginary "barn door", the value ranges from 0 to 100, the higher the value, the more concentrated the light will be, the wireframe in the viewport can be visualised to represent the shape of the "barn door" and its effect on the light source.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLsRk7krPFDjc9DhR9sCy%252F%25E9%2581%25AE%25E5%2585%2589%25E6%259D%25BF%25E9%25AB%2598%25E5%25BA%25A6.gif%3Falt%3Dmedia%26token%3Deaae115f-e2f2-4abd-8d9e-218c9ac5c5e2&width=768&dpr=3&quality=100&sign=3b15adba&sv=2)

---

## Disc Light

Strip Light, Rect Light and Disc Light provide Directionality parameter.

### Directionality

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FuN90rJaLgHopm1hx6bPT%252Fimage.png%3Falt%3Dmedia%26token%3D94411477-dee3-4703-9204-234d4e1fc379&width=768&dpr=3&quality=100&sign=71bb8c11&sv=2)

Directionality can be adjusted by checking the ****Apply Directionality**** parameter in the Light Property. A smaller value creates a more diffuse light edge, resulting in a soft, broad lighting effect, while a larger value concentrates the light edge, forming a more obvious light boundary.

---

## Visible in Reflection

Use the shortcut key L or the "Light Source" button in the "Display" in the upper right corner of the viewport to switch the light source icons to show/hide, so that we can easily see the spatial location of the light source, source switching does not affect the lighting effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FiKIrlIpBeClOnEUw160z%252F%25E5%2585%2589%25E6%25BA%2590%25E9%259A%2590%25E8%2597%258F%25E6%2598%25BE%25E7%25A4%25BA.gif%3Falt%3Dmedia%26token%3D43962518-e628-4d56-9de8-2a8bb3838202&width=768&dpr=3&quality=100&sign=14f84d2a&sv=2)

If you want to turn off a light source temporarily, turn off the visibility of that light source in the scene resource list on the left (click on the eye icon).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FPAVhRB2j1cuVDCt6ePlx%252F%25E5%2585%2589%25E6%25BA%2590%25E9%259A%2590%25E8%2597%258F%25EF%25BC%2588%25E5%259C%25BA%25E6%2599%25AF%25E5%2588%2597%25E8%25A1%25A8.gif%3Falt%3Dmedia%26token%3Dda737164-3a25-485c-9f06-bb9f61dd0469&width=768&dpr=3&quality=100&sign=f83ca0f7&sv=2)