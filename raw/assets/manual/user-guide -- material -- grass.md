# How to set grass? How to grow grass with one click?

Use the Grass material template to quickly create large areas of natural grass.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-Mket05fc_W0B0rNHtfF%252F-MkeuquObuEXjS4h44Jh%252FGrass1.gif%3Falt%3Dmedia%26token%3Dc2c47de6-f7c4-402a-a8ec-a0b20de2bfcd&width=768&dpr=3&quality=100&sign=7a29cf00&sv=2)

The grass material parameters are as follows:

- ****Base Color/Base Color Map:**** Controls the color of the ground as well as the grass.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-Mket05fc_W0B0rNHtfF%252F-MkevBkY7UplZRYo7tcx%252FGrass11.gif%3Falt%3Dmedia%26token%3D23029dc9-abc3-472c-92d2-6e7de7aa7c2c&width=768&dpr=3&quality=100&sign=cad81e2c&sv=2)
> ✅ > It is recommended to use a grass texture map linked to the Base Color Map slot, the generated grass will automatically load the color of the base color map to generate a natural grassland.

- ****Normal:**** Controls the bumpy effect of the ground below the grass.
- ****Specular:**** Controls the Reflectance of the grass and the ground.
- ****Roughness:**** Controls the Roughness of the grass and the ground, which affects the reflection blur.
- ****Height:**** Controls the height of the automatically generated grass.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-Mket05fc_W0B0rNHtfF%252F-MkevS2fO1p23Qlc6Wfl%252FGrass111.gif%3Falt%3Dmedia%26token%3Df120f29a-a8e5-480b-b8f5-6d8fb6cb887e&width=768&dpr=3&quality=100&sign=74f79581&sv=2)

## FAQS

- The grass material algorithms of versions before 2.7 make it hard to align with the edges of small-area models. Users have to manually fill in the flawed areas with models from D5 Asset Library > Nature > Other Herbs, which can also be found by searching 'Grass Material'.
- D5 2.7 optimizes grass with better scattering and edge-cutting algorithms to precisely align with model edges. It also optimizes existing grass materials with brighter colors and a denser appearance in aerial view.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Ft30dWmdJo0RbKJTBSpY5%252Fimage.png%3Falt%3Dmedia%26token%3D8f58bd7f-2402-437d-92d0-6c5741237161&width=768&dpr=3&quality=100&sign=7728a351&sv=2)

Comparison of Grass between 2.6 and 2.7

Models having chamfers or uneven surfaces may cause the grass to be lifted. In this case, please modify the model.

Please adjust this part of the model.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FTepE9VrADcDp1F0ffo3O%252Fimage.png%3Falt%3Dmedia%26token%3D38599790-8cf6-439e-8a9a-c87877333e29&width=768&dpr=3&quality=100&sign=2b6e8a89&sv=2)

For real-time efficiency, the grasses in the farther distance will become pure colour in the preview, and will be shown as the actual terrain grass effect in the output, which will not affect the rendering results.

In ‘Preference’ -> ‘Rendering’ -> ‘Cull Distance’, you can set the fading distance from the camera for the smaller online assets library models in the scene to achieve the desired effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FWsNrnesGTKRAYUdXQDnD%252Fimage.png%3Falt%3Dmedia%26token%3D509a0890-3496-4d97-8546-49e275b9a1f2&width=768&dpr=3&quality=100&sign=da162b32&sv=2)

Preview Cull Distance: Support to set the fading distance within the preview, the range is 20-9999 metres. When the distance is large, it will cause real-time preview lag.

Output Cull Distance: Support to set the culling distance when rendering images, the range is 20-9999 metres. When the distance is large, it will prolong the time of rendering out. To ensure the consistency between rendering and preview, the output cull distance must be greater than or equal to the real-time cull distance.

> You can set different distances for real-time preview and rendering results separately, and this option follows the archive record.

Please check the model faces before using the terrain grass material, terrain grass will only be generated on the positive side of the model normal.

In SketchUp

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FevfWF16xXb3n9Kl0Q14G%252Fimage.png%3Falt%3Dmedia%26token%3D0a95bac5-4b3e-4544-8e61-1a9d842d2e8a&width=768&dpr=3&quality=100&sign=981971ab&sv=2)

In D5 Render

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fp8dgrHw3LbdK0wFaNVST%252Fimage.png%3Falt%3Dmedia%26token%3D9f18db4f-34a9-4ff5-a742-4197dd97cadb&width=768&dpr=3&quality=100&sign=22d650fe&sv=2)

This is a known issue with the current version: terrain grass is not displayed in orthogonal view (only the base color map is displayed).

Please avoid using terrain grass in orthogonal views.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F3f3hKzJ7lv1jSnsuebTA%252Fimage.png%3Falt%3Dmedia%26token%3D340a1b91-6367-4ead-9c33-6c1ebc517159&width=768&dpr=3&quality=100&sign=440e0fb5&sv=2)

Perspective View Effect & Orthogonal View Effect

The current version restricts the terrain grass area to a maximum of 25 square kilometers.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FX5HX4NiVT6CKIQH4Je5u%252Fimage.png%3Falt%3Dmedia%26token%3D413ddc9a-a6f0-4dbe-b546-b6a039133210&width=768&dpr=3&quality=100&sign=4412b590&sv=2)