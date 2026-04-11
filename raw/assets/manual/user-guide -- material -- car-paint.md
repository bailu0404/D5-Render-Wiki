# What materials are the Car Paint templates suitable for? What are the special parameters?

The basic principle of the Car Paint material is to add a new layer of reflection calculation on top of the standard custom material template to simulate the effect of a clear coat layer. In short, this material has two reflection layers, and the roughness can be defined separately.

> After switching to the Car Paint template, most of the parameters are exactly the same as the Custom template. Please refer to the Custom template for the definition of the Base color, Normal, Specular, Metallic, AO, etc.
>
> - These parameters can be considered as controlling the Base Paint.

The following two parameters control the properties of the Clear Coat layer:

- ****Clear Coat:**** Controls the Reflectance of the Clear Coat layer. A value of 0 means no Clear Coat. A value of 1 maximizes the Reflectance of the Clear Coat.
- ****Clear Coat Roughness:**** Defines the Roughness of the Clear Coat layer, which affects whether the reflection of the clear coat is blurred or not.

> ℹ️ > For common Car Paints, the Roughness of the base paint is generally higher, and the Roughness of the Clear Coat layer is close to 0.

In the following figure, keeping the value of Clear Coat layer 0.85 and the Clear Coat Roughness 0, adjusting the Roughness of base paint, you can see the effect of two reflections in the highlight area.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-MkelEk65kb_zAuMJjNc%252F-MkemMz680J1jGkuSrhd%252Fcar.gif%3Falt%3Dmedia%26token%3D40b8783d-8418-48c9-9386-69ad27072e2a&width=768&dpr=3&quality=100&sign=ba608ce2&sv=2)