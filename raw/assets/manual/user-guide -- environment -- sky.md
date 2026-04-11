# How to adjust parameters of Sky Light?

## Geo Sky

Geographic sky can quickly provide natural lighting for interior and exterior scenes.

### Simple adjustment

Drag the sun angle control lever to change the time period and the corresponding sun angle.

- As the sun angle changes, the color of the sky will dynamically change accordingly, showing the light color in the early morning, noon, dusk and other time periods.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F5npTJ9MUMvkxVVBRP3ON%252Fsky.gif%3Falt%3Dmedia%26token%3D576ae296-a321-41d7-adbc-a4f8c1f23986&width=768&dpr=3&quality=100&sign=e3eeb4f0&sv=2)

### Precise Simulation

The Geo and Sky system can accurately simulate the real sunlight angle, which is great for project preview and visualization.

- Click the `⋮` button to the right of the ****North Offset**** to expand the detailed parameter panel.

> - The default parameter of the geographic sky is the sun angle at 16:00 PM on January 1 in Nanjing, Jiangsu Province (D5 headquarters, 118.8°E, 32°N).
>
> Please modify the parameters according to the actual geographic data of your own project in order to get accurate simulation results.

#### ****1.North offset****

This parameter is used to correct the direction of "north compass".

Drag the control and the sun's orientation will rotate horizontally. The default value of the control is in the middle, meaning no offset. In the top view, dragging to the right or entering a positive value will rotate the north direction clockwise.

D5 Render will set one of the main axis direction of the model as north. e.g. The positive direction of green axis in SketchUp scene will be recognized as north.

> This means that the axes of most scene files deviate from the geographic north direction, which can be corrected by using the "North Offset" parameter.
>
> For example, if you set the time to 12:00 noon, the shadow of an object north of the Tropic of Cancer (23.5°N) will then point due north.

#### ****2.Time****

Enter parameter as needed.

#### ****3.Date****

Enter parameter as needed.

#### ****4.Latitude and longitude****

Please enter the real latitude and longitude coordinates of the project.

- The positive value of the longitude parameter indicates the E longitude, and the negative value indicates the W longitude (parameter range 180°~-180°).
- The positive value of the latitude parameter indicates N latitude, and the negative value indicates S latitude (parameter range 90°~-90°).

Note that here is Decimal Degree (DD), different from Degree Minute Second (DMS), accurate to one decimal point. Pay attention to the conversion in actual use.

> For example: 35°30'E should be converted to 35.5°E.

#### ****5.Custom sun/moon/starlight parameters****

Supports to custom adjust relevant parameters to meet specific scene requirements.

- Sunlight Intensity: Controls the brightness of the Sunlight source.
- Sun Disk Radius: Controls the diameter of the sun in the sky also affects the softening of the shadows to some extent, but the scene brightness stays the same.
- Moonlight Intensity: Controls the brightness of the moonlight source.
- Moon Disk Radius: Controls the diameter of the moon in the sky, but the scene brightness stays the same.
- Starlight Intensity: Controls the brightness of stars.

> Note: **Sun Disk Radius & Moon Disk Radius** are artistic effect options, not physically accurate.

#### ****6.Caustics****

Supports Sun Caustics to better simulate the visual effects of refraction and reflection of sunlight in the real world.

- ****Caustics Intensity:**** The multiplier value of the Caustics effect, the higher the value, the brighter the caustics.
- ****Softness:**** The degree of Caustics softening which takes effect at the Light Source Radius greater than 0.

