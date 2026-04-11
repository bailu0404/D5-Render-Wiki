# How to achieve caustics effect

To achieve the caustic effect, the ‘Caustics’ option must be enabled simultaneously for ****both the material and the light source****.

- Among the materials, only the ****"Custom", "Transparent" and "Water" material templates**** currently support caustics.

> The Custom material supports reflective caustics;
>
> the Transparent and Water materials support both reflective and refractive caustics;

- ****Four types of light sources**** ****and**** ****the sun(Geo Sky, and HDRI-Sun)**** support the caustic effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSCZf2m09fpMO9KqZFx9C%252Fimage.png%3Falt%3Dmedia%26token%3D0ec620ac-78ea-4372-ab2f-d132f6be9370&width=768&dpr=3&quality=100&sign=81c6a04d&sv=2)

- ****Caustics Intensity:**** The multiplier value of the Caustics effect, the higher the value, the brighter the caustics.
- ****Softness:**** The degree of Caustics softening which takes effect at the Light Source Radius greater than 0.

> Note:

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F4GZHaSYYDxQVXAn4Y1js%252Flight%2520caustics.PNG%3Falt%3Dmedia%26token%3D58eece30-5d3e-4b31-84c1-20f3e1de64fc&width=768&dpr=3&quality=100&sign=7539e58b&sv=2)

light caustics

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fr8lSujeYvSkfB5Odw8CU%252Fmaterial%2520caustics.PNG%3Falt%3Dmedia%26token%3D75ee1199-1c2a-4190-9a3c-6159a61729d3&width=768&dpr=3&quality=100&sign=ee77aff2&sv=2)

material caustics

## FAQ

### Why do the sunlight caustics flicker?

Sunlight caustics consume huge computation resources. To reduce the consumption, Sunlight Caustics may slightly flicker in preview, but will appear static in rendered images.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FpJXHRAA2vhiVk2VVvuho%252Fcaustics.gif%3Falt%3Dmedia%26token%3Dd80f46ee-5e65-439a-a749-4d4dcca85992&width=768&dpr=3&quality=100&sign=8b2b9c14&sv=2)

Sunlight Caustics slightly flickers in preview, but will appear static in rendered images.