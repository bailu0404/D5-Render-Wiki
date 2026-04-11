# What is 'Real-time Path Tracing'?

> Real-time Path Tracing is D5's self-developed Global Illumination (GI) technology scheme to optimize real-time rendering + image outputs + video outputs.

## 1. Preference - Legacy D5 GI Compatible Mode

In Preference > Rendering, users can enable ''Legacy D5 GI Compatible Mode''.

- Enabling this option activates the ReSTIR Surfel GI from D5 2.9 version to maintain visual consistency across legacy scenes.
- This option solely works for better compatibility. It will be removed in future releases.

> ****Please note:****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fz9U8f5vMA8NyfG0IUrOq%252Fimage.png%3Falt%3Dmedia%26token%3D48191538-8bd4-49fd-93c3-54db52cbba01&width=768&dpr=3&quality=100&sign=e14c6248&sv=2)

## 2. Display - Accumulation&Custom Settings

The upper right scene control ‘Display - Precise Realtime Quality’, provides an ‘Accumulate’ button and custom settings.

> ℹ️ > ****Note:****

Custom parameters do not affect the preview, only the quality of the accumulation mode, the rendered images and the rendered videos.

(After adjusting custom parameters, it is necessary to click ‘Accumulate F4’ to see the corresponding effect in the preview interface.)

### 2.1 Accumulate (shortcut F4)

When enabled, pixel samples will be accumulated until the real-time preview quality reaches the final output. Moving the camera or pressing the ESC button will terminate the process.

### 2.2 Custom parameters

> ****Note:****
>
> When custom settings are enabled, they will be applied to the accumulation.
>
> Otherwise, it's set by default to GI Precision at 1, Reflection Depth at 2, and SPP at 64.

- ****GI Precision:**** This parameter affects the number of GI bounces and includes 3 levels. The lower the level, the faster the accumulation converges; the higher the level, the more accurate the GI quality of the image.

> ****Note:**** The quality of GI in reflections is also affected by the ‘GI Precision’.

- ****Refl. Depth:**** Controls the number of times rays bounce between highly reflective material surfaces.
- ****SPP:**** Determines the number of times each pixel is sampled. Increasing the value helps optimize artifacts in challenging areas and enhance details but will also increase the rendering time.
- ****Roughness limit:**** The roughness of the material used in the calculation has an upper limit that can be adjusted. The default value is 0.5. Setting a higher value for this limit will result in more accurate accumulation and rendering, ensuring consistency between the preview and the final output.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F9ZFXX47Mb3RLQj6PmDam%252Fimage.png%3Falt%3Dmedia%26token%3Dd73df10a-647b-4406-b409-38521cb7125e&width=768&dpr=3&quality=100&sign=37b62208&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fiej3J7Aq5r89VQ38R6CK%252Fgi%2520custom.gif%3Falt%3Dmedia%26token%3D440769c3-1ce9-45be-83ee-5ad21d6db689&width=768&dpr=3&quality=100&sign=b6b111eb&sv=2)

## 3. Major changes in the new GI

### 3.1 Improved GI Caching

The new GI solution has improved both quality and precision. It utilizes path tracing to calculate and cache ray bounces before rendering begins, thereby improving caching quality.

> For example: Below is a relatively special high-reflection floor scene.
>
> In version 2.9 of the preview viewport, the floor did not accurately render highly reflective objects, appearing inaccurate and blackish. In version 2.10, the metal floor appears correct reflection effects.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fy5ZULIzZvxfILzUA3cEt%252Fgi%25E5%258F%258D%25E5%25B0%2584%25E5%25AF%25B9%25E6%25AF%2594.png%3Falt%3Dmedia%26token%3D6fdb2f2f-a012-4a2d-8b8f-1742d098d28f&width=768&dpr=3&quality=100&sign=27942d76&sv=2)

### 3.2 Optimized GI bouncing details

GI bouncing details are more accurate in areas like the joint where the wall meets the floor.

### 3.3 Unbiased sampling and visibility detection

The sampling logic has been optimized to sample more important pixels in a more efficient way. This makes indirect lighting details closer to the Ground Truth.

> Especially in the corner parts of some indoor and outdoor scenes, the change is more obvious.

### 3.4 Optimized plant and fabric materials

Improved the color shading model for plant and fabric materials, fixing the color attenuation issue in light transmission, resulting in more physically accurate transmission effects. As a result of these improvements, the color of vegetation and their reflections may change if they were created using previous versions.

> ℹ️ > ****Note****

Due to these improvements, the color of plants and their reflections in old archives may change.