> Note:
>
> To achieve the caustic effect, the ‘Caustics’ option must be enabled simultaneously for both the material and the light source. Among the materials, only the "Custom", "Transparent" and "Water" material templates currently support caustics.
>
> The Custom material supports reflective caustics,
>
> the Transparent and Water materials support both reflective and refractive caustics;
>
> For more details, please refer to: [How to achieve caustics effect](https://docs.d5render.com/user-guide/material/how-to-achieve-caustics-effect)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FXVMpdcUKnApq3t7oqE9O%252Fimage.png%3Falt%3Dmedia%26token%3D3e91cb64-e3c0-4141-8b4e-4359b0b8f423&width=768&dpr=3&quality=100&sign=54a779e8&sv=2)

Geo Sky

## Custom

Click the ‘Custom’ panel to expand the detailed parameter panel and adjust the daytime and night parameters.

### Custom Daytime

#### 1. Sunlight Intensity

Controls the brightness of the Sunlight source.

#### 2. Sun Disk Radius

Controls the diameter of the sun in the sky also affects the softening of the shadows to some extent, but the scene brightness stays the same.

> Note: This option is an artistic effect, not physically accurate.

#### 3. Altitude

Adjusts the height of the sun in the sky by the altitude.

#### 4. Azimuth

Adjusts the direction of the sun in the sky by the azimuth.

#### 5. Caustics

Enable the caustics calculation of the sun.

> To achieve the caustic effect, the ‘Caustics’ option must be enabled simultaneously for both the material and the light source.
>
> For more details, please refer to: [How to achieve caustics effect](https://docs.d5render.com/user-guide/material/how-to-achieve-caustics-effect)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FRoDJfHyE8ImxW354EWsS%252Fimage.png%3Falt%3Dmedia%26token%3D68323d66-a4f7-4df3-8496-afcb89e435d6&width=768&dpr=3&quality=100&sign=67040f24&sv=2)

Custom Daytime

### Custom Night

#### 1. Moon Intensity

Support to adjust moon brightness as needed.

#### 2. Moon Disk Radius

Supports to customize the size of moon, the diameter of the moon in the sky will change significantly when adjusting the parameter, but the brightness of the scene stays the same.

> Note: This option is an artistic effect, not physically accurate.

#### 3. Moon Phases

Customize the moon's waxing and waning by adjusting the moon phase.

#### 4. Moon Phase Direction

Customize the direction of the moon's waxing and waning by adjusting the moon phase direction.

5. Altitude

Adjusts the height of the moon in the sky by altitud.

#### 6. Azimuth

Adjusts the orientation of the moon in the sky by azimuth.

#### 7. Starlight Intensity

Adjust the brightness of the stars in the sky.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FI0L6g0seorPraUpM9fVV%252Fimage.png%3Falt%3Dmedia%26token%3D8eb67a3e-22a5-43dc-98f6-60ecdb9de28e&width=768&dpr=3&quality=100&sign=a960a910&sv=2)

Custom Night

## HDRI

### Background Knowledge

#### What is HDRI?

****HDRI is the abbreviation of High Dynamic Range Image.**** Common image formats are hdr, exr, etc.

> - The opposite concept is called ****"LDRI (Low Dynamic Range Image)"****. Images in jpeg and png formats are all LDRI.

How can we create an HDRI?

Usually, using a camera to capture the same scene at different exposure levels, resulting in several LDR images. Then using specific software, combine LDR information into a single image to obtain an HDR image. Ideally, the pixel values in an HDR image are proportional to the true intensity of light in nature. It records both very bright and very dark information, the so-called "dynamic range" is very high.

> ✅ > ****HDRI is not only the background, but also illuminates the whole scene.****

#### Why use HDRI?

Here's an example to demonstrate the benefits of HDRI.

Open the low and high dynamic versions of the same image in Photoshop and place them together.

(HDR image credit: [Sunflowers HDRI • Poly Haven](https://polyhaven.com/a/sunflowers)).

- The upper image is in jpeg format, bit depth: 8 bits/channel.
- The lower image is in hdr format, bit depth: 32 bits/channel.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkevVflUG8ncLT5OEI9%252F-Mkevir-zOlosCJndxb7%252F03%2520%25E5%259B%25BE%25E7%2589%2587%25E5%25AF%25B9%25E6%25AF%2594.png%3Falt%3Dmedia%26token%3D6c46bd1f-b4e3-486c-ab3a-7d3b6332eb99&width=768&dpr=3&quality=100&sign=88b4f0ff&sv=2)

By default, both images look the same on the screen, because the bit depth of the screen display is also 8 bits/channel.

Information outside of this range will appear on the screen as "overexposed" pure white, or severely underexposed pure black.

Let's add [Exposure] adjustment layers to both images and lower the exposure level by 3 stops:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkevkfRIhbO8dVCCrbf%252F-Mkevs1PqDSbnajq9BRr%252F04%2520%25E9%2599%258D%25E4%25BD%258E%25E6%259B%259D%25E5%2585%2589.png%3Falt%3Dmedia%26token%3De36e7d2a-440e-4147-8c76-576af444a335&width=768&dpr=3&quality=100&sign=43506f8d&sv=2)

The difference is apparent:

- in the lower HDR image, the areas that were overexposed and turned white show more content: cloud detail, blue sky, sun, etc.
- The overexposed areas of the LDR image above, on the other hand, simply change from pure white to a dull gray, because no detail was recorded in these overexposed areas in the first place.

We use these two images, as the sky environment background, to render the model, and the difference is also significant:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkOLtC1GoTmMvKGp2c_%252F-MkOLw98dbWaGy6qAB1E%252F5dce3084-eb57-466c-af92-8413d2cd4196.gif%3Falt%3Dmedia%26token%3Dce042403-ce6e-4b73-bf96-890cd22fd127&width=768&dpr=3&quality=100&sign=5a6a5b71&sv=2)

Differences in sky details:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkOLtC1GoTmMvKGp2c_%252F-MkOM4EHt-iNmNo569T_%252Fa9202cb5-6abf-43d0-98cf-385fe178b70d.gif%3Falt%3Dmedia%26token%3Dd545f751-d41e-4706-88b9-7a1b6e738391&width=768&dpr=3&quality=100&sign=6dc4b8dc&sv=2)

