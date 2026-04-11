# What is "Invisible in Raytracing"?

Click on the locked model surface in the scene, or use the "Select Material" tool (shortcut key: I) to pick up the model surface, you can select the material. At this time, the corresponding material parameter panel will appear in the right column.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FDGW5KaUsphuWycnWIIca%252Fimage.png%3Falt%3Dmedia%26token%3D6d8edb7d-71c1-4bf6-acae-7dd13b7f2bfe&width=768&dpr=3&quality=100&sign=fc23dc67&sv=2)

The "Invisible in Raytracing" option controls whether the material participates in lighting (specifically, diffuse light) calculations. When this option is checked, the material will be visible in the camera and in the reflections of other materials, but it will no longer produce shadows or light bounces.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8TC9XQyM6ImORhAZano0%252F9-1.gif%3Falt%3Dmedia%26token%3De85ec6da-8922-477a-81e9-740e03a482e1&width=768&dpr=3&quality=100&sign=fcfa22e2&sv=2)

## Why does the "Invisible in Raytracing" material appears in the reflection?

Considering that the "Invisible in raytracing" material is generally used for sky exteriors, but in actual rendering, it is still necessary to display the sky exteriors in the reflection. Therefore, the "Invisible in raytracing" material will appear in the reflection.