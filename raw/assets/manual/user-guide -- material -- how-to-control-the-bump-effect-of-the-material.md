# How to control the bump effect of the material?

Using normal maps can create a bumpy visual effect on the material surface without the need for additional modeling work. Normal maps usually look like this:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FCYP8NDY90XR8VbWNjukB%252Fimage.png%3Falt%3Dmedia%26token%3D607ae421-8941-42cd-ad58-31e06e78cef6&width=768&dpr=3&quality=100&sign=b47b1a0b&sv=2)

Normal map

When using PBR texture mapping resources, the blue-purple images with "Normal" in the filename are normal maps, which need to be linked to the "Normal" map column.

#### Generating Normals

In the D5 renderer, even if the user does not have a normal map, D5 will automatically generate normal information based on the base color map, allowing the material to reflect bumps and dents. As shown in the figure below, the normal field is empty, D5 automatically generates normal information based on the base color map, and you can adjust the strength of the bump effect through the control. (For demonstration purposes, the base color map has been temporarily adjusted to gray.)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FTCMaam4GwqQnkItEgX6B%252F3.gif%3Falt%3Dmedia%26token%3Dc33d016b-daf4-470d-a81c-0102a330467f&width=768&dpr=3&quality=100&sign=4586c2f4&sv=2)

Adjusting the Normal Intensity Control Widget can enhance or weaken the normal bump effect, you can even drag it to the left to input a negative value, reversing the bump effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FmIDpRBvM5qruEnOegAni%252F2.gif%3Falt%3Dmedia%26token%3D8526ee11-921c-4f6b-8ae5-309bb831ff61&width=768&dpr=3&quality=100&sign=49e328e8&sv=2)

## Detailed parameters of normal mapping

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FwnWP9iF0hf1T0FzDLu1L%252Fimage.png%3Falt%3Dmedia%26token%3D66f722a4-2502-42f3-8ef5-9feb53d255a8&width=768&dpr=3&quality=100&sign=97d46910&sv=2)

- Inverted: This flips the direction of the normal bumps.
- Individual UV: This parameter has the same function as the detailed parameters of the base color.
- Triplanar: his parameter is the same as the detailed parameters of the base color map. It should be noted that if the base color has enabled Individual UV and Triplanar, the normal field also needs to enable Individual UV and triplanar mapping, and input the same parameters to match the base color. If you want the normal bumps to align with the base color texture, the correct Triplanar mapping process is: do not enable Individual UV for each channel, use the Triplanar mapping repair in the global UV control of the material.