Differences in reflection details:

Most importantly, the sun in HDRI can cast shadows:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkOLtC1GoTmMvKGp2c_%252F-MkOMFUyeqLwcuhlzqft%252F34de5fef-76a0-42f9-b1f0-1366c69ee436.gif%3Falt%3Dmedia%26token%3D9744bb1e-e592-4a82-b61b-a5527c976b53&width=768&dpr=3&quality=100&sign=1b4c5d1f&sv=2)

HDRI can cast shadows

#### What should I look for when selecting HDRI?

The HDRI environment used in D5 Render are "spherical projection" panoramas. In addition, there are other common panorama projection methods such as cubic and mirror ball.

The spherical projection panorama is characterized by:

- ****Image aspect ratio is 2:1****
- The horizon line is usually at the middle height of the frame.
- The content of the picture can completely cover all angles around the camera.

Here is what a typical HDRI image suitable for D5 Render would look like (compressed to a low dynamic image for web display purposes), and we are going to use this type of image for Sky Light.

(HDR image credit: [Sunflowers HDRI • Poly Haven](https://polyhaven.com/a/sunflowers))

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkOLtC1GoTmMvKGp2c_%252F-MkOMVjHNPM5psMOAFwg%252F87719105-00cb-49dc-bdbe-b13a64439120.png%3Falt%3Dmedia%26token%3D4af611df-49dd-43d9-abc9-f579e5cdc9ad&width=768&dpr=3&quality=100&sign=e62ce007&sv=2)

### Detailed explanation of parameters

#### 1. Light

Overall control of the brightness of the HDRI image, which affects the lighting of the scene.

Note: If Auto Exposure is turned on, it will always compensate for changes in overall brightness, making the adjustment of this parameter less effective:

- Skylight: Adjusts the effects of light and material diffuse reflections individually. Does not affect material reflections.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FqNlNVhhuqiEw5m9r0eZo%252Fskylight.gif%3Falt%3Dmedia%26token%3D3f39a3ea-4ff0-4dbe-a51b-bf7e2c4a8b30&width=768&dpr=3&quality=100&sign=f06a5026&sv=2)

