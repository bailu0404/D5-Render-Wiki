# How to use Stage Light Widget?

How to use Stage Light

****'Stage Light'**** is designed to simulate professional dynamic lighting effects.

- Go to ****Menu > Preference > Widget**** , and you can check what you have installed, click to toggle on/off and manage your widgets.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F419uLP4b3CsziRpXHVFY%252Fimage.png%3Falt%3Dmedia%26token%3Db058f626-00d1-4ce4-88a9-1670f978c99c&width=768&dpr=3&quality=100&sign=6cc78a3e&sv=2)

Stage Light

- Gobo: Choose preset Gobo or upload customized Gobo.
- Intensity: The luminous intensity of the light source, the unit is lm, the maximum brightness can be input 8000000.
- Iris: Control the radius of the light-emitting cone of the stage light, the larger the aperture, the larger the light-emitting radius.
- Rotate: Used to control the rotation of the Gobo when the Prism parameter is not turned on. Negative values of the parameter suggest that the Gobo will rotate clockwise. The smaller the value, the faster it rotates. When the rotation parameter is positive, the Gobo rotates counterclockwise. The larger the value, the faster it rotates. 0 means that the stage light stays static.
- Attenuation Radius: Limit the range of influence of the light source. Within this range, the light attenuates according to the normal inverse square law, beyond which the light calculation stops.
- Haze: Control the effect of smoke in the simulated stage light, adjust the smoke concentration by adjusting the value.
- Prism: One key switch, split the light into multiple beams.
- Number: Control the number of split lights.
- Color: Control the lights' color.

### FAQs

#### 1.Why is it invalid to adjust the Haze parameter for Stage Light? /How to realize the beam light effect?

Turn on Fog and Tindal in the Environment panel, then can get the beam light effect, and the change of Haze parameter is also visible in real time.

> ⚠️ > In order to make other fill light sources not affected by the Tindal effect, the Fog parameter in the Environment panel does not need to be too high, just increase the Haze parameter of the Stage Light.

#### 2. Why the Stage Light effects become abnormal?

The maximum number of the Stage Light/Projector is 64, if it exceeds the change limit it may cause abnormal preview or output effect.

By default, the maximum number of volumetric lights is 32. This can be adjusted up to a maximum of 256 in:

****Preference > Rendering > Detailed Stage Light Beam Quantity Limit.****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FZElMpfPUxDUhcearUesl%252Fimage.png%3Falt%3Dmedia%26token%3D42c2d84d-6f52-49d3-ae7c-977870015c82&width=768&dpr=3&quality=100&sign=fe874653&sv=2)

If the duplicated stage lights randomly display abnormal effects (such as faded colours), this may be related to the light beam detail restrictions. Try increasing the ‘Max Detailed Beams’ value for 'Detailed Stage Light Beam Quantity Limit'.

> ****Note:****
>
> - This setting follows the current project.
> - The higher this value, the richer the number of lights and details rendered on screen. However, this also leads to increased graphics memory and performance consumption. It's recommended to set it reasonably, based on your project's requirements and hardware performance, to balance visual effect and rendering efficiency.

#### 3. Why the specular reflection Stage Light/Projector effect is not shown in the rendering result?

This effect is not supported in the current version and will be supported in subsequent versions.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2Fsaas.bk-cdn.com%2Ft%2F18217684-957c-4109-9021-5866cc58cc60%2Fu%2F10a66288-31af-4b72-adee-8249db06c5f0%2F1707188011317%2F%25E6%259C%25AA%25E6%25A0%2587%25E9%25A2%2598-2.png&width=768&dpr=3&quality=100&sign=687dd63f&sv=2)

Preview and output effect of the current version of Mirror Reflection Stage Light/Projector