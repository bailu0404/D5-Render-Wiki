# What materials are the Subsurface scattering templates suitable for? What are the special parameters

After switching to the Subsurface scattering template, most of the parameters are exactly the same as the custom template. The definition of normal, specular, roughness, AO and other parameters refer to the custom template, ****matallic parameter adjustment and emissive feature are not supported****.

## Base color/ Base coler map

Control the colour of the light on the surface of the material.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FOYuQOqinvmVptTkR2Y11%252Fsubsurface.jpg%3Falt%3Dmedia%26token%3D216a3f61-dd26-458c-bc1f-6b22fa9ba4da&width=768&dpr=3&quality=100&sign=ca49421e&sv=2)

## Scattering color

Controls the color of light being scattered inside the material. The brighter the color, the more translucent the material appears.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FAVXx1VKVFoEAzOsQzfVE%252Fsubsurface%2520color.jpg%3Falt%3Dmedia%26token%3D6a181d10-947d-4317-87ef-5d585f9f4266&width=768&dpr=3&quality=100&sign=24e9080b&sv=2)

## Scattering intensity

The multiplier value of the subsurface color. The larger the value, the more transparent the material appears.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FDFmafGRqyvcqSFYVge4F%252FScattering%2520intensity.jpg%3Falt%3Dmedia%26token%3D3dcb9b1c-5f2b-4fa6-bc7b-486c6bdcbb81&width=768&dpr=3&quality=100&sign=862dc798&sv=2)

## Sky light

Allow environmental light (sky light and HDRI in the GeoSky) to influence the subsurface scattering effect.

> Note: This option increases the rendering overhead.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FlZbHtlFBDtr6IvWp5aJf%252Fsubsurface%2520sky%2520light.jpg%3Falt%3Dmedia%26token%3D403e7077-0fc9-43df-b635-17d54e882a07&width=768&dpr=3&quality=100&sign=f389fe23&sv=2)