- Background: Adjust the brightness and darkness of the background individually. Affect the material reflection.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FHqHZItFDYZSV8P1DcnTe%252Fbackground.gif%3Falt%3Dmedia%26token%3Dc33b6fbd-8100-460e-9fc0-afb46f7958d3&width=768&dpr=3&quality=100&sign=ca626531&sv=2)

#### 2. Rotate

Rotates the HDRI sky environment map horizontally, this affects the content of the background, the material reflection environment, and the sun's azimuth.

#### 3. Flip Horizontal

Supports flipping the current HDRI.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FBcZQ5rmk4nMWOaaAmgSv%252Fimage.png%3Falt%3Dmedia%26token%3D36dd0b4e-bf01-474f-95ac-5ecc4590c9a6&width=768&dpr=3&quality=100&sign=d4f0969f&sv=2)

#### 4. Sky Temperature and Sky Color adjustment option

Sky Temperature: Affects the colour tendency of the sky lighting, which will affect the diffuse lighting effect, not the background image or reflections. The default value is 6500K, the lower the temperature, the more yellowish the diffuse reflection, the higher the temperature, the more bluish the diffuse reflection.

Sky Color: Supports Hue and Saturation adjustments.

- Hue: The default value does not affect the original hue. Adjust parameters to change the degree of hue shift.
- Saturation: The intensity or purity of colors, with the parameter ranging from -100 (grey) to 100 (fully saturated).

Adjustments to Temperature and Sky Color only work on Skylight (i.e., sky light color) by default. Supports setting the 'Area of Effect' to 'Background Only' or 'All'.

Note:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLXeZicfxqReLISQr7oMQ%252Fimage.png%3Falt%3Dmedia%26token%3D48554ef1-2a4e-4852-8f1a-9779091f4f08&width=768&dpr=3&quality=100&sign=b05252b9&sv=2)

Sky Color

#### 5. HDRI Resolution Control

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLmR2EAcFfU0LbXjXqAn5%252Fimage.png%3Falt%3Dmedia%26token%3Db4f02d9b-9317-4110-b8fd-beccb57fa0b3&width=768&dpr=3&quality=100&sign=c20047dc&sv=2)

- Added HDRI Resolution to ****Preference > Rendering**** with 2K, 4K, 8K, and Actual Resolution options. The resolution setting affects both real-time viewport and image/video output.
- The Default setting, Adaptive (recommended), inherits the logic of previous versions, which compresses HDRI to 2K resolution for viewport to boost FPS and reduce VRAM consumption, while supporting a panoramic background up to 8K resolution for image/video renders.

> ⚠️ > ****Note:****

Higher resolutions consume more graphics memory. Please set the resolution appropriately based on hardware capabilities to avoid lag or crash.

---

## FAQs

### How to reuse HDRI images in archives?

There are two ways to achieve this in the current version:

The HDRI images used in the archive are saved in the corresponding asset path, which allows you to find the HDRI images you need directly.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFTNotVt5TVxZIIjlG9jL%252Fimage.png%3Falt%3Dmedia%26token%3D34bc75f9-39c3-4f9b-a9a1-3821e271238a&width=768&dpr=3&quality=100&sign=7c44a813&sv=2)

Where HDRI images are saved in archive files

Through Studio-save preset feature, you can add the environment/effect parameters of the current scene to My Space/Team Space. (If you only tick Effect when adding environment and effect preset, the preset parameters added successfully will only contain effect information, without environment information such as HDRI).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FjpIhIFGEBU4rZ8q9xcbQ%252Fimage.png%3Falt%3Dmedia%26token%3D8a55f14a-46ee-4ebf-97d9-32990e3a55da&width=768&dpr=3&quality=100&sign=cae3934f&sv=2)

Creating environment and effect preset