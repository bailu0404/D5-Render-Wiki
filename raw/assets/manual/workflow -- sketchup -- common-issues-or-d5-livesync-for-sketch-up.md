# Common issues | D5 LiveSync for Sketch up

## Why does the terrain grass not show up when a group/component is imported into D5 after mirrored in SU and given terrain grass?

If you sync the model via D5 direct reading/SU-D5 live sync plugin in the current 2.5 version, and mirror the model after creating the group/component, the mirrored model will not show the terrain grass. This is a known issue in the current version and we will fix it in future versions.

The current recommendation is to explode the mirrored part of the component and then sync it through the plugin or read it directly into D5 to get the correct effect.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fxm4myEmbHBmPBVo2iQjT%252Fsu-grass.png%3Falt%3Dmedia%26token%3D391f05e2-b1ec-4400-b536-a0211247829a&width=768&dpr=3&quality=100&sign=6062a1a9&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FXvL23IOZIiR8zhZt7yup%252Fsu-grass-2.jpg%3Falt%3Dmedia%26token%3Da4f829f7-7ae8-4c90-9e71-63fa224aa491&width=768&dpr=3&quality=100&sign=9eaf5a93&sv=2)

## Why the model is misaligned when using 'replace and link' the model via plugin connection after SU crashed?

This is a known issue with the version 2.7, and we will modify it in subsequent versions.

The current temporary solution:

## How to switch graphics engines in SketchUp 2024?

The new graphics engine function of SketchUp 2024 can be switched in ****Preferences**** window.

> ℹ️ > Note:

Relatively speaking, the new graphics engine is not stable.

If you are prone to crashes of SU2024 during use, it is recommended to Use a classic graphics engine.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FlHoalnwGPYkckquCHC6P%252F44lQLPItk4JW63EAnNBDbNB36wMA1r0yX0hJUHXGwqRfefAA_1918_1078.png%3Falt%3Dmedia%26token%3Dc5a5d86b-34bb-44ab-896e-e57603666e07&width=768&dpr=3&quality=100&sign=e813792e&sv=2)

## Why prompt ‘The following issues have been detected, which may cause data errors’ when connecting?

> Newly added function ****since SU LiveSync 1.3.0.0035****: Popup window on first time connection to indicate abnormal texture information.

If it prompts ↓ image content when syncing for the first time, i.e. ‘Material "Material" - Unsupported texture formats: xxx (currently in .psd format)’.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJQVk76FrPEJo43PomwuP%252F51549ea485a6108c7462840c525beb84.png%3Falt%3Dmedia%26token%3D35c44a4c-754f-4722-b658-0511cbc65c34&width=768&dpr=3&quality=100&sign=7cde540f&sv=2)