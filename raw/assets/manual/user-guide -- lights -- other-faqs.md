# Other FAQs

## 1. How to hide light source icons in the scene？

Select "Display" in the navigation bar in the upper right corner of the viewport , select the icon of the light source in the drop-down panel.

> Or ****use the shortcut L to hide all sources in one click****.

If you want to ****turn off a light source**** temporarily, you can hide it directly in the scene resources list on the left (by clicking on the eye icon).

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FEJ3ADvQ4pLyYY3aRSy69%252F3.png%3Falt%3Dmedia%26token%3D34ac7ed4-b6fe-4dac-b712-192f1a635dd5&width=768&dpr=3&quality=100&sign=49aa70ff&sv=2)

"Display--Light Source" in the navigation bar

## 2. How to duplicate lights？

Light duplication is performed basically the same way as model duplication.

> For details, please refer to : <https://docs.d5render.com/model/how-to-duplicate-the-model>

### Shift + Axes

Hold down Shift, then click on an axis in any direction to duplicate that light source in the specified direction.

### Ctrl+D/Alt+D

It will duplicate a previously selected light source at the mouse hover position.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F38I7LvdHQtBBw8GymSsB%252Fimage.png%3Falt%3Dmedia%26token%3Dc7528b0b-3f32-4537-85e7-34aa3d4b535f&width=768&dpr=3&quality=100&sign=89661638&sv=2)

## 3. How to select lights in a group in a scene？

In the scene, clicking on a light selects, by default, the group in which the light is located.

- Double-clicking on a light's icon with the mouse can select the individual light.
- If there are multiple layers in the group, click to select the highest layer by default, while ****double-clicking will select a single model/element****.

## 4. How to quickly adjust the light orientation?

Added extension lines and control points to make it easier to adjust the light orientation.

- When the target point is moved, the light source direction will follow the mouse dragging direction based on the screen view space, and if any mesh surface is reached by the mouse ray, it will be attached. When the target point is moved, the location and rotation parameters in the right sidebar will change accordingly.
- When multiple lights are selected, only the target orientation point of the last selected light will be displayed, in which case all the selected lights will change when moving the target orientation point.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFrBtH9fZao24V5Kp7lNs%252F4559002630645f7e391858afa07787845732ef42.gif%3Falt%3Dmedia%26token%3D00640385-d692-41f5-8e26-d2068592001b&width=768&dpr=3&quality=100&sign=f2c77d08&sv=2)