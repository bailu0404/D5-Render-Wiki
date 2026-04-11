# How do I adjust the material UV and why does adjusting the UV have no effect?

The UVs of the material are currently divided into two parts: the individual UVs of the parameter maps and the overall UVs of the material.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fps7VDOpUpbTb7QXDlacP%252Findividual%2520UV.jpg%3Falt%3Dmedia%26token%3Dc6cbd428-2853-450f-a57d-28f133f1959d&width=768&dpr=3&quality=100&sign=ebb55bd7&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FC6WcKELTtX1ZengBft0Q%252FUV.jpg%3Falt%3Dmedia%26token%3D476ebdfd-3a3d-4954-a90c-efd840d75941&width=768&dpr=3&quality=100&sign=68f05540&sv=2)

Individual UVs for each parameter enable the mapping in this field to have separate UVs, independent of the overall UVs. can be further stretched, offset, rotated, and can also be repaired using triplanar.

If adjusting the overall UV has no effect, it is probable that the individual UV switch has been turned on in a parameter.

## Stretch

Stretch the texture map along the UV direction, the larger the value, the more the texture repeats per unit area, which looks like a "shrinking" texture effect. The map aspect ratio is locked by default, and can be unlocked to stretch in a certain direction.

## Offset

UV axis direction panning texture mapping.

## Rotate

Rotate the texture map on a plane with controls ranging from 0-360°.

## Keep texture shape

Enable this option to keep the texture shape of the material map from deformation after non-isometric scaling and rotating UVs.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FRdxxctzbUkiYgVi9poQ4%252Fkeep%2520texture.jpg%3Falt%3Dmedia%26token%3D1a70befb-85f7-47da-a121-f5ef2caf22cd&width=768&dpr=3&quality=100&sign=9332e206&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FapQJfQ9VOT31B5hblR6R%252Fkeep%2520texture-2.jpg%3Falt%3Dmedia%26token%3Dde464a28-719a-4e78-a694-24b1ff944f59&width=768&dpr=3&quality=100&sign=71acc5b&sv=2)

## Triplanar

For models with complex morphology and UV clutter, this option can be turned on to quickly obtain a uniform and continuous texture mapping.

> Water, Flowing Water, Displacement, Multimedia, Foliage, and Grass material templates do not support this feature.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FpjmjvLZxBgqqbqF2h9qd%252Ftriplanar.gif%3Falt%3Dmedia%26token%3Dc1aee839-394c-40f3-b12c-a0ce91e6def8&width=768&dpr=3&quality=100&sign=b744858a&sv=2)

## Blend Amount

Let the textured seams created by Triplanar blend together.

## UV Randomizer

Used to rotate and blend edge textures to avoid a repetitive feel to the texture, for use in scenarios with ****natural ground surfaces such as water and grass****.

> Currently, this feature ****is not supported for Transparent, Flowing Water, Displacement, Multimedia, and Foliage material templates****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fz9wDJAEbclk9KTFuPbvQ%252Fuv1.gif%3Falt%3Dmedia%26token%3Db313c144-da43-4064-b40f-f64d1edc63ee&width=768&dpr=3&quality=100&sign=af218023&sv=2)

## Common issue

How can I do it if the texture stretches when rotating the UVs?

Open the Keep texture shape and rotate again.