# What materials are the Transparent templates suitable for? What are the special parameters?

Transparent material templates are suitable for making transparent materials such as glass.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-Mkej2vEOwHn4uu-tC2U%252F-MkejHo4G05FxCgFWtQu%252Ftrans.gif%3Falt%3Dmedia%26token%3Dd3f234b1-fa0b-4121-989e-b38be01b35b7&width=768&dpr=3&quality=100&sign=ca30c0dc&sv=2)

The transparent material template parameters are as follows:

### ****1. Base color/Base Color Map:****

Used to control the color of the stained glass.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-Mkej2vEOwHn4uu-tC2U%252F-Mkej8hSQRDSsBDzmWeX%252Ftrans%2520color.gif%3Falt%3Dmedia%26token%3D194b1061-8aed-46fa-a456-660dd532e87e&width=768&dpr=3&quality=100&sign=92b2fe08&sv=2)

### ****2. Specular:****

Used to control the Reflectance of the material.

### ****3. Refraction:****

Used to control the Index of Refraction (IOR) of the material. The IOR of glass is generally around 1.5-1.6, the IOR of water is 1.33, and the IOR of diamond is 2.4. When the IOR is 1, there is no refractive effect.

> ⚠️ > Due to the refraction effect, the flat glass must ****thickness****.

### ****4. Roughness:****

Defines the roughness of the material surface, which macroscopically affects whether the reflection is blurred or not.

> ⚠️ > Please note that Roughness only affects whether the reflection is blurred or not, not the refraction, so if you want to make frosted glass, you need to use normal noise map. We recommend using the preset frosted glass from the Asset Library, located at Assets>Material>Glass>Frosted Glass

### 5. Opacity:

#### Affected by Light

- Enables direct&indirect lighting for transparent materials with the new 'Affected by Light' option, to achieve effects such as colored gradient glass easily.
- Check 'Affected by Light', keep the Opacity value less than 1, and the material will be illuminated. You can use black-and-white maps to control the opacity pattern.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FoZigozlkTwWyjlpWnZWl%252Fedb8eb43821334eddc5893caa82d312428d07292.gif%3Falt%3Dmedia%26token%3D3b6006c7-c461-4fdf-a107-6baed6857548&width=768&dpr=3&quality=100&sign=88c83141&sv=2)

- The library provides several basic semi-transparent materials, located in the [Glass] category, including Frosted acrylic, Semi-transparent gradient glass, Polycarbonate sheet, as well as Basic semi-transparent materials suitable for a bird's eye view of architectural buildings.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fc9zrSaPouO6EDxEHe6vn%252Fimage.png%3Falt%3Dmedia%26token%3D6c744986-0a21-4b32-97da-1e622ece1ace&width=768&dpr=3&quality=100&sign=4ad880d6&sv=2)

Semi-transparent materials in the library