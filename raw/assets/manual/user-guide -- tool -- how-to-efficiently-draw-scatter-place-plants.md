# How to efficiently draw/scatter/place plants?

## Brush

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F21nFu7A84acsBTAaVcdz%252Fbrush.jpg%3Falt%3Dmedia%26token%3Dd125e0a0-894e-4fe4-be1c-0bbbff053182&width=768&dpr=3&quality=100&sign=8c460fb2&sv=2)

- ****Radius****: The brush radius scales according to the screen scale.
- ****Density****: Control the density of plants at the time of drawing.
- ****Size****: Controls the size of the selected plants as they are drawn in the scene.
- ****Random Size****: Controls the extent to which the size of each model size varies randomly as the selected plants are drawn in the scene.
- ****Align to Terrain****: Plants will be generated in the normal direction of the model surface when this feature selected, and will grow in the vertical direction when closed.

> ****Dynamic plants**** do not support the [Align to Terrain] feature for this time being.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FibVFFRiZbH8cnRaXhPa5%252Falign.gif%3Falt%3Dmedia%26token%3De98a5d09-b7a5-4bc3-9a69-b5abe82f2e97&width=768&dpr=3&quality=100&sign=fd9808b8&sv=2)

- For small areas, you can move the viewpoint to a closer distance and use a smaller scale brush.
- For scenes that require wider coverage, such as a bird's-eye view of a city, you can use a farther view and adjust the brush to a large scale.

> TIPS:

> ℹ️ > Hint:

For the reason of efficiency, we still limit the maximum range of brushes, the maximum adjustable brush radius is 100m.

---

## Scatter

When the Radius parameter of the Brush tool is set to Maximum, you can enable the Scatter tool, and fill the selected face with plants.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FNLW49GMiW9CkFuK250PI%252Fscatter.jpg%3Falt%3Dmedia%26token%3D4f58e58b-e3b5-435e-be53-ea4db0b228e2&width=768&dpr=3&quality=100&sign=fce85d03&sv=2)

When the Radius parameter of the Brush tool is set to Maximum, you can enable the Scatter tool.

---

## Quick Placement

When adding a model to the scene from the library, or placing a model directly in the scene, use the shortcut keys to adjust the direction of rotation and size of the object when the model follows the mouse.

****Rotation****:

- ****Tap the shortcut key R to adjust the rotation direction of the object's Z-axis****, each tap will rotate the object by 90 degrees.
- Hold the R key and drag the mouse to draw circles around the object, you can control the rotation direction of the object.

****Scale****:

- ****The shortcut key C allows you to adjust the size of the objects.**** Every time you press the C key, the object will be enlarged by 1.1 times by default.
- Hold the C key and drag the mouse left and right. Left to reduce the size of the object, right to increase the size of the object.

---

## Random Placement

> Note:
>
> - ****Random Location does not support the 'Reset' feature.****
> - The Random feature ****is not applicable to special scene resources such as procedurally-generated Vines, Path, Scatter, Light, Camera, and Section.**** When you select these unsupported resources or include them in the selection, the 'Random' feature button will turn grey, indicating it's unavailable.

### Random before placement

After 2.9 version, it supports random size and random rotation effects when continuously adding assets from the Asset Library-Nature category.

> Use the ****shortcut 'U'**** to switch random placement on/off.

### Random after placement

- Added Random Size, Rotation, and Location buttons to the right sidebar. Supports single or multi-selection. Keep clicking to generate new random effect until you are satisfied. Custom shortcuts can be set in Preferences.
- Use the ‘Reset’ feature to restore size and rotation parameters to their original settings.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FP3ywvHHpeZsQvxvhR2q9%252F13.jpeg%3Falt%3Dmedia%26token%3D5ad9709c-2809-46c5-a955-ad45a1746bbb&width=768&dpr=3&quality=100&sign=1d949b92&sv=2)