# How to create a lawn effect?

## By scattering

Select the desired model grass in the library, then pull the parameters of the brush up to the maximum to activate the Scatter tool to scatter it within the selected faces.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FVWPfeVeesS8MC0rTlC72%252Flawn%25201.jpg%3Falt%3Dmedia%26token%3D62e8cdfe-45ef-418a-a33c-f735c9ca5a70&width=768&dpr=3&quality=100&sign=3a3c17d6&sv=2)

## By grass material template

Learn more: <https://docs.d5render.com/user-guide/material/grass>

Select the material where the grass is located and switch the material template of that material to grass. Model grass will be generated on the surface of the material. Select the material where the grass is located and switch the material template of that material to grass. Model grass will be generated on the surface of the material. You can adjust the height, density and trim parameters of the grass, as well as the roughness, specular and normal of the surface through the material parameters.

Depending on the area of the material, there may be a delay in generation.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FAoSLRrSaNrqPBq8to0Ns%252Flawn%25202.jpg%3Falt%3Dmedia%26token%3Db9500f0b-e390-42f0-8306-923900e10c14&width=768&dpr=3&quality=100&sign=1d481b0a&sv=2)

Both of the above methods will introduce large amounts of model surfaces, and are not recommended for large areas. Grass in the distant view is recommended to use the grass material template which takes up less resources. The grass in the close-up view that needs to be close-up can use the model grass.

## Common issues

### Why can't I scatter grass/generate grass on the model?

Please check the model face before scattering/using grass material template. The scattering tool and the grass material template generation are only available for the front side of the model.

In Sketch Up

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F3GJXvOCUl2DbS4cp2wWl%252Fimage.png%3Falt%3Dmedia%26token%3Dde0cae35-eea8-4a42-8932-ffe35866bfaa&width=768&dpr=3&quality=100&sign=5905d554&sv=2)

In D5

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FZzBgWGKsCXmicEqnhuj6%252Fimage.png%3Falt%3Dmedia%26token%3Dbc9643bf-79e5-4f95-b153-1f1f30e93796&width=768&dpr=3&quality=100&sign=26edc946&sv=2)