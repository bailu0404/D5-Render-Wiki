# Common issues | D5 Sync for C4D

## 1. Why do materials synced to D5 appear differently than in C4D?

****Reason:**** The current plugin version does not support syncing [Material UV] parameters. It currently only supports [UVW Map] projection types; we will implement this functionality in future releases.
****Temporary workaround:****
Set the material ball's projection type to [UVW Map] and retain all UV parameters at their default values;
If you need to use a specific texture, please re-adjust the UVs within [UVEdit] before syncing it to D5 via the plugin.

## 2. Why did the base colour values set in C4D deviate after syncing to D5?

In ****Scene > Colour Management****, if the render space is set to ****anything other than ‘Traditional (sRGB linear workflow)’****, operations involving ****colour values**** within the C4D file may exhibit ****inconsistency in values**** after syncing to D5 Render.

> e.g.: When the render space is set to ****ACEScg****, the base color values defined in C4D cannot ****maintain a 1:1 correspondence**** with the base color values in the renderer, potentially causing colour difference.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FWrbo0gGxQixB1n2LGaOz%252Fen-c4d.gif%3Falt%3Dmedia%26token%3Dbaf336d9-00f5-4283-8a33-ce88fdad0ed6&width=768&dpr=3&quality=100&sign=196b0e90&sv=2)

Notes:

● ****C4D 2025 and earlier versions**** use ****sRGB**** as the default render space

● ****C4D 2026**** uses ****ACEScg**** as the default render space, making it more likely to encounter the differences mentioned above