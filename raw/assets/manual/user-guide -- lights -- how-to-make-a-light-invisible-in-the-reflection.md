# How to make a light invisible in the reflection?

Use the ****''Visible in Reflection''**** parameter to control the visibility of lights in the reflection.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FAsspbLkJc9SuMnYriMoL%252Flight%2520%281%29.gif%3Falt%3Dmedia%26token%3D4bbe8dce-8ce3-4d4f-aad0-2fd583f8f51c&width=768&dpr=3&quality=100&sign=87c87be3&sv=2)

Reflections from lights usually appear on materials with high "Specular" and "Metallic", and the ****"Intensity"**** parameter can be used to adjust the influence of the light on reflections.

By default ''Visible in Reflection'' is turned on and is 1. When it is turned off, i.e. the parameter is set to 0, the light will be completely invisible in the reflection.

> ℹ️ #### Know issue

> Currently, it is not possible to switch off reflections using "Visible in Reflection" for lights reflected in glass.