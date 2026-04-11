# How to adjust the material map?

● Map Formats: Currently supported formats: .png / .jpg / .bmp / .tif / .tiff / .tga

● Map Location: In the map editor, right-clicking on the map slot and clicking "File Location" will directly open the file directory where the map is located, making it easy to find and edit the map.

## Base Color/Base Color Map

Base Color controls the color properties of the material itself.

- When the material is metallic (Metallic=1), it is the reflection color of the metal.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FifVqwFZOrYgOayBJU0QN%252Fbase%2520color%25E9%2587%2591%25E5%25B1%259E%25E5%25BA%25A6.gif%3Falt%3Dmedia%26token%3D668c51f4-3382-433d-9ce2-d85056f8539a&width=768&dpr=3&quality=100&sign=5be2de6b&sv=2)

Metallic=1

- When the material is non-metallic (Metallic=0), it is the diffuse color of the non-metallic material.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fi3vyrPpEwq3EhzLwD3tN%252F%25E9%2587%2591%25E5%25B1%259E%25E5%25BA%25A6%25E4%25B8%25BA0.gif%3Falt%3Dmedia%26token%3Ddbac2ab6-1a85-49a2-ae24-ffd7f2fabec5&width=768&dpr=3&quality=100&sign=ae662a91&sv=2)

Metallic=0

The base color palette can only define a single color for the material. If you want more complex variations, you need to use maps to control the color of the material. Click on the "Base Color Map" tab, and then click on the map slot to read the map file.

> ℹ️ > If using PBR texture mapping resources, ****images with keywords such as "Color," "Base Color," "Albedo," and "Diffuse" in the file name**** are all considered as the base color of the material, and are generally linked to the "****Base Color Map****" slot.

In D5 Render, when there is a map in the "Base Color Map" slot, the color in the "Base Color" palette will be superimposed with the map color, resulting in a coloring effect. The blend mode is "Multiply."

> If you need to ****use the original color of the "Base Color Map"****, make sure that ****the "Base Color" palette is pure white****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7oByesvAcSJ1dgKRpJjV%252F%25E5%259F%25BA%25E7%25A1%2580%25E8%2589%25B2%25E8%25B4%25B4%25E5%259B%25BE%25E6%25B7%25B7%25E8%2589%25B2.gif%3Falt%3Dmedia%26token%3D8ff7b06e-df82-42bf-959d-598da1a14539&width=768&dpr=3&quality=100&sign=789fcc2a&sv=2)

## Map Editing

Clicking on the "Detailed Parameters" button on the right side of the "Base Color Map" will expand the base color map editing panel.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7APCVyEJs20NGXdGZtth%252Fimage.png%3Falt%3Dmedia%26token%3Ded8b4890-80f5-4659-a92f-af18e2a32009&width=768&dpr=3&quality=100&sign=648959e5&sv=2)

Base Color Map

## Color Space Transfer Function

color space of the map. There are two options available: "Linear" and "sRGB".

In the PBR workflow, the base color map, the back map of the leaf template, and the AO channel should be imported in sRGB mode. Other maps can be set with no data processing.

Currently, correct presets have been made for new imported maps by default. For existing old projects, to ensure that the effect remains unchanged, all channels are set to sRGB mode.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FU5Z7o9fF7s9nw4SIZAuE%252Fimage.png%3Falt%3Dmedia%26token%3D91c66f88-b51e-40f4-8884-be5d5a7fa3c6&width=768&dpr=3&quality=100&sign=f7fce8b6&sv=2)

## ****Inverted****

"Inverted" refers to the inverse color of the map, where the hue becomes the complementary color, and the brightness and darkness are reversed.

## ****Contrast****

Increasing or decreasing the contrast of an image. Decreasing the contrast will make the image tend towards gray.

## ****Hue****

Translating the hue parameter of a map on the hue circle. The control range is -180° to +180°, covering the entire hue circle.

## ****Saturation****

Adjusting the saturation of the base color map. If the control is pulled to the minimum, the map will become "black and white." If the control is pulled to the maximum, the map will be very "vibrant."

## ****Brightness****

Adjusting the brightness of the base color map. If the control is pulled to the minimum, the map will become black. If the control is pulled to the maximum, the map will become white.

## ****Individual UV****

After enabling this option, the map in this field has an independent UV, which can be further stretched, offset, and rotated, and Triplanar UV can also be used. This feature is useful when you want to adjust a specific map channel separately. For example, when you want to translate the base color map without changing the normal position.

## FAQ

#### Why is the "File Location" option disabled?

In the current version, the "File Location" function only works for locally imported maps and does not support opening models/materials in the asset library or materials that are synced from modeling software to D5.