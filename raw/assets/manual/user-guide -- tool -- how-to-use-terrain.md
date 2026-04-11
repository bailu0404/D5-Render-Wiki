# How to use Terrain?

Directly create terrain in D5, using brush tool for sculpting and texture painting. Easily apply a variety of preset heightmap resources and material templates with just one click, and combine with D5 Scatter to effortlessly craft diverse natural landscapes.

- Added Terrain tool in the top menu bar. Upon clicking, the default terrain will appear in the viewport, featuring an endless plane and an editable area within the white wireframe. The editable terrain spans 4000m x 4000m.
- Terrain can be selected, hidden, or deleted from the resource list on the left via right-click. After selecting the terrain in the object list, terrain sculpting, texture painting and heightmap management can be enabled in the right sidebar.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F4xwMJMBfuaVxL8QBcHyY%252Fen.png%3Falt%3Dmedia%26token%3D0413b9d9-3aa0-45c1-86c1-aaa59d54ce42&width=768&dpr=3&quality=100&sign=a4276f85&sv=2)

## Sculpt:

### ****Terrain sculpting modes****

- ****Upward:**** Increase the height of selected areas.
- ****Downward:**** Reduce the height of selected areas.
- ****Erase:**** Erase sculpted shapes to restore the terrain to its previous or flat state.
- ****Smooth:**** Smoothen the terrain surface, remove sharp edges or unnatural bumps.
- ****Flatten:**** Level the selected area, typically used to create plains or platforms.

> Note:
>
> Users can use ****the shortcut key Alt**** to switch Sculpt-Upward/Downward.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6psZQ0204cUxDu0KV5z0%252Falt11_compressed.gif%3Falt%3Dmedia%26token%3D52301ea1-7239-416f-bb28-9f9724d6e80e&width=768&dpr=3&quality=100&sign=43c7d31&sv=2)

### ****Sculpt brush settings****

- ****Size:**** Control the size of the area affected by the Sculpt tool.
- ****Strength:**** Control the intensity of the tool's effect on the terrain.
- ****Edge Falloff:**** Control the effect that decreases from the center to the edge.
- ****Angle:**** Controls the angle of the brush texture map.
- ****Brush texture:**** Control the shape drawn by the Sculpt tool using the preset maps in the brush library.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSMEUA5z5PXqGVvn8TsOy%252Fimage.png%3Falt%3Dmedia%26token%3Db865bcae-231f-48e6-a4d1-70b87c27e201&width=768&dpr=3&quality=100&sign=876b0077&sv=2)

### ****Heightmap Resources****

Added 'Terrain' library into D5 Asset Library, providing preset terrain templates for easy access.

- Currently, a maximum of 10 height map resources can be added simultaneously.
- After placement, height map can be replaced (supporting formats include .png, .r16, and .raw), along with height settings, edge falloff, and other parameters.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FgXP3ljkl2NLQ48jJNbyw%252Fscreenshot_2024-12-18_19-26-57.png%3Falt%3Dmedia%26token%3D8e7ea128-7181-42fb-912f-37ad1e0e2d73&width=768&dpr=3&quality=100&sign=22abe6dd&sv=2)

- Supports to bake all height maps to total height

Added Apply to terrain option in Height maps column, which applies all height map results to the total height and inherits its blend mode relationship with the overall height map before application.

> Supports Undo

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7VXZHMnNV0qm3CooOycE%252Fbake.gif%3Falt%3Dmedia%26token%3Db7fa4163-4081-485b-a490-f380378eaecc&width=768&dpr=3&quality=100&sign=375230f&sv=2)

### ****Reset Height****

Click the 'More' button on the right side of the Landscape panel to reset the terrain height. All terrain effects created with the Sculpt brush will revert to the initial flat state

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7Z2t7DMITFCzLsvfFtke%252Fscreenshot_2024-12-18_19-51-41.png%3Falt%3Dmedia%26token%3D96683b15-258d-49ee-9a6b-cfe109b08d2a&width=768&dpr=3&quality=100&sign=b54741a5&sv=2)

---

## Terrain texture editing:

Enables assigning different textures to different parts of the terrain (ground, slope, peak).

### ****Ground****

Ground texture mainly appears in flatter areas of the model.

- Supports up to 6 materials. Click on the "+" icon to open the asset library and add the required material.
- The first material serves as the primary texture covering the ground surface. The other five materials can be added onto the primary texture using the Paint tool.

The Paint tool provides several parameters available for blending materials:

- ****Size:**** Adjust the size of the brush's influence area.
- ****Strength:**** Control the extent to which the new material covers the original material.
- ****Edge Falloff:**** Control the transition between different materials for an organic appearance along edges.
- ****Brush texture:**** Support using preset maps from the brush library to control the shape of the brush tool.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FL7RaQ8CuFSE1X1xJ4nul%252F3.png%3Falt%3Dmedia%26token%3D22ceb3f7-8eed-4693-8abe-44fc25fa1b95&width=768&dpr=3&quality=100&sign=10a54856&sv=2)

### ****Slope****

Slope texture mainly appears in steeper areas of the model and allows adjustments for ****slope range**** and ****weathering levels**** to help create natural slope effects.

### ****Peak****

Peak texture appears in the higher elevation areas of the model and supports maintaining peak altitude, as well as adjusting edge blending, erosion, and UV stretching to better simulate realistic peak environments.

> - All the ****material channels**** support custom maps, base color, normal, roughness, and random UV.
> - Right-click or hover over the material channel and click the ****'More'**** button to replace or delete the current material. This allows you to replace/delete the current material, enable/disable template override, add the current texture to local, and create a scatter area on the current material.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FtjE6hidk5M0aWxwf91R7%252Fterrain%25E5%258F%2582%25E6%2595%25B0.gif%3Falt%3Dmedia%26token%3D219791bb-f06d-47ec-a3df-751325875c0a&width=768&dpr=3&quality=100&sign=e0bd8772&sv=2)

### ****Material Template****

Available in Assets > Terrain and can be applied with one click.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FRVTUjG5HoBTkPt0fmvec%252F4.png%3Falt%3Dmedia%26token%3Df0150445-6471-41b6-81f6-84714165bb2d&width=768&dpr=3&quality=100&sign=733b514c&sv=2)

---

## Surface Texture:

Added Erosion Mask to Paint > Surface Texture for accurate control over the erosion effect and area. Supports automatically adapting the erosion layer to changed terrain heights.

> ⚠️ > ****Note:****

- The erosion layer effect ****will be refreshed automatically**** and calculated according to the current terrain height. This process will take a small amount of time to complete.
- Supports Undo

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSw3n2ZHOjuHAPvMq05aL%252Fimage.png%3Falt%3Dmedia%26token%3Dc1e81b29-057e-478f-9f00-7526ccfd1c0f&width=768&dpr=3&quality=100&sign=1ee9aad0&sv=2)

---

## Height map import:

Supports importing custom height maps to generate corresponding 3D terrain models based on the topographic relief presented by the image.

- It is recommended to import height maps with a minimum bit depth of 16-bit and a resolution of at least 2K.
- Supports to reset height via the ****'more'**** option.

> \*Heightmap can represent terrain height with grayscale values. Typically, black (value 0) indicates the lowest point, while white (value 255) indicates the highest point.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FtI7wPyjLcKJC0Xrepm8e%252Fimage.png%3Falt%3Dmedia%26token%3D9f52db9f-5ab4-455e-90df-fc240773c9af&width=768&dpr=3&quality=100&sign=46feebf8&sv=2)

---

## Terrain Area Setting:

Supports setting terrain range and Z-axis position. Added Terrain Range Settings to Terrain > Manage.

- Position: Determines the position of the boundless plane along the Z axis.
- Size: Determines the size of the editable terrain range. Smaller terrains take up less ram and vram.

> ⚠️ > ****Note:****

Changing the terrain size will affect the painted materials and heights. Please operate with caution.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FNA0vZs7yVOYg8C4pTmR4%252Fimage.png%3Falt%3Dmedia%26token%3D896f3719-2f71-455f-8ea6-6b8deb07c1c0&width=768&dpr=3&quality=100&sign=a8c98dd1&sv=2)

---

## Creating Scatter on Terrain:

- Supports creating Scatter on the terrain using the ****"Select Material"**** method. When selecting materials, it automatically picks up the textures from peaks, slopes, and the ground.
- To select a specific material for Scatter, right-click the corresponding material channel in the terrain texture editor and choose "Create Scatter Area."

> ℹ️ > ****Note:****

The ****"Select Model"**** method is not supported for creating Scatter on the terrain.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F9rrtGDjbqxU3LGxggwm4%252Fw.png%3Falt%3Dmedia%26token%3Da48f4309-5e7d-4f42-8d22-f35aba9b6f58&width=768&dpr=3&quality=100&sign=ce359f4c&sv=2)