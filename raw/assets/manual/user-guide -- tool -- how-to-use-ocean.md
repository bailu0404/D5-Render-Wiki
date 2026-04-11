# How to use Ocean?

Introduces Ocean to simulate realistic waves, coastlines, foam, water materials, and physical interactions between water and objects. By adding an Ocean object, a dynamic ocean surface can be created efficiently, with automatic detection of the scene’s terrain range to generate seamless and natural transitions from ocean to coast.

## Create and Basic Properties

### Ocean Creation

- Supports adding ocean from the top toolbar > Terrain.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJqQCyLoiGGe2nIk7SYjd%252Fimage.png%3Falt%3Dmedia%26token%3Daff53980-d8fe-432a-9680-4a7be2bbd81a&width=768&dpr=3&quality=100&sign=962808a1&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQkGhdusjFxbkyEzaNZkk%252Focean.gif%3Falt%3Dmedia%26token%3D1c5ee348-57e2-4fa1-91ea-a5243db2f7b6&width=768&dpr=3&quality=100&sign=32d4c05a&sv=2)

- An ocean object is automatically created upon selection and appears in the Resource List.
- When ocean is selected, its corresponding control panel appears on the right sidebar, enabling adjustments to coastline range, waves, and materials.

### General Attributes

The ocean divides the water body into two logical areas for fine control: the ****Surface**** and the ****Coastline****.

SurfaceCoastline

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F269m1HJdaBGsNnEsQxBD%252Fimage.png%3Falt%3Dmedia%26token%3D622a9fc3-022a-453b-9b28-ded8b332f81f&width=300&dpr=3&quality=100&sign=ad6c6c8b&sv=2)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Foaxqqc20MWyOYl5P6UZx%252Fimage.png%3Falt%3Dmedia%26token%3D8e003b81-57ae-4d60-b88a-bbfc98f0fda3&width=300&dpr=3&quality=100&sign=ca863d86&sv=2)

#### ****1. Ocean Surface****

It is used to control the behavior of deep water away from the coast, primarily affecting the wave form and the optical properties of water bodies.

****General parameters:****

- Height: Controls the sea level height.
- Wave Scale: Controls the horizontal size of waves. The larger the value, the wider the wave crest.
- Wave Height: Controls the vertical amplitude of the wave crest, affecting the wave's volumetric effect.
- Speed: Controls the flow speed of ocean waves.

****Material Settings:****

Affects the entire ocean surface material.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FrTi8pu9sietnsAbBEFy5%252Fimage.png%3Falt%3Dmedia%26token%3D71f6ed27-130f-420e-8d6d-1b2560641960&width=768&dpr=3&quality=100&sign=261a6de&sv=2)

Ocean Material Parameters

- Absorption: Controls the degree of light absorption in water. Higher values result in deeper water color.
- Scattering: Controls the light scattering effect, affecting water turbidity and volumetric effect.
- Depth: Controls the surface transparency.

****Underwater Volumetric Effect:****

- Supports simulation of underwater light scattering and turbidity to enhance realism.

#### ****2. Coastline****

Controls the effects of nearshore waves, foams, intertidal zone, and transition from land to ocean.

****Automatic Coastline Generation****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fc359doHPMm7ijNARAfVM%252Fimage.png%3Falt%3Dmedia%26token%3D52cfaec9-86c4-4946-855e-80a2302d07e3&width=768&dpr=3&quality=100&sign=a877c544&sv=2)

Supports automatic detection of intersections between terrain/geometry and the ocean surface to generate a coastline with tidal and caustic effects near the shore.

> ⚠️ > Range: For now, the coastline covers a ****5120m\*5120m**** area and ****doesn't**** allow adjustments.

****General Parameters:****

- Size: Controls the width range of the shoreline wave area.
- Shoreline Wave Speed: Controls the movement speed of waves near the coastline.
- Shoreline Wave Width: Controls the wave coverage range near the coastline.

****Material Settings:****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FjN0SREnsKJycwEQNGN6U%252Fimage.png%3Falt%3Dmedia%26token%3Dcc02ce20-56b0-4518-85a6-5baaafcdcde2&width=768&dpr=3&quality=100&sign=be8bc3&sv=2)

- Based on the height difference between the ocean surface and the ground: as the distance decreases, the color shifts toward the coastline material; as the distance increases, it shifts toward the ocean surface material.
- Absorption: Controls the dark-to-light transition of nearshore water material.
- Scattering: Controls the water turbidity near the shore to create a natural shallow water area.

****Foam Parameters:****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FdeTDBOOkk6udwYj1g0dQ%252Fimage.png%3Falt%3Dmedia%26token%3Def8bfd56-ce48-4a9a-b1d4-31b8d1da2c4e&width=768&dpr=3&quality=100&sign=3af2f45f&sv=2)

- Nearshore Foam Intensity: Adjusts the visibility and brightness of foam in nearshore areas, defined as the coastal zone where the model meets the sea surface, including island edges, structures, or terrain intersecting with seawater. Increased values result in more pronounced nearshore spray and whiter foam.
- Offshore Foam Intensity: Adjusts the overall visibility and brightness of foam in offshore waters. Higher values produce a more distinct spray in distant waves and whiter foam.
- Offshore Foam Size: Modifies the scale and distribution density of offshore foam on the sea surface. Higher values increase both the quantity and density of offshore spray and foam.

> ****Note:**** The change in foam direction when adjusting this parameter is under expectations; the value corresponds to the number of divisions of the foam area.

- Offshore Foam Offset: Adjusts the positional displacement of offshore foam textures on the sea surface.

X-axis Offset: Adjusts the horizontal (left-right) translation of foam.

Y-axis Offset: Adjusts the depth (front-back) translation of foam.

****Coastline Anchor:****

- Supports select objects from the viewport or the resource list as the Coastline Anchor, around which the coastline will be automatically generated.
- Supports individual objects only. Grouped/path-based/scattered/.abc objects are not supported.
- The coastline area updates dynamically with any addition/deletion/modification of anchor objects, similar to the cull effect of D5 Scatter.
- Allows up to 50 objects to be set as Coastline Anchors.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FnEF5GqJk2Ve2VACxjefH%252F14.gif%3Falt%3Dmedia%26token%3D8b35d12f-3cf2-436e-b9dd-b6cc538de4a6&width=768&dpr=3&quality=100&sign=939ffcb2&sv=2)

operation

****Auto-refresh of Coastline Range:****

The following actions lead to auto-refresh of the coastline rage:

- Adjust ocean surface height
- Sculpt and modify terrain
- Modify terrain range
- Add Coastline Anchor objects

****Manual Refresh of Coastline:****

The following actions require manual refresh of the coastline rage:

- Delete/edit Coastline Anchor objects

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FIhbmjFLg8FbqK2Y7bP44%252Fimage.png%3Falt%3Dmedia%26token%3Dc8fdec81-74ea-4399-9ab7-c3ca1f348473&width=768&dpr=3&quality=100&sign=95236d5e&sv=2)

Refresh button