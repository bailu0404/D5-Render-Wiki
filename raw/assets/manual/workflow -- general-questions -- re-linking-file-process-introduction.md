# Re-linking File Process Introduction

If you change the path or name of the model file, you can update the D5 project using the re-linking function, ensuring that previous lighting and material settings are preserved. This process is compatible with ****SU/SketchUp**** and ****3dsMax**** real-time plug-ins.

- Data synchronisation after model renaming/path changes
- Avoid duplicate light overlays
- Preserve historical material parameters
- Inheritance of model attributes

## Workflow

### Method 1: Models linked to .drs before

****Scenario:**** The model has been linked to a D5 project, but the local storage path or name has been altered.

#### ****Operating Steps:****

****Activate Connection****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fvm7XX2it0VNIjK1MUOrw%252Fimage.png%3Falt%3Dmedia%26token%3Db4ee741c-4217-408a-9b9f-a06439be4bd2&width=768&dpr=3&quality=100&sign=e8b67e78&sv=2)

Step 1

****Select the model to replace****

Tick the target model to be replaced in the popup window. (D5 materials will be inherited after replacement)

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FKppIuZ9xROhwnjY6yaau%252Fimage.png%3Falt%3Dmedia%26token%3Dac7a39a7-c468-4ac7-add6-3bba330b112a&width=768&dpr=3&quality=100&sign=df98150b&sv=2)

Step 2

Click ‘Replace and link’ to complete the synchronisation.

### Method 2: Open .drs and the modeling file together

****Scenario:**** need to update both the model file and the associated project at the same time

#### ****Workflow:****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FVIZkhoZAOLTGSDD8SL8B%252Fimage.png%3Falt%3Dmedia%26token%3Df6188570-3ed2-4197-9c01-e7ddf81c27a2&width=768&dpr=3&quality=100&sign=8d2441d7&sv=2)

Step 1

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FbBi45l93E4cYqSjghAK8%252Fimage.png%3Falt%3Dmedia%26token%3D1aacf0af-ead7-4067-97a6-d44ee73b5a07&width=768&dpr=3&quality=100&sign=4369898d&sv=2)

Step 2

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6cimOdjlINH8zG824AZA%252Fimage.png%3Falt%3Dmedia%26token%3D27b08b5a-e70c-4a91-b3e1-f974e07e8f91&width=768&dpr=3&quality=100&sign=d9119a09&sv=2)

Replace and link logic

### Option Description:

- Tick ‘’Light‘’: Replace the light group with the same ID (historical parameters are preserved)
- Tick ‘Material’: Replace materials with same names (historical parameters are preserved).

> ⚠️ > ****Note:****

- ‘’Light‘’ replacement only supports SU/3dsMax LiveSync plug-ins.
- No light/material ticking options for non-real-time plug-ins and direct imported models.

## FAQs

### Q1: Why does the DCC prompts "Please retry after exit rendering mode or finish the rendering within D5 Render"?

A：

The general situation is: after entering the picture/video mode in D5, and then performing the increase or decrease model operation in DCC and transmitting new data (real-time update or manual update) to D5, this error will occur.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F760rca4sE0h9baqtQ3rW%252Fimage.png%3Falt%3Dmedia%26token%3D987450c8-21fa-4bca-9389-0c5821f8a409&width=768&dpr=3&quality=100&sign=9fbba6b9&sv=2)

In this case, exit the picture/video mode, and then re-associate the synchronization.