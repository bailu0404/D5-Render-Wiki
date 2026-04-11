# Why is the effect of the glass material not obvious/anomalous?

## Why doesn't the effect of glass look obvious?

There may be the following reasons:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FjWRft3O8UOceEpntgl8y%252Fglass%2520thickness.jpg%3Falt%3Dmedia%26token%3Dae91d3fb-35b8-449e-8169-095ebfcc7c03&width=768&dpr=3&quality=100&sign=93664a7f&sv=2)

---

## Why is the glass flickering/effect unusual?

The coordinates of the glass model are too far away from the world coordinate origin (0,0,0) to cause this anomaly.

Solution: Select the model in the scene resource list and zero the model coordinates in the right sidebar.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FOuN1gEQ05nvfXGWmyc9K%252Fstreak.jpg%3Falt%3Dmedia%26token%3D3d7b13b9-e7e0-4a9b-839f-29f55df1adea&width=768&dpr=3&quality=100&sign=5c886ade&sv=2)

- The effect of multiple reflections between glass is not displayed when the camera is moving.
- Multiple reflections between transparent objects are automatically calculated when the screen is stationary, as well as the colour and transparency of the glass material will be involved in the calculation of the reflection effect.

Therefore, the preview is closer to the actual image when the FPS is stable.

Single sided models imported into D5 and given a transparent material will have incorrect refraction and reflection effects.

Solution:

- It is recommended to regulate ****double-sided modelling**** to avoid such problems.
- Or turn on the ****"Thickness"**** parameter in the glass material template parameter, which can simulate the plate glass with thickness, and the single-sided glass can get the correct refraction effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQ7651VO9TokmgJVrYOak%252Fimage.png%3Falt%3Dmedia%26token%3D56e21a26-d7dd-475d-a995-b876db31398d&width=768&dpr=3&quality=100&sign=c408c2f2&sv=2)

---

## Why don't distant plants appear in the reflection of glass?

Considering the performance in preview/output, there are certain restrictions on the display range in glass reflections of ****not separately placed plants from D5 Assets Library (e.g., brushes, paths):****

The following reference values are the distances from ****the camera position**** to ****the plants**** ↓

- Models behind the current scene camera:

  - ****Grass category:****

  - Less than 15,000: Preview/Output are both 50m

  - More than 15,000: Preview is 0m, with no grass reflection visible; Output is 50m

  - ****Tree category:**** Preview/output are both 150m
- Models in front of the camera and not shown in the camera's viewport are ****150m**** in preview and ****900m**** in output.

This issue can be solved by increasing the ****Cull Distance of Outside the Viewport**** since version 3.0.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FmTCHmUgUI4QPoM7sQmoo%252Fimage.png%3Falt%3Dmedia%26token%3D35db4ea8-1a15-4925-9383-f2804bb5244e&width=768&dpr=3&quality=100&sign=e17f61ef&sv=2)

****Please note, Cull Distance of Outside the Viewport now only works for trees.**** If you want it to also work for grass, you can set it to treat grass as trees by adjusting the `Engine.ini` file, adding the following fields to it.↓

Steps:

Refer to the illustration below ↓

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FyySFSF0p01Ruqb4Jgqoh%252F12.png%3Falt%3Dmedia%26token%3D03dfff2b-81c6-4fa3-8208-0e8404061266&width=768&dpr=3&quality=100&sign=b2cfe209&sv=2)

Left: Location of the Engine.ini file Right: Relevant fields for modification