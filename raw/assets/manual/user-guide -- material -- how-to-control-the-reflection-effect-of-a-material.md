# How to control the reflection effect of a material?

## Specular

The Specular is specifically used to describe ****the refraction of the non-metallic materials.****

- ****Metallic=1****: specular parameters have no effect on the material
- ****Metallic=0****: specular parameters affect the refraction of the material

Due to the Fresnel phenomenon, the refraction of light striking a material vertically is the weakest and is called Fresnel Reflectance at 0 Degrees (F0). Due to the reversibility of the light path, you can also interpret it as the camera or the observer looks at the surface of the material vertically, they will see the weakest reflection effect.

- When ****Specular=0****, the F0 intensity of the material is also 0%, the material has no specular reflection phenomenon, only diffuse reflection phenomenon.
- When ****Specular=1****, the F0 intensity of the material is 8%, which is the highest refraction of non-metallic materials.

> Generally, gemstones, jade and other materials will reach this value.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fplrbv2BreMnBxQ0mb8u2%252F%25E9%25AB%2598%25E5%2585%2589%25E5%258F%2582%25E6%2595%25B0.gif%3Falt%3Dmedia%26token%3D2efae4ee-5745-4553-b49a-52ec1088b675&width=768&dpr=3&quality=100&sign=7f6d72b3&sv=2)

The Specular value of 0-1 linearly corresponds to the F0 reflectance of non-linear materials from 0% to 8%.

> For example, a highlight value of 0.5 represents a 4% reflectance when facing directly towards the material.

Most non-metallic materials have an F0 between 2% and 5%, which translates into a specular value of 0.25~0.625. In other words, when making non-metallic materials, the minimum specular parameter should not be lower than 0.25. The specular parameter for water materials is 0.25, and most non-metallic materials (glass, plastic, etc.) have a specular value of about 0.5. The specular factor for gemstones and jade can be set to 1.0.

In the process of using, in order to achieve a better reflection effect, some users will adjust the metallic parameter, but in fact, this is wrong. If a non-metallic material, set the metallic parameter, such as marble/wall, etc., it will make the material look very reflective and the material in the screen will look too greasy.

## Roughness

The roughness parameter describes the microscopic roughness of the material surface, which affects whether the reflection effect is blurred or not.

- ****The lower the roughness****, the flatter the surface of the material, the closer the reflected light path will be to the ideal specular reflection, and the clearer the image reflected from the surface of the material will be.
- ****Roughness increases****, representing the material surface gradually becomes rugged, the reflected light path in a certain range of irregular jitter, the macroscopic reflection will become blurred.

"Roughness" and "glossiness" are antonyms, and theoretically, if you do the inverse color processing to "glossiness map", you will get "roughness map".

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FfVlzLmj8V4DPngv1k5q9%252F%25E7%25B2%2597%25E7%25B3%2599%25E5%25BA%25A6.gif%3Falt%3Dmedia%26token%3D7921b3ef-b449-4575-911b-c24db7c92961&width=768&dpr=3&quality=100&sign=4addc45d&sv=2)