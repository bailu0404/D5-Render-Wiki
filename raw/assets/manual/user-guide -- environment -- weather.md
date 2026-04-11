# How to adjust the weather in D5?

The second item in the "Environment" panel on the right sidebar contains three settings for the weather: ****Cloud, Fog , Wind and Precipitation****.

## Volumetric Clouds:

Introduces Volumetric Clouds with cloud presets and advanced settings, enabling authentic volumetric effects and flexible sky appearance creation.

- Added Volumetric Clouds to Environment > Weather.
- Contains multiple built-in cloud presets including Cumulus, Stratocumulus, Stratus, Altocumulus, Cumulonimbus, Cirrus Clouds, and Clear Blue Sky.
- ****Advanced Cloud Settings:**** Contains advanced options to customize the cloud appearance for different weather and lighting conditions.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6xnXfgky6qGIj7bQn3h7%252Fimage.png%3Falt%3Dmedia%26token%3D4ffd847b-34a2-4fa1-8476-d02de489b367&width=768&dpr=3&quality=100&sign=bb5e28b0&sv=2)

### Cloud parameters

****Settings****

Description

Amount

Controls the area and volume of clouds in the sky. The larger the value, the more the clouds.

Amount - Thickness

Controls the thickness of cumulus clouds.

Amount - Density

Controls the light transmission degree of clouds.

Amount - Curl

Controls the curliness of cloud edges.

Amount - Aggregation

Controls the aggregation degree of clouds. Increasing this value will cause clouds to merge into larger formations.

Cloud Coverage

Cloud coverage modes:

• Entire Sky(default): As cloud amount increases, small clouds are randomly generated across the sky, gradually covering the entire sky.

• Skyline: Small clouds first appear near the skyline, gradually spreading towards the center and eventually covering the entire sky.

• Direction: Clouds appear along the specified direction, gradually covering the entire sky as their amount increases.

Middle-level clouds

Controls the amount of altocumulus and altostratus clouds.

Cirrus Clouds

Controls the amount of high-level cirrus clouds.

Random Seed

Randomly creates varied cloud appearance. The same seed creates consistent cloud appearance in the first frame.

****Global settings****

Height

Controls the altitude at which low-level and high-level clouds start to appear.

Speed

Controls the cloud movement speed. Increasing the value will make clouds move faster.

💡 To view the cloud movement, please first enable the Dynamic option from the Display menu.

Direction

Controls the cloud movement direction with a range of 0-360 degree.

💡To view the cloud movement, please set a movement speed above 0 and enable the Dynamic option from the Display menu.

Rotate

Controls the cloud rotation or offset angle.

Offset

Controls the cloud position offset.

Cast Shadow

When this option is enabled, clouds cast shadows and affect the light from the sun.

> ⚠️ > ****Compatibility****

- Volumetric cloud is the new feature introduced in version 3.0; before version 3.0, it took standard cloud parameters.
- When opening scenes created with earlier versions of D5 Render, the cloud effects remain consistent with the original scene.
- Includes a "Legacy" preset for compatibility with historical projects.

## Fog

Control the fog effect in the scene to add realism and depth to the scene.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fmu45V0SPaHwjEYLTo1C1%252Fimage.png%3Falt%3Dmedia%26token%3Dbf837ecf-6429-4460-b3a2-946be995dc93&width=768&dpr=3&quality=100&sign=74fbcdef&sv=2)

### ****Color****

Click the color slot to open the color picker and change the color of the fog. When the color is warm, it will produce a desert-like, smog effect. When the color is cooler, it will produce a water vapor-like effect.

### ****Density****

Controls how dense the fog effect is. The higher the value, the thicker the fog.

### Height

Controls the location of the height at which the fog appears. At higher values of the falloff control, the change in fog height is more noticeable.

### Falloff

Controls the rate at which the fog falls off in the height direction. The higher the value, the faster the fall off, while the lower the value, the softer the transition of the fog in the vertical direction.

### Start Distance

Controls the starting position of the fog relative to the distance from the camera. The larger the value of the control, the further away the fog appears from the camera position.

### ****Volume Light****

Light is scattered by particles in the air, making light paths visible. This effect is also often referred to as "God Ray".

### ****Scattering****

Controls the distribution of the volume light scattering effect. The default value of 0 makes the fog uniformly bright, and adjusting it to 1 makes the fog from the direction of the light source brighter.

> ⚠️ > Turning on Volume Light option will increase GPU memory consumption.

****Compatibility Notice:****

When opening files saved in version 3.0 using previous versions of D5, fog effects may alter. Please manually adjust fog parameters accordingly.

## Wind

### ****Strength****

Control the wind movement effect of the plant. The higher the value, the more obvious the wind-driven effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkONq_bn6LpZUEmvN8m%252F-MkOOOqecxS0ZC1tlJkR%252F27769ed3-d8da-4cca-98c1-00b05c222ac8.gif%3Falt%3Dmedia%26token%3D8f44d6c9-9691-4a0f-ac38-673d9a18c6c9&width=768&dpr=3&quality=100&sign=c42222a9&sv=2)

Strength: 0.3

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkONq_bn6LpZUEmvN8m%252F-MkOOYMcnMiyGDjwN5A1%252F2f939a9b-1bbc-4a4e-9c60-4977378b4ce2.gif%3Falt%3Dmedia%26token%3D3c684044-e343-4e60-a001-acdd7e14f31d&width=768&dpr=3&quality=100&sign=707d582&sv=2)

Strength: 0.5

### ****Direction****

Freely change the wind direction, the control value range is 0°-360°.

> ℹ️ > Please turn on "Realtime" in the display mode to preview the wind effect.

## ****Precipitation (Rain and Snow)****

Precipitation Contains snow and rain system , with adjustable strength and puddle effects.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F9lKbzvkBffrS8Yi2WTqi%252Fimage.png%3Falt%3Dmedia%26token%3Dcb4ce333-b461-42c0-a68c-f644d88c4736&width=768&dpr=3&quality=100&sign=c664acf8&sv=2)

### ****Rain and snow parameters****

Switch weather effects and transition states through the Rain and Snow slide bar. The precipitation velocity gets higher when the value is closer to both ends.

> Note:
>
> This feature can be displayed in real time only in Dynamic state.

### ****Strength****

We can adjust the Strength parameter to control the size and density of raindrops or snowflakes in the sky, from light drizzle to full-blown downpour, from winter flurry to whiteout blizzard, or even sleet if you want.

### ****Puddle****

Ponding parameter is to control the degree of the ground affected by precipitation. The greater the value, the greater the ponding or snow on the ground. There is no ponding or snow when the value is 0.

> ⚠️ > Note:

Due to the changes in the rain and snow effects in version 2.10, the rain, snow and puddle effects may change when opening old archives (archives from versions before 2.10) in version 2.10 Client, so users need to manually re-adjust them or continue to use previous versions of Client.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FtLmAurpyhimvGzrtTd0Q%252Fimage.png%3Falt%3Dmedia%26token%3D533daae1-e353-4d1f-b5a4-f5b105320fc2&width=768&dpr=3&quality=100&sign=bb2f0fc1&sv=2)

2.10 | 2.9

### Raindrop Transparency

Customize the transparency of the rain line as the effect requires. The smaller the value, the more transparent the rain line will be.

> Note: This parameter is resident and does not affect the effect of rain.

### Snow Flake Size

Customize the size of the snowflake as the effect requires, the larger the value, the larger the snowflake size.

> Note: This parameter is resident and does not affect the effect of rain.

### Water Mist & Density

Simulates water mist in humid air to enhance the realism of rainy day scenes. The larger the density parameter, the more intense the water mist will be.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKzeVBaw3xX3jtDZ9AVHK%252Fimage.png%3Falt%3Dmedia%26token%3Dbab5090a-ebdc-47db-a560-b2e36d9057e1&width=768&dpr=3&quality=100&sign=f5bb7837&sv=2)

## Milky Way

Adjust the brightness and angle of Milky Way as needed to enhance the realism of the night sky. Supports adjusting intensity and rotation.

> ⚠️ > Note

Milky Way is only displayed in night environments.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Ff9W6JtIf0JBxxLvx7gJc%252Fimage.png%3Falt%3Dmedia%26token%3D6831e7b6-0e1b-48fa-990f-8830d8eb609e&width=768&dpr=3&quality=100&sign=cd3300fb&sv